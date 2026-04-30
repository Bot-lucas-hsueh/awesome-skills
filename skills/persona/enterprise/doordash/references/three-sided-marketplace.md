# Three-Sided Marketplace — Deep Dive Reference

## Overview

DoorDash operates a three-sided marketplace that must balance the needs of:
1. **Consumers** — People ordering food and goods
2. **Merchants** — Restaurants, grocery stores, and retailers
3. **Dashers** — Independent delivery drivers

```
┌─────────────────────────────────────────────────────────────┐
│              THREE-SIDED MARKETPLACE DYNAMICS               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    ┌───────────────┐                        │
│                    │   CONSUMERS   │                        │
│                    │  (42M+ MAUs)  │                        │
│                    └───────┬───────┘                        │
│                            │ Orders                         │
│                            ▼                                │
│              ┌─────────────────────────┐                    │
│              │   DOORDASH PLATFORM     │                    │
│              │  (Technology + Logistics)│                   │
│              │     $80B+ GOV          │                     │
│              └───────────┬─────────────┘                    │
│                          │                                  │
│         ┌────────────────┼────────────────┐                 │
│         │                │                │                 │
│         ▼                │                ▼                 │
│  ┌─────────────┐         │         ┌─────────────┐          │
│  │  MERCHANTS  │         │         │   DASHERS   │          │
│  │ (600K+      │◄────────┴────────►│  (8M+       │          │
│  │  stores)    │    Fulfillment    │  drivers)   │          │
│  └─────────────┘                   └─────────────┘          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Side 1: Consumers

### Value Proposition
- **Convenience**: Order from anywhere, anytime
- **Selection**: 600,000+ merchants
- **Speed**: Sub-30-minute delivery target
- **Reliability**: >95% on-time performance
- **Affordability**: DashPass subscription reduces costs

### Key Metrics
| Metric | Value | Target |
|--------|-------|--------|
| Monthly Active Users | 42+ million | Growth |
| DashPass Subscribers | 26+ million | Retention |
| Average Order Value | $35-40 | Increase |
| Order Frequency | 4.6x/month | Increase |
| NPS Score | 50-60 | >60 |

### Consumer Segments
1. **DashPass Members** (26M+) — High-frequency, loyal users
2. **Occasional Users** — Event-driven ordering
3. **New Verticals Users** — Grocery, convenience, retail
4. **Corporate/Group Orders** — DoorDash for Work

---

## Side 2: Merchants

### Value Proposition
- **Revenue Growth**: Incremental sales channel
- **Customer Acquisition**: Access to 42M+ consumers
- **Marketing Reach**: Promoted listings, advertising
- **Operational Efficiency**: Delivery without fleet investment
- **Data & Insights**: Consumer behavior analytics

### Merchant Types

| Type | Examples | Key Needs |
|------|----------|-----------|
| **National Chains** | McDonald's, Chipotle, Starbucks | Reliability, scale, integration |
| **Regional Chains** | Local favorites | Growth, marketing |
| **Independent** | Mom & pop restaurants | Simplicity, support |
| **Grocery** | Safeway, ALDI, Sprouts | Fulfillment, substitutions |
| **Convenience** | 7-Eleven, CVS | Speed, availability |
| **Retail** | PetSmart, Sephora | Brand experience |

### Merchant Revenue Impact
- Average incremental revenue: 20-30%
- Top 100 US restaurants: 94% partnered with DoorDash
- New merchant acquisition: 100,000+ annually

---

## Side 3: Dashers

### Value Proposition
- **Flexible Earnings**: Work when, where, how much
- **Accessibility**: Low barrier to entry
- **Transparency**: Clear pay structure upfront
- **Safety**: Insurance, support, safety features
- **Incentives**: Peak pay, challenges, rewards

### Dasher Economics

| Component | Description |
|-----------|-------------|
| **Base Pay** | Time + distance + desirability |
| **Promotions** | Peak pay, challenges, hotspots |
| **Tips** | 100% to Dasher |
| **Total Earnings (2024)** | $18+ billion |
| **Active Dashers** | 8 million |
| **Avg Earnings/Dasher** | ~$2,250/year |

### Dasher Segments
1. **Full-time** — Primary income source
2. **Part-time** — Supplemental income
3. **Goal-oriented** — Saving for specific purpose
4. **Flexible** — Between jobs, students

---

## Marketplace Dynamics

### Network Effects

```
Positive Feedback Loops:

More Consumers → More Orders → More Dasher Earnings
      ↑                                    ↓
      └──────── Better Selection ←─────────┘

More Merchants → More Selection → More Consumers
      ↑                                    ↓
      └────── More Orders/Dasher Pay ←─────┘

More Dashers → Faster Delivery → Better Consumer Experience
      ↑                                      ↓
      └──────── More Orders → More Merchant Revenue
```

### Balancing Act

Every decision impacts all three sides:

| Decision | Consumers | Merchants | Dashers |
|----------|-----------|-----------|---------|
| Increase delivery fees | Negative | Neutral | Neutral |
| Add peak pay | Neutral | Positive | Positive |
| Batch orders | Neutral | Positive | Positive |
| Reduce ETAs | Positive | Positive | Negative (pressure) |
| Promote new merchants | Positive (selection) | Positive | Positive (orders) |

---

## Optimization Framework

### Consumer Optimization
- Minimize ETA while maintaining accuracy
- Maximize selection and availability
- Optimize discovery and recommendations
- Reduce friction in ordering process

### Merchant Optimization
- Maximize order volume and GMV growth
- Minimize order errors and cancellations
- Optimize prep time predictions
- Provide marketing and promotional tools

### Dasher Optimization
- Maximize earnings per hour
- Minimize wait times at restaurants
- Optimize batching for efficiency
- Provide flexibility and transparency

### Platform Optimization
The goal is to maximize **Marketplace GOV** while improving **contribution margin**:

```
Contribution Profit = 
    (Commission Revenue + Delivery Fees + Service Fees + Advertising)
    -
    (Dasher Costs + Payment Processing + Support + Refunds)
```

---

## Key Challenges

### 1. Supply-Demand Balance
- **Problem**: Too few Dashers = long ETAs; Too many = idle time
- **Solution**: Dynamic pricing, incentives, forecasting

### 2. Quality Consistency
- **Problem**: Variable restaurant prep times, Dasher performance
- **Solution**: ML prediction, ratings, training

### 3. Geographic Coverage
- **Problem**: Rural/suburban areas have lower density
- **Solution**: Zone optimization, scheduled orders

### 4. Peak Time Management
- **Problem**: Lunch/dinner rushes overwhelm capacity
- **Solution**: Pre-positioning, surge pricing, batching

### 5. International Complexity
- **Problem**: Different regulations, cultures, preferences
- **Solution**: Wolt/Deliveroo local expertise, adaptation

---

## Success Metrics by Side

### Consumer Health
- MAU growth
- Order frequency
- NPS score
- Retention rate
- DashPass subscription rate

### Merchant Health
- GMV growth per merchant
- Order volume growth
- Merchant satisfaction
- Retention rate
- NPS score

### Dasher Health
- Active Dasher growth
- Earnings per hour
- Retention rate
- Satisfaction scores
- Safety incidents

### Platform Health
- Marketplace GOV growth
- Contribution margin
- On-time delivery %
- Customer service contacts
- Overall NPS

---

*Reference: DoorDash S-1, Investor Presentations, Earnings Calls*
