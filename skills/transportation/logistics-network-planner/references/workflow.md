## § 8 · Standard Workflow

### 8.1 Network Design Project

```
Phase 1: Analysis & Data Gathering
├── Collect customer location data, order volumes, SLAs
├── Analyze current network performance (cost per unit, service levels)
├── Identify constraints (facility capacity, carrier capabilities)
└── Define optimization objectives (cost, service, sustainability)

Phase 2: Candidate Design
├── Generate facility location alternatives (3-5 scenarios)
├── Design routing options for each (direct, milk-run, hub-and-spoke)
├── Calculate capacity requirements for each scenario
└── Model inventory positioning strategy

Phase 3: Optimization & Selection
├── Run optimization models for each scenario
├── Compare total landed cost vs. service level
├── Perform sensitivity analysis (demand volatility, fuel cost)
└── Select optimal configuration with risk assessment

Phase 4: Implementation Planning
├── Detail facility requirements (size, equipment, labor)
├── Develop carrier transition plan
├── Create implementation timeline
└── Define success metrics and monitoring
```

### 8.2 Route Optimization

```
Step 1: Define constraints (vehicle capacity, time windows, driver hours)
Step 2: Input stops and demand (delivery locations, quantities)
Step 3: Generate route alternatives (nearest neighbor, savings algorithm)
Step 4: Optimize using VRP solver (minimize distance/time/cost)
Step 5: Validate against constraints (check capacity, time windows)
Step 6: Output route plan (sequence, estimated times, load plan)
```

---
