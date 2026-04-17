## § 4 · Core Philosophy

### 4.1 Data Science Mental Model

```
          ┌─────────────────────────────┐
          │     Business Impact Layer    │  ← Revenue, retention, cost reduction
        ┌─┴─────────────────────────────┴─┐
        │   Online Metrics & Experiments  │  ← A/B tests, canary rollouts, SLOs
      ┌─┴─────────────────────────────────┴─┐
      │     Model Quality & Evaluation      │  ← AUC, RMSE, NDCG, calibration
    ┌─┴───────────────────────────────────────┴─┐
    │         Feature Engineering Layer          │  ← Leakage-free, reproducible
  ┌─┴─────────────────────────────────────────────┴─┐
  │        Data Quality & Observability Foundation   │  ← Schema, freshness, drift
  └─────────────────────────────────────────────────┘
```

Build bottom-up: you cannot trust model quality without clean features; you cannot interpret online metrics without a properly powered experiment.

### 4.2 Guiding Principles

1. **Baseline before complexity**: Every ML project starts with the dumbest possible model. If majority-class prediction captures 80% of the business value, complex models must justify their maintenance cost, inference latency, and explainability burden.

2. **Metric alignment is the hardest problem**: Optimizing the wrong metric — AUC when the business cares about revenue per user, RMSE when extreme errors cost 100× more — produces models that ace offline eval and fail in production A/B tests. Define the metric before touching data.

3. **Models decay, monitoring is mandatory**: No model is static. Data distributions shift, user behavior evolves, upstream data pipelines break silently. Every model in production must have drift detection, performance alerting, and a documented retraining playbook before go-live.

---

