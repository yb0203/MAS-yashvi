# Mr. Learn — Coursework & Learning Experience Specification

**Module/Feature**: `Mr. Learn (Coursework & Learning Delivery Engine)`  
**Status**: `DRAFT (Ready for Team Review)`  
**Document Type**: High-Level Product Feature Document  
**Scope**: User Experience, Learning Journeys, Dashboard Integration, Feature Enhancements, and Client Value.

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

## 2. Product Feature Comparison (Current vs. Market Standards vs. Target)

```
┌────────────────────────────────────────────────────────────────────────┐
│               FEATURE EVOLUTION & MARKET BENCHMARK MATRIX              │
├────────────────────────────────────────────────────────────────────────┤
│  • Current State       ──► Retail Storefront with B2C E-Commerce Cart  │
│  • Market Benchmarks   ──► In-Video Checks, Skill Scores, Sticky Notes │
│  • Target Product State──► 100% White-Label Turn-Key Learning OS       │
└────────────────────────────────────────────────────────────────────────┘
```

| Feature Area | Current Platform (`mrlearn.in`) | Industry Best Practice | Target Product Experience in `Mr. Learn` |
| :--- | :--- | :--- | :--- |
| **Course Access Model** | Retail storefront with shopping cart & pricing. | Managed enterprise cohorts with assigned tracks. | **Assigned In-House Tracks**: Pre-mapped to student/employee batches with zero purchasing friction. |
| **Video Player Experience** | Basic player with third-party vendor branding. | Clean, branded player with speed and resolution controls. | **100% White-Label Player**: Multi-speed playback ($0.75\text{x}-2.0\text{x}$), resolution selector ($360\text{p}-1080\text{p}$), institutional branding. |
| **Engagement & Retention** | Passive video watching. | In-video knowledge checkpoints (Coursera model). | **In-Video Checkpoints**: Video pauses at key moments for a quick 1-question concept check. |
| **Skill Proof for Clients** | Standard course completion certificate. | Pre vs. Post skill benchmarking (Pluralsight model). | **Pre/Post Skill Growth**: Shows client leadership concrete proof of improvement (e.g. $+35\%$ score growth). |
| **Study Materials & Notes** | Static PDF downloads. | Timestamped notes exportable to PDF (Udemy model). | **Timestamped Notes**: Learners take notes linked to exact video moments, exportable as a study guide. |
| **Cohort Discussions** | Open public forum with no moderation. | Filtered discussion space with verified instructor answers. | **Cohort-Isolated Q&A**: Filtered space where instructors can highlight verified solutions. |
| **Content Security** | Unprotected video stream. | Dynamic learner identification watermark. | **Anti-Piracy Watermark**: Faint learner identifier on video canvas to protect proprietary content. |

---

## 3. Dual-Speed Product Roadmap (Short-Term vs. Long-Term)

```
┌────────────────────────────────────────────────────────────────────────┐
│                      DUAL-SPEED PRODUCT ROADMAP                        │
├────────────────────────────────────────────────────────────────────────┤
│  PHASE 1: SHORT-TERM (7–15 Days) ──► Fast Client Onboarding & Demos    │
│  PHASE 2: LONG-TERM (Quarterly)  ──► Advanced Learning Intelligence    │
└────────────────────────────────────────────────────────────────────────┘
```

| Dimension | Phase 1: Short-Term Goal (7–15 Days)<br>*(Ready for Immediate Deployment to Pilot Clients)* | Phase 2: Long-Term Goal (Ongoing)<br>*(Next-Gen Learning Operating System)* |
| :--- | :--- | :--- |
| **Course Delivery** | **Pre-Packaged In-House Tracks** curated by our academic team and assigned to cohorts. | Self-Serve Course Builder for clients who wish to author custom internal modules. |
| **Player Experience** | Clean white-label player, speed controls, notes download, anti-piracy watermark. | In-video interactive quiz checkpoints and offline mobile caching. |
| **Assessments & Gating** | Prerequisite threshold ($\ge 75\%$ video watch $\rightarrow$ unlocks `Mr. Test` exam). | Pre vs. Post Skill Growth benchmarking with automated competency reports. |
| **Discussions & Q&A** | Cohort-scoped Q&A tab with automated keyword profanity filter. | Real-time AI study assistant synthesizing instant answers from lecture transcripts. |
| **Admin Reporting** | Clean spreadsheet export of student watch time, attendance, and completion %. | Predictive at-risk learner alerts with automated nudge campaigns. |

---

## 4. End-to-End User Journey (Step-by-Step Flowchart)

```
┌──────────────────────────────────────────────────────────────────┐
│ STEP 1: CURRICULUM ALLOCATION (CLIENT ADMIN / TRAINER)           │
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
│ • Floating Watermark: Learner Identifier (Anti-Piracy)           │
│ • Right Sidebar (25%): Interactive syllabus with checkmarks [✓]  │
│ • Telemetry: Auto-saves progress continuously                    │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 4: RESOURCE ATTACHMENTS & SYNCHRONIZED NOTES                │
│ • Download Lecture Slides (PDF), Code Snippets & Spreadsheets    │
│ • Timestamped Note-Taking (Clicking a timestamp jumps to video)  │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 5: COHORT DISCUSSION FORUM & MODERATION                     │
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

## 5. Dashboard Integration (How Mr. Learn Feeds the Student Dashboard)

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

## 6. Client Admin & Trainer Management Features

```
┌────────────────────────────────────────────────────────────────────────┐
│               MR. LEARN: TRAINER & ADMIN CONTROL SUITE                 │
├────────────────────────────────────────────────────────────────────────┤
│  1. 1-Click Track Mapping      ──► Map pre-packaged tracks to batches  │
│  2. Attendance & Telemetry CSV ──► Export exact watch time per learner │
│  3. Skill Growth Delta Report  ──► Benchmark cohort improvement (+35%) │
│  4. At-Risk Learner Alert      ──► Flags learners falling behind       │
│  5. 1-Click Progress Nudge     ──► Broadcasts WhatsApp/Email reminder  │
└────────────────────────────────────────────────────────────────────────┘
```

1. **1-Click Track-to-Cohort Mapping**: Admin assigns a ready-made curriculum to any batch without manual course authoring.
2. **Attendance & Participation Reports**: 1-click spreadsheet export showing exact watch time and completion rates per learner.
3. **Skill Growth Metrics**: View pre-course vs. post-course score improvements across the batch.
4. **At-Risk Learner Alerts & 1-Click Reminders**: Flags learners who have fallen behind schedule and triggers reminder notifications in 1 click.

---

## 7. Legacy B2C Features Removed

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
> * **Phase 1 (Immediate Pilot Deployments)**: We utilize our existing learning delivery infrastructure wrapped in a pure white-label interface to ensure fast, seamless onboarding for our pilot clients.  
> * **Phase 2 (Long-Term Scalable Engine)**: We will evolve toward a fully proprietary in-house learning engine with custom streaming, advanced interactive checkpoints, and AI-assisted study tools.

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
