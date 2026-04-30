## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Controller Instability** | 🔴 Critical | Excessive PID gains cause oscillation that can destroy gearboxes, strip encoders, or injure operators | Always start with gains at 10% of calculated values; increase incrementally; verify gain/phase margins > 6dB/45° via Bode analysis before full-speed operation |
| **Real-Time Deadline Miss** | 🔴 Critical | Control loop overrun in a 1ms cycle causes missed torque commands, leading to jerk and potential mechanical damage | Use PREEMPT_RT; set CPU affinity; pre-allocate all memory; profile with cyclictest achieving < 50µs jitter before deployment |
| **Singularity Approach** | 🔴 Critical | Near singular configurations, joint velocities → ∞ for finite Cartesian velocities, causing saturation and loss of control | Implement damped least squares (DLS) IK with variable damping factor λ; add singularity index monitoring; enforce exclusion zones |
| **Integrator Windup** | 🟡 Warning | Integrator accumulates during saturation periods, causing large overshoot upon limit release | Implement back-calculation or clamping anti-windup; separate integrator for each cascade level |
| **Torque Sensor Offset Drift** | 🟡 Warning | FT sensor zero-drift causes spurious force readings, biasing impedance controller and causing slow drift in compliant mode | Zero FT sensor at startup with arm in known pose; monitor drift with Kalman filter; re-zero if bias exceeds 1N |
| **MPC Horizon Too Short** | 🟡 Warning | Short prediction horizon (N<5) causes myopic behavior: controller cannot predict constraint violations, leading to aggressive last-moment corrections | Use N ≥ 20 for manipulation; validate that planned trajectory is feasible before execution; warm-start solver |
| **Gravity Compensation Error** | 🟢 Low | Incorrect center-of-mass estimates cause constant torque offset, biasing all position controllers | Measure CoM experimentally (FT sensor with payload attached); update model when payload changes > 100g |
