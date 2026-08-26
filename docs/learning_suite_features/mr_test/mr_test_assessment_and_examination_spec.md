# Mr. Test — Assessment & Examination Engine Specification

**Module/Feature**: `Mr. Test (Assessments & Proctored Examination Engine)`  
**Status**: `DRAFT (Ready for Team Review)`  
**Document Type**: High-Level Product Feature Document  
**Scope Definition**:
* **Current Immediate Scope (Phase 1: 15–20 Days)**: Enhancing the current assessment engine for immediate client handover — single silent sign-on, clean "Online Exams" portal, zero-ad white-labeling, MCQ assessment player with section-wise negative marking, instant scorecards, and Student/Admin dashboard integration.
* **Future Long-Term Scope (Phase 2)**: In-house coding sandbox (Python/SQL/Java runner), AI-driven proctoring (webcam & dual-screen detection), automated percentile benchmarking, and adaptive testing.

---

## 1. Product Overview & Market Segments

`Mr. Test` is the core evaluation, benchmarking, and proctored examination engine of our B2B Learning Suite. It delivers structured diagnostic tests, weekly module quizzes, mid-term evaluations, and recruitment screening assessments across our 4 core client domains:

### 🌐 The 4 Core Educational & Enterprise Segments:
```
┌────────────────────────────────────────────────────────────────────────┐
│             THE 4 DIVERSE B2B EVALUATION & ASSESSMENT DOMAINS          │
├────────────────────────────────────────────────────────────────────────┤
│  1. Enterprise Workforce Upskilling & Corporate Training Partners      │
│  2. Online Higher Ed Aggregators & Distance Learning Portals           │
│  3. Universities, Engineering & Management Colleges                    │
│  4. Placement Bootcamps, Finishing Schools & Test-Prep Academies       │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Enterprise Workforce Upskilling & Corporate Training**:
   - Evaluates technical competence (e.g. ERP, Cloud, Software) with granular sectional scorecards to prove training ROI to corporate managers.
2. **Online Higher Ed Aggregators & Digital Universities**:
   - Delivers timed, proctored semester mid-terms and final examinations with authenticated student identity logs.
3. **Universities & Engineering Colleges**:
   - Delivers internal assessments, lab quizzes, and semester benchmark tests with automatic negative marking calculations.
4. **Placement Bootcamps & Finishing Schools**:
   - Delivers high-intensity placement aptitude screening (Quant, LRDI, Verbal, Technical Coding MCQs) to rank students for recruitment drives.

---

## 2. End-to-End User Experience & Assessment Journey

```
┌────────────────────────────────────────────────────────────────────────┐
│                   MR. TEST: 4-STAGE ASSESSMENT JOURNEY                 │
├────────────────────────────────────────────────────────────────────────┤
│  Stage 1: Silent SSO & Discovery ──► Dashboard Slot 2 / Online Exams   │
│  Stage 2: Pre-Exam Rules Modal   ──► Instructions & Palette Legend     │
│  Stage 3: Live Assessment Canvas ──► MCQ Player, Palette Grid & Timer  │
│  Stage 4: Instant Submission     ──► Sectional Scores & Review Link    │
└────────────────────────────────────────────────────────────────────────┘
```

---

### 2.1 The Authentication Contrast & Seamless SSO Fix
* **Current Operational Reality**:
  - While `Mr. Learn` supports direct authenticated transition from the current student dashboard, **`Mr. Test` currently forces the student to log in again with separate credentials** on `ezexam.in`.
  - For the upcoming client demos, **the rest of the EzExam platform (test canvas, questions, negative marking, timer) is completely demoable as-is**.
  - Therefore, **the primary critical deliverable for Mr. Test in the current scope is fixing this secondary login** via a **Silent SSO Handshake** so students launch exams directly from Dashboard Slot 2 without entering credentials. Deeper UI/UX revamps will be phased into later versions.

---

### 2.2 Universal Top Header & Navigation
Across all pages in `Mr. Test`, the platform maintains the **standardized institutional header**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [LOGO] INSTITUTIONAL PORTAL   [ 🏠 Home / Dashboard ]   [ 📚 My Courses ]   [ 📝 Exams ]│
│                                           [ 🔍 Search assessments... ]     [👤 Alex M. ▼]│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

* **🏠 [ Home / Dashboard ] Link**: Instant 1-click return to the primary Student Dashboard (`portal.institution.edu/student/dashboard`).
* **👤 Master Avatar Dropdown**: Shared single source of truth (`Master Profile`, `Learning History`, `Theme`, `[ 🚪 Log Out ]`).

---

### 2.3 Screen 1: Online Exams Hub (`/online-exams`)
A clean, focused assessment portal dividing tests into **two distinct operational buckets**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 📝 ONLINE EXAMS & ASSESSMENTS                                                          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 🟢 OPEN & UPCOMING EXAMS (Active Deadlines)                                            │
│ ┌────────────────────────────────────────────────────────────────────────────────────┐ │
│ │ test-exam-2: Comprehensive Diagnostic Benchmark                                   │ │
│ │ • 30 Questions  • 60 Mins Duration  • 120 Total Marks (Quant, LRDI, SQL, Python)   │ │
│ │ • Window: Starts Aug 21, 2026 ➔ Start Before Aug 31, 2026, 11:59 PM                │ │
│ │ [ 🚀 START EXAM ➔ ]                                                                │ │
│ └────────────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                        │
│ 📋 RECENT EXAMS (Submitted in the last 2 weeks)                                        │
│ ┌──────────────────────────────────────┐ ┌───────────────────────────────────────────┐│ │
│ │ test-exam-1 (Weekly-Test)            │ │ test-exam-2 (Diagnostic Test)             ││ │
│ │ 40 Questions • 60 Mins • 40 Marks    │ │ 30 Questions • 60 Mins • 120 Marks        ││ │
│ │ Submitted: Aug 25, 2026, 6:39 PM     │ │ Submitted: Aug 25, 2026, 6:45 PM          ││ │
│ │ Total Score: 13 / 40 (32.5%)         │ │ Total Score: 1 / 120                      ││ │
│ │ • Myanalyticsschool: 13 / 40         │ │ • Quant: -4/36  • LRDI: 1/36  • SQL: 3/12 ││ │
│ │ [ 📊 View Analysis & Solutions ➔ ]   │ │ • Python: -3/12 • ML: 2/12   • DI: 2/12   ││ │
│ │                                      │ │ [ 📊 View Analysis & Solutions ➔ ]        ││ │
│ └──────────────────────────────────────┘ └───────────────────────────────────────────┘│ │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 2.4 Screen 2: Pre-Exam Instruction & Compliance Modal
Before the timer begins, students must review rules in a mandatory modal:

```
┌────────────────────────────────────────────────────────────────────────┐
│                 PLEASE READ INSTRUCTIONS CAREFULLY                     │
├────────────────────────────────────────────────────────────────────────┤
│  ⚠️ Exam Admin can see your Device details — Your actions are recorded! │
│                                                                        │
│  1. Select "Save & Next" to save your answer and go to next question.  │
│  2. Select "Mark for Review & Next" to flag question for later review. │
│  3. Select "Finish Exam" to submit your final responses.               │
│  4. You CANNOT pause this test once started.                           │
│  5. Please disable background notifications before proceeding.         │
│                                                                        │
│  OVERVIEW PALETTE LEGEND:                                              │
│  [ 🟢 Answered ]     [ 🔴 Not Answered ]     [ ⚪ Not Seen Yet ]       │
│  [ 🟣 Marked for Review ]  [ 🟣✓ Answered & Marked for Evaluation ]   │
│                                                                        │
│  [✓] I have read and understood all the instructions                   │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                     [ 🚀 START EXAM NOW ➔ ]                      │  │
│  └──────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────┘
```

---

### 2.5 Screen 3: Live Assessment Player Canvas (`/online-exams/:id`)
A focused, distraction-free examination environment:

```
┌────────────────────────────────────────────────────────────────────────┬─────────────────────┐
│ [LOGO] test-exam-2 | Section: [ QUANT ] [ LRDI ] [ SQL ] [ PYTHON ]    │ ⏱️ TIMER: 00:57:39   │
├────────────────────────────────────────────────────────────────────────┼─────────────────────┤
│ LEFT QUESTION CANVAS (75% Width)                                       │ RIGHT PALETTE (25%) │
│                                                                        │                     │
│ Q.No. 17: Which statement does NOT describe object encapsulation?      │ 1   2   3   4   5   │
│ A. It protects the data from outside modification.                     │ 6   7   8   9   10  │
│ B. A parent class is encapsulated and inherited by child classes.      │ 11  12  13  14  15  │
│ C. It keeps data and methods private inside a single unit.             │ 16 [17] 18  19  20  │
│ D. It only allows data to be changed through dedicated getters/setters.│ 21  22  23  24  25  │
│                                                                        │ 26  27  28  29  30  │
│ ┌────────────────────────────────────────────────────────────────────┐ │                     │
│ │ ( ) Option A     (•) Option B     ( ) Option C     ( ) Option D    │ │ [ 📄 Question Paper]│
│ └────────────────────────────────────────────────────────────────────┘ │ [ ℹ️ Instructions ] │
│                                                                        │                     │
│ [ 🟣 Mark for Review & Next ]                 [ 🔵 Save & Next ➔ ]     │ [ 🔴 SUBMIT EXAM ]  │
└────────────────────────────────────────────────────────────────────────┴─────────────────────┘
```

* **Sectional Navigation Tabs**: Switch effortlessly between exam sections (`Quant`, `LRDI`, `SQL`, `Python`).
* **Active Countdown Timer**: Persistent top-right countdown with auto-submit on expiry.
* **40-Question Visual Palette**: Color-coded grid showing real-time question statuses.
* **Proctoring Warning Shield**: Logs tab-switching and window defocus events.

---

### 2.6 Screen 4: Instant Result Popup & Deep Analysis (`/performance`)
* **Immediate Result Modal**: Displayed instantly upon clicking `[ Submit Exam ]`:
  - `Total Score`: e.g. `13 out of 40`
  - `Section Scores`: e.g. `Quant: 10/10 • Python: 3/30`
* **Deep Performance Analysis Suite (`/performance` & `/micro/:id`)**:
  - **Subject Analysis**: Marks breakdown per topic.
  - **Per-Question Time Analysis (Micro Analysis)**: Shows exact seconds spent per question vs. correct solution.
  - **Diagnostic Remediation ("Topics with Accuracy < 50%")**: Directly pinpoints weak areas (e.g. `Python List Comprehensions: -3 Marks`) for targeted revision.
  - **1-Click Solutions & Accuracy CSV Export**: Downloadable answer keys with explanations.

---

## 3. Student & Admin Dashboard Integration

### 🎓 3.1 Student Dashboard Integration (Slot 2: Top-Right Card)
On the Student Dashboard, `Mr. Test` drives **Slot 2**:

```
┌────────────────────────────────────────────────────────────────────────┐
│  ASSESSMENTS & BENCHMARKS (SLOT 2)                                     │
├────────────────────────────────────────────────────────────────────────┤
│  🔴 UPCOMING: test-exam-2 (Comprehensive Diagnostic Benchmark)         │
│  • 30 Questions • 60 Mins • 120 Marks (Quant, LRDI, SQL, Python)       │
│  • Due Before: Aug 31, 2026, 11:59 PM                                  │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                    [ 🚀 LAUNCH ASSESSMENT ➔ ]                    │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  📊 RECENT PERFORMANCE:                                                │
│  • test-exam-1: 13 / 40 (32.5%) [ 📄 View Breakdown ]                  │
│  • Diagnostic Weakness: Python (-3) • Quant (-4)                       │
└────────────────────────────────────────────────────────────────────────┘
```

---

### 👤 3.2 Admin Dashboard Integration (TPO / Dean / Corporate Trainer)

```
┌────────────────────────────────────────────────────────────────────────┐
│               MR. TEST: TRAINER & ADMIN EVALUATION CONSOLE             │
├────────────────────────────────────────────────────────────────────────┤
│  1. Batch Participation Tracker ──► Completed (84%) vs. Absent (16%)   │
│  2. Sectional Competency Heatmap──► Quant: 45% • SQL: 72% • Python: 28%│
│  3. Proctoring Anomaly Flags    ──► High tab-switch & speed anomalies  │
│  4. 1-Click Batch Scorecard CSV ──► Export full marks & ranks in 1 click│
│  5. 1-Click WhatsApp Test Nudge ──► Reminder to unattempted students   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Current vs. Target State Gap Analysis Matrix

