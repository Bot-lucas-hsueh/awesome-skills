## §5 · Examples

### Example 1: Dispatch Optimization — Batching Decision

**Context:**
High-volume dinner rush in downtown Seattle. Three orders ready for dispatch from nearby restaurants:
- Order A: 2 miles north, 25 min ETA solo
- Order B: 1.5 miles northeast, 20 min ETA solo  
- Order C: 2.5 miles east, 28 min ETA solo

One dasher available nearby. Should we batch all three?

**Expert Response:**

**Batching Analysis:**

| Scenario | A ETA | B ETA | C ETA | Dasher Earnings | Efficiency |
|----------|-------|-------|-------|-----------------|------------|
| **Solo dispatch** | 25 min | 20 min | 28 min (wait) | $18 ($6×3) | Baseline |
| **Batch A+B** | 32 min (+7) | 26 min (+6) | 28 min (separate) | $21 (+$3) | +15% |
| **Batch A+B+C** | 38 min (+13) | 33 min (+13) | 40 min (+12) | $26 (+$8) | +20% |

**Decision Framework:**

**Option A: Batch A+B Only (Recommended)**
```
Rationale:
• Route: Dasher → Restaurant A → Restaurant B → Customer A → Customer B
• Total distance: 4.2 miles (vs 3.5 solo + 4 solo = 7.5 miles)
• Time impact: +6-7 minutes for A/B, but C gets separate dasher quickly
• Quality check: Both ETAs still <35 min (acceptable for dinner rush)
• Dasher benefit: +$3 for minimal extra time (~$24/hr effective rate)
```

**Option B: Batch All Three ❌**
```
Risk factors:
• Order C is 2.5 miles east — adds significant detour
• Customer C ETA slips to 40+ minutes (quality degradation)
• Food temperature risk for first pickup (A)
• One bad rating from C offsets efficiency gains
```

**Three-Sided Impact:**
| Side | Impact | Verdict |
|------|--------|---------|
| Consumers A/B | Minor delay, but still reasonable | ✅ Acceptable |
| Consumer C | Gets dedicated dasher, on-time | ✅ Positive |
| Merchants | All orders picked up promptly | ✅ Positive |
| Dasher | Higher earnings, efficient route | ✅ Positive |

**Recommendation:**
> Batch orders A+B with quality score threshold of 0.85. Dispatch separate dasher for C with priority flag to ensure <30 min delivery. Monitor customer satisfaction scores post-delivery.

---

### Example 2: Marketplace Balancing — Supply-Demand Mismatch

**Context:**
Phoenix submarket showing concerning patterns: Lunch rush (11:30-13:30) has 40% longer ETAs than target, but dinner is over-supplied with idle dashers.

**Expert Response:**

**Root Cause Analysis:**

| Factor | Lunch | Dinner | Gap |
|--------|-------|--------|-----|
| Order Volume | 2,500/hr | 3,200/hr | +28% |
| Active Dashers | 180 | 420 | +133% |
| Demand/Supply Ratio | 13.9 | 7.6 | -45% |
| Avg ETA | 42 min | 24 min | -43% |

**Supply-Demand Mismatch Diagnosis:**
- **Lunch**: Insufficient dasher supply for office/downtown orders
- **Dinner**: Excess supply due to part-time dashers joining after day jobs
- **Dasher Behavior**: Preference for evening flexibility, avoiding midday heat

**Intervention Strategy:**

**Phase 1: Immediate (This Week)**
```
Lunch Incentives:
• Peak Pay: +$3 per delivery (11:00-14:00)
• Hotspots: Dynamic zones around business districts
• Challenges: "Complete 3 lunch deliveries, earn extra $10"
• Promo to Dashers: "Lunch rush = higher earnings per hour"

Dinner Optimization:
• Reduce new dasher onboarding for evening shifts
• Shift some dinner-committed dashers to lunch via incentives
• Implement "early dinner" peak pay (16:30-17:30) to smooth demand
```

**Phase 2: Structural (Next Month)**
```
Scheduling Adjustments:
• Introduce lunch-shift scheduling blocks with guaranteed minimums
• Dasher Rewards tier bonus for lunch completion consistency
• Partner with businesses for corporate lunch accounts (predictable demand)

Demand Shaping:
• Free delivery promotions for off-peak ordering (10:30-11:30, 13:30-14:30)
• Scheduled orders: "Order by 10 AM for guaranteed 12 PM delivery"
```

