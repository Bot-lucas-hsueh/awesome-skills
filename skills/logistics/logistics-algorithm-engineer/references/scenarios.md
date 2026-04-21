## § 9 Scenario Examples

### Scenario A: Last-Mile VRPTW — 500 Stops

**User:** "I have 500 delivery stops in a city, 20 vans with 500kg capacity each, and all customers have 2-hour delivery windows. How do I solve this efficiently?"

**Logistics Algorithm Engineer:**

> **Instance analysis**: 500 stops × 20 vehicles = medium-scale VRPTW. Exact methods will not converge in reasonable time. OR-Tools with Guided Local Search (GLS) is the production-recommended approach — it routinely achieves <5% optimality gap on Solomon benchmark instances of this scale within 60-120 seconds.
>
> **Step 1 — Build the time matrix using OSRM (not Euclidean distance):**
> ```python
> import requests
> import numpy as np
>
> def build_osrm_time_matrix(coordinates):
>     """
>     Build n×n travel time matrix using OSRM Table API.
>     coordinates: list of (lon, lat) tuples
>     Returns: n×n numpy array of travel times in seconds
>     """
>     coords_str = ";".join(f"{lon},{lat}" for lon, lat in coordinates)
>     url = f"http://router.project-osrm.org/table/v1/driving/{coords_str}"
>     params = {"annotations": "duration"}
>     response = requests.get(url, params=params).json()
>
>     if response.get("code") != "Ok":
>         raise ValueError(f"OSRM error: {response.get('message')}")
>
>     # Convert to integer seconds (OR-Tools requires integers)
>     matrix = np.array(response["durations"])
>     return np.round(matrix).astype(int)
> ```
>
> **Step 2 — Zone pre-clustering to reduce solver complexity:**
> ```python
> from sklearn.cluster import KMeans
>
> def zone_cluster(customer_df, n_zones=20):
>     """
>     Pre-cluster 500 stops into n_zones zones (one per vehicle).
>     This seeds the VRP solver with a good initial partition.
>     """
>     kmeans = KMeans(n_clusters=n_zones, random_state=42, n_init=10)
>     customer_df['zone'] = kmeans.fit_predict(
>         customer_df[['lat', 'lon']].values
>     )
>     return customer_df
> ```
>
> **Step 3 — Solve per zone with VRPTW, then merge and improve:**
> ```python
> # Use the solve_vrptw() function from § 8 with:
> # time_limit_seconds = 120
> # first_solution_strategy = PATH_CHEAPEST_ARC
> # metaheuristic = GUIDED_LOCAL_SEARCH
>
> # Expected performance on 500-stop instance:
> # - Runtime: 60-120 seconds on 8-core machine
> # - Optimality gap: 3-6% vs. lower bound
> # - Vehicle utilization: typically 80-92%
> # - On-time rate: >97% if time windows are not overly tight
> ```
>
> **Expected ROI**: Compared to manual dispatch, OR-Tools VRPTW typically reduces total distance by 15-25%, fleet size by 1-3 vehicles, and on-time rate improves from ~88% manual to >95% optimized.

---

### Scenario B: Warehouse Slotting — ABC Analysis + QAP

**User:** "Our warehouse picking team walks 12km per shift. I want to reduce travel distance by optimizing where SKUs are stored."

**Logistics Algorithm Engineer:**

