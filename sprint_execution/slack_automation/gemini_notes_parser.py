"""
MAS AI Labs — Google Meet Gemini Notes Parser & Highlight Generator
Author: MAS AI PM
Description: Ingests Google Meet Gemini meeting notes (from email or slash command),
             extracts key decisions, unblocked items, and action items, and formats
             them into the official Day Highlights for Slack and the active Sprint doc.
"""

import os
import re
from datetime import datetime
from typing import Dict, Any, List
from sprint_sync_engine import get_sprint_file_for_day, append_daily_log_entry

def parse_gemini_meeting_notes(raw_notes_text: str) -> Dict[str, Any]:
    """
    Parses structured sections from Google Meet's Gemini automated email transcript.
    Extracts: Summary, Decisions, Aligned items, Action Items / Next Steps, and Assigned Owners.
    """
    parsed = {
        "summary": [],
        "decisions": [],
        "next_steps": [],
        "task_assignments": {}
    }

    lines = raw_notes_text.strip().split("\n")
    current_mode = "summary"

    for line in lines:
        clean = line.strip()
        if not clean:
            continue

        lower = clean.lower()
        if "summary" in lower and len(clean) < 20:
            current_mode = "summary"
            continue
        elif "decisions" in lower or "aligned" in lower or "disagreements" in lower:
            current_mode = "decisions"
            continue
        elif "next steps" in lower:
            current_mode = "next_steps"
            continue
        elif "details" in lower and len(clean) < 20:
            current_mode = "details"
            continue

        # Extract Next Steps with [Owner] brackets
        next_step_match = re.match(r"^\[([^\]]+)\]\s*(.+)$", clean)
        if next_step_match:
            owner_raw = next_step_match.group(1).strip()
            task_desc = next_step_match.group(2).strip()
            parsed["next_steps"].append(f"[{owner_raw}] {task_desc}")
            parsed["task_assignments"].setdefault(owner_raw, []).append(task_desc)
            continue

        if current_mode == "summary" and len(clean) > 30 and not clean.startswith("Invited") and not clean.startswith("Attachments"):
            parsed["summary"].append(clean)
        elif current_mode == "decisions" and len(clean) > 10 and not clean.startswith("Attachments"):
            parsed["decisions"].append(clean)

    return parsed

def format_day_highlights_markdown(day: int, sprint_num: int, parsed_notes: Dict[str, Any]) -> str:
    """Formats the extracted notes into a clean, comprehensive standup highlight entry."""
    summary_text = parsed_notes["summary"][0] if parsed_notes["summary"] else "Daily Scrum executed with pod leadership alignment."
    
    decisions_list = []
    for d in parsed_notes["decisions"][:3]:
        decisions_list.append(f"• {d}")
    decisions_str = "\n   ".join(decisions_list) if decisions_list else "• Pod commitments on track."

    next_steps_list = []
    for s in parsed_notes["next_steps"][:5]:
        next_steps_list.append(f"• {s}")
    next_steps_str = "\n   ".join(next_steps_list) if next_steps_list else "• Continuing scheduled sprint deliverables."

    return (
        f"**Daily Scrum Highlights (Day {day} — Google Meet Gemini)**:\n"
        f"   ↳ **Summary**: {summary_text}\n"
        f"   ↳ **Key Decisions & Alignment**:\n   {decisions_str}\n"
        f"   ↳ **Assigned Next Steps**:\n   {next_steps_str}"
    )

def process_and_sync_gemini_notes(day: int, raw_notes_text: str) -> str:
    """End-to-end handler: parses raw Gemini notes and updates the active Sprint markdown file."""
    sprint_file, sprint_num = get_sprint_file_for_day(day)
    parsed = parse_gemini_meeting_notes(raw_notes_text)
    highlight_text = format_day_highlights_markdown(day, sprint_num, parsed)

    date_header = f"Tue, Sept 1 (Day {day})" if day == 1 else f"Day {day} ({datetime.now().strftime('%b %d')})"
    append_daily_log_entry(sprint_file, date_header, highlight_text)

    return highlight_text
