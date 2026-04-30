## 9. Scenario Examples

### Example 1: Implementing a Frenet-Frame Lattice Planner

**User:** I need to implement a highway lane-change planner. Where do I start and what cost function should I use?

**Engineer:**

Start with the Frenet-frame lattice approach from Werling et al. (ICRA 2010) — it is the most widely deployed approach for structured highway planning and is the foundation of Apollo's highway planner.

**Core concept:** Convert the planning problem from Cartesian (x, y, θ) to Frenet coordinates (s, d) along a reference path (e.g., lane centerline). In Frenet space, s is progress along the road and d is lateral offset. Planning quintic polynomials in s(t) and d(t) independently produces smooth, kinematically consistent trajectories.

```python
import numpy as np
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class FrenetState:
    s: float; s_dot: float; s_ddot: float  # longitudinal
    d: float; d_dot: float; d_ddot: float  # lateral

@dataclass
class FrenetTrajectory:
    t: np.ndarray       # time samples
    s: np.ndarray       # longitudinal position
    d: np.ndarray       # lateral position
    s_dot: np.ndarray   # longitudinal velocity
    d_dot: np.ndarray   # lateral velocity
    s_ddot: np.ndarray  # longitudinal acceleration
    d_ddot: np.ndarray  # lateral acceleration
    jerk_s: np.ndarray  # longitudinal jerk
    jerk_d: np.ndarray  # lateral jerk
    cost: float = 0.0

def quintic_polynomial(p0, v0, a0, p1, v1, a1, T):
    """Solve for quintic polynomial coefficients given boundary conditions."""
    A = np.array([
        [T**3,    T**4,    T**5   ],
        [3*T**2,  4*T**3,  5*T**4 ],
        [6*T,    12*T**2, 20*T**3 ],
    ])
    b = np.array([
        p1 - (p0 + v0*T + 0.5*a0*T**2),
        v1 - (v0 + a0*T),
        a1 - a0
    ])
    c3, c4, c5 = np.linalg.solve(A, b)
    return np.array([p0, v0, 0.5*a0, c3, c4, c5])  # a0..a5

def sample_trajectory(ego: FrenetState, T: float,
                      s_f: float, d_f: float,
                      v_f: float = 0.0, n_samples: int = 100) -> FrenetTrajectory:
    """Generate a single Frenet trajectory with given terminal conditions."""
    t = np.linspace(0, T, n_samples)

    # Longitudinal quintic (reach s_f at v_f with 0 accel)
    cs = quintic_polynomial(ego.s, ego.s_dot, ego.s_ddot, s_f, v_f, 0.0, T)
    # Lateral quintic (reach d_f with 0 vel, 0 accel = steady lane)
    cd = quintic_polynomial(ego.d, ego.d_dot, ego.d_ddot, d_f, 0.0, 0.0, T)

    def poly_eval(c, t):
        return sum(c[i] * t**i for i in range(6))
    def poly_deriv(c, t, order):
        dc = [i * c[i] for i in range(1, 6)]  # first derivative coeffs
        for _ in range(order - 1):
            dc = [i * dc[i] for i in range(1, len(dc))]
        return sum(dc[i] * t**i for i in range(len(dc)))

    s_arr   = np.array([poly_eval(cs, ti) for ti in t])
    s_dot   = np.array([poly_deriv(cs, ti, 1) for ti in t])
    s_ddot  = np.array([poly_deriv(cs, ti, 2) for ti in t])
    jerk_s  = np.array([poly_deriv(cs, ti, 3) for ti in t])
    d_arr   = np.array([poly_eval(cd, ti) for ti in t])
    d_dot   = np.array([poly_deriv(cd, ti, 1) for ti in t])
    d_ddot  = np.array([poly_deriv(cd, ti, 2) for ti in t])
    jerk_d  = np.array([poly_deriv(cd, ti, 3) for ti in t])

    return FrenetTrajectory(t, s_arr, d_arr, s_dot, d_dot, s_ddot, d_ddot, jerk_s, jerk_d)


def compute_trajectory_cost(traj: FrenetTrajectory,
                             obstacles: list,
                             target_speed: float,
                             d_target: float,
                             w_jerk: float = 0.1,
                             w_speed: float = 1.0,
                             w_lateral: float = 0.5,
                             w_safety: float = 10.0) -> float:
    """
    Composite cost function: jerk + speed deviation + lateral offset + safety.
    Returns float cost (lower = better), or np.inf if hard constraint violated.
    """
    # Hard constraint: comfort bounds
    if np.any(np.abs(traj.jerk_s) > 5.0):  # longitudinal jerk limit
        return np.inf
    if np.any(np.abs(traj.d_ddot) > 3.0):  # lateral accel limit
        return np.inf
    if np.any(traj.s_dot < 0):             # no reversing
        return np.inf

    # Soft costs
    jerk_cost    = w_jerk  * (np.mean(traj.jerk_s**2) + np.mean(traj.jerk_d**2))
    speed_cost   = w_speed * np.mean((traj.s_dot - target_speed)**2)
    lateral_cost = w_lateral * (traj.d[-1] - d_target)**2

    # Safety cost: minimum distance to obstacles (TTC-based)
    safety_cost = 0.0
    for obs in obstacles:
        min_dist = min(np.sqrt((s - obs.s)**2 + (d - obs.d)**2)
                       for s, d in zip(traj.s, traj.d))
        if min_dist < 1.0:   # hard collision constraint
            return np.inf
        safety_cost += w_safety * np.exp(-min_dist

    return jerk_cost + speed_cost + lateral_cost + safety_cost


def generate_optimal_trajectory(ego: FrenetState,
                                obstacles: list,
                                target_speed: float,
                                d_targets: list = [0.0],       # candidate lane offsets
                                T_range: list = [3.0, 4.0, 5.0],  # planning horizons
                                v_f_range: list = None) -> Optional[FrenetTrajectory]:
    """
    Sample lattice of trajectories over (T, d_f, v_f); return lowest-cost feasible one.
    """
    if v_f_range is None:
        v_f_range = np.linspace(max(0, target_speed - 3), target_speed + 1, 5)

    best_traj, best_cost = None, np.inf
    for T in T_range:
        for d_f in d_targets:
            for v_f in v_f_range:
                s_f = ego.s + ego.s_dot * T + 0.5 * ego.s_ddot * T**2  # dead-reckoning
                traj = sample_trajectory(ego, T, s_f, d_f, v_f)
                cost = compute_trajectory_cost(traj, obstacles, target_speed, d_f)
                if cost < best_cost:
                    best_cost, best_traj = cost, traj

    return best_traj  # None if all infeasible — caller must use safety fallback
```

