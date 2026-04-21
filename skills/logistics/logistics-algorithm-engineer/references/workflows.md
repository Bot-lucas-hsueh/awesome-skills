## § 8 Standard Workflow

### Phase 1: Problem Formulation and Data Preparation

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
  [ ] Check triangle inequality: d(A,C) ≤ d(A,B) + d(B,C) for all triplets
  [ ] Profile demand distribution: mean, std dev, 95th percentile (for capacity planning)
  [ ] Detect infeasible customers: demand > max vehicle capacity → flag for special handling
```

```python
# Data validation template
import numpy as np
import pandas as pd

def validate_vrp_input(customers_df, distance_matrix, vehicle_capacity):
    """
    Validate VRP input data before solving.
    Returns list of validation errors.
    """
    errors = []

    # Check coordinates
    if customers_df[['lat', 'lon']].isna().any().any():
        errors.append("NULL coordinates detected — fix before solving")

    # Check demands
    if (customers_df['demand'] < 0).any():
        errors.append(f"Negative demands: {(customers_df['demand'] < 0).sum()} records")

    oversized = customers_df[customers_df['demand'] > vehicle_capacity]
    if len(oversized) > 0:
        errors.append(f"Demand exceeds vehicle capacity: {len(oversized)} customers — needs split delivery")

    # Check time windows
    if 'time_window_open' in customers_df.columns:
        invalid_tw = customers_df[customers_df['time_window_open'] > customers_df['time_window_close']]
        if len(invalid_tw) > 0:
            errors.append(f"Infeasible time windows (open > close): {len(invalid_tw)} customers")

    # Check distance matrix
    n = len(distance_matrix)
    diag_violations = np.diag(distance_matrix).sum()
    if diag_violations > 0:
        errors.append("Non-zero diagonal in distance matrix")

    # Triangle inequality sample check (sample 1000 triplets)
    violations = 0
    sample_size = min(1000, n * (n-1) * (n-2) // 6)
    indices = np.random.choice(n, size=(sample_size, 3), replace=True)
    for a, b, c in indices:
        if a != b and b != c and a != c:
            if distance_matrix[a][c] > distance_matrix[a][b] + distance_matrix[b][c] + 1e-6:
                violations += 1
    if violations > 0:
        errors.append(f"Triangle inequality violations: {violations}

    return errors
```

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

```python
# OR-Tools VRPTW production template
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def solve_vrptw(distance_matrix, time_matrix, demands, time_windows,
                vehicle_capacities, depot=0, time_limit_seconds=60):
    """
    Solve VRPTW with OR-Tools.

    Args:
        distance_matrix: n×n integer distance matrix (meters)
        time_matrix: n×n integer travel time matrix (seconds)
        demands: list of n integer demands (depot = 0)
        time_windows: list of n (open, close) tuples in seconds from midnight
        vehicle_capacities: list of per-vehicle capacity integers
        depot: depot node index (default 0)
        time_limit_seconds: solver time budget

    Returns:
        routes: list of lists (node sequences per vehicle)
        total_distance: total route distance in meters
        metrics: dict with utilization, on_time_rate, optimality_gap
    """
    num_vehicles = len(vehicle_capacities)
    n = len(distance_matrix)

    manager = pywrapcp.RoutingIndexManager(n, num_vehicles, depot)
    routing = pywrapcp.RoutingModel(manager)

    # Distance callback
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Time callback
    def time_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return time_matrix[from_node][to_node]

    time_callback_index = routing.RegisterTransitCallback(time_callback)

    # Add Time Window dimension
    routing.AddDimension(
        time_callback_index,
        3600,        # max wait time (1 hour slack)
        86400,       # max route time (24 hours)
        False,       # Don't force start cumul to zero
        'Time'
    )
    time_dimension = routing.GetDimensionOrDie('Time')
    for location_idx, (open_time, close_time) in enumerate(time_windows):
        index = manager.NodeToIndex(location_idx)
        time_dimension.CumulVar(index).SetRange(open_time, close_time)

    # Add Capacity dimension
    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_index)
        return demands[from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,                    # null capacity slack
        vehicle_capacities,   # per-vehicle capacities
        True,                 # start cumul to zero
        'Capacity'
    )

    # Search parameters
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    search_parameters.time_limit.seconds = time_limit_seconds
    search_parameters.log_search = True

    solution = routing.SolveWithParameters(search_parameters)

    if not solution:
        return None, None, {"status": "INFEASIBLE"}

    # Extract routes
    routes = []
    total_distance = 0
    for vehicle_id in range(num_vehicles):
        route = []
        index = routing.Start(vehicle_id)
        while not routing.IsEnd(index):
            node = manager.IndexToNode(index)
            route.append(node)
            index = solution.Value(routing.NextVar(index))
        route.append(manager.IndexToNode(index))  # depot return
        routes.append(route)
        total_distance += sum(
            distance_matrix[route[i]][route[i+1]]
            for i in range(len(route)-1)
        )

    # Compute metrics
    loads = [sum(demands[n] for n in r[1:-1]) for r in routes]
    utilizations = [l
    metrics = {
        "status": "OPTIMAL" if routing.status() == 1 else "FEASIBLE",
        "total_distance_m": total_distance,
        "avg_vehicle_utilization": sum(utilizations)
        "active_vehicles": sum(1 for r in routes if len(r) > 2),
    }

    return routes, total_distance, metrics
```

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
