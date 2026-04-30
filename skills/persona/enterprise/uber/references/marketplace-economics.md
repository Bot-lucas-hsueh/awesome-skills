# Marketplace Economics at Uber

## Two-Sided Marketplace Fundamentals

Uber operates a **two-sided marketplace** connecting:
- **Supply side**: Drivers (mobility), Couriers (delivery), Carriers (freight)
- **Demand side**: Riders, Eaters, Shippers

### Key Economic Properties

| Property | Description |
|----------|-------------|
| **Network Effects** | More riders → more drivers → better service → more riders |
| **Cross-Side Network Effects** | Value to one side increases with participation on other side |
| **Same-Side Network Effects** | Limited (drivers compete for trips) |
| **Chicken-and-Egg Problem** | Need both sides to start marketplace |
| **Multi-Homing** | Drivers can work for multiple platforms (Lyft, DoorDash) |

---

## Marketplace Balance Metrics

### Health Indicators

| Metric | Target | Description |
|--------|--------|-------------|
| **Utilization Rate** | >70% | Driver active time with passenger/order |
| **Wait Time** | <5 min | Average time for rider to get pickup |
| **Completion Rate** | >95% | Requests that result in completed trips |
| **Cancellation Rate** | <5% | Trips cancelled by either party |
| **ETA Accuracy** | MAE <2 min | Difference between predicted and actual arrival |

### Imbalance Scenarios

| Scenario | Symptom | Solution |
|----------|---------|----------|
| **Undersupply** | Long wait times, high prices | Surge pricing, driver incentives |
| **Oversupply** | Low driver earnings, idle time | Demand stimulation, driver repositioning |
| **Geographic Mismatch** | Surge in some areas, idleness in others | Heatmaps, destination mode |

---

## Dynamic Pricing (Surge Pricing)

### Economic Theory

**Price as Signal**: Higher prices achieve:
1. **Supply Response**: Attract more drivers to high-demand areas
2. **Demand Management**: Discourage non-essential trips
3. **Market Clearing**: Balance supply and demand in real-time

### Price Elasticity

| Segment | Elasticity | Response to Price Increase |
|---------|-----------|---------------------------|
| Commuters | High | Shift to transit, delay trip |
| Airport | Low | Willing to pay premium |
| Entertainment | Medium | Some elasticity based on urgency |
| Late Night | Low | Few alternatives available |

### Surge Algorithm Components

```
┌────────────────────────────────────────────────────────┐
│                    SURGE CALCULATION                   │
├────────────────────────────────────────────────────────┤
│  Inputs:                                               │
│  • Demand: Ride requests, app opens, cancellations     │
│  • Supply: Active drivers, ETA to hot zone             │
│  • External: Weather, events, traffic                  │
│                                                        │
│  Processing:                                           │
│  1. Forecast demand 5-15 min ahead (ML model)          │
│  2. Calculate supply-demand ratio                      │
│  3. Apply price elasticity model                       │
│  4. Optimize for marketplace objectives                │
│                                                        │
│  Output:                                               │
│  • Surge multiplier (e.g., 1.5x, 2.0x)                │
│  • Geofenced zones with independent pricing            │
│  • Driver heatmap for supply repositioning             │
└────────────────────────────────────────────────────────┘
```

---

## Matching Economics

### Global vs. Local Optimization

| Approach | Description | Efficiency |
|----------|-------------|------------|
| **Greedy** | Assign nearest available driver | 70-80% optimal |
| **Batch** | Collect requests, solve globally | 90-95% optimal |
| **Predictive** | Anticipate demand, pre-position | 95%+ optimal |

### Matching Factors

1. **Proximity**: Distance between driver and rider
2. **ETA**: Estimated time to pickup
3. **Destination**: Driver's preferred direction
4. **Rating**: Driver and rider quality scores
5. **Service Type**: UberX, Black, Pool, etc.
6. **Supply Forecast**: Predicted future availability

### Batching Trade-offs

| Batch Window | Pros | Cons |
|--------------|------|------|
| 1 second | Near real-time | Suboptimal matching |
| 2-5 seconds | Good balance | Slight rider wait |
| 10+ seconds | Optimal matches | Riders may cancel |

---

## Causal Inference in Marketplace Experiments

### The SUTVA Problem

**Stable Unit Treatment Value Assumption (SUTVA)** violations occur when:
- Treated riders compete with control riders for same drivers
- Driver supply is finite and shared
- Network effects create spillovers

### Solutions

| Method | Description | Use Case |
|--------|-------------|----------|
| **Switchback** | Alternate treatment by time period | When geographic spillover likely |
| **Geographic Randomization** | Randomize by region | Large markets with natural boundaries |
| **Marketplace Model** | Model network effects explicitly | Complex multi-market experiments |
| **Instrumental Variables** | Use exogenous variation | When direct randomization impossible |

---

## Driver Economics

### Earnings Structure

| Component | Description |
|-----------|-------------|
| **Base Fare** | Fixed amount per trip |
| **Per-Mile/Minute** | Variable based on distance/time |
| **Surge Multiplier** | Additional earnings during high demand |
| **Promotions** | Quests, consecutive trip bonuses |
| **Tips** | Rider-provided gratuity |

### Driver Decision Factors

1. **Expected Earnings**: Hourly rate projection
2. **Flexibility**: Ability to work when convenient
3. **Utilization**: Time spent with passengers vs. idle
4. **Expenses**: Gas, maintenance, insurance
5. **Alternative Opportunities**: Lyft, DoorDash, traditional employment

---

## References

- [Practical Marketplace Optimization at Uber Using Causally-Informed ML](https://arxiv.org/abs/2106.06657)
- [How Uber Uses Predictive Analytics](https://brainforge.ai/uber-predictive-analytics/)
- [Uber Dynamic Pricing](https://www.uber.com/blog/uber-dynamic-pricing/)
