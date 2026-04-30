## § 8 · Scenario Examples

### Example 1: Customer Churn Prediction

**Context**: Predict which customers will cancel subscription.

**Approach**:
```
Data: 2 years of user behavior, demographics, support tickets

Features:
├── Engagement (logins, sessions, features used)
├── Financial (payment delays, plan changes)
├── Support (ticket volume, sentiment)
└── Temporal (tenure, seasonality)

Model: Gradient Boosting (XGBoost)
├── AUC-ROC: 0.87
├── Precision@10%: 0.72
└── Top factors: Days since login, support tickets

Action:
├── Intervention campaign for high-risk users
├── Early warning dashboard for customer success
```

---

### Example 2: A/B Test Analysis

**Context**: Test new checkout flow conversion rate.

**Design**:
```
Setup:
├── Metric: Purchase conversion rate
├── Allocation: 50/50 (control/treatment)
├── Duration: 2 weeks (2 business cycles)
├── Sample: 100K users per variant

Analysis:
├── Control: 12.3% conversion
├── Treatment: 13.1% conversion
├── Lift: +6.5% relative
├── p-value: 0.003 (significant)
├── 95% CI: [+2.1%, +10.9%]

Decision: Roll out new checkout flow
```

---

### Example 3: Price Elasticity Analysis

**Context**: Understand how price changes affect demand.

**Method**:
```
Data: Historical sales with price variations

Approach:
├── Natural experiment: competitor price changes
├── Instrumental variables for causality
├── Log-log regression for elasticity

Results:
├── Price elasticity: -1.8 (elastic)
├── 10% price increase → 18% demand decrease
├── Optimal price point: $X (profit-maximizing)

Recommendation: Lower prices to increase volume
```

---

### Example 4: Cohort Retention Analysis

**Context**: Understand user retention patterns by acquisition cohort.

**Analysis**:
```
Cohorts:
├── Group users by signup month
├── Track retention over time
├── Compare across acquisition channels

Findings:
├── Organic: 40% Month-12 retention
├── Paid: 25% Month-12 retention
├── Mobile app: 15% higher retention than web

Action:
├── Increase organic acquisition investment
├── Improve mobile onboarding
```

---

### Example 5: Fraud Detection Model

**Context**: Real-time transaction fraud detection.

**Solution**:
```
Features:
├── Transaction amount, velocity
├── Device fingerprint, location
├── Historical behavior patterns
├── Network features (linked accounts)

Model: Ensemble (XGBoost + Neural Network)
├── Precision: 95% at 80% recall
├── False positive rate: 2%
└── Latency: < 50ms

Deployment:
├── Real-time scoring API
├── Human review queue for borderline cases
├── Model retraining monthly
```

---
