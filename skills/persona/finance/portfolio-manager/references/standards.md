## § 7 · Standards & Reference

### 7.1 Mean-Variance Optimization

```
Objective: Maximize Sharpe Ratio

Maximize: (E[Rp] - Rf) / σp

Subject to:
- Sum of weights = 1
- Individual weight constraints (min/max)
- Group constraints (asset class targets)
- Tracking error constraint (if applicable)
```

### 7.2 Performance Attribution

| Attribution Component | Formula | Interpretation |
|----------------------|---------|----------------|
| **Allocation Effect** | (wi - Wi) × (Bi - B) | Value from overweighting outperforming segments |
| **Selection Effect** | wi × (Ri - Bi) | Value from security selection within segments |
| **Currency Effect** | (1+Ri)(1+Ci) - (1+Ri) | Return from currency movements |

### 7.3 Rebalancing Strategies

| Strategy | Trigger | Pros | Cons |
|----------|---------|------|------|
| **Calendar** | Fixed dates (quarterly/annual) | Simple, predictable | May rebalance unnecessarily |
| **Threshold** | Drift > X% from target | Efficient, risk-focused | More complex to monitor |
| **Range** | Band around target | Allows small deviations | Requires band calibration |

---
