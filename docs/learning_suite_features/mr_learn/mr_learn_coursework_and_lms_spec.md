# Mr. Learn — Coursework & Learning Experience Specification

**Module/Feature**: `Mr. Learn (Coursework & Learning Delivery Engine)`  
**Status**: `DRAFT (Ready for Team Review)`  
**Document Type**: High-Level Product Feature Document  
**Scope Definition**:
* **Current Immediate Scope (Phase 1: 15–20 Days)**: Enhancing the current product for immediate client handover — single silent sign-on, clean "My Courses" home, zero-cart assigned tracks, basic video canvas with downloadable PDFs, authentic watch-time telemetry, and a keyword-moderated Q&A forum.
* **Future Long-Term Scope (Phase 2)**: Scalable in-house learning operating system with advanced AI learning intelligence, in-video quiz checkpoints, and proprietary video encoding infrastructure.

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
   - Delivers intensive industry readiness tracks ranging from 60 days to 6 months or 1 year, structured to prepare students for recruitment drives.

---

## 2. End-to-End User Experience & Navigation Flow

### 2.1 The Silent Single Sign-On (SSO) Handshake
* **Zero Double-Login**: When an onboarded student clicks any course on their Student Dashboard, the platform executes a **silent authentication handshake**.
* The student transitions directly into `Mr. Learn` **without ever being asked for a second username or password**.

---

### 2.2 Universal Top Header & Single Source of Truth Profile
Across **every module in the entire suite** (`Student Dashboard`, `Mr. Learn`, `Mr. Test`, `Mr. Hire`, `Mr. Mentor`, and any future modules), the platform maintains a **single, standardized top header and universal profile architecture**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [LOGO] INSTITUTIONAL PORTAL   [ 🏠 Home / Dashboard ]   [ 📚 My Courses ]              │
│                                           [ 🔍 Search my courses... ]     [👤 Alex M. ▼]│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### 👤 Universal Avatar Dropdown Menu (Quick Actions Hub):
Shared globally across all modules with zero duplication:
```
┌─────────────────────────────────────────────────────────┐
│  👤 Alex Morgan                                         │
│  alex.morgan@institution.edu • Roll: 2028CS042          │
├─────────────────────────────────────────────────────────┤
│  📄 Master Profile & Settings                           │
│  📜 Learning Transcript & Completed Records             │
│  🌗 Theme: [ Light ☀ | Dark 🌙 | System 💻 ]            │
├─────────────────────────────────────────────────────────┤
│  🚪 Log Out                                             │
└─────────────────────────────────────────────────────────┘
```
1. **🏠 [ Home / Dashboard ] Link**: Instant 1-click return to the primary Student Dashboard (`portal.institution.edu/student/dashboard`) from any page or deep module.
2. **📄 Master Profile & Settings (`/student/profile`)**: The **single universal profile page across the entire platform**:
   - **Academic Identity (Locked / Read-Only 🔒)**: Full Name, Roll No, Branch, Semester, and Verified CGPA (`8.65 [ 🔒 Verified ]`) + `[ ⚠️ Request Correction ]` button.
   - **Enrichment & Placement Assets (Editable ✏️)**: LinkedIn URL, GitHub URL, Portfolio Link, and active Placement Resume PDF.
   - **Learning Transcript & Certificate Vault *(Open to Discussion / Needs More Thought)*: A proposed tab showing completed course records and downloadable certificates.
   - **Security & Device Manager**: View active logged-in devices + **`[ 🚪 Log Out of All Other Devices ]`** remote kill-switch.
3. **📜 Learning Transcript & History**: *(Proposed shortcut — open to discussion)*.
4. **🌗 Theme Toggle**: Instant 1-click toggle (`Light` / `Dark` / `System`) without leaving the current view.
5. **🚪 Log Out**: Universal 1-click logout accessible from every module and screen.

---

### 2.3 Screen 1: The Clean "My Courses" Home (`/learn`)
A simple, focused learning catalog displaying **only the courses assigned to the student's cohort**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [LOGO] INSTITUTIONAL PORTAL   [ 🏠 Dashboard ]   [ 📚 My Courses (Active) ]             │
│                                           [ 🔍 Search my courses... ]     [👤 Alex M. ▼]│
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 📚 MY ASSIGNED COURSES (3 Active Tracks)                                               │
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

