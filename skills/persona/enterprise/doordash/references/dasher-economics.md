# Dasher Economics & Supply — Reference

## Overview

Dashers are independent contractors who form the supply side of DoorDash's three-sided marketplace. With 8 million Dashers earning $18+ billion annually, the Dasher network is critical to platform success.

---

## Dasher Demographics

### Scale
| Metric | Value |
|--------|-------|
| Total Dashers (2024) | 8 million |
| Active monthly | ~2-3 million |
| Dasher earnings (2024) | $18+ billion |
| Average per Dasher | ~$2,250/year |

### Profile
| Attribute | Distribution |
|-----------|--------------|
| **Work Pattern** | 80% part-time, 20% full-time |
| **Vehicle Type** | 85% car, 10% bike, 5% scooter |
| **Age Range** | 18-55 (median ~30) |
| **Gender** | Mixed (varies by market) |
| **Primary Motivation** | Supplemental income (60%), Primary income (25%), Goals (15%) |

---

## Earnings Structure

### Pay Components

```
Total Earnings = Base Pay + Promotions + Tips
```

| Component | Description | Typical Range |
|-----------|-------------|---------------|
| **Base Pay** | Time + Distance + Desirability | $2-10 per order |
| **Peak Pay** | Bonus during high demand | +$1-5 per order |
| **Challenges** | Complete X orders, earn $Y | Variable |
| **Tips** | 100% to Dasher | $2-8 average |
| **Hotspots** | Bonus for waiting in zone | Variable |

### Base Pay Formula

```python
base_pay = (
    time_component +           # Time expected for delivery
    distance_component +       # Miles traveled
    desirability_adjustment    # Unpopular orders get boost
)
```

### Average Earnings

| Metric | Value |
|--------|-------|
| Hourly rate (active time) | $20-25/hour |
| Hourly rate (total time) | $15-20/hour |
| Per delivery | $8-15 |
| Weekly (active Dashers) | $200-800 |
| Annual (median) | $2,000-5,000 |
| Annual (top 10%) | $15,000-30,000 |

---

## Dasher Rewards Program

### Tier Structure

| Tier | Requirements | Benefits |
|------|--------------|----------|
| **New** | First delivery | Basic access |
| **Silver** | 100+ deliveries, 4.7+ rating | Priority support |
| **Gold** | 500+ deliveries, 4.8+ rating | High-value orders, scheduling priority |
| **Platinum** | 1000+ deliveries, 4.9+ rating | Premium support, exclusive perks |

### Rewards Benefits
- **Priority Dispatch**: Higher-rated Dashers see offers first
- **High-Value Orders**: Access to large/catering orders
- **Scheduling**: Early access to time slots
- **Support**: Dedicated support lines
- **Perks**: Gas discounts, phone plans, insurance

---

## Supply Management

### Supply-Demand Balancing

