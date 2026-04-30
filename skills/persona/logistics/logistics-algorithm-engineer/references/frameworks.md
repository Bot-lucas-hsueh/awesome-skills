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
