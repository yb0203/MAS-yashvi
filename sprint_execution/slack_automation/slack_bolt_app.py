#!/usr/bin/env python3
"""
MAS AI Labs — Interactive Slack Standup & Living Sprint Sync Bot
Author: MAS AI PM
Features:
  1. Personalized 7:00 PM DMs with consolidated single-screen update modal (< 45s).
  2. Real-time 2-way sync into SPRINT_0X_WEEK_0X.md & MONTH_01_MASTER_PLAN.md.
  3. 7:45 PM Pre-Standup Digest in #all-mas-ai-labs with direct Google Meet link.
  4. Google Meet Gemini Notes Ingestion via `/standup-notes` (Day Highlights auto-sync).
  5. Weekend Living Sprint Rollover via `/sprint-rollover`.
"""

import os
import sys
import ssl
import json
import logging
import certifi
from datetime import datetime
from typing import Dict, Any, List
from dotenv import load_dotenv

# Load environment variables from .env file
ENV_PATH = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(ENV_PATH)

# SSL context for macOS certificate verification
ssl_context = ssl.create_default_context(cafile=certifi.where())

# Slack Bolt & SDK
try:
    from slack_bolt import App
    from slack_bolt.adapter.socket_mode import SocketModeHandler
    from slack_sdk import WebClient
except ImportError:
    App = None
    SocketModeHandler = None
    WebClient = None

from sprint_sync_engine import (
    get_sprint_file_for_day,
    parse_sprint_tasks,
    update_sprint_task,
    append_daily_log_entry,
    sync_active_blockers_to_master,
    rollover_incomplete_tasks
)
from block_kit_views import (
    build_personal_dm_view,
    build_consolidated_update_modal,
    build_pre_standup_digest_card,
    build_post_standup_gemini_card,
    map_status_to_rag
)
from gemini_notes_parser import process_and_sync_gemini_notes
from dm_scheduler import start_standup_scheduler, get_current_september_day

# Load Environment Variables
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "xoxb-dummy-token")
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN", "xapp-dummy-token")
MAIN_STANDUP_CHANNEL = os.environ.get("SLACK_STANDUP_CHANNEL", "#all-mas-ai-labs")
GOOGLE_MEET_URL = os.environ.get("GOOGLE_MEET_URL", "https://meet.google.com")

TEAM_SLACK_IDS = {
    "Gaurav": os.environ.get("SLACK_ID_GAURAV", "U_GAURAV"),
    "Shubham": os.environ.get("SLACK_ID_SHUBHAM", "U_SHUBHAM"),
    "Rohan": os.environ.get("SLACK_ID_ROHAN", "U_ROHAN"),
    "Prakhar": os.environ.get("SLACK_ID_PRAKHAR", "U_PRAKHAR"),
    "Yashvi": os.environ.get("SLACK_ID_YASHVI", "U_YASHVI"),
    "QA / Tester": os.environ.get("SLACK_ID_QA", "U_QA"),
    "PM Intern": os.environ.get("SLACK_ID_INTERN", "U_INTERN"),
}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MAS_StandupBot")

if App and WebClient:
    slack_client = WebClient(token=SLACK_BOT_TOKEN, ssl=ssl_context)
    app = App(client=slack_client)
else:
    app = None

# ==============================================================================
# Bolt Event Handlers & Interactivity
# ==============================================================================

