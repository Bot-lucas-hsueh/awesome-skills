## § 6 Professional Toolkit

### Optimization Solvers

| Tool | Type | Best For | License |
|------|------|----------|---------|
| **Gurobi** | MIP, LP, QP, MIQP | Large-scale MILP network design, exact VRP column generation; sub-second LP re-solves for real-time dispatch | Commercial (free academic) |
| **CPLEX (IBM)** | MIP, LP, CP | Enterprise TMS integration; constraint programming for scheduling problems with logical constraints | Commercial |
| **OR-Tools (Google)** | CP-SAT, VRP, Routing | Production-grade VRPTW solver; supports time windows, breaks, multi-depot; Python/C++/Java/Go | Apache 2.0 |
| **PuLP** | LP, MILP | Rapid prototyping of facility location and load assignment models in Python; solver-agnostic API | MIT |
| **SCIP** | MIP, MINLP | Research-grade exact solver for nonlinear logistics models; strong for academic benchmarking | ZIB Academic |
| **LKH-3** | TSP/VRP heuristic | State-of-the-art Lin-Kernighan-Helsgott heuristic; best-known solutions on Solomon benchmark instances | Free for research |
| **HiGHS** | LP, MIP | Open-source high-performance LP/MIP; excellent PuLP backend; 10-50x faster than CBC | MIT |

### Geospatial and Routing APIs

| Tool | Use Case |
|------|----------|
| **Google Maps Distance Matrix API** | Time-dependent travel times with `departure_time`; essential for realistic VRPTW distance matrices |
| **OSRM (Open Source Routing Machine)** | Self-hosted, high-throughput routing engine; 10,000+ distance matrix requests/second; ideal for batch route planning |
| **Valhalla** | Open-source routing with truck profile support (height/weight/hazmat restrictions); ideal for freight routing |
| **HERE Routing API** | Commercial truck routing with live traffic; supports hazmat, trailer dimensions, weight limits |

### Data and Pipeline Infrastructure

| Tool | Use Case |
|------|----------|
| **Apache Kafka** | Real-time event streaming for dynamic dispatch: new order events, GPS position updates, driver status changes |
| **Apache Airflow** | Batch optimization pipeline orchestration; daily route planning DAGs with dependency management and retry logic |
| **AnyLogic** | Agent-based and discrete-event simulation for logistics network validation before live deployment |
| **SimPy** | Python-native discrete-event simulation for warehouse throughput and dock scheduling analysis |

### Scientific Python Stack

| Library | Use Case |
|---------|----------|
| **NetworkX** | Graph modeling for network flow problems, shortest path preprocessing, distance matrix construction |
| **SciPy (spatial, optimize)** | K-means clustering for zone design, scipy.optimize for parameter tuning |
| **NumPy
| **Scikit-learn** | Demand forecasting for routing (RandomForest, gradient boosting), travel time prediction |

---
