# Mr. Learn — Coursework & Learning Management Engine Specification

**Module/Journey**: `Mr. Learn (Coursework & Video Learning Delivery)`  
**Status**: `DRAFT (Ready for Team Review)`  
**Target Platform**: 100% Pure White-Label Academic & Enterprise Learning OS (`portal.college.edu` / `learn.partner.com`)  
**Scope**: Course Catalog, Video Learning Player, Cohort Discussions, Progress Telemetry, Dashboard Integration, and Trainer/Admin Management.

---

## 1. Executive Summary & Multi-Client Positioning

`Mr. Learn` is the core learning delivery and video management engine for the white-label B2B platform. It is engineered to serve **4 diverse client archetypes**:

```
┌────────────────────────────────────────────────────────────────────────┐
│             THE 4 DIVERSE B2B TRAINING & UPSKILLING CLIENTS            │
├────────────────────────────────────────────────────────────────────────┤
│  1. Enterprise B2B Upskilling Partners (e.g. Brain / SAP Trainers)     │
│  2. College Finishing Schools & Readiness Academies (e.g. Orin)        │
│  3. Higher Ed Universities & Accredited Engineering Colleges           │
│  4. Competitive Test-Prep & Coaching Chains                            │
└────────────────────────────────────────────────────────────────────────┘
```

* **For Enterprise Partners (e.g. Brain)**: Upskills corporate employees with employee ID mapping, proprietary video watermarking, and manager completion dashboards.
* **For College Readiness Partners (e.g. Orin)**: Delivers 60-day intensive placement preparation tracks across multiple university campuses.
* **For Higher Ed Colleges**: Delivers semester-based accredited video coursework mapped by branch and year.
* **For Coaching Chains**: Delivers fast-paced batch lecture roadmaps with ranked progress tracking.

---

## 2. Dual-Speed Execution Strategy (Short-Term vs. Long-Term)

```
┌────────────────────────────────────────────────────────────────────────┐
│                   DUAL-SPEED EXECUTION ROADMAP                         │
├────────────────────────────────────────────────────────────────────────┤
│  PHASE 1: SHORT-TERM (7–15 Days) ──► Fast Client Onboarding & Demos    │
│  PHASE 2: LONG-TERM (Quarterly)  ──► In-House Scalable Native Engine   │
└────────────────────────────────────────────────────────────────────────┘
```

| Dimension | Phase 1: Short-Term Goal (7–15 Days)<br>*(For Onboarding Active Clients: Brain / Orin / Colleges)* | Phase 2: Long-Term Goal (Ongoing)<br>*(Scalable Enterprise Learning OS)* |
| :--- | :--- | :--- |
| **Learner Home** | Context-aware post-login dashboard with 1-click `[ ▶ Resume ]` card. | Hyper-personalized AI learning path & pace predictor. |
| **Course Catalog** | Direct assigned course cards (Zero e-commerce cart/checkout). | Multi-department elective course self-registration. |
| **Video Player** | White-label player container, speed ($0.75\text{x}-2.0\text{x}$), resolution ($360\text{p}-1080\text{p}$). | Native HLS streaming, adaptive bitrate & offline caching. |
| **Anti-Piracy Security** | Dynamic floating watermark with Student Roll No / Employee ID + IP. | DRM encryption (Google Widevine & Apple FairPlay). |
| **Course Authoring** | Drag-and-drop video & PDF module uploader for trainers. | AI Course Builder (auto-curriculum, summaries & quizzes). |
| **Discussions & Q&A** | Cohort-isolated forum with automated keyword profanity blacklist. | Real-time AI doubt solver with timestamped video links. |
| **Assessment Gating** | Prerequisite threshold ($\ge 75\%$ video watch $\rightarrow$ unlocks `Mr. Test`). | Adaptive diagnostic milestone tests per module. |
| **Admin Reporting** | Real-time CSV export of student watch time & completion %. | Live attendance telemetry & automated at-risk nudges. |

---

## 3. End-to-End User Journey (Step-by-Step Flowchart)