| Feature Dimension | Current Platform (`ezexam.in`) | Target White-Label State | Gap Classification | Implementation Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **Authentication & SSO** | Disconnected standalone login with manual credentials. | **Silent Seamless SSO Handshake** from Dashboard Slot 2. | 🔴 **Critical UX Fix** | Generate single-use signed auth token on assessment launch. |
| **Third-Party Ads & Popups** | Contains Google AdSense scripts (`adsbygoogle.js`) & ad-blocker popups. | **100% Pure White-Label, Zero-Ad Platform**. | 🔴 **Critical Brand Fix** | Strip all external ad scripts and remove ad-blocker modals. |
| **Vendor Branding Leaks** | EzExam logos, footer links, and Android APK installation prompts. | **Pure Institutional Branding** (`portal.institution.edu/test`). | 🔴 **Critical Brand Fix** | Replace vendor assets with client crest and institutional header. |
| **Negative Marking Engine** | Built-in section-wise negative marking calculation. | **Supported & Surfaced on Scorecards**. | 🟢 **Existing Engine** | Retain existing scoring engine and display cleanly on dashboard. |
| **Question Palette Grid** | 5-state color-coded palette with timer. | **Modernized Responsive Palette Canvas**. | 🟡 **UX Polish** | Clean CSS restyling with responsive layout for all screen sizes. |
| **Question Micro-Analysis** | Granular time spent per question and accuracy reports. | **Unified Scorecard View** with instant weak-topic tags. | 🟡 **UX Polish** | Consolidate 4 separate analysis pages into a single tabbed scorecard. |
| **Admin Reporting** | Basic batch results view. | **1-Click Batch Scorecard CSV & Competency Heatmaps**. | 🟢 **Low-Effort Build** | Expose CSV download endpoint containing all student sectional scores. |

