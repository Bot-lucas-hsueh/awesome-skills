## § 4 Core Philosophy

### Mental Model: Vehicle Design Hierarchy

```
CUSTOMER REQUIREMENTS
(Safety, Comfort, Performance, Cost)
         │
         ▼
REGULATORY REQUIREMENTS
(ECE/FMVSS/GB/T + NCAP targets)
         │
         ▼
VEHICLE SYSTEM ARCHITECTURE
(Platform, wheelbase, track, heights)
         │
    ┌────┴────────────────┐
    ▼                     ▼
BIW STRUCTURE         CHASSIS SYSTEM
(Crash load paths)    (Suspension geometry)
    │                     │
    ▼                     ▼
SUBSYSTEM INTEGRATION
(Powertrain, Battery, ADAS, Thermal)
         │
         ▼
MASS & COST TARGETS
(System-level mass budget, BOM cost)
         │
         ▼
DVP&R → VALIDATION → HOMOLOGATION
```

### Guiding Principles

1. **Geometry Is Architecture**: The vehicle package drawing (side view + plan view + cross-sections) is not just an illustration — it's the engineering contract that all subsystems must conform to; protect package constraints from engineering changes without formal impact assessment
2. **Simulate First, Then Test**: Crash simulation (LS-DYNA/ABAQUS) should predict performance within ±10% of hardware test; if correlation is poor, the model is not reliable for design decisions; invest in model correlation before relying on simulation for design trade decisions
3. **Mass Center Is a Handling Parameter**: Every mass addition/relocation changes CG height, polar moment of inertia, and front/rear weight distribution; vehicle dynamics must re-sign off every mass change > 5 kg above knee height

---

