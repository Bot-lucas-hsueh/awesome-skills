## § 4 Core Philosophy

### Mental Model: Vehicle Design Architecture

```
PAYLOAD REQUIREMENTS
(mass, orbit, volume, environment)
         │
         ▼
MISSION DELTA-V BUDGET
(orbit mechanics + gravity/drag losses)
         │
         ▼
STAGING OPTIMIZATION
(Distribute ΔV to minimize GLOW)
    ┌────┴────┐
    ▼         ▼
STAGE 1     STAGE 2 (+ upper stage)
(thrust/wt,  (Isp, structural fraction,
 reusability  restart capability)
 trade)
    └────┬────┘
         ▼
PROPULSION SELECTION
(Isp, T/W, restart, cost)
         │
         ▼
STRUCTURAL SIZING
(Axial load, bending, buckling)
         │
         ▼
GNC ARCHITECTURE
(Mission accessibility, reuse, safety)
         │
         ▼
VEHICLE BASELINE
(GLOW, payload fraction, reliability)
```

### Guiding Principles

1. **Payload Fraction is the Report Card**: A launch vehicle's fundamental performance metric is payload fraction (PML/GLOW); best current values: Falcon 9 Block 5 reuse ≈ 2.5% (LEO), Electron ≈ 1.8%, Long March 5 ≈ 1.7%; design decisions should be evaluated against this target
2. **The Tyranny of the Rocket Equation**: Every extra kilogram of structure or system that flies costs ~50× its mass in propellant at stage-1 or ~10× at stage-2 to compensate (via GLOW growth); this is why weight discipline at Chief Designer level is non-negotiable
3. **Reusability Economics Requires Scale**: A Falcon 9 first stage costs ~$45M to manufacture; if it can fly 10 times, the per-flight manufacturing cost drops to $4.5M; but this requires ~10 flights/year per booster to achieve the economic benefit before the booster ages out

---

