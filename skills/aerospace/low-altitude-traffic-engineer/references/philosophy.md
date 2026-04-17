## § 4 Core Philosophy

### Mental Model: The UTM Safety Stack

```
┌─────────────────────────────────────────────────────────────┐
│  LAYER 4: EMERGENCY
│  ATC override, emergency vehicles, NOTAM implementation     │
├─────────────────────────────────────────────────────────────┤
│  LAYER 3: COLLISION AVOIDANCE (DAA)                         │
│  Onboard sense-and-avoid, ACAS-like autonomous maneuver     │
│  Last resort: <15 sec to impact                             │
├─────────────────────────────────────────────────────────────┤
│  LAYER 2: TACTICAL DECONFLICTION (real-time)                │
│  Conformance monitoring, dynamic rerouting, speed changes   │
│  Operates on 4D trajectories, 30-60 sec lookahead           │
├─────────────────────────────────────────────────────────────┤
│  LAYER 1: STRATEGIC DECONFLICTION (pre-flight)              │
│  Flight plan approval, corridor allocation, time-slot mgmt  │
│  Resolves 95%+ of conflicts before takeoff                  │
├─────────────────────────────────────────────────────────────┤
│  LAYER 0: REGULATORY FRAMEWORK                              │
│  Geofencing, airspace classification, operator registration │
│  Defines the rules of the road                              │
└─────────────────────────────────────────────────────────────┘
```

### Guiding Principles

1. **Distributed Responsibility, Centralized Awareness**: Operators retain responsibility for their aircraft; the UTM provides shared situational awareness and conflict notification, not direct control
2. **Proportional Authority**: UTM intervention authority scales with operational risk; strategic deconfliction is advisory, tactical deconfliction is binding, collision avoidance is autonomous
3. **Graceful Degradation Over Hard Failure**: Every UTM component must have a defined safe state when it fails; the default should always be "more conservative" not "more permissive"

---

