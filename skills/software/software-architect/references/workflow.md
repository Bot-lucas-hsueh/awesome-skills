## § 7 · Standard Workflow

### Phase 1: Discovery & Requirements (Days 1-3)

```
├── Stakeholder Interviews
│   ├── Business goals and constraints
│   ├── Growth projections (6mo, 1yr, 3yr)
│   └── Regulatory/compliance requirements
├── Current State Assessment
│   ├── Existing architecture review
│   ├── Technical debt inventory
│   └── Team structure and capabilities
├── Quality Attributes Workshop
│   ├── Define SLOs (availability, latency, throughput)
│   ├── Rank QAS by business criticality
│   └── Document acceptable trade-offs
└── [✓ Done]: QAS documented, constraints identified, team assessed
    [✗ FAIL]: Missing SLOs → cannot proceed to design
```

### Phase 2: Architecture Design (Days 4-10)

```
├── Domain Modeling
│   ├── Event storming workshop
│   ├── Bounded context identification
│   └── Context mapping (partnership, customer-supplier, etc.)
├── Pattern Selection
│   ├── Apply decision matrix (§6.1)
│   ├── Document rationale in ADR
│   └── Validate against QAS
├── C4 Modeling
│   ├── Level 1: System Context (external actors)
│   ├── Level 2: Containers (deployable units)
│   └── Level 3: Components (major structures)
├── Failure Mode Analysis
│   ├── Identify single points of failure
│   ├── Design circuit breakers and bulkheads
│   └── Plan graceful degradation
└── [✓ Done]: C4 diagrams, ADRs, failure analysis complete
    [✗ FAIL]: No failure mode analysis → architecture incomplete
```

### Phase 3: Validation & Planning (Days 11-14)

```
├── Architecture Review Board
│   ├── Present to senior engineers + SRE
│   ├── Security review (threat modeling)
│   └── Cost review (infrastructure estimates)
├── Proof of Concept
│   ├── Build riskiest component first
│   ├── Load test at 2× expected peak
│   └── Validate critical assumptions
├── Migration Planning
│   ├── Strangler Fig pattern for transitions
│   ├── Rollback strategy at each stage
│   └── Team enablement plan
└── [✓ Done]: Review board approval, PoC success, migration planned
    [✗ FAIL]: PoC fails → revisit design decisions
```

### Phase 4: Observability & Governance (Ongoing)

```
├── Monitoring Strategy
│   ├── Define SLOs and error budgets
│   ├── OpenTelemetry instrumentation
│   ├── Dashboards and alerting rules
│   └── Runbooks for every service
├── Architecture Governance
│   ├── ADR repository maintenance
│   ├── Quarterly architecture reviews
│   └── Technical debt tracking
└── [✓ Done]: SLOs monitored, runbooks written, governance established
    [✗ FAIL]: Missing observability → not production ready
```

📄 **Workflow Details**: [references/workflow.md](references/workflow.md)

---
