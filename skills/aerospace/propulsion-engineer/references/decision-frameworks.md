## § 5 · Decision Frameworks

### Cycle Selection Process

```
Step 1: Define Requirements
├── Thrust: Takeoff, cruise, climb
├── Mission: Range, payload, speed
├── Constraints: Noise, emissions, weight
└── Market: Timing, competition

Step 2: Select Architecture
├── BPR: Based on speed (high BPR for M0.8)
├── OPR: Balance ηth vs complexity
├── TIT: Material/technology readiness
└── Fan drive: Direct vs geared

Step 3: Component Sizing
├── Fan: Diameter from bypass flow
├── Core: Flow from core thrust requirement
├── Turbine: Work extraction matching compression
└── Mechanical: Shaft speeds, bearing locations

Step 4: Performance Optimization
├── On-design: Design point efficiency
├── Off-design: Operating line, surge margin
├── Transient: Acceleration, deceleration
└── Control: Schedules, limits
```

### Material Selection Matrix

| Component | Temperature | Material | Technology |
|-----------|-------------|----------|------------|
| Fan blades | <500°C | Ti-6Al-4V, CFRP | Wide chord, 3D aero |
| Compressor | 500-700°C | Ti alloys, Ni alloys | Blisk, TiAl LPT |
| Combustor | 1,800°C+ | Superalloys, TBC | Advanced cooling |
| HPT | 1,700°C+ | Single crystal, CMCs | Film cooling, TBC |

📄 **Full Details**: [references/09-decision-frameworks.md](references/09-decision-frameworks.md)

---
