# Private Banking Client Onboarding Transformation

### Redesigning KYC, client onboarding and operating models for a Luxembourg private banking business

> **[Explore the Interactive Transformation Dashboard →](index.html)**

---

## Executive Summary

I built this project as a consulting-style transformation case study focused on **private banking client onboarding**.

I wanted to answer a practical question:

> **How can I reduce onboarding friction and cycle time without weakening risk-based KYC / AML controls?**

I created a reproducible synthetic dataset of **6,000 onboarding cases** and used it to diagnose operational bottlenecks, quantify manual effort, identify transformation opportunities and design a target operating model.

I then translated the analysis into a practical transformation roadmap covering client onboarding, KYC / AML activities, risk-based routing, workflow orchestration, document management, relationship-manager capacity, operational KPIs, target operating model, technology requirements, business case and implementation sequencing.

**Important:** all operational figures in this project are synthetic and are used only to demonstrate my analytical and consulting approach. They do not represent the performance of a real financial institution.

---

## Why I Chose This Topic

I chose private banking onboarding because it sits at the intersection of several areas I want to demonstrate as a Financial Services Consultant:

- strategy
- operating model design
- process optimisation
- business requirements
- regulatory awareness
- data analytics
- technology transformation
- project management
- performance management

---

## Business Challenge

I framed the case around a hypothetical Luxembourg private bank experiencing:

- long onboarding cycle times
- high manual effort
- repeated document requests
- multiple operational hand-offs
- limited case visibility
- increasing compliance complexity

My objective is **not** to remove controls.

Instead, I would redesign the operating model so that the bank can preserve appropriate risk-based controls while reducing avoidable manual work and improving client transparency.

---

## My Analytical Questions

I structured the analysis around six questions:

1. Where is onboarding effort concentrated?
2. Which process steps create the greatest friction?
3. How do risk and client complexity affect cycle time?
4. Where do manual touchpoints and rework create avoidable effort?
5. Which transformation opportunities should I prioritise?
6. What would a more effective target operating model look like?

---

## Dataset

I generated a **fully synthetic dataset of 6,000 private-banking onboarding cases** using a fixed random seed.

Each case includes attributes such as client segment, client type, region, onboarding channel, risk tier, document complexity, missing-document events, manual touchpoints, rework, screening alerts, compliance escalation, cycle time, SLA performance, relationship-manager effort and onboarding outcome.

The dataset is deliberately designed to reproduce realistic operational patterns while remaining completely fictional.

---

## Executive KPI Snapshot

| KPI | Illustrative result |
|---|---:|
| Onboarding cases | **6,000** |
| Average cycle time | **19.7 days** |
| Median cycle time | **18.0 days** |
| SLA compliance | **77.5%** |
| Average RM effort | **~4 hours / case** |
| Cases involving rework | **~50%** |
| High-risk share | **~15%** |

---

## AS-IS Process

I modelled the journey around five stages:

```text
Client Intake
      ↓
Document Collection
      ↓
KYC / AML Assessment
      ↓
Risk & Acceptance Decision
      ↓
Account Opening
```

At a more granular level, I analysed initial data capture, document collection, KYC / identity verification, beneficial ownership review, source of wealth / funds, PEP / sanctions screening, compliance assessment, acceptance approval and account opening.

---

## Operational Diagnosis

I focused on four dimensions:

### Cycle Time

I measured the time from initial intake to onboarding completion.

### SLA Performance

I compared actual cycle time with risk-based illustrative SLA targets.

### Manual Effort

I used manual touchpoints and relationship-manager hours as indicators of operational capacity consumption.

### Rework

I tracked repeated work and missing-document events as potential sources of avoidable delay.

---

## Key Findings

### 1. Document collection is a major source of friction

I found a strong combination of manual touchpoints, missing-document events and rework around document collection.

I would therefore prioritise structured document intake and earlier completeness validation.

### 2. Higher-risk cases require more capacity

Risk tier is associated with longer cycle times and higher operational effort.

I would therefore avoid applying exactly the same workflow to every client and instead introduce risk-based routing with appropriate human oversight.

### 3. Rework creates avoidable delay

Repeated requests and incomplete evidence increase both client friction and internal workload.

I would move completeness checks earlier in the process.

### 4. Relationship-manager capacity is affected by process design

RM effort increases when cases require more manual intervention, rework or escalation.

A single onboarding cockpit could improve both operational efficiency and front-office visibility.

---

## Transformation Opportunity Framework

I prioritised opportunities using four dimensions:

| Dimension | Weight |
|---|---:|
| Business value | **35%** |
| Feasibility | **20%** |
| Risk reduction | **25%** |
| Client experience | **20%** |

This gives me a structured decision framework rather than relying only on perceived impact.

---

## Priority Opportunities

### 1. Digital document intake & completeness validation

I would introduce structured document collection, completeness checks and earlier validation.

### 2. KYC workflow orchestration

I would connect KYC, compliance and approval activities through a transparent workflow.

### 3. Risk-based onboarding routing

I would route cases according to risk and complexity while maintaining appropriate human decision points.

### 4. RM onboarding cockpit

I would give relationship managers a single view of case status, missing documents, blockers, SLA status and next actions.

### 5. Exception & SLA management dashboard

I would make operational bottlenecks visible before they become material delays.

---

## Target Operating Model

My proposed target operating model moves from a largely sequential process towards a **risk-based and orchestrated model**.

