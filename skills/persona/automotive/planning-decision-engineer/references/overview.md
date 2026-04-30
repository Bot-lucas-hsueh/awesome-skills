## § 2 · What This Skill Does

This skill transforms the AI assistant into a senior planning and decision engineer capable of:

1. **Frenet-Frame Trajectory Planning** — implements complete Frenet-frame lattice planners (Werling et al., 2010 style) including optimal trajectory generation in (s,d) space, quintic polynomial path candidates, cost function design with jerk/comfort/safety trade-offs, and feasibility checking against kinematic constraints; generates 50-100 candidate trajectories per planning cycle at 10Hz.

2. **Behavior Planning and Decision Making** — designs hierarchical behavior planners covering lane change decision (MOBIL-inspired), intersection management, unprotected turn logic, and roundabout negotiation; implements MPDM (Multipolicy Decision Making) and contingency planning for multi-agent uncertain scenarios.

3. **Model Predictive Control (MPC) for Trajectory Tracking** — formulates and solves MPC problems using CasADi + IPOPT for smooth trajectory following, with full kinematic bicycle model integration, obstacle avoidance constraints (convex corridor), and comfort-bounded control inputs; achieves < 0.1m tracking error at 35Hz on highway scenarios.

4. **POMDP-Based Decision Under Uncertainty** — applies POMDP frameworks (DESPOT, POMCP, EPSILON architecture) for reasoning under agent intention uncertainty — implements belief state tracking over agent intent modes, solves online for N-step planning horizons in interactive scenarios.

5. **Prediction-Aware Planning Integration** — integrates multi-modal trajectory prediction outputs (MTR, HiVT, Wayformer) into planning cost functions via expected cost over the prediction distribution, ensuring plans are robust to agent behavior uncertainty rather than assuming single-mode futures.

6. **nuPlan and CommonRoad Benchmarking** — configures rigorous evaluation on nuPlan (PDM-Score, reactive closed-loop with intelligent agents) and CommonRoad (solution feasibility, collision rate, comfort metrics); provides complete evaluation harness code and debugging workflows for planning failures.

---
