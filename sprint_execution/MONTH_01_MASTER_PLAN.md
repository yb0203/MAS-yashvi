# MAS AI Labs — Month 1 Master Execution Plan

**Period**: September 1 – September 30, 2026 (Kickoff: Tuesday, Sept 1)  
**Function Head**: Gaurav (CTO) | **AI PM Lead**: Yashvi  
**Focus**: Foundation & Gap Definition (Both flagship suites are already live inside MAS; Month 1 establishes product stability, cost visibility, client intake gates, and gap analysis for externalization. No new suite features).  
**Overall Status**: 🟢 ON TRACK  

---

## 🏛️ 1. Executive Overview of the 4 Compartments

To transform MAS AI Labs from an internal engineering team into a **product-led AI capability engine**, all Month 1 activities are divided into **4 distinct, interconnected compartments**.

```
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                          MAS AI LABS — 4 OPERATING COMPARTMENTS                           │
├───────────────────────────────┬───────────────────────────────────────────────────────────┤
│ 1. Market, Intake & POCs      │ Standard Intake Gate | 3 Client POC Scopes | Catalogues   │
│ 2. Product & Demo Stability   │ P0 Bug Squashing | Clean Demo Envs | Gap Sheet (Tenancy)  │
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
  3. **Product Catalogue v1 & Capability Registry v1 (Day 14: Mon, Sept 14)**: Published reference assets defining the exact scope, use cases, demo readiness, and reusable AI engines powering both suites.

### 📦 Compartment 2: Product & Demo Stabilisation
* **Leadership**: Shubham (Tech Lead) & Rohan (SDE-2)
* **Strategic Purpose**: Both flagship suites (**Learning Suite** and **Sales & Admin Suite**) are actively running MAS operations today. The goal is to make them rock-solid, client-safe, and demo-ready on 24 hours' notice.
* **Key Month 1 Deliverables**:
  1. **P0 Bug Squashing & Demo Readiness (Day 25: Fri, Sept 25)**: Zero critical blocker bugs; 100% demo-ability on demand across both suites.
  2. **Sanitized Demo Environments (Week 2: Sept 7–11)**: Staging environments seeded with realistic, non-MAS sample students, courses, and CRM leads (zero proprietary MAS PII leakage).
  3. **Externalisation Gap Sheet (Day 18: Fri, Sept 18)**: Honest technical audit defining what breaks outside MAS (multi-tenancy, RBAC, data isolation, white-labeling, onboarding, and cost-to-serve) to form the Month 2/3 engineering backlog.

### 📦 Compartment 3: Cloud, Cost & Internal Automation
* **Leadership**: Rohan (SDE-2) & Shubham (Tech Lead)
* **Strategic Purpose**: Make technology economics visible, eliminate cloud waste, attribute AI token spend, and deliver measurable internal automation value back to MAS.
* **Key Month 1 Deliverables**:
  1. **GCP + AWS Cleanup & Restructuring (Day 25: Fri, Sept 25)**: Deletion of idle VMs, orphaned disks, and unassociated static IPs; standardized cost tagging by environment and product.
  2. **AI Cost Instrumentation Baseline (Day 21: Mon, Sept 21)**: Real-time token and API spend logging across OpenAI, Anthropic, Gemini, and Whisper to calculate cost-per-user and cost-to-serve.
  3. **First Internal AI Automation Workflow (Day 28: Mon, Sept 28)**: Launch 1 high-value departmental workflow to production with measured weekly hours saved.

### 📦 Compartment 4: Leadership, Compute & Enablers
* **Leadership**: Gaurav (CTO)
* **Strategic Purpose**: Maintain function-wide governance, secure critical hiring capacity, lead the GPU compute transition, and close foundational financial baselines.
* **Key Month 1 Deliverables**:
  1. **Weekly Product & Capability Review (Every Friday 8:00 PM IST)**: Enforces scope discipline, audits ad-hoc workload percentages, and resolves blockers.
  2. **QA & PM Intern Fulfillment (Day 21: Mon, Sept 21)**: QA Tester onboarded for P0 regression; PM Intern onboarded for client and catalogue tracking.
  3. **September GPU / Compute Track (Day 30: Wed, Sept 30)**: Hardware options, vendor discussions, and self-hosted model serving architecture evaluated with Sajan.
  4. **Financial Baselines & Month-End Report (Day 30: Wed, Sept 30)**: Reconcile 6-month revenue target, monthly AI Labs run-rate, and publish Month 2 backlog.

---

## 🎯 2. Month 1 Commitments Dashboard (11 Targets)

| # | Commitment & KPI | Compartment | Lead Owner (Support) | Target Date (Day) | Assigned Sprint(s) | Status | Delivered Outcome | Active Blockers & Delay Reasons | RAG |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|---|:---:|
| **1** | **Advance Orane, College Vidya & Chitkara to agreed POC scope**<br>*KPI: 3 written POC scopes accepted by client & Business* | **C1: Market & Intake** | Yashvi *(Prakhar, Shubham)* | **Sept 20 (Day 20)** | Sprint 1, 2, 3 | `[ ] Planned` | - | None | 🟢 |
| **2** | **P0 stabilisation & demo readiness across both live suites**<br>*KPI: 100% P0 demo-able on 24h notice; critical bug count at zero* | **C2: Product & Demo** | Shubham *(Rohan, QA)* | **Sept 25 (Day 25)** | Sprint 1, 2, 3, 4 | `[ ] Planned` | - | None | 🟢 |
| **3** | **Externalisation gap sheet for both suites**<br>*KPI: Modules live today, what breaks outside MAS, effort & cost-to-serve* | **C2: Product & Demo** | Prakhar *(Shubham, Gaurav)* | **Sept 18 (Day 18)** | Sprint 2, 3 | `[ ] Planned` | - | None | 🟢 |
| **4** | **AI cost instrumentation & GCP/AWS cleanup**<br>*KPI: Product-level token / API / infra spend visible for live workloads* | **C3: Cloud & Cost** | Rohan *(Shubham)* | **Sept 21 (Day 21)** | Sprint 1, 2, 3 | `[ ] Planned` | - | None | 🟢 |
| **5** | **Publish Product Catalogue v1 & Capability Registry v1**<br>*KPI: Catalogue v1 complete; Registry v1 seeded from live suites* | **C1: Market & Intake** | Prakhar *(Catalogue)*<br>Yashvi *(Registry)* | **Sept 14 (Day 14)** | Sprint 1, 2, 3 | `[ ] Planned` | - | None | 🟢 |
| **6** | **Business-to-Tech intake format signed off**<br>*KPI: Joint format signed off with Pranab Sir; live from Day 11 (Sept 11)* | **C1: Market & Intake** | Prakhar *(with Pranab Sir)* | **Sept 10 (Day 10)** | Sprint 1, 2 | `[ ] Planned` | - | None | 🟢 |
| **7** | **Launch first internal automation workflow**<br>*KPI: 1 workflow live; hours saved per week measured* | **C3: Cloud & Cost** | Rohan *(Gaurav selection)* | **Sept 28 (Day 28)** | Sprint 2, 3, 4 | `[ ] Planned` | - | None | 🟢 |
| **8** | **Secure QA capacity & onboard PM Intern**<br>*KPI: QA coverage active on P0 regression; intern onboarded* | **C4: Leadership** | Gaurav *(with HR/Admin)* | **Sept 21 (Day 21)** | Sprint 1, 2, 3 | `[ ] Planned` | - | None | 🟢 |
| **9** | **Start weekly product/capability review cadence**<br>*KPI: Weekly review running every Friday at 8:00 PM IST* | **C4: Leadership** | Gaurav | **Sept 4 (Week 1)** | Sprint 1, 2, 3, 4 | `[ ] Planned` | - | None | 🟢 |
| **10**| **Start September GPU / compute setup track**<br>*KPI: Compute option, vendor contact, architecture & cost plan ready* | **C4: Leadership** | Gaurav *(with Sajan)* | **Sept 30 (Day 30)** | Sprint 1, 2, 3, 4 | `[ ] Planned` | - | None | 🟢 |
| **11**| **MAS AI Labs website & Info ID**<br>*KPI: Website live without consuming core engineering capacity* | **C4: Leadership** | Marketing / Vendor *(Prakhar/Gaurav)* | **Sept 30 (Day 30)** | Sprint 1, 2, 3, 4 | `[ ] Planned` | - | None | 🟢 |

---

## ⚠️ 3. Consolidated Blockers & Delay Log (Cross-Sprint View)

| Log ID | Date Flagged | Source Sprint | Task ID & Owner | Blocker Description | Root Cause / Reason | Impact & Target Resolution Date | Status |
|:---:|:---:|:---:|:---:|---|---|---|:---:|
| - | - | - | - | *No active blockers logged yet* | - | - | `🟢 Clear` |

---

## 📊 4. Workload Visibility & Ad-Hoc Share Guardrail

* **Work Discipline Rule**: 
  - **70–80%** Capacity $\rightarrow$ Core Product & Reusable AI Capabilities.
  - **Maximum 20–30%** Capacity $\rightarrow$ Ad-hoc / Cross-departmental MAS Support & Custom Requests.
* **Anti-Agency Guardrail**: If ad-hoc MAS requests exceed 30% of total team effort across two consecutive weeks, new requests must displace a named commitment via the Friday review.

| Sprint Window | Primary Work Taking Time (Core Focus) | Incoming Ad-Hoc Requests (Description & Source) | Est. Ad-Hoc Effort Share (%) | Guardrail Status |
|---|---|---|:---:|:---:|
| **Sprint 1 (Sept 1–4)** | P0 product freeze, bug triage, cloud & API inventories, client context dossiers | *None logged yet* | `0%` | `🟢 Healthy (≤ 30%)` |
| **Sprint 2 (Sept 7–11)** | P0 bug fixing, clean demo envs, intake sign-off, client scoping calls | *None logged yet* | `0%` | `🟢 Healthy (≤ 30%)` |
| **Sprint 3 (Sept 14–18)** | Externalisation gap sheet, 3 POC scopes, cost baseline, QA onboarding | *None logged yet* | `0%` | `🟢 Healthy (≤ 30%)` |
| **Sprint 4 (Sept 21–30)** | P0 demo readiness sign-off, automation live, GPU track, Month 1 report | *None logged yet* | `0%` | `🟢 Healthy (≤ 30%)` |

---

## ✅ 5. Month 1 Success Checklist (Due by Sept 30 / Day 30)

- [ ] P0 products can be demoed on 24-hour notice without a scramble.
- [ ] Critical P0 bugs are cleared (zero critical bugs).
- [ ] Demo environments are clean, curated, and client-safe (no MAS-only clutter).
- [ ] GCP and AWS are cleaned, structured, and documented.
- [ ] Orane, College Vidya, and Chitkara have agreed, written scopes accepted by client and Business.
- [ ] Business $\rightarrow$ Tech intake process is live and used for 100% of new requests.
- [ ] Product Catalogue v1 is published.
- [ ] Capability Registry v1 is published.
- [ ] Externalisation gaps are documented (multi-tenancy, RBAC, data isolation, cost-to-serve).
- [ ] AI/API cost baseline is available and visible per workload.
- [ ] First internal automation workflow is live with measured hours saved per week.
- [ ] QA capacity is active on P0 regression testing.
- [ ] PM Intern is onboarded with clear weekly tracking tasks.
- [ ] Ad-hoc MAS work stayed strictly $\le 30\%$ of total engineering workload.
- [ ] GPU / compute preparation has a clear September path with Sajan.
- [ ] MAS AI Labs website + Info ID are live.
- [ ] Month 2 backlog is clearly defined.
