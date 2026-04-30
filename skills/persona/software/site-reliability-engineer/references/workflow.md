## § 7 · Standard Workflow

### Phase 1: SLO Definition (Week 1)

```
├── Identify user journeys (login, checkout, search)
├── Define SLIs for each journey (latency, availability)
├── Set SLO targets (99.9%, 99.99%)
├── Calculate error budgets
└── [✓ Done]: SLOs defined, error budgets calculated
    [✗ FAIL]: No user-centric metrics → redefine SLIs
```

### Phase 2: Observability Implementation (Weeks 2-4)

```
├── Instrument services with OpenTelemetry
├── Create RED metrics dashboards
├── Set up alerting (symptom-based)
├── Write runbooks for every alert
└── [✓ Done]: Services observable, alerts actionable
    [✗ FAIL]: Alert fatigue → tune thresholds, reduce noise
```

### Phase 3: Automation & Self-Healing (Ongoing)

```
├── Identify toil (manual, repetitive tasks)
├── Automate highest-impact toil
├── Implement auto-remediation for known issues
├── Measure toil percentage (target < 50%)
└── [✓ Done]: Toil eliminated or automated
    [✗ FAIL]: Toil increasing → prioritize automation
```

### Phase 4: Chaos Engineering (Monthly)

```
├── Design failure scenarios (hypothesis-driven)
├── Test in staging first
├── Execute controlled chaos in production
├── Measure recovery time
└── [✓ Done]: Resilience validated, improvements identified
    [✗ FAIL]: Recovery failed → fix before next chaos test
```

---
