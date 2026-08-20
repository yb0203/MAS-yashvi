# Route Specification: Student Profile & Settings (`/student/profile`)

This document defines the layout and screen interactions for the **Student Profile & Settings Portal** (`/student/profile`).

---

## 📌 Route Metadata
- **Route Path**: `/student/profile` & `/student/settings`
- **Purpose**: Manage student academic profile details, upload updated resumes, set notification preferences, and contact institutional support.

---

## 📐 Screen Layout: Student Profile & Settings Screen (`/student/profile`)

```
+---------------------------------------------------------------------------------------------------+
|  PAGE HEADER: Student Profile & Institutional Settings                                            |
|  [ 👤 Academic Profile ]   [ 📄 Resumes & Documents ]   [ ⚙️ Settings ]   [ ❓ Support & TPO ]    |
+---------------------------------------------------------------------------------------------------+
|  SECTION 1: PERSONAL & ACADEMIC INFORMATION                                                       |
|  +----------------------------------------------------------------------------------------------+  |
|  | [PROFILE PHOTO]  Yashvi Bansal                                                               |  |
|  | Student Roll No: 2026CSE042  |  College: IIT Delhi (Partner Institution)                      |  |
|  | Degree: B.Tech Computer Science & Engineering  |  Current Semester: Semester 6 (2026 Batch)     |  |
|  | College Email: yashvi.bansal@cse.iitd.ac.in  |  Mobile: +91 98765 43210                        |  |
|  +----------------------------------------------------------------------------------------------+  |
|                                                                                                   |
|  SECTION 2: RESUME & ACADEMIC VERIFICATION DOCUMENTS                                              |
|  +----------------------------------------------------------------------------------------------+  |
|  | Primary Resume: [ 📄 Yashvi_Bansal_Software_Eng_2026.pdf ] (Verified by TPO)                  |  |
|  | Secondary Resume: [ 📄 Yashvi_Bansal_Data_Analyst_2026.pdf ]                                   |  |
|  | CGPA Transcript: [ 📄 Semester_5_Official_Transcript.pdf ]                                    |  |
|  | [ 📤 Upload New Resume Version ]                                                             |  |
|  +----------------------------------------------------------------------------------------------+  |
|                                                                                                   |
|  SECTION 3: NOTIFICATION & COMMUNICATION PREFERENCES                                              |
|  +----------------------------------------------------------------------------------------------+  |
|  | [✓] Receive Instant WhatsApp Notifications for Urgent Placement Drives                         |  |
|  | [✓] Receive Email Reminders for Upcoming Exam Deadlines                                        |  |
|  | [✓] Receive SMS Alerts for Scheduled 1-on-1 Mentor Calls                                       |  |
|  | [ Save Preferences ]                                                                           |  |
|  +----------------------------------------------------------------------------------------------+  |
+---------------------------------------------------------------------------------------------------+
```

---

## 🎨 Key Component Specifications

### 1. Read-Only Academic Fields
- Fields verified by the college (Roll Number, CGPA, Branch, Graduation Year) are set to **Read-Only** with a lock icon.
- Tooltip: *"Academic fields are pre-verified by your College TPO. Contact placement office to request changes."*

### 2. Resume Version Manager
- Allows students to store multiple resume versions (e.g. *Software Engineer*, *Data Analyst*).
- Indicates which resume is marked as **Primary** for 1-click job drive applications.
