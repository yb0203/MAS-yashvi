# Mr. Learn — Coursework & Learning Management Engine Specification

**Module/Journey**: `Mr. Learn (Coursework & Video Learning Delivery Engine)`  
**Status**: `DRAFT (Ready for Team Review)`  
**Target Platform**: 100% Pure White-Label Learning OS (`portal.institution.edu` / `learn.partner.com`)  
**Scope**: In-House Content Delivery, Video Player Canvas, Interactive Checkpoints, Cohort Discussions, Progress Telemetry, Dashboard Integration, and Client Management.

---

## 1. Executive Summary & Market-Wide B2B Positioning

`Mr. Learn` is the core learning delivery and video management engine for the white-label B2B Learning Suite. Rather than placing authoring overhead on client staff, **our in-house academic and curriculum team builds, packages, and curates gold-standard course tracks** and delivers them to client cohorts as a managed, turn-key learning engine.

### 🌐 The 4 Core Educational & Enterprise Segments:
```
┌────────────────────────────────────────────────────────────────────────┐
│             THE 4 DIVERSE B2B TRAINING & UPSKILLING DOMAINS            │
├────────────────────────────────────────────────────────────────────────┤
│  1. Enterprise Enterprise Systems & Workforce Upskilling Partners      │
│  2. Online Higher Ed Aggregators & Distance Learning Portals           │
│  3. Tier-1/2 Premier Universities & Engineering Institutions           │
│  4. Competitive Test-Prep, Placement Bootcamps & Finishing Schools     │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Enterprise Systems & Workforce Upskilling (e.g. ERP / Enterprise Tech)**:
   - Delivers specialized workforce upskilling tracks to corporate trainees and client employees.
   - Requires Employee ID / Trainee ID mapping, proprietary video watermarking (anti-piracy), and manager completion dashboards.
2. **Online Higher Ed Aggregators & Digital Universities**:
   - Delivers credit-backed, semester-long digital coursework to thousands of distributed remote students.
   - Requires scalable video streaming, structured module milestones, and verifiable completion transcripts.
3. **Premier On-Campus Universities & Engineering Colleges**:
   - Delivers department-specific academic tracks (CSE, ECE, Data Science, Core Engineering) mapped to university semesters.
   - Requires attendance telemetry for accreditation bodies (NAAC/NIRF) and prerequisite exam threshold gating.
4. **Placement Finishing Schools & Bootcamps**:
   - Delivers 60-day intensive industry readiness, aptitude, and technical interview preparation.
   - Requires fast cohort progression, diagnostic skill scoring, and integration with campus placement drives.

---

## 2. Market Benchmark & Comparative Analysis

To deliver a high-retention, enterprise-grade learning engine, `Mr. Learn` synthesizes the best UX patterns from industry leaders:

```
┌────────────────────────────────────────────────────────────────────────┐
│               ENTERPRISE LMS BENCHMARK COMPARISON MATRIX               │
├────────────────────────────────────────────────────────────────────────┤
│  • Coursera for Campus ──► In-Video Knowledge Checkpoints & Gating     │
│  • Pluralsight Skills  ──► Pre vs. Post Course Skill IQ Score Delta    │
│  • Canvas LMS          ──► Accordion Syllabus Tree & Assignment Box    │
│  • Udemy Business      ──► Timestamped Synchronized Notes & Q&A Badges │
└────────────────────────────────────────────────────────────────────────┘
```

| Dimension | Legacy B2C Storefront (`mrlearn.in`) | Industry Standard (Coursera / Pluralsight / Canvas) | Target `Mr. Learn` White-Label Architecture |
| :--- | :--- | :--- | :--- |
| **Content Sourcing** | Retail catalog with individual course purchases. | Managed enterprise content tracks assigned by cohort. | **Pre-Packaged In-House Tracks**: Curated by our academic team, assigned per cohort (Zero e-commerce). |
| **Video Player** | Basic embedded player with vendor watermarks. | Multi-speed, adaptive bitrate, anti-piracy watermarking. | **100% White-Label Player**: Speeds ($0.75\text{x}-2.0\text{x}$), resolutions ($360\text{p}-1080\text{p}$), dynamic Roll/Employee ID watermark. |
| **Learner Engagement** | Passive video watching (susceptible to background idling). | In-video pop-up quizzes (Coursera model). | **In-Video Checkpoints**: Video pauses at key timestamps for a 1-question concept check. |
| **Skill Validation** | Basic course completion certificate. | Pre vs. Post Skill IQ diagnostic benchmarking (Pluralsight model). | **Pre/Post Skill Delta**: 5-min diagnostic before course $\rightarrow$ Final assessment in `Mr. Test` showing concrete skill growth (+35%). |
| **Notes & Materials** | Static PDF downloads. | Timestamped synchronized notes exportable to PDF (Udemy model). | **Timestamped Note-Taking**: Notes saved with clickable timestamps + 1-click PDF study guide export. |
| **Cohort Discussions** | Open public forum with zero moderation. | Role-scoped Q&A with instructor verification badges. | **Cohort-Isolated Q&A**: Keyword profanity filter + `[ ✅ Verified Instructor Answer ]` badges. |

---

## 3. Dual-Speed Execution Strategy (Short-Term vs. Long-Term)

```
┌────────────────────────────────────────────────────────────────────────┐
│                   DUAL-SPEED EXECUTION ROADMAP                         │
├────────────────────────────────────────────────────────────────────────┤
│  PHASE 1: SHORT-TERM (7–15 Days) ──► Fast Client Onboarding & Demos    │
│  PHASE 2: LONG-TERM (Quarterly)  ──► In-House Scalable Native Engine   │
└────────────────────────────────────────────────────────────────────────┘
```

| Dimension | Phase 1: Short-Term Goal (7–15 Days)<br>*(Ready for Immediate Deployment to Pilot Clients)* | Phase 2: Long-Term Goal (Ongoing)<br>*(Proprietary In-House Learning OS)* |
| :--- | :--- | :--- |
| **Content Sourcing** | **Pre-Packaged In-House Tracks** curated by our academic team and assigned to client batches. | Self-Serve AI Course Builder for institutions wanting to author custom modules. |
| **Video Player** | White-label player container, speed/resolution controls, notes download, anti-piracy watermark. | In-video pop-up quiz checkpoints, native HLS/DASH streaming (migrating off Graphy). |
| **Telemetry & Gating** | Prerequisite threshold ($\ge 75\%$ video watch $\rightarrow$ unlocks `Mr. Test` exam). | Pre vs. Post Skill IQ benchmarking with automated competency growth reporting. |
| **Security & Privacy** | Dynamic floating watermark with Student Roll No / Employee ID + IP. | Full DRM encryption (Google Widevine & Apple FairPlay). |
| **Discussions & Q&A** | Cohort-scoped Q&A tab with automated keyword profanity blacklist. | Real-time AI doubt solver synthesizing answers from lecture transcripts. |
| **Admin Reporting** | Clean CSV export of student watch time, attendance, and completion %. | Predictive at-risk student intervention engine with automated nudge triggers. |

---

## 4. End-to-End User Journey (Step-by-Step Flowchart)

```
┌──────────────────────────────────────────────────────────────────┐
│ STEP 1: IN-HOUSE CURRICULUM ALLOCATION (ADMIN / TRAINER)         │
│ Admin assigns pre-packaged tracks to specific Cohorts / Batches  │
│ (e.g. Enterprise Batch 1 / B.Tech CSE Semester 4)                │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 2: STUDENT DISCOVERY (DASHBOARD SLOT 1)                     │
│ Student sees active course card with progress ring & next video  │
│ CTA: [ ▶ Resume: Lecture 3.2 — Core Module Concepts (18 min) ➔ ] │
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
│ STEP 5: COHORT DISCUSSION FORUM & KEYWORD MODERATION             │
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