---

## 5. Current Immediate Scope vs. Future Long-Term Scope

```
┌────────────────────────────────────────────────────────────────────────┐
│                   DUAL-SPEED SCOPE & EXECUTION ROADMAP                 │
├────────────────────────────────────────────────────────────────────────┤
│  🎯 CURRENT SCOPE (Next 15–20 Days — Client Handover Ready)            │
│     Silent SSO login, clean white-label wrapper, MCQ test player with  │
│     negative marking, instant scorecards, and Dashboard Slot 2 sync    │
│                                                                        │
│  🚀 FUTURE SCOPE (Long-Term Scalable Engine)                           │
│     Interactive Coding Sandbox (Python/SQL/Java), AI proctoring        │
│     (webcam & eye-tracking), and adaptive difficulty benchmarking      │
└────────────────────────────────────────────────────────────────────────┘
```

| Feature Area | Current Immediate Scope (Next 15–20 Days)<br>*(Keep it Very Basic & Client-Ready)* | Future Long-Term Scope<br>*(Iterative Platform Enhancements)* |
| :--- | :--- | :--- |
| **Authentication** | **Silent SSO Handshake**: 1-Click launch from Dashboard Slot 2 with zero double login. | Unified single-session cookie across all subdomains. |
| **Test Delivery Engine** | White-label MCQ player with section tabs, countdown timer, and 40-grid palette. | **Interactive Coding Sandbox**: In-browser compiler & testcase runner for Python, SQL, C++, Java. |
| **Scoring & Marks** | Sectional scores with negative marking support (e.g. `Quant: -4/36`, `SQL: 3/12`). | AI-driven candidate ranking, percentile benchmarking, and percentile curves. |
| **Scorecard & Analytics** | Instant score popup + Recent Exams card with weak spot flags. | Automated remedial video recommendation linking weak topics to `Mr. Learn`. |
| **Proctoring & Integrity** | Basic browser tab-switch warning and device logging. | **AI Proctoring**: Webcam face verification, dual-screen detection, and audio anomaly alerts. |
| **Admin Controls** | 1-Click downloadable Batch Results CSV + unattempted student reminder nudges. | Live exam monitoring dashboard with real-time candidate proctoring video streams. |

