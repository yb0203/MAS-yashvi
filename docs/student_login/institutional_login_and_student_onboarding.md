# Institutional Login & Student Onboarding — Feature Specifications & Gap Analysis

**Module/Journey**: `Institutional Login & Student Onboarding`  
**Status**: `DRAFT (Ready for Team Review)`  
**Target Platform**: 100% Pure White-Label Academic OS (`portal.college.edu`)  
**Scope**: Institutional Admin Provisioning, Authentication Engine, Student Profile Onboarding, and Session Management up to Dashboard Entry.

---

## 1. Executive Summary & B2B Institutional Context

This specification defines the **Login, Identity, and Onboarding System** for the white-label B2B Academic OS. The platform is sold directly to **Universities, Engineering & Management Colleges, and Test-Prep / Coaching Academies**.

### 🏛️ The 3 Institutional Customer Archetypes:
1. **Tier-1 & Accredited Universities**: Require strict institutional SSO (Google Workspace / Microsoft Entra ID), automated ERP sync, strict grading integrity, and locked CGPA governance.
2. **Tier-2/3 Engineering & Private Colleges**: Do not issue `@college.edu` emails to students, manage rosters via manual Excel/CSV files, and require low-friction onboarding with minimal IT overhead.
3. **Coaching & Upskilling Institutes**: Focus on fast batch rollouts, flexible personal email matching, and rapid student activation tracking.

---

## 2. B2B Client Pain Points, Key Questions & Solutions

| # | Institutional Admin Question / Pain Point | Real-World Concern | How Our Platform Solves It |
| :-: | :--- | :--- | :--- |
| **1** | **"How much IT effort is required from our staff to set this up?"** | Colleges dread 6-month software deployments and complex API setups. | **5-Minute Zero-Code CSV Ingestion**: Admin uploads an existing student spreadsheet. Smart validator auto-flags errors before saving. |
| **2** | **"Will our students know this is a third-party vendor?"** | Institutions fiercely protect their brand and refuse to expose external vendors to students. | **100% Pure White-Labeling**: Hosted on the college subdomain (`portal.college.edu`), with the college crest, dean announcements, and brand colors. Zero vendor mentions. |
| **3** | **"Can students fake their CGPA or branch to cheat in campus placement drives?"** | Placement officers fear recruiter blacklisting due to fake student credentials. | **Immutable Admin-Locked Records**: CGPA, Roll No, Branch, and Backlog status are read-only for students. Sourced exclusively from the college exam cell. |
| **4** | **"What if our college does not issue `@college.edu` institutional emails?"** | Tier-2/3 colleges only have personal Gmail IDs in their admission records. | **Dual-Mode Auth Engine**: Colleges can toggle between **Mode A (Campus SSO)** or **Mode B (Roster-Matched Personal Email + OTP)**. |
| **5** | **"What happens when students flood our office with login support issues?"** | Admins don't want 2,000 students lining up at the TPO office for password resets. | **Passwordless Login + In-App TPO Correction Queue**: 1-click magic links/OTPs eliminate password resets. Data typos are resolved via a 1-click approval queue. |
| **6** | **"How do we know how many students have actually started using the portal?"** | Deans have zero visibility into onboarding adoption rates. | **Live Activation Funnel Tracker**: Real-time progress bar with a **`[ 🔔 1-Click Resend Activation ]`** button for pending students. |

---

## 3. End-to-End Visual Process Flow (Granular Step-by-Step Flowchart)

