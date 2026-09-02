#!/usr/bin/env python3
"""
MAS AI Labs — Ingest Day 1 Gemini Meeting Notes & Post Structured Highlights to Slack
"""

import os
import ssl
import certifi
from dotenv import load_dotenv
from slack_sdk import WebClient
from gemini_notes_parser import process_and_sync_gemini_notes

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

RAW_NOTES = """
Sep 1, 2026
MAS AI Labs Daily Scrum
Invited MAS Admin, kumar Gaurav, shubham.kumar.patel.2410@gmail.com, MAS Team, rohan.kr.pandey2.0@gmail.com, prakhar goswami, Yashvi Bansal
Summary
The meeting covered team leadership changes, technical infrastructure updates, and consensus on video content standards.
Leadership Transition and Operations
The team transitioned leadership for daily meetings and formalized task tracking through shared documentation. This shift aims to improve workflow management and project transparency.
Technical Infrastructure and Triage
Technical leads prioritized triaging critical bugs and defining requirements for the Google Cloud Platform environment setup. Efforts also focused on establishing stable configurations for the platform.
Content Standards and Modeling
The team decided to adopt a 16 by 9 aspect ratio for all social media video content. Discussions also assessed artificial intelligence model performance based on business feasibility.
Decisions
Aligned
Bug hunter response time: The bug hunter response time interval is set to 48 hours.
Social Media Video: Adopt 16:9 aspect ratio for all social media video content.
Daily Scrum Leadership: Yashvi Bansal to lead daily scrum and manage task updates via GitHub/Excel.
Next steps
[The group] Triage P0 Bugs: Triage all P0 bugs across the live suite by severity levels.
[The group] Define Requirements: Define the requirements for a clean demo environment.
[Shubham Patel] Document Salesuit Plan: Create a technical documentation and research plan for the salesuit code and generalized setup.
[Rohan kr. pandey] Understand GCP Scope: Review current Google Cloud Platform project services and virtual machines to understand the project scope.
[Rohan kr. pandey] Review Learning Suite: Evaluate the learning suite and second based pipeline.
[Yashvi Bansal] Fix P Bugs: Coordinate and track P-bug fixing tasks identified for the week.
[Shubham Patel] Document Catalog Pointers: Compile technical pointers for product components in the catalog sheet from a developer perspective.
"""

def main():
    print("📝 Ingesting Day 1 Gemini Meeting Notes...")
    markdown_log, card = process_and_sync_gemini_notes(1, RAW_NOTES)
    print("✅ SPRINT_01_WEEK_01.md updated successfully!")
    print("\nFormatted Summary for Markdown Log:\n", markdown_log)

    # Post to Slack #all-mas-ai-labs
    token = os.environ.get("SLACK_BOT_TOKEN")
    channel = os.environ.get("SLACK_STANDUP_CHANNEL", "C0B2NHS5ZH6")
    ssl_ctx = ssl.create_default_context(cafile=certifi.where())
    client = WebClient(token=token, ssl=ssl_ctx)

    try:
        resp = client.chat_postMessage(
            channel=channel,
            text="📝 MAS AI Labs — Post-Standup Highlights (Sprint 1 | Day 1)",
            blocks=card["blocks"]
        )
        print(f"\n🚀 Broadcasted Structured Post-Standup Highlights to Slack channel {channel}! ts: {resp.get('ts')}")
    except Exception as e:
        print(f"Error posting to Slack: {e}")

if __name__ == "__main__":
    main()
