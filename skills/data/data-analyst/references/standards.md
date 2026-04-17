## § 7 · Standards & Reference

### SQL Window Functions Reference

```sql
-- Running total
SUM(revenue) OVER (PARTITION BY user_id ORDER BY date) AS running_revenue

-- Lag/Lead for period comparison
revenue - LAG(revenue, 1) OVER (ORDER BY date) AS revenue_delta

-- Rank within group
RANK() OVER (PARTITION BY country ORDER BY revenue DESC) AS country_rank

-- N-day retention (cohort)
COUNT(DISTINCT CASE WHEN activity_date = cohort_date + INTERVAL '7 days'
      THEN user_id END) * 1.0 /
COUNT(DISTINCT user_id) AS day7_retention
```

### A/B Test Sample Size Calculator

```python
from scipy import stats
import numpy as np

def sample_size(baseline_rate, mde, alpha=0.05, power=0.80):
    """
    Calculate required sample size per variant.
    baseline_rate: Control conversion rate (e.g., 0.10 for 10%)
    mde: Minimum detectable effect as relative lift (e.g., 0.10 for 10% lift)
    alpha: Significance level (default 0.05)
    power: Statistical power (default 0.80)
    """
    treatment_rate = baseline_rate * (1 + mde)
    pooled_rate = (baseline_rate + treatment_rate)

    z_alpha = stats.norm.ppf(1 - alpha
    z_beta = stats.norm.ppf(power)

    n = (2 * pooled_rate * (1 - pooled_rate) * (z_alpha + z_beta) ** 2)
        (baseline_rate - treatment_rate) ** 2

    return int(np.ceil(n))

# Example: 10% baseline, want to detect 10% lift, α=0.05, power=0.80
# n = sample_size(0.10, 0.10) → ~3,842 per variant
```

### Key SaaS Metrics Formulas

```python
# Monthly Recurring Revenue
MRR = sum(monthly_subscription_value_per_customer)

# Customer Acquisition Cost
CAC = total_sales_marketing_spend

# Lifetime Value (simple)
LTV = ARPU * gross_margin_pct * (1

# LTV:CAC (target ≥ 3:1)
ltv_cac_ratio = LTV

# Net Revenue Retention
NRR = (beginning_MRR + expansion_MRR - contraction_MRR - churned_MRR)

# Payback Period (months)
payback_months = CAC
```

---