```text
                         CLIENT
                           │
                           ▼
                 Digital / Assisted Intake
                           │
                           ▼
                Completeness Validation
                           │
                           ▼
                  Risk-Based Routing
                   ┌───────┼───────┐
                   ▼       ▼       ▼
                 LOW    MEDIUM    HIGH
                   │       │       │
                   └───────┼───────┘
                           ▼
                  KYC / AML Workflow
                           │
                           ▼
                    Acceptance Decision
                           │
                           ▼
                     Account Opening
```

My key principle is:

> **I would automate and simplify the process around the controls, not automate the control decisions themselves.**

---

## Technology & Solution Requirements

### Workflow

- centralised case management
- automated task assignment
- SLA monitoring
- escalation rules
- audit trail

### Document Management

- structured document request lists
- completeness validation
- document status tracking
- reusable evidence
- controlled access

### KYC / AML

- identity verification integration
- beneficial ownership information
- source of wealth / source of funds workflow
- PEP and sanctions screening
- risk-based escalation

### Management Information

- onboarding volume
- cycle time
- SLA performance
- rework
- manual effort
- backlog
- exception rate

---

## Target KPI Framework

I would monitor the transformation through four lenses.

**Client:** onboarding cycle time, client drop-off, document requests, communication frequency.

**Operations:** SLA compliance, backlog, manual touchpoints, rework rate, handling time.

**Compliance:** screening alerts, escalation rate, high-risk turnaround, exception ageing.

**Transformation:** automation rate, straight-through processing, adoption and benefits realised.

---

## Illustrative Business Case

I used conservative scenario assumptions to demonstrate how I would quantify the transformation.

My illustrative target is:

- **~28% reduction in average cycle time**
- **~22% reduction in relationship-manager effort**
- **35% reduction in rework**
- **+12 percentage points in SLA performance**

These are **scenario assumptions**, not observed market or bank results.

I would validate them in a real engagement using historical operational data, process mining, stakeholder interviews and time-and-motion analysis.

---

## Transformation Roadmap

### Phase 1 — Stabilise | 0–3 months

I would establish the KPI baseline, implement an exception dashboard, clarify ownership and define operational SLAs.

### Phase 2 — Simplify | 3–6 months

I would redesign document intake, introduce completeness validation and remove avoidable hand-offs.

### Phase 3 — Orchestrate | 6–12 months

I would implement risk-based routing and workflow orchestration across KYC and approval activities.

### Phase 4 — Scale | 12–18 months

I would deploy a reusable evidence repository and relationship-manager onboarding cockpit.

### Phase 5 — Optimise | 18+ months

I would evaluate advanced automation and AI-assisted document or case processing with appropriate governance and human oversight.

---

## Regulatory Considerations

I deliberately designed the target model around **risk-based AML/CFT principles** rather than treating compliance as an obstacle to efficiency.

The CSSF's private-banking risk assessment highlights customer due diligence at onboarding, individual ML/TF risk assessment, identification and verification, beneficial ownership, source of wealth and funds, screening and enhanced due diligence for higher-risk situations.

The CSSF also clarified in 2026 that supervised entities are expected to **manage ML/FT risks effectively rather than simply avoid them**, while client cooperation and adequate documentation remain important to the onboarding process.

I therefore frame the transformation challenge as:

> **How can I make a controlled, risk-based onboarding process more efficient without weakening the control framework?**

I also consider the broader technology and operational-resilience context. DORA has applied to in-scope financial entities since **17 January 2025**, making technology governance and operational resilience relevant when redesigning financial-services processes.

### Regulatory references

- CSSF — Private Banking Sub-Sector Risk Assessment 2023
- CSSF — AML/CFT framework
- CSSF Circular 12/552
- EU Regulation 2022/2554 — DORA

---

## Consulting Deliverables

| Deliverable | Purpose |
|---|---|
| Executive diagnosis | Summarise the business problem |
| KPI framework | Establish the performance baseline |
| Process analysis | Identify operational bottlenecks |
| Target operating model | Define the future-state model |
| Business requirements | Translate pain points into system needs |
| Transformation prioritisation | Sequence initiatives |
| Business case | Quantify potential benefits |
| Transformation roadmap | Define implementation phases |
| Interactive dashboard | Support management decision-making |

---

## Project Structure

```text
private-banking-client-onboarding-transformation/
│
├── index.html
├── private_banking_onboarding_transformation.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── outputs/
    ├── synthetic_onboarding_cases.csv
    ├── step_performance.csv
    ├── kpi_summary.csv
    ├── monthly_operational_kpis.csv
    ├── transformation_opportunities.csv
    ├── business_case.csv
    ├── transformation_roadmap.csv
    ├── target_operating_model_raci.csv
    ├── monthly_onboarding_volume.png
    ├── step_duration.png
    └── transformation_opportunity_priority.png
```

---

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- HTML
- CSS
- JavaScript
- GitHub Pages

---

## What I Demonstrate Through This Project

Through this case study, I demonstrate how I approach a financial-services transformation problem from **business challenge to implementation roadmap**.

I combine:

**Business understanding → Data → Diagnosis → Operating Model → Technology → Prioritisation → Business Case → Roadmap**

This is the type of approach I would like to contribute to in a **Financial Services Consulting** environment, particularly across banking, private banking and wealth management.

---

## Interactive Dashboard

**[Explore the Private Banking Client Onboarding Transformation Dashboard →](index.html)**

The dashboard is standalone and can be deployed through GitHub Pages without requiring Streamlit or a Python runtime.

---

## Author

**Aishwarya Markandu**

Business Analyst · Change Management · Financial Services · Data & Transformation

I am interested in the intersection of **financial services, business transformation, data analytics and technology**.

[GitHub](https://github.com/AishwaryaMarkandu)