```
┌──────────────────────────────────────────────────────────────────┐
│ STEP 1: COURSEWORK ALLOCATION (ADMIN / TRAINER)                  │
│ Admin assigns courses to specific Cohorts / Branches / Batches   │
│ (e.g. Brain SAP Batch 4 / B.Tech CSE Semester 4)                 │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 2: STUDENT DISCOVERY (DASHBOARD SLOT 1)                     │
│ Student sees active course card with progress ring & next video  │
│ CTA: [ ▶ Resume: Lecture 3.2 — Backpropagation (18 min) ➔ ]      │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 3: BESPOKE VIDEO LEARNING PLAYER CANVAS                     │
│ • Left Canvas (75%): Responsive player with speed controls       │
│ • Floating Watermark: Roll No / Employee ID (Anti-Piracy)        │
│ • Right Sidebar (25%): Interactive syllabus with checkmarks [✓]  │
│ • Telemetry: Auto-saves watch timestamp every 15 seconds         │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 4: RESOURCE ATTACHMENTS & SYNCHRONIZED NOTES                │
│ • Download Lecture Slides (PDF), Code Snippets (.py/.sql)        │
│ • Timestamped Note-Taking (Clicking 04:15 jumps to exact video)  │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 5: COHORT DISCUSSION FORUM & AI/KEYWORD MODERATION          │
│ • Cohort-scoped Q&A tab under video player                       │
│ • Keyword Blacklist auto-blocks spam, profanity & phone numbers  │
│ • Instructor pinned announcements & verified answer badges       │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 6: PREREQUISITE ASSESSMENT THRESHOLD UNLOCK                 │
│ Reaching >= 75% video completion automatically unlocks:          │
│ ➔ Mid-Term Exam (Mr. Test) / Campus Drive Eligibility (Mr. Hire) │
└──────────────────────────────────────────────────────────────────┘
```

---

## 4. Student Dashboard Integration (How Mr. Learn Feeds Dashboard Slot 1)

The Student Dashboard is powered by **real-time telemetry** from `Mr. Learn`:

```
┌────────────────────────────────────────────────────────────────────────┐
│  CURRENT COURSEWORK & LEARNING TRACKS (SLOT 1)                         │
├────────────────────────────────────────────────────────────────────────┤
│  📚 CS401: Advanced Machine Learning                                   │
│  Instructor: Dr. K. Sharma • Cohort: Class of 2028                     │
│                                                                        │
│  Progress: [██████████████████████████░░░░░░░░] 75% (15/20 Lectures)   │
│                                                                        │
│  ▶ NEXT LESSON: Module 3.2 — Backpropagation & Gradient Descent (18m)  │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                    [ ▶ RESUME COURSEWORK ➔ ]                     │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│  🔓 Prerequisite Met: [ CS401 Mid-Term Examination Unlocked ]          │
└────────────────────────────────────────────────────────────────────────┘
```

### Telemetry Data Pipe:
* `course_id` & `course_title`: Active primary course.
* `completion_percentage`: Float (e.g. `75.0%`).
* `last_watched_lecture_id` & `playback_timestamp_sec`: Opens video player at the exact second paused.
* `next_recommended_lecture_title`: Name and duration of next unwatched lecture.
* `is_prerequisite_met`: Boolean (turns green when progress $\ge 75\%$, enabling `Mr. Test` link).

---

## 5. College & Enterprise Admin Console Capabilities