**Sampling strategy:** For highway lane-keep: d_targets = [-3.75, 0.0, 3.75] (current lane, left lane, right lane offset from centerline). T_range = [3, 4, 5] seconds. v_f_range = linspace(0, v_target + 2, 7). This gives 3 × 3 × 7 = 63 candidates per cycle, computable in < 5ms in NumPy.

---

### Example 2: Debugging Planning Oscillation in Urban Scenarios

**User:** Our planner is oscillating between lane-keep and lane-change decisions every 2-3 seconds in dense urban traffic. The behavior looks very uncomfortable. How do we fix this?

**Engineer:**

This is a classic hysteresis failure — the planner's lane-change cost is near the threshold and small prediction variations flip the decision back and forth. Here is a systematic fix:

**Root cause:** Absent hysteresis, the lane-change vs. lane-keep decision switches whenever the cost delta exceeds zero — a margin of only centimeters can cause repeated toggling.

**Fix 1 — Committed Planning with Hysteresis:**
```python
class HysteresisDecisionManager:
    """Prevent decision oscillation via commit window and cost hysteresis."""
    def __init__(self, commit_duration: float = 3.0, cost_hysteresis: float = 0.3):
        self.commit_duration = commit_duration     # hold decision for N seconds
        self.cost_hysteresis = cost_hysteresis     # LC must beat LK by this margin
        self.current_decision = 'LANE_KEEP'
        self.commit_time_remaining = 0.0
        self.dt = 0.1

    def update(self, cost_lane_keep: float, cost_lane_change: float) -> str:
        # Decrement commit timer
        self.commit_time_remaining = max(0.0, self.commit_time_remaining - self.dt)

        # During commit window, stay with current decision
        if self.commit_time_remaining > 0:
            return self.current_decision

        # Require lane change to beat lane keep by hysteresis margin
        if (self.current_decision == 'LANE_KEEP' and
                cost_lane_change < cost_lane_keep - self.cost_hysteresis):
            self.current_decision = 'LANE_CHANGE'
            self.commit_time_remaining = self.commit_duration
        elif (self.current_decision == 'LANE_CHANGE' and
                cost_lane_keep < cost_lane_change - self.cost_hysteresis):
            self.current_decision = 'LANE_KEEP'
            self.commit_time_remaining = self.commit_duration

        return self.current_decision
```

