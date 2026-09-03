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
| **S1.1** | Draft Business $\rightarrow$ Tech Intake Format v1 | **Prakhar** *(Yashvi)* | Thu, Sept 3 (Day 3) | `[-] In Progress` | Standard intake format defining: Who $\rightarrow$ Wants What $\rightarrow$ Context $\rightarrow$ POC $\rightarrow$ Scale $\rightarrow$ Tech expectation | Creating client contact intake sheet in Google Sheet format | None | None | 🟡 |
| **S1.2** | Collect client context: **Orane** | **Yashvi** *(Prakhar)* | Fri, Sept 4 (Day 4) | `[ ] Planned` | Complete background, target audience, scale, missing items identified | Will start today | None | None | ⚪ |
| **S1.3** | Collect client context: **College Vidya** | **Yashvi** *(Prakhar)* | Fri, Sept 4 (Day 4) | `[ ] Planned` | Complete admissions/CRM context, scale, integration requirements | Will start today | None | None | ⚪ |
| **S1.4** | Collect client context: **Chitkara** | **Yashvi** *(Prakhar)* | Fri, Sept 4 (Day 4) | `[ ] Planned` | Complete placement/academic scope, 100-student cohort context | Will start today | None | None | ⚪ |
| **S1.5** | Define schema & draft **Product Catalogue v1** | **Prakhar** *(Gaurav)* | Fri, Sept 4 (Day 4) | `[ ] Planned` | Product, buyer, use case, maturity, demo readiness, limitations | - | None | None | ⚪ |
| **S1.6** | Define schema & seed **Capability Registry v1** | **Yashvi** *(Shubham)* | Fri, Sept 4 (Day 4) | `[x] Completed` | Core AI capabilities (RAG, Eval, Voice, Parser) mapped to products | Need to update it at end of the month | Need to discuss the artifacts required for capability mapping | None | 🟢 |

---

## 📦 Compartment 2: Product, In-House LMS & Demo Stabilisation

| ID | Task / Activity | Owner (Support) | Target Date (Day) | Status | Expected Outcome | Actual Outcome | Blocker | Delay Reason | RAG |
|:---:|---|:---:|:---:|:---:|---|---|---|---|:---:|
| **S1.7** | Freeze P0 product/module list & assign owners | **Shubham** *(Rohan)* | Wed, Sept 2 (Day 2) | `[x] Completed` | Final P0 list with named module owners across both suites | - | None | None | 🟢 |
| **S1.8** | Triage all P0 bugs across live suites by severity | **Shubham** *(Rohan)* | Wed, Sept 2 (Day 2) | `[ ] Planned` | Critical / blocker bug list ready with reproduction steps | - | None | None | ⚪ |
| **S1.9** | **Fix critical / blocking P0 bugs on staging** | **Rohan** *(Shubham)* | **Fri, Sept 4 (Day 4)** | `[-] In Progress` | **Critical blocker issues cleared in Week 1; verified** | Email delivery bug fixed; info email account migrated; testing pipeline | GPT credit exhausted | None | 🔴 |
| **S1.10** | Define clean demo environment requirements | **Shubham** *(Rohan)* | Fri, Sept 4 (Day 4) | `[ ] Planned` | Spec sheet for dummy student rosters & sanitized CRM leads | - | None | None | ⚪ |
| **S1.11** | **Demo #1: Sales & Admin Suite Walkthrough** | **Prakhar** *(Shubham)* | **Thu, Sept 3 (Day 3)** | `[ ] Planned` | **Weekday baseline demo of Sales & Admin Suite** | - | None | None | ⚪ |
| **S1.22** | Sales Suite technical documentation & research plan | **Shubham** | Fri, Sept 4 (Day 4) | `[x] Completed` | Technical architecture doc & generalized setup plan | Sales Suite prototype presented (DB separation & lead import); backend analysis underway | None | None | 🟢 |

---

## 📦 Compartment 3: Cloud, Cost & Internal Automation

| ID | Task / Activity | Owner (Support) | Target Date (Day) | Status | Expected Outcome | Actual Outcome | Blocker | Delay Reason | RAG |
|:---:|---|:---:|:---:|:---:|---|---|---|---|:---:|
| **S1.12** | Inventory current GCP projects, services & VMs | **Rohan** *(Shubham)* | Thu, Sept 3 (Day 3) | `[!] Blocked` | Complete GCP infrastructure inventory with instance sizes | - | GPT credit exhausted | None | 🔴 |
| **S1.13** | Inventory AWS accounts/services used by AI Labs | **Rohan** *(Shubham)* | Fri, Sept 4 (Day 4) | `[ ] Planned` | Complete AWS inventory (S3, compute, IAM) | - | GPT credit exhausted | None | 🔴 |
| **S1.14** | Master inventory of AI/API keys, models & endpoints | **Rohan** *(Shubham)* | Fri, Sept 4 (Day 4) | `[ ] Planned` | All third-party AI keys mapped to product modules | - | GPT credit exhausted | None | 🔴 |
| **S1.15** | Collect top repetitive workflows across MAS departments | **Rohan** *(Gaurav)* | Fri, Sept 4 (Day 4) | `[ ] Planned` | Departmental automation intake list (Problem $\rightarrow$ Effort $\rightarrow$ Value) | - | GPT credit exhausted | None | 🔴 |
| **S1.16** | **Build & configure MAS Slack Standup Bot v1.0** | **Yashvi** *(Rohan)* | **Thu, Sept 3 (Day 3)** | `[-] In Progress` | **Personal DMs, dropdown modal, 7:45 PM summary & 2-way sync** | slack bot formatting fixing in progress | None | None | 🟡 |
| **S1.17** | **Test & pilot Slack Standup Bot with core team** | **Yashvi** *(All)* | **Fri, Sept 4 (Day 4)** | `[-] In Progress` | **Live test during Friday standup & Friday review #1** | Testing daily summaries and improve the AI summarisation | None | None | 🟡 |

