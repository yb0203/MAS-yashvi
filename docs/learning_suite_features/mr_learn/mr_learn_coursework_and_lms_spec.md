# Mr. Learn — Coursework & Learning Experience Specification

**Module/Feature**: `Mr. Learn (Coursework & Learning Delivery Engine)`  
**Status**: `DRAFT (Ready for Team Review)`  
**Document Type**: High-Level Product Feature Document  
**Scope Definition**:
* **Current Immediate Scope (Phase 1: 15–20 Days)**: A clean, lightweight, highly functional Learning Experience ready for immediate client handover — single silent sign-on, clean "My Courses" home, zero-cart assigned tracks, basic video canvas with downloadable PDFs, and a keyword-moderated Q&A forum.
* **Future Long-Term Scope (Phase 2)**: In-house video streaming engine, AI discussion moderator, and deep assessment milestone linking.

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
   - Delivers semester-based curriculum mapped by branch and year, tracking attendance and learning milestones.
4. **Placement Bootcamps & Finishing Schools**:
   - Delivers fast-paced 60-day intensive industry readiness tracks to prepare students for recruitment drives.

---

## 2. End-to-End User Experience & Navigation Flow

### 2.1 The Silent Single Sign-On (SSO) Handshake
* **Zero Double-Login**: When an onboarded student clicks any course on their Student Dashboard, the platform executes a **silent authentication handshake**.
* The student transitions directly into `Mr. Learn` **without ever being asked for a second username or password**.

---

### 2.2 Screen 1: The Clean "My Courses" Home (`/learn`)
A simple, focused learning catalog displaying **only the courses assigned to the student**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [LOGO] INSTITUTIONAL PORTAL              [ 🔍 Search my courses... ]     [👤 Alex M. ▼] │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 📚 MY ASSIGNED COURSES (3 Tracks Active)                                               │
│                                                                                        │
│ ┌──────────────────────────────┐ ┌──────────────────────────────┐ ┌──────────────────┐ │
│ │ [ COURSE THUMBNAIL ]         │ │ [ COURSE THUMBNAIL ]         │ │ [ THUMBNAIL ]    │ │
│ │ Core Systems & Architecture  │ │ Technical Problem Solving    │ │ Professional Prep│ │
│ │ 15 / 20 Lectures Completed   │ │ 0 / 10 Lectures Completed    │ │ 5 / 8 Lectures   │ │
│ │ Progress: [=======>--- 75%]  │ │ Progress: [----------   0%]  │ │ Progress: [== 62%]│ │
│ │ [ ▶ Resume Coursework ➔ ]    │ │ [ 🚀 Start Coursework ➔ ]    │ │ [ ▶ Resume ➔ ]   │ │
│ └──────────────────────────────┘ └──────────────────────────────┘ └──────────────────┘ │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

* **Clear Progress Bars**: Each card displays total lectures, completed count, and a visual progress bar (`0%` to `100%`).
* **Smart Dynamic CTA**:
  - `[ 🚀 Start Coursework ➔ ]` for brand-new courses (0% progress).
  - `[ ▶ Resume Coursework ➔ ]` for in-progress courses (jumps to the exact paused video).
* **Zero E-Commerce Distractions**: No shopping cart, no pricing badges, no "Buy Now" buttons.

---

### 2.3 Screen 2: The Video Learning Canvas & Syllabus (`/learn/courses/:id`)
A distraction-free, 2-column learning environment:

```
┌────────────────────────────────────────────────────────────────────┬─────────────────────────┐
│ ← Back to My Courses | Core Systems & Architecture                 │ PROGRESS: 75% Completed │
├────────────────────────────────────────────────────────────────────┼─────────────────────────┤
│ LEFT VIDEO CANVAS (75% Width)                                      │ RIGHT SYLLABUS (25%)    │
│                                                                    │                         │
│ ┌────────────────────────────────────────────────────────────────┐ │ SECTION 1: FOUNDATIONS  │
│ │                                                                │ │ [✓] 1.1 Intro (12m)     │
│ │                 [ RESPONSIVE VIDEO PLAYER ]                    │ │ [✓] 1.2 Setup (15m)     │
│ │               (Speed: 0.75x - 2.0x | 360p-1080p)               │ │                         │
│ │                                                                │ │ SECTION 2: ARCHITECTURE │
│ └────────────────────────────────────────────────────────────────┘ │ [▶] 2.1 Core Flow (Now) │
│                                                                    │ [ ] 2.2 Data Models     │
│ LECTURE TITLE: 2.1 System Architecture & Core Data Flow            │                         │
│ ────────────────────────────────────────────────────────────────── │ SECTION 3: ADVANCED     │
│ [ TAB 1: Resources & Downloads ]      [ TAB 2: Cohort Discussion ] │ [ ] 3.1 Scaling         │
│ • 📄 Download Lecture Slides PDF                                   │                         │
│ • 💻 Download Starter Code Script (.py / .sql)                     │                         │
└────────────────────────────────────────────────────────────────────┴─────────────────────────┘
```

1. **Responsive Video Player**: Multi-speed playback ($0.75\text{x}-2.0\text{x}$), resolution toggle ($360\text{p}-1080\text{p}$), and full-screen mode. Auto-saves playback position.
2. **Interactive Syllabus Sidebar**: Module accordion with clear status icons (`[✓]` Completed, `[▶]` Currently Playing, `[ ]` Not Started).
3. **Resource & PDF Downloads Tab**: 1-click download of official lecture slide decks, cheat sheets, and source code files.
4. **Cohort Discussion Tab**: Cohort-scoped Q&A space where students can ask questions and read peer discussions.
   - **Keyword-Restricted Filter**: Automated dictionary blacklist that blocks spam, offensive language, and unverified phone numbers.

