"""
MAS AI Labs — Automated Standup DM & Digest Scheduler
Author: MAS AI PM
Description: Uses APScheduler to automatically dispatch:
             1. 7:00 PM IST: Personalized DMs to task owners.
             2. 7:45 PM IST: Aggregated Pre-Standup Digest in #all-mas-ai-labs.
"""

import os
import logging
from datetime import datetime
try:
    from apscheduler.schedulers.background import BackgroundScheduler
    from apscheduler.schedulers.blocking import BlockingScheduler
except ImportError:
    BackgroundScheduler = None
    BlockingScheduler = None

from sprint_sync_engine import get_sprint_file_for_day, parse_sprint_tasks
from block_kit_views import build_personal_dm_view, build_pre_standup_digest_card

logger = logging.getLogger("MAS_Scheduler")

def get_current_september_day() -> int:
    """Calculates the current day number in September 2026."""
    now = datetime.now()
    if now.month == 9 and now.year == 2026:
        return now.day
    # Fallback to Day 1 for testing / out-of-bounds dates
    return 1

def dispatch_daily_dms(client, team_slack_ids: dict):
    """Sends personalized DMs to all task owners at 7:00 PM IST."""
    day = get_current_september_day()
    sprint_file, sprint_num = get_sprint_file_for_day(day)
    tasks = parse_sprint_tasks(sprint_file)

    owners_tasks = {}
    for t in tasks:
        owners_tasks.setdefault(t["owner"], []).append(t)

    logger.info(f"🚀 Dispatching 7:00 PM DMs for Day {day} (Sprint {sprint_num}) to {len(owners_tasks)} owners...")

    for owner, o_tasks in owners_tasks.items():
        slack_user_id = team_slack_ids.get(owner)
        if not slack_user_id:
            logger.warning(f"⚠️ No Slack ID configured for {owner}; skipping DM.")
            continue

        dm_blocks = build_personal_dm_view(owner, o_tasks, day, sprint_num)
        try:
            client.chat_postMessage(
                channel=slack_user_id,
                text=f"Daily Quick Standup Update (Day {day})",
                blocks=dm_blocks
            )
            logger.info(f"✅ DM sent to {owner} ({slack_user_id})")
        except Exception as e:
            logger.error(f"❌ Failed to DM {owner}: {e}")

def dispatch_channel_digest(client, main_channel: str, meet_url: str):
    """Posts the aggregated pre-standup digest to the main channel at 7:45 PM IST."""
    day = get_current_september_day()
    sprint_file, sprint_num = get_sprint_file_for_day(day)
    tasks = parse_sprint_tasks(sprint_file)

    done_tasks = [t for t in tasks if "done" in t["status"].lower() or "[x]" in t["status"]]
    blocked_tasks = [t for t in tasks if t["blocker"] and t["blocker"].lower() != "none" and t["blocker"] != "-"]

    logger.info(f"📊 Dispatching 7:45 PM Digest for Day {day} to {main_channel}...")

    card = build_pre_standup_digest_card(
        day=day,
        sprint_num=sprint_num,
        all_tasks=tasks,
        meet_url=meet_url
    )

    try:
        client.chat_postMessage(
            channel=main_channel,
            text=f"Standup Digest (Sprint {sprint_num} | Day {day})",
            blocks=card["blocks"]
        )
        logger.info(f"✅ 7:45 PM Digest posted to {main_channel}")
    except Exception as e:
        logger.error(f"❌ Failed to post digest to {main_channel}: {e}")

def start_standup_scheduler(client, team_slack_ids: dict, main_channel: str, meet_url: str):
    """Initializes the background scheduler to run daily at 7:00 PM and 7:45 PM IST."""
    if not BackgroundScheduler:
        logger.error("APScheduler is not installed. Run: pip install apscheduler")
        return None

    scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
    
    # 7:00 PM IST Monday-Friday: Personal DMs
    scheduler.add_job(
        dispatch_daily_dms,
        "cron",
        day_of_week="mon-fri",
        hour=19,
        minute=0,
        args=[client, team_slack_ids]
    )

    # 7:45 PM IST Monday-Friday: Channel Digest
    scheduler.add_job(
        dispatch_channel_digest,
        "cron",
        day_of_week="mon-fri",
        hour=19,
        minute=45,
        args=[client, main_channel, meet_url]
    )

    scheduler.start()
    logger.info("🕒 Daily Standup Scheduler started (7:00 PM DMs & 7:45 PM Digest in IST).")
    return scheduler
