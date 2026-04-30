## § 4 Core Philosophy

### Mental Model: eVTOL Design Pyramid

```
                    ┌─────────────────┐
                    │   CERTIFICATION  │  ← Defines what's achievable
                    │   (FAA/EASA)     │
                    └────────┬────────┘
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │ SAFETY   │  │ PHYSICS  │  │ MISSION  │
        │ (FMEA/   │  │ (Power   │  │ (Range/  │
        │  FTA)    │  │  budget) │  │  Payload)│
        └────┬─────┘  └────┬─────┘  └────┬─────┘
             └─────────────┼─────────────┘
                           ▼
              ┌────────────────────────────┐
              │   CONFIGURATION TRADE      │
              │   (Architecture selection) │
              └────────────┬───────────────┘
                           ▼
              ┌────────────────────────────┐
              │   DETAILED DESIGN          │
              │   (Aero/Structures/Avion.) │
              └────────────────────────────┘
```

### Guiding Principles

1. **Weight Is Everything**: In electric aviation, every kilogram of structure trades directly against battery capacity and range; relentless weight discipline from concept to flight test is the single most important design habit
2. **Redundancy at the Right Level**: Not every component needs triple redundancy — identify the failure modes that lead to loss-of-control and apply N+2 redundancy there; apply N+1 elsewhere; single-point-of-failure is unacceptable only in catastrophic-failure paths
3. **Design to the Mission, Not to the Technology**: Technology will improve (batteries, motors); design the right vehicle for the mission and the current technology will determine when it becomes economically viable

---
