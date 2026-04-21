## 7. Standards & Reference

### 7.1 ML Pipeline Architecture

| Stage / 阶段 | Tools / 工具 | Key Validation
|-------------|-------------|--------------------------|
| **Data Ingestion** | Airflow, Spark, dbt | Schema validation, null rate < 1%, row count check |
| **Feature Engineering** | Feast, Tecton, Pandas | Point-in-time correctness, no future leakage, train-serve parity test |
| **Model Training** | XGBoost, LightGBM, PyTorch + MLflow | Reproducible seed, hyperparameter logged, artifact versioned |
| **Offline Evaluation** | scikit-learn, custom slicing | Beat production baseline by > 1% on primary metric; slice analysis by user segment |
| **Model Registry** | MLflow Registry, W&B Artifacts | Staging → Human review → Production transition with audit log |
| **Deployment** | BentoML, Triton, Kubernetes | Shadow mode → Canary 5% → Canary 20% → Full traffic |
| **Monitoring** | Evidently, Whylogs, Prometheus | PSI drift, prediction distribution, business KPI alignment |

### 7.2 Model Serving Patterns

| Pattern / 模式 | Latency / 延迟 | When to Use / 使用场景 | Caution
|---------------|--------------|----------------------|---------------|
| **Real-time API** | p99 < 50ms | Fraud detection, search ranking, recommendations | Feature freshness critical; monitor feature staleness |
| **Batch Scoring** | Hours | Churn prediction, lead scoring, risk assessment | Ensure no label leakage in batch; version output dataset |
| **A/B Test** | Same as production | Model comparison, feature experiments | User-level splitting; define guardrail metrics before launch |
| **Canary Deployment** | Same as production | Gradual traffic shift for new model | Auto-rollback if error rate > 1% or latency p99 > 2× baseline |
| **Shadow Mode** | Adds ~5ms overhead | Pre-production validation; compare predictions offline | Log both model outputs; do not use shadow model predictions in production |

### 7.3 ML Metrics & Thresholds

| Metric / 指标 | Formula / 公式 | Target
|--------------|--------------|---------------|
| **Real-time Prediction Latency** | p99 of end-to-end inference (feature fetch + model + post-process) | p99 < 50ms for real-time serving |
| **Feature Freshness** | Current time − feature computation timestamp | Staleness alert if features > 4h old for real-time model |
| **Data Drift (PSI)** | Σ (P_i − Q_i) × ln(P_i
| **Offline-Online Metric Alignment** | Pearson correlation of offline metric trend vs. online KPI trend | Must move in same direction; negative correlation = wrong proxy metric |
| **Model Recall/Precision** | Per use case; fraud recall > 90%, precision > 80% | Define thresholds per business requirement before training begins |
| **Training Pipeline Success Rate** | Successful runs

### 7.4 MLOps Maturity Levels

| Level / 等级 | Description / 描述 | Characteristics
|-------------|-------------------|----------------------|
| **Level 0: Manual** | Data scientists run notebooks; models deployed ad-hoc | No versioning, no monitoring, months to retrain |
| **Level 1: Pipeline Automation** | Automated training pipeline; model registry | CI/CD for ML code; manual deployment trigger; basic monitoring |
| **Level 2: Full MLOps** | Automated retraining on drift; self-healing pipelines | Drift-triggered retraining; canary deployment; SLO-based alerts |

---
