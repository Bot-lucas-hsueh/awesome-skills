# python Example

```
def check_kinematic_feasibility(trajectory, max_steer_angle=35.0,
                                 max_steer_rate=20.0, wheelbase=2.7):
    """Verify trajectory satisfies bicycle model constraints."""
    for i in range(len(trajectory) - 1):
        dt = trajectory.t[i+1] - trajectory.t[i]
        v = trajectory.s_dot[i]
        kappa = trajectory.curvature[i]  # 1/R

        # Maximum steering angle: tan(delta) = kappa * wheelbase
        delta = np.degrees(np.arctan(kappa * wheelbase))
        if abs(delta) > max_steer_angle:
            return False, f"Steering angle {delta:.1f}° exceeds limit {max_steer_angle}°"

        # Maximum steering rate
        if i > 0:
            delta_prev = np.degrees(np.arctan(trajectory.curvature[i-1] * wheelbase))
            steer_rate = abs(delta - delta_prev)
            if steer_rate > max_steer_rate:
                return False, f"Steer rate {steer_rate:.1f} deg/s exceeds {max_steer_rate}"
    return True, "OK"

traj = optimize_smooth_path(waypoints)
feasible, reason = check_kinematic_feasibility(traj)
if not feasible:
    traj = replan_with_tighter_curvature_bound(waypoints)
```
