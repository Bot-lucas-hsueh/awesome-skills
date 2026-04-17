## § 3 Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|-------------------|------------|
| **Propulsion System Failure in Hover** | CATASTROPHIC | Uncontrolled descent from low altitude; no autorotation authority for most eVTOL configurations | N+1 motor/battery redundancy; minimum 25% power margin on remaining motors post single-failure; autonomous emergency landing capability |
| **Battery Thermal Runaway** | CATASTROPHIC | Fire in occupied cabin; potential explosion; total loss of aircraft | Cell-level fusing; thermal barriers between modules; automatic cell isolation; venting pathways away from cabin; fire suppression |
| **Transition Failure (Hover↔Cruise)** | CRITICAL | Loss of airspeed authority or thrust authority during transition at low altitude | Transition abort criteria and reverse transition capability; minimum altitude for transition initiation; overlapping hover+cruise authority through full transition |
| **Icing Encounter** | SERIOUS | Rotor/wing performance degradation; asymmetric ice accumulation causes control departure | Define clear-air icing certification basis; if not icing-certified, strict operational limitations; thermal protection for critical surfaces |
| **Battery Energy Depletion** | CRITICAL | Vehicle forced landing without adequate reserve energy for missed approach | 20% minimum reserve policy; continuous state-of-charge monitoring; automatic RTH trigger at reserve threshold; pre-flight energy check |
| **Rotor Strike on Ground** | SERIOUS | Injury to ground crew; vehicle damage; operational shutdown | Rotor guard design; ground power interlock; proximity sensors; standard rotor clearance envelope during surface operations |

---
