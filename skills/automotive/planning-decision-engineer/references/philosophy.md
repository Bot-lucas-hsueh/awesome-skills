## § 4 · Core Philosophy

```
[Code block moved to code-block-1.md]
```

**4.1 Guiding Principles:**

1. **Safety is Not a Cost Term — It is a Constraint**: Safety must be encoded as hard constraints (not soft cost terms with weights) in the planning optimization. A "safe enough" plan with weight tuning is not acceptable for production AV — zero constraint-violating trajectories must be committed to execution.

2. **The Prediction-Planning Loop**: Planning and prediction are not independent sequential modules. The ego plan influences how other agents respond (game-theoretic interaction). At minimum, planning must account for the conditional prediction P(agent_i trajectory | ego plan) via contingency planning or MPDM-style policy enumeration.

3. **Comfort is a Business Metric**: In L4 robotaxi deployment, harsh braking and excessive lateral acceleration directly affect customer retention and regulatory scrutiny. Treat comfort metrics (jerk, lateral acceleration) as first-class product requirements, not secondary concerns after safety.

---

