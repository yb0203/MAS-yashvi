#!/usr/bin/env python3
"""
MAS AI Labs — Automated Slack Standup & Quick Update Bot
Author: MAS AI PM
Description: Dynamically reads active sprint markdown files (SPRINT_01_WEEK_01.md, etc.),
             extracts assigned tasks with Expected Outcomes, Blockers & Delay Reasons,
             and sends Slack Block Kit prompts & standup summaries.
"""

import os
import re
import sys
import json
import argparse
import urllib.request
from typing import List, Dict, Any, Tuple

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MASTER_PLAN_PATH = os.path.join(BASE_DIR, "MONTH_01_MASTER_PLAN.md")

def get_sprint_file_for_day(day: int) -> Tuple[str, int]:
    if 1 <= day <= 5:
        return os.path.join(BASE_DIR, "SPRINT_01_WEEK_01.md"), 1
    elif 6 <= day <= 10:
        return os.path.join(BASE_DIR, "SPRINT_02_WEEK_02.md"), 2
    elif 11 <= day <= 15:
        return os.path.join(BASE_DIR, "SPRINT_03_WEEK_03.md"), 3
    else:
        return os.path.join(BASE_DIR, "SPRINT_04_WEEK_04.md"), 4

SLACK_USER_HANDLES = {
    "Gaurav": "@Gaurav",
    "Shubham": "@Shubham",
    "Rohan": "@Rohan",
    "Prakhar": "@Prakhar",
    "Yashvi": "@Yashvi",
    "QA / Tester": "@QA",
    "PM Intern": "@PM_Intern",
    "Marketing / Vendor": "@Vendor",
    "All": "@channel"
}

def parse_sprint_file(file_path: str) -> List[Dict[str, Any]]:
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return []

    tasks = []
    task_regex = re.compile(
        r"\|\s*\*\*(S\d+\.\d+)\*\*\s*\|\s*([^|]+)\s*\|\s*\*\*([^*]+)\*\*(?:\s*\*\([^*]+\)\*)?\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|"
    )

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = task_regex.search(line)
            if match:
                task_id = match.group(1).strip()
                task_desc = match.group(2).strip()
                owner = match.group(3).strip()
                day_str = match.group(4).strip()
                status = match.group(5).strip().replace("`", "")
                expected_outcome = match.group(6).strip()
                actual_outcome = match.group(7).strip()
                blocker = match.group(8).strip()
                delay_reason = match.group(9).strip()
                rag = match.group(10).strip()

                day_nums = [int(d) for d in re.findall(r"\d+", day_str)]

                tasks.append({
                    "id": task_id,
                    "task": task_desc,
                    "owner": owner,
                    "day_str": day_str,
                    "day_nums": day_nums,
                    "status": status,
                    "expected_outcome": expected_outcome,
                    "actual_outcome": actual_outcome,
                    "blocker": blocker,
                    "delay_reason": delay_reason,
                    "rag": rag
                })

    return tasks

def filter_tasks_by_day(tasks: List[Dict[str, Any]], day: int) -> List[Dict[str, Any]]:
    active = []
    for t in tasks:
        if not t["day_nums"]:
            active.append(t)
            continue
        if len(t["day_nums"]) == 1 and t["day_nums"][0] == day:
            active.append(t)
        elif len(t["day_nums"]) >= 2 and min(t["day_nums"]) <= day <= max(t["day_nums"]):
            active.append(t)
    return active

def build_daily_prompt_payload(day_tasks: List[Dict[str, Any]], day: int, sprint_num: int) -> Dict[str, Any]:
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"🚀 MAS AI Labs — Daily Quick Update (Sprint {sprint_num} | Day {day})",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"⏰ *Daily Standup Call is at 8:00 PM IST (in 1 hour).*\n"
                    f"Please reply in this thread before *7:45 PM* with your quick status, blockers, and delay reasons."
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*📌 Today's Scheduled Deliverables & Task Owners:*"
            }
        }
    ]

    owners: Dict[str, List[Dict[str, Any]]] = {}
    for t in day_tasks:
        owners.setdefault(t["owner"], []).append(t)

    for owner, t_list in owners.items():
        slack_tag = SLACK_USER_HANDLES.get(owner, f"*{owner}*")
        task_bullets = []
        for t in t_list:
            task_bullets.append(
                f"• `{t['id']}`: {t['task']}\n"
                f"   ↳ *Target Outcome:* _{t['expected_outcome']}_\n"
                f"   ↳ *Status:* `{t['status']}` | *RAG:* {t['rag']}"
            )
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"👤 *{slack_tag}*:\n" + "\n".join(task_bullets)
            }
        })

    blocks.append({"type": "divider"})
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*📝 Thread Reply Template:*\n"
                "```\n"
                "*Name:* [Your Name]\n"
                "1. Task IDs: [e.g. S1.1 - Done / In Progress / Blocked]\n"
                "2. Actual Outcome: [Completed PR / Doc link / output summary]\n"
                "3. Time Sink: [What specific work took the most time today?]\n"
                "4. Ad-Hoc MAS Requests: [Any new incoming requests? (e.g. none / HR automation)]\n"
                "5. Blockers: [None / Description]\n"
                "6. Delay Reason (if delayed): [Root cause & required resolution]\n"
                "7. RAG: [🟢 GREEN / 🟡 AMBER / 🔴 RED]\n"
                "```"
            )
        }
    })

    return {"blocks": blocks}

