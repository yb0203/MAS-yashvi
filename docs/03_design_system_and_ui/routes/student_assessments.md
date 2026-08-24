# Route Specification: Assessments & Exams (`/student/assessments`)

This document defines the layout and screen interactions for the **Exams & Assessments Portal** (`/student/assessments`) and the **Live Test Examination Portal** (`/student/assessments/:testId/take`).

---

## 📌 Route Metadata
- **Route Path**: `/student/assessments` (Portal) & `/student/assessments/:id/take` (Exam Execution)
- **Module**: Mr. Test (Assessment Engine)
- **External Engine**: EzExam Assessment Integration (`/api/ezexam`)
- **Purpose**: View assigned aptitude and technical exams, check prerequisite eligibility, attempt proctored live tests, and view scorecards.

---

## 📐 Screen Layout 1: Assessments Catalog View (`/student/assessments`)

```
+---------------------------------------------------------------------------------------------------+
|  PAGE HEADER: Institutional Assessments & Diagnostic Tests                                         |
|  [ Active Exams (2) ]   [ Completed (4) ]   [ Missed (0) ]                [ 🔍 Search Tests... ]   |
+---------------------------------------------------------------------------------------------------+
|  EXAM CARDS GRID                                                                                  |
|                                                                                                   |
|  +---------------------------------------+ +----------------------------------------------------+ |
|  | 🔴 LIVE NOW                           | | 🔒 LOCKED (Prerequisite Required)                 | |
|  | DBMS & SQL Mid-Term Screening         | | Advanced Python & Data Analytics Diagnostic       | |
|  | Category: Technical Assessment        | | Category: Aptitude & Coding                      | |
|  | Duration: 60 Mins | Total Marks: 100  | | Duration: 90 Mins | Total Marks: 150                | |
|  | Passing Threshold: 50%                | | Unlock Rule: Requires 75% Data Analytics Course  | |
|  | Deadline: Today at 11:59 PM           | | Progress: [=======>----- 65% Completed]          | |
|  | CTA: [ 🚀 Start Test Now ]            | | CTA: [ 🔒 Complete Prerequisite Course ➔ ]       | |
|  +---------------------------------------+ +----------------------------------------------------+ |
|                                                                                                   |
|  +----------------------------------------------------------------------------------------------+ |
|  | 🟢 COMPLETED EXAMS & SCORECARDS                                                              | |
|  | Aptitude Benchmark Test #1 | Date: Aug 05, 2026 | Score: 82/100 (PASSED) | Badge: 📝 Achiever   | |
|  | CTA: [ 📄 View Detailed Question Analysis & Performance Report ]                             | |
|  +----------------------------------------------------------------------------------------------+ |
+---------------------------------------------------------------------------------------------------+
```

---

## 📐 Screen Layout 2: Live Exam Execution Screen (`/student/assessments/:id/take`)

```
+--------------------------------------------------------------------+------------------------------+
|  EXAM HEADER: DBMS & SQL Mid-Term Exam                             | ⏳ TIME REMAINING: 42:18 Mins |
+--------------------------------------------------------------------+------------------------------+
|  LEFT QUESTION CANVAS (75% Width)                                  | RIGHT QUESTION PALETTE (25%) |
|                                                                    |                              |
|  QUESTION 14 OF 30 (Single Select MCQ)                             |  [1] [2] [3] [4] [5]         |
|  What is the primary difference between `WHERE` and `HAVING`       |  [6] [7] [8] [9] [10]        |
|  clauses in SQL?                                                   |  [11] [12] [13] [14🔴] [15]  |
|                                                                    |  [16] [17] [18] [19] [20]    |
|  ( ) A. WHERE filters rows before aggregation, HAVING filters      |                              |
|         aggregated groups after GROUP BY.                          |  LEGEND:                     |
|  ( ) B. WHERE is only used with JOINs.                             |  🟢 Answered (12)            |
|  ( ) C. HAVING cannot accept string functions.                     |  ⚪ Unanswered (15)          |
|  ( ) D. There is no operational difference.                        |  🟡 Marked for Review (3)    |
|                                                                    |                              |
|  ----------------------------------------------------------------  |  PROCTORING STATUS:          |
|  [ ◄ Previous ]   [ Mark for Review ]   [ Save & Next ► ]          |  📷 Webcam Active (Secure)   |
|                                                                    |  [ 🏁 Submit Test ]          |
+--------------------------------------------------------------------+------------------------------+
```

---

## 🎨 Key Component Specifications

### 1. Prerequisite Threshold Lock Card
- Visually displays why an exam is locked (e.g. *"Requires 75% video completion on Mr. Learn"*).
- Includes a direct CTA button that links straight into the unfinished course module.

### 2. Live Question Palette
- Grid of numbered question buttons color-coded by status:
  - 🟢 Green: Answered & Saved
  - ⚪ White/Gray: Not Yet Answered
  - 🟡 Amber: Marked for Review
  - 🔴 Red: Current Active Question

### 3. Exam Result & Scorecard Modal (`MrTestSubmissionReport`)
- Breakdown of Total Score, Accuracy %, Percentile Rank, Time Spent per Question, and Question-level Explanation Key.
