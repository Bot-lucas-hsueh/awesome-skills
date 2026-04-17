## § 4 · Core Philosophy

```
                    CASCADE CONTROL ARCHITECTURE
    ┌─────────────────────────────────────────────────────┐
    │  TASK SPACE (100Hz)                                 │
    │  Mission planner → Cartesian trajectory x_d(t)     │
    └──────────────────────────┬──────────────────────────┘
                               │ IK + Jacobian
    ┌──────────────────────────▼──────────────────────────┐
    │  JOINT POSITION LOOP (500Hz)                        │
    │  e_q = q_d - q_meas                                 │
    │  [PID / LQR
    │  Gravity + friction compensation                    │
    └──────────────────────────┬──────────────────────────┘
                               │ Joint torque command
    ┌──────────────────────────▼──────────────────────────┐
    │  VELOCITY LOOP (1kHz)                               │
    │  e_ω = ω_d - ω_meas                                 │
    │  PI controller → I_q command                        │
    └──────────────────────────┬──────────────────────────┘
                               │ Current setpoint
    ┌──────────────────────────▼──────────────────────────┐
    │  CURRENT
    │  FOC: I_d=0, I_q tracking → PWM duty cycle         │
    │  Bandwidth: 2-5kHz, latency < 100µs                 │
    └──────────────────────────┬──────────────────────────┘
                               │ Motor voltages (SVPWM)
                              PMSM
```

**Principle 1 — Inner Loops Must Be Faster**: Each loop in the cascade must run at least 5-10× faster than the loop it controls. Current loop > 5kHz, velocity loop ≥ 1kHz, position loop ≥ 250Hz. Violating this hierarchy makes the outer loop fight the inner loop dynamics.

**Principle 2 — Model-Based Feedforward is Not Optional**: For manipulators with nonlinear dynamics, a pure PID without gravity and Coriolis feedforward requires very high gains — at the cost of stability margin. Always compute feedforward torques via inverse dynamics (Pinocchio recursive Newton-Euler) and use feedback only for disturbance rejection.

**Principle 3 — Safety is Hardcoded, Not Parameterized**: Joint limits, torque limits, and e-stop logic must be implemented in the hardware interface layer where they cannot be overridden by a buggy controller. A controller should never be able to command beyond hardware limits regardless of software state.

