# Component Specification: Mr Learn — Video Learning Engine (Graphy LMS Integration)

## 1. Overview
**Mr Learn** is the video course and Learning Management System (LMS) integration console for the MAS Mentor Platform. It connects MAS to an external specialist LMS platform (**Graphy** via `/api/graphy`). It handles video course mapping, learner progress synchronization, new-student auto-enrolment, and automated WhatsApp progress reminders.

---

## 2. System Architecture & Progress Loop

```mermaid
flowchart TD
    ADMIN[Admin Panel\nadmin/mrlearn/*] -->|Manage & Sync| BE[Express Backend\n/api/graphy]
    BE -->|LMS API Calls| GR[Graphy LMS]
    
    GR -->|Learner Video Watching| PROG[Video Completion %]
    PROG -->|MrLearnSyncConfig / Cron| SYNC[MrLearnSyncService]
    SYNC -->|Write Snapshot| DB[(mrlearn Schema DB\nMrLearnLearner)]
    
    DB -->|Falling Behind?| WA[MrLearnReminderService]
    WA -->|Trigger Template| MSG[WhatsApp Progress Nudge]
    
    DB -->|Feed Completion| STU[Student Roadmap & Scholar Badge]
```

---

## 3. Core Features

### 3.1 Course & Learner Management
- Browse video courses, manage enrolled learners, and review question banks (`admin/mrlearn/`).
- Push MAS students into Graphy LMS as learners (`POST /api/graphy/sync/students/seed-all-missing`).

### 3.2 Learner Progress Sync (`mrlearn` schema)
- `MrLearnCourse`: Synchronized course metadata.
- `MrLearnLearner`: Tracks individual student completion (`progressPercentage`, completion status, raw JSON report).
- `MrLearnSyncConfig`: Sets sync interval (e.g., default 168 hours / 7 days).

### 3.3 Automated WhatsApp Progress Reminders
- System detects students who are falling behind on video milestones.
- `MrLearnReminderService` triggers automated WhatsApp messages using the template `mrlearn_course_progress_reminder`.
- Execution details logged in `MrLearnReminderLog`.

### 3.4 New-Student Auto-Sync Cron Job
- `new-student-cron`: Periodically scans newly enrolled MAS applications and automatically provisions learner accounts inside Graphy without manual admin intervention.

### 3.5 Gamification Integration
Completing the first video course module unlocks the **Scholar Badge** (`module_master`) and grants `+50 XP`.
