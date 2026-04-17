## §2 · Domain Knowledge

### §2.1 Company Context

**ServiceNow (NYSE: NOW)** — The AI Platform for Business Transformation

| Metric | Value | Context |
|--------|-------|---------|
| **Revenue** | $10.98B+ (FY2024) | Fastest enterprise software to $10B organically |
| **cRPO** | $10.27B (19% YoY) | Strong future revenue visibility |
| **$1M+ ACV Customers** | 2,109+ | Deep enterprise adoption |
| **$5M+ ACV Customers** | 500+ (21% growth) | Strategic platform consolidation |
| **Employees** | 23,000+ | Hiring 3,000+ for AI expansion |
| **Customers** | 8,100+ (85% Fortune 500) | Mission-critical deployments |
| **Platform Uptime** | 99.9%+ SLA | Enterprise-grade reliability |

**Leadership:**
- **Bill McDermott** (Chairman & CEO, since 2019): Former SAP CEO, transformed ServiceNow into "AI platform for business transformation"
- **Fred Luddy** (Founder, Chairman Emeritus): Founded 2004 at age 50, platform visionary
- **Amit Zavery** (President, Head of Product & Engineering, since 2024): Former Google Cloud/Oracle
- **Frank Slootman** (former CEO, 2011-2019): Scaled ServiceNow from startup to enterprise giant

**Headquarters:** Santa Clara, California (Born in the cloud, 2004)

---

### §2.2 Core Product Suite

```
┌─────────────────────────────────────────────────────────────────┐
│                    NOW PLATFORM XANADU                           │
├─────────────────────────────────────────────────────────────────┤
│  AI LAYER: Now Assist, Predictive Intelligence, Virtual Agent   │
├─────────────────────────────────────────────────────────────────┤
│  WORKFLOW LAYER:                                                │
│    • Flow Designer (visual automation)                          │
│    • Integration Hub (200+ spokes)                              │
│    • Process Automation (RPA)                                   │
├─────────────────────────────────────────────────────────────────┤
│  APP ENGINE:                                                    │
│    • App Engine Studio (low-code)                               │
│    • UI Builder (modern experiences)                            │
│    • Mobile Publisher (native apps)                             │
├─────────────────────────────────────────────────────────────────┤
│  ENTERPRISE APPLICATIONS:                                       │
│    • ITSM — Incident, Problem, Change, Request Management       │
│    • ITOM — Event Management, Discovery, Service Mapping, AIOps │
│    • HRSD — Employee onboarding, case management                │
│    • CSM — Customer Service Management                          │
│    • GRC — Governance, Risk, Compliance                         │
│    • ITBM — Strategic Portfolio Management                      │
├─────────────────────────────────────────────────────────────────┤
│  DATA & ANALYTICS:                                              │
│    • CMDB — Configuration Management Database                   │
│    • CSDM — Common Services Data Model                          │
│    • Performance Analytics — Embedded BI                        │
└─────────────────────────────────────────────────────────────────┘
```

---

### §2.3 ITSM (IT Service Management) — Flagship Product

**Core Modules:**

| Module | Purpose | Key Features |
|--------|---------|--------------|
| **Incident** | Restore service fast | Priority matrix, major incident process, SLA tracking |
| **Problem** | Eliminate root causes | Root cause analysis, known error database |
| **Change** | Control changes | Risk calculator, CAB approval, standard changes |
| **Request** | Fulfill service requests | Service Catalog, fulfillment workflows |
| **Asset** | Track IT assets | Hardware/software lifecycle, procurement |
| **Knowledge** | Share information | Article lifecycle, AI-powered search |

**Priority Matrix (Impact × Urgency):**
```
          Urgency
          Low    Medium   High
Impact    ┌─────┬─────┬─────┐
High      │  3  │  2  │  1  │  ← Critical
Medium    │  4  │  3  │  2  │  ← High
Low       │  5  │  4  │  3  │  ← Medium
          └─────┴─────┴─────┘
```

---

### §2.4 ITOM (IT Operations Management)

**Capabilities:**
- **Event Management:** Alert aggregation, correlation, remediation
- **Discovery:** Automatic CI detection and population
- **Service Mapping:** Visualize service dependencies
- **Cloud Operations:** Multi-cloud visibility and management
- **AIOps:** AI-powered anomaly detection and remediation

---

### §2.5 Now Assist — GenAI Integration

**Now Assist Features:**
- **Virtual Agent:** AI-powered chatbot for self-service
- **Predictive Intelligence:** ML-based categorization, routing, resolution
- **Now Assist for ITSM:** Summarize incidents, generate resolution notes
- **Now Assist for Creator:** AI-assisted development

---

### §2.6 Technical Architecture

**Key Technologies:**
- **Glide API:** Server-side scripting (Business Rules, Script Includes)
- **Flow Designer:** Visual workflow automation
- **Integration Hub:** Pre-built connectors for 200+ systems
- **UI Builder:** Modern, responsive interface design
- **Service Portal:** Legacy but still-used interface framework

**GlideRecord Patterns:**
```javascript
// CREATE
var inc = new GlideRecord('incident');
inc.initialize();
inc.short_description = 'Server outage';
inc.caller_id = gs.getUserID();
inc.priority = 1;
var sysId = inc.insert();

// READ with conditions
var gr = new GlideRecord('incident');
gr.addQuery('active', true);
gr.addQuery('priority', '<=', 2);
gr.orderByDesc('priority');
gr.setLimit(100);
gr.query();

while (gr.next()) {
    gs.info(gr.number + ': ' + gr.short_description);
}

// UPDATE batch (performance optimized)
var bulk = new GlideRecord('incident');
bulk.addQuery('state', 1);
bulk.setWorkflow(false);
bulk.autoSysFields(false);
bulk.query();
while (bulk.next()) {
    bulk.state = 7;
    bulk.update();
}
```

---
