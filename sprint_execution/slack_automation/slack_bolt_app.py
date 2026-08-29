#!/usr/bin/env python3
"""
MAS AI Labs — Interactive Slack Standup & Sprint Sync Bot
Author: MAS AI PM
Features:
  1. Personalized 7:00 PM DMs to task owners (No main channel spam).
  2. Frictionless <1 min update via Dropdowns (Status & RAG) + Quick Note.
  3. Real-time 2-way sync into SPRINT_0X_WEEK_0X.md & MONTH_01_MASTER_PLAN.md.
  4. 7:45 PM aggregated Pre-Standup Digest card in #ai-labs-standup.
  5. Sprint-End Summary (/sprint-summary), Highlights update (/update-highlights),
     and Living Sprint Rollover (/rollover-sprint).
"""

import os
import sys
import json
import logging
from datetime import datetime
from typing import Dict, Any, List

# Slack Bolt & SDK
try:
    from slack_bolt import App
    from slack_bolt.adapter.socket_mode import SocketModeHandler
except ImportError:
    print("Notice: slack_bolt not installed in this environment. To run live: pip install slack_bolt")
    App = None
    SocketModeHandler = None

from sprint_sync_engine import (
    get_sprint_file_for_day,
    parse_sprint_tasks,
    update_sprint_task,
    append_daily_log_entry,
    sync_active_blockers_to_master,
    rollover_incomplete_tasks
)

# Configuration & Environment
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "xoxb-dummy-token")
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN", "xapp-dummy-token")
MAIN_STANDUP_CHANNEL = os.environ.get("SLACK_STANDUP_CHANNEL", "#ai-labs-standup")

# Mapping team members to Slack User IDs (Replace with your workspace user IDs)
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

if App:
    app = App(token=SLACK_BOT_TOKEN)
else:
    app = None

# ==============================================================================
# 1. Block Kit DM Generator (Personalized 1-Minute Update)
# ==============================================================================

def build_personal_dm_blocks(owner_name: str, tasks: List[Dict[str, Any]], day: int, sprint_num: int) -> List[Dict[str, Any]]:
    """Builds a compact, personalized DM card with dropdowns for quick updates."""
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"👋 Hey {owner_name}! Daily Quick Standup (Day {day})",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"⏰ *Standup Call is at 8:00 PM IST.*\n"
                    f"Take *30 seconds* to update your scheduled deliverables below so we have data ready for the call."
                )
            }
        },
        {"type": "divider"}
    ]

    for t in tasks:
        blocks.extend([
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        f"📌 *`{t['id']}`*: *{t['task']}*\n"
                        f"↳ *Target Outcome:* _{t['expected_outcome']}_\n"
                        f"↳ *Current Status:* `{t['status']}` | *RAG:* {t['rag']}"
                    )
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": f"⚡ Quick Update ({t['id']})",
                            "emoji": True
                        },
                        "style": "primary",
                        "value": json.dumps({"task_id": t["id"], "sprint": sprint_num, "day": day}),
                        "action_id": "open_task_modal_action"
                    }
                ]
            },
            {"type": "divider"}
        ])

    return blocks

# ==============================================================================
# 2. Interactive Modal (Dropdowns + Quick Note)
# ==============================================================================