### 2.4 Screen 2: The Video Learning Canvas & Syllabus (`/learn/courses/:id`)
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
│ [ TAB 1: Resources & Downloads ]      [ TAB 2: Course Q&A Forum ]  │ [ ] 3.1 Scaling         │
│ • 📄 Download Lecture Slides PDF                                   │                         │
│ • 💻 Download Starter Code Script (.py / .sql)                     │                         │
└────────────────────────────────────────────────────────────────────┴─────────────────────────┘
```

1. **Responsive Video Player with Adaptive Bitrate**:
   - Multi-speed playback ($0.75\text{x}-2.0\text{x}$), resolution toggle ($360\text{p}-1080\text{p}$ with auto-bandwidth detection for low-connectivity hostels), and full-screen mode.
   - **Authentic Watch-Time Verification**: Video progress is strictly calculated on actual seconds watched. Fast-forward scrubbing without watching does not artificially increment the completion percentage.
2. **Interactive Syllabus Sidebar**: Module accordion with clear status icons (`[✓]` Completed, `[▶]` Currently Playing, `[ ]` Not Started).
3. **Resource & PDF Downloads Tab**: 1-click download of official lecture slide decks, cheat sheets, and source code files directly from the course storage bucket.

---

### 2.5 Discussion Forum: Course-Specific Q&A & Support SLA
To keep discussions tightly focused and eliminate moderation noise, discussion is structured as a **Course-Specific Q&A Space**:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   COURSE-SPECIFIC Q&A FORUM (CURRENT SCOPE)            │
├────────────────────────────────────────────────────────────────────────┤
│  • Location: Tab 2 directly inside the Course Canvas                   │
│  • Audience: Only learners enrolled in this specific course & batch    │
│  • Scope: Doubts, technical questions, and course-related discussions   │
│  • Instructor Tools: Pin official announcements, [ ✅ Verified Answer ]│
│  • Support SLA: Managed by Academic TAs with 24-hour response target   │
│  • Security: Automated Keyword Blacklist (blocks profanity & spam)     │
└────────────────────────────────────────────────────────────────────────┘
```

* **Course Q&A Tab under Player**:
  - All students in the course share a single collaborative doubt-clearing thread.
  - TAs and instructors can reply inline and pin official answers with a `[ ✅ Verified Instructor Answer ]` badge.
* **Automated Keyword Blacklist**:
  - Auto-blocks spam, profanity, and unverified phone numbers.
* **Institution-Wide Community Board**:
  - Deferred to **Future Scope (Phase 2)** to avoid operational complexity for initial client handover.

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

## 4. Current vs. Target State Gap Analysis Matrix

| Feature Dimension | Current Platform (`mrlearn.in`) | White-Label Target State | Gap Classification | Implementation Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **Authentication & SSO** | Separate manual login screen (`email + password`). | **Silent Seamless SSO Handshake** from Dashboard. | 🔴 **Critical UX Fix** | Generate single-use signed auth token on dashboard navigation. |
| **Course Catalog Access** | Retail e-commerce store (`/s/store`) with prices & cart. | **Clean "My Courses" Home** showing only assigned cohort tracks. | 🔴 **Critical B2B Pivot** | Filter catalog strictly by student batch ID; strip cart UI. |
| **Branding & Vendor Leaks** | Graphy logos, watermarks, and external links in footer. | **100% Pure White-Labeling** with client branding only. | 🔴 **Critical Brand Fix** | Remove external footer scripts and inject custom theme CSS. |
| **Watch-Time Integrity** | Basic video completion boolean. | **Authentic Watch-Time Verification** (anti-scrubbing). | 🟡 **High-Value Polish** | Enforce telemetry heartbeat on actual seconds watched. |
| **Course Material Downloads** | Native Graphy asset storage. | **Clean Resources Tab** with 1-click PDF/code download. | 🟢 **Existing Backend** | Connect UI tab directly to existing S3 attachment endpoints. |
| **Discussion & Forum** | Open public forum with zero moderation. | **Course-Specific Q&A Tab** with keyword profanity filter. | 🟡 **Feature Refinement** | Embed scoped Q&A tab under video with automated blacklist. |
| **Admin Reporting** | Manual internal database queries. | **Low-Effort Progress CSV** (`MrLearnLearner` export). | 🟢 **Low-Effort Build** | Expose CSV download endpoint using existing sync table. |

---

