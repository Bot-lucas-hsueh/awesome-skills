## § 4 Core Philosophy

```
┌─────────────────────────────────────────────────────────────────┐
│              INDUSTRIAL ELECTRICAL DESIGN FLOW                   │
│                                                                 │
│  REQUIREMENTS ──► LOAD ANALYSIS ──► SYSTEM DESIGN ──► PROTECTION│
│       │               │                 │              │          │
│   [User needs]   [Demand calc]    [SLD & wiring]  [Coordination] │
│   [Process]     [Diversity]      [Panel layout]  [Settings]     │
│                                                            │
│       ▼            ▼                 ▼              ▼           │
│  SAFETY DESIGN ──► COMPONENT SPEC ──► DOCUMENTATION ──► COMMI   │
│   [SIL/PLr]      [PLC/VFD/MCC]    [NEC/IEC refs]   [Start-up]   │
│                                                            │
│  GATE REVIEWS: Concept → Detailed Design → Panel Build → On-site│
│  EXIT CRITERIA: Short-circuit study passed, coordination plot <1 │
└─────────────────────────────────────────────────────────────────┘
```

**Principle 1 — Protection Is Layered:** Use coordinated protection (main breaker → feeder → branch) so only the faulted circuit trips. Selectivity prevents total plant shutdowns.

**Principle 2 — Safety Circuits Are Independent:** Safety-rated functions must be separate from standard control. Single failures must not defeat safety — use redundant contacts and monitoring.

**Principle 3 — Documentation Drives Compliance:** A design not documented is a design not compliant. NEC 110.12 requires "readily accessible" diagrams. Missing drawings delay UL inspection and commissioning.

---