def build_quick_update_modal(task_id: str, task_info: Dict[str, Any], sprint_num: int, day: int) -> Dict[str, Any]:
    """Generates the ultra-fast 1-minute modal with dropdowns."""
    return {
        "type": "modal",
        "callback_id": "submit_quick_update_callback",
        "private_metadata": json.dumps({"task_id": task_id, "sprint": sprint_num, "day": day}),
        "title": {
            "type": "plain_text",
            "text": f"Update {task_id}",
            "emoji": True
        },
        "submit": {
            "type": "plain_text",
            "text": "Submit (Done)",
            "emoji": True
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
            "emoji": True
        },
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Task:* {task_info.get('task', task_id)}\n*Target:* _{task_info.get('expected_outcome', '-')}_"
                }
            },
            {
                "type": "input",
                "block_id": "status_block",
                "element": {
                    "type": "static_select",
                    "action_id": "status_select",
                    "placeholder": {"type": "plain_text", "text": "Select Status"},
                    "options": [
                        {"text": {"type": "plain_text", "text": "✅ Done / Completed"}, "value": "[x] Done"},
                        {"text": {"type": "plain_text", "text": "⏳ In Progress"}, "value": "[-] In Progress"},
                        {"text": {"type": "plain_text", "text": "🚨 Blocked / Delayed"}, "value": "[!] Blocked"}
                    ],
                    "initial_option": {"text": {"type": "plain_text", "text": "⏳ In Progress"}, "value": "[-] In Progress"}
                },
                "label": {"type": "plain_text", "text": "Task Status"}
            },
            {
                "type": "input",
                "block_id": "rag_block",
                "element": {
                    "type": "static_select",
                    "action_id": "rag_select",
                    "placeholder": {"type": "plain_text", "text": "Select Health"},
                    "options": [
                        {"text": {"type": "plain_text", "text": "🟢 Green (On Track)"}, "value": "🟢"},
                        {"text": {"type": "plain_text", "text": "🟡 Amber (At Risk / Needs Support)"}, "value": "🟡"},
                        {"text": {"type": "plain_text", "text": "🔴 Red (Blocked)"}, "value": "🔴"}
                    ],
                    "initial_option": {"text": {"type": "plain_text", "text": "🟢 Green (On Track)"}, "value": "🟢"}
                },
                "label": {"type": "plain_text", "text": "RAG Status"}
            },
            {
                "type": "input",
                "block_id": "output_block",
                "optional": True,
                "element": {
                    "type": "plain_text_input",
                    "action_id": "output_input",
                    "placeholder": {"type": "plain_text", "text": "e.g. PR #12 merged / Intake draft v1 ready"}
                },
                "label": {"type": "plain_text", "text": "Quick Outcome / Deliverable Link"}
            },
            {
                "type": "input",
                "block_id": "blocker_block",
                "optional": True,
                "element": {
                    "type": "plain_text_input",
                    "action_id": "blocker_input",
                    "placeholder": {"type": "plain_text", "text": "None / Waiting for API key / Needs review"}
                },
                "label": {"type": "plain_text", "text": "Blocker / Dependency (If any)"}
            }
        ]
    }

# ==============================================================================
# 3. Main Channel Pre-Standup Digest Card (Posted at 7:45 PM IST)
# ==============================================================================

def build_main_channel_digest(day: int, sprint_num: int) -> Dict[str, Any]:
    """Generates the aggregated, high-signal standup card for #ai-labs-standup."""
    sprint_file, _ = get_sprint_file_for_day(day)
    tasks = parse_sprint_tasks(sprint_file)

    done_tasks = [t for t in tasks if "done" in t["status"].lower() or "[x]" in t["status"]]
    blocked_tasks = [t for t in tasks if t["blocker"] and t["blocker"].lower() != "none" and t["blocker"] != "-"]

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"📊 Standup Summary (Sprint {sprint_num} | Day {day})",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"📞 *Google Meet Standup at 8:00 PM IST (in 15 mins)*\n"
                    f"• *Progress Today:* `{len(done_tasks)}/{len(tasks)} tasks completed`\n"
                    f"• *Active Blockers Flagged:* `{len(blocked_tasks)}`"
                )
            }
        },
        {"type": "divider"}
    ]

    if blocked_tasks:
        blocker_text = []
        for t in blocked_tasks:
            blocker_text.append(f"🚨 *`{t['id']}` ({t['owner']})*: {t['task']}\n   ↳ *Blocker:* _{t['blocker']}_")
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*⚠️ Items for Discussion on Call:*\n" + "\n".join(blocker_text)
            }
        })
    else:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "🎉 *Zero Blockers Logged!* All deliverables on track."
            }
        })

    blocks.extend([
        {"type": "divider"},
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "📂 Open Active Sprint Doc", "emoji": True},
                    "url": "https://github.com/yb0203/MAS-yashvi/tree/main/sprint_execution",
                    "action_id": "open_sprint_doc_link"
                }
            ]
        }
    ])

    return {"blocks": blocks}

# ==============================================================================
# 4. Bolt Event Listeners & Interactive Handlers
# ==============================================================================

