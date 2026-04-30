## § 3 Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|-------------------|------------|
| **Control Instability** | CATASTROPHIC | Loss of vehicle, potential ground casualties, mission failure | Verify stability margins in simulation before flight; validate on HIL; enforce gain limits in software; implement envelope protection |
| **Sensor Failure Mid-Flight** | CRITICAL | Navigation loss, uncontrolled descent, flyaway | Redundant IMU/GPS; sensor health monitoring; graceful degradation to safe modes; automatic Return-to-Home on GPS loss |
| **Software Bug in Flight-Critical Path** | CATASTROPHIC | Uncommanded maneuvers, system crash | DO-178C DAL-A qualification; structural coverage (MC/DC); independent verification; watchdog timers |
| **Actuator Saturation** | SERIOUS | Control authority loss, pilot unable to recover | Anti-windup in all integrators; actuator saturation detection; command limiting with priority logic |
| **EMI/RF Interference** | SERIOUS | Communication loss, sensor corruption, GPS spoofing | EMI shielding; redundant datalinks; FHSS protocols; signal plausibility monitors |
| **VTOL Transition Failure** | CRITICAL | Loss of airspeed in fixed-wing mode or loss of thrust authority in hover | Airspeed sensor redundancy; transition abort criteria; minimum airspeed protection; hover-capable fallback |

---
