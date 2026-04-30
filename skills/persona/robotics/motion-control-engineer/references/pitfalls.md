## 10. Common Pitfalls & Anti-Patterns

### Anti-Pattern 1 — Derivative on Error Instead of Measurement

```python
# BAD: Derivative of error causes kick when setpoint changes
e_prev = 0
def bad_pid(e, dt):
    de = (e - e_prev)
    return Kp*e + Kd*de

# GOOD: Derivative of measurement only
y_prev = 0
def good_pid(e, y, dt):
    dy = (y - y_prev)
    return Kp*e - Kd*dy  # Note: minus sign for measurement derivative
```
**Why it matters**: Derivative on error causes a torque spike equal to Kd×Δsetpoint/dt when the reference steps. For a 45° joint step at dt=1ms and Kd=10, this is a 785 N·m spike — potentially destructive.

### Anti-Pattern 2 — No Anti-Windup in Saturation

```python
# BAD: Integrator accumulates during motor current saturation
integral = 0
def bad_pid(e, dt, tau_max=50.0):
    integral += e * dt  # Unguarded — windup during saturation
    tau = Kp*e + Ki*integral
    return np.clip(tau, -tau_max, tau_max)  # Output clipped, but integral keeps growing

# GOOD: Back-calculation anti-windup
integral = 0
Tt = 0.1  # Anti-windup time constant
def good_pid(e, dt, tau_max=50.0):
    global integral
    tau_unsat = Kp*e + Ki*integral
    tau_sat = np.clip(tau_unsat, -tau_max, tau_max)
    integral += dt * (e + (tau_sat - tau_unsat)
    return tau_sat
```
**Why it matters**: Without anti-windup, after joint limit contact the integrator accumulates for the full contact duration. Upon release, 5-10× overshoot occurs, potentially hitting the opposite joint limit and causing oscillation between limits.

### Anti-Pattern 3 — Blocking Calls in Real-Time Control Loop

```cpp
// BAD: ROS subscriber callback in 1ms RT thread — may block
void control_loop() {
    auto msg = ros_subscriber.take();  // May wait for mutex — RT violation!
    compute_control(msg);
}

// GOOD: Lock-free SPSC queue between RT and non-RT threads
#include <boost/lockfree/spsc_queue.hpp>
boost::lockfree::spsc_queue<JointState, boost::lockfree::capacity<16>> state_queue;

// Non-RT thread: push new state
state_queue.push(new_state);

// RT thread: poll without blocking
void control_loop_rt() {
    JointState state;
    if (state_queue.pop(state)) {
        compute_control(state);
    }
    // Else: use last valid state (stale-but-valid strategy)
}
```
**Why it matters**: A single blocking call in a 1ms RT loop causes a deadline miss, which the OS logs as an XRun. Accumulated deadline misses corrupt control at exact moments of heavy system load — creating intermittent instability that is extremely difficult to debug.

### Anti-Pattern 4 — Using MoveIt Joint Trajectory as Direct Torque Command

```python
# BAD: MoveIt trajectory gives position waypoints — feeding directly to torque mode
for waypoint in moveit_trajectory:
    send_torque(waypoint.positions)  # WRONG: positions ≠ torques!

# GOOD: Use the trajectory as position reference, compute torque via controller
for waypoint in moveit_trajectory:
    q_des = waypoint.positions
    dq_des = waypoint.velocities
    # Compute feedforward + feedback torque
    tau_ff = inverse_dynamics(q_des, dq_des, ddq_des=waypoint.accelerations)
    tau_fb = Kp * (q_des - q_meas) + Kd * (dq_des - dq_meas)
    send_torque(tau_ff + tau_fb)
```
**Why it matters**: MoveIt outputs kinematic trajectories (positions, velocities). Torque-controlled robots require proper inverse dynamics for feedforward — without it, dynamic accuracy degrades with speed and payload.

### Anti-Pattern 5 — Ignoring EtherCAT Sync Manager Timing

```bash
# BAD: Using default EtherCAT configuration without distributed clocks
# Results in 50-500µs jitter instead of < 10µs

# GOOD: Enable IEEE 1588 Distributed Clocks in SOEM
ec_configdc();  # Must be called during EtherCAT init
# Set DC sync0 period to match control cycle: 1000000 ns = 1ms
ec_dcsync0(slave_index, TRUE, 1000000, 0);
# Verify: cyclictest should show < 50µs jitter
# sudo cyclictest -l100000 -m -n -a2 -t1 -p99 -i200 -h400
```
**Why it matters**: Without distributed clocks, each EtherCAT slave uses its own oscillator, causing inter-slave timing skew. In a 6-DOF arm, this means joint 1 and joint 6 receive commands with 200µs offset — causing coordinated motion errors visible as jitter in Cartesian trajectories.

## 11. Integration with Other Skills

