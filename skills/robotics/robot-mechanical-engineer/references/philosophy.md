## § 4 · Core Philosophy

```
         ROBOT MECHANICAL DESIGN MENTAL MODEL
         =====================================

  Requirements                Design Space              Validation
  ───────────                 ────────────              ──────────
  Payload [kg]                [Kinematic Chain]         FEA Static
  Reach [m]         ──────►  [Material Selection] ──► FEA Modal
  Cycle Time [s]              [Cross-Section]           FEA Fatigue
  IP Rating                   [Joint Mechanism]         Prototype Test
  Mass Budget [kg]            [Tolerance Plan]          ISO 9283 Bench
  Safety Standard             [DFM Review]              CE Audit
        │                           │                       │
        └───────────────────────────┴───────────────────────┘
                              Iteration Loop

  MASS BUDGET ALLOCATION (typical 6-DOF, 10kg payload):
  Base + Shoulder:  35% of robot mass  →  stiff, heavy OK
  Upper Arm Link:   20% of robot mass  →  max stiffness per kg
  Forearm Link:     15% of robot mass  →  CFRP or Al7075
  Wrist Assembly:   18% of robot mass  →  compact, IP67
  End Effector IF:   7% of robot mass  →  standardized flange
  Cables + Covers:   5% of robot mass  →  minimize routing

  STIFFNESS DESIGN RULE:
  First natural frequency ωn [Hz] > 10 × control bandwidth [Hz]
  For 3Hz position bandwidth → ωn > 30Hz
  ωn = (1/2π) × sqrt(K_structure
```

**Guiding Principle 1 — Structure Before Motors.** Motor and gearbox selection is often done first, but the structural design must be validated before finalizing actuator sizing. A link that deflects 1mm under load changes the effective inertia seen by the motor and invalidates the original torque budget. Iterate: preliminary actuator sizing → structural analysis → deflection → updated actuator sizing.

**Guiding Principle 2 — Stiffness is a System Property.** Individual link stiffness, joint compliance (gearbox torsional stiffness, bearing preload), and cable routing contribute in series to end-effector compliance. A stiff link mated to a flexible harmonic drive achieves the same compliance as a flexible link — model the entire series compliance chain, not just the structural members.

**Guiding Principle 3 — Design for the Worst Load Case, Test at Rated Load.** Safety factor ≥ 3.0 on yield means the arm must survive 3× its rated payload without permanent deformation. This accounts for dynamic overloads, manufacturing variation, and material property scatter. Test protocols must verify rated load performance (ISO 9283), not maximum structural load — distinguish design verification from structural margin demonstration.

---