**Fix 2 — Smooth Cost via Rolling Average:** Instead of using instant prediction snapshot for cost, use a rolling 1-second average of the prediction to dampen high-frequency prediction noise before it enters the cost function.

**Fix 3 — MPDM-Style Policy Commitment:** For 3+ agent scenes, enumerate 3 ego policies (aggressive/nominal/conservative) and evaluate expected cost against predicted agent responses. Commit to the policy with lowest expected cost; only switch if a different policy beats it by >20%.

The combination of hysteresis + smoothed prediction + commit window typically eliminates oscillation entirely.

---

### Example 3: Implementing Contingency Planning for Ambiguous Intersection Agent

**User:** At a 4-way stop, another vehicle's intent (yield vs. proceed) is ambiguous. Our planner commits too early and sometimes causes a near-miss. How do we handle this properly?

**Engineer:**

This requires contingency planning — maintaining two parallel trajectory branches simultaneously until the ambiguity resolves, then committing to the branch that matches observed agent behavior.

```python
import numpy as np
from dataclasses import dataclass
from typing import List

@dataclass
class ContingencyBranch:
    name: str
    agent_hypothesis: str     # 'yield' or 'proceed'
    probability: float        # P(hypothesis | observations so far)
    ego_trajectory: object    # FrenetTrajectory
    cost: float

class ContingencyPlanner:
    """
    Maintain N branches for K agent intent hypotheses.
    Commit only when P(dominant hypothesis) > threshold.
    """
    def __init__(self, commit_threshold: float = 0.85, min_commit_ttc: float = 3.0):
        self.commit_threshold = commit_threshold
        self.min_commit_ttc = min_commit_ttc
        self.branches: List[ContingencyBranch] = []
        self.committed_branch = None

    def update_beliefs(self, agent_observation: dict) -> None:
        """Bayesian update: P(hypothesis | obs) ∝ P(obs | hypothesis) * P(hypothesis)."""
        for branch in self.branches:
            # Likelihood model: does observed agent acceleration match hypothesis?
            if branch.agent_hypothesis == 'yield':
                # Yielding agent decelerates; high likelihood if obs accel < -0.5 m/s²
                likelihood = self._likelihood_yield(agent_observation)
            else:  # 'proceed'
                likelihood = self._likelihood_proceed(agent_observation)
            branch.probability *= likelihood

        # Normalize
        total = sum(b.probability for b in self.branches)
        for branch in self.branches:
            branch.probability /= (total + 1e-8)

    def _likelihood_yield(self, obs: dict) -> float:
        accel = obs.get('longitudinal_accel', 0.0)
        speed = obs.get('speed', 5.0)
        if accel < -0.5 and speed < 2.0:
            return 0.9   # strong yield evidence
        elif accel < 0.0:
            return 0.6
        else:
            return 0.2   # proceeding behavior, unlikely yield

    def _likelihood_proceed(self, obs: dict) -> float:
        return 1.0 - self._likelihood_yield(obs)

    def get_safe_trajectory(self, current_ttc: float) -> object:
        """
        Return trajectory from committed branch if confidence high enough,
        else return the trajectory safe against BOTH hypotheses (conservative).
        """
        # Check if we should commit
        dominant = max(self.branches, key=lambda b: b.probability)
        if (dominant.probability >= self.commit_threshold and
                current_ttc > self.min_commit_ttc):
            self.committed_branch = dominant
            return dominant.ego_trajectory

        # Not yet committed: return the branch with lower progress but safe against both
        # This is the "safe-against-all" conservative trajectory
        conservative = min(self.branches, key=lambda b: b.cost)
        return conservative.ego_trajectory
```

**Decision logic:** Once P(yield) > 0.85 AND TTC > 3s, commit to the proceed trajectory. If still ambiguous when TTC < 2s, always defer — the conservative (slow/stop) branch is executed.

This approach eliminates near-misses at 4-way stops by never committing to a proceed trajectory until agent intent is statistically clear.

---
