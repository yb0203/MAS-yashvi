# Route Specification: Campus Placement Drives (`/student/placements`)

This document defines the layout and screen interactions for the **Placement Drives Portal** (`/student/placements`) and the **Company Drive Detail & Application View** (`/student/placements/:driveId`).

---

## 📌 Route Metadata
- **Route Path**: `/student/placements` (Portal) & `/student/placements/:driveId` (Drive Details)
- **Module**: Mr. Hire (Recruitment & Placement Suite)
- **Purpose**: Browse campus job opportunities published by College TPO, check eligibility, submit job applications, and track interview shortlist updates.

---

## 📐 Screen Layout 1: Placement Drives Catalog (`/student/placements`)

```
+---------------------------------------------------------------------------------------------------+
|  PAGE HEADER: Campus Recruitment & Placement Drives                                               |
|  [ Eligible Drives (4) ]   [ My Applications (2) ]   [ All Drives (8) ]     [ 🔍 Search Company... ] |
+---------------------------------------------------------------------------------------------------+
|  ACTIVE DRIVES GRID (2 Columns)                                                                   |
|                                                                                                   |
|  +---------------------------------------+ +----------------------------------------------------+ |
|  | [COMPANY LOGO]  MICROSOFT             | | [COMPANY LOGO]  DELOITTE                           | |
|  | Role: Software Development Engineer   | | Role: Business & Technology Analyst              | |
|  | CTC: ₹18 - ₹24 LPA | Location: Noida  | | CTC: ₹9 - ₹12 LPA | Location: Gurgaon            | |
|  | Eligibility: B.Tech CS/IT (CGPA ≥ 7.5)  | | Eligibility: All B.Tech Branches (CGPA ≥ 6.0)    | |
|  | Deadline: Aug 18, 2026 at 5:00 PM      | | Deadline: Aug 22, 2026 at 5:00 PM                | |
|  | Status Tag: 🟢 Eligible (Not Applied)  | | Status Tag: 🔵 Applied (Shortlist Pending)       | |
|  | CTA: [ 💼 View Details & Apply ➔ ]    | | CTA: [ 📄 Track Application Status ➔ ]          | |
|  +---------------------------------------+ +----------------------------------------------------+ |
+---------------------------------------------------------------------------------------------------+
```

---

## 📐 Screen Layout 2: Drive Detail & Application View (`/student/placements/:driveId`)

```
+---------------------------------------------------------------------------------------------------+
|  ← Back to Placement Drives                                                                       |
|  +----------------------------------------------------------------------------------------------+  |
|  | [MICROSOFT LOGO]  Microsoft Corporation — Software Development Engineer                      |  |
|  | 💰 Package: ₹18.0 - ₹24.0 LPA  |  📍 Location: Bangalore / Hyderabad / Noida                  |  |
|  | ⏳ Application Deadline: August 18, 2026 • 5:00 PM IST                                       |  |
|  +----------------------------------------------------------------------------------------------+  |
|                                                                                                   |
|  TAB NAVIGATION:                                                                                  |
|  [ 📄 Job Description ]   [ 🎯 Eligibility Criteria ]   [ 🔄 Selection Process ]   [ 📮 Apply ]   |
|  -----------------------------------------------------------------------------------------------  |
|  JOB DESCRIPTION:                                                                                 |
|  - Designing, coding, testing, and debugging distributed cloud services.                          |
|  - Technical Stack: C++, Java, Data Structures, Algorithms, Azure System Design.                  |
|                                                                                                   |
|  ELIGIBILITY CHECK (Automated System Validation):                                                 |
|  [✓] Graduation Batch: 2026 (Matches requirement)                                                 |
|  [✓] CGPA: 8.4 / 10 (Exceeds minimum 7.5 threshold)                                               |
|  [✓] Academic Backlogs: 0 (Matches 0 backlog policy)                                              |
|                                                                                                   |
|  APPLICATION SECTION:                                                                             |
|  Resume Selected: [ Yashvi_Bansal_Software_Resume.pdf ]  (Change Resume)                          |
|  [ ] I confirm that all information provided is accurate per college guidelines.                  |
|                                                                                                   |
|  CTA: [ 🚀 Submit Application to College TPO ]                                                    |
+---------------------------------------------------------------------------------------------------+
```

---

## 🎨 Key Component Specifications

### 1. Drive Status Badge Variants
- 🟢 `Eligible (Not Applied)`: Student meets all CGPA/branch rules; blue/green CTA button enabled.
- 🔵 `Applied`: Application submitted; shows live status step (*Applied ➔ TPO Shortlisted ➔ Interview Scheduled ➔ Offer Issued*).
- 🔴 `Not Eligible`: Student does not meet criteria (e.g. CGPA below threshold); displays exact failing condition.

### 2. Application Tracker Pipeline
Horizontal step tracker showing progression:
1. `Application Submitted` ➔ 2. `TPO Verified` ➔ 3. `Company Shortlist` ➔ 4. `Interview Round 1` ➔ 5. `Offer Extended`.