```
┌─────────────────────────────────────────────────────────┐
│              SUPPLY-DEMAND BALANCING                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  High Demand / Low Supply                               │
│  └── Peak Pay (+$X/order)                               │
│  └── Hotspot Zones                                      │
│  └── Challenges ("Complete 3, earn $15")                │
│  └── Extended Delivery Radius                           │
│                                                         │
│  Low Demand / High Supply                               │
│  └── Scheduling Controls                                │
│  └── New Dasher Waitlists                               │
│  └── Reduced Peak Pay                                   │
│                                                         │
│  Optimal Balance                                        │
│  └── Standard Pay Structure                             │
│  └── Normal Dispatch Radius                             │
│  └── Balanced Batching                                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Dynamic Incentives

| Incentive Type | Trigger | Effect |
|----------------|---------|--------|
| **Peak Pay** | High demand periods | +$1-5/order |
| **Hotspots** | Low supply zones | Extra $ for waiting |
| **Challenges** | Specific goals | One-time bonuses |
| **Scheduled Shifts** | Predictable demand | Guaranteed minimums |

---

## Dasher Experience

### Onboarding Process
1. Sign up online or via app
2. Background check (3-7 days)
3. Identity verification
4. Orientation (online)
5. First delivery (often with guidance)

### Active Dashing

**Dash Process:**
```
1. Log in → Check for available time slots or "Dash Now"
2. Accept order → Navigate to restaurant
3. Pickup → Confirm items, communicate delays
4. Delivery → Navigate to customer, handoff
5. Complete → Rate experience, get paid
```

**Key Features:**
- **Dash Now**: Immediate availability (if supply needed)
- **Schedule**: Book time slots in advance
- **Pause**: Temporary break without ending shift
- **Decline**: No penalty for rejecting orders (within limits)

### Dasher App Features

| Feature | Purpose |
|---------|---------|
| Real-time earnings | Track income |
| Navigation | Turn-by-turn directions |
| Order details | Items, instructions, customer info |
| Communication | Text/call customer/restaurant |
| Support | Help with issues |
| Hotspots | High-demand zones |
| Challenges | Active promotions |

---

## Retention & Engagement

### Retention Metrics

| Metric | Target | Description |
|--------|--------|-------------|
| 30-day retention | >70% | Still active after 30 days |
| 90-day retention | >50% | Still active after 90 days |
| Annual retention | >30% | Active for full year |
| Session frequency | 3-5x/week | Regular engagement |

### Retention Drivers

| Factor | Impact | Strategy |
|--------|--------|----------|
| Earnings | High | Ensure competitive pay |
| Flexibility | High | Maintain schedule control |
| App experience | Medium | Smooth, reliable app |
| Support | Medium | Fast issue resolution |
| Safety | High | Insurance, safety features |
| Community | Low | Dasher forums, events |

### Churn Reasons

| Reason | Percentage | Mitigation |
|--------|------------|------------|
| Insufficient earnings | 35% | Peak pay, challenges |
| Better opportunities | 25% | Competitive pay, perks |
| App/technical issues | 15% | Reliability improvements |
| Customer issues | 15% | Support, deactivation policies |
| Personal reasons | 10% | — |

---

## Safety & Support

### Safety Features

| Feature | Description |
|---------|-------------|
| **SafeDash** | Emergency button, ADT monitoring |
| **Real-time tracking** | Share location with trusted contacts |
| **No-contact delivery** | Minimize physical interactions |
| **Insurance** | Occupational accident insurance |
| **Deactivation appeals** | Fair process for disputes |

### Support Channels

| Channel | Response Time | Use Case |
|---------|---------------|----------|
| In-app chat | <2 min | Quick issues |
| Phone support | <5 min | Urgent issues |
| Email | 24 hours | Non-urgent |
| Dasher Help Center | Self-serve | FAQs, guides |

---

## Regulatory Environment

### Gig Worker Classification

| Issue | Status | Impact |
|-------|--------|--------|
| **AB5 (California)** | Prop 22 passed | Maintained contractor status with benefits |
| **EU regulations** | Evolving | Potential reclassification risks |
| **Minimum wage** | Various laws | Pay floor requirements |
| **Benefits** | Emerging | Health stipends, insurance |

### Prop 22 (California)

**Key Provisions:**
- Dashers remain independent contractors
- 120% minimum wage for active time
- Healthcare stipend
- Insurance coverage
- Expense reimbursement

---

## Optimization Strategies

### For DoorDash
1. **Match supply to demand** — Use forecasting and incentives
2. **Improve Dasher earnings** — Optimize batching, reduce wait times
3. **Enhance experience** — App reliability, support quality
4. **Build community** — Recognition, perks, communication
5. **Ensure safety** — Insurance, support, features

### For Dashers (Best Practices)
1. **Know your market** — Peak times, hotspots, restaurant speeds
2. **Be selective** — Decline low-value orders
3. **Batch strategically** — Accept batched orders when efficient
4. **Provide great service** — Higher ratings = better offers
5. **Track expenses** — Mileage, maintenance for taxes

---

## Key Metrics Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│                DASHER HEALTH DASHBOARD                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Supply Metrics                                             │
│  ├── Active Dashers: 2.4M (monthly)                        │
│  ├── New Signups: 150K (monthly)                           │
│  └── Retention (30d): 72%                                   │
│                                                             │
│  Earnings Metrics                                           │
│  ├── Avg Hourly: $22.50                                     │
│  ├── Total Paid (MTD): $1.5B                                │
│  └── Peak Pay Distributed: $45M                             │
│                                                             │
│  Experience Metrics                                         │
│  ├── Avg Rating: 4.85                                       │
│  ├── Completion Rate: 96%                                   │
│  └── On-Time Rate: 94%                                      │
│                                                             │
│  Engagement Metrics                                         │
│  ├── Sessions/Dasher/Week: 4.2                              │
│  ├── Avg Session Length: 3.5 hours                          │
│  └── Decline Rate: 18%                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

*Source: DoorDash Dasher Portal, Earnings Reports, Regulatory Filings*
