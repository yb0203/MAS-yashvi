# Student Login & Onboarding — Feature Specifications & Gap Analysis

**Module/Journey**: `Student Login & Onboarding`  
**Status**: `DRAFT (Ready for Team Review)`  
**Target Platform**: 100% Pure White-Label Academic OS (`portal.college.edu`)  
**Scope**: From institutional bulk provisioning and authentication up to first landing on the dashboard.

---

## 1. End-to-End User Journey (Visual Flow Diagram)

```
┌──────────────────────────────────────────────────────────────────┐
│              STAGE 1: INSTITUTIONAL BULK PROVISIONING            │
├──────────────────────────────────────────────────────────────────┤
│  [ College Admin / TPO ]                                         │
│          │                                                       │
│          ▼                                                       │
│  [ Bulk Uploads Student CSV / ERP Sync ]                         │
│  (Roll No, Name, Program, Branch, Verified CGPA, Email, Year)    │
│          │                                                       │
│          ▼                                                       │
│  [ Backend Provisions Records in PENDING_ACTIVATION State ]      │
│          │                                                       │
│          ▼                                                       │
│  [ Dispatches Official Activation Email with 7-Day Token ] ────┐ │
└────────────────────────────────────────────────────────────────│─┘
                                                                 │
┌────────────────────────────────────────────────────────────────▼─┐
│               STAGE 2: AUTHENTICATION & VALIDATION               │
├──────────────────────────────────────────────────────────────────┤
│  Student accesses: https://portal.college.edu/auth/login         │
│          │                                                       │
│          ▼                                                       │
│  [ Student Enters Email & Roll Number ]                          │
│  (+ "Public/Shared Computer" Session Security Toggle)            │
│          │                                                       │
│          ├──► [ Non-College Email (@gmail.com) in SSO Mode ]     │
│          │    └──► 🔴 ERROR: "Use official college email"        │
│          │                                                       │
│          ├──► [ Valid Domain, but Missing from CSV Roster ]      │
│          │    └──► 🟡 ERROR: "Unprovisioned Account"             │
│          │         └──► [ Contact College Admin / TPO ]          │
│          │                                                       │
│          └──► [ Verified College Email in Active Roster ]        │
│               └──► [ Dispatches 6-Digit OTP / Campus SSO ] ────┐ │
└────────────────────────────────────────────────────────────────│─┘
                                                                 │
┌────────────────────────────────────────────────────────────────▼─┐
│        STAGE 3: 1-TIME 30-SECOND SETUP MODAL (FIRST LOGIN)       │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  🔒 1. Verified Academic Identity (READ-ONLY / LOCKED)           │
│     • Name: Alex Morgan       • Roll No: 2028CS042               │
│     • Program: B.Tech (CSE)   • Academic Standing: Year 2, Sem 4 │
│     • Verified CGPA: 8.65     • Official Email & Mobile          │
│     👉 [ ⚠️ Data Incorrect? Request Correction from TPO ]        │
│                                                                  │
│  🎯 2. Career Interests (1-CLICK CHIPS — MAX 3, OPTIONAL)        │
│     [✓ Software Engg] [✓ Data & AI] [Product] [Cloud] [Finance]  │
│                                                                  │
│  ✏️ 3. Professional Links & Placement Resume (OPTIONAL)          │
│     • LinkedIn URL [ ... ]    • GitHub / Portfolio [ ... ]       │
│     • Placement Resume PDF (Max 5MB, Virus-Scanned)              │
│     ℹ️ (Upload now or update anytime in Profile Settings)        │
│                                                                  │
│  ⚙️ 4. Institutional Policy Checkbox (CONFIGURABLE BY COLLEGE)   │
│     [ ] "I agree to Institutional Guidelines" (Optional)         │
│                                                                  │
│  [ 🚀 Click "Complete Setup & Enter Dashboard" ] ──────────────┐ │
└────────────────────────────────────────────────────────────────│─┘
                                                                 │
┌────────────────────────────────────────────────────────────────▼─┐
│              STAGE 4: ARRIVAL ON STUDENT DASHBOARD               │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Backend marks has_completed_onboarding = true                   │
│                                                                  │
│  • Scenario A: 2-Module Subscription (Learn + Test only)         │
│    └──► All Students (Years 1 to 4) ──► 2-Module Academic Suite  │
│                                                                  │
│  • Scenario B: Full 4-Module Subscription                        │
│    ├──► Junior Cohort (Years 1–2)   ──► 2-Module Academic Suite  │
│    └──► Senior Cohort (Years 3–4)   ──► 4-Module Full Suite      │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 2. Institutional Data Schema & Field Dictionary

### 2.1 Academic Integrity Rule: The CGPA Policy
> [!IMPORTANT]
> **CGPA IS STRICTLY IMMUTABLE (READ-ONLY FOR STUDENTS)**  
> CGPA is the primary gating criterion used by campus recruiters and TPOs for placement drives. Allowing students to self-edit CGPA creates severe fraud risk and compliance liability.  
> 
> * **Source of Truth**: CGPA is fed exclusively by the **College Examination Cell / Admin** via semester CSV or ERP sync.
> * **Student View**: Displayed with a **`[ 🔒 Verified by Institution ]`** trust badge.
> * **Discrepancy Resolution**: If a student's newly published semester GPA is missing or incorrect, clicking `[ ⚠️ Request CGPA Update ]` opens a support modal with optional mark sheet upload, routing directly to the TPO approval queue.

---

### 2.2 Bulk Ingestion Data Fields (College CSV / ERP Sync)

| Field Name | Type | Allowed Values / Format | Example Value | Description & System Use |
| :--- | :---: | :--- | :--- | :--- |
| **`first_name`** | String | Alphanumeric (Max 50 chars) | `Alex` | Student first name. |
| **`last_name`** | String | Alphanumeric (Max 50 chars) | `Morgan` | Student last name. |
| **`roll_number`** | String | Unique Alphanumeric | `2028CS042` / `21BCSE104` | Primary university registration ID. |
| **`institutional_email`** | String | Valid Email (`@college.edu` or verified Gmail) | `alex.morgan@college.edu` | Whitelisted login identifier. |
| **`mobile_number`** | String | E.164 phone format | `+919876543210` | OTP delivery and SMS alerts. |
| **`program_name`** | Enum | `B.Tech`, `M.Tech`, `MBA`, `BCA`, `MCA`, `B.Sc`, `Dual Degree` | `B.Tech` | Degree program level. |
| **`branch_name`** | Enum | `CSE`, `DSX (Data Science)`, `ECE`, `IT`, `Mechanical`, `Civil`, `EE`, `BioTech` | `Computer Science & Engineering (CSE)` | Departmental specialization. |
| **`graduation_year`** | Integer | `2025` to `2030` | `2028` | "Class of 2028" — drives placement timelines. |
| **`current_year`** | Integer | `1`, `2`, `3`, `4`, `5` | `2` | Academic standing (Year 1/2/3/4). |
| **`current_semester`** | Integer | `1` to `10` | `4` | Active semester for course & exam mapping. |
| **`cgpa_score`** | Float | `0.00` to `10.00` (Read-Only) | `8.65` | **Immutable**. Gatekeeper for recruitment drives. |
| **`section_batch`** *(Optional)* | String | Alphanumeric | `Section A` / `Batch 1` | Internal classroom grouping. |

---

### 2.3 Onboarding Form UI Mapping (Student Setup Modal)

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

## 3. Current Website Experience vs. White-Label Gap Matrix

| Feature Dimension | Current Platform (`myanalyticsschool.com`) | White-Label Target State (`portal.college.edu`) | Gap Classification | Technical & UX Resolution |
| :--- | :--- | :--- | :--- | :--- |
| **Domain & Subdomain** | Single public domain `myanalyticsschool.com`. | Multi-tenant custom subdomains (`portal.<college>.edu`). | 🔴 **Net-New Architecture** | Reverse proxy router with automatic SSL certificate provisioning. |
| **Branding & Visuals** | MAS logos, teal gradients, retail marketing banners. | 100% institutional branding (Crest, brand colors, campus photos). Zero vendor mentions. | 🔴 **Net-New Architecture** | Dynamic theme tokens injected per tenant hostname. |
| **User Provisioning** | Open self-signup (`/auth/register`) open to public. | Closed roster pre-provisioned via Admin CSV/ERP upload. | 🔴 **Critical Shift** | Disable public registration; whitelist-only authentication. |
| **Authentication Modes** | Generic B2C Email/Password + Public Google OAuth. | **Dual-Mode Auth**: Mode A (Campus SSO / SAML) + Mode B (Roster-Matched Email + OTP). | 🔴 **Critical Gap** | Enterprise Auth Engine supporting both Tier-1 SSO and Tier-2/3 roster emails. |
| **CGPA Integrity** | Self-reported or missing. | **100% Immutable**: Admin-provided only. Displayed with verification badge. | 🔴 **Critical Enterprise Feature** | Database constraints preventing student mutation of academic & CGPA records. |
| **Shared Lab Security** | Standard persistent browser cookie. | Dedicated **"Public / Shared Computer"** toggle with 15-min auto-lockout. | 🔴 **Net-New Security** | Session management middleware based on device trust flag. |
| **Discrepancy Reporting** | None. | Direct **`[ Request Correction ]`** 3-field modal sent to College Admin queue. | 🔴 **Net-New Feature** | Support ticketing engine with ID proof upload & admin approval. |
| **Resume Security** | Unverified file upload. | PDF-only mime validation, 5MB limit, automated malware scan. | 🔴 **Net-New Security** | Secure S3 bucket with lambda virus scanning. |

---

## 4. Failure Modes, Edge Cases & Escalation Protocols

| # | Failure Mode / Edge Case | UX Behavior & User Message | Escalation / Fallback Path |
| :-: | :--- | :--- | :--- |
| **1** | **Personal Email in SSO Mode**<br>(Student enters `alex@gmail.com` on a college that enforces `@college.edu`). | Red validation banner: *"Unauthorized Email. Please enter your official college email address (e.g. @college.edu)."* | Prevents external user access. |
| **2** | **College Email Missing from Roster**<br>(Student has `@college.edu` email, but was omitted from CSV). | Modal: *"Account Not Found. Your college email is valid, but your profile has not been uploaded to this semester's roster."* | **`[ Contact College Admin / TPO ]`** button opens pre-filled support modal sent directly to the college admin. |
| **3** | **Pre-Filled Academic Data / CGPA Typo**<br>(Wrong name spelling, branch, or outdated CGPA). | Fields are locked to preserve institutional records. | **`[ Request Correction ]`** button logs an academic correction request ticket with optional mark sheet / ID card proof. |
| **4** | **Expired Activation Magic Link** | Token expired after 7 days: *"Activation link expired. Enter your college email below to receive a fresh 10-minute code."* | Re-dispatches a single-use 6-digit OTP to verified institutional email. |
| **5** | **OTP Rate Limit Exceeded**<br>(5 consecutive failed OTP attempts). | Security banner: *"Too many failed attempts. For security reasons, please wait 15 minutes before trying again."* | Account temporarily throttled; admin alert logged if repeated. |
| **6** | **Deactivated / Suspended Student** | Login blocked: *"Your portal access has been deactivated by the institution administration."* | College support helpline and TPO office email displayed. |
