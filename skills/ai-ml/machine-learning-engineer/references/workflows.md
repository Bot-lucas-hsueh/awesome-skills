## 8. Standard Workflow

### 8.1 Phase 1: Problem Framing & Data

```
Phase 1: Problem Framing & Data (Week 1)
├── Business metric to ML metric translation
│   ├── Define primary business KPI (e.g., "reduce fraud loss by 20%")
│   ├── Map to measurable ML metric (e.g., recall@precision=0.9)
│   └── [✓ Done]: Both metrics logged; stakeholder agreement on success threshold
│       [✗ FAIL]: "Improve model accuracy" without business target → stop, demand KPI
├── Data audit
│   ├── Profile dataset: row count, null rates, class imbalance, date range
│   ├── Check for label leakage: ensure no future information in features
│   ├── Validate point-in-time correctness in historical data joins
│   └── [✓ Done]: Great Expectations suite passes; leakage tests clean
│       [✗ FAIL]: Null rate > 10% in key features → investigate upstream pipeline first
├── Baseline model
│   ├── Implement rule-based baseline: if no rules exist, use frequency/average baseline
│   ├── Train simple model (logistic regression
│   └── [✓ Done]: Baseline AUC
│       [✗ FAIL]: Simple model already exceeds target → reconsider if complex ML needed
```

### 8.2 Phase 2: Feature Engineering & Model Development

```
Phase 2: Feature Engineering & Model Development (Week 2–3)
├── Feature pipeline
│   ├── Define features in Feast/Tecton feature definitions (not ad-hoc code)
│   ├── Test: run same feature computation on training data and a live request
│   ├── Verify output is bit-for-bit identical (train-serve parity test)
│   └── [✓ Done]: Parity test passes; feature definitions version-controlled in git
│       [✗ FAIL]: Any difference in train vs. serve feature values → STOP, fix before training
├── Model training
│   ├── Start with XGBoost/LightGBM on tabular data; log all runs to MLflow
│   ├── Hyperparameter search with Optuna (50–200 trials); cross-validate with time-based splits
│   ├── Slice analysis: check performance on minority groups, recent data, edge cases
│   └── [✓ Done]: Best model logged; outperforms baseline by > 1% on primary metric
│       [✗ FAIL]: Model fails slice analysis for regulated segments → bias review required
├── Production parity test
│   ├── Replay last 7 days of live traffic through new model using logged features
│   ├── Compare prediction distribution to current production model
│   └── [✓ Done]: Prediction distributions match expected shift; no anomalies
│       [✗ FAIL]: Extreme distribution difference → investigate feature or code issue
```

### 8.3 Phase 3: Deployment & Monitoring

```
Phase 3: Deployment & Monitoring (Week 4)
├── Shadow mode deployment (Days 1–7)
│   ├── Route 100% of traffic through new model in parallel (predictions not served)
│   ├── Log all predictions; compare to production model outputs
│   ├── Measure latency overhead (must be < 10ms additional overhead)
│   └── [✓ Done]: Shadow predictions within expected range; p99 latency acceptable
│       [✗ FAIL]: Shadow model crashes or produces NaN predictions → STOP, debug
├── Canary deployment (Days 8–14)
│   ├── Route 5% of traffic to new model (predictions served to users)
│   ├── Monitor: error rate, latency p99, primary business KPI
│   ├── Define auto-rollback trigger: error rate > 1% OR latency p99 > 100ms
│   ├── Expand to 20% if 48h stable; expand to 100% if 7-day A/B result positive
│   └── [✓ Done]: Primary KPI improved or neutral; guardrails not breached
│       [✗ FAIL]: Auto-rollback triggered → post-mortem before next attempt
├── Drift alerting (Ongoing)
│   ├── Configure Evidently: PSI > 0.25 on any input feature → PagerDuty alert
│   ├── Configure AUC trend alert: > 5% degradation over 7-day window → retrain trigger
│   ├── Feature staleness alert: any feature > 4h without update → on-call alert
│   └── [✓ Done]: All alerts firing in staging environment; runbook written
│       [✗ FAIL]: Alert not tested in staging → treat monitoring as undeployed
```

---
