## § 4 · Core Philosophy

### 4.1 MLOps Architecture

```
┌─────────────────────────────────────────┐
│         Model Serving                   │  ← KServe, REST/gRPC APIs
├─────────────────────────────────────────┤
│         Model Registry                  │  ← MLflow Model Registry
├─────────────────────────────────────────┤
│         Feature Store                   │  ← Feast, online/offline store
├─────────────────────────────────────────┤
│         Training Pipeline               │  ← Kubeflow, Airflow
├─────────────────────────────────────────┤
│         Experiment Tracking             │  ← MLflow, W&B
├─────────────────────────────────────────┤
│         Data Versioning                 │  ← DVC, LakeFS
└─────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Version Everything** — Code, data, models, configurations
2. **Automate Everything** — Training, testing, deployment
3. **Monitor Everything** — Data, model, business metrics
4. **Test ML Systems** — Model quality, not just code
5. **Enable Collaboration** — Centralized tracking, clear lineage

---
