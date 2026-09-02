# MAS AI Labs — Month 1 Master Execution Plan

**Period**: September 1 – September 30, 2026 (Kickoff: Tuesday, Sept 1)  
**Function Head**: Gaurav (CTO) | **AI PM Lead**: Yashvi  
**Focus**: Foundation, In-House LMS Prototype & Client Intake (Both flagship suites live inside MAS; Month 1 establishes product stability, in-house LMS build to replace Graphy in Mr. Learn, cost visibility, client intake gates, and weekly stakeholder demos. Externalisation Gap Sheet moved to Month 2).  
**Overall Status**: 🟢 ON TRACK  

---

## 🏛️ 1. Executive Overview of the 4 Compartments

```
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                          MAS AI LABS — 4 OPERATING COMPARTMENTS                           │
├───────────────────────────────┬───────────────────────────────────────────────────────────┤
│ 1. Market, Intake & POCs      │ Standard Intake Gate | 3 Client POC Scopes | Catalogues   │
│ 2. Product & Demo Stability   │ Week 1 P0 Bug Fix | 2-Wk In-House LMS Build | Weekly Demos│
│ 3. Cloud, Cost & Automation   │ GCP/AWS Cleanup | AI Spend Attribution | 1st Automation   │
│ 4. Leadership & Enablers      │ Friday Reviews | QA & Intern Sourcing | GPU Compute Track │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

### 📦 Compartment 1: Market, Intake & Client POCs
* **Leadership**: Prakhar (PM - Client / Business-Tech Bridge) & Yashvi (AI PM + FDE)
* **Strategic Purpose**: Establish strict demand gatekeeping with the Business Team (Pranab Sir) and advance active client opportunities without custom code rabbit holes.
* **Key Month 1 Deliverables**:
  1. **Business $\rightarrow$ Tech Intake Process (Day 10: Thu, Sept 10)**: Eliminates unstructured handoffs (*"Here is the client, handle it"* is banned). Mandates structured context on scale, timeline, and tech expectations before engineering touches a lead. (Live from Day 11: Fri, Sept 11).
  2. **3 Written POC Scopes (Day 20: Sun, Sept 20 / Mon, Sept 21)**: Scoping and technical feasibility agreements for **Orane**, **College Vidya**, and **Chitkara**.
  3. **Product Catalogue v1 & Capability Registry v1 (Day 14: Mon, Sept 14)**: Published reference assets defining the exact scope, use cases, demo readiness, and reusable AI engines.

### 📦 Compartment 2: Product, In-House LMS & Demo Stabilisation
* **Leadership**: Shubham (Tech Lead), Rohan (SDE-2), Yashvi (Learning Suite Demos), Prakhar (Sales Suite Demos)
* **Strategic Purpose**: Fix all critical P0 bugs in Week 1, replace Graphy with a proprietary in-house LMS prototype inside `Mr. Learn`, and establish a weekly weekday demo cadence. *(Note: Externalisation Gap Sheet is moved to Month 2)*.
* **Key Month 1 Deliverables**:
  1. **Week 1 Critical P0 Bug Clearing (Sept 1–4)**: Complete bug triage and 100% fix of critical blocker bugs during Sprint 1.
  2. **In-House LMS Creation (Weeks 2–3: Sept 7–18)**: Dedicated 2-week engineering track to build an in-house LMS prototype to replace the third-party Graphy dependency inside `Mr. Learn` / Learning Suite.
  3. **Weekly Weekday Demos (4 Demos in Month 1)**:
     * **Yashvi (Learning Suite)**: 2 demos across the month (Week 2 & Week 4).
     * **Prakhar (Sales & Admin Suite)**: 2 demos across the month (Week 1 & Week 3).
  4. **P0 Stabilisation & Demo Readiness (Day 25: Fri, Sept 25)**: 100% demo-ability on 24h notice across both suites.
  5. **Externalisation Gap Sheet Deferred to Month 2**: Sizing multi-tenancy, RBAC, and data isolation moved to Month 2 to prioritize the in-house LMS prototype.

### 📦 Compartment 3: Cloud, Cost & Internal Automation
* **Leadership**: Rohan (SDE-2) & Shubham (Tech Lead)
* **Strategic Purpose**: Make technology economics visible, eliminate cloud waste, attribute AI token spend, and deliver measurable internal automation value back to MAS.
* **Key Month 1 Deliverables**:
  1. **GCP + AWS Cleanup & Restructuring (Day 25: Fri, Sept 25)**: Deletion of idle VMs, orphaned disks, and unassociated static IPs; standardized cost tagging by environment and product.
  2. **AI Cost Instrumentation Baseline (Day 21: Mon, Sept 21)**: Real-time token and API spend logging across OpenAI, Anthropic, Gemini, and Whisper to calculate cost-per-user and cost-to-serve.
  3. **First Internal AI Automation Workflow (Day 28: Mon, Sept 28)**: Launch 1 high-value departmental workflow to production with measured weekly hours saved.

### 📦 Compartment 4: Leadership, Compute & Enablers
* **Leadership**: Gaurav (CTO) & Yashvi (AI PM)
* **Strategic Purpose**: Maintain function-wide governance, secure critical hiring capacity, lead the GPU compute transition, and run the automated daily standup & weekly review rhythm.
* **Key Month 1 Deliverables**:
  1. **Daily Standup Cadence & Google Meet Gemini Notes (Daily 8:00 PM IST)**: 20-minute focused standup call. Google Meet automatically records Gemini AI meeting notes and transcripts sent to the team email, which the bot ingests to post finalized Day Highlights in `#all-mas-ai-labs` and update the Sprint Log.
  2. **Weekly Product & Capability Review (Every Friday 8:00 PM IST)**: Enforces scope discipline, audits ad-hoc workload percentages, and resolves blockers.
  3. **QA & PM Intern Fulfillment (Day 21: Mon, Sept 21)**: QA Tester onboarded for P0 regression; PM Intern onboarded for client and catalogue tracking.
  4. **September GPU / Compute Track (Day 30: Wed, Sept 30)**: Hardware options, vendor discussions, and self-hosted model serving architecture evaluated with Sajan.
  5. **Financial Baselines & Month-End Report (Day 30: Wed, Sept 30)**: Reconcile 6-month revenue target, monthly AI Labs run-rate, and publish Month 2 backlog.

