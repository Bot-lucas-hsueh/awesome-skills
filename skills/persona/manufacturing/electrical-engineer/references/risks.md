## § 3 Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|--------------------|------------|
| Inadequate short-circuit rating | CRITICAL | Equipment damage, arc flash injury, fire | Specify AIC rating ≥ available short-circuit current; use proper interrupting rating |
| Protection device too large for wire | CRITICAL | Wire overheats before breaker trips; fire | NEC 240.4: wire ampacity must match or exceed protection |
| Ground fault not detected | CRITICAL | Undetected fault continues; equipment damage, shock hazard | Specify ground fault protection (30mA for personnel, 300mA for equipment) |
| Unsafe safety circuit design | CRITICAL | Injury or death when system fails | Use safety-rated components; validate with SISTEMA or PAScal |
| Harmonic overload on transformer | HIGH | Transformer overheating, insulation failure | Derate transformer per IEEE C57.110; add harmonic filters |
| Improper hazardous area wiring | CRITICAL | Explosion risk in Zone 0/1/2 or Class I Div 1/2 | Use intrinsically safe or explosion-proof methods per NEC 500-505 |
| VFD oversizing / undersizing | HIGH | Motor overheating, poor process control, reduced VFD life | Match VFD to motor FLA; use proper V/Hz ratio and carrier frequency |

---
