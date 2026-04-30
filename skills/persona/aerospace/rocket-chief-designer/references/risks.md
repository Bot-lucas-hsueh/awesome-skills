## § 3 Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|-------------------|------------|
| **Stage Separation Failure** | CATASTROPHIC | Vehicle loss; upper stage or payload lost; potential debris over range | Redundant separation systems (mechanical + pyrotechnic); clean separation analysis (CFD at separation Mach number); flight safety range closure |
| **Structural Failure at Max-Q** | CATASTROPHIC | Vehicle loss due to aerodynamic overload; debris hazard to ground population | Conservative aerodynamic load analysis; structural margin (1.4 on limit load, per NASA-STD-5001); load relief trajectory if max-Q exceeds design load |
| **Engine-Out at First Stage** | CRITICAL | Mission continues only if vehicle has engine-out capability designed in | Engine-out trajectory analysis; Falcon 9 operates on 8/9 engines; GNC must handle CG shift and thrust asymmetry |
| **Range Safety Violation** | CRITICAL | Vehicle destroyed by range safety officer if violating instantaneous impact point (IIP) constraints | Autonomous Flight Safety System (AFSS); pre-computed IIP boundaries; redundant termination system |
| **Payload Fairing Separation Failure** | CRITICAL | Payload cannot deploy; mission failure; payload heating above limit if fairing remains | Redundant fairing separation systems; qualification test of both halves in combined release; passive heating limit (typically 135°C/1135 W/m²) |
| **Propellant Leak / Unexpected Mass** | CRITICAL | Off-nominal trajectory; reduced payload margin; potential engine damage | Propellant loading accuracy (± 0.1% of design load); mass properties verification before launch; Go/No-Go based on measured vs. predicted mass |

---