---

## 🎯 2. Month 1 Commitments Dashboard

| # | Commitment & KPI | Compartment | Lead Owner (Support) | Target Date (Day) | Assigned Sprint(s) | Status | Delivered Outcome | Active Blockers | RAG |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|---|:---:|
| **1** | **Clear Critical P0 Bugs in Week 1**<br>*KPI: 100% critical blocker bugs resolved in Sprint 1* | **C2: Product & Demo** | Rohan *(Shubham)* | **Sept 4 (Day 4)** | Sprint 1 | `[ ] Planned` | - | None | 🟢 |
| **2** | **In-House LMS Prototype Build (Replacing Graphy in Mr. Learn)**<br>*KPI: 2 weeks dedicated build; core LMS prototype functional* | **C2: Product & Demo** | Shubham *(Rohan)* | **Sept 18 (Day 18)** | Sprint 2, 3 | `[ ] Planned` | - | None | 🟢 |
| **3** | **Weekly Demo Cadence (1 Demo/Week Alternating)**<br>*KPI: W1 Prakhar (Sales) ➔ W2 Yashvi (Learning) ➔ W3 Prakhar (Sales) ➔ W4 Yashvi (Learning)* | **C2: Product & Demo** | Prakhar *(W1, W3)*<br>Yashvi *(W2, W4)* | **Weekly (W1–W4)** | Sprint 1, 2, 3, 4 | `[ ] Planned` | - | None | 🟢 |
| **4** | **P0 Stabilisation & 24h Demo Readiness Sign-Off**<br>*KPI: 100% P0 demo-able on 24h notice; zero critical bugs* | **C2: Product & Demo** | Shubham *(Rohan, QA)* | **Sept 25 (Day 25)** | Sprint 1, 2, 3, 4 | `[ ] Planned` | - | None | 🟢 |
| **5** | **Business-to-Tech Intake Format Signed Off**<br>*KPI: Joint format signed off with Pranab Sir; live from Sept 11* | **C1: Market & Intake** | Prakhar *(with Pranab Sir)* | **Sept 10 (Day 10)** | Sprint 1, 2 | `[ ] Planned` | - | None | 🟢 |
| **6** | **Advance Orane, College Vidya & Chitkara to agreed POC scope**<br>*KPI: 3 written POC scopes accepted by client & Business* | **C1: Market & Intake** | Yashvi *(Prakhar, Shubham)* | **Sept 20 (Day 20)** | Sprint 1, 2, 3 | `[ ] Planned` | - | None | 🟢 |
| **7** | **Publish Product Catalogue v1 & Capability Registry v1**<br>*KPI: Catalogue v1 complete; Registry v1 seeded from live suites* | **C1: Market & Intake** | Prakhar *(Catalogue)*<br>Yashvi *(Registry)* | **Sept 14 (Day 14)** | Sprint 1, 2, 3 | `[ ] Planned` | - | None | 🟢 |
| **8** | **AI Cost Instrumentation & GCP/AWS Cleanup**<br>*KPI: Product-level token / API / infra spend visible for live workloads* | **C3: Cloud & Cost** | Rohan *(Shubham)* | **Sept 21 (Day 21)** | Sprint 1, 2, 3 | `[ ] Planned` | - | None | 🟢 |
| **9** | **Launch First Internal AI Automation Workflow**<br>*KPI: 1 workflow live; hours saved per week measured* | **C3: Cloud & Cost** | Rohan *(Gaurav selection)* | **Sept 28 (Day 28)** | Sprint 2, 3, 4 | `[ ] Planned` | - | None | 🟢 |
| **10**| **Secure QA Capacity & Onboard PM Intern**<br>*KPI: QA coverage active on P0 regression; intern onboarded* | **C4: Leadership** | Gaurav *(with HR/Admin)* | **Sept 21 (Day 21)** | Sprint 1, 2, 3 | `[ ] Planned` | - | None | 🟢 |
| **11**| **Start September GPU Track & Live Website**<br>*KPI: Compute plan ready with Sajan; Website + Info ID live* | **C4: Leadership** | Gaurav *(GPU)*<br>Vendor *(Website)* | **Sept 30 (Day 30)** | Sprint 1, 2, 3, 4 | `[ ] Planned` | - | None | 🟢 |

