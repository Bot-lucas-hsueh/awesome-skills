## § 4 · Core Philosophy

### 4.1 Logistics Network Optimization Framework

```
                    ┌─────────────────────────┐
                    │   SERVICE TARGETS       │
                    │ (Delivery time, %OTIF)  │
                    └───────────┬─────────────┘
                                ↓
        ┌───────────────────────────────────────────┐
        │         DEMAND ANALYSIS                   │
        │  (Volume,地理分布,季节性,SLAs)            │
        └───────────────────┬───────────────────────┘
                            ↓
        ┌───────────────────────────────────────────┐
        │      NETWORK CANDIDATE DESIGN              │
        │  (DC位置,Hub数量,路由方案)                 │
        └───────────────────┬───────────────────────┘
                            ↓
        ┌───────────────────────────────────────────┐
        │      COST-SERVICE OPTIMIZATION            │
        │  (Total landed cost vs. service level)     │
        └───────────────────┬───────────────────────┘
                            ↓
        ┌───────────────────────────────────────────┐
        │      RISK & RESILIENCE VERIFICATION       │
        │  (Single points, redundancy, contingency)  │
        └───────────────────────────────────────────┘
```

The framework starts with service requirements, analyzes demand patterns, generates candidate network configurations, optimizes for total cost at target service levels, and verifies resilience. Each iteration tests trade-offs between cost and service.

### 4.2 Guiding Principles

1. **Total Landed Cost**: Optimize the complete cost picture—not just transportation, but facility, inventory, and handling costs combined
2. **Service Level as Constraint**: Design to meet specific service targets (e.g., 95% OTD in 2 days) at minimum cost, not maximize service
3. **Network Resilience**: Design for failure—every critical node needs a backup
4. **Data-Driven Decisions**: Base location and routing decisions on quantitative analysis, not intuition

---