```
┌──────────────────────────────────────────────────────────────────┐
│ STEP 1: ADMIN ROSTER INGESTION                                   │
│ College Admin drops semester CSV or connects Campus ERP          │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 2: PRE-FLIGHT VALIDATION & SMART ERROR CHECK                │
│ System parses rows. If errors exist ──► Inline Error Editor      │
│ (e.g. Duplicate Roll No / Malformed Email auto-flagged)          │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 3: BATCH PROVISIONING & TOKEN GENERATION                    │
│ Backend creates records in PENDING_ACTIVATION state              │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 4: INSTITUTIONAL ACTIVATION CAMPAIGN DISPATCH               │
│ System sends branded activation email with 7-day magic token     │
│ (Optional WhatsApp/SMS fallback for high open rates)             │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
                                  ▼ (Transitions to Student Action)
┌──────────────────────────────────────────────────────────────────┐
│ STEP 5: STUDENT ACCESSES PORTAL                                  │
│ Student receives invite & opens https://portal.college.edu       │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 6: CREDENTIAL SUBMISSION                                    │
│ Student inputs Email ID & Roll Number                            │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
┌─────────────────────────────────▼────────────────────────────────┐
│ STEP 7: TENANT AUTHENTICATION MODE VALIDATION                    │
│ ├──► Mode A (Campus SSO): Enforces @college.edu domain match     │
│ └──► Mode B (Roster Email): Validates email in Admin CSV list    │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
         ┌────────────────────────┴────────────────────────┐
         │                                                 │
┌────────▼────────────────────────┐       ┌────────────────▼───────────────┐
│ STEP 8A: ERROR BRANCH           │       │ STEP 8B: SUCCESS BRANCH        │
│ 🔴 Personal Email in SSO Mode   │       │ ✅ Verified Roster Match       │
│    └──► "Use college email"     │       │ 📲 Dispatches 6-Digit OTP /    │
│ 🟡 Valid Domain, Not in Roster  │       │    Completes SSO Handshake     │
│    └──► [ Contact TPO Support ] │       └────────────────┬───────────────┘
└─────────────────────────────────┘                        │
                                                           │
┌──────────────────────────────────────────────────────────▼───────┐
│ STEP 9: OTP VERIFICATION & RETURNING USER CHECK                  │
│ Student enters OTP. Backend checks has_completed_onboarding:     │
│ ├──► [ Returning Student (true) ] ─────────────────────────────┐ │
│ └──► [ First-Time Student (false)] ──► Proceed to Step 10      │ │
└──────────────────────────────────────────────┬─────────────────│─┘
                                               │                 │
┌──────────────────────────────────────────────▼─────────────────│─┐
│ STEP 10: 1-TIME 30-SECOND SETUP MODAL (SINGLE SCREEN)          │ │
│                                                                │ │
│ 🔒 Section 1: Locked Academic Identity (Read-Only)             │ │
│    • Name, Roll No, Branch, Sem, Verified CGPA (8.65 🔒)       │ │
│    👉 [ ⚠️ Data Incorrect? Request Correction from TPO ] ──┐   │ │
│                                                            │   │ │
│ 🎯 Section 2: Career Interests (1-Click Chips, Max 3)      │   │ │
│    [✓ Software Engg] [✓ Data & AI] [Product] [Finance]     │   │ │
│                                                            │   │ │
│ ✏️ Section 3: Optional Enrichment & Placement Resume       │   │ │
│    • LinkedIn URL | GitHub URL | Resume PDF (Max 5MB)      │   │ │
│    ℹ️ (Upload now or update anytime in Profile Settings)   │   │ │
│                                                            │   │ │
│ ⚙️ Section 4: Institutional Guidelines Checkbox            │   │ │
│    [ ] "I agree to Guidelines" (Tenant-configurable)       │   │ │
└──────────────────────────────────────────────┬─────────────│───│─┘
                                               │             │   │
┌──────────────────────────────────────────────▼──────────┐  │   │
│ STEP 11: DISCREPANCY TICKET (IF TRIGGERED)              │  │   │
│ Student submits typo correction with optional ID proof  │  │   │
│ ➔ Routes directly to Admin Correction Approval Queue ◄──┘  │   │
└──────────────────────────────────────────────┬──────────┘  │   │
                                               │             │   │
┌──────────────────────────────────────────────▼─────────────│───│─┐
│ STEP 12: SETUP COMPLETION & ONBOARDING FLAG UPDATE         │   │ │
│ Student clicks [ Complete Setup & Enter Dashboard ➔ ]      │   │ │
│ Backend marks has_completed_onboarding = true              │   │ │
└──────────────────────────────────────────────┬─────────────│───│─┘
                                               │             │   │
                                               ▼             │   │
┌────────────────────────────────────────────────────────────▼───▼─┐
│ STEP 13: MULTI-TIER COHORT ROUTING & DASHBOARD ARRIVAL           │
│ • Scenario A (2-Module Purchase): All Students ➔ 2-Module Suite  │
│ • Scenario B (4-Module Purchase):                                │
│   ├──► Junior Cohort (Years 1–2) ──► 2-Module Academic Suite     │
│   └──► Senior Cohort (Years 3–4) ──► 4-Module Full Suite         │
└──────────────────────────────────────────────────────────────────┘
```