**Success Metrics:**
| Metric | Current | 30-Day Target | 90-Day Target |
|--------|---------|---------------|---------------|
| Lunch ETA | 42 min | 32 min | 28 min |
| Dasher Utilization (Lunch) | 78% | 85% | 88% |
| Dasher Utilization (Dinner) | 62% | 75% | 80% |
| Consumer NPS | 45 | 55 | 60 |

**Three-Sided Impact Forecast:**
- **Consumers**: Lunch reliability improves dramatically
- **Merchants**: Lunch order volume increases 15-20%
- **Dashers**: More consistent earnings throughout day

---

### Example 3: ETA Prediction — ML Model Enhancement

**Context:**
Current ETA model under-predicting by average 4 minutes in dense urban areas (Manhattan, SF, Chicago). Need to improve prediction accuracy.

**Expert Response:**

**Problem Decomposition:**

```
ETA = Prep Time + Travel Time + Parking/Handoff Time

Current model errors:
├── Prep Time: ±3 min (acceptable)
├── Travel Time: ±2 min (acceptable)
└── Parking/Handoff: ±6 min (PROBLEM - underestimated in dense urban)
```

**Root Causes (Urban Context):**
1. **Parking time**: Not accounting for street parking search (2-5 min)
2. **Building access**: High-rises with doorman/security (2-4 min)
3. **Restaurant handoff**: Busy urban locations with crowded pickup areas
4. **Traffic model**: Doesn't capture last-mile micro-congestion

**Model Enhancement Plan:**

**Feature Engineering:**
| New Feature | Data Source | Expected Impact |
|-------------|-------------|-----------------|
| **Parking Difficulty Score** | Historical GPS + Street data | -2 min error |
| **Building Type** | Address lookup (high-rise vs house) | -1.5 min error |
| **Restaurant Busy Score** | Real-time order queue depth | -1 min error |
| **Micro-Traffic** | Live traffic APIs + historical patterns | -0.5 min error |

**Implementation:**

```python
# Urban ETA Model Enhancement
class UrbanETAPredictor:
    def predict(self, order):
        base_eta = super().predict(order)
        
        # Urban adjustments
        parking_time = self.parking_model.predict(
            lat=order.restaurant_lat,
            lng=order.restaurant_lng,
            time_of_day=order.created_at,
            day_of_week=order.created_at.weekday()
        )
        
        building_handoff = self.building_model.predict(
            address_type=order.customer_address.type,
            floor=order.customer_address.floor,
            doorman=order.customer_address.doorman
        )
        
        restaurant_congestion = self.congestion_model.predict(
            restaurant_id=order.restaurant_id,
            active_orders=order.restaurant.active_orders,
            avg_wait_time_30min=order.restaurant.recent_wait
        )
        
        return base_eta + parking_time + building_handoff + restaurant_congestion
```

**Validation Strategy:**
1. **Shadow Mode**: Run new model parallel to production for 2 weeks
2. **Backtest**: Historical accuracy on last 90 days of urban orders
3. **A/B Test**: 5% traffic → 50% → 100% rollout
4. **Metrics**: MAE (Mean Absolute Error), % within 5 minutes, customer satisfaction

**Expected Outcomes:**
| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| MAE (urban) | 4.2 min | 1.8 min | 57% better |
| % Within 5 min | 72% | 89% | +17pp |
| Consumer NPS | 52 | 61 | +9 points |
| On-Time % | 91% | 96% | +5pp |

---

### Example 4: Merchant Integration — National Chain Launch

**Context:**
New national pizza chain (500 locations) wants to launch on DoorDash. Need integration plan that ensures quality launch.

**Expert Response:**

**Phased Rollout Strategy:**

**Phase 1: Pilot (Weeks 1-2)**
```
Markets: 5 representative locations
• 1 urban high-volume (Manhattan)
• 2 suburban (Austin, Phoenix suburbs)
• 1 college town (Ann Arbor)
• 1 rural/smaller city (Boise)

Goals:
• Validate POS integration
• Calibrate prep time models
• Test packaging/handoff procedures
• Train restaurant staff

Success Criteria:
• <5% order error rate
• Prep time predictions within 3 minutes
• Consumer NPS > 50
• Merchant satisfaction > 4.0/5
```

