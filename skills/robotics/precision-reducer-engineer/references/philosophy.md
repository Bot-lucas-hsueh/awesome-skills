## § 4 · Core Philosophy

**Reducer Type Selection — 5-Gate Decision Tree:**

```
Gate 1: Ratio required?
  ├── i ≤ 30 → Standard spur/helical planetary (efficiency ≥ 95%)
  ├── 30 < i ≤ 100 → Harmonic Drive preferred (compact, zero backlash)
  └── i > 100 → Harmonic Drive or RV reducer (two-stage)

Gate 2: Backlash requirement?
  ├── ≤±30 arcsec (precision servo) → Harmonic Drive (zero backlash by design)
  ├── ≤±1 arcmin → RV reducer (preloaded)
  └── >1 arcmin → Planetary acceptable

Gate 3: Shock load factor Ks?
  ├── Ks ≤ 1.5 (smooth, e.g., SCARA elbow) → Harmonic Drive cup type
  ├── 1.5 < Ks ≤ 3.0 (robot J1/J2) → Harmonic Drive hat type or RV
  └── Ks > 3.0 (heavy robot J1 waist) → RV reducer mandatory

Gate 4: Speed requirement?
  ├── Input ≤ 3000 rpm → Both types suitable
  ├── 3000–6000 rpm → Harmonic Drive (wave generator bearing speed limit)
  └── >6000 rpm → Special high-speed harmonic or inline planetary

Gate 5: Size/weight constraint?
  ├── Hollow shaft required (cable routing) → Harmonic Drive (large hollow bore)
  └── Maximum stiffness/weight ratio → RV reducer (rigid output flange)
```

**Fatigue Life Philosophy:** Always calculate L10 life, not just rated torque comparison. A reducer at 110% rated torque has L10 reduced by ~50% (life ∝ (T_rated/T_applied)^3 for rolling contact). Apply Miner's rule for variable duty cycles.

**Manufacturing Quality Philosophy:** Gear tooth accuracy to DIN 3960/ISO 1328 Grade 4–6 for reducers; surface roughness Ra ≤ 0.2 μm on contact surfaces; heat treatment to 58–62 HRC (case depth 0.8–1.5 mm on cycloidal discs, 0.5–0.8 mm on flexspline).
