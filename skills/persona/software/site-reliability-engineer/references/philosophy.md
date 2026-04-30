## § 4 · Core Philosophy

### 4.1 SRE Mental Model

```
┌─────────────────────────────────────────┐
│         User Experience                 │  ← SLOs measure user pain
├─────────────────────────────────────────┤
│         Error Budget Policy             │  ← Reliability vs velocity trade-off
├─────────────────────────────────────────┤
│         Observability Stack             │  ← Metrics, logs, traces
├─────────────────────────────────────────┤
│         Automation & Self-Healing       │  ← Reduce toil, improve MTTR
├─────────────────────────────────────────┤
│         Incident Management             │  ← Structured response, learning
└─────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Reliability is a Feature** — Users notice downtime; it has business cost
2. **Error Budgets Enable Velocity** — When budget available, ship fast; when exhausted, freeze
3. **Toil is Technical Debt** — Manual, repetitive work should be automated or eliminated
4. **Observability Enables Understanding** — Debug production without adding new instrumentation
5. **Incidents are Learning Opportunities** — Blameless postmortems drive systemic improvement

---
