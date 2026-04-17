## § 3 · Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|--------------------|------------|
| Constraint violation at trajectory endpoints | 🔴 Critical | Kinematically infeasible trajectory sent to control causes actuator saturation and instability | Always verify kinematic feasibility with bicycle model forward simulation before committing trajectory |
| Single-mode prediction assumption in planner | 🔴 Critical | Plan optimal for most-likely prediction fails when agent takes minority mode (e.g., unexpected lane change) | Plan against full multi-modal distribution; maintain contingency plan for second-highest-probability mode |
| MPC solver infeasibility causing no output | 🔴 Critical | Missing control command causes vehicle to follow stale trajectory, potential collision | Always have a pre-computed fallback (constant-decel-to-stop); MPC must always return something safe |
| Comfort metric creep in production | 🟡 High | Passengers experience chronic nausea or unsafe perceived G-forces in robotaxi | Hard-code jerk (< 5 m/s³) and lateral acceleration (< 3 m/s²) as constraint bounds, not soft costs only |
| Planning horizon too short for complex scenes | 🟡 High | Shortsighted plan causes deadlock at intersection or necessitates aggressive late correction | Minimum 5s horizon for intersection planning; adaptive horizon extension in complex multi-agent scenes |
| Reactive oscillation in close-following scenario | 🟡 High | Jerky stop-go behavior from over-sensitive IDM parameters causes rear-end risk and poor experience | Tune IDM time headway T ≥ 1.5s, minimum gap s0 ≥ 2m; add velocity smoothing hysteresis |
| Over-conservative planning blocking intersection | 🟢 Medium | Excessively safe gap acceptance never finds a gap, vehicle stuck indefinitely | Implement timeout-based gap acceptance relaxation with V2X SPaT as override authority |

> **IMPORTANT**: Planning algorithm outputs must be validated in closed-loop simulation (CARLA, nuPlan reactive) before any road deployment. Comfort and safety constraints must be tuned for the specific vehicle dynamics model of the deployment platform.

---
