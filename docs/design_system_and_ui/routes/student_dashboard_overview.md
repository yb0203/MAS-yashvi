# Route Specification: Student Dashboard Overview (`/student/dashboard`)

This document defines the exact layout, component architecture, data touchpoints, and visual screen structure for the **Student Dashboard Overview** screen.

---

## 📌 Route Metadata
- **Route Path**: `/student/dashboard`
- **User Role**: Enrolled Student
- **Purpose**: Centralized academic & career command center providing at-a-glance status, urgent pending tasks, and quick access to active modules.

---

## 📐 Screen Wireframe Layout Diagram

```
+---------------------------------------------------------------------------------------------------+
|  ZONE 1: WELCOME & ACADEMIC STATUS BANNER                                                         |
|  "Welcome back, Yashvi Bansal 👋"                                                                 |
|  B.Tech Computer Science & Engineering • Semester 6 (Batch of 2026)                               |
|                                                                                                   |
|  [ 📊 Course Progress: 78% ]  [ 📝 Pending Exams: 2 ]  [ 💼 Eligible Drives: 4 ] [ 🎫 Tokens: 3 ]|
+---------------------------------------------------------------------------------------------------+
|  ZONE 2: ACTION-ORIENTED FOCUS GRID (3 Columns)                                                   |
|  +-----------------------------------+ +----------------------------------+ +-------------------+  |
|  | 📘 ACTIVE LEARNING TRACK          | | 📝 PENDING ASSESSMENTS           | | 💼 PLACEMENT    |  |
|  | Data Analytics & DBMS             | | Mid-Term Diagnostic Exam        | | Microsoft SDE-1 |  |
|  | Progress: [=======>---- 70%]      | | ⏳ Scheduled: Tomorrow, 10:00 AM | | 💰 ₹18-24 LPA   |  |
|  | CTA: [Resume Learning ➔]          | | CTA: [View Instructions ➔]      | | CTA: [Apply ➔]  |  |
|  +-----------------------------------+ +----------------------------------+ +-------------------+  |
+---------------------------------------------------------------------------------------------------+
|  ZONE 3: PERFORMANCE & CAREER ANALYTICS MATRIX                                                     |
|  +-----------------------------------+ +----------------------------------+ +-------------------+  |
|  | 📊 ACADEMIC OVERVIEW              | | 🕸️ SKILL PROFICIENCY MATRIX     | | 🎯 READINESS    |  |
|  | • Completed Modules: 12 / 16      | | • Data Structures: 85%           | | [✓] Resume      |  |
|  | • Attendance: 92%                 | | • SQL & Databases: 78%           | | [✓] Aptitude    |  |
|  | • Avg Score: 84/100               | | • System Design: 60%            | | [ ] Mock Call   |  |
|  +-----------------------------------+ +----------------------------------+ +-------------------+  |
+---------------------------------------------------------------------------------------------------+
|  ZONE 4: INSTITUTIONAL ANNOUNCEMENTS & HELPLINE FOOTER                                           |
|  +------------------------------------------------------------------+ +---------------------------+  |
|  | 📢 COLLEGE PLACEMENT CELL ANNOUNCEMENTS                          | | 📞 TPO CONTACT HELPLINE   |  |
|  | "TCS drive eligibility updated for 2026 batch"                   | | Prof. Sharma (TPO Lead) |  |
|  | Posted 2 hours ago by TPO Desk                                    | | [WhatsApp]  [Email]     |  |
|  +------------------------------------------------------------------+ +---------------------------+  |
+---------------------------------------------------------------------------------------------------+
```

---

## 🎨 Zone-by-Zone Visual Component Specification

### Zone 1: Academic Summary Header Banner
- **Card Background**: Gradient Soft Blue/Gray container (`#F8FAFC` to `#EFF6FF`).
- **Student Greeting**: `heading-lg` ("Welcome back, [Student Name] 👋").
- **Institutional Subtitle**: `body-md` ("B.Tech Computer Science & Engineering • Semester 6").
- **Quick-Pills Row**: 4 metric pill chips showing course progress, pending exams, active drives, and remaining mentor tokens.

### Zone 2: Action Focus Grid (3 Columns)
- **Column 1 (Mr. Learn)**: Active course card with progress bar and high-contrast **"Resume Learning ➔"** button.
- **Column 2 (Mr. Test)**: Urgent exam card with status tag (`Mandatory`, `Live Now`, `Upcoming`) and **"View Instructions ➔"** button.
- **Column 3 (Mr. Hire)**: Top eligible placement drive card with company CTC, deadline countdown, and **"Apply Now ➔"** button.

### Zone 3: Analytics Matrix
- **Academic Overview**: Attendance Donut Chart + Completion metrics.
- **Skill Proficiency Matrix**: Skill radar/bar progress derived from Mr. Test scores.
- **Placement Readiness Checklist**: Checkbox list showing resume verification, benchmark test status, and mock interview status.

### Zone 4: TPO Notice Board & Contact Strip
- **Notice Board**: List of official announcements posted by the College Placement Office.
- **Contact Card**: TPO Lead / Batch Coordinator details with direct `[WhatsApp TPO]` and `[Email TPO Support]` buttons.

---

## ⚙️ Modular Display Rules (B2B SaaS)
- If a college has **disabled Placement Drives (Mr. Hire)**, Column 3 in Zone 2 hides and Columns 1 & 2 expand to `50%` width each.
- If a college has **disabled Gamification (XP/Streaks)**, the gamification progress strip hides cleanly.
