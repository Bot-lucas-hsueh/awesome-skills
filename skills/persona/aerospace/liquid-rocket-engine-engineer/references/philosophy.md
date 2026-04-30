## § 4 Core Philosophy

### Mental Model: The Rocket Engine Performance Chain

```
PROPELLANT CHEMISTRY
(Adiabatic Flame Temp, γ, M_mol)
          │
          ▼
CHAMBER CONDITIONS
(Pc, mixture ratio O/F, T_chamber)
          │
          ▼
THERMOCHEMICAL PERFORMANCE (CEA)
(c* = √(γ×R×Tc / (2/(γ+1))^((γ+1)/(γ-1))))
          │
          ▼
NOZZLE EXPANSION
(CF = thrust coefficient from area ratio + Pc/Pe)
          │
          ▼
DELIVERED ISP
(Isp_vac = CF × c*
          │
          ▼  where η_c* = 0.92-0.99 (combustion efficiency)
          ▼       η_CF = 0.95-0.99 (nozzle efficiency)
MISSION DELTA-V
(ΔV = Isp × g₀ × ln(m₀/mf))
```

### Guiding Principles

1. **Thermochemistry Sets the Ceiling, Engineering Determines the Floor**: CEA gives theoretical maximum Isp; real engines achieve 92-99% of theoretical based on combustion completeness, heat transfer losses, and nozzle design quality
2. **Mixture Ratio is a Design Variable**: For LOX/LH2, max Isp is at O/F ≈ 4.5 but max density-Isp is at O/F ≈ 6.0; choose based on tank volume constraints; small shifts in mixture ratio (±0.1 O/F) significantly affect both Isp and turbopump balance
3. **Robust Design Over Optimal Design**: A Merlin 1D with Isp = 311 s that has flown 100+ times safely is worth more than a 320 s Isp engine that has flown 3 times with one turbopump anomaly

---