---

## 4. College Admin Feature Suite & Management Capabilities

```
┌────────────────────────────────────────────────────────────────────────┐
│               THE 5 CORE ADMIN STUDENT MANAGEMENT FEATURES             │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Smart CSV Ingestor & Pre-Flight Validator (Inline Cell Fixes)       │
│ 2. Live Student Activation Funnel Tracker & 1-Click Bulk Reminders     │
│ 3. Master Student Directory (Filter by Branch, Year, Status, CGPA)     │
│ 4. In-App Academic Correction Approval Queue (1-Click Update Roster)   │
│ 5. Quick-Add Single Student Modal (Lateral Entry & Late Admissions)    │
└────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Admin Feature Specifications:
1. **Smart Ingestion Validator**:
   - Parses CSV pre-upload. Displays green valid rows and highlights red error cells (*Duplicate Roll No*, *Invalid Email Format*).
   - Allows admin to fix typos inline in the table before writing to the database.
2. **Non-Destructive Semester Rollover**:
   - Admin uploads new semester rosters without wiping historical student test scores, course progress, or resumes.
3. **Live Activation Funnel Tracker**:
   - Real-time widget: `Provisioned (1,200)` ➔ `Active (1,020 - 85%)` ➔ `Pending (180 - 15%)`.
   - Action: **`[ 🔔 1-Click Resend Activation to 180 Pending Students ]`**.
4. **Academic Correction Approval Queue**:
   - Displays student typo tickets with old vs. requested values and optional mark sheet/ID photo.
   - Admin has 1-click **`[ ✅ Approve & Update ]`** or **`[ ❌ Reject with Note ]`**.
5. **Single-Student Quick-Add**:
   - 6-field modal (`Name`, `Roll No`, `Email`, `Branch`, `Year`, `CGPA`) for instant lateral entry admissions.

---

## 5. Institutional Data Schema & Field Dictionary

### 5.1 The CGPA & Academic Integrity Policy
> [!IMPORTANT]
> **CGPA IS STRICTLY IMMUTABLE (READ-ONLY FOR STUDENTS)**  
> CGPA is the primary gating metric used by recruiters and TPOs for campus placements. Allowing students to self-edit CGPA creates severe fraud risk and compliance liability.  
> 
> * **Source of Truth**: Fed exclusively by the **College Exam Cell / Admin** via semester CSV or ERP sync.
> * **Student View**: Rendered with a **`[ 🔒 Verified by Institution ]`** trust badge.
> * **Correction Path**: If an updated grade is missing, clicking `[ ⚠️ Request CGPA Update ]` opens a support modal routing to the TPO queue.

---

### 5.2 Bulk Ingestion Data Fields (College CSV / ERP Sync)

| Field Name | Type | Allowed Values / Format | Example Value | Description & System Use |
| :--- | :---: | :--- | :--- | :--- |
| **`first_name`** | String | Alphanumeric (Max 50 chars) | `Alex` | Student first name. |
| **`last_name`** | String | Alphanumeric (Max 50 chars) | `Morgan` | Student last name. |
| **`roll_number`** | String | Unique Alphanumeric | `2028CS042` / `21BCSE104` | Primary university registration ID. |
| **`institutional_email`** | String | Valid Email (`@college.edu` or verified Gmail) | `alex.morgan@college.edu` | Whitelisted login identifier. |
| **`mobile_number`** | String | E.164 phone format | `+919876543210` | OTP delivery and emergency alerts. |
| **`program_name`** | Enum | `B.Tech`, `M.Tech`, `MBA`, `BCA`, `MCA`, `B.Sc`, `Dual Degree` | `B.Tech` | Degree program level. |
| **`branch_name`** | Enum | `CSE`, `DSX (Data Science)`, `ECE`, `IT`, `Mechanical`, `Civil`, `EE`, `BioTech` | `Computer Science & Engineering (CSE)` | Departmental specialization. |
| **`graduation_year`** | Integer | `2025` to `2030` | `2028` | "Class of 2028" — drives placement timelines. |
| **`current_year`** | Integer | `1`, `2`, `3`, `4`, `5` | `2` | Academic standing (Year 1/2/3/4). |
| **`current_semester`** | Integer | `1` to `10` | `4` | Active semester for course & exam mapping. |
| **`cgpa_score`** | Float | `0.00` to `10.00` (Read-Only) | `8.65` | **Immutable**. Gatekeeper for recruitment drives. |
| **`section_batch`** *(Optional)* | String | Alphanumeric | `Section A` / `Batch 1` | Internal classroom grouping. |

---

### 5.3 Onboarding Form UI Mapping (Student Setup Modal)

| Form Section | Data Field | State & Type | UI Behavior & Rules |
| :--- | :--- | :---: | :--- |
| **Section 1: Academic Identity** | **Full Name** | 🔒 **Locked** | Pre-filled: `first_name` + `last_name`. |
| | **Roll Number** | 🔒 **Locked** | Pre-filled: `roll_number`. |
| | **Email Address** | 🔒 **Locked** | Pre-filled: `institutional_email`. |
| | **Mobile Number** | 🔒 **Locked** | Pre-filled: `mobile_number`. |
| | **Degree & Program** | 🔒 **Locked** | Pre-filled: `program_name` (e.g. B.Tech). |
| | **Branch / Department** | 🔒 **Locked** | Pre-filled: `branch_name` (e.g. CSE, ECE, DSX). |
| | **Academic Standing** | 🔒 **Locked** | `Year [current_year] • Sem [current_semester] (Class of [graduation_year])`. |
| | **Verified CGPA** | 🔒 **Locked** | Displayed as `8.65 / 10.0 [ 🔒 Verified by Institution ]`. |
| | **Discrepancy Action** | ⚠️ **Link** | `[ Request Correction / CGPA Update ]` opens 3-field ticket modal. |
| **Section 2: Career Interests** | **Domain Interest Chips** | 🎯 **Optional** | 1-click selectable chips (Max 3). Pre-selected default based on branch. |
| **Section 3: Professional Links** | **LinkedIn URL** | ✏️ **Optional** | Validated `https://linkedin.com/in/...` format. |
| | **GitHub / Portfolio** | ✏️ **Optional** | Validated `https://github.com/...` format. |
| | **Placement Resume** | 📄 **Optional** | Drag-and-drop PDF (Max 5MB). Microcopy: *"Upload now or update anytime in Settings."* |
| **Section 4: Policy Checkbox** | **Institutional Policy** | ⚙️ **Configurable** | Checkbox: *"I agree to College Guidelines"*. (Shown only if enabled by Admin). |