---

## 📦 Compartment 4: Leadership, Compute & Enablers

| ID | Task / Activity | Owner (Support) | Target Date (Day) | Status | Expected Outcome | Actual Outcome | Blocker | Delay Reason | RAG |
|:---:|---|:---:|:---:|:---:|---|---|---|---|:---:|
| **S1.18** | Kick off QA Tester (contract/2-mo) hiring | **Gaurav** *(HR/Admin)* | Tue, Sept 1 (Day 1) | `[-] In Progress` | Active job description & candidate pipeline with HR | - | None | None | 🟡 |
| **S1.19** | Kick off PM Intern (25 hrs/wk) hiring | **Gaurav** *(HR/Admin)* | Tue, Sept 1 (Day 1) | `[ ] Planned` | Active job description & candidate sourcing | - | None | None | ⚪ |
| **S1.20** | Initial September GPU/compute sync with Sajan | **Gaurav** *(Sajan)* | Thu, Sept 3 (Day 3) | `[ ] Planned` | Compute vendor contacts & initial workload candidate list | - | None | None | ⚪ |
| **S1.21** | **Weekly Product & Capability Review #1 (8:00 PM)** | **Gaurav** *(All)* | Fri, Sept 4 (Day 4) | `[ ] Planned` | Review minutes, Week 1 bug fix verification & RAG audit | - | None | None | ⚪ |

---

## 📊 Workload & Ad-Hoc Effort Tracking (Sprint 1)
* **Primary Work Consuming Time (Time Sinks)**: `[Log key focus areas / deep work items]`
* **Incoming Ad-Hoc MAS Requests**: `[Log any incoming ad-hoc or custom requests]`
* **Estimated Ad-Hoc Workload Share**: `0%` *(Guardrail: Must stay ≤ 20–30% of total team effort)*

---

## 📝 Daily Quick Updates Log

### 📅 Wed, Sept 2 (Day 2) — Standup Call Summary & Highlights

* **👤 Yashvi**:
  * `S1.16 / S1.17`: Slack bot integrated with Gmail & Gemini LLM for automated standup summaries.
  * `S1.2 – S1.4`: Initiating client context dossiers (Orane, College Vidya, Chitkara).
  * `S1.6`: Aligned on Week 2 demo readiness; assigning primary & technical component owners.
* **👤 Shubham**:
  * `S1.10 / S1.22`: Presented Sales Suite prototype featuring dedicated client login & database separation.
  * `S1.8`: Triaging live suite bugs and conducting backend technical evaluation of Sales Suite.
  * Proposed revenue model for WhatsApp campaigns (Meta/Google Ads integration).
* **👤 Rohan**:
  * `S1.9`: Fixed email delivery bug; completed 'info' email account migration to clear clutter.
  * `S1.9`: Coordinating with Yashvi to stabilize Student Admin dashboard with seeded data.
* **👤 Prakhar**:
  * `S1.1`: Creating client contact intake sheet in Google Sheet format.
  * `S1.5 / S1.11`: Aligning Product Catalogue schema for Week 2 demos.
* **👤 Gaurav**:
  * `S1.18 / S1.19`: Steered prototype direction; confirmed Week 2/3 demo readiness milestones.
* **🎯 Key Decisions & Alignments**:
  * Defined component ownership (primary & technical owners) for Learning and Sales suites.
  * Prioritize core feature parity for Sales Suite launch over monetization/billing.
  * Sales Suite sequence: P0 Bug Fixes ➔ Technicalization ➔ Component-wise Imports.
  * Approved Sales Suite architecture with database-level separation & independent client scaling.
* **✨ New Action Items from Call**:
  * 🆕 Shubham: Distribute Sales Suite prototype artifact to the team.
  * 🆕 Shubham: Conduct backend analysis and evaluate component-wise import jobs.
  * 🆕 Rohan & Yashvi: Align Student Admin dashboard with seeded test data.

### 📅 Tue, Sept 1 (Day 1) — Standup Call Summary & Highlights
* **👤 Yashvi**:
  * `S1.9`: Coordinate & track weekly P0 bug fixes with engineering.
* **👤 Shubham**:
  * `S1.8`: Triage all P0 bugs across live suites by severity levels.
  * `S1.10`: Define requirements for a clean demo environment.
  * `S1.5 / S1.7`: Document technical pointers for product catalog.
  * 🆕 `S1.22`: Create technical documentation & research plan for Sales Suite setup.
* **👤 Rohan**:
  * `S1.12`: Investigate GCP project scope, services, and VM instances.
  * `S1.14`: Evaluate Learning Suite and secondary pipeline.
* **👤 Prakhar**:
  * `S1.1`: Draft Business ➔ Tech Intake Format v1.
* **👤 Gaurav**:
  * `S1.18 / S1.19`: QA Tester & PM Intern hiring pipelines active.
* **🎯 Key Decisions & Alignments**:
  * Adopted **16:9** aspect ratio standard for all video content.
  * Set bug hunter response time window to **48 hours**.
  * Yashvi Bansal confirmed to lead daily scrum and manage sprint tracking on GitHub/Excel.

---
*(Bot automatically appends the single final daily summary after each evening's standup)*