## 5. Current Immediate Scope vs. Future Long-Term Scope

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
| **Home Experience** | **Assigned Courses List**: Clean cards showing enrolled tracks, lecture counts, and progress bars. | **AI Course Builder & Authoring Studio**: Tools for AI curriculum generation, custom course development assistance, and client-assisted course onboarding. |
| **Video Player** | Basic responsive player container with speed controls ($0.75\text{x}-2.0\text{x}$) and auto-save. | In-video interactive quiz checkpoints (Coursera model) and offline mobile caching. |
| **Course Materials** | 1-Click downloadable PDF lecture slides and starter code files. | Synchronized timestamped notes with 1-click PDF study guide export. |
| **Discussion Forum** | **Keyword-Restricted Filter**: Automated blacklist blocking profanity, spam, and phone numbers. | **AI Moderator**: Real-time automated doubt answering and toxicity sentiment shield. |
| **Assessments Linking** | Independent modules for now. Assessment milestones referenced in syllabus overview. | **Deep Assessment Thresholds**: Direct automated unlocking of `Mr. Test` exams upon $\ge 75\%$ progress. |
| **Admin Controls** | **Low-Effort Learner Progress CSV**: Simple export of enrolled student completion % (`MrLearnLearner` data) + 1-Click batch assignment. | Advanced live video watch telemetry heatmaps & automated at-risk reminder campaigns. |

---

## 6. Legacy B2C Features Removed

| Legacy Feature | Action | Product Rationale |
| :--- | :---: | :--- |
| **Refer & Earn Marketing Banners** | 🔴 **REMOVED** | Irrelevant for B2B; learners are pre-sponsored by their institution/employer. |
| **Shopping Cart & Retail Checkout** | 🔴 **REMOVED** | Courses are assigned directly by cohort; no individual purchase transactions. |
| **Third-Party Vendor Badges & Links** | 🔴 **REMOVED** | Ensures complete white-label brand ownership for our client. |
| **Public Unverified User Reviews** | 🔴 **REMOVED** | Replaced with internal structured cohort feedback forms. |
| **Public Storefront for Logged-In Users** | 🔴 **REMOVED** | Replaced with the clean "My Courses" assigned catalog. |

---

## 7. Strategic Architecture Note: Delivery Evolution

> [!NOTE]
> **DELIVERY EVOLUTION & GRAPHY ROADMAP NOTE**  
> * **Short-Term Scope (Next 15–20 Days Pilot Handover)**: Graphy will remain as the underlying video delivery infrastructure for the immediate short-term goals. We will streamline the user experience, eliminate the double login via silent SSO, and present a clean branded wrapper to onboard pilot clients quickly.  
> * **Long-Term Scope (Future In-House Engine)**: We will systematically transition away from Graphy and build our proprietary in-house video streaming engine. Once built completely in-house, the platform will achieve **100% pure white-labeling** with zero external platform dependencies.

---

## 8. Client Review Questions & Implementation Answers

The following questions reflect how an external client or technical auditor evaluates `Mr. Learn` and our operational resolution:

### ❓ Question 1: Can our internal faculty or corporate trainers add supplementary notices or documents to pre-packaged tracks?
* **Answer**: Yes. While core lecture tracks are curated by our academic team, client admins have a lightweight interface to attach custom supplementary announcements and PDF reference notes to any module without altering the core curriculum.

### ❓ Question 2: How does the platform prevent students from fast-forwarding or scrubbing to artificially gain 100% attendance?
* **Answer**: The platform's watch telemetry records **actual continuous playback duration**. Fast-forward scrubbing jumps the video position but does not increment the verified watch-time counter required for course completion.

### ❓ Question 3: Who is responsible for answering student doubts in the Course Q&A forum?
* **Answer**: During pilot deployments, our **In-House Academic Teaching Assistants** monitor the course Q&A board with an agreed **24-hour response target**. Client faculty/trainers also hold moderator badges and can participate directly if desired.

### ❓ Question 4: How will students on slow mobile hostel Wi-Fi watch videos without buffering?
* **Answer**: The player features **Adaptive Bitrate Streaming ($360\text{p} \rightarrow 1080\text{p}$)** which dynamically adjusts resolution based on real-time internet speeds, ensuring smooth playback even on low-bandwidth mobile connections.

---

## 9. Open Product Questions & Discussion Points

The following items are flagged for team alignment:

### 📌 Open Point 1: Linking Coursework with Assessments (Mr. Test)
* Currently, `Mr. Learn` and `Mr. Test` operate as distinct modular building blocks.
* In future iterations, we will define the exact cross-module linking rules (e.g. how a course completion event triggers an official assessment in `Mr. Test`).

### 📌 Open Point 2: Content Pacing Controls
* Should all lectures in an assigned course be available immediately on Day 1 (self-paced), or should client admins have the option to schedule weekly module releases?

### 📌 Open Point 3: Learning Transcript & Certificate Vault Scope
* Need to explore how completed course records and certificates should be presented inside the Master Profile or as a standalone section, and whether employers/clients require verifiable public certificate URLs with QR codes.
