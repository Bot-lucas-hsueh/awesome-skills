## 8. Standard Workflow

### 8.1 Phase 1: Requirements & Context

```
Phase 1: Requirements & Context (Day 1–2)
├── Stakeholder Interviews
│   ├── Business: What is the revenue model? What are the growth projections?
│   ├── Product: What features are non-negotiable for launch?
│   ├── Engineering: What is the current team size and skill distribution?
│   └── Operations: What is the on-call maturity? What monitoring exists?
│
├── Quality Attribute Scenarios (QAS)
│   ├── "Under 10,000 concurrent users, the API must respond in p99 < 200ms"
│   ├── "The system must recover from a single AZ failure within 60 seconds"
│   ├── "A feature team of 3 must be able to deploy independently once per day"
│   └── "PCI-DSS Level 1 compliance is required for all payment flows"
│
├── Existing System Audit (for brownfield projects)
│   ├── Dependency map: what calls what?
│   ├── Database schema: what is coupled through shared tables?
│   ├── Deployment units: monolith vs. what is already extracted?
│   └── Incident history: what actually fails in production?
│
├── Constraints Mapping
│   ├── Technology: Existing stack that cannot be replaced
│   ├── Time: Hard deadlines (regulatory, contractual)
│   ├── Budget: Infrastructure cost ceiling
│   └── Team: Skills available, hiring constraints
│
└── [✓ Done]: QAS documented, constraints listed, stakeholders aligned on priorities
    [✗ FAIL]: No clear quality attribute priorities → return to stakeholders; do not design without them
```

### 8.2 Phase 2: Architecture Design

```
Phase 2: Architecture Design (Day 3–7)
├── Pattern Selection
│   ├── Apply decision matrix (§7.1): team size + traffic + operational maturity
│   ├── Rule: default to simplest pattern that meets QAS; escalate only when required
│   └── Document rationale in ADR: why this pattern, what alternatives were considered
│
├── Component Design
│   ├── C4 Level 1: system context (external actors and systems)
│   ├── C4 Level 2: containers (deployable units, databases, queues)
│   ├── C4 Level 3: components (major internal structure of each container)
│   └── Failure mode analysis: for each component, how does it fail gracefully?
│
├── ADR Creation
│   ├── One ADR per significant decision (database choice, communication pattern, auth strategy)
│   ├── Minimum: context, decision, 2 alternatives considered, consequences
│   └── Store in /docs/adr/ in the repository; link from PR descriptions
│
└── Risk Analysis
    ├── Single points of failure: what has no redundancy?
    ├── Data consistency risks: where can split-brain occur?
    ├── Operability risks: what cannot be monitored or rolled back?
    └── [✓ Done]: C4 Level 1+2 complete, ADRs written, risks documented with mitigations
        [✗ FAIL]: Missing failure mode analysis → do not proceed to implementation; failure is the most important case
```

### 8.3 Phase 3: Validation & Governance

```
Phase 3: Validation & Governance (Day 8–14 and ongoing)
├── Architecture Review Board
│   ├── Present C4 diagrams and ADRs to senior engineers + SRE
│   ├── Review checklist: QAS met? Conway's Law aligned? Observability plan?
│   └── Required sign-offs: tech lead, security, SRE lead (for production systems)
│
├── Prototype
│   ├── Build the riskiest component first (not the easiest)
│   ├── Load test at 2× expected peak before committing to the design
│   └── Spike timebox: 3–5 days; output is "go/no-go" on the pattern
│
├── Monitoring Strategy
│   ├── Define SLOs before writing code: availability %, latency p99, error rate
│   ├── Instrument with OpenTelemetry: traces, metrics, structured logs
│   ├── Runbook for each service: what to do when it pages at 3am
│   └── [✓ Done]: SLOs defined, dashboards created, runbooks written, alerting tested
│
└── Evolution Roadmap
    ├── Document: what this architecture cannot handle (the known limitations)
    ├── Define: the trigger conditions for the next architectural evolution
    │   Example: "When write throughput exceeds 5,000/s, introduce CQRS"
    └── [✓ Done]: Documented in README under "Architecture Decisions and Future Evolution"
        [✗ FAIL]: No evolution trigger defined → team will be surprised by scale wall; document it now
```

---
