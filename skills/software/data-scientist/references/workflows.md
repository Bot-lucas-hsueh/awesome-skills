## 8. Standard Workflow

### 8.1 ML Model Development Lifecycle

```
Phase 1: Problem Framing & Data (Day 1-3)
├── Define business objective: what decision will this model drive?
├── Translate to ML task: classification / regression / ranking
├── Define success metric BEFORE seeing data (AUC-ROC, NDCG, MAPE)
├── Data audit: volume, label quality, class distribution, temporal coverage
├── EDA: target distribution, missing value patterns, feature correlations
├── Baseline model: majority class / mean
└── [✓ Done]: Baseline AUC/RMSE established; data quality issues documented; team
            aligned on success metric and minimum detectable business impact
    [✗ FAIL]: No agreed success metric → STOP, align with business stakeholder first
              before any feature engineering or modeling

Phase 2: Feature Engineering & Modeling (Day 4-10)
├── Temporal split: train / validation
├── Feature creation: lag features, rolling aggregations, encodings, embeddings
├── Feature validation: Great Expectations schema check on each feature
├── Model progression: Logistic Regression → LightGBM → Hyperparameter tuning
├── Cross-validation: StratifiedKFold for classification, TimeSeriesSplit for temporal
├── Hyperparameter optimization: Optuna with 100+ trials on validation set
├── Error analysis: where does the model fail? Which segments underperform?
├── SHAP analysis: global feature importance + individual prediction explanations
└── [✓ Done]: Model beats baseline by >10% on primary metric; no leakage confirmed
            via temporal holdout; SHAP summary prepared for stakeholder review
    [✗ FAIL]: Validation metric < baseline + 5% → investigate leakage, add features,
              or escalate to DL; do NOT proceed to deployment with marginal gains

Phase 3: Production & Monitoring (Day 11-15)
├── MLflow: log all parameters, metrics, artifacts; register champion model
├── Shadow deployment: run new model alongside current; compare outputs for 48h
├── A/B test launch: 10% traffic canary → verify SRM → expand to 50% → 100%
├── Drift monitoring: PSI alert > 0.2 on top-10 features; daily scheduled check
├── Performance monitoring: rolling 7-day AUC
├── Retraining playbook: trigger conditions, data window, validation gate, rollback
└── [✓ Done]: A/B test shows statistically significant lift (p < 0.05, power > 80%);
            drift monitoring active; retraining pipeline tested end-to-end
    [✗ FAIL]: A/B test shows null result or negative metric → roll back; investigate
              offline/online metric gap before next iteration
```

---