## 5. Student Dashboard Integration (How Mr. Learn Feeds Dashboard Slot 1)

The Student Dashboard is powered by **real-time telemetry** from `Mr. Learn`:

```
┌────────────────────────────────────────────────────────────────────────┐
│  CURRENT COURSEWORK & LEARNING TRACKS (SLOT 1)                         │
├────────────────────────────────────────────────────────────────────────┤
│  📚 Enterprise Track: Core Systems & Architecture                      │
│  Curated by Academic Team • Cohort: Batch 2028                         │
│                                                                        │
│  Progress: [██████████████████████████░░░░░░░░] 75% (15/20 Lectures)   │
│                                                                        │
│  ▶ NEXT LESSON: Module 3.2 — Data Flow & Configuration (18m)           │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                    [ ▶ RESUME COURSEWORK ➔ ]                     │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│  🔓 Prerequisite Met: [ Comprehensive Assessment Unlocked ]            │
└────────────────────────────────────────────────────────────────────────┘
```

### Telemetry Data Pipe:
* `course_id` & `course_title`: Active primary course track.
* `completion_percentage`: Float (e.g. `75.0%`).
* `last_watched_lecture_id` & `playback_timestamp_sec`: Opens video player at the exact second paused.
* `next_recommended_lecture_title`: Name and duration of next unwatched lecture.
* `is_prerequisite_met`: Boolean (turns green when progress $\ge 75\%$, enabling `Mr. Test` link).

