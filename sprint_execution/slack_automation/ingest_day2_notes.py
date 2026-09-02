"""
Trigger Script — Ingest Day 2 Google Meet Notes and Broadcast to #all-mas-ai-labs
"""
import os
import sys
import ssl
import certifi
from dotenv import load_dotenv
from slack_sdk import WebClient
from gemini_notes_parser import process_and_sync_gemini_notes

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
MAIN_STANDUP_CHANNEL = os.getenv("MAIN_STANDUP_CHANNEL", "C0B2NHS5ZH6")

RAW_NOTES = """
Sep 2, 2026
MAS AI Labs Daily Scrum
Invited [MAS Admin](mailto:admin@myanalyticsschool.com) [kumar Gaurav](mailto:kg262005@gmail.com) [shubham.kumar.patel.2410@gmail.com](mailto:shubham.kumar.patel.2410@gmail.com) [MAS Team](mailto:info@myanalyticsschool.com) [rohan.kr.pandey2.0@gmail.com](mailto:rohan.kr.pandey2.0@gmail.com) [prakhar goswami](mailto:prakhar.goswami.30698@gmail.com) [Yashvi Bansal](mailto:bansaly0203@gmail.com)
Attachments [MAS AI Labs Daily Scrum](https://calendar.google.com/calendar/event?eid=NzBwbThvaGtja3M2Y2I5azYxaDNpYjlrNjlqMzBiOW83MG82MmI5azc0cmo4Y3I2NzBxamlkaG42Z18yMDI2MDkwMlQxNDMwMDBaIGluZm9AbXlhbmFseXRpY3NzY2hvb2wuY29t)
Meeting records [Transcript](https://docs.google.com/document/d/1he6_-AZpVK3MaNuu1mUveDzf4xUrg5kSWm2k-roV7gI/edit?usp=drive_web&tab=t.2yfn30gdr7tv)
Summary
Team members aligned on project technical requirements and established the prototype direction for upcoming suite demonstrations.
Integration and project status
Tools like the Slack bot and Gemini Large Language Model were reviewed for project tracking. Technical schemas for learning and sales suites require finalization for 2nd week demonstrations.
Sales suite prototype review
The team decided to proceed with the prototype featuring database separation and independent scaling for client management. This architecture enables vendor management and independent lead imports.
Stability and deployment progress
Email delivery bugs were resolved and migration tasks completed. Focus remains on stabilizing the student dashboard to ensure platform reliability for future milestones.
Decisions
Aligned
Component ownership structure defined Component ownership is established, designating primary and technical owners for the learning and sales suites.
Feature development prioritized for launch Feature development is prioritized over monetization implementation for the sales suite.
Sales suite development workflow defined The development workflow for the sales suite is established as prioritizing P0 bug fixes, followed by technicalization, then component-wise imports.
Next steps
[Yashvi Bansal] Create client context: Initiate the creation process for client context documents.
[Prakhar] Create client sheet: Generate the client information seat in Google Sheet format.
[Yashvi Bansal] Update component owners: Assign primary and technical owners for the learning and sales suite components.
[Shubham Patel] Share prototype artifact: Distribute the developed sales suite prototype artifact to the team.
[Shubham Patel] Evaluate prototype backend: Conduct technical analysis and evaluation of the sales suite prototype from a backend perspective.
[Rohan kr. pandey] Align on dashboard: Coordinate with Yashvi to understand the student dashboard requirements with seeded data after resolving existing bugs.
Details
Team Introductions and Backgrounds: Shubham Aryan provided an overview of their professional background, noting their 2020 graduation from IIT BHU with a degree in chemical engineering, prior experience at United Health Group, their role as a growth manager at Blinket during the launch in tier-2 cities, and their current position as a lead product analyst at Tide. Yashvi Bansal shared their background as a 2003 graduate of IIT BHU, detailing their work history at Kotak Mahindra Bank and their current responsibilities in the platform team at "mass" working on the learning suite. Shubham Patel, a recent IIT BHU mining graduate, discussed their experience at Risk Prediction 360 and their role as a tech lead at "mass," where they contribute to projects including Mr. Mentor and the student dashboard. Rohan kr. pandey detailed their journey from a biology background to self-taught software development, moving from mobile repair to software development, and their current role at "mass". MAS Team (Gaurav) introduced themself as an IIT Madras alumnus who has been with "mass" for five years.
Yashvi Bansal's Project Status and Tooling: Yashvi Bansal updated the team on the Slack bot project, which has been integrated with Gmail and utilizes the Gemini LLM to generate post-standup summaries. MAS Team (Gaurav) requested that a client contact sheet be created in a Google Sheet format, noting that this task was assigned to Prakhar. Yashvi Bansal and MAS Team discussed the "define schema and seed capability registry" task, with the team establishing that they must be "demo ready" for both the learning and sales suites by the end of the second week.
Shubham Patel's Sales Suite Prototype and Architecture: Shubham Patel presented a prototype for the "Sales Suite," demonstrating a design with a dedicated login page for clients and a strategy for database-level separation to allow for independent scaling. The prototype includes features for vendor management, tag editing, IP whitelisting, API integration, and team management, allowing clients to handle lead imports independently of the main platform database. Shubham Patel also proposed a revenue-generating feature for WhatsApp campaigns, where clients could be charged for sending template messages, with integration capabilities for platforms like Meta and Google Ads. MAS Team (Gaurav) directed the team to proceed with the prototype, focusing on feature parity for the admin and salesperson roles, and instructed that the team start evaluating the backend analysis and subsequent integration of the component-wise import job.
Rohan kr. pandey's Development Progress: Rohan kr. pandey reported that the bug preventing email message delivery is fixed, and they have successfully completed the migration of the "info" email account to a new location to resolve clutter issues. Rohan kr. pandey is currently testing the new pipeline and mentioned they would re-verify the migration once their ChatGPT subscription is renewed. MAS Team (Gaurav) noted that the "Student Admin" dashboard lacks stability and instructed that once the current bugs are resolved, Rohan kr. pandey should connect with Yashvi Bansal to align the student dashboard with seeded data.
Meeting Conclusion and Demo Readiness: Shubham Aryan provided final feedback, emphasizing the importance of clear communication from the team and efficient bug reporting. The meeting concluded with a commitment to be "demo ready" for the suites by the third week, with MAS Team (Gaurav) confirming the timeline.
"""

if __name__ == "__main__":
    print("🚀 Ingesting Day 2 Google Meet Notes...")
    markdown_log, card = process_and_sync_gemini_notes(day=2, raw_notes_text=RAW_NOTES)
    print("\n--- Markdown Log Added to SPRINT_01_WEEK_01.md ---\n")
    print(markdown_log)

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    client = WebClient(token=SLACK_BOT_TOKEN, ssl=ssl_context)
    resp = client.chat_postMessage(
        channel=MAIN_STANDUP_CHANNEL,
        text="📝 Standup Call Summary • Day 2 (Wed, Sep 02)",
        blocks=card["blocks"]
    )
    if resp.get("ok"):
        print(f"✅ Successfully posted Day 2 Standup Summary to Slack channel {MAIN_STANDUP_CHANNEL}!")
    else:
        print(f"❌ Failed to post to Slack: {resp}")