---

## 6. Strategic Architecture Note: Delivery Evolution

> [!NOTE]
> **DELIVERY EVOLUTION & EZEXAM ROADMAP NOTE**  
> * **Short-Term Scope (Next 15–20 Days Pilot Handover)**: EzExam will remain as the underlying assessment delivery engine for the immediate pilot goals. We will streamline the user experience, eliminate the secondary login screen via silent SSO, strip all third-party ad scripts, and present a clean white-labeled interface.  
> * **Long-Term Scope (Future In-House Engine)**: We will plan to systematically transition away from EzExam and build our proprietary in-house evaluation and coding sandbox engine. Once built in-house, the platform will achieve **100% pure white-labeling** with integrated AI proctoring and coding compilers.

---

## 7. Open Product Questions & Discussion Points

The following items are flagged for team alignment:

### 📌 Open Point 1: Negative Marking Customization per Client
* Should the negative marking penalty (e.g. $-1$ for incorrect MCQ) be customizable per assessment by client admins, or strictly standardized by our academic team?

### 📌 Open Point 2: Coursework Gating Enforcement (`Mr. Learn` $\rightarrow$ `Mr. Test`)
* Should test access be strictly locked until the student achieves $\ge 75\%$ progress in the corresponding `Mr. Learn` track, or should client admins have an override toggle?

### 📌 Open Point 3: Immediate Score Release vs. Scheduled Publication
* Should student scorecards be visible immediately upon submission (as currently shown in Screenshot 2), or should client admins have the option to withhold scores until the entire batch deadline passes?
