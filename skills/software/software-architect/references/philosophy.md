## § 4 · Core Philosophy

### 4.1 Architecture Mental Model

```
┌─────────────────────────────────────────┐
│     Business Capability Layer           │  ← Services align to business domains
├─────────────────────────────────────────┤
│     Quality Attributes (SLOs)           │  ← Availability, latency, throughput targets
├─────────────────────────────────────────┤
│     Architectural Patterns              │  ← Microservices, event-driven, CQRS
├─────────────────────────────────────────┤
│     System & Service Boundaries         │  ← DDD bounded contexts
├─────────────────────────────────────────┤
│     Observability Foundation            │  ← Traces, metrics, logs, SLOs
└─────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Architect for Replaceability** — Components will be replaced; design interfaces that outlive implementations
2. **Delay Irreversible Decisions** — Keep options open; use feature flags and abstraction layers
3. **Design for Failure** — Everything fails; graceful degradation is more valuable than perfect operation
4. **Data Outlives Code** — Schema design is architecture; migrations are harder than deployments
5. **Conway's Law is Real** — Team structure dictates system structure; align them intentionally

---
