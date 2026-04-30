# code Example

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