if app:
    @app.action("open_consolidated_modal_action")
    def handle_open_consolidated_modal(ack, body, client):
        ack()
        payload = json.loads(body["actions"][0]["value"])
        owner_name = payload["owner"]
        sprint_num = payload["sprint"]
        day = payload["day"]

        sprint_file, _ = get_sprint_file_for_day(day)
        all_tasks = parse_sprint_tasks(sprint_file)
        owner_tasks = [t for t in all_tasks if t["owner"] == owner_name]

        modal = build_consolidated_update_modal(owner_name, owner_tasks, sprint_num, day)
        client.views_open(trigger_id=body["trigger_id"], view=modal)

    @app.view("submit_consolidated_standup_callback")
    def handle_consolidated_modal_submit(ack, body, view, client):
        ack()
        meta = json.loads(view["private_metadata"])
        sprint_num = meta["sprint"]
        day = meta["day"]
        task_ids = meta["task_ids"]

        values = view["state"]["values"]
        outcome = values.get("deliverable_link_block", {}).get("deliverable_link_input", {}).get("value") or "-"
        blocker = values.get("blocker_notes_block", {}).get("blocker_notes_input", {}).get("value") or "None"

        sprint_file, _ = get_sprint_file_for_day(day)

        for t_id in task_ids:
            status_val = values.get(f"status_{t_id}", {}).get(f"select_status_{t_id}", {}).get("selected_option", {}).get("value", "[-] In Progress")
            rag_val = map_status_to_rag(status_val, has_blocker=(blocker.lower() != "none" and blocker != "-"))
            update_sprint_task(sprint_file, t_id, status_val, outcome, blocker, rag_val)

        tasks = parse_sprint_tasks(sprint_file)
        sync_active_blockers_to_master(tasks, sprint_num)
        logger.info(f"✅ Successfully updated {len(task_ids)} tasks in {os.path.basename(sprint_file)}")

    @app.command("/standup")
    def handle_standup_command(ack, body, client):
        ack()
        user_id = body["user_id"]
        day = get_current_september_day()
        sprint_file, sprint_num = get_sprint_file_for_day(day)
        all_tasks = parse_sprint_tasks(sprint_file)

        # Match user ID or prompt
        matched_owner = None
        for name, u_id in TEAM_SLACK_IDS.items():
            if u_id == user_id:
                matched_owner = name
                break

        if matched_owner:
            owner_tasks = [t for t in all_tasks if t["owner"] == matched_owner]
            modal = build_consolidated_update_modal(matched_owner, owner_tasks, sprint_num, day)
            client.views_open(trigger_id=body["trigger_id"], view=modal)
        else:
            client.chat_postEphemeral(
                channel=body["channel_id"],
                user=user_id,
                text="⚡ Standup trigger received! You can also check your DM for daily updates."
            )

    @app.command("/standup-notes")
    def handle_standup_notes_command(ack, body, client):
        ack()
        raw_text = body.get("text", "").strip()
        day = get_current_september_day()
        sprint_file, sprint_num = get_sprint_file_for_day(day)

        if not raw_text:
            client.chat_postEphemeral(
                channel=body["channel_id"],
                user=body["user_id"],
                text="Usage: `/standup-notes <paste Google Meet Gemini summary or key decisions>`"
            )
            return

        # Ingest, parse and sync notes into Sprint doc
        highlight_text = process_and_sync_gemini_notes(day, raw_text)
        card = build_post_standup_gemini_card(day, sprint_num, highlight_text)

        client.chat_postMessage(
            channel=MAIN_STANDUP_CHANNEL,
            text=f"📝 Post-Standup Highlights (Day {day})",
            blocks=card["blocks"]
        )

    @app.command("/sprint-rollover")
    def handle_sprint_rollover(ack, body, client):
        ack()
        text = body.get("text", "").strip()
        args = text.split()
        if len(args) == 2 and args[0].isdigit() and args[1].isdigit():
            from_s = int(args[0])
            to_s = int(args[1])
            rolled = rollover_incomplete_tasks(from_s, to_s)
            client.chat_postMessage(
                channel=MAIN_STANDUP_CHANNEL,
                text=f"🔄 *Weekend Sprint Rollover Completed!* Moved {len(rolled)} incomplete tasks from Sprint {from_s} to Sprint {to_s} as `[Rollover]`. (Tasks: {', '.join(rolled) if rolled else 'None'})"
            )
        else:
            client.chat_postEphemeral(
                channel=body["channel_id"],
                user=body["user_id"],
                text="Usage: `/sprint-rollover <from_sprint> <to_sprint>` (e.g. `/sprint-rollover 1 2`)"
            )

