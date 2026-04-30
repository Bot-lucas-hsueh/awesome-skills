## § 3 Risk Disclaimer

**Before deploying any logistics optimization model, understand these domain-specific risks:**

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|--------------------|
| **Model-Reality Gap** | High | Distance matrices from static maps diverge from real travel times during peak hours, weather events, and road closures. A route optimal in the model may be infeasible or costly in practice | Use time-dependent travel time data (Google Maps Distance Matrix API with departure_time); validate against historical GPS traces quarterly |
| **Overfitting to Historical Data** | High | Routing models trained or tuned on historical demand distributions perform poorly when demand patterns shift (new customers, seasonal spikes, promotional events) | Use rolling 90-day training windows; include demand variability buffers; test on held-out future dates, not random splits |
| **Local Optima Traps** | Medium | Greedy construction heuristics and simulated annealing can converge to solutions 15-30% above optimal, especially on heterogeneous fleets | Run multi-start initialization with 10+ random seeds; apply LNS (Large Neighborhood Search) perturbation; compare against OR-Tools LNS upper bound |
| **Real-time Latency Failures** | High | A dispatch algorithm that runs in 200ms for 50 stops may time out at 500 stops in production, causing missed assignments and driver idle time | Load-test at 2x expected peak volume; implement timeout fallbacks to nearest-neighbor insertion; monitor p99 latency in production |
| **Data Quality Issues** | High | Invalid coordinates, duplicate customer IDs, infeasible time windows (close < open), and negative demands will cause solvers to produce incorrect or infeasible solutions | Implement pre-solve validation pipeline: coordinate bounding boxes, demand sign checks, time window feasibility checks, distance matrix triangle inequality audit |
| **Constraint Omission** | Medium | Real-world routing has soft constraints often omitted in models: driver break regulations (HOS rules), preferred customer time windows, vehicle-customer compatibility, and toll avoidance preferences | Maintain a constraint registry; categorize hard vs. soft; add soft constraints as penalty terms; conduct monthly constraint audit with operations team |

---
