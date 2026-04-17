## § 7 Standards and Reference

### Algorithm Complexity Reference

| Algorithm | Problem | Complexity | Practical Scale | Notes |
|-----------|---------|------------|-----------------|-------|
| Nearest Neighbor | TSP/VRP | O(n²) | 100,000+ nodes | Construction heuristic; solution quality ~20-25% above optimal |
| 2-opt | TSP | O(n²) per iteration | 10,000 nodes | Classic improvement; use with nearest-neighbor initialization |
| LKH-3 | TSP/VRP | O(n² log n) empirical | 1,000-100,000 nodes | Best known heuristic; near-optimal on most benchmarks |
| OR-Tools LNS | VRPTW | Varies | 50-5,000 stops | Production-recommended; guided LNS with CP-SAT backend |
| Branch & Cut | MILP | Exponential worst-case | <300 nodes for VRP | Exact; Gurobi/CPLEX; use for network design and facility location |
| Column Generation | VRP | Polynomial per column | 500-2,000 nodes | Exact or near-exact; handles VRPTW well; complex to implement |
| Genetic Algorithm | Any combinatorial | O(g × p × f) | 500-10,000 nodes | g = generations, p = population size, f = fitness eval cost |
| Simulated Annealing | Any combinatorial | O(iter × neighborhood) | 200-5,000 nodes | Easy to implement; sensitive to cooling schedule |
| Tabu Search | Any combinatorial | O(iter × neighborhood) | 200-10,000 nodes | Strong short-term memory prevents cycling; good for VRP |

### Performance Metrics

| Metric | Formula | Target | Benchmark |
|--------|---------|--------|-----------|
| **Optimality Gap** | `(best_found - lower_bound)
| **Vehicle Utilization Rate** | `actual_load
| **On-Time Delivery Rate** | `deliveries_on_time
| **Cost per Delivery** | `total_route_cost / number_of_stops` | Baseline − 10-20% | Compare before/after optimization with same demand set |
| **Route Density** | `stops / km_driven` | Urban: >2.5 stops/km; Suburban: >1.0; Rural: >0.3 | Lower density = longer routes; review zone boundaries |
| **Driver Utilization** | `active_driving_time
| **Fleet Size Reduction** | `(baseline_vehicles - optimized_vehicles)
| **Solver Runtime** | Wall-clock seconds to produce solution | Batch: <10 min; Tactical: <5 min; Real-time: <1 sec | Log p50/p95/p99; alert on p99 > 3× p50 |

---

## Phase 1: Problem Formulation and Data Preparation

```
STEP 1.1 — Define the Problem
  [ ] Identify problem type: pure routing / with scheduling
  [ ] Document objective function: minimize cost / distance / time / emissions
  [ ] List all hard constraints: capacity, time windows, driver hours, vehicle compatibility
  [ ] List all soft constraints: preferred windows, driver-customer affinity, toll avoidance
  [ ] Agree on instance scope: how many stops, vehicles, depots, time horizon

  [✓ Done]: Written problem statement with formal notation agreed with business owner
  [✗ FAIL]: Proceed without clear objective → model will optimize the wrong thing

STEP 1.2 — Data Acquisition and Validation
  [ ] Extract customer locations (lat/lon), time windows, demands, service times
  [ ] Build distance/time matrix (OSRM for batch; Google Maps API for time-dependent)
  [ ] Validate: no NaN coordinates, demands ≥ 0, time windows (open ≤ close)
  [ ] Check triangle inequality: expert(A,C) ≤ d(A,B) + d(B,C) for all triplets
  [ ] Profile demand distribution: mean, std dev, 95th percentile (for capacity planning)
  [ ] Detect infeasible customers: demand > max vehicle capacity → flag for special handling