# ==============================================================================
# CLI Testing & Execution
# ==============================================================================

def main():
    import argparse
    parser = argparse.ArgumentParser(description="MAS AI Labs Slack Standup Bot")
    parser.add_argument("--day", type=int, default=1, help="Day in September 2026 (1 to 30)")
    parser.add_argument("--mode", choices=["dry-run", "socket-mode", "test-gemini-notes", "test-dm", "test-channel"], default="dry-run")
    parser.add_argument("--notes", type=str, default="Decisions: Resolved P0 bug on staging. Action items: Yashvi to finalize Orane scope.", help="Sample Gemini notes for test")

    args = parser.parse_args()
    sprint_file, sprint_num = get_sprint_file_for_day(args.day)
    tasks = parse_sprint_tasks(sprint_file)

    if args.mode == "dry-run":
        print(f"\n================ [PERSONAL DM VIEW (Sprint {sprint_num} | Day {args.day})] ================\n")
        owners = {}
        for t in tasks:
            owners.setdefault(t["owner"], []).append(t)
        for owner, o_tasks in owners.items():
            print(f"--- DM to {owner} ---")
            print(json.dumps(build_personal_dm_view(owner, o_tasks, args.day, sprint_num), indent=2))

        print(f"\n================ [7:45 PM PRE-STANDUP DIGEST CARD] ================\n")
        print(json.dumps(build_pre_standup_digest_card(args.day, sprint_num, tasks, GOOGLE_MEET_URL), indent=2))

    elif args.mode == "test-dm":
        if not app:
            print("Error: Slack app not initialized.")
            sys.exit(1)
        target_user = TEAM_SLACK_IDS.get("Yashvi")
        yashvi_tasks = [t for t in tasks if t["owner"] == "Yashvi"]
        dm_blocks = build_personal_dm_view("Yashvi", yashvi_tasks, args.day, sprint_num)
        print(f"🚀 Sending live test DM to Yashvi ({target_user})...")
        resp = app.client.chat_postMessage(
            channel=target_user,
            text=f"Daily Quick Standup Update (Day {args.day})",
            blocks=dm_blocks
        )
        print(f"✅ Test DM dispatched successfully! Slack ts: {resp.get('ts')}")

    elif args.mode == "test-channel":
        if not app:
            print("Error: Slack app not initialized.")
            sys.exit(1)
        print(f"🚀 Sending live pre-standup digest to {MAIN_STANDUP_CHANNEL}...")
        card = build_pre_standup_digest_card(args.day, sprint_num, tasks, GOOGLE_MEET_URL)
        resp = app.client.chat_postMessage(
            channel=MAIN_STANDUP_CHANNEL,
            text=f"Daily Standup Digest (Sprint {sprint_num} | Day {args.day})",
            blocks=card["blocks"]
        )
        print(f"✅ Test Channel Digest dispatched successfully! Slack ts: {resp.get('ts')}")

    elif args.mode == "test-gemini-notes":
        highlight = process_and_sync_gemini_notes(args.day, args.notes)
        print(f"✅ Gemini Notes Processed & Synced for Day {args.day}:")
        print(highlight)

    elif args.mode == "socket-mode":
        if not SocketModeHandler or not app:
            print("Error: slack_bolt not installed or app tokens missing. Run: pip install slack_bolt")
            sys.exit(1)
        # Start background timer scheduler
        start_standup_scheduler(app.client, TEAM_SLACK_IDS, MAIN_STANDUP_CHANNEL, GOOGLE_MEET_URL)
        handler = SocketModeHandler(app, SLACK_APP_TOKEN)
        print("⚡ MAS Standup Bot is LIVE in Socket Mode...")
        handler.start()

if __name__ == "__main__":
    main()
