# Sprint 1 (Week 1: Days 1–4) — Set Up, Bug Fixing & Understand

**Function Head**: Gaurav (CTO) | **AI PM Lead**: Yashvi  
**Sprint Window**: Tuesday, Sept 1 (Day 1) – Friday, Sept 4 (Day 4), 2026  
**Daily Standup**: **8:00 PM IST** (Async notes by 7:30 PM) | **Weekly Review**: **Friday, Sept 4 at 8:00 PM IST**  
**Sprint Status**: `[ ] Planned` | **RAG**: 🟢 ON TRACK  

---

## 🎯 Sprint 1 Core Goals (High-Level & Quantifiable)

* **C1: Market & Intake**: Draft Intake Format v1 + compile 3 Client Dossiers (Orane, College Vidya, Chitkara).
* **C2: Product & Demo**: Freeze P0 Product List + **Fix 100% of Critical P0 Blocker Bugs in Week 1** + **Demo #1: Sales Suite (Prakhar)**.
* **C3: Cloud, Cost & Automation**: 100% GCP & AWS Asset Inventory + **Build & Pilot Slack Standup Bot v1.0 (Yashvi)**.
* **C4: Leadership & Enablers**: Hand over QA & PM Intern JDs to HR + launch Friday Review #1 (Sept 4, 8:00 PM).

---

## 📦 Compartment 1: Market, Intake & Client POCs

| ID | Task / Activity | Owner (Support) | Target Date (Day) | Status | Expected Outcome | Actual Outcome | Blocker | Delay Reason | RAG |
|:---:|---|:---:|:---:|:---:|---|---|---|---|:---:|
| **S1.1** | Draft Business $\rightarrow$ Tech Intake Format v1 | **Prakhar** *(Yashvi)* | Thu, Sept 3 (Day 3) | `[ ] Planned` | Standard intake format defining: Who $\rightarrow$ Wants What $\rightarrow$ Context $\rightarrow$ POC $\rightarrow$ Scale $\rightarrow$ Tech expectation | - | None | None | 🟢 |
| **S1.2** | Collect client context: **Orane** | **Yashvi** *(Prakhar)* | Fri, Sept 4 (Day 4) | `[-] In Progress` | Complete background, target audience, scale, missing items identified | - | None | None | 🟢 |
| **S1.3** | Collect client context: **College Vidya** | **Yashvi** *(Prakhar)* | Fri, Sept 4 (Day 4) | `[-] In Progress` | Complete admissions/CRM context, scale, integration requirements | - | None | None | 🟢 |
| **S1.4** | Collect client context: **Chitkara** | **Yashvi** *(Prakhar)* | Fri, Sept 4 (Day 4) | `[-] In Progress` | Complete placement/academic scope, 100-student cohort context | - | None | None | 🟢 |
| **S1.5** | Define schema & draft **Product Catalogue v1** | **Prakhar** *(Gaurav)* | Fri, Sept 4 (Day 4) | `[ ] Planned` | Product, buyer, use case, maturity, demo readiness, limitations | - | None | None | 🟢 |
| **S1.6** | Define schema & seed **Capability Registry v1** | **Yashvi** *(Shubham)* | Fri, Sept 4 (Day 4) | `[!] Blocked` | Core AI capabilities (RAG, Eval, Voice, Parser) mapped to products | - | None | None | 🔴 |

---

## 📦 Compartment 2: Product, In-House LMS & Demo Stabilisation

| ID | Task / Activity | Owner (Support) | Target Date (Day) | Status | Expected Outcome | Actual Outcome | Blocker | Delay Reason | RAG |
|:---:|---|:---:|:---:|:---:|---|---|---|---|:---:|
| **S1.7** | Freeze P0 product/module list & assign owners | **Shubham** *(Rohan)* | Wed, Sept 2 (Day 2) | `[-] In Progress` | Final P0 list with named module owners across both suites | - | None | None | 🟢 |
| **S1.8** | Triage all P0 bugs across live suites by severity | **Shubham** *(Rohan)* | Wed, Sept 2 (Day 2) | `[-] In Progress` | Critical / blocker bug list ready with reproduction steps | - | None | None | 🟢 |
| **S1.9** | **Fix critical / blocking P0 bugs on staging** | **Rohan** *(Shubham)* | **Fri, Sept 4 (Day 4)** | `[ ] Planned` | **Critical blocker issues cleared in Week 1; verified** | - | None | None | 🟢 |
| **S1.10** | Define clean demo environment requirements | **Shubham** *(Rohan)* | Fri, Sept 4 (Day 4) | `[-] In Progress` | Spec sheet for dummy student rosters & sanitized CRM leads | - | None | None | 🟢 |
| **S1.11**| **Demo #1: Sales & Admin Suite Walkthrough** | **Prakhar** *(Shubham)* | **Thu, Sept 3 (Day 3)** | `[ ] Planned` | **Weekday baseline demo of Sales & Admin Suite** | - | None | None | 🟢 |

---

## 📦 Compartment 3: Cloud, Cost & Internal Automation