```

> See [references/09-scenarios.md](./references/09-scenarios.md) for Phase 1 code templates (data validation, distance matrix)

### Phase 2: Algorithm Design and Solve

```
STEP 2.1 — Select Algorithm
  [ ] Determine instance size (n = number of customer nodes)
  [ ] If n < 100: try Gurobi/OR-Tools exact; set time limit 300s
  [ ] If 100 ≤ n < 1000: OR-Tools LNS with guided local search; time limit 120s
  [ ] If n ≥ 1000: custom metaheuristic (LKH-3 or GA/SA/Tabu); time limit 600s
  [ ] For real-time (< 1s budget): nearest-neighbor construction + 1-pass 2-opt

  [✓ Done]: Algorithm selected with documented rationale and time budget
  [✗ FAIL]: Using branch-and-cut on 500+ node VRP without decomposition

STEP 2.2 — Implement and Tune
  [ ] Implement solution with unit tests on small instances (n=5, n=10)
  [ ] Benchmark against OR-Tools baseline on medium instances
  [ ] Tune solver parameters: time limit, neighborhood size, perturbation rate
  [ ] Compute lower bound (LP relaxation or BHH bound) to calculate optimality gap
  [ ] Log solution quality and runtime for each instance size bucket
```

> See [references/09-scenarios.md](./references/09-scenarios.md) for Phase 2 code templates (OR-Tools VRPTW solver, metaheuristics)

### Phase 3: Validation and Deployment

```
STEP 3.1 — Solution Validation
  [ ] Compute optimality gap: (best_found - lower_bound)
  [ ] Verify all hard constraints satisfied: capacity, time windows, vehicle count
  [ ] Compare KPIs against baseline: cost per delivery, fleet size, utilization
  [ ] Run simulation backtest: replay 30 days of historical demand through new algorithm
  [ ] Conduct field pilot: select 10% of routes; compare planned vs. actual completion

  [✓ Done]: Optimality gap <5%, all constraints satisfied, KPI improvement ≥ 10%
  [✗ FAIL]: Gap >10% or any hard constraint violation → return to Phase 2

STEP 3.2 — Deployment
  [ ] Wrap solver as REST API (Flask/FastAPI): POST /optimize, GET /status/:job_id
  [ ] Implement async job queue for batch runs (Celery + Redis)
  [ ] Add timeout fallback: if solver exceeds limit, return best partial solution
  [ ] Set up monitoring: solution quality score, runtime p99, infeasibility rate
  [ ] Document override UI: dispatchers must be able to manually adjust routes
  [ ] Schedule model revalidation: monthly performance review against actuals

  [✓ Done]: API deployed, <1% infeasibility rate, latency p99 within SLA
  [✗ FAIL]: p99 latency > 3× SLA or infeasibility rate > 5% → scale back scope
```

---

## Quick Reference

| Scenario | Problem Type | Algorithm | Expected Outcome |
|----------|--------------|-----------|------------------|
| **A: Last-Mile VRPTW** | 500 stops, 20 vehicles, time windows | OR-Tools GLS + zone clustering | 15-25% distance reduction, 88%→95% on-time |
| **B: Warehouse Slotting** | ABC QAP, 12km picker travel | ABC velocity + affinity heuristic | 25-42% travel reduction |
| **C: Network Design** | 50 candidates, ±30% demand uncertainty | Stochastic MILP (PuLP + HiGHS) | Robust facility selection across scenarios |

### Anti-Patterns Summary

| Severity | Anti-Pattern | Mitigation |
|----------|--------------|------------|
| 🔴 High | Over-optimizing on historical data | Evaluate on held-out future dates |
| 🔴 High | Exact solver on 1000+ nodes | OR-Tools LNS or LKH-3 for large instances |
| 🔴 High | Ignoring soft constraints | Penalty terms in objective + tuning |
| 🟡 Medium | No sensitivity analysis | Multi-scenario analysis table |
| 🟡 Medium | Black-box model | Route explainability API |
| 🟡 Medium | Ignoring real-time drift | Kafka + re-optimization triggers |

---

