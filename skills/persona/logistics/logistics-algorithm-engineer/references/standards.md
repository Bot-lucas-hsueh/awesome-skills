# Standards & Reference

## 7.1 Optimization Algorithms

### Routing Problems
| Problem | Algorithm | Complexity |
|---------|-----------|------------|
| TSP | Nearest neighbor, 2-opt, OR-Tools | NP-hard |
| VRP | Clarke-Wright, Google OR-Tools | NP-hard |
| VRPTW | Genetic algorithm | NP-hard |

### Inventory Optimization
| Model | Use Case |
|-------|----------|
| EOQ | Constant demand |
| Newsvendor | Single period |
| (s,S) | Continuous review |
| Multi-echelon | Network optimization |

## 7.2 Supply Chain Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Fill rate | Orders fulfilled / ordered | > 98% |
| Inventory turnover | COGS / Avg inventory | Industry dependent |
| Days of inventory | Inventory / (COGS/365) | Match demand |
| Perfect order rate | No defects/tardies | > 95% |
| Supply chain cost | Total costs / Revenue | < 10% |
