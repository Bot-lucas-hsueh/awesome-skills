## §4 · Engineering Systems

### §4.1 · DeepRed Dispatch System

**Architecture:**

```
┌─────────────────────────────────────────────────────────────┐
│                      DEEPRED DISPATCH                        │
│              (Reinforcement Learning Engine)                 │
├─────────────────────────────────────────────────────────────┤
│  INPUTS                        │  OUTPUTS                   │
│  • Order (pickup, dropoff)     │  • Dasher assignment       │
│  • Dasher locations/status     │  • Route optimization      │
│  • Restaurant prep times (ML)  │  • Batching decisions      │
│  • Traffic patterns            │  • ETA predictions         │
│  • Historical delivery data    │  • Quality scores          │
│  • Real-time demand/supply     │  • Incentive triggers      │
└─────────────────────────────────────────────────────────────┘
```

**Key Algorithms:**

| Algorithm | Purpose | Approach |
|-----------|---------|----------|
| **ETA Prediction** | Accurate delivery time estimates | Deep learning on prep + travel + parking |
| **Dasher Matching** | Real-time assignment | Multi-factor scoring (location, load, ratings) |
| **Batching Optimization** | Stack orders efficiently | Integer programming with quality constraints |
| **Supply Positioning** | Predict demand hotspots | Time series forecasting + RL incentives |
| **Dynamic Pricing** | Balance supply-demand | Real-time surge algorithms |

### §4.2 · ML Feature Store (Riviera)

| Feature Category | Examples | Latency | Use Case |
|------------------|----------|---------|----------|
| **Real-time** | Dasher location, order status, traffic | <100ms | Dispatch decisions |
| **Near-real-time** | Restaurant wait times, demand surge | <1min | ETA adjustments |
| **Batch** | User preferences, historical patterns | Hourly | Personalization |
| **Predictive** | Demand forecasting, prep time | Minutes | Supply positioning |

### §4.3 · Key Performance Indicators

| Metric | Definition | Target | Context |
|--------|------------|--------|---------|
| **On-Time %** | Deliveries within ETA promise | >95% | Core reliability metric |
| **Consumer NPS** | Net Promoter Score | >60 | Loyalty indicator |
| **Dasher Retention** | 30-day active rate | >70% | Supply health |
| **Merchant GMV Growth** | YoY growth per merchant | >20% | Partner success |
| **Batch Rate** | % of orders batched | 30-40% | Efficiency sweet spot |
| **Delivery Time** | End-to-end delivery minutes | <30 min avg | Speed promise |
| **Contribution Margin** | Profit per order | Positive | Unit economics |

---
