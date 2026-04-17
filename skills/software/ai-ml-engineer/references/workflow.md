## § 8 · Standard Workflow

### 8.1 Feature Store Setup & Onboarding

```
Phase 1: Infrastructure Setup (Week 1)
├── Deploy Feast registry (Redis online store + S3/GCS offline store)
├── Configure Feast feature_store.yaml: provider, registry path, online store
├── Set up offline store connector (BigQuery or Parquet on S3)
└── Deliverable: Feast deployed; feature_store.yaml committed to repo

Phase 2: Feature Definition (Week 2)
├── Define Entity (user_id, item_id) in entities.py
├── Define FeatureView per domain (user_features, item_features, context_features)
├── Set TTL per feature view (user activity: 7 days; item stats: 1 day)
└── Deliverable: feature_views.py with documented schemas and data sources

Phase 3: Backfill & Validation (Week 3)
├── Run feast materialize for offline backfill (last 90 days)
├── Validate point-in-time joins: compare feast.get_historical_features() output
│   vs. manual SQL join; diff should be < 0.01% on sampled rows
├── Load test online store: feast get_online_features() at target QPS (e.g., 5K QPS)
└── Deliverable: Backfill complete; latency P99 < 20ms for online fetch

Phase 4: Skew Monitoring (Week 4)
├── Log 1% sample of online feature vectors to S3
├── Configure daily Spark job to compare online samples vs. offline store distributions
├── Set KS-test alert: p-value < 0.05 → PagerDuty alert to ML platform on-call
└── Deliverable: Skew monitoring dashboard live; runbook for alert response
```

### 8.2 Model Training & Experiment Workflow

```
Pre-Training Checklist:
□ Feature data profiled: null rate < 1%, no constant features, no target leakage
□ Train/val/test split is time-based (not random) for time-series data
□ Baseline model logged in MLflow (e.g., LightGBM with default params as reference)
□ MLflow experiment created with consistent naming: {team}/{model_name}/{date}

Training:
□ DataLoader configured: num_workers=4, pin_memory=True, prefetch_factor=2
□ Mixed precision enabled: torch.amp.autocast(device_type='cuda') + GradScaler
□ Gradient accumulation set: effective_batch_size = batch_size × accumulation_steps
□ MLflow autolog enabled: mlflow.pytorch.autolog() or mlflow.sklearn.autolog()
□ Hyperparameter sweep: Optuna study with TPE sampler, n_trials=100, n_jobs=4

Post-Training Evaluation:
□ Offline metrics vs. baseline: must exceed by ≥ 5% (relative) on held-out test set
□ Latency profiling: measure P50/P95/P99 on target serving hardware
□ Slice-based evaluation: break down metrics by key segments (geography, user cohort)
□ Fairness check: metric disparity across demographic groups < 3% absolute
□ Model registered in MLflow registry with tags: {feature_version, dataset_date, metrics}
```

---

