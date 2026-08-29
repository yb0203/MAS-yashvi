# College Admin Dashboard — Operations & Institutional Governance Specification

**Module/Feature**: `College Admin Dashboard (Institutional Operations Console)`  
**Status**: `DRAFT (Ready for Team Review)`  
**Document Type**: High-Level Product Feature Document  
**Scope Definition**:
* **Current Immediate Scope (Phase 1: 15–20 Days)**: Low-touch operational control suite — flexible roster management (Bulk CSV upload + Single-Student manual entry), licensed course catalog allocation, scheduled exam window manager, 1-click student ticket resolution hub, automated WhatsApp/Email reminders, and batch exam scorecard CSV export.
* **Future Long-Term Scope (Phase 2)**: Self-serve AI Course & Quiz Creation Studio, automated executive summary PDF generator, and advanced skill growth analytics.

---

## 1. Product Overview & Core Operating Philosophy

The **College Admin Dashboard** (`admin.institution.edu`) is the institutional command center for Deans, Department Heads, Placement Officers (TPOs), and Corporate Training Leads.

### 🏛️ The "Zero Operational Overhead" Philosophy
* **No Extra Staff Required**: Designed specifically so that an existing coordinator or faculty member can manage the entire institution's learning and assessment operations in **under 5 minutes a week**.
* **Exception-Based Attention**: Admins do not need to sit and monitor screens all day. The system automates routine student reminders and only alerts admins when an action is required (e.g. pending student tickets).
* **Licensed Catalog Distribution**: Institutions receive access to **curated, pre-packaged course tracks and question banks** provided by our in-house academic team, which admins can allocate to their batches with zero authoring burden.

---

## 2. Content & Evaluation Sourcing Models

