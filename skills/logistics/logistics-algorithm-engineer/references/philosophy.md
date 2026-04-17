## § 4 Core Philosophy

### Optimization Pipeline

```
┌─────────────────────────────────────────────────────────────────────┐
│                  LOGISTICS OPTIMIZATION PIPELINE                    │
├──────────────┬──────────────┬──────────────┬──────────────┬─────────┤
│   PROBLEM    │    MODEL     │    SOLVE     │  VALIDATE    │ DEPLOY  │
│              │              │              │              │         │
│ - Define     │ - Sets &     │ - Exact:     │ - Optimality │ - API   │
│   objective  │   parameters │   Gurobi
│ - Identify   │ - Decision   │   CPLEX      │ - KPI vs     │ - A/B   │
│   constraints│   variables  │ - Heuristic: │   baseline   │   test  │
│ - Validate   │ - Objective  │   OR-Tools
│   data       │   function   │   LKH-3      │   backtest   │ - Retrain│
│ - Scope      │ - Constraint │ - Meta:      │ - Field      │         │
│   instance   │   set        │   GA / SA
│   size       │              │   Tabu       │              │         │
└──────────────┴──────────────┴──────────────┴──────────────┴─────────┘
       │               │              │              │            │
  Gate: Data      Gate: Scale    Gate: Budget   Gate: Gap    Gate: SLA
  quality OK?     <500 exact?    runtime OK?    <5%?         latency OK?
```

### Guiding Principles

1. **Model before code**: Every optimization problem deserves a formal mathematical specification before implementation. A clean MILP or CP formulation prevents ambiguity, exposes hidden constraints, and enables solver selection based on problem structure.

2. **Scale-appropriate methods**: No single algorithm wins at all scales. A branch-and-cut solver that finds optimal solutions for 100-stop instances will time out for 1000-stop instances. Always benchmark your specific instance size and select the method that delivers the best quality-within-time-budget tradeoff.

3. **Validation as a first-class concern**: An algorithm that produces a 10% better route on paper but is rejected by drivers because it ignores realistic constraints has zero business value. Validate solutions with operations teams, pilot on a subset of routes before full rollout, and track actual vs. planned KPIs after deployment.

---

