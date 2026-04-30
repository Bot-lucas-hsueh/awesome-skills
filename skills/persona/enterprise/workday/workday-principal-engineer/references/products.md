# Workday Product Suite Reference

## Human Capital Management (HCM)

### Core Modules

| Module | Function | Key Objects |
|--------|----------|-------------|
| **Workforce Lifecycle** | Hire to retire | Employee, Position, Job Requisition |
| **Organization Management** | Structure & hierarchy | Organization, Cost Center, Location |
| **Compensation** | Pay management | Compensation Plan, Salary Band, Bonus |
| **Benefits** | Enrollment & admin | Benefit Plan, Enrollment, Life Events |
| **Talent Management** | Performance & goals | Performance Review, Goal, 360 Feedback |
| **Learning** | Training & development | Course, Learning Path, Certification |
| **Recruiting** | ATS & CRM | Candidate, Job Application, Offer |
| **Time & Absence** | Tracking & policies | Time Entry, Absence Request, Accrual |
| **Payroll** | Global payroll | Pay Input, Pay Calculation, Payslip |

### HCM Data Model

```
┌─────────────────────────────────────────────────────────────┐
│                    HCM OBJECT RELATIONSHIPS                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Worker (abstract)                                           │
│     ├── Employee                                             │
│     │     ├── Position (1:1 current)                        │
│     │     ├── Compensation (1:many effective dated)         │
│     │     ├── Benefits Enrollment (1:many)                  │
│     │     └── Time Entries (1:many)                         │
│     │                                                        │
│     └── Contingent Worker                                    │
│           └── Supplier Contract                              │
│                                                              │
│  Organization Hierarchy                                      │
│     └── Organization                                         │
│           ├── Cost Center (financial)                       │
│           ├── Department (operational)                      │
│           └── Matrix Team (project-based)                   │
│                                                              │
│  Position Management                                         │
│     └── Position                                             │
│           ├── Job Profile                                    │
│           ├── Location                                       │
│           └── Budget                                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Financial Management

### Finance Modules

| Module | Function | Key Features |
|--------|----------|--------------|
| **General Ledger** | Core accounting | Multi-book, allocations, eliminations |
| **Accounts Payable** | Vendor payments | 3-way matching, invoice scanning |
| **Accounts Receivable** | Customer billing | Revenue recognition, collections |
| **Cash Management** | Banking & liquidity | Bank rec, cash positioning |
| **Asset Management** | Fixed assets | Depreciation, transfers, disposal |
| **Expense Management** | Employee expenses | Mobile capture, policy enforcement |
| **Procurement** | Purchasing | Requisitions, catalogs, approvals |
| **Project & Work** | Project accounting | Billing, capitalization, resources |
| **Grants Management** | Research funding | Effort reporting, compliance |

### Financial Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│                  FINANCIAL TRANSACTION FLOW                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Source Document                                              │
│       │                                                       │
│       ▼                                                       │
│  ┌─────────────┐                                             │
│  │   Expense   │ ──► Approval Workflow                       │
│  │   Report    │                                             │
│  └─────────────┘                                             │
│       │                                                       │
│       ▼                                                       │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐       │
│  │   Journal   │───►│   Ledger    │───►│  Financial  │       │
│  │   Entry     │    │   Account   │    │  Reporting  │       │
│  └─────────────┘    └─────────────┘    └─────────────┘       │
│       │                                                       │
│       ▼                                                       │
│  ┌─────────────┐    ┌─────────────┐                          │
│  │  Adaptive   │◄───│  Budget vs  │                          │
│  │  Planning   │    │  Actuals    │                          │
│  └─────────────┘    └─────────────┘                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Adaptive Planning

### Planning Capabilities

| Capability | Description | Use Case |
|------------|-------------|----------|
| **Financial Planning** | Budgeting & forecasting | P&L, Balance Sheet, Cash Flow |
| **Workforce Planning** | Headcount & skills | Hiring plans, org changes |
| **Operational Planning** | Cross-functional | Sales capacity, marketing spend |
| **Consolidation** | Multi-entity close | Currency conversion, eliminations |
| **Scenario Modeling** | What-if analysis | M&A, market changes |

### Planning Model Structure

```
┌─────────────────────────────────────────────────────────────┐
│              ADAPTIVE PLANNING DIMENSIONS                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  STANDARD DIMENSIONS:                                        │
│  ├── Time (Year > Quarter > Month > Week > Day)             │
│  ├── Version (Actual, Budget, Forecast, Plan)               │
│  ├── Organization (Entity > Department > Cost Center)       │
│  └── Account (GL Account hierarchy)                         │
│                                                              │
│  CUSTOM DIMENSIONS:                                          │
│  ├── Product (Product Line > SKU)                           │
│  ├── Region (Continent > Country > State > City)            │
│  ├── Channel (Direct > Partner > Online)                    │
│  └── Scenario (Base, Upside, Downside, Risk)                │
│                                                              │
│  LEVELS:                                                     │
│  ├── Top Level (Consolidated)                               │
│  ├── Intermediate (Divisions)                               │
│  └── Leaf (Lowest planning unit)                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Workday Student

