# MAS AI Labs — Automated Slack Standup & Living Sprint Engine
## Technical Specification & Operational Blueprint

**Document Version**: 1.0  
**Target Start Date**: September 1, 2026  
**Primary Consumers**: Gaurav (CTO), Yashvi (AI PM + FDE), MAS AI Labs Engineering & Product Pod  
**Main Slack Channel**: `#all-mas-ai-labs`  
**Daily Standup Cadence**: 8:00 PM IST (Google Meet) | **Bot Trigger**: 7:00 PM IST  

---

## 📌 1. Executive Summary: What We Are Building & Why

### The Problem
* The MAS AI Labs team operates in a **remote, dual-speed model** (part-time/flexible working schedules across different locations).
* Chasing daily updates manually in group channels creates **noise, message bombardment, and administrative fatigue**.
* Status updates in chat channels often get lost and fail to update the **actual engineering sprint documents** and **monthly milestone trackers**.

### What We Are Building
An automated, lightweight **Slack Standup & Living Sprint Sync Bot** that:
1. **Eliminates Group Spam**: DMs individual task owners privately at **7:00 PM IST** with *only* their scheduled deliverables for the day.
2. **Takes < 45 Seconds per Person**: Provides a consolidated single-screen card with **quick dropdowns** (Status & RAG) and an optional 1-line note for blockers.
3. **Prepares the 8:00 PM Standup**: Posts a single, high-signal **Pre-Standup Digest** at **7:45 PM IST** in `#all-mas-ai-labs` highlighting completed work and active blockers.
4. **Captures Post-Standup Highlights**: Enables the PM/Lead to log key decisions and action items from the 8:00 PM call directly into Slack and the active sprint document.
5. **Maintains Living Sprint Documents**: Automatically updates `SPRINT_0X_WEEK_0X.md` tables, logs daily updates, and rolls over spill-over tasks during weekend sprint planning.

---

## ⏰ 2. End-to-End Daily & Weekly Lifecycle