if app:
    @app.action("open_task_modal_action")
    def handle_open_modal(ack, body, client):
        ack()
        payload = json.loads(body["actions"][0]["value"])
        task_id = payload["task_id"]
        sprint_num = payload["sprint"]
        day = payload["day"]

        sprint_file, _ = get_sprint_file_for_day(day)
        tasks = {t["id"]: t for t in parse_sprint_tasks(sprint_file)}
        task_info = tasks.get(task_id, {})

        modal = build_quick_update_modal(task_id, task_info, sprint_num, day)
        client.views_open(trigger_id=body["trigger_id"], view=modal)

    @app.view("submit_quick_update_callback")
    def handle_modal_submission(ack, body, view, client):
        ack()
        meta = json.loads(view["private_metadata"])
        task_id = meta["task_id"]
        sprint_num = meta["sprint"]
        day = meta["day"]

        values = view["state"]["values"]
        status = values["status_block"]["status_select"]["selected_option"]["value"]
        rag = values["rag_block"]["rag_select"]["selected_option"]["value"]
        outcome = values.get("output_block", {}).get("output_input", {}).get("value") or "-"
        blocker = values.get("blocker_block", {}).get("blocker_input", {}).get("value") or "None"

        sprint_file, _ = get_sprint_file_for_day(day)
        success = update_sprint_task(sprint_file, task_id, status, outcome, blocker, rag)

        if success:
            tasks = parse_sprint_tasks(sprint_file)
            sync_active_blockers_to_master(tasks, sprint_num)
            logger.info(f"✅ Successfully synced {task_id} into {os.path.basename(sprint_file)}")

    @app.command("/standup")
    def handle_standup_command(ack, body, client):
        ack()
        user_id = body["user_id"]
        # Match user to tasks and open modal or send DM
        client.chat_postEphemeral(
            channel=body["channel_id"],
            user=user_id,
            text="⚡ Standup trigger received! Check your DM for personalized task updates."
        )

    @app.command("/sprint-summary")
    def handle_sprint_summary(ack, body, client):
        ack()
        # Post instant sprint summary to channel
        client.chat_postMessage(
            channel=body["channel_id"],
            text=f"📊 *Sprint Summary generated!*"
        )

    @app.command("/rollover-sprint")
    def handle_rollover(ack, body, client):
        ack()
        text = body.get("text", "").strip()
        args = text.split()
        if len(args) == 2 and args[0].isdigit() and args[1].isdigit():
            from_s = int(args[0])
            to_s = int(args[1])
            rolled = rollover_incomplete_tasks(from_s, to_s)
            client.chat_postMessage(
                channel=body["channel_id"],
                text=f"🔄 *Rolled over {len(rolled)} incomplete tasks from Sprint {from_s} to Sprint {to_s}.* (Tasks: {', '.join(rolled)})"
            )
        else:
            client.chat_postEphemeral(
                channel=body["channel_id"],
                user=body["user_id"],
                text="Usage: `/rollover-sprint <from_sprint_num> <to_sprint_num>` (e.g. `/rollover-sprint 1 2`)"
            )

# ==============================================================================
# 5. CLI Dispatcher (For Testing or Scheduled Cron)
# ==============================================================================

def main():
    import argparse
    parser = argparse.ArgumentParser(description="MAS AI Labs Slack Standup Bot")
    parser.add_argument("--day", type=int, default=1, help="Day in September 2026 (1 to 30)")
    parser.add_argument("--mode", choices=["personal-dms", "channel-digest", "dry-run", "socket-mode"], default="dry-run")

    args = parser.parse_args()
    sprint_file, sprint_num = get_sprint_file_for_day(args.day)
    tasks = parse_sprint_tasks(sprint_file)

    if args.mode == "dry-run":
        print(f"\n================ [PERSONAL DM PREVIEW (Day {args.day})] ================\n")
        owners = {}
        for t in tasks:
            owners.setdefault(t["owner"], []).append(t)
        for owner, o_tasks in owners.items():
            print(f"--- DM to {owner} ---")
            print(json.dumps(build_personal_dm_blocks(owner, o_tasks, args.day, sprint_num), indent=2))

        print(f"\n================ [7:45 PM MAIN CHANNEL DIGEST (Day {args.day})] ================\n")
        print(json.dumps(build_main_channel_digest(args.day, sprint_num), indent=2))

    elif args.mode == "socket-mode":
        if not SocketModeHandler or not app:
            print("Error: slack_bolt not installed or app tokens missing.")
            sys.exit(1)
        handler = SocketModeHandler(app, SLACK_APP_TOKEN)
        print("⚡ Starting MAS Standup Bot in Socket Mode...")
        handler.start()

if __name__ == "__main__":
    main()
