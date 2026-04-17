## § 4 · Core Philosophy

### 4.1 The ML Lifecycle Stack

```
        ┌──────────────────────────────────────────┐
        │   MONITORING & RETRAINING                │  Drift · Degradation · Auto-retrain
        │   (keep the model fresh)                 │
      ┌─┴──────────────────────────────────────────┴─┐
      │   SERVING & INFERENCE                        │  Triton · Ray Serve · TensorRT
      │   (deliver predictions at SLA)              │
    ┌─┴──────────────────────────────────────────────┴─┐
    │   ORCHESTRATION & CI/CD                          │  Kubeflow · Airflow · Prefect
    │   (automate reproducible pipelines)             │
  ┌─┴──────────────────────────────────────────────────┴─┐
  │   MODEL TRAINING                                      │  PyTorch · TF · MLflow · Optuna
  │   (efficient, reproducible experiments)             │
┌─┴──────────────────────────────────────────────────────┴─┐
│   FEATURE ENGINEERING & FEATURE STORE                     │  Spark · Flink · Feast · Tecton
│   (the foundation; garbage in = garbage out)            │
└──────────────────────────────────────────────────────────┘
```

Each layer depends on the layer below it. A fast serving stack cannot compensate for stale or leaky features. Invest in lower layers first.

### 4.2 Guiding Principles

1. **Feature Parity is Non-Negotiable**: The exact same feature computation code must run in training and serving — use a shared library, never duplicate logic

2. **Experiment Everything, Ship Nothing Untested**: Every model change — architecture, hyperparameter, preprocessing — is an experiment tracked in MLflow with a before/after metric comparison

3. **Monitoring is Part of the Model**: Drift detection, performance tracking, and retraining triggers are designed alongside the model, not retrofitted after incidents

---

