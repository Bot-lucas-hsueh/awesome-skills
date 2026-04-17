## § 4 · Core Philosophy

**Superconductor Material Selection — 5-Gate Decision Tree:**

```
Gate 1: Operating temperature?
  ├── 4.2 K (LHe, high field) → NbTi (≤9 T), Nb3Sn (≤20 T), REBCO (>20 T)
  ├── 20–30 K (cryo-cooled) → MgB2 (≤6 T), REBCO (high Jc up to 30 K)
  └── 65–77 K (LN2, low cost) → REBCO tape (low Jc vs 4.2K), BSCCO-2223 (very low Jc at 77K, high B)

Gate 2: Peak magnetic field?
  ├── B ≤ 9 T → NbTi (cheapest, mature, ductile) for MRI, NMR, accelerator quadrupoles
  ├── 9 T < B ≤ 20 T → Nb3Sn (brittle, react-and-wind, ITER TF coil baseline)
  └── B > 20 T → REBCO (SPARC fusion, 40+ T research magnets, no Bc2 limit at 4.2K)

Gate 3: AC loss requirement?
  ├── Low AC loss (power cables, transformers, motors) → BSCCO-2223 multifilamentary tape,
  │   MgB2 (low hysteresis loss), or REBCO striated/twisted tape
  └── DC application (magnets) → Standard HTS tape (low twist pitch irrelevant)

Gate 4: Mechanical flexibility?
  ├── Flexible cable/coil → NbTi (ductile), REBCO tape (flexible but strain-sensitive)
  └── Rigid coil, react-and-wind acceptable → Nb3Sn (best Jc in 10-20 T range)

Gate 5: Cost constraint?
  ├── Cost-dominated → NbTi ($1-2/kA·m at 5 T, 4.2 K) or MgB2 ($5-10/kA·m at 20 K)
  ├── Performance-dominated → REBCO ($20-50/kA·m at 12 T, 4.2 K, improving)
  └── Volume production → NbTi (mature supply chain, 50+ years industrial production)
```

**Jc Characterization Philosophy:** Always specify: (1) measurement temperature, (2) applied field magnitude, (3) field orientation (B‖ab or B‖c for HTS), (4) measurement technique (magnetic vs. transport). A Jc of "300 A/mm²" is meaningless without these four parameters. For REBCO: Jc varies 10× between B‖ab (in-plane, favorable) and B‖c (perpendicular, worst case).

**Flux Pinning Philosophy:** Strong flux pinning requires defects matching the vortex diameter (ξ, coherence length ~ 1–3 nm in HTS). Point defects dominate low-field Jc; correlated columnar defects (BZO nanorods, ion tracks) enhance high-field Jc. Engineering Jc requires understanding which defect type dominates at the operating (B, T) condition.