**Phase 2: Expansion (Weeks 3-6)**
```
Markets: 50 locations across 10 major metros

Focus Areas:
• Operational playbook refinement
• Dasher training (pizza handling)
• Quality assurance monitoring
• Promotional launch coordination

Key Metrics:
• 95% uptime for ordering
• Average delivery time <35 min
• Order accuracy >98%
```

**Phase 3: National Launch (Weeks 7-10)**
```
Markets: All 500 locations

Launch Sequence:
Week 7: Top 25 metros (300 locations)
Week 8: Secondary metros (150 locations)
Week 9: Remaining markets (50 locations)
Week 10: Optimization & refinement
```

**Three-Sided Preparation:**

| Side | Preparation | Owner |
|------|-------------|-------|
| **Merchants** | POS integration, staff training, menu optimization | Account Managers |
| **Dashers** | Pizza-specific training (thermal bags, handling) | Dasher Operations |
| **Consumers** | Promotional launch ($0 delivery fee week), awareness | Marketing |

**Risk Mitigation:**
| Risk | Mitigation |
|------|------------|
| Volume surge crashes kitchen | Staged rollout + throttling |
| Pizza quality (cold/soggy) | Thermal bag mandate + training |
| Prep time variability | Dedicated ML model per location |
| Dasher supply shortage | Pre-positioning incentives |

---

### Example 5: New Vertical Expansion — Grocery Delivery Strategy

**Context:**
DoorDash expanding beyond restaurants into grocery (competing with Instacart). Need marketplace strategy for grocery logistics.

**Expert Response:**

**Grocery vs Restaurant Logistics Comparison:**

| Dimension | Restaurants | Grocery | Implication |
|-----------|-------------|---------|-------------|
| **Order Size** | 1-4 items, $25 avg | 15-50 items, $75 avg | Larger vehicles, longer shopping |
| **Prep Time** | 10-20 min (cook) | 30-60 min (shopping) | Different Dasher model |
| **Substitution** | Rare | Common (30%+ orders) | Real-time communication required |
| **Temperature** | Hot food | Frozen, cold, ambient | Multi-zone bags needed |
| **Weight** | <10 lbs | 20-50 lbs | Physical demands, car required |
| **Scheduling** | On-demand | Scheduled windows | Different demand patterns |

**Grocery Logistics Model:**

```
┌─────────────────────────────────────────────────────────────┐
│               GROCERY DELIVERY MODEL                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CONSUMER          STORE             DASHER                 │
│     │                │                 │                    │
│     │── Order ───────>│                 │                    │
│     │                │                 │                    │
│     │                │── Pick List ───>│                    │
│     │                │                 │                    │
│     │                │<─ Shopping ─────│                    │
│     │                │                 │                    │
│     │<─ Subs? ───────│                 │                    │
│     │── Approval ────>│                 │                    │
│     │                │                 │                    │
│     │                │<─ Checkout ─────│                    │
│     │                │                 │                    │
│     │<─ Delivery ──────────────────────│                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Dasher Model Adaptations:**

**Dedicated Grocery Dashers:**
- Larger vehicle requirement (SUV/minivan)
- Thermal equipment: insulated bags + cooler packs
- Shopping training: produce selection, expiration dates
- Higher base pay (longer time per order)

**Batched Shopping:**
```
Traditional: 1 order = 1 Dasher = 45 min shopping + 15 min delivery
Optimized:   2-3 orders = 1 Dasher = 60 min shopping + 20 min delivery
Efficiency gain: 30% more orders per Dasher hour
```

**Substitution Workflow:**
1. Item out of stock detected
2. ML suggests substitution (brand, size, type)
3. Real-time notification to customer
4. Customer approves/rejects via app
5. Dasher continues shopping

**Three-Sided Value Proposition:**

| Side | Value | DoorDash Differentiation |
|------|-------|--------------------------|
| **Consumers** | Convenience, time savings | Same-day delivery, restaurant + grocery in one app |
| **Merchants** | Digital channel, fulfillment | Existing Dasher network, lower delivery fees |
| **Dashers** | Higher earnings per order | Batch shopping, consistent demand |

**Key Metrics (Grocery):**
| Metric | Target | Why Different |
|--------|--------|---------------|
| Fulfillment accuracy | >98% | More items = higher error risk |
| Substitution rate | <15% | Inventory management partnership |
| Shopping time/item | <45 seconds | Dasher efficiency |
| Customer satisfaction | >4.5/5 | Higher expectations than restaurant |

---
