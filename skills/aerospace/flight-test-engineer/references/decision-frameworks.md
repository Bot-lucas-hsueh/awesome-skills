## § 5 · Decision Frameworks

### Envelope Expansion Strategy

```
Phase 1: Initial Envelope (First Flight)
├── Altitude: 10,000-15,000 ft
├── Speed: 250 KCAS / M0.6
├── G-load: ±1.5g
├── Configuration: Clean, flaps up
└── Duration: 1-2 hours

Phase 2: Flutter Clearance
├── Sequential speed increments: M0.1 steps
├── Excitation: Control surfaces, boom
├── Analysis: Damping, frequency tracking
└── Sign-off: Aeroelastic stability

Phase 3: Loads Survey
├── Maneuvers: Pushover-pullup, steady heading sideslip
├── Conditions: Vary weight, CG, altitude
├── Validation: Loads model correlation
└── Structural clearance

Phase 4: Full Envelope
├── Maximum operating altitude
├── Maximum operating Mach
├── Design dive speed (VD/MD)
└── All operational configurations
```

### Performance Data Correction

| Parameter | Standard Conditions | Correction Method |
|-----------|---------------------|-------------------|
| True Airspeed | ISA, sea level | Density, compressibility |
| Rate of Climb | Standard weight | Weight ratio squared |
| Takeoff Distance | Standard weight, ISA | Temperature, pressure, weight |
| Landing Distance | Standard weight, ISA | Temperature, weight, wind |

📄 **Full Details**: [references/09-decision-frameworks.md](references/09-decision-frameworks.md)

---
