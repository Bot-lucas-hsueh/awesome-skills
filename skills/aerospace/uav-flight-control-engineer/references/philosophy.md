## § 4 Core Philosophy

### ASCII Mental Model: Flight Control System Architecture

```
 ┌─────────────────────────────────────────────────────────────────┐
 │                    MISSION
 │           Waypoints → 4D Trajectory → Path Following           │
 └─────────────────────────┬───────────────────────────────────────┘
                           │ Position/Velocity Commands
 ┌─────────────────────────▼───────────────────────────────────────┐
 │                   OUTER LOOP (Position Control)                 │
 │        PID / MPC
 └─────────────────────────┬───────────────────────────────────────┘
                           │ Attitude
 ┌─────────────────────────▼───────────────────────────────────────┐
 │                INNER LOOP (Attitude Control)                    │
 │      PID Cascaded / LQR
 └─────────────────────────┬───────────────────────────────────────┘
                           │ Actuator Commands
 ┌─────────────────────────▼───────────────────────────────────────┐
 │                   ACTUATOR ALLOCATION                           │
 │        Control Mixer → ESC/Servo → Motors/Surfaces             │
 └─────────────────────────┬───────────────────────────────────────┘
                           │ Vehicle Response
 ┌─────────────────────────▼───────────────────────────────────────┐
 │                  STATE ESTIMATION (EKF/UKF)                     │
 │   IMU + GPS + Baro + Mag + VIO + Optical Flow → State Vector   │
 └─────────────────────────────────────────────────────────────────┘
```

### Three Core Principles

**Principle 1 — Safety Through Hierarchy**: Flight control architecture must enforce a strict command hierarchy. Higher-level commands (mission, position) can be overridden by safety functions (envelope protection, collision avoidance) at any time. This hierarchy is non-negotiable and must survive any single software or hardware fault.

**Principle 2 — Observability Before Controllability**: You cannot control what you cannot observe. Invest disproportionately in sensor fusion quality, health monitoring, and fault detection. A robust estimator with a mediocre controller outperforms the reverse.

**Principle 3 — Validate at Every Integration Level**: Never skip integration test levels. Algorithm validation in simulation → HIL validation with real hardware → Ground functional test → Flight test with incremental envelope expansion. Each level catches different failure modes.

---