> **Problem formulation**: This is a **Quadratic Assignment Problem (QAP)** — assign n SKUs to n slots to minimize total weighted travel distance. QAP is NP-hard; for 1000+ SKUs, use ABC velocity analysis to first reduce the search space, then apply a greedy heuristic.
>
> **Step 1 — ABC Velocity Analysis:**
> ```python
> import pandas as pd
>
> def abc_velocity_analysis(order_lines_df, sku_col='sku_id', cutoffs=(0.70, 0.90)):
>     """
>     Classify SKUs by pick frequency (velocity).
>     A items = top 70% of picks (store closest to shipping dock)
>     B items = next 20% of picks
>     C items = bottom 10% of picks (store furthest away)
>     """
>     freq = order_lines_df[sku_col].value_counts().reset_index()
>     freq.columns = ['sku_id', 'pick_count']
>     freq['cum_pct'] = freq['pick_count'].cumsum()
>
>     def classify(cum_pct):
>         if cum_pct <= cutoffs[0]:
>             return 'A'
>         elif cum_pct <= cutoffs[1]:
>             return 'B'
>         return 'C'
>
>     freq['abc_class'] = freq['cum_pct'].apply(classify)
>
>     summary = freq.groupby('abc_class').agg(
>         sku_count=('sku_id', 'count'),
>         total_picks=('pick_count', 'sum')
>     )
>     summary['pct_of_picks'] = summary['total_picks']
>     print(summary)
>     return freq
> ```
>
> **Step 2 — Slot assignment by ABC class and distance from dock:**
> ```python
> def assign_slots_by_abc(sku_abc_df, slot_distances_df):
>     """
>     Assign A-class SKUs to closest slots, C-class to farthest.
>     slot_distances_df: DataFrame with columns ['slot_id', 'distance_from_dock']
>     """
>     slots_sorted = slot_distances_df.sort_values('distance_from_dock').reset_index(drop=True)
>
>     a_skus = sku_abc_df[sku_abc_df['abc_class'] == 'A']['sku_id'].tolist()
>     b_skus = sku_abc_df[sku_abc_df['abc_class'] == 'B']['sku_id'].tolist()
>     c_skus = sku_abc_df[sku_abc_df['abc_class'] == 'C']['sku_id'].tolist()
>
>     all_skus = a_skus + b_skus + c_skus
>     assignment = {sku: slots_sorted.loc[i, 'slot_id']
>                   for i, sku in enumerate(all_skus)}
>     return assignment
>
> # Expected improvement: 20-35% reduction in picker travel distance
> # based on published warehouse slotting benchmarks
> ```
>
> **Step 3 — Affinity-based refinement (frequently co-picked SKUs near each other):**
> ```python
> from itertools import combinations
> from collections import defaultdict
>
> def compute_sku_affinity(order_lines_df):
>     """
>     Compute pairwise co-pick frequency for SKU affinity slotting.
>     Returns dict of {(sku_a, sku_b): co_pick_count}
>     """
>     order_skus = order_lines_df.groupby('order_id')['sku_id'].apply(list)
>     affinity = defaultdict(int)
>     for skus in order_skus:
>         for a, b in combinations(sorted(set(skus)), 2):
>             affinity[(a, b)] += 1
>     return dict(sorted(affinity.items(), key=lambda x: -x[1]))
> ```
>
> **Typical results**: ABC + affinity slotting reduces average pick path from 12km to 7-9km per shift (25-42% reduction). Combine with S-shape or largest-gap routing policy for maximum impact.

---

### Scenario C: Multi-Depot Network Design Under Demand Uncertainty

**User:** "We're designing a nationwide distribution network. We have 50 candidate warehouse locations and need to select 5-8 to serve 200 demand zones. Demand forecasts have ±30% uncertainty."

**Logistics Algorithm Engineer:**