```
┌────────────────────────────────────────────────────────────────────────┐
│               MR. LEARN: TRAINER & ADMIN CONTROL SUITE                 │
├────────────────────────────────────────────────────────────────────────┤
│  1. Course-to-Cohort Mapping   ──► 1-Click assign tracks to batches    │
│  2. Custom Drag-and-Drop Builder► Upload MP4s, PDFs & create syllabus  │
│  3. Attendance & Telemetry CSV ──► Export exact seconds watched/learner│
│  4. At-Risk Student Alert      ──► Flags learners falling behind       │
│  5. 1-Click Progress Nudge     ──► Broadcasts WhatsApp/Email reminder  │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Course-to-Cohort Assignment**:
   - Admin selects a course (e.g. *SAP MM Procurement Track*) and maps it to a batch (*Brain Corporate Batch 2*) in 1 click.
2. **Custom Drag-and-Drop Course Builder (Phase 1)**:
   - Create Course ➔ Add Module ➔ Upload Video (AWS S3 / YouTube unlisted) ➔ Attach PDF slides / code ➔ Publish.
3. **Accreditation & Attendance Telemetry (NAAC / HR Compliance)**:
   - 1-Click CSV export showing exact watch time per student across all course modules.
4. **Automated At-Risk Nudges**:
   - Detects students who have completed $< 25\%$ of coursework 5 days before an exam deadline and triggers 1-click WhatsApp/Email reminders.

---

## 6. Features Cleaned Up & Stripped (Legacy B2C Removal)

| Legacy B2C Feature (`mrlearn.in`) | Action | Rationale |
| :--- | :---: | :--- |
| **Refer & Earn (₹500 Promo Banners)** | 🔴 **STRIPPED** | Irrelevant for B2B; students/employees are pre-sponsored. |
| **Shopping Cart & Checkout (`/s/store/cart`)** | 🔴 **STRIPPED** | Courses are pre-assigned by cohort; no retail transactions. |
| **Third-Party Graphy Vendor Badges & Footer** | 🔴 **STRIPPED** | Complete removal of vendor watermarks and external links. |
| **Public Unverified Course Reviews** | 🔴 **STRIPPED** | Replaced by internal structured cohort feedback forms. |
| **Storefront Homepage for Logged-In Users** | 🔴 **STRIPPED** | Replaced with context-aware learning dashboard. |

---

## 7. Migration Note: Graphy LMS Integration ➔ In-House Architecture

> [!NOTE]
> **CURRENT INTEGRATION & FUTURE IN-HOUSE ROADMAP**  
> * **Current Phase (Short-Term MVP)**: The platform utilizes a white-labeled wrapper on top of Graphy LMS APIs (`/api/graphy`) to deliver video streaming, course metadata, and basic progress synchronization.  
> * **Target Phase (Long-Term In-House Engine)**: In future milestones, the platform will systematically **deprecate and migrate away from Graphy** to a proprietary in-house learning engine:
>   - Custom HLS/DASH video encoding pipeline on AWS MediaConvert + CloudFront.
>   - Proprietary multi-schema PostgreSQL course and telemetry tables (`mrlearn.courses`, `mrlearn.watch_sessions`).
>   - In-house AI Course Builder powered by LLMs for automated syllabus and quiz generation.
>   - Direct SCORM/xAPI connectors for enterprise HRMS integration.

---

## 8. Open Product Questions & Roadmap Considerations

The following items are flagged for deeper discussion and technical validation:

### 📌 Open Point 1: Custom Course Builder vs. AI Course Builder Scope
* How much authoring capability is required in Phase 1 for trainers (e.g. Brain / Orin) vs. delivering pre-packaged curriculum?
* Determine whether the Phase 1 MVP should support direct MP4 uploads or embed external secure video URLs (Vimeo OTT, AWS S3, YouTube unlisted).

### 📌 Open Point 2: Offline Download & Mobile Low-Bandwidth Support
* How should we handle low-connectivity environments for students in tier-2/3 college hostels?
* Explore PWA offline slide caching vs. audio-only low-bandwidth stream toggle.

### 📌 Open Point 3: Granular Prerequisite & Drip-Content Logic
* Should prerequisite locking be strictly sequential (Module 1 $\rightarrow$ Module 2) or calendar-scheduled (Week 1 $\rightarrow$ Week 2), or configurable per course by the instructor?

### 📌 Open Point 4: Forum Moderation Engine & Instructor SLAs
* Define the automated keyword dictionary categories (profanity, cheating solicitations, external links).
* Determine if instructor response SLAs (e.g. *"Instructor answers within 24 hours"*) should be visible to learners on corporate training tracks.
