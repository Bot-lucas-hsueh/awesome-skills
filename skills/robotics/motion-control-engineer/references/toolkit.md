## § 6 · Professional Toolkit

| Tool | Purpose — When to Use |
|------|----------------------|
| **Pinocchio 2.7** | Rigid-body dynamics library (URDF/SDF loading, RNEA for inverse dynamics, ABA for forward dynamics, Jacobian computation) — use for gravity compensation and MPC dynamics model |
| **Acados
| **CasADi 3.6** | Symbolic differentiation and NLP solver interface — use for offline trajectory optimization and MPC problem formulation |
| **ros2_control** | ROS2 real-time control framework — use for standardized hardware abstraction, controller manager, and lifecycle management |
| **SOEM (EtherCAT Master)** | Open-source EtherCAT master library — use for < 1ms deterministic communication with servo drives |
| **TOPP-RA** | Time-Optimal Path Parameterization — use to compute time-optimal velocity profiles along a given geometric path under torque/velocity/acceleration constraints |
| **MoveIt2** | Motion planning framework (OMPL, Pilz planners) — use for collision-aware path planning integrated with ros2_control |
| **Matplotlib + control (Python)** | Classical control analysis: Bode plots, root locus, step response simulation — use during controller design validation |
