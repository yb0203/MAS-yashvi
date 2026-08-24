# MAS Mentor Platform — Master Component Index

This directory contains complete technical & functional specifications for all **10 major platform components** identified across the Claude Artifact (`Mr. Mentor — Mentorship Core`), Technical Guide & Sales Guide PDFs, and Platform Overview Architecture Posters.

---

## 📚 Component Documentation Index

| # | Component Name | Description | Specification Link |
| :-: | :--- | :--- | :--- |
| 1 | **Student Dashboard & Learning Portal** | Student-facing dashboard, progress ribbon, weekly roadmap view, learning support widgets, navigation sidebar, and student API surface. | [`student_dashboard.md`](file:///Users/yashvi/Documents/MAS%20-%20AI%20PM/docs/components/student_dashboard.md) |
| 2 | **Gamification Engine** | XP points, 5 level tiers, daily streak tracker ("On Fire Today"), 6 starter achievement badges, idempotent evaluation engine, and badge popups. | [`gamification_engine.md`](file:///Users/yashvi/Documents/MAS%20-%20AI%20PM/docs/components/gamification_engine.md) |
| 3 | **Roadmap Architecture & Course Builder** | Course entity JSON structure, 7 built-in step types, drag-and-drop authoring, batch mapping layer, prerequisite gating, and bulk JSON import. | [`roadmap_and_course_builder.md`](file:///Users/yashvi/Documents/MAS%20-%20AI%20PM/docs/components/roadmap_and_course_builder.md) |
| 4 | **Sales CRM & Aarya AI Calling Engine** | Lead capture funnel, qualification buckets, ElevenLabs AI voice agent ("Aarya"), predicted interest chips (Hot/Warm/Cold), React Flow nurture automation, and MAS101 PAP legal workflow. | [`sales_crm_and_aarya_ai.md`](file:///Users/yashvi/Documents/MAS%20-%20AI%20PM/docs/components/sales_crm_and_aarya_ai.md) |
| 5 | **Courses, Modules & AI Classrooms** | Classic courses, New Course public marketing catalog (`mas_courses`), Course Plans generating 50–200 AI Classrooms, and `course_modules` structure. | [`courses_and_modules.md`](file:///Users/yashvi/Documents/MAS%20-%20AI%20PM/docs/components/courses_and_modules.md) |
| 6 | **Batch Management & Student Overrides** | Cohort creation workflow, capacity/pricing/document rules, batch KPI analytics, Excel exports, and per-student course override capabilities. | [`batch_management.md`](file:///Users/yashvi/Documents/MAS%20-%20AI%20PM/docs/components/batch_management.md) |
| 7 | **Mr Test — Assessment Engine** | EzExam integration console, online exam proxy, score sync pipeline (`mrtest` schema), roadmap attachment, prerequisite completion threshold gating, and Achiever badge feed. | [`mr_test_engine.md`](file:///Users/yashvi/Documents/MAS%20-%20AI%20PM/docs/components/mr_test_engine.md) |
| 8 | **Mr Learn — Video Learning Engine** | Graphy LMS integration console, video course catalog, learner progress sync (`mrlearn` schema), automated WhatsApp progress nudges, and new-student auto-sync cron. | [`mr_learn_lms.md`](file:///Users/yashvi/Documents/MAS%20-%20AI%20PM/docs/components/mr_learn_lms.md) |
| 9 | **Mentorship & Mentor Experience Engine** | 1-on-1 mentor guidance, token credit system, slot booking workflow, `SlotCompletionService` execution, Collaborator badge unlock, and mentor leaderboard rankings. | [`mentorship_and_mentor_experience.md`](file:///Users/yashvi/Documents/MAS%20-%20AI%20PM/docs/components/mentorship_and_mentor_experience.md) |
| 10 | **System Architecture, Schemas & API Layer** | High-level system architecture, multi-schema PostgreSQL structure (`default`, `mas_crm`, `mrtest`, `mrlearn`), 6 background workers/cron jobs, API route hierarchy, and security standards. | [`system_architecture_and_api.md`](file:///Users/yashvi/Documents/MAS%20-%20AI%20PM/docs/components/system_architecture_and_api.md) |

---

## 🎨 Source Artifact Traceability

The specifications above synthesize information from all 5 provided artifacts:

1. **Claude Artifact**: `https://claude.ai/code/artifact/035028e5-544d-4667-bedb-df1f6b6171db` (*Mr. Mentor — Mentorship Core*)
2. **Technical Guide PDF**: [`Student_Dashboard_TECHNICAL_GUIDE.pdf`](file:///Users/yashvi/Documents/MAS%20-%20AI%20PM/docs/Student_Dashboard_TECHNICAL_GUIDE.pdf)
3. **Sales Guide PDF**: [`Student_Dashbaord_Sales.pdf`](file:///Users/yashvi/Documents/MAS%20-%20AI%20PM/docs/Student_Dashbaord_Sales.pdf)
4. **Technical Overview Poster Image**: [`Stu_Dashboard_Tech.png`](file:///Users/yashvi/Documents/MAS%20-%20AI%20PM/docs/Stu_Dashboard_Tech.png)
5. **Sales Overview Poster Image**: [`Stu_dashboard_sale.png`](file:///Users/yashvi/Documents/MAS%20-%20AI%20PM/docs/Stu_dashboard_sale.png)
