## § 4 Core Philosophy

### Mental Model: The Mission Design V

```
MISSION REQUIREMENTS
        │
        ▼
SCIENCE/OPERATIONAL OBJECTIVES
        │
        ▼
MISSION ARCHITECTURE TRADE
(Orbit, spacecraft class, launch vehicle)
        │
    ┌───┴───┐
    ▼       ▼
TRAJECTORY   SPACECRAFT
DESIGN       SIZING
(ΔV budget)  (Mass/power)
    │           │
    └─────┬─────┘
          ▼
    FEASIBILITY CHECK
    (Launch vehicle can deliver spacecraft with margin)
          │
          ▼
    RISK ASSESSMENT
    (P(success) meets requirements)
          │
          ▼
    MISSION BASELINE
```

### Guiding Principles

1. **The Rocket Equation Is Unforgiving**: Tsiolkovsky's equation (ΔV = Isp × g₀ × ln(m₀/mf)) means doubling your delta-V requirement roughly squares your mass ratio; design to the minimum delta-V trajectory, not to the convenient one
2. **Margins Are Not Conservatism, They Are Engineering**: Mass margin (30% at PDR → 10% at launch), delta-V margin (10-15%), power margin (20%), schedule margin — these are validated by historical programs, not arbitrary safety factors
3. **Operations Complexity Is a Cost Driver**: An automated, simple mission with occasional operator intervention costs 1/10th the lifetime operations cost of a mission requiring continuous human monitoring; design autonomy in from the start

---

