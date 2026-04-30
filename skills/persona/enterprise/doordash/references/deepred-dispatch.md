# DeepRed Dispatch System — Technical Reference

## Overview

DeepRed is DoorDash's reinforcement learning-based dispatch system that powers real-time order assignment, batching, and ETA prediction. Named after the chess-playing computer Deep Blue, it represents the cutting edge of on-demand logistics optimization.

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DEEPRED DISPATCH SYSTEM                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   INPUTS     │───►│    CORE      │───►│   OUTPUTS    │          │
│  │   LAYER      │    │   ENGINE     │    │   LAYER      │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                   │                   │                   │
│         ▼                   ▼                   ▼                   │
│  • Orders            • RL Policy          • Dasher Assignments     │
│  • Dasher State      • Batching Logic     • Route Optimization     │
│  • Restaurant Data   • ETA Models         • ETA Predictions        │
│  • Traffic           • Quality Scoring    • Incentive Triggers     │
│  • Historical Data   • Supply Position    • Batch Decisions        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Core Components

### 1. Order Ingestion & Feature Engineering

**Order Features:**
```python
order_features = {
    # Spatial
    'pickup_lat': float,
    'pickup_lng': float,
    'dropoff_lat': float,
    'dropoff_lng': float,
    
    # Temporal
    'created_at': timestamp,
    'promised_eta': minutes,
    
    # Merchant
    'restaurant_id': string,
    'prep_time_estimate': minutes,
    'restaurant_busyness_score': float,
    
    # Order
    'item_count': int,
    'total_value': dollars,
    'order_complexity': float,
    
    # Consumer
    'customer_tier': string,
    'order_history': list,
    'delivery_instructions': text
}
```

### 2. Dasher State Management

**Dasher Features:**
```python
dasher_features = {
    # Location & Status
    'current_lat': float,
    'current_lng': float,
    'status': enum[available, en_route, pickup, delivery],
    
    # Load
    'active_orders': list[Order],
    'estimated_completion_time': timestamp,
    
    # Performance
    'rating': float,
    'on_time_rate': float,
    'completion_rate': float,
    'experience_level': enum[new, experienced, veteran],
    
    # Preferences
    'preferred_zones': list,
    'vehicle_type': enum[car, bike, scooter],
    'shift_schedule': list
}
```

### 3. Reinforcement Learning Policy

**State Space:**
- Current orders awaiting dispatch
- Available Dashers with locations
- Active deliveries in progress
- Restaurant queue depths
- Traffic conditions
- Time of day, day of week

**Action Space:**
- Assign Dasher to Order
- Batch Orders together
- Wait for better match
- Trigger incentive

**Reward Function:**
```python
def calculate_reward(action_result):
    reward = 0
    
    # Consumer satisfaction
    reward += eta_accuracy_bonus * 10
    reward += on_time_bonus * 20
    reward += customer_rating * 5
    
    # Dasher efficiency  
    reward += dasher_earnings_per_hour * 2
    reward -= dasher_idle_time * 0.5
    
    # Platform efficiency
    reward += batching_efficiency_savings * 3
    reward -= missed_eta_penalty * 15
    
    return reward
```

### 4. Batching Optimization

**Batching Decision Criteria:**

| Factor | Weight | Description |
|--------|--------|-------------|
| Geographic proximity | High | Pickup/dropoff locations within acceptable radius |
| Time compatibility | High | Prep times aligned for simultaneous pickup |
| Quality impact | Critical | No order's ETA degraded beyond threshold |
| Dasher capacity | High | Vehicle type, current load |
| Order value | Medium | Higher value orders get priority consideration |

**Batching Algorithm:**
```python
def should_batch(order_a, order_b, dasher):
    # Calculate individual ETAs
    eta_a_solo = calculate_eta(order_a, dasher)
    eta_b_solo = calculate_eta(order_b, dasher)
    
    # Calculate batched ETA
    batched_eta_a, batched_eta_b = calculate_batched_eta(
        order_a, order_b, dasher
    )
    
    # Quality checks
    if batched_eta_a > eta_a_solo + MAX_ACCEPTABLE_DELAY:
        return False
    if batched_eta_b > eta_b_solo + MAX_ACCEPTABLE_DELAY:
        return False
    if batched_eta_a > ABSOLUTE_MAX_ETA or batched_eta_b > ABSOLUTE_MAX_ETA:
        return False
    
    # Efficiency check
    efficiency_gain = (eta_a_solo + eta_b_solo) - max(batched_eta_a, batched_eta_b)
    if efficiency_gain < MIN_EFFICIENCY_THRESHOLD:
        return False
    
    return True
```

### 5. ETA Prediction Model

**ETA Decomposition:**
```
Total ETA = 
    Order Acceptance Time
  + Restaurant Prep Time (ML predicted)
  + Dasher Travel to Restaurant
  + Parking & Pickup Time
  + Travel to Customer
  + Parking & Handoff Time
  + Buffer (for uncertainty)
```

