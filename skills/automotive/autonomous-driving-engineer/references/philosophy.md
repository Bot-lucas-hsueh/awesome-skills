## § 4 — Core Philosophy

```
                    AUTONOMOUS DRIVING STACK
    +-------------------------------------------------+
    |                  SENSORS                        |
    |  [Camera] [LiDAR] [Radar] [IMU] [GNSS] [V2X]  |
    +------------------+------------------------------+
                       | raw sensor data
    +------------------v------------------------------+
    |              PERCEPTION                         |
    |  3D Detection -> Tracking -> Semantic Seg -> BEV|
    +------------------+------------------------------+
                       | tracked objects + drivable area
    +------------------v------------------------------+
    |             PREDICTION                          |
    |  Trajectory Prediction -> Interaction Modeling  |
    +------------------+------------------------------+
                       | predicted futures
    +------------------v------------------------------+
    |         BEHAVIOR
    |  Scene Understanding -> Decision -> Path Gen    |
    +------------------+------------------------------+
                       | reference trajectory
    +------------------v------------------------------+
    |               CONTROL                           |
    |        MPC / PID
    +------------------+------------------------------+
                       | throttle, brake, steer commands
    +------------------v------------------------------+
    |             VEHICLE ACTUATORS                   |
    +-------------------------------------------------+
         ^                              |
         |    SAFETY MONITOR
         +------------------------------+
```

**Guiding Principle 1 — Defense in Depth**: No single sensor, algorithm, or software module is trusted without corroboration. Every safety-critical detection path has at least two independent confirmation channels.

**Guiding Principle 2 — Graceful Degradation**: The system must define a safe fallback for every module failure: from full autonomy to driver alert to controlled stop. Minimal Risk Condition (MRC) must be reachable in all foreseeable failure states.

**Guiding Principle 3 — Validation Before Deployment**: Miles driven are not a proxy for safety coverage. Structured scenario-based testing (SOTIF, ISO 34501 ontology) covering known and unknown unsafe scenarios must gate every software release.

---
