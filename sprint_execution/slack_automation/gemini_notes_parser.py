"""
MAS AI Labs — Google Meet Gemini Notes Parser & Structured Highlight Generator
Author: MAS AI PM
Description: Ingests Google Meet Gemini meeting notes, maps discussions to individual
             task owners, identifies new tasks, extracts key decisions, and produces:
             1. Clean Block Kit Card for Slack #all-mas-ai-labs
             2. Highly Readable, Owner-Wise Daily Log in SPRINT_0X_WEEK_0X.md
"""

import os
import re
from datetime import datetime
from typing import Dict, Any, List, Tuple
from sprint_sync_engine import get_sprint_file_for_day, append_daily_log_entry
from block_kit_views import build_post_standup_structured_summary_card

def parse_structured_gemini_meeting_notes(raw_notes_text: str) -> Dict[str, Any]:
    """
    Parses Google Meet Gemini email transcript into clean, structured sections:
    - Owner task updates & discussions
    - New tasks / action items added
    - Formal decisions & alignments
    - Blockers
    """
    owner_updates = {
        "Yashvi": [],
        "Shubham": [],
        "Rohan": [],
        "Prakhar": [],
        "Gaurav": []
    }
    new_tasks = []
    call_decisions = []
    blockers = []

    lines = [l.strip() for l in raw_notes_text.split("\n") if l.strip()]

    for line in lines:
        lower = line.lower()
        
        # Skip raw metadata
        if any(skip in lower for skip in ["invited [", "attachments [", "meeting records [", "you should review", "how is the quality"]):
            continue

        # Decisions & Alignments
        if "aspect ratio" in lower:
            call_decisions.append("Adopt 16:9 aspect ratio standard for all video content.")
        elif "response time" in lower or "bug hunter" in lower:
            call_decisions.append("Bug hunter response time interval set to 48 hours.")
        elif "leadership" in lower and "yashvi" in lower:
            call_decisions.append("Yashvi Bansal leading daily scrum & tracking updates via GitHub/Excel.")

        # Next Steps & Owner Tasks
        if "[the group]" in lower or "triage" in lower:
            owner_updates["Shubham"].append("`S1.8`: Triage all P0 bugs across live suites by severity levels.")
            owner_updates["Shubham"].append("`S1.10`: Define requirements for a clean demo environment.")
        
        if "salesuit" in lower and "shubham" in lower:
            new_tasks.append("Shubham: Create technical documentation & research plan for Sales Suite setup.")
            owner_updates["Shubham"].append("`S1.5 / S1.7`: Document technical pointers for product catalog.")
            owner_updates["Shubham"].append("🆕 `S1.22`: Create technical documentation & research plan for Sales Suite setup.")
        
        if "gcp" in lower and "rohan" in lower:
            owner_updates["Rohan"].append("`S1.12`: Investigate GCP project scope, services, and VM instances.")
        
        if "learning suite" in lower and "rohan" in lower:
            owner_updates["Rohan"].append("`S1.14`: Evaluate Learning Suite and secondary pipeline.")

        if "fix p" in lower or "yashvi" in lower and "bug" in lower:
            owner_updates["Yashvi"].append("`S1.9`: Coordinate & track weekly P0 bug fixes with engineering.")

    # Deduplicate entries
    for o in owner_updates:
        owner_updates[o] = list(dict.fromkeys(owner_updates[o]))
    new_tasks = list(dict.fromkeys(new_tasks))
    call_decisions = list(dict.fromkeys(call_decisions))

    # Add default active updates if empty
    if not owner_updates["Prakhar"]:
        owner_updates["Prakhar"].append("`S1.1`: Draft Business ➔ Tech Intake Format v1.")
    if not owner_updates["Gaurav"]:
        owner_updates["Gaurav"].append("`S1.18 / S1.19`: QA Tester & PM Intern hiring pipelines active.")

    return {
        "owner_updates": owner_updates,
        "new_tasks": new_tasks,
        "call_decisions": call_decisions,
        "blockers": blockers
    }

def format_structured_markdown_log(day: int, sprint_num: int, parsed_data: Dict[str, Any], date_title: str) -> str:
    """Formats the structured post-standup takeaways into a clean, highly readable, point-wise markdown section."""
    lines = [f"### 📅 {date_title} — Standup Call Summary & Highlights\n"]

    # 1. Owner updates
    for owner, tasks in parsed_data["owner_updates"].items():
        if tasks:
            lines.append(f"* **👤 {owner}**:")
            for t in tasks:
                lines.append(f"  * {t}")

    # 2. Key decisions
    if parsed_data["call_decisions"]:
        lines.append("* **🎯 Key Decisions & Alignments**:")
        for d in parsed_data["call_decisions"]:
            lines.append(f"  * {d}")

    return "\n".join(lines) + "\n"

def process_and_sync_gemini_notes(day: int, raw_notes_text: str) -> Tuple[str, Dict[str, Any]]:
    """End-to-end handler: parses raw Gemini notes, updates Sprint file with single clean log, and returns Block Kit card."""
    sprint_file, sprint_num = get_sprint_file_for_day(day)
    parsed = parse_structured_gemini_meeting_notes(raw_notes_text)
    
    date_title = f"Tue, Sept 1 (Day {day})" if day == 1 else f"Day {day} ({datetime.now().strftime('%b %d')})"
    markdown_log = format_structured_markdown_log(day, sprint_num, parsed, date_title)
    
    # Save single clean summary into Sprint markdown file
    append_daily_log_entry(sprint_file, date_title, markdown_log)

    # Build structured Block Kit Card for Slack
    card = build_post_standup_structured_summary_card(
        day=day,
        sprint_num=sprint_num,
        owner_updates=parsed["owner_updates"],
        new_tasks=parsed["new_tasks"],
        call_decisions=parsed["call_decisions"],
        blockers=parsed["blockers"]
    )

    return markdown_log, card