> **Problem type**: Stochastic Capacitated Facility Location Problem (SCFLP). Deterministic MILP is a good starting point; uncertainty is handled via scenario-based stochastic programming or robust optimization.
>
> **Deterministic MILP Formulation:**
> ```
> Sets:
>   I = candidate facility locations (|I| = 50)
>   J = demand zones (|J| = 200)
>   S = demand scenarios (|S| = 10, sampled from ±30% uncertainty)
>
> Parameters:
>   f_i   = fixed annual cost of opening facility i ($)
>   c_ij  = unit transportation cost from facility i to zone j ($/unit)
>   d_js  = demand at zone j under scenario s (units)
>   cap_i = capacity of facility i (units/year)
>   p_min, p_max = min and max number of open facilities (5, 8)
>
> Decision Variables:
>   y_i       ∈ {0,1}  = 1 if facility i is opened
>   x_ijs     ≥ 0      = fraction of zone j's demand served by facility i under scenario s
>
> Objective (minimize expected total cost):
>   min  Σ_i(f_i × y_i)  +  (1/|S|) × Σ_s Σ_i Σ_j(c_ij × x_ijs × d_js)
>
> Constraints:
>   Σ_i x_ijs = 1                    ∀ j,s   (demand satisfaction)
>   x_ijs ≤ y_i                      ∀ i,j,s (only open facilities serve)
>   Σ_j x_ijs × d_js ≤ cap_i × y_i  ∀ i,s   (capacity constraint)
>   Σ_i y_i ≥ p_min                  (min facilities)
>   Σ_i y_i ≤ p_max                  (max facilities)
>   y_i ∈ {0,1}, x_ijs ≥ 0
> ```
>
> ```python
> import pulp
>
> def solve_stochastic_facility_location(facilities, demand_zones, scenarios,
>                                         fixed_costs, transport_costs, capacities,
>                                         p_min=5, p_max=8):
>     """
>     Solve stochastic capacitated facility location via deterministic equivalent MILP.
>
>     facilities: list of facility IDs
>     demand_zones: list of zone IDs
>     scenarios: list of dicts {zone_id: demand} per scenario
>     fixed_costs: dict {facility_id: annual_fixed_cost}
>     transport_costs: dict {(facility_id, zone_id): unit_cost}
>     capacities: dict {facility_id: annual_capacity}
>     """
>     prob = pulp.LpProblem("Stochastic_FLP", pulp.LpMinimize)
>     n_scenarios = len(scenarios)
>
>     # Decision variables
>     y = {i: pulp.LpVariable(f"y_{i}", cat='Binary') for i in facilities}
>     x = {(i, j, s): pulp.LpVariable(f"x_{i}_{j}_{s}", lowBound=0, upBound=1)
>          for i in facilities for j in demand_zones for s in range(n_scenarios)}
>
>     # Objective
>     fixed = pulp.lpSum(fixed_costs[i] * y[i] for i in facilities)
>     transport = (1.0
>         transport_costs.get((i, j), 1e9) * x[i, j, s] * scenarios[s].get(j, 0)
>         for i in facilities for j in demand_zones for s in range(n_scenarios)
>     )
>     prob += fixed + transport
>
>     # Constraints
>     for j in demand_zones:
>         for s in range(n_scenarios):
>             prob += pulp.lpSum(x[i, j, s] for i in facilities) == 1  # demand satisfaction
>
>     for i in facilities:
>         for j in demand_zones:
>             for s in range(n_scenarios):
>                 prob += x[i, j, s] <= y[i]  # linking
>
>     for i in facilities:
>         for s in range(n_scenarios):
>             prob += (pulp.lpSum(x[i, j, s] * scenarios[s].get(j, 0)
>                                 for j in demand_zones)
>                      <= capacities[i] * y[i])  # capacity
>
>     prob += pulp.lpSum(y[i] for i in facilities) >= p_min
>     prob += pulp.lpSum(y[i] for i in facilities) <= p_max
>
>     solver = pulp.HiGHS_CMD(msg=True, timeLimit=600)
>     prob.solve(solver)
>
>     open_facilities = [i for i in facilities if pulp.value(y[i]) > 0.5]
>     total_cost = pulp.value(prob.objective)
>
>     return open_facilities, total_cost, pulp.LpStatus[prob.status]
> ```
>
> **Handling the ±30% uncertainty edge case**: Generate 10 demand scenarios by sampling from a truncated normal distribution (mean = base forecast, sigma = base × 0.15). The stochastic MILP selects facilities that are robust across all scenarios — typically yielding 8-12% higher fixed cost vs. deterministic model but 20-35% lower expected cost in high-variability years.

---
