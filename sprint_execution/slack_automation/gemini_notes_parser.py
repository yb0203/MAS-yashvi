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

def parse_gemini_meeting_notes(raw_notes_text: str) -> Dict[str, List[str]]:
    """
    Parses structured sections from Google Meet's Gemini automated email transcript.
    Extracts: Summary, Key Decisions, Action Items / Unblocked Tasks.
    """
    sections = {
        "summary": [],
        "decisions": [],
        "action_items": []
    }

    current_section = "summary"
    lines = raw_notes_text.strip().split("\n")

    for line in lines:
        clean = line.strip()
        if not clean:
            continue

        lower = clean.lower()
        if "decision" in lower or "agreed" in lower:
            current_section = "decisions"
            continue
        elif "action item" in lower or "next step" in lower or "unblock" in lower or "owner" in lower:
            current_section = "action_items"
            continue
        elif "summary" in lower or "overview" in lower:
            current_section = "summary"
            continue

        # Bullet point or sentence
        bullet = re.sub(r"^[-*•\d.]+\s*", "", clean)
        if bullet:
            sections[current_section].append(bullet)

    return sections

def format_day_highlights_markdown(day: int, sprint_num: int, parsed_notes: Dict[str, List[str]]) -> str:
    """Formats the extracted notes into a clean, professional standup highlight bullet."""
    summary_snippet = " | ".join(parsed_notes["summary"][:2]) if parsed_notes["summary"] else "Daily standup executed."
    decisions_snippet = "; ".join(parsed_notes["decisions"][:2]) if parsed_notes["decisions"] else "All commitments on track."
    actions_snippet = "; ".join(parsed_notes["action_items"][:3]) if parsed_notes["action_items"] else "Proceeding with scheduled sprint tasks."

    return (
        f"**Standup Highlights (Gemini Notes)**: {summary_snippet} "
        f"| *Decisions*: {decisions_snippet} "
        f"| *Action Items*: {actions_snippet}"
    )

def process_and_sync_gemini_notes(day: int, raw_notes_text: str) -> str:
    """End-to-end handler: parses raw Gemini notes and updates the active Sprint markdown file."""
    sprint_file, sprint_num = get_sprint_file_for_day(day)
    parsed = parse_gemini_meeting_notes(raw_notes_text)
    highlight_text = format_day_highlights_markdown(day, sprint_num, parsed)

    date_header = f"Day {day} ({datetime.now().strftime('%b %d')})"
    append_daily_log_entry(sprint_file, date_header, highlight_text)

    return highlight_text