### Student System Modules

| Module | Function | Key Features |
|--------|----------|--------------|
| **Recruiting** | Admissions CRM | Prospect tracking, events |
| **Admissions** | Application processing | Decisions, deposits |
| **Curriculum** | Academic structure | Programs, courses, requirements |
| **Registration** | Enrollment | Shopping cart, waitlist |
| **Advising** | Student guidance | Degree audit, alerts |
| **Records** | Academic history | Grades, transcripts |
| **Financials** | Student billing | Tuition, payments |
| **Financial Aid** | Funding | Packaging, disbursement |

### Student Data Model

```
┌─────────────────────────────────────────────────────────────┐
│                  STUDENT OBJECT MODEL                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Person (shared with HCM)                                    │
│     └── Student (academic persona)                           │
│           ├── Academic Record                                │
│           │     ├── Program of Study                         │
│           │     ├── Academic Plan                            │
│           │     └── Academic Standing                        │
│           │                                                  │
│           ├── Registration                                   │
│           │     ├── Course Registrations                     │
│           │     ├── Waitlist Entries                         │
│           │     └── Academic Appointments                    │
│           │                                                  │
│           └── Student Financials                             │
│                 ├── Charges (tuition, fees)                  │
│                 ├── Payments                                 │
│                 └── Financial Aid Awards                     │
│                                                              │
│  Course Catalog                                              │
│     └── Course                                               │
│           ├── Academic Units                                 │
│           ├── Prerequisites                                  │
│           └── Course Sections                                │
│                 └── Class Schedule                           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Workday Extend

### Extend Platform Services

| Service | Technology | Purpose |
|---------|------------|---------|
| **Presentation Services** | JSON + JavaScript | Custom UI components |
| **Data Services** | REST APIs + WQL | Data access |
| **Conversation Services** | Bot framework | Chat/messaging |
| **Orchestration Services** | Visual builder | Business process |
| **Integration Services** | REST/SOAP | External connectivity |

### Extend App Types

```
┌─────────────────────────────────────────────────────────────┐
│                  EXTEND APPLICATION TYPES                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  TYPE 1: WORKDAY-HOSTED APP                                  │
│  ├── Runs within Workday UI                                 │
│  ├── Uses Presentation Services                             │
│  ├── Same security model                                    │
│  └── JSON-based UI definition                               │
│                                                              │
│  TYPE 2: INTEGRATED EXTERNAL APP                             │
│  ├── External UI (React, Angular, etc.)                     │
│  ├── Workday APIs for data                                  │
│  ├── OAuth authentication                                   │
│  └── Update-safe integration                                │
│                                                              │
│  TYPE 3: ORCHESTRATION-ONLY                                  │
│  ├── No custom UI                                           │
│  ├── Workflow automation                                    │
│  ├── Integration coordination                               │
│  └── Business process extension                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Integration Tools

### Integration Decision Matrix

| Requirement | Tool | Complexity |
|-------------|------|------------|
| Simple file import/export | EIB | Low |
| Scheduled bulk data sync | EIB + Scheduling | Low |
| Real-time API integration | REST/SOAP APIs | Medium |
| Complex data transformation | Workday Studio | High |
| Third-party pre-built | Core Connectors | Low |
| Custom business process | Orchestration Builder | Medium |
| External application | Extend + APIs | Medium |

### Integration Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  INTEGRATION LANDSCAPE                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  INBOUND (to Workday)                                        │
│  ├── EIB: Bulk data load (CSV, XML)                         │
│  ├── Core Connectors: ADP, Salesforce, etc.                 │
│  ├── Studio: Complex transformations                        │
│  └── API: Real-time programmatic                            │
│                                                              │
│  OUTBOUND (from Workday)                                     │
│  ├── EIB: Scheduled exports                                 │
│  ├── Notification: Event-driven messages                    │
│  ├── Studio: Multi-endpoint orchestration                   │
│  └── API: On-demand requests                                │
│                                                              │
│  STUDIO CAPABILITIES:                                        │
│  ├── XSLT transformations                                   │
│  ├── Multi-step orchestrations                              │
│  ├── Error handling & retry                                 │
│  └── Custom Xpresso logic                                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```
