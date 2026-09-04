"""
Publish Day 3 Post-Standup Highlights to #all-mas-ai-labs
"""
import os
import ssl
import certifi
from dotenv import load_dotenv
from slack_sdk import WebClient
from gemini_notes_parser import format_structured_markdown_log
from block_kit_views import build_post_standup_structured_summary_card
from sprint_sync_engine import get_sprint_file_for_day, append_daily_log_entry

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
MAIN_STANDUP_CHANNEL = os.getenv("MAIN_STANDUP_CHANNEL", "C0B2NHS5ZH6")

day = 3
sprint_file, sprint_num = get_sprint_file_for_day(day)

day3_data = {
    "owner_updates": {
        "Yashvi": [
            "`S1.6`: Capability Registry schema seeded and aligned `[Completed]`",
            "`S1.16 / S1.17`: Slack bot App Home dashboard deployed and live testing with pod",
            "`S1.2 – S1.4`: Client context dossiers (Orane, College Vidya, Chitkara) initiated"
        ],
        "Shubham": [
            "`S1.7`: P0 product & module list frozen with named owners `[Completed]`",
            "`S1.22`: Sales Suite prototype architecture & DB separation plan delivered `[Completed]`",
            "`S1.8 / S1.10`: Live bug triage and clean demo environment requirements underway"
        ],
        "Rohan": [
            "`S1.9`: Email delivery bug resolved and info email pipeline migrated",
            "`S1.12`: GCP asset inventory flagged as blocked due to API credit renewal"
        ],
        "Prakhar": [
            "`S1.1`: Intake format v1 & client contact Google Sheet in progress",
            "`S1.5 / S1.11`: Product Catalogue schema & Sales Suite Demo #1 alignment"
        ],
        "Gaurav": [
            "`S1.18`: QA Tester (2-month contract) hiring pipeline active with HR",
            "`S1.21`: Preparing for Friday Review #1 (Sept 4, 8:00 PM)"
        ]
    },
    "call_decisions": [
        "Confirmed 3 deliverables completed ahead of Friday review (S1.6, S1.7, S1.22).",
        "Team focusing on demo stabilization and client dossier compilation for Day 4.",
        "Friday Weekly Review #1 scheduled for tomorrow, Sept 4 at 8:00 PM IST."
    ],
    "new_tasks": [
        "Align student dashboard with seeded test data (Rohan & Yashvi)",
        "Finalize client contact Google Sheet structure (Prakhar)"
    ],
    "blockers": [
        "Rohan (S1.12): GCP inventory blocked pending AI/API credit renewal"
    ]
}

if __name__ == "__main__":
    date_title = "Thu, Sept 3 (Day 3)"
    md_log = format_structured_markdown_log(day, sprint_num, day3_data, date_title)
    append_daily_log_entry(sprint_file, date_title, md_log)
    print("✅ Day 3 Markdown Log synced to SPRINT_01_WEEK_01.md")

    card = build_post_standup_structured_summary_card(
        day=day,
        sprint_num=sprint_num,
        owner_updates=day3_data["owner_updates"],
        new_tasks=day3_data["new_tasks"],
        call_decisions=day3_data["call_decisions"],
        blockers=day3_data["blockers"]
    )

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    client = WebClient(token=SLACK_BOT_TOKEN, ssl=ssl_context)
    resp = client.chat_postMessage(
        channel=MAIN_STANDUP_CHANNEL,
        text="📝 Standup Call Summary • Day 3 (Thu, Sep 03)",
        blocks=card["blocks"]
    )
    if resp.get("ok"):
        print(f"✅ Successfully published Day 3 Standup Summary to Slack channel {MAIN_STANDUP_CHANNEL}!")
    else:
        print(f"❌ Failed to publish: {resp}")
