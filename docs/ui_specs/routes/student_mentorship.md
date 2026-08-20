# Route Specification: 1-on-1 Mentorship & Booking (`/student/mentorship`)

This document defines the layout and screen interactions for the **Mentorship Booking Portal** (`/student/mentorship`) and the **Mentor Slot Reservation Flow**.

---

## 📌 Route Metadata
- **Route Path**: `/student/mentorship`
- **Module**: Mr. Mentor (1-on-1 Mentorship & Token Currency System)
- **Backend Settlement**: `SlotCompletionService.ts`
- **Purpose**: Redeem available mentor tokens to book 1-on-1 mock interviews, resume review calls, or technical doubt-clearing sessions with industry mentors.

---

## 📐 Screen Layout 1: Mentorship Portal & Mentor Directory (`/student/mentorship`)

```
+---------------------------------------------------------------------------------------------------+
|  PAGE HEADER: 1-on-1 Industry Mentorship & Mock Interviews                                        |
|  +----------------------------------------------------------------------------------------------+  |
|  | 🎫 YOUR MENTOR CREDIT BALANCE: 3 Tokens Available                                             |  |
|  | Need extra tokens? Contact College TPO Desk | Token Usage History: [ View Ledger ➔ ]          |  |
|  +----------------------------------------------------------------------------------------------+  |
|                                                                                                   |
|  FILTERS: [ All Categories ▼ ]  [ Mock Interview ▼ ]  [ Resume Review ▼ ]   [ 🔍 Search Mentor ]   |
+---------------------------------------------------------------------------------------------------+
|  MENTOR CARDS GRID (3 Columns)                                                                    |
|                                                                                                   |
|  +--------------------------------+ +--------------------------------+ +------------------------+ |
|  | [MENTOR PHOTO]                 | | [MENTOR PHOTO]                 | | [MENTOR PHOTO]         | |
|  | Rajesh Varma                   | | Ananya Sen                     | | Vikram Malhotra      | |
|  | Senior Data Engineer @ Amazon  | | Product Manager @ Microsoft    | | Tech Lead @ Flipkart | |
|  | ⭐ 4.9 (42 sessions)           | | ⭐ 4.95 (68 sessions)          | | ⭐ 4.88 (31 sessions)| |
|  | Token Cost: 1 Token / Session  | | Token Cost: 1 Token / Session  | | Token Cost: 1 Token  | |
|  | Expertise: SQL, Data Pipelines | | Expertise: System Design, PM   | | Expertise: DSA, C++  | |
|  | Next Slot: Tomorrow at 4:00 PM | | Next Slot: Friday at 6:00 PM   | | Next Slot: Saturday  | |
|  | CTA: [ 📅 Book Session ➔ ]     | | CTA: [ 📅 Book Session ➔ ]     | | CTA: [ Book ➔ ]      | |
|  +--------------------------------+ +--------------------------------+ +------------------------+ |
+---------------------------------------------------------------------------------------------------+
```

---

## 📐 Screen Layout 2: Slot Booking Modal Flow

```
+---------------------------------------------------------------------------------------------------+
|  MODAL: Book 1-on-1 Session with Rajesh Varma (Amazon)                                            |
|  -----------------------------------------------------------------------------------------------  |
|  STEP 1: SELECT SESSION TYPE                                                                      |
|  (•) Technical Mock Interview (Coding & SQL)                                                      |
|  ( ) Resume & Portfolio Review                                                                    |
|  ( ) General Career Guidance & Placement Prep                                                     |
|                                                                                                   |
|  STEP 2: SELECT DATE & TIME SLOT                                                                  |
|  Date: [ August 16, 2026 ▼ ]                                                                      |
|  Available Slots: [ 4:00 PM - 4:45 PM ]   [ 5:00 PM - 5:45 PM ]   [ 7:00 PM - 7:45 PM ]           |
|                                                                                                   |
|  STEP 3: UPLOAD RESUME & NOTES FOR MENTOR                                                         |
|  Attach Resume: [ Yashvi_Bansal_Software_Resume.pdf ]                                            |
|  Notes for Mentor: "I want to focus on SQL window functions and database indexing questions."    |
|                                                                                                   |
|  -----------------------------------------------------------------------------------------------  |
|  TOKEN SUMMARY:                                                                                   |
|  Current Balance: 3 Tokens | Session Deduction: -1 Token | Balance After Booking: 2 Tokens        |
|                                                                                                   |
|  [ Cancel ]                                            [ 🎫 Confirm & Reserve Slot (1 Token) ]    |
+---------------------------------------------------------------------------------------------------+
```

---

## 🎨 Key Component Specifications

### 1. Token Credit Badge
- Displays remaining token quota granted by the college.
- Disables the "Book Session" button if token balance is `0`, showing an alert: *"You have 0 tokens remaining. Request additional tokens from your TPO."*

### 2. Post-Call Scorecard View (`SlotCompletionService.ts`)
- After a mentor completes the call, the student receives a detailed **Mentor Feedback Scorecard**:
  - Technical Rating: ⭐⭐⭐⭐☆ (`4/5`)
  - Communication Rating: ⭐⭐⭐⭐⭐ (`5/5`)
  - Detailed Mentor Notes & Placement Recommendation (`Hire`, `Needs Practice`, `Not Ready`).