---

## 6. Client Admin & Trainer Console Capabilities

```
┌────────────────────────────────────────────────────────────────────────┐
│               MR. LEARN: TRAINER & ADMIN CONTROL SUITE                 │
├────────────────────────────────────────────────────────────────────────┤
│  1. 1-Click Track Mapping      ──► Map pre-packaged tracks to batches  │
│  2. Attendance & Telemetry CSV ──► Export exact seconds watched/learner│
│  3. Skill Growth Delta Report  ──► Benchmark cohort improvement (+35%) │
│  4. At-Risk Learner Alert      ──► Flags learners falling behind       │
│  5. 1-Click Progress Nudge     ──► Broadcasts WhatsApp/Email reminder  │
└────────────────────────────────────────────────────────────────────────┘
```

1. **1-Click Track-to-Cohort Mapping**:
   - Client admin selects a pre-packaged track from the catalog and assigns it to their batch with zero manual curriculum setup.
2. **Accreditation & Attendance Telemetry (NAAC / HR Compliance)**:
   - 1-Click CSV export showing exact watch time per student across all course modules.
3. **Skill Growth Delta Analytics**:
   - Real-time dashboard showing the cohort's pre-course vs. post-course score improvement.
4. **Automated At-Risk Nudges**:
   - Detects students who have completed $< 25\%$ of coursework 5 days before an exam deadline and triggers 1-click WhatsApp/Email reminders.

---

## 7. Legacy B2C Features Stripped

| Legacy B2C Feature (`mrlearn.in`) | Action | Rationale |
| :--- | :---: | :--- |
| **Refer & Earn (₹500 Promo Banners)** | 🔴 **STRIPPED** | Irrelevant for B2B; students/employees are pre-sponsored. |
| **Shopping Cart & Checkout (`/s/store/cart`)** | 🔴 **STRIPPED** | Courses are pre-assigned by cohort; no retail transactions. |
| **Third-Party Graphy Vendor Badges & Footer** | 🔴 **STRIPPED** | Complete removal of vendor watermarks and external links. |
| **Public Unverified Course Reviews** | 🔴 **STRIPPED** | Replaced by internal structured cohort feedback forms. |
| **Storefront Homepage for Logged-In Users** | 🔴 **STRIPPED** | Replaced with context-aware learning dashboard. |

---

## 8. Migration Note: Graphy LMS Integration ➔ In-House Architecture

> [!NOTE]
> **CURRENT INTEGRATION & FUTURE IN-HOUSE ROADMAP**  
> * **Current Phase (Short-Term MVP)**: The platform utilizes a white-labeled wrapper on top of Graphy LMS APIs (`/api/graphy`) to deliver video streaming, course metadata, and basic progress synchronization.  
> * **Target Phase (Long-Term In-House Engine)**: In future milestones, the platform will systematically **deprecate and migrate away from Graphy** to a proprietary in-house learning engine:
>   - Custom HLS/DASH video encoding pipeline on AWS MediaConvert + CloudFront.
>   - Proprietary multi-schema PostgreSQL course and telemetry tables (`mrlearn.courses`, `mrlearn.watch_sessions`).
>   - In-house AI Course Builder powered by LLMs for clients who wish to author custom content.
>   - Direct SCORM/xAPI connectors for enterprise HRMS integration.

---

## 9. Open Product Questions & Roadmap Considerations

The following items are flagged for deeper architectural exploration and stakeholder review:

### 📌 Open Point 1: In-Video Quiz Checkpoint Enforcement
* Should in-video pop-up quizzes (Coursera model) be mandatory to resume playback, or optional self-assessment checks?
* How should in-video quiz scores be weighted in the student's overall internal evaluation grade?

### 📌 Open Point 2: Offline Caching & Low-Bandwidth Optimization
* For students in tier-2/3 college hostels or remote areas with poor connectivity, evaluate PWA progressive offline slide caching vs. an audio-only stream toggle.

### 📌 Open Point 3: Content Drip vs. Self-Paced Access
* Should courses unlock all modules at once (self-paced) or follow a weekly drip schedule configured by the client admin?

### 📌 Open Point 4: Forum SLA & Faculty Response Metrics
* Determine if discussion response SLAs (e.g. *"Academic TA responds within 12 hours"*) should be visible to learners on high-intensity upskilling tracks.
