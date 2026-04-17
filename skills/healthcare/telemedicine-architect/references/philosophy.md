## § 4 · Core Philosophy

### 4.1 Clinical-First Architecture

```
                    ┌─────────────────┐
                    │  Patient Need  │
                    │    (Use Case)   │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
     ┌────────────┐  ┌────────────┐  ┌────────────┐
     │  Clinical  │  │ Regulatory │  │  Technical │
     │  Workflow  │  │  Mapping   │  │ Feasibility│
     └─────┬──────┘  └─────┬──────┘  └─────┬──────┘
           │              │              │
           └──────────────┼──────────────┘
                          │
                          ▼
                 ┌────────────────┐
                 │ Design Decision│
                 └────────────────┘
```

Every architectural choice must satisfy all three gates: clinical utility, regulatory compliance, and technical feasibility — in that priority order.

### 4.2 Guiding Principles

1. **The Patient Record is the Source of Truth**: Telemedicine platforms are adjuncts to the EHR, not replacements. Design for bidirectional sync, not parallel data stores.
2. **Fail Safe, Fail Explicitly**: When video freezes, data fails to sync, or connection drops — the system must alert the clinician and preserve session state for recovery.
3. **Minimum Necessary Applies to Architecture**: Don't ingest entire EHR records for a video visit; pull only the relevant problem list, medications, and allergies.

---

