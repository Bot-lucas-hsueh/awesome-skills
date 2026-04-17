## § 4 · Core Philosophy

### 4.1 Defense-in-Depth Signaling Model

```
        ┌─────────────────────────────────────────────┐
        │           OPERATIONAL LAYER                 │
        │  (Timetables, Traffic Management)           │
        └─────────────────────────────────────────────┘
                         ↓ Safety
        ┌─────────────────────────────────────────────┐
        │           PROTECTION LAYER                  │
        │  (Signals, Speed Checks, Route Locking)      │
        └─────────────────────────────────────────────┘
                         ↓ Fail-Safe
        ┌─────────────────────────────────────────────┐
        │           DETECTION LAYER                  │
        │  (Track Circuits, Axle Counters, TSR)       │
        └─────────────────────────────────────────────┘
```

Signaling creates multiple independent layers of protection. The detection layer identifies train position, the protection layer enforces safe movement authorities, and the operational layer manages capacity. Each layer must fail safe—transitioning to the most restrictive safe state.

### 4.2 Guiding Principles

1. **Fail-Safe Design**: When any component fails, the system must default to the safest state (stop signal, restricted speed)
2. **Fail-Operational for High-Availability Lines**: ETCS Level 3 and CBTC require fail-operational design for headway
3. **Modular Safety**: Divide system into safety blocks with defined SIL levels; verify each independently
4. **Demonstrable Reliability**: All safety claims must be quantified per EN 50126 (MTBF, availability, safety integrity)

---