| ID | Task / Activity | Owner (Support) | Target Date (Day) | Status | Expected Outcome | Actual Outcome | Blocker | Delay Reason | RAG |
|:---:|---|:---:|:---:|:---:|---|---|---|---|:---:|
| **S1.12**| Inventory current GCP projects, services & VMs | **Rohan** *(Shubham)* | Thu, Sept 3 (Day 3) | `[ ] Planned` | Complete GCP infrastructure inventory with instance sizes | - | None | None | 🟢 |
| **S1.13**| Inventory AWS accounts/services used by AI Labs | **Rohan** *(Shubham)* | Fri, Sept 4 (Day 4) | `[ ] Planned` | Complete AWS inventory (S3, compute, IAM) | - | None | None | 🟢 |
| **S1.14**| Master inventory of AI/API keys, models & endpoints | **Rohan** *(Shubham)* | Fri, Sept 4 (Day 4) | `[ ] Planned` | All third-party AI keys mapped to product modules | - | None | None | 🟢 |
| **S1.15**| Collect top repetitive workflows across MAS departments | **Rohan** *(Gaurav)* | Fri, Sept 4 (Day 4) | `[ ] Planned` | Departmental automation intake list (Problem $\rightarrow$ Effort $\rightarrow$ Value) | - | None | None | 🟢 |
| **S1.16** | **Build & configure MAS Slack Standup Bot v1.0** | **Yashvi** *(Rohan)* | **Thu, Sept 3 (Day 3)** | `[-] In Progress` | **Personal DMs, dropdown modal, 7:45 PM summary & 2-way sync** | - | None | None | 🟢 |
| **S1.17** | **Test & pilot Slack Standup Bot with core team** | **Yashvi** *(All)* | **Fri, Sept 4 (Day 4)** | `[-] In Progress` | **Live test during Friday standup & Friday review #1** | - | None | None | 🟢 |

---

## 📦 Compartment 4: Leadership, Compute & Enablers

| ID | Task / Activity | Owner (Support) | Target Date (Day) | Status | Expected Outcome | Actual Outcome | Blocker | Delay Reason | RAG |
|:---:|---|:---:|:---:|:---:|---|---|---|---|:---:|
| **S1.18** | Kick off QA Tester (contract/2-mo) hiring | **Gaurav** *(HR/Admin)* | Tue, Sept 1 (Day 1) | `[-] In Progress` | Active job description & candidate pipeline with HR | - | None | None | 🟢 |
| **S1.19**| Kick off PM Intern (25 hrs/wk) hiring | **Gaurav** *(HR/Admin)* | Tue, Sept 1 (Day 1) | `[ ] Planned` | Active job description & candidate sourcing | - | None | None | 🟢 |
| **S1.20**| Initial September GPU/compute sync with Sajan | **Gaurav** *(Sajan)* | Thu, Sept 3 (Day 3) | `[ ] Planned` | Compute vendor contacts & initial workload candidate list | - | None | None | 🟢 |
| **S1.21**| **Weekly Product & Capability Review #1 (8:00 PM)** | **Gaurav** *(All)* | Fri, Sept 4 (Day 4) | `[ ] Planned` | Review minutes, Week 1 bug fix verification & RAG audit | - | None | None | 🟢 |

---

## 📊 Workload & Ad-Hoc Effort Tracking (Sprint 1)
* **Primary Work Consuming Time (Time Sinks)**: `[Log key focus areas / deep work items]`
* **Incoming Ad-Hoc MAS Requests**: `[Log any incoming ad-hoc or custom requests]`
* **Estimated Ad-Hoc Workload Share**: `0%` *(Guardrail: Must stay ≤ 20–30% of total team effort)*

---

## 📝 Daily Quick Updates Log
* **Tue, Sept 1 (Day 1)**: **Post-Standup Call Summary (Sprint 1 | Day 1)**:
   ↳ **Pod Deliverable Discussions**:
     • **Yashvi**: `S1.9`: Coordinate & track weekly P0 bug fixes with engineering.
     • **Shubham**: `S1.8`: Triage all P0 bugs across live suites by severity levels.; `S1.10`: Define requirements for a clean demo environment.; `S1.5 / S1.7`: Document technical pointers for product catalog.
     • **Rohan**: `S1.12`: Investigate GCP project scope, services, and VM instances.; `S1.14`: Evaluate Learning Suite and secondary pipeline.
     • **Prakhar**: `S1.1`: Draft Business ➔ Tech Intake Format v1.
     • **Gaurav**: `S1.18 / S1.19`: QA Tester & PM Intern hiring pipelines active.
   ↳ **✨ New Action Items Added from Call**:
     • 🆕 Shubham: Create technical documentation & research plan for Sales Suite setup.
   ↳ **🎯 Formal Decisions & Alignments**:
     • Adopt 16:9 aspect ratio standard for video content.
     • Bug hunter response time interval set to 48 hours.
     • Yashvi Bansal leading daily scrum & tracking updates via GitHub/Excel.

* **Tue, Sept 1 (Day 1)**: **Daily Scrum Highlights (Day 1 — Google Meet Gemini)**:
   ↳ **Summary**: The meeting covered team leadership changes, technical infrastructure updates, and consensus on video content standards.
   ↳ **Key Decisions & Alignment**:
   • Bug hunter response time: The bug hunter response time interval is set to 48 hours.
   • Social Media Video: Adopt 16:9 aspect ratio for all social media video content.
   • Daily Scrum Leadership: Yashvi Bansal to lead daily scrum and manage task updates via GitHub/Excel.
   ↳ **Assigned Next Steps**:
   • [The group] Triage P0 Bugs: Triage all P0 bugs across the live suite by severity levels.
   • [The group] Define Requirements: Define the requirements for a clean demo environment.
   • [Shubham Patel] Document Salesuit Plan: Create a technical documentation and research plan for the salesuit code and generalized setup.
   • [Rohan kr. pandey] Understand GCP Scope: Review current Google Cloud Platform project services and virtual machines to understand the project scope.
   • [Rohan kr. pandey] Review Learning Suite: Evaluate the learning suite and second based pipeline.
 (Bot & Owner Feed)
* *Tue, Sept 1 (Day 1)*: 
* *Wed, Sept 2 (Day 2)*: 
* *Thu, Sept 3 (Day 3)*: 
* *Fri, Sept 4 (Day 4)*: 