| Combination | Workflow | Result |
|-------------|----------|--------|
| **Motion Control + Robot Perception** | Perception node detects target object pose → generates Cartesian goal → IK solver → joint trajectory → MPC tracks trajectory with force feedback | Fully closed-loop bin-picking: perception updates goal pose at 20Hz, controller adapts at 500Hz |
| **Motion Control + Robot Mechanical Engineer** | Mechanical engineer provides link inertias and joint compliance parameters → control engineer updates Pinocchio URDF model → retunes MPC cost weights | Accurate dynamics model reduces tracking error by 40% vs nominal URDF; impedance control stiffness matches mechanical design intent |
| **Motion Control + Precision Reducer Engineer** | Reducer engineer provides backlash, stiffness, and damping model → control engineer adds joint compliance model to state estimator → friction compensation tuned to actual measured friction | Eliminates low-speed hunting in position hold; improves trajectory tracking at reversal points |

## 12. Scope & Limitations

**Use When:**
- Designing or tuning PID/LQR/MPC controllers for robotic joints or Cartesian space
- Implementing ROS2 control hardware interfaces or custom controller plugins
- Solving inverse kinematics for 4-7 DOF serial manipulators including singularity handling
- Implementing force/impedance control for compliant or collaborative robot applications
- Debugging real-time control loop performance, EtherCAT timing, or jitter issues

**Do NOT Use When:**
- Bipedal or quadruped locomotion control — requires whole-body control (WBC) and centroidal dynamics expertise (use a specialized legged-robot skill)
- Autonomous vehicle path tracking (pure pursuit, Stanley) — different latency/safety model
- Aerospace flight control systems — require avionics certification (DO-178C, DO-254) beyond this skill's scope
- Soft robot control — continuum mechanics require completely different modeling approaches

## 13. How to Use This Skill

**Quick Install:**
```bash
# OpenCode
opencode skill add motion-control-engineer

# Cursor
mkdir -p .cursor/rules
cp motion-control-engineer.md .cursor/rules/motion-control-engineer.mdc

# Claude Code
claude --system-prompt "$(sed -n '/^```$/,/^```$/p' motion-control-engineer.md | head -n -1 | tail -n +2)"
```

**Trigger Words
- `motion control engineer`
- `PID tuning`
- `MPC robot`
- `inverse kinematics`
- `impedance control`
- `ros2_control`
- `real-time control loop`
- `trajectory tracking`

## 14. Quality Verification

**Self-Checklist:**
- [ ] All 5 stability gates evaluated: Lyapunov stability, safety limits, real-time budget, performance, tuning path
- [ ] Cascade loop frequency ratios stated (inner > 5× outer)
- [ ] Gravity compensation included in all position controller designs
- [ ] Anti-windup strategy specified for all integrating controllers
- [ ] Real-time safety: no blocking calls, lock-free data exchange, memory pre-allocated
- [ ] Joint and torque limits enforced at hardware interface layer
- [ ] Coordinate frames and units specified (rad, N·m, m/s)

**Test Cases:**

| # | Input | Expected Output |
|---|-------|-----------------|
| 1 | "My joint PID oscillates at 8Hz with Kp=200" | Diagnosis: resonant mode near 8Hz. Solution: add notch filter at 8Hz (Q=5) in derivative path; reduce Kp to 100; re-verify PM > 45°. Provide biquad filter coefficients for 1kHz sample rate. |
| 2 | "Design LQR for a SCARA robot with 2 joints, given inertia matrix and gravity vector" | Complete Python LQR design with scipy.linalg.solve_continuous_are, Q/R weight selection rationale, closed-loop eigenvalue placement, and discrete-time implementation at 500Hz |
| 3 | "How do I implement collision detection without an FT sensor?" | Generalized momentum observer implementation using Pinocchio RNEA: τ_ext = τ_cmd - τ_model - d/dt(M(q)·dq); threshold tuning; distinguish contact from estimation noise |

## 15. Version History

| Version | Date | Changes |
|---------|------|---------|
| **3.0.0** | 2026-03-04 | Full rewrite to exemplary standard. Added complete Acados MPC formulation, DLS IK with Pinocchio, anti-windup pattern, EtherCAT distributed clocks, collision detection observer, 5-gate decision framework, ROS2 control RT anti-patterns |
| **2.0.0** | 2025-08-15 | Added impedance control formulation, TOPP-RA trajectory planning, Pinocchio integration, ROS2 Iron compatibility |
| **1.0.0** | 2025-03-01 | Initial release with PID tuning guide and basic ROS2 control overview |

## 16. License & Author

**License**: MIT License — free to use, modify, and distribute with attribution.

**Author**: neo.ai — Advanced Robotics & AI Engineering Skills Platform

**Attribution**: When using or adapting this skill, include: "Motion Control Engineer skill by neo.ai (v3.0.0)"

**Contact**: For enterprise licensing, custom skill development, or technical collaboration: skills@neo.ai

**Disclaimer**: Motion control systems in safety-critical applications (collaborative robots, medical devices, heavy industrial automation) require independent safety analysis per ISO 10218, ISO/TS 15066, and IEC 62061. Controller designs provided here require hardware commissioning, safety assessment, and validation by qualified safety engineers before deployment.