---

## 6. Smart Session Management & Device Security Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                   SMART CONTEXT-AWARE SESSION ENGINE                   │
├────────────────────────────────────────────────────────────────────────┤
│  1. Personal Device (Default)  ──► 30-Day Persistent Refresh Token     │
│  2. Automated Lab PC Detection ──► Flushes session on browser close    │
│  3. Remote Kill Switch         ──► 1-Click logout from all other PCs   │
└────────────────────────────────────────────────────────────────────────┘
```

1. **30-Day Persistent Login on Personal Devices (Zero Interruption)**:
   - Personal laptops and phones receive a **30-Day Persistent Refresh Token** stored in an encrypted `HttpOnly` cookie.
   - Students stay logged in across the semester without annoying 30-minute popups.
2. **Automated Shared Lab PC Detection (No Manual Checkbox Needed)**:
   - The backend tracks hardware device fingerprints. If **multiple distinct student accounts log into the same device fingerprint within 48 hours**, that machine is automatically classified as `SHARED_LAB_PC`.
   - On detected lab machines, session tokens are stored **in-memory only** and flush immediately upon browser close.
3. **Remote Kill Switch (Active Session Revocation)**:
   - If a student forgets to log out of a campus lab computer, they can open **`Profile ➔ Active Devices`** on their phone and tap **`[ 🚪 Log Out of All Other Devices ]`** to instantly revoke the lab session.

---

## 7. Current Website Experience vs. White-Label Gap Matrix

| Feature Dimension | Current Platform (`myanalyticsschool.com`) | White-Label Target State (`portal.college.edu`) | Gap Classification | Technical & UX Resolution |
| :--- | :--- | :--- | :--- | :--- |
| **Domain & Subdomain** | Single public domain `myanalyticsschool.com`. | Multi-tenant custom subdomains (`portal.<college>.edu`). | 🔴 **Net-New Architecture** | Reverse proxy router with automatic SSL certificate provisioning. |
| **Branding & Visuals** | MAS logos, teal gradients, retail marketing banners. | 100% institutional branding (Crest, brand colors, campus photos). Zero vendor mentions. | 🔴 **Net-New Architecture** | Dynamic theme tokens injected per tenant hostname. |
| **User Provisioning** | Open self-signup (`/auth/register`) open to public. | Closed roster pre-provisioned via Admin CSV/ERP upload. | 🔴 **Critical Shift** | Disable public registration; whitelist-only authentication. |
| **Authentication Modes** | Generic B2C Email/Password + Public Google OAuth. | **Dual-Mode Auth**: Mode A (Campus SSO / SAML) + Mode B (Roster-Matched Email + OTP). | 🔴 **Critical Gap** | Enterprise Auth Engine supporting both Tier-1 SSO and Tier-2/3 roster emails. |
| **Admin Onboarding UI** | None. Manual internal database queries. | Dedicated **Admin Onboarding Suite** (Smart CSV Validator, Activation Funnel, Roster Table). | 🔴 **Net-New Admin Suite** | Comprehensive College Admin / TPO portal. |
| **CGPA Integrity** | Self-reported or missing. | **100% Immutable**: Admin-provided only. Displayed with verification badge. | 🔴 **Critical Enterprise Feature** | Database constraints preventing student mutation of academic & CGPA records. |
| **Discrepancy Reporting** | None. | Direct **`[ Request Correction ]`** 3-field modal sent to College Admin queue. | 🔴 **Net-New Feature** | Support ticketing engine with ID proof upload & admin approval. |

---

## 8. Failure Modes, Edge Cases & Escalation Protocols

| # | Failure Mode / Edge Case | UX Behavior & User Message | Escalation / Fallback Path |
| :-: | :--- | :--- | :--- |
| **1** | **Personal Email in SSO Mode**<br>(Student enters `alex@gmail.com` on a college that enforces `@college.edu`). | Red validation banner: *"Unauthorized Email. Please enter your official college email address (e.g. @college.edu)."* | Prevents external user access. |
| **2** | **College Email Missing from Roster**<br>(Student has `@college.edu` email, but was omitted from CSV). | Modal: *"Account Not Found. Your college email is valid, but your profile has not been uploaded to this semester's roster."* | **`[ Contact College Admin / TPO ]`** button opens pre-filled support modal sent directly to the college admin. |
| **3** | **Pre-Filled Academic Data / CGPA Typo**<br>(Wrong name spelling, branch, or outdated CGPA). | Fields are locked to preserve institutional records. | **`[ Request Correction ]`** button logs an academic correction request ticket with optional mark sheet / ID card proof. |
| **4** | **Expired Activation Magic Link** | Token expired after 7 days: *"Activation link expired. Enter your college email below to receive a fresh 10-minute code."* | Re-dispatches a single-use 6-digit OTP to verified institutional email. |
| **5** | **OTP Rate Limit Exceeded**<br>(5 consecutive failed OTP attempts). | Security banner: *"Too many failed attempts. For security reasons, please wait 15 minutes before trying again."* | Account temporarily throttled; admin alert logged if repeated. |
| **6** | **Deactivated / Suspended Student** | Login blocked: *"Your portal access has been deactivated by the institution administration."* | College support helpline and TPO office email displayed. |
