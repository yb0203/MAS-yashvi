# MAS AI Labs — Automated Slack Standup & Living Sprint Engine

## 🎯 Architecture Overview

```
┌────────────────────────────────────────────────────────────────────────┐
│                        SLACK STANDUP BOT ENGINE                        │
├────────────────────────────────────────────────────────────────────────┤
│ 7:00 PM IST ──► [Personal DMs to Owners]                               │
│                 No main group spam! Individual teammates get a private │
│                 DM with ONLY their scheduled tasks for today.          │
│                                                                        │
│ 7:00–7:45 PM ─► [Ultra-Fast <1 Min Update]                             │
│                 Teammates select:                                      │
│                 • Status Dropdown: [x] Done | [-] In Progress          │
│                 • RAG Dropdown:    🟢 Green | 🟡 Amber | 🔴 Red        │
│                 • Quick Note:      PR link or Blocker description      │
│                                                                        │
│ 7:45 PM IST ──► [Main Channel Pre-Standup Card]                        │
│                 Single high-signal summary posted to #ai-labs-standup: │
│                 • Tasks completed today                                │
│                 • Red/Amber blockers requiring unblocking on call      │
│                 • Direct Google Meet link for 8:00 PM call             │
│                                                                        │
│ 8:30 PM IST ──► [2-Way Living Sprint Sync]                             │
│                 Bot writes outcomes directly into SPRINT_0X_WEEK_0X.md │
│                 and updates active blockers in MONTH_01_MASTER_PLAN.md │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Setup (1-Click App Manifest)

1. Go to **[api.slack.com/apps](https://api.slack.com/apps)** $\rightarrow$ Click **Create New App**.
2. Select **From an app manifest**.
3. Choose your Slack Workspace.
4. Copy & paste the contents of [`slack_app_manifest.json`](./slack_app_manifest.json) $\rightarrow$ Click **Create**.
5. Generate an **App-Level Token** with `connections:write` scope (starts with `xapp-...`).
6. Install the app to your workspace and copy the **Bot User OAuth Token** (starts with `xoxb-...`).

---

## 🔐 Environment Variables (`.env`)

Create a `.env` file in `sprint_execution/slack_automation/`:

```ini
SLACK_BOT_TOKEN="xoxb-your-bot-token"
SLACK_APP_TOKEN="xapp-your-app-token"
SLACK_STANDUP_CHANNEL="#ai-labs-standup"

# Mapping team member names to their Slack User IDs (Right click profile in Slack -> Copy Member ID)
SLACK_ID_GAURAV="U01XXXXXX"
SLACK_ID_SHUBHAM="U02XXXXXX"
SLACK_ID_ROHAN="U03XXXXXX"
SLACK_ID_PRAKHAR="U04XXXXXX"
SLACK_ID_YASHVI="U05XXXXXX"
```

---

## ⚡ Slash Commands Available to Team

| Slash Command | What It Does |
|---|---|
| `/standup` | Opens your personal daily standup modal on demand anytime. |
| `/sprint-summary` | Generates an instant summary card of sprint progress. |
| `/rollover-sprint 1 2` | Moves uncompleted/delayed tasks from Sprint 1 to Sprint 2 as `[Rollover]`. |

---

## 🧪 Testing Locally (Dry Run)

```bash
# Test Day 1 Personal DMs & 7:45 PM Digest Output
python3 sprint_execution/slack_automation/slack_bolt_app.py --day 1 --mode dry-run

# Run Live Bot in Socket Mode
python3 sprint_execution/slack_automation/slack_bolt_app.py --mode socket-mode
```
