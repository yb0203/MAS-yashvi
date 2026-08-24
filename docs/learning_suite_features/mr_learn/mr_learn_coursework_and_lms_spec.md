# Mr. Learn — Coursework & Learning Experience Specification

**Module/Feature**: `Mr. Learn (Coursework & Learning Delivery Engine)`  
**Status**: `DRAFT (Ready for Team Review)`  
**Document Type**: High-Level Product Feature Document  
**Scope Definition**:
* **Current Immediate Scope (Phase 1: 15–20 Days)**: Enhancing the current product for immediate client handover — stripping B2C artifacts, fixing major UX/branding flaws, and seamlessly integrating learning telemetry into the Student Dashboard.
* **Future Long-Term Scope (Phase 2)**: Scalable in-house learning operating system with advanced AI learning intelligence.

---

## 1. Product Overview & Market Segments

`Mr. Learn` is the core learning and coursework delivery engine for our B2B Learning Suite. Rather than requiring client organizations to create courses from scratch, **our in-house academic team designs, packages, and delivers complete, high-quality course tracks** ready for immediate deployment.

### 🌐 The 4 Core Educational & Enterprise Segments:
```
┌────────────────────────────────────────────────────────────────────────┐
│             THE 4 DIVERSE B2B TRAINING & UPSKILLING DOMAINS            │
├────────────────────────────────────────────────────────────────────────┤
│  1. Enterprise Workforce Upskilling & Corporate Training Partners      │
│  2. Online Higher Ed Aggregators & Distance Learning Portals           │
│  3. Universities, Engineering & Management Colleges                    │
│  4. Placement Bootcamps, Finishing Schools & Test-Prep Academies       │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Enterprise Workforce Upskilling & Corporate Training**:
   - Delivers specialized skill tracks to corporate trainees and employees with manager progress reporting and verified completion badges.
2. **Online Higher Ed Aggregators & Digital Universities**:
   - Delivers structured digital semester courses to distributed remote students with verifiable progress transcripts.
3. **Universities & Engineering Colleges**:
   - Delivers semester-based curriculum mapped by branch and year, tracking attendance and unlocking exams.
4. **Placement Bootcamps & Finishing Schools**:
   - Delivers fast-paced 60-day intensive industry readiness tracks to prepare students for recruitment drives.

---

## 2. Current Immediate Scope vs. Future Vision

```
┌────────────────────────────────────────────────────────────────────────┐
│                   DUAL-SPEED SCOPE & EXECUTION ROADMAP                 │
├────────────────────────────────────────────────────────────────────────┤
│  🎯 CURRENT SCOPE (Immediate Handover: 15–20 Days)                     │
│     Fix major UX issues, strip B2C artifacts, integrate into Dashboard │
│                                                                        │
│  🚀 FUTURE SCOPE (Long-Term Scalable Learning OS)                      │
│     In-video checkpoints, AI study assistant, in-house video engine    │
└────────────────────────────────────────────────────────────────────────┘
```

### 🎯 2.1 Current Immediate Scope (Fix & Hand Over to Clients)
* **Goal**: Deliver a polished, client-ready learning portal that can be handed over to our pilot clients immediately within the next 15–20 days.
* **Core Deliverables**:
  1. **Fix Critical Brand & UX Flaws**:
     - 100% white-labeled player container under client branding.
     - Strip all B2C e-commerce artifacts (Refer & Earn banners, shopping cart, retail checkout, public prices).
  2. **Context-Aware Learning Home**:
     - Logged-in learners bypass the public storefront and land directly on their active course tracks.
  3. **In-House Curriculum Mapping**:
     - Pre-packaged tracks curated by our academic team mapped directly to client batches (zero authoring burden on clients).
  4. **Student Dashboard Integration (Slot 1)**:
     - Real-time progress bar, "Next Up" lesson title, and 1-click **`[ ▶ Resume Coursework ➔ ]`** button.
  5. **Basic Client Admin Tools**:
     - 1-Click track assignment to cohorts + downloadable CSV attendance/watch-time reports.

---

### 🚀 2.2 Future Long-Term Scope (Scalable Learning OS)
* In-video interactive quiz checkpoints (Coursera model).
* Pre vs. Post Skill Growth benchmarking (Pluralsight model).
* Timestamped synchronized notes with 1-click PDF study guide export.
* Dynamic anti-piracy learner watermarking on video canvas.
* Real-time AI study assistant and self-serve AI Course Builder for clients wanting custom content.

---

## 3. Product Feature Comparison Matrix

| Feature Area | Current Legacy Platform (`mrlearn.in`) | Current Immediate Scope (Handover Ready) | Future Long-Term Scope |
| :--- | :--- | :--- | :--- |
| **Course Access Model** | Retail storefront with shopping cart & pricing. | **Assigned In-House Tracks**: Pre-mapped to cohorts with zero purchase friction. | Self-Serve Course Builder for client-authored modules. |
| **Video Player Experience** | Basic player with third-party vendor branding. | **Clean White-Label Player**: Speeds ($0.75\text{x}-2.0\text{x}$), resolutions ($360\text{p}-1080\text{p}$). | In-video quiz checkpoints + offline mobile caching. |
| **Dashboard Integration** | Standalone disconnected website. | **Seamless Slot 1 Card**: Live % progress + 1-click resume at last timestamp. | Skill competency graph & personalized pace forecaster. |
| **Cohort Discussions** | Open public forum with no moderation. | **Cohort-Isolated Q&A Tab**: Keyword profanity filter + pinned announcements. | Real-time AI doubt solver synthesizing answers from video transcripts. |
| **Admin Reporting** | Manual database queries. | **Clean Spreadsheet Export**: Student watch time, attendance, completion %. | Predictive at-risk learner alerts with automated nudge campaigns. |

---

## 4. End-to-End User Journey (Current Scope Flowchart)

```
┌──────────────────────────────────────────────────────────────────┐
│ STEP 1: IN-HOUSE CURRICULUM ALLOCATION (ADMIN / TRAINER)         │
│ Admin assigns pre-packaged tracks to specific Batches / Cohorts  │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 2: LEARNER DISCOVERY (DASHBOARD SLOT 1)                     │
│ Learner sees active course card with progress bar & next video   │
│ CTA: [ ▶ Resume: Lecture 3.2 — Core Concepts (18 min) ➔ ]        │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 3: CLEAN VIDEO LEARNING PLAYER CANVAS                       │
│ • Left Canvas (75%): Responsive player with speed controls       │
│ • Right Sidebar (25%): Interactive syllabus with checkmarks [✓]  │
│ • Telemetry: Auto-saves progress continuously                    │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 4: RESOURCE ATTACHMENTS & STUDY MATERIALS                   │
│ • Download Lecture Slides (PDF), Code Snippets & Spreadsheets    │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 5: COHORT DISCUSSION FORUM & BASIC MODERATION               │
│ • Cohort-scoped Q&A tab under video player                       │
│ • Keyword Filter auto-blocks spam and inappropriate text         │
│ • Instructor pinned announcements & verified answer badges       │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 6: PREREQUISITE ASSESSMENT THRESHOLD UNLOCK                 │
│ Reaching >= 75% video completion automatically unlocks:          │
│ ➔ Comprehensive Exam (Mr. Test) / Placement Eligibility (Mr. Hire│
└──────────────────────────────────────────────────────────────────┘
```

---

## 5. Student Dashboard Integration (How Mr. Learn Feeds Dashboard Slot 1)

On the Student Dashboard, `Mr. Learn` drives **Slot 1 (Top-Left Card)**:

```
┌────────────────────────────────────────────────────────────────────────┐
│  CURRENT COURSEWORK & LEARNING TRACKS (SLOT 1)                         │
├────────────────────────────────────────────────────────────────────────┤
│  📚 Enterprise Track: Core Systems & Architecture                      │
│  Curated by Academic Team • Cohort: Class of 2028                      │
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

### Key Visual & Functional Elements:
* **Active Course Card**: Displays the title and banner of the current assigned track.
* **Live Progress Bar**: Displays percentage and module completion count (e.g. `75% • 15/20 Lectures`).
* **"Next Up" Lesson Reminder**: Highlights the exact upcoming lesson name and duration.
* **1-Click Resume Button**: Jumps straight into the player at the exact second where the learner paused.
* **Exam Gating Indicator**: Turns green when the prerequisite threshold ($\ge 75\%$) is achieved.

---

## 6. Client Admin & Trainer Management Features (Current Scope)

```
┌────────────────────────────────────────────────────────────────────────┐
│               MR. LEARN: TRAINER & ADMIN CONTROL SUITE                 │
├────────────────────────────────────────────────────────────────────────┤
│  1. 1-Click Track Mapping      ──► Map pre-packaged tracks to batches  │
│  2. Attendance & Telemetry CSV ──► Export exact watch time per learner │
│  3. At-Risk Learner Alert      ──► Flags learners falling behind       │
│  4. 1-Click Progress Nudge     ──► Broadcasts WhatsApp/Email reminder  │
└────────────────────────────────────────────────────────────────────────┘
```

1. **1-Click Track-to-Cohort Mapping**: Admin assigns a ready-made curriculum to any batch without manual course authoring.
2. **Attendance & Participation Reports**: 1-click spreadsheet export showing exact watch time and completion rates per learner.
3. **At-Risk Learner Alerts & 1-Click Reminders**: Flags learners who have fallen behind schedule and triggers reminder notifications in 1 click.

---

## 7. Legacy B2C Features Removed in Current Scope

| Legacy Feature | Action | Product Rationale |
| :--- | :---: | :--- |
| **Refer & Earn Marketing Banners** | 🔴 **REMOVED** | Irrelevant for B2B; learners are pre-sponsored by their institution/employer. |
| **Shopping Cart & Retail Checkout** | 🔴 **REMOVED** | Courses are assigned directly by cohort; no individual purchase transactions. |
| **Third-Party Vendor Badges & Links** | 🔴 **REMOVED** | Ensures complete white-label brand ownership for our client. |
| **Public Unverified User Reviews** | 🔴 **REMOVED** | Replaced with internal structured cohort feedback forms. |
| **Public Storefront for Logged-In Users** | 🔴 **REMOVED** | Replaced with a personalized, context-aware learning dashboard. |

---

## 8. Strategic Product Note: Evolution of Platform Delivery

> [!NOTE]
> **DELIVERY EVOLUTION NOTE**  
> * **Current Scope (Immediate Client Handover)**: We utilize our existing learning delivery infrastructure wrapped in a pure white-label interface to ensure fast, seamless onboarding for our pilot clients.  
> * **Future Scope (Long-Term Scalable Engine)**: We will evolve toward a fully proprietary in-house learning engine with custom streaming, advanced interactive checkpoints, and AI-assisted study tools.

---

## 9. Open Product Questions & Discussion Points

The following product questions are open for exploration:

### 📌 Open Point 1: In-Video Checkpoint Experience
* Should in-video quiz popups be mandatory before video playback can resume, or optional self-check milestones?
* How should in-video checkpoints contribute to the learner's overall completion grade?

### 📌 Open Point 2: Low-Bandwidth & Mobile Experience
* What is the optimal experience for learners in low-connectivity areas (e.g. downloadable slide summaries, audio-first listening mode)?

### 📌 Open Point 3: Content Scheduling & Pacing
* Should courses unlock all modules at once (self-paced) or follow a weekly schedule set by the trainer/admin?

### 📌 Open Point 4: Discussion Forum Engagement
* Should discussion response expectations (e.g. *"Instructor responds within 24 hours"*) be shown to learners on intensive upskilling tracks?