```
┌────────────────────────────────────────────────────────────────────────┐
│             CONTENT & EVALUATION SOURCING ARCHITECTURE                 │
├────────────────────────────────────────────────────────────────────────┤
│  MODEL 1 (Current Core): In-House Academic Delivery                   │
│  • Our in-house team curates gold-standard video tracks & quiz banks. │
│  • Institution receives licensed access to specific courses.           │
│  • Admin simply maps licensed courses/tests to target student batches. │
│                                                                        │
│  MODEL 2 (Future Scope): AI Course & Quiz Creation Studio              │
│  • Self-serve AI-powered authoring tools for faculty/trainers.         │
│  • Upload syllabus/PDFs ➔ Auto-generate modules, videos & quiz banks.  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Exhaustive Step-by-Step Admin Action Workflows

```
┌────────────────────────────────────────────────────────────────────────┐
│                   THE 5-STEP ADMIN WORKFLOW LIFECYCLE                  │
├────────────────────────────────────────────────────────────────────────┤
│  1. Roster Provisioning  ──► Bulk CSV Upload OR Single Student Add     │
│  2. Course Allocation    ──► Assign Licensed Tracks to Batches         │
│  3. Exam Scheduling      ──► Set Non-Conflicting Test Windows          │
│  4. Automated Reminders  ──► System Auto-Nudges Lagging Students       │
│  5. Ticket & Score Hub   ──► 1-Click CGPA Approval & Scorecard CSV     │
└────────────────────────────────────────────────────────────────────────┘
```

---

### 🚀 Action 1: Flexible Student Roster Provisioning (Bulk + Single-Entry)
* **Goal**: Enable effortless onboarding whether an admin is adding a batch of 500 students or a single late-admitted student.
* **Dual Provisioning Methods**:
  1. **Bulk Excel/CSV Upload**: Admin drops the college master sheet (`Name`, `Email`, `Roll No`, `Branch`). System auto-validates and provisions 100+ accounts in seconds.
  2. **Single-Student Manual Entry (`+ Add Single Student`)**: If a new student joins late or changes sections, the admin simply fills a quick 4-field modal (`Name`, `Email`, `Roll No`, `Batch`) without needing to re-upload the entire batch CSV.

---

### 📚 Action 2: Licensed Course Track Allocation (Mr. Learn)
* **Goal**: Zero course authoring friction for college staff.
* **Workflow**:
  - The institution's license unlocks specific pre-packaged tracks curated by our academic team (e.g. *Enterprise Systems Track*, *Placement Aptitude Track*).
  - Admin clicks **`[ Allocate Course ]`** ➔ Selects Licensed Track ➔ Selects Target Batch (`B.Tech CSE 2028`) ➔ Clicks **`[ Confirm ]`**.
  - All students in that batch instantly receive the course in their Student Dashboard Slot 1.

---

### 📅 Action 3: Zero-Conflict Exam Window Scheduling (Mr. Test)
* **Goal**: Empower college admins to coordinate exam timing so tests never clash with internal semester exams.
* **Workflow**:
  - Admin browses pre-packaged question banks / tests provided by our academic team (e.g. `Weekly-Test-1` or `Mid-Term Diagnostic`).
  - Sets the **Active Assessment Window**:
    - *Start Date/Time*: `Aug 29, 2026 • 9:00 AM`
    - *End Date/Time*: `Aug 31, 2026 • 11:59 PM`
  - Clicks **`[ Publish Schedule ]`**.
  - Students see the upcoming test in their Dashboard Slot 3 with a live countdown timer.

---

### 🤖 Action 4: Fully Automated Student Reminder Engine
* **Goal**: Admins should NEVER have to manually track down students or send individual reminder emails.
* **Automated Workflow**:
  - The platform's automated notification service automatically monitors deadlines:
    - **T-48 Hours Alert**: Sends automated WhatsApp / Email reminder to unattempted students.
    - **T-12 Hours Final Call**: Sends urgent notification to students who have not started.
  - The admin dashboard displays a clean live status card: *"82% Completed • 18 Students Auto-Nudged via WhatsApp"*.

---

### 🎫 Action 5: Student Ticket Resolution Hub (CGPA / Identity Corrections)
* **Goal**: Resolve student profile updates without chaotic email chains.
* **Workflow**:
  - When a student requests a profile update (e.g. correcting a CGPA from `8.20 ➔ 8.65` with an attached grade sheet PDF), a ticket appears in the admin's **Pending Tickets Queue**.
  - Admin clicks **`[ ✅ Approve ]`** (instantly updates student's locked master record) or **`[ ❌ Reject with Note ]`**.
  - Resolution takes **under 5 seconds**.

---

### 📊 Action 6: 1-Click Batch Scorecard CSV Export
* **Goal**: Provide complete academic and placement evaluation data for Deans and Faculty.
* **Workflow**:
  - Admin clicks **`[ 📥 Export Batch Scorecards CSV ]`**.
  - Instantly downloads a clean spreadsheet containing:
    - `Student Name`, `Roll No`, `Email`, `Batch`
    - `Total Score Obtained`, `Max Score`, `Accuracy %`, `Batch Rank`
    - `Sectional Breakdown` (Quant, LRDI, SQL, Python marks with negative marking impact).

---

## 4. Current vs. Target State Gap Analysis Matrix

| Feature Dimension | Traditional / Legacy Admin System | Target College Admin Dashboard | Gap Classification | Implementation Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **Student Roster Entry** | Full CSV re-upload required for any change. | **Bulk CSV Upload + Single-Student Modal**. | 🔴 **Critical Admin UX** | Provide quick single-row insertion modal alongside bulk CSV parser. |
| **Course Setup Burden** | Faculty must build syllabus & upload videos. | **Pre-Packaged Licensed Track Allocation**. | 🔴 **Core B2B Model** | Deliver curated courses from in-house academic team. |
| **Test Reminders** | Manual faculty emails / notice board circulars. | **Fully Automated WhatsApp & Email Engine**. | 🟡 **Automation Win** | Cron-triggered reminder templates dispatched based on exam deadlines. |
| **Student Corrections** | Scattered manual emails and paper forms. | **1-Click Ticket Resolution Hub**. | 🟡 **Workflow Polish** | Centralized approval queue with PDF proof viewer. |
| **Evaluation Export** | Complex database queries or manual grading. | **1-Click Batch Scorecards CSV Export**. | 🟢 **Low-Effort Build** | Expose CSV endpoint pulling sectional data from `ezexam` sync tables. |

---

## 5. Current Immediate Scope vs. Future Long-Term Scope

```
┌────────────────────────────────────────────────────────────────────────┐
│                   DUAL-SPEED SCOPE & EXECUTION ROADMAP                 │
├────────────────────────────────────────────────────────────────────────┤
│  🎯 CURRENT SCOPE (Next 15–20 Days — Client Handover Ready)            │
│     Bulk CSV + Single Student Add, Licensed Course Mapping, Exam       │
│     Scheduler, Automated Nudges, Ticket Hub, Scorecard CSV Export      │
│                                                                        │
│  🚀 FUTURE SCOPE (Long-Term Scalable Engine)                           │
│     Self-Serve AI Course & Quiz Creation Studio, Executive Summary     │
│     PDF Generator, and Automated Remedial Video Recommendations        │
└────────────────────────────────────────────────────────────────────────┘
```

| Feature Area | Current Immediate Scope (Next 15–20 Days)<br>*(Keep it Very Basic & Client-Ready)* | Future Long-Term Scope<br>*(Iterative Platform Enhancements)* |
| :--- | :--- | :--- |
| **Roster Provisioning** | Bulk CSV upload + **Single-Student Add Modal** (`+ Add Student`). | Direct API sync with College SIS / ERP systems (SAP, Ellucian, Edusaint). |
| **Course Management** | Allocate licensed in-house tracks to student batches. | **Self-Serve AI Course Builder**: Author custom modules from syllabus PDFs. |
| **Assessment Management**| Schedule pre-packaged exam windows (Start/End dates). | **AI Quiz Generator**: Generate MCQs & coding testcases from lecture notes. |
| **Student Interventions**| **Fully Automated Reminders**: WhatsApp/Email nudges sent to unattempted students. | AI-driven predictive dropout alerts and personalized learning nudges. |
| **Profile & Corrections**| **Ticket Resolution Hub**: 1-Click Approve/Reject for student CGPA/profile changes. | Automated OCR grade-card verification for instant CGPA verification. |
| **Reporting & Analytics**| **1-Click Batch Scorecards CSV**: Detailed sectional marks, ranks, and accuracy. | **Executive Summary PDF**: 2-page visual PDF report with charts for Deans/Leadership. |

---

## 6. Open Product Questions & Discussion Points

The following items are flagged for team review:

### 📌 Open Point 1: Batch De-allocation & Archival
* When an academic year finishes, should completed batches be archived automatically or kept active in read-only mode for historical audit?

### 📌 Open Point 2: Admin Role-Based Permissions
* In future phases, should we support sub-roles (e.g. *Super Admin / Dean* vs. *Department Coordinator / TA* with restricted batch view)?
