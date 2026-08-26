# Student Dashboard — Central Mission Control Specification

**Module/Feature**: `Student Dashboard (Primary Learning Command Center)`  
**Status**: `DRAFT (Ready for Team Review)`  
**Document Type**: High-Level Product Feature Document  
**Scope Definition**:
* **Current Immediate Scope (Phase 1: 15–20 Days)**: The core centralized hub connecting `Mr. Learn` and `Mr. Test` — minimalist welcome greeting, 4-slot telemetry grid, dual-state experience (Day-1 First-Time vs. Returning Student), optional lightweight tour, and notification drawer.
* **Future Long-Term Scope (Phase 2)**: AI study recommendations, peer leaderboards, and placement drive eligibility widgets.

---

## 1. Product Overview & Architectural Role

The **Student Dashboard** (`portal.institution.edu`) is the **single landing page and primary mission control room** for all enrolled learners. It synthesizes real-time progress from **Mr. Learn (Coursework LMS)** and **Mr. Test (Assessments & Exams)** into a clean, 4-slot dashboard.

### 🌐 Key Architectural Principles:
1. **The Dashboard IS the Home Page**: The institutional logo in the header acts as the 1-click home anchor. There is no redundant secondary "Home" page.
2. **Zero Clutter**: Search bars and unnecessary sidebars are stripped to keep students 100% focused on active learning and assessment deadlines.
3. **Seamless Silent Transition**: Clicking any card smoothly transitions into `Mr. Learn` or `Mr. Test` without a secondary login prompt.

---

## 2. Universal Header & Top Bar

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [LOGO] INSTITUTION CREST                                             [🔔(2)] [👤 Yashvi▼]│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

1. **Left: Institutional Crest / Logo**: White-labeled per client institution (e.g. Chitkara University). Clicking this logo always navigates back to the Dashboard home.
2. **Right-Hand Utility Cluster**:
   - **`🔔 Notification Bell`**: Opens a clean slide-out drawer showing active test deadlines, newly assigned modules, and discussion replies.
   - **`👤 Master Avatar Menu`**:
     - `Student Full Name & Institutional Email`
     - `📄 Master Profile & Settings` (`/student/profile`)
     - `📜 Learning Transcript & Completed Records`
     - `🌗 Theme Toggle (Light / Dark / System)`
     - `🚪 Log Out`

---

## 3. The Minimalist Welcome Banner

Positioned directly below the top header, this section gives the student instant personal and institutional context:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  👋 Welcome back, Yashvi!                                                              │
│  🎓 Chitkara University • B.Tech CSE (Batch of 2028)                                   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

* **Personalized Greeting**: Time-aware greeting (`Welcome back, [First Name]!` / `Welcome, [First Name]!`).
* **Institution & Cohort Subtitle**: Clean badge displaying the client institution name and the student's assigned academic batch/branch.

---

