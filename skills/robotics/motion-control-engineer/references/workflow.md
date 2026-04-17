## 8. Standard Workflow

### Phase 1 — System Identification & Model Building
**Actions**: Mount each joint individually. Apply chirp torque input (0.1-50Hz, 5% rated torque). Record velocity response. Fit second-order model (inertia J, damping b, resonance ωn). Measure friction (Coulomb + viscous) via velocity sweep. Load URDF into Pinocchio and validate gravity torques against FT measurements.

**[✓ Done]**: Transfer function identified with R² > 0.95. Friction model error < 5% rated torque across speed range. Pinocchio gravity torques match FT measurements within 0.5 N·m.

**[✗ FAIL]**: Chirp response shows multiple resonant peaks — mechanical coupling or backlash present. Gravity model error > 2 N·m — re-measure CoM or check URDF mass properties.

### Phase 2 — Inner Loop Commissioning (Current/Torque Loop)
**Actions**: Commission in drive software (Beckhoff TwinCAT

**[✓ Done]**: Current loop bandwidth ≥ 2kHz. Step response overshoot < 5%. No oscillation at rated torque command. Thermal de-rating profile validated.

**[✗ FAIL]**: Oscillation at high current → reduce current loop gain. Slow response → increase Ki. Check motor inductance measurement accuracy.

### Phase 3 — Velocity and Position Loop Tuning
**Actions**: Use systematic PID tuning: start with Kp = J × ωn² / 10, Ki = 0, Kd = 0. Apply step inputs at 10% range. Increase Kp until oscillation onset (-6dB margin point). Back off to 50%. Add Kd with first-order filter (ωfilter = 5-10 × ωbandwidth). Add Ki last. Add gravity/friction feedforward.

**[✓ Done]**: Step response: rise time meets spec, overshoot < 5%, no oscillation. Tracking error < 0.5mm at design speed. Bode plot: PM > 45°, GM > 6dB.

**[✗ FAIL]**: Oscillation persists at any Kp → mechanical resonance below bandwidth. Add notch filter at resonant frequency. Recheck joint coupling.

### Phase 4 — Force/Impedance Control Validation
**Actions**: Implement Cartesian impedance with desired stiffness Kd (100-500 N/m), damping Dd = 2×√(Kd×M), inertia Md. Test with known contact forces from FT sensor. Validate stiffness: apply 10N force, measure 10/Kd deflection. Test collision detection: tap arm and verify detection < 10ms.

**[✓ Done]**: Impedance behavior within ±10% of specified Kd/Dd over ±20mm displacement. Collision detection latency < 10ms at 5× rated disturbance torque. Robot recovers to nominal within 500ms.

**[✗ FAIL]**: Force oscillation during contact → reduce Kd or increase Dd. Slow collision detection → reduce observer gain thresholds or check torque sensor calibration.

## 9. Scenario Examples

### Scenario A — MPC Design for a 6-DOF Manipulator

**User**: I need to implement MPC for a 6-DOF arm to track a Cartesian trajectory while respecting joint torque limits. What's the best approach with Acados?

**Engineer**: For a 6-DOF arm with joint torque limits, I recommend a joint-space MPC with Cartesian task in the cost function. Here's the complete formulation:

```python
from acados_template import AcadosModel, AcadosOcp, AcadosOcpSolver
import casadi as ca
import numpy as np

def build_robot_mpc(N: int = 20, dt: float = 0.01,
                    n_joints: int = 6,
                    tau_max: np.ndarray = None,
                    q_limits: tuple = None):
    """
    Joint-space MPC with Cartesian task cost.
    State: x = [q (n), dq (n)]  (2n states)
    Input: u = tau (n)  (n inputs)
    """
    if tau_max is None:
        tau_max = np.array([80, 80, 50, 30, 20, 10])  # N·m per joint
    q_min, q_max = q_limits or (np.full(n_joints, -np.pi),
                                 np.full(n_joints, np.pi))

    model = AcadosModel()
    model.name = 'robot_arm_mpc'

    # CasADi symbolic variables
    q   = ca.SX.sym('q',  n_joints)
    dq  = ca.SX.sym('dq', n_joints)
    tau = ca.SX.sym('tau', n_joints)
    x   = ca.vertcat(q, dq)
    u   = tau

    # Simplified dynamics: M(q)*ddq + C(q,dq)*dq + g(q) = tau
    # For real system, use Pinocchio via C++ interface
    # Here: use identity mass matrix approximation for demo
    M_diag = ca.SX([3.5, 3.5, 2.0, 1.0, 0.5, 0.2])  # kg·m² estimated
    g_comp = ca.SX.zeros(n_joints)  # gravity (computed externally and added as parameter)

    ddq = (tau - g_comp)
    f_expl = ca.vertcat(dq, ddq)

    model.x = x
    model.u = u
    model.f_expl_expr = f_expl

    # OCP setup
    ocp = AcadosOcp()
    ocp.model = model
    ocp.dims.N = N

    # Cost: penalize joint position tracking + control effort
    # Cartesian task cost added via FK in stage cost
    Q_q  = np.diag([100.0] * n_joints)
    Q_dq = np.diag([1.0]   * n_joints)
    R_tau = np.diag([0.01]  * n_joints)

    ocp.cost.cost_type = 'NONLINEAR_LS'
    ocp.cost.cost_type_e = 'NONLINEAR_LS'

    # Reference: [q_ref, dq_ref, tau_ref=0]
    ocp.cost.W = ca.diag(ca.vertcat(
        ca.DM([100.0]*n_joints),
        ca.DM([1.0]*n_joints),
        ca.DM([0.01]*n_joints)
    ))

    # Constraints
    ocp.constraints.lbu = -tau_max
    ocp.constraints.ubu =  tau_max
    ocp.constraints.idxbu = np.arange(n_joints)

    ocp.constraints.lbx = np.concatenate([q_min, np.full(n_joints, -3.0)])  # rad/s limit
    ocp.constraints.ubx = np.concatenate([q_max, np.full(n_joints,  3.0)])
    ocp.constraints.idxbx = np.arange(2 * n_joints)

    # Solver: SQP with HPIPM interior-point
    ocp.solver_options.qp_solver = 'PARTIAL_CONDENSING_HPIPM'
    ocp.solver_options.integrator_type = 'ERK'
    ocp.solver_options.nlp_solver_type = 'SQP_RTI'  # Real-Time Iteration
    ocp.solver_options.tf = N * dt

    solver = AcadosOcpSolver(ocp, json_file='robot_mpc.json')
    return solver

# Expected: SQP_RTI solves in < 2ms on i7, suitable for 100Hz MPC loop
```

The SQP Real-Time Iteration scheme runs a single SQP step per cycle — warm-started from the previous solution. For your 6-DOF arm with N=20 at dt=10ms, expect 1-3ms solve time on a modern CPU, fitting comfortably in a 10ms control cycle.

---

### Scenario B — Damped Least Squares IK with Null-Space Control

**User**: Near the singularities of my robot arm, my Jacobian-based IK goes unstable with huge joint velocities. How do I fix this?

**Engineer**: Classic singularity problem. Use Damped Least Squares (DLS) with a singularity-adaptive damping factor. Here is a complete implementation using Pinocchio:

```python
import pinocchio as pin
import numpy as np

def dls_ik_velocity(model, data, q: np.ndarray, v_cart: np.ndarray,
                    lambda_min: float = 0.01, lambda_max: float = 0.1,
                    sigma_threshold: float = 0.05,
                    q_null: np.ndarray = None,
                    k_null: float = 5.0) -> np.ndarray:
    """
    Damped Least Squares IK with singularity-robust damping and null-space control.

    Args:
        q: current joint configuration (n_joints,)
        v_cart: desired Cartesian velocity [vx,vy,vz,wx,wy,wz] (6,)
        lambda_min/max: damping factor range
        sigma_threshold: minimum singular value before increasing damping
        q_null: null-space preferred configuration (e.g., mid-range joints)
        k_null: null-space gain
    Returns:
        dq: joint velocity command (n_joints,)
    """
    # Compute Jacobian at current config
    pin.computeJointJacobians(model, data, q)
    pin.framesForwardKinematics(model, data, q)

    # Get end-effector frame Jacobian (6 x n_joints)
    ee_id = model.getFrameId('tool0')
    J = pin.getFrameJacobian(model, data, ee_id,
                              pin.ReferenceFrame.LOCAL_WORLD_ALIGNED)

    # SVD for singularity analysis
    U, sigma, Vt = np.linalg.svd(J, full_matrices=False)

    # Adaptive damping: increase near singularities
    min_sigma = np.min(sigma)
    if min_sigma < sigma_threshold:
        # Levenberg-Marquardt style: λ² inversely proportional to σ_min
        lambda_sq = lambda_max**2 * (1 - (min_sigma
    else:
        lambda_sq = lambda_min**2

    # DLS pseudo-inverse: J^T (J J^T + λ²I)^{-1}
    JJT = J @ J.T
    J_dls = J.T @ np.linalg.inv(JJT + lambda_sq * np.eye(6))

    # Primary task: Cartesian velocity tracking
    dq_primary = J_dls @ v_cart

    # Null-space projection: minimize deviation from preferred config
    if q_null is not None:
        N_proj = np.eye(model.nv) - J_dls @ J  # null-space projector
        dq_null = k_null * (q_null - q)
        dq = dq_primary + N_proj @ dq_null
    else:
        dq = dq_primary

    # Log singularity measure for monitoring
    manipulability = np.sqrt(np.linalg.det(JJT))
    if manipulability < 0.01:
        print(f"WARNING: Near singularity, σ_min={min_sigma:.4f}, λ²={lambda_sq:.6f}")

    return dq
```

The key insight: when σ_min drops below your threshold, λ² increases, which reduces the pseudo-inverse gain before velocities blow up. Set σ_threshold to match your robot's singular values in typical configurations — typically 0.02-0.1 for 6-DOF arms.

---

### Scenario C — Anti-Pattern: Tuning PID Without Feedforward (Classic Mistake)

**User**: My 3kg payload arm vibrates badly. I keep increasing Kd to dampen it but it just gets worse and eventually causes instability.

**Engineer**: You have identified the most common control tuning anti-pattern. Increasing Kd to fight gravity-induced error is fundamentally wrong:

```python
# WRONG: Pure feedback PID fighting gravity
class BadController:
    def compute(self, q_des, q_meas, dq_meas):
        e = q_des - q_meas
        de = -dq_meas  # derivative of error (target is stationary)
        # High Kd amplifies sensor noise, causes instability
        tau = self.Kp * e + self.Kd * de  # + Ki*integral
        return tau

# CORRECT: Gravity feedforward + low-gain feedback for disturbance rejection
import pinocchio as pin

class GoodController:
    def __init__(self, model):
        self.model = model
        self.data = model.createData()

    def compute(self, q_des, q_meas, dq_meas, payload_mass=3.0):
        # Step 1: Compute gravity compensation (feedforward)
        # This is what the motor must produce just to hold position
        tau_grav = pin.computeGeneralizedGravity(self.model, self.data, q_meas)

        # Step 2: Add payload gravity (update model or add analytically)
        # tau_grav already includes payload if URDF payload inertia is correct

        # Step 3: Low-gain PD for tracking (disturbance rejection only)
        e   = q_des - q_meas   # position error
        de  = -dq_meas          # velocity error (zero target velocity)
        tau_pd = 50.0 * e + 5.0 * de  # MUCH lower Kp than pure PID

        return tau_grav + tau_pd
```

**Why it matters**: With 3kg payload, gravity torque on a 0.5m forearm link is ~15 N·m. A pure PD must overcome this with Kp × error — requiring huge Kp and correspondingly huge Kd for stability, which amplifies noise. With gravity feedforward, the PD only needs to handle ±0.5 N·m disturbances at low gains. Vibration disappears, stability margin improves by ~15dB.

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
