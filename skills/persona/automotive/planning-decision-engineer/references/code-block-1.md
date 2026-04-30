# python Example

```
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