## 4. The 4-Slot Dashboard Grid (Layout Blueprint)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                        │
│  ┌──────────────────────────────────────────┐  ┌────────────────────────────────────┐  │
│  │ 📚 SLOT 1: Coursework & Learning LMS     │  │ 🏆 SLOT 2: Overall Standing & Score│  │
│  │ (Powered by Mr. Learn)                   │  │ (Cohort Benchmark & Readiness)     │  │
│  │                                          │  │                                    │  │
│  │ Enterprise Systems & Architecture        │  │ Batch Standing: Top 15% (#14 / 120)│  │
│  │ Progress: [██████████████░░░░] 75%       │  │ Readiness Score: 78 / 100          │  │
│  │ Next: 3.2 System Architecture (18m)      │  │ Competency: Quant 80% • SQL 75%    │  │
│  │ [ ▶ RESUME COURSEWORK ➔ ]                │  │ [ 📊 View Performance Insights ➔ ] │  │
│  └──────────────────────────────────────────┘  └────────────────────────────────────┘  │
│                                                                                        │
│  ┌──────────────────────────────────────────┐  ┌────────────────────────────────────┐  │
│  │ 📝 SLOT 3: Upcoming Quizzes & Tests      │  │ 📊 SLOT 4: Recent Results & Review │  │
│  │ (Powered by Mr. Test)                    │  │ (Scorecards & Diagnostic Gaps)     │  │
│  │                                          │  │                                    │  │
│  │ test-exam-2: Comprehensive Benchmark     │  │ Recent Test: test-exam-1           │  │
│  │ 30 Questions • 60 Mins • Due Aug 31      │  │ Score: 13 / 40 (Accuracy: 88%)     │  │
│  │ [ 🚀 LAUNCH ASSESSMENT ➔ ]               │  │ Weak Spot: Python Recursion (<50%) │  │
│  │                                          │  │ [ 📄 View Solutions & Analysis ➔ ] │  │
│  └──────────────────────────────────────────┘  └────────────────────────────────────┘  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. First-Time Student (Day 1) vs. Returning Student State

```
┌────────────────────────────────────────────────────────────────────────┐
│                   DUAL-STATE DASHBOARD EXPERIENCE                      │
├────────────────────────────────────────────────────────────────────────┤
│  STATE A: FIRST-TIME STUDENT (Day 1 / Zero Progress)                   │
│  STATE B: RETURNING STUDENT (Active Learning Journey)                  │
└────────────────────────────────────────────────────────────────────────┘
```

| Slot Component | First-Time Student (Day 1 / 0% Progress) | Returning Student (In-Progress) |
| :--- | :--- | :--- |
| **Welcome Banner** | `👋 Welcome, Yashvi! • Chitkara University • B.Tech CSE (Batch of 2028)` | `👋 Welcome back, Yashvi! • Chitkara University • B.Tech CSE (Batch of 2028)` |
| **Slot 1: Coursework** | Shows Module 1.1 Orientation with `0%` progress bar + **`[ 🚀 START COURSEWORK ➔ ]`**. | Shows active course with live progress % and next lesson + **`[ ▶ RESUME COURSEWORK ➔ ]`**. |
| **Slot 2: Standing & Score** | Shows `Baseline Pending` badge: *"Complete a quiz or module to establish your starting batch rank!"* | Displays live **Readiness Score (78/100)** + **Cohort Standing (Top 15%)** + Skill Breakdown. |
| **Slot 3: Upcoming Tests** | Shows scheduled **Sample Practice Quiz** (10 Qs • 15 Mins) + **`[ 📝 TRY PRACTICE QUIZ ➔ ]`**. | Displays active test deadline (`test-exam-2`) with countdown + **`[ 🚀 LAUNCH ASSESSMENT ➔ ]`**. |
| **Slot 4: Results & Review** | Shows educational placeholder: *"Your test scorecards and weak-topic analysis will appear here."* | Displays latest scorecard (`13/40`) + sectional weak spot tags + **`[ 📄 View Solutions ]`**. |

---

## 6. Optional Day-1 Lightweight Dashboard Tour

To onboard new students without annoying modal wizards, the platform supports a **Lightweight 3-Spotlight Tooltip Tour**:

```
┌─────────────────────────────────────────────────────────┐
│  💡 Welcome to your Learning Hub!                       │
│  Step 1 of 3: Start your assigned coursework right here.│
│                                                         │
│  [ Skip Tour ]                         [ Next Step ➔ ]  │
└─────────────────────────────────────────────────────────┘
```

* **Step 1 Beacon (Slot 1)**: *"Start your video coursework and track lecture progress here."*
* **Step 2 Beacon (Slot 3)**: *"Check your upcoming quizzes, mid-terms, and deadlines here."*
* **Step 3 Beacon (Slot 2 & 4)**: *"View your performance scorecards, batch rank, and weak spots here."*
* **1-Click Dismissal**: Fully dismissible in 1 click (`[ Skip Tour ]`), never shown again once completed.

---

## 7. Current vs. Target State Gap Analysis Matrix

| Feature Dimension | Legacy Experience | Target White-Label State | Gap Classification | Implementation Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **Unified Command Center** | Disconnected websites for LMS and Exams. | **Single 4-Slot Unified Dashboard**. | 🔴 **Critical UX Fix** | Build responsive Next.js grid pulling telemetry from `mrlearn` and `ezexam`. |
| **Authentication Flow** | Separate logins required for different modules. | **Silent SSO Token Handshake** across all cards. | 🔴 **Critical UX Fix** | Session token carries authenticated context on 1-click CTA launch. |
| **First-Time Student State** | Empty grey screens with missing data errors. | **Actionable Day-1 State** (Module 1.1 + Sample Practice Quiz). | 🟡 **UX Polish** | Render dedicated onboarding defaults when progress count equals 0. |
| **Visual Hierarchy** | Cluttered with search boxes and sidebars. | **Minimalist Banner + 4 Focused Cards**. | 🟢 **Core Design** | Standardized card containers with clear primary action buttons. |

---

## 8. Current Immediate Scope vs. Future Long-Term Scope

```
┌────────────────────────────────────────────────────────────────────────┐
│                   DUAL-SPEED SCOPE & EXECUTION ROADMAP                 │
├────────────────────────────────────────────────────────────────────────┤
│  🎯 CURRENT SCOPE (Next 15–20 Days — Client Handover Ready)            │
│     Minimalist welcome header, 4-slot telemetry grid, dual-state flow, │
│     sample practice quiz link, and silent SSO module transitions       │
│                                                                        │
│  🚀 FUTURE SCOPE (Long-Term Scalable Engine)                           │
│     AI study pace predictor, campus recruitment drive widgets, and     │
│     batch-wide live competitive leaderboards                           │
└────────────────────────────────────────────────────────────────────────┘
```

| Feature Area | Current Immediate Scope (Next 15–20 Days)<br>*(Keep it Very Basic & Client-Ready)* | Future Long-Term Scope<br>*(Iterative Platform Enhancements)* |
| :--- | :--- | :--- |
| **Top Navigation** | Institutional Logo (Home Anchor) + Notification Bell + Avatar Menu (Zero search bar). | Global AI semantic search across transcripts, quizzes, and documentation. |
| **Welcome Area** | Clean 2-line greeting: `Welcome back, [Name]! • [Institution] • [Batch]`. | Dynamic daily streak counter + personalized learning milestone progress. |
| **Slot 1 (Learn)** | Active course progress bar + next lesson + 1-click resume button. | Multi-course carousel switcher + personalized lecture recommendations. |
| **Slot 2 (Standing)**| Overall Readiness Score (0–100) + Cohort Percentile / Rank. | Batch-wide interactive leaderboard + historical skill growth curves. |
| **Slot 3 (Tests)** | Active upcoming exam deadline + Sample Practice Quiz for new learners. | Adaptive diagnostic test generator + calendar scheduling sync. |
| **Slot 4 (Results)** | Latest test scorecard + sectional scores + weak spot tag (`< 50% accuracy`). | Automated AI video study playlist generated from incorrect test answers. |

---

## 9. Open Product Questions & Discussion Points

The following items are flagged for team review:

### 📌 Open Point 1: Readiness Score Algorithm (Slot 2)
* Determine the exact weighting formula for the **Readiness Score (0–100)** (e.g. 50% Course Completion + 50% Assessment Accuracy).

### 📌 Open Point 2: Sample Practice Quiz Availability (Slot 3)
* Confirm whether the **Sample Practice Quiz** should be a standardized 10-question general aptitude test provided by our academic team for all new batches.

### 📌 Open Point 3: Notification Push Channels
* In addition to the top-bar notification drawer, determine if critical exam deadlines should also trigger WhatsApp template reminders.
