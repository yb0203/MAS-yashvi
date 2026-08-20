# Route Specification: My Courses & Learning Player (`/student/courses`)

This document defines the layout and screen interactions for the **My Courses Catalog** (`/student/courses`) and the **Video Learning Player View** (`/student/courses/:courseId/lecture/:lectureId`).

---

## 📌 Route Metadata
- **Route Path**: `/student/courses` (Catalog) & `/student/courses/:id` (Player)
- **Module**: Mr. Learn (Video LMS)
- **External Engine**: Graphy LMS API (`/api/graphy`)
- **Purpose**: Browse assigned course roadmaps, watch video lectures, track module progress, and unlock prerequisite exams.

---

## 📐 Screen Layout 1: Courses Catalog View (`/student/courses`)

```
+---------------------------------------------------------------------------------------------------+
|  PAGE HEADER: My Course Roadmaps                                                                  |
|  [ All Courses (4) ]   [ In Progress (2) ]   [ Completed (2) ]          [ 🔍 Search Courses... ]   |
+---------------------------------------------------------------------------------------------------+
|  COURSE CARDS GRID (3 Columns)                                                                    |
|                                                                                                   |
|  +--------------------------------+ +--------------------------------+ +------------------------+ |
|  | [COURSE THUMBNAIL IMAGE]       | | [COURSE THUMBNAIL IMAGE]       | | [COURSE THUMBNAIL]   | |
|  | Data Structures & Algorithms   | | Database Management Systems    | | Business Analytics   | |
|  | Instructor: Dr. K. Sharma        | | Instructor: Prof. V. Roy       | | Instructor: MAS      | |
|  | Progress: [=======>---- 65%]   | | Progress: [===========> 100%]  | | Progress: [--- 0%]   | |
|  | 14 / 20 Lectures Completed     | | Certificate: [ 📜 Download ]  | | [ Start Course ]     | |
|  | CTA: [ Resume Course ➔ ]       | | CTA: [ Review Modules ➔ ]     | |                      | |
|  +--------------------------------+ +--------------------------------+ +------------------------+ |
+---------------------------------------------------------------------------------------------------+
```

---

## 📐 Screen Layout 2: Video Learning Player View (`/student/courses/:id`)

```
+--------------------------------------------------------------------+------------------------------+
|  TOP NAV BAR: ← Back to Courses | Data Analytics Roadmap           |  COURSE PROGRESS: 65%        |
+--------------------------------------------------------------------+------------------------------+
|  LEFT PLAYER CANVAS (75% Width)                                    | RIGHT CURRICULUM SIDEBAR(25%)|
|                                                                    |                              |
|  +--------------------------------------------------------------+  |  SECTION 1: SQL FOUNDATIONS  |
|  |                                                              |  |  [✓] 1.1 Intro to RDBMS (12m)|
|  |                  [ VIDEO PLAYER CONTAINER ]                  |  |  [✓] 1.2 SELECT Statements   |
|  |                     (Graphy Player Embed)                    |  |  [▶] 1.3 JOIN Operations (Now|
|  |                                                              |  |                              |
|  +--------------------------------------------------------------+  |  SECTION 2: ADVANCED SQL     |
|                                                                    |  |  [🔒] 2.1 Window Functions   |
|  LECTURE TITLE: 1.3 Master SQL JOIN Operations (Inner & Outer)     |  |  [🔒] 2.2 Indexing & Performance
|  ----------------------------------------------------------------  |                              |
|  [ TAB 1: Lecture Notes ]   [ TAB 2: Resources ]   [ TAB 3: Q&A ]   |  PREREQUISITE EXAM UNLOCK    |
|  - Download Lecture Slides PDF                                     |  |  🔒 DBMS Mid-Term Exam       |
|  - Download SQL Query Scripts (.sql)                               |  |  (Requires 75% Completion)   |
+--------------------------------------------------------------------+------------------------------+
```

---

## 🎨 Key Component Specifications

### 1. Video Player Container
- Powered by Graphy LMS embed with playback speed controls ($0.75\text{x}$ to $2.0\text{x}$), resolution selector ($360\text{p}$ to $1080\text{p}$), and full-screen toggle.
- Auto-saves watch progress every 15 seconds.

### 2. Curriculum Sidebar Navigation
- Accordion list of sections and lectures.
- Icons indicate status: `[✓]` Completed (Green checkmark), `[▶]` Currently Playing (Active Teal), `[🔒]` Locked (Prerequisite required).

### 3. Exam Unlock Threshold Widget
- Shows locked exam badges attached to the course (e.g. *"Complete 75% of this course to unlock DBMS Mid-Term Exam"*).
- When progress $\ge 75\%$, badge turns green with a **"Take Exam Now ➔"** button.
