## § 7 Standards & Reference

See [references/07-standards.md](references/07-standards.md)

---

---

## Phase 2: Design, Implementation & Simulation

**Activities:**
- Develop linear plant models at multiple operating points
- Design controllers (PID gains, LQR Q/R matrices, MPC cost functions)
- Implement EKF/UKF sensor fusion with tuned process/measurement noise covariance
- Conduct nonlinear 6-DOF simulation with actuator and sensor models
- Perform Monte Carlo analysis over parametric uncertainty

**✓ Done Criteria:**
- Bode plots confirming stability margins at all operating points
- Nonlinear simulation shows stable response to ±3σ parameter variations
- Position hold accuracy <15 cm in simulation (with sensor noise models)
- All failure scenarios in FMEA have verified safe behavior in simulation
- Code passes static analysis (MISRA-C compliance if DO-178C applicable)

**✗ FAIL Criteria:**
- Any operating point with phase margin <30° or gain margin <4 dB
- Integrator windup causing saturation in nominal simulation scenarios
- EKF divergence during GPS dropout simulation >30 seconds

---

### Phase 3: HIL Validation & Flight Test

**Activities:**
- Integrate real flight controller hardware into HIL simulation
- Validate all sensor interfaces and actuator commands at hardware level
- Conduct progressive flight testing: hover, low-speed, full envelope
- System identification via frequency sweeps (10-50 rad/s range)
- Compare in-flight identified model to design model; update if deviation >20%

**✓ Done Criteria:**
- HIL shows identical behavior to SIL simulation within tolerances
- Flight test confirms position hold <10 cm in calm air
- Frequency sweep confirms phase margin ≥45° in flight
- All failure injection tests (GPS dropout, actuator failure) pass safe mode transitions
- Flight data logged at ≥100 Hz with timestamp accuracy <1 ms

**✗ FAIL Criteria:**
- Any flight oscillation not present in simulation (model fidelity issue)
- Attitude error >5° during step wind disturbance injection
- Any uncommanded mode transition during normal operations

---