---

## 3. Student Dashboard Integration (Slot 1 Dual-State Experience)

On the main Student Dashboard, `Mr. Learn` drives **Slot 1 (Top-Left Card)** with a clean, dual-state experience:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   DASHBOARD SLOT 1: DUAL-STATE EXPERIENCE              │
├────────────────────────────────────────────────────────────────────────┤
│  STATE A: FIRST-TIME STUDENT (0% Progress / Day 1)                     │
│  • Badge: [ 🆕 Newly Assigned Track ]                                  │
│  • Course: Enterprise Track: Core Systems & Architecture               │
│  • Progress: [--------------------] 0% (0/20 Lectures Completed)       │
│  • Next Lesson: Module 1.1 — Orientation & Foundations (12m)           │
│  • Primary CTA: [ 🚀 START COURSEWORK ➔ ]                              │
│                                                                        │
│  STATE B: RETURNING STUDENT (In-Progress)                              │
│  • Badge: [ 📚 In Progress ]                                           │
│  • Course: Enterprise Track: Core Systems & Architecture               │
│  • Progress: [████████████████░░░░] 75% (15/20 Lectures Completed)     │
│  • Next Lesson: Module 2.1 — System Architecture & Data Flow (18m)     │
│  • Primary CTA: [ ▶ RESUME COURSEWORK ➔ ]                              │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Current Immediate Scope vs. Future Long-Term Scope

```
┌────────────────────────────────────────────────────────────────────────┐
│                   DUAL-SPEED SCOPE & EXECUTION ROADMAP                 │
├────────────────────────────────────────────────────────────────────────┤
│  🎯 CURRENT SCOPE (Next 15–20 Days — Client Handover Ready)            │
│     Basic assigned course list, clean player canvas, PDF downloads,    │
│     keyword-moderated forum, silent SSO login, dashboard integration   │
│                                                                        │
│  🚀 FUTURE SCOPE (Long-Term Scalable Engine)                           │
│     AI discussion moderator, in-video quiz checkpoints, in-house video │
│     streaming architecture, deep assessment milestone linking          │
└────────────────────────────────────────────────────────────────────────┘
```

| Feature Area | Current Immediate Scope (Next 15–20 Days)<br>*(Keep it Very Basic & Client-Ready)* | Future Long-Term Scope<br>*(Iterative Platform Enhancements)* |
| :--- | :--- | :--- |
| **Authentication** | **Silent SSO Handshake**: 1-Click transition from Dashboard to `Mr. Learn` with zero double login. | Unified single-session cookie across all platform subdomains. |
| **Home Experience** | **Assigned Courses List**: Clean cards showing enrolled tracks, lecture counts, and progress bars. | AI-curated elective discovery & multi-department course browser. |
| **Video Player** | Basic responsive player container with speed controls ($0.75\text{x}-2.0\text{x}$) and auto-save. | In-video interactive quiz checkpoints (Coursera model) and offline mobile caching. |
| **Course Materials** | 1-Click downloadable PDF lecture slides and starter code files. | Synchronized timestamped notes with 1-click PDF study guide export. |
| **Discussion Forum** | **Keyword-Restricted Filter**: Automated blacklist blocking profanity, spam, and phone numbers. | **AI Moderator**: Real-time automated doubt answering and toxicity sentiment shield. |
| **Assessments Linking** | Independent modules for now. Assessment milestones referenced in syllabus overview. | **Deep Assessment Thresholds**: Direct automated unlocking of `Mr. Test` exams upon $\ge 75\%$ progress. |
| **Admin Controls** | 1-Click track assignment to cohorts + downloadable CSV attendance & watch-time reports. | Live student watch telemetry heatmaps & automated at-risk reminder campaigns. |

---

## 5. Legacy B2C Features Removed

| Legacy Feature | Action | Product Rationale |
| :--- | :---: | :--- |
| **Refer & Earn Marketing Banners** | 🔴 **REMOVED** | Irrelevant for B2B; learners are pre-sponsored by their institution/employer. |
| **Shopping Cart & Retail Checkout** | 🔴 **REMOVED** | Courses are assigned directly by cohort; no individual purchase transactions. |
| **Third-Party Vendor Badges & Links** | 🔴 **REMOVED** | Ensures complete white-label brand ownership for our client. |
| **Public Unverified User Reviews** | 🔴 **REMOVED** | Replaced with internal structured cohort feedback forms. |
| **Public Storefront for Logged-In Users** | 🔴 **REMOVED** | Replaced with the clean "My Courses" assigned catalog. |

---

## 6. Strategic Architecture Note: Delivery Evolution

> [!NOTE]
> **DELIVERY EVOLUTION NOTE**  
> * **Current Phase (Immediate Client Handover)**: We utilize our existing learning delivery infrastructure wrapped in a pure white-label interface to ensure fast, seamless onboarding for our pilot clients.  
> * **Future Phase (Long-Term In-House Engine)**: We will plan to systematically move away from external wrappers and build our proprietary in-house video streaming and course management infrastructure.

---

## 7. Open Product Questions & Discussion Points

The following items are flagged for team alignment:

### 📌 Open Point 1: Linking Coursework with Assessments (Mr. Test)
* Currently, `Mr. Learn` and `Mr. Test` operate as distinct modular building blocks.
* In future iterations, we will define the exact cross-module linking rules (e.g. how a course completion event triggers an official assessment in `Mr. Test`).

### 📌 Open Point 2: Keyword Filter Customization per Client
* Should the keyword moderation dictionary be globally managed by our academic team, or should client admins be able to add custom blacklisted terms?

### 📌 Open Point 3: Content Pacing Controls
* Should all lectures in an assigned course be available immediately on Day 1 (self-paced), or should client admins have the option to schedule weekly module releases?
