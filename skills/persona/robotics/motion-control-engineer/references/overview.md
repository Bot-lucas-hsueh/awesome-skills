## § 2 · What This Skill Does

**Controller Design & Tuning** — Designs cascaded PID, LQR, and MPC controllers for robot joints and Cartesian space, providing complete transfer functions, stability margins, and systematic hardware tuning procedures. Includes anti-windup, derivative filtering, and gravity/friction compensation strategies.

**Real-Time ROS2 Control Implementation** — Implements custom ros2_control hardware interfaces and controllers in C++ with PREEMPT_RT compatibility, EtherCAT communication via SOEM, and lock-free data exchange between real-time and non-real-time threads.

**Inverse Kinematics & Trajectory Planning** — Solves analytical and numerical IK with singularity handling (damped least squares, null-space projection), generates time-optimal trajectories using TOPP-RA, and validates against joint limits and velocity/acceleration constraints.

**Force/Impedance Control for Safe HRI** — Implements Cartesian impedance control with tunable virtual stiffness/damping, admittance control for compliant motion, and generalized momentum observer for collision detection — enabling safe physical human-robot interaction.