**ML Features for ETA Prediction:**

| Category | Features | Model Type |
|----------|----------|------------|
| **Prep Time** | Restaurant history, item count, time of day, day of week | XGBoost/LightGBM |
| **Travel Time** | Distance, traffic, route complexity | Neural Network |
| **Parking** | Location type, time of day, historical data | Random Forest |
| **Uncertainty** | Weather, events, historical variance | Ensemble |

**Urban Adjustments:**
- Parking difficulty score (+2-5 min in dense areas)
- Building type (high-rise +2-4 min)
- Restaurant congestion (+1-3 min during peak)

---

## Dispatch Decision Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    DISPATCH PIPELINE                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. ORDER RECEIVED                                          │
│     └── Restaurant confirms order                           │
│         └── Trigger: Order ready for dispatch              │
│                                                             │
│  2. CANDIDATE GENERATION                                    │
│     └── Find Dashers within radius                         │
│         └── Filter: Available, qualified, proximity        │
│                                                             │
│  3. SCORING                                                 │
│     └── Score each candidate Dasher                        │
│         └── Factors: Distance, ETA, rating, load, etc.     │
│                                                             │
│  4. BATCHING CHECK                                          │
│     └── Check for batchable orders                         │
│         └── Validate: Quality thresholds, compatibility    │
│                                                             │
│  5. ASSIGNMENT                                              │
│     └── Select optimal Dasher + batch                      │
│         └── Send offer to Dasher                           │
│                                                             │
│  6. CONFIRMATION                                            │
│     └── Dasher accepts/declines                            │
│         └── If declined: Re-queue to next candidate        │
│                                                             │
│  7. EXECUTION                                               │
│     └── Track delivery progress                            │
│         └── Update ETA in real-time                        │
│         └── Handle exceptions                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Quality Gates

### Pre-Dispatch Checks
- [ ] Dasher rating >= threshold
- [ ] Dasher completion rate >= threshold
- [ ] Order within Dasher service area
- [ ] Vehicle type matches order requirements
- [ ] No recent violations or issues

### Batching Quality Gates
- [ ] No order's ETA degraded beyond MAX_ACCEPTABLE_DELAY
- [ ] Total batched route time < threshold
- [ ] Food temperature risk assessed (hot food priority)
- [ ] Customer tier consideration (DashPass, high-value)

### Real-Time Adjustments
- [ ] Monitor for traffic incidents
- [ ] Detect restaurant delays
- [ ] Re-route if faster path available
- [ ] Trigger customer communication if delays expected

---

## Performance Metrics

### System-Level Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Dispatch latency | <500ms | Time from order ready to offer sent |
| Assignment rate | >95% | % of orders successfully assigned |
| Batching rate | 30-40% | % of orders in multi-order batches |
| ETA accuracy | ±3 min | Mean absolute error |
| On-time % | >95% | % delivered within promised ETA |

### Optimization Metrics

| Metric | Target | Impact |
|--------|--------|--------|
| Dasher utilization | >75% | % of time Dasher is active on order |
| Miles per delivery | Minimize | Efficiency of routing |
| Dasher earnings/hour | >$20 | Dasher satisfaction |
| Consumer NPS | >60 | Overall satisfaction |

---

## Reinforcement Learning Training

### Training Pipeline
1. **Data Collection**: Real dispatch decisions and outcomes
2. **Simulation**: Test new policies in simulation
3. **Shadow Mode**: Run parallel to production
4. **A/B Testing**: Gradual rollout
5. **Full Deployment**: Monitor continuously

### Reward Shaping
- **Immediate rewards**: Assignment success, ETA accuracy
- **Delayed rewards**: Customer rating, Dasher retention
- **Long-term rewards**: Marketplace growth, profitability

---

## Integration with Other Systems

| System | Integration | Purpose |
|--------|-------------|---------|
| **Riviera** | Feature store | Real-time features for ML |
| **Demand Forecasting** | Prediction | Supply positioning |
| **Pricing Engine** | Dynamic fees | Balance supply-demand |
| **Dasher App** | Notifications | Offer delivery, navigation |
| **Consumer App** | ETA display | Real-time updates |
| **Merchant Portal** | Prep time | Order ready signals |

---

## Key Algorithms Summary

| Component | Algorithm | Update Frequency |
|-----------|-----------|------------------|
| Dasher Matching | Multi-factor scoring + RL | Real-time |
| ETA Prediction | Deep learning ensemble | Per order |
| Batching | Integer programming | Per dispatch |
| Supply Positioning | Time series + RL | Every 15 min |
| Route Optimization | Modified Dijkstra/A* | Per assignment |

---

*Reference: DoorDash Engineering Blog, Reinforcement Learning Papers, Internal Documentation*