def build_pre_standup_digest_payload(day_tasks: List[Dict[str, Any]], day: int, sprint_num: int) -> Dict[str, Any]:
    blocked_tasks = [
        t for t in day_tasks
        if t["blocker"] and t["blocker"].lower() != "none" and t["blocker"] != "-"
    ]
    delayed_tasks = [
        t for t in day_tasks
        if t["delay_reason"] and t["delay_reason"].lower() != "none" and t["delay_reason"] != "-"
    ]

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"📊 Standup Digest & Blocker Summary (Sprint {sprint_num} | Day {day})",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"📞 *Google Meet at 8:00 PM IST.*\n"
                    f"Active Tasks: *{len(day_tasks)}* | Flagged Blockers: *{len(blocked_tasks)}* | Delays: *{len(delayed_tasks)}*"
                )
            }
        },
        {"type": "divider"}
    ]

    if blocked_tasks or delayed_tasks:
        flagged = list({t["id"]: t for t in (blocked_tasks + delayed_tasks)}.values())
        alert_lines = []
        for t in flagged:
            alert_lines.append(
                f"🚨 *`{t['id']}` ({t['owner']})*: {t['task']}\n"
                f"   ↳ *Blocker:* `{t['blocker']}`\n"
                f"   ↳ *Delay Reason / Root Cause:* _{t['delay_reason']}_"
            )
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*⚠️ Items Requiring Discussion / Unblocking on the Call:*\n\n" + "\n\n".join(alert_lines)
            }
        })
    else:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "🎉 *Zero Blockers or Delays Flagged!* All active deliverables on track."
            }
        })

    blocks.append({"type": "divider"})
    blocks.append({
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": f"📂 Master Plan: `MONTH_01_MASTER_PLAN.md` | Sprint Doc: `SPRINT_0{sprint_num}_WEEK_0{sprint_num}.md`"
            }
        ]
    })

    return {"blocks": blocks}

def send_slack_webhook(webhook_url: str, payload: Dict[str, Any]) -> bool:
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            webhook_url,
            data=data,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req) as resp:
            return resp.getcode() == 200
    except Exception as e:
        print(f"❌ Webhook Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="MAS AI Labs Slack Standup Bot")
    parser.add_argument("--day", type=int, default=1, help="Day number in Month 1 (1 to 30)")
    parser.add_argument(
        "--mode",
        choices=["prompt", "digest", "dry-run"],
        default="dry-run",
        help="Mode: 'prompt' (7 PM prompt), 'digest' (7:45 PM digest), or 'dry-run' (print JSON)"
    )
    parser.add_argument("--webhook", type=str, default=None, help="Slack Webhook URL")

    args = parser.parse_args()

    sprint_file, sprint_num = get_sprint_file_for_day(args.day)
    tasks = parse_sprint_file(sprint_file)
    day_tasks = filter_tasks_by_day(tasks, args.day)

    if not day_tasks:
        print(f"No tasks found for Day {args.day} in {os.path.basename(sprint_file)}")
        sys.exit(0)

    webhook_url = args.webhook or os.environ.get("SLACK_WEBHOOK_URL")

    if args.mode == "prompt":
        payload = build_daily_prompt_payload(day_tasks, args.day, sprint_num)
        if webhook_url:
            send_slack_webhook(webhook_url, payload)
            print("✅ 7:00 PM Prompt sent to Slack!")
        else:
            print("⚠️ No SLACK_WEBHOOK_URL. JSON Payload:\n")
            print(json.dumps(payload, indent=2))

    elif args.mode == "digest":
        payload = build_pre_standup_digest_payload(day_tasks, args.day, sprint_num)
        if webhook_url:
            send_slack_webhook(webhook_url, payload)
            print("✅ 7:45 PM Standup Digest sent to Slack!")
        else:
            print("⚠️ No SLACK_WEBHOOK_URL. JSON Payload:\n")
            print(json.dumps(payload, indent=2))

    elif args.mode == "dry-run":
        print(f"\n================ [7:00 PM PROMPT (Sprint {sprint_num} | Day {args.day})] ================\n")
        print(json.dumps(build_daily_prompt_payload(day_tasks, args.day, sprint_num), indent=2))
        print(f"\n================ [7:45 PM DIGEST (Sprint {sprint_num} | Day {args.day})] ================\n")
        print(json.dumps(build_pre_standup_digest_payload(day_tasks, args.day, sprint_num), indent=2))

if __name__ == "__main__":
    main()
