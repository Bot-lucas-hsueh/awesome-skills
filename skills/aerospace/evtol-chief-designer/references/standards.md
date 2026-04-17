## § 7 Standards & Reference

### Regulatory Framework for eVTOL Certification
```
FAA (USA):                         EASA (EU):
  Part 23 PoweredLift (G-1 basis)    SC-VTOL-01 + AMC-20-35
  or Part 27 (small rotorcraft)       CS-23 (for fixed-wing modes)
  FAA AMC EVTOL (2024)               Special Conditions as needed
       ↑                                    ↑
  Issue Papers for novel features     EASA AMC EVTOL discussions
```

### Key Performance Metrics
| Metric | Target | Warning | Critical |
|--------|--------|---------|---------|
| Empty Weight Fraction (EWF) | < 0.52 | 0.52–0.58 | > 0.58 (mission viability at risk) |
| Hover Figure of Merit (FM) | > 0.75 | 0.65–0.75 | < 0.65 |
| Hover power loading (N/kW) | > 100 N/kW | 80–100 | < 80 N/kW |
| Cruise L/D (lift+cruise config) | > 10 | 8–10 | < 8 |
| Specific energy (battery cells) | > 280 Wh/kg | 250–280 | < 250 Wh/kg |
| Rotor tip speed (acoustic) | < 180 m/s | 180–220 m/s | > 220 m/s (community concern) |
| Structural weight (% MTOW) | 20–26% | 26–30% | > 30% |
| Power redundancy margin (single-failure) | ≥ 25% | 15–25% | < 15% |

### Configuration Trade Decision Tree
```
Mission Range?
├─ < 30 km (urban shuttle)
│   └─ Noise priority?
│       ├─ YES → Multirotor (low tip speed, high disk area, community accepted)
│       └─ NO  → Lift+Cruise (better cruise efficiency, higher noise)
└─ 30–150 km (regional)
    └─ Payload > 4 passengers?
        ├─ YES → Tiltwing / Tiltrotor (best cruise L/D, complex cert)
        └─ NO  → Lift+Cruise (simpler cert, acceptable cruise perf)
```