*(Note: Externalisation Gap Sheet is explicitly scheduled as Commitment #1 for Month 2 / October)*.

---

## ⚠️ 3. Consolidated Blockers & Delay Log

| Log ID | Date Flagged | Source Sprint | Task ID & Owner | Blocker Description | Root Cause / Reason | Impact & Target Resolution Date | Status |
|:---:|:---:|:---:|:---:|---|---|---|:---:|
| BLK-01 | Sep 02 | Sprint 1 | `S1.6` (Yashvi) | Need to discuss the artifacts required for capability mapping | None | Under review for unblocking | `🔴 Blocked` |
| BLK-02 | Sep 02 | Sprint 1 | `S1.9` (Rohan) | working on bug hunterz pipeline migrating it to new email and also improving the pipeline | None | Under review for unblocking | `🔴 Blocked` |
| BLK-03 | Sep 02 | Sprint 1 | `S1.16` (Yashvi) | Need to discuss the artifacts required for capability mapping | None | Under review for unblocking | `🔴 Blocked` |
| BLK-04 | Sep 02 | Sprint 1 | `S1.17` (Yashvi) | Need to discuss the artifacts required for capability mapping | None | Under review for unblocking | `🔴 Blocked` |

---

## 📊 4. Workload Visibility & Ad-Hoc Share Guardrail

* **Work Discipline Rule**: 
  - **70–80%** Capacity $\rightarrow$ Core Product, In-House LMS & Capabilities.
  - **Maximum 20–30%** Capacity $\rightarrow$ Ad-hoc / Cross-departmental MAS Support & Custom Requests.
* **Anti-Agency Guardrail**: If ad-hoc MAS requests exceed 30% of total team effort across two consecutive weeks, new requests must displace a named commitment via the Friday review.

| Sprint Window | Primary Work Taking Time (Core Focus) | Incoming Ad-Hoc Requests (Description & Source) | Est. Ad-Hoc Effort Share (%) | Guardrail Status |
|---|---|---|:---:|:---:|
| **Sprint 1 (Sept 1–4)** | P0 product freeze, Week 1 bug fixes, cloud inventories, Demo #1 (Sales) | *None logged yet* | `0%` | `🟢 Healthy (≤ 30%)` |
| **Sprint 2 (Sept 7–11)** | In-House LMS Build (Part 1), intake sign-off, scoping calls, Demo #2 (Learning) | *None logged yet* | `0%` | `🟢 Healthy (≤ 30%)` |
| **Sprint 3 (Sept 14–18)** | In-House LMS Build (Part 2), 3 POC scopes, cost baseline, Demo #3 (Sales) | *None logged yet* | `0%` | `🟢 Healthy (≤ 30%)` |
| **Sprint 4 (Sept 21–30)** | P0 demo readiness sign-off, LMS dry-runs, Demo #4 (Learning), automation live | *None logged yet* | `0%` | `🟢 Healthy (≤ 30%)` |

---

## ✅ 5. Month 1 Success Checklist (Due by Sept 30 / Day 30)

- [ ] Critical P0 bugs are cleared in Week 1.
- [ ] In-House LMS Prototype built and demonstrated inside Mr. Learn (Graphy replacement).
- [ ] 4 structured weekday demos conducted (2 by Yashvi for Learning, 2 by Prakhar for Sales).
- [ ] P0 products can be demoed on 24-hour notice without a scramble.
- [ ] Demo environments are clean, curated, and client-safe (no MAS-only clutter).
- [ ] GCP and AWS are cleaned, structured, and documented.
- [ ] Orane, College Vidya, and Chitkara have agreed, written scopes accepted by client and Business.
- [ ] Business $\rightarrow$ Tech intake process is live and used for 100% of new requests.
- [ ] Product Catalogue v1 is published.
- [ ] Capability Registry v1 is published.
- [ ] AI/API cost baseline is available and visible per workload.
- [ ] First internal automation workflow is live with measured hours saved per week.
- [ ] QA capacity is active on P0 regression testing.
- [ ] PM Intern is onboarded with clear weekly tracking tasks.
- [ ] Ad-hoc MAS work stayed strictly $\le 30\%$ of total engineering workload.
- [ ] GPU / compute preparation has a clear September path with Sajan.
- [ ] MAS AI Labs website + Info ID are live.
- [ ] Month 2 backlog (including Externalisation Gap Sheet) is clearly defined.
