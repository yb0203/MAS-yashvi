# MAS AI Labs — Automated Slack Standup & Quick Update System

This system automates daily standup data collection for the remote **MAS AI Labs** team, ensuring tasks, blockers, and root causes are pre-populated before the **8:00 PM IST** daily standup call.

---

## 🏗️ System Architecture & Workflow

```
┌────────────────────────────────────────────────────────────────────────┐
│               DAILY SLACK AUTOMATED STANDUP TIMELINE                   │
├────────────────────────────────────────────────────────────────────────┤
│ 7:00 PM IST ──► Automated Slack Prompt sent to #ai-labs-standup        │
│                 Bot parses LIVE_SPRINT_BOARD.md and pings owners with  │
│                 their assigned daily tasks & blocker form.             │
│                                                                        │
│ 7:00–7:40 PM ─► Teammates submit "Quick Updates" via Slack Thread     │
│                 or interactive modal (Done, Status, Blocker & Reason). │
│                                                                        │
│ 7:45 PM IST ──► Bot aggregates submissions into the Pre-Standup Digest │
│                 card with RAG indicators and Blocker highlights.       │
│                                                                        │
│ 8:00 PM IST ──► 20-min Live Standup call focuses directly on unblocking│
│                 the pre-aggregated Amber/Red items.                    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Implementation Options

### Option 1: Lightweight Python Script + Slack Webhook (Recommended & Ready)
* Uses `slack_standup_bot.py` via cron, GitHub Actions, or local runner.
* Parses `LIVE_SPRINT_BOARD.md` in real-time, extracts the day's active tasks by teammate, and posts formatted Block Kit cards to your Slack webhook URL.

### Option 2: Slack Interactive Modal (Slack Bolt App)
* Enables teammates to type `/quick-update` or `/standup` in Slack to open an interactive modal with dropdowns for status, text inputs for blockers and reasons, and auto-saves to markdown.

### Option 3: Slack Native Workflow Builder
* Import the JSON payloads in `slack_block_kit_payloads.json` into Slack's built-in Workflow Builder to schedule daily prompts at 7:00 PM IST.

---

## 🚀 Quick Start (Running Option 1)

### 1. Setup Environment
```bash
cd "/Users/yashvi/Documents/MAS - AI PM/sprint_execution/slack_automation"
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
```

### 2. Test Local Run (Dry Run Mode)
To see the exact Block Kit payload generated from `LIVE_SPRINT_BOARD.md` without posting to Slack:
```bash
python3 slack_standup_bot.py --day 1 --dry-run
```

### 3. Send 7:00 PM Daily Task Reminder to Slack
```bash
python3 slack_standup_bot.py --day 1 --mode prompt
```

### 4. Generate Pre-Standup Summary for 8:00 PM Call
```bash
python3 slack_standup_bot.py --day 1 --mode digest
```

---

## ⚙️ Automated Scheduling (Cron Example)

Add this to your server or GitHub Actions workflow to run automatically Monday through Friday:

```cron
# 7:00 PM IST (13:30 UTC): Send Daily Quick Update Prompt
30 13 * * 1-5 cd "/Users/yashvi/Documents/MAS - AI PM/sprint_execution/slack_automation" && python3 slack_standup_bot.py --mode auto-prompt

# 7:45 PM IST (14:15 UTC): Send Pre-Standup Digest Card
15 14 * * 1-5 cd "/Users/yashvi/Documents/MAS - AI PM/sprint_execution/slack_automation" && python3 slack_standup_bot.py --mode auto-digest
```