```
┌────────────────────────────────────────────────────────────────────────┐
│                   DAILY SLACK STANDUP TIMELINE                         │
├────────────────────────────────────────────────────────────────────────┤
│ 7:00 PM IST ──► [Personalized DM Dispatched]                           │
│                 Bot checks date, reads active SPRINT_0X_WEEK_0X.md,    │
│                 and sends a private DM to each assigned owner.         │
│                                                                        │
│ 7:00–7:40 PM ─► [Frictionless Update Submission]                       │
│                 Teammates submit their 45-second update via dropdowns: │
│                 • Status: [x] Done | [-] In Progress | [!] Blocked     │
│                 • RAG:    🟢 Green | 🟡 Amber | 🔴 Red                 │
│                 • Quick Note: Deliverable link or blocker description  │
│                                                                        │
│ 7:45 PM IST ──► [Pre-Standup Digest in #all-mas-ai-labs]               │
│                 Single aggregated summary posted to the main group:    │
│                 • Completed deliverables today                         │
│                 • Flagged Blockers & Delays (Amber/Red)                │
│                 • Direct Google Meet link for the 8:00 PM call         │
│                                                                        │
│ 8:00 PM IST ──► [Live Standup Call (Google Meet)]                      │
│                 Focused 20-min discussion to align and unblock tasks.  │
│                 Google Meet Gemini AI automatically records call notes.│
│                                                                        │
│ 8:20 PM IST ──► [Google Meet Gemini Notes Received by Email]          │
│                 Gemini sends automated meeting notes & action items to │
│                 the team mail ID.                                      │
│                                                                        │
│ 8:25 PM IST ──► [Post-Standup Day Highlights Published]                │
│                 Command: /standup-notes (or automated email webhook).  │
│                 Bot extracts key decisions & action items from Gemini  │
│                 notes, posts the official Day Highlights to            │
│                 #all-mas-ai-labs, and appends to the Sprint Doc.       │
│                                                                        │
│ Sat/Sun Aft. ─► [Weekend Sprint Rollover & Next Sprint Planning]       │
│                 Command: /sprint-rollover                              │
│                 Incomplete/delayed items automatically rolled over to  │
│                 the next sprint document as marked [Rollover] tasks.   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ 3. Detailed Step-by-Step Functional Specifications

### Step 1: 7:00 PM IST — Personalized Direct Messages (No Channel Spam)
* The bot runs dynamically, mapping the current date to the active sprint document:
  * **Sprint 1 (Week 1)**: Sept 1 (Tue) – Sept 4 (Fri)
  * **Sprint 2 (Week 2)**: Sept 7 (Mon) – Sept 11 (Fri)
  * **Sprint 3 (Week 3)**: Sept 14 (Mon) – Sept 18 (Fri)
  * **Sprint 4 (Week 4)**: Sept 21 (Mon) – Sept 30 (Wed)
* It queries today's active tasks and sends a private DM to each owner.
* **The Single-View DM Card Contains**:
  * Greeting + Standup reminder for 8:00 PM.
  * List of today's assigned tasks (ID + Title + Expected Outcome).
  * A single **`[⚡ Submit Today's Update]`** button opening one consolidated modal.

### Step 2: 7:00 PM – 7:40 PM IST — The 45-Second Teammate Update Modal
* **Modal Fields**:
  1. **Task Status (Dropdown)**: `✅ Done / Completed` | `⏳ In Progress` | `🚨 Blocked / Delayed`
  2. **RAG Indicator (Dropdown)**: `🟢 Green (On Track)` | `🟡 Amber (At Risk)` | `🔴 Red (Blocked)`
  3. **Completed Deliverable / PR Link (Optional Text)**: e.g. `PR #14 merged / Scope v1 doc ready`
  4. **Blocker / Dependency (Optional Text)**: e.g. `Waiting for GCP service account permissions`
  5. **Time Sink / Key Focus (Optional Text)**: What took the most deep-work time today?
* Clicking **"Submit"** immediately writes data to `SPRINT_0X_WEEK_0X.md`.

### Step 3: 7:45 PM IST — Pre-Standup Digest Card in `#all-mas-ai-labs`
* Aggregates all submissions into a single visual Block Kit card posted to `#all-mas-ai-labs`:
  * **Header**: `📊 MAS AI Labs — Standup Summary (Sprint X | Day Y)`
  * **Progress Bar**: `4 / 6 tasks completed today`
  * **🚨 Discussion Items**: Highlights only Amber/Red items with the blocker description and owner.
  * **Join Standup Button**: Direct link to the 8:00 PM Google Meet.

### Step 4: 8:25 PM IST — Post-Standup Day Highlights & Call Decisions
* After the 8:00 PM Google Meet call, the PM/Lead runs `/standup-notes`:
  * Pops up a modal: `Enter Post-Standup Highlights & Action Items`.
  * The bot posts the formatted **Day Highlights** to `#all-mas-ai-labs`.
  * Appends the summary directly under `## 📝 Daily Quick Updates Log` in `SPRINT_0X_WEEK_0X.md`.

### Step 5: Saturday / Sunday Afternoon — Living Sprint Rollover
* During weekend sprint planning, the lead executes `/sprint-rollover <from_sprint> <to_sprint>` (e.g. `/sprint-rollover 1 2`):
  * Scans the previous sprint file for uncompleted or delayed tasks.
  * Appends them into the upcoming sprint file under `### 🔄 Rollover Tasks from Sprint X`.
  * Preserves original task history while ensuring no deliverable is forgotten.

---

## 📋 4. Required Configuration & Information Checklist

To deploy and run the bot in the live pod, the following details are required:

| Configuration Item | Value / Description | Status |
|---|---|:---:|
| **Main Slack Channel** | `#all-mas-ai-labs` | ✅ Confirmed |
| **Bot DM Trigger Time** | `7:00 PM IST` (Monday – Friday) | ✅ Confirmed |
| **Standup Digest Time** | `7:45 PM IST` (in `#all-mas-ai-labs`) | ✅ Confirmed |
| **Daily Standup Call** | `8:00 PM IST` (Google Meet) | ✅ Confirmed |
| **Weekend Rollover Window** | Saturday / Sunday Afternoon | ✅ Confirmed |
| **Standup Google Meet URL** | `[Provide Permanent Meeting Link]` | ⏳ Needed |
| **Slack App Credentials** | `SLACK_BOT_TOKEN` (`xoxb-...`) & `SLACK_APP_TOKEN` (`xapp-...`) | ⏳ Needed |
| **Teammates Slack IDs** | Member IDs for: Gaurav, Shubham, Rohan, Prakhar, Yashvi | ⏳ Needed |

---

## ⚙️ 5. Technical Architecture & Slack Permissions

### Socket Mode Architecture (Zero Public Infrastructure / No ngrok)
The bot uses **Slack Bolt for Python** running in **Socket Mode**:
* Outbound WebSocket connection securely connects to Slack's servers.
* **No public IP, ngrok tunnel, or open firewall ports required**.
* Can run on any local machine, cloud VM, or container.

### Slack App OAuth Scopes (Included in `slack_app_manifest.json`)
* `chat:write` — Post cards and messages to channels and DMs.
* `chat:write.public` — Post to `#all-mas-ai-labs` without manual bot invitation.
* `im:write` / `im:history` — Send and receive 1-on-1 direct messages with teammates.
* `commands` — Register `/standup`, `/standup-notes`, `/sprint-summary`, and `/sprint-rollover`.
* `users:read` — Resolve teammate member IDs.

---

## 📖 6. Summary of Discussions & Key Product Decisions

1. **Anti-Agency 30% Guardrail**: Ad-hoc MAS support work is capped at maximum 20–30% total team effort (split equally: 15% Shubham / 15% Rohan).
2. **Zero Channel Spam**: Teammates receive clean, private DMs; the main channel receives only 2 high-signal posts per day (7:45 PM Pre-Standup Digest + 8:25 PM Post-Standup Highlights).
3. **Living Document Sync**: Markdown files are the single source of truth. The bot acts as the bridge between Slack and git.
4. **Calendar Alignment**: All 4 sprints are synchronized with the exact September 2026 calendar (Month 1 kicks off **Tuesday, September 1**).
5. **Weekend Rollovers**: Sprint rollovers and spill-over evaluations occur on **Saturday/Sunday afternoon** to prepare the clean board before Monday kickoff.
