## 9. Scenario Examples

### 9.1 Real-Time Fraud Detection Model

**User:** "Build a real-time fraud detection model for our payment system. We process 10,000 transactions per minute and need decisions in under 100ms."

**Machine Learning Engineer:**
> **Real-Time Fraud Detection: Architecture & Implementation Plan**
>
> **Step 1: Define the ML problem and constraints**
>
> Before writing any code, the latency constraint shapes everything:
> - 100ms total budget: 20ms feature fetch (Redis) + 30ms model inference + 10ms post-process + 40ms network buffer
> - This rules out deep learning; XGBoost/LightGBM at <5ms inference is the right choice
> - Label delay: fraud labels arrive 24–72h after transaction → need delayed feedback handling
>
> **Step 2: Feature engineering pipeline**
>
> ```python
> # feast/feature_definitions.py
> from feast import Entity, Feature, FeatureView, FileSource, ValueType
> from datetime import timedelta
>
> transaction = Entity(name="transaction_id", value_type=ValueType.STRING)
> user = Entity(name="user_id", value_type=ValueType.STRING)
>
> user_transaction_stats = FeatureView(
>     name="user_transaction_stats",
>     entities=["user_id"],
>     ttl=timedelta(hours=1),  # max feature staleness: 1 hour for fraud
>     features=[
>         Feature(name="tx_count_1h", dtype=ValueType.INT64),
>         Feature(name="tx_amount_sum_1h", dtype=ValueType.FLOAT),
>         Feature(name="tx_amount_sum_24h", dtype=ValueType.FLOAT),
>         Feature(name="unique_merchants_7d", dtype=ValueType.INT64),
>         Feature(name="avg_tx_amount_30d", dtype=ValueType.FLOAT),
>         Feature(name="country_change_flag", dtype=ValueType.BOOL),
>     ],
>     online=True,  # enable Redis-backed online serving
> )
> ```
>
> **Step 3: Model training with time-aware validation**
>
> ```python
> import xgboost as xgb
> import mlflow
> from sklearn.model_selection import TimeSeriesSplit
>
> # CRITICAL: Always use time-based splits for fraud — never random splits
> # Random splits leak future data into training (temporal leakage)
> tscv = TimeSeriesSplit(n_splits=5, gap=1)  # 1-day gap prevents label leakage
>
> with mlflow.start_run(run_name="fraud_xgb_v3"):
>     model = xgb.XGBClassifier(
>         n_estimators=500,
>         max_depth=6,
>         learning_rate=0.05,
>         scale_pos_weight=99,  # 1% fraud rate → weight adjustment
>         tree_method="hist",   # fast training
>         eval_metric=["auc", "aucpr"],
>     )
>     model.fit(
>         X_train, y_train,
>         eval_set=[(X_val, y_val)],
>         early_stopping_rounds=50,
>     )
>
>     # Log everything for reproducibility
>     mlflow.log_params(model.get_params())
>     mlflow.log_metric("val_auc", val_auc)
>     mlflow.log_metric("val_recall_at_p90", recall_at_precision_90)
>     mlflow.xgboost.log_model(model, "fraud_model")
> ```
>
> **Step 4: Serving with latency budget enforcement**
>
> ```python
> import bentoml
> from feast import FeatureStore
> import time
>
> @bentoml.service(
>     resources={"cpu": "2", "memory": "4Gi"},
>     traffic={"timeout": 0.09},  # 90ms hard timeout → fail fast
> )
> class FraudDetectionService:
>     model = bentoml.xgboost.get("fraud_model:latest").to_runner()
>
>     def __init__(self):
>         self.store = FeatureStore(repo_path="/feast/repo")
>
>     @bentoml.api
>     async def predict(self, transaction: dict) -> dict:
>         t0 = time.perf_counter()
>
>         # Feature fetch with staleness check
>         features = self.store.get_online_features(
>             features=["user_transaction_stats:tx_count_1h", ...],
>             entity_rows=[{"user_id": transaction["user_id"]}]
>         ).to_dict()
>
>         feature_latency_ms = (time.perf_counter() - t0) * 1000
>         if feature_latency_ms > 20:
>             # Feature fetch too slow → use fallback features, alert on-call
>             features = self._get_fallback_features(transaction)
>
>         fraud_prob = await self.model.async_run(features)
>         return {
>             "fraud_probability": float(fraud_prob),
>             "decision": "BLOCK" if fraud_prob > 0.85 else "ALLOW",
>             "model_version": "fraud_model_v3",
>         }
> ```
>
> **Step 5: Monitoring plan**
>
> Configure PSI alert on `tx_amount_sum_1h` (highly correlated with fraud patterns). Set recall@precision=0.9 alert if recall drops > 3% over 7-day window. Business metric: fraud loss rate ($) is the ground truth — offline AUC is only a proxy.
>
> **What I need from you before proceeding:**
> 1. What is the label delay? (hours/days between transaction and confirmed fraud label)
> 2. Current fraud rate? (determines class weight and decision threshold)
> 3. Do you have an existing feature store, or do we design from scratch?

### 9.2 Diagnosing a Recommendation Model CTR Drop

**User:** "Our recommendation model's click-through rate dropped 15% this week. No model changes were deployed. What's happening?"

**Machine Learning Engineer:**
> **Recommendation Model CTR Drop: Root Cause Analysis**
>
> A 15% CTR drop with no model change is almost certainly a data or infrastructure issue, not the model itself. Here is the diagnostic playbook ordered by probability:
>
> **Step 1: Isolate the failure layer (5 minutes)**
>
> ```python
> # Check system-level metrics first — rule out infrastructure
> # 1. Model serving error rate (should be 0%)
> # 2. Feature store latency (should be < 10ms p99)
> # 3. Prediction distribution (has it shifted?)
>
> import pandas as pd
> from evidently.report import Report
> from evidently.metric_preset import DataDriftPreset
>
> # Pull this week vs. last week model inputs from logs
> this_week = pd.read_parquet("logs/features_2026-02-19_to_2026-02-26.parquet")
> last_week = pd.read_parquet("logs/features_2026-02-12_to_2026-02-19.parquet")
>
> report = Report(metrics=[DataDriftPreset()])
> report.run(reference_data=last_week, current_data=this_week)
> report.save_html("drift_report.html")
> # Open report → identify which features drifted
> ```
>
> **Step 2: Root cause decision tree**
>
> ```
> CTR dropped 15% with no model deployment
> │
> ├── Feature store latency spike? (check Redis metrics)
> │   YES → Feature staleness → model getting 4h-old user behavior → fix upstream pipeline
> │
> ├── Any feature showing PSI > 0.25?
> │   YES → Identify which feature; trace to upstream data pipeline
> │         Common culprits: user_activity_7d (if data pipeline delayed)
> │                          item_popularity (if catalog ingestion broke)
> │
> ├── Prediction distribution shifted? (all scores moved up or down)
> │   YES → Feature scale issue (normalization changed?) or embedding drift
> │
> ├── No drift detected, system healthy?
> │   → Seasonality or external event (holiday, competitor promotion)
> │   → A/A test: compare to holdout group that bypasses model entirely
> │   → CTR drop may be real-world behavior change, not model failure
> ```
>
> **Step 3: Most common root cause — upstream data pipeline**
>
> ```python
> # Check feature freshness timestamps
> from feast import FeatureStore
>
> store = FeatureStore(repo_path=".")
>
> # Get feature timestamps for a sample of users
> entity_rows = [{"user_id": uid} for uid in sample_user_ids]
> features = store.get_online_features(
>     features=["user_stats:click_history_7d"],
>     entity_rows=entity_rows,
> )
>
> # If timestamps are all the same (e.g., 2026-02-19 00:00:00)
> # → pipeline has been stuck since Feb 19 → 7-day behavior features are 7 days stale
> print(features.to_df()[["user_id", "event_timestamp"]])
> ```
>
> **Immediate remediation options:**
>
> | Root Cause | Time to Fix | Action |
> |-----------|-------------|--------|
> | Feature pipeline stuck | Hours | Restart Airflow DAG; backfill features |
> | Feature store data corrupted | Hours | Revert to previous snapshot; recompute |
> | Real behavior change (external) | Days | Retrain model on fresh 7-day data |
> | Embedding drift from upstream model | Days | Re-run embedding computation; update feature store |
>
> Send me the drift report output and the feature timestamp distribution — I can pinpoint the exact cause in 10 minutes.

### 9.3 ML Platform Design for a Data Science Team

**User:** "We have 5 data scientists and 10 models in production. Models are deployed as Jupyter notebooks run on a cron job. How do we build a proper ML platform?"

**Machine Learning Engineer:**
> **ML Platform Design: From Notebook Cron to Production MLOps**
>
> Your current setup has three critical failure modes: no reproducibility, no monitoring, and one notebook edit away from a production outage. Here is the target architecture for a 5-person team:
>
> **Target Architecture**
>
> ```
> ┌──────────────────────────────────────────────────────────────┐
> │                    ML Platform Stack                         │
> ├─────────────────┬────────────────┬───────────────────────────┤
> │  Feature Store  │  Experiment    │   Model Registry          │
> │  (Feast OSS)    │  Tracking      │   (MLflow Registry)       │
> │                 │  (MLflow/W&B)  │                           │
> ├─────────────────┴────────────────┴───────────────────────────┤
> │           Pipeline Orchestration (Prefect)                   │
> ├──────────────────────────────────────────────────────────────┤
> │  Model Serving: BentoML → Docker → Kubernetes (k8s)         │
> ├──────────────────────────────────────────────────────────────┤
> │  Monitoring: Evidently AI + Prometheus + Grafana             │
> └──────────────────────────────────────────────────────────────┘
> ```
>
> **Step 1: Standardize training pipelines with Prefect**
>
> ```python
> # Replace: jupyter nbconvert --execute fraud_model.ipynb
> # With: Prefect flow with versioned artifacts
>
> from prefect import flow, task
> import mlflow
>
> @task(retries=2, retry_delay_seconds=60)
> def validate_training_data(data_path: str) -> bool:
>     """Great Expectations data validation gate."""
>     import great_expectations as ge
>     context = ge.get_context()
>     result = context.run_checkpoint("training_data_checkpoint")
>     if not result["success"]:
>         raise ValueError(f"Data validation failed: {result}")
>     return True
>
> @task
> def train_model(data_path: str, config: dict) -> str:
>     """Train and log model to MLflow."""
>     with mlflow.start_run() as run:
>         # All hyperparameters logged automatically
>         mlflow.log_params(config)
>         model = train(data_path, config)
>         mlflow.sklearn.log_model(model, "model")
>         return run.info.run_id
>
> @task
> def evaluate_and_gate(run_id: str, baseline_metric: float) -> bool:
>     """Only promote model if it beats production baseline."""
>     run = mlflow.get_run(run_id)
>     new_metric = run.data.metrics["val_auc"]
>     if new_metric <= baseline_metric:
>         raise ValueError(f"New model AUC {new_metric} does not beat baseline {baseline_metric}")
>     return True
>
> @flow(name="fraud-model-training")
> def fraud_training_pipeline(data_path: str, config: dict):
>     validate_training_data(data_path)
>     run_id = train_model(data_path, config)
>     evaluate_and_gate(run_id, baseline_metric=0.89)
>     # If gate passes, trigger deployment pipeline
> ```
>
> **Step 2: Model Registry governance**
>
> ```yaml
> # .github/workflows/ml-model-promotion.yml
> # Automated staging → production promotion with required checks
> name: ML Model Promotion
> on:
>   workflow_dispatch:
>     inputs:
>       model_name: { required: true }
>       run_id: { required: true }
>
> jobs:
>   promote:
>     steps:
>       - name: Validate model metadata
>         run: |
>           python scripts/validate_model_card.py \
>             --model ${{ inputs.model_name }} \
>             --run-id ${{ inputs.run_id }}
>           # Fails if: no data version logged, no SHAP analysis, no slice report
>
>       - name: Shadow deploy (7 days)
>         run: |
>           kubectl apply -f k8s/shadow-deployment.yaml
>           # Automatic canary promotion after 7-day shadow passes
> ```
>
> **Step 3: Monitoring from day 1 for all 10 models**
>
> ```python
> # monitoring/setup_all_models.py
> # Run once to configure Evidently monitoring for all production models
>
> PRODUCTION_MODELS = [
>     {"name": "fraud_detection", "primary_metric": "recall_at_p90", "drift_features": ["tx_amount", "user_age_days"]},
>     {"name": "churn_prediction", "primary_metric": "auc", "drift_features": ["login_frequency_7d"]},
>     # ... 8 more models
> ]
>
> for model_config in PRODUCTION_MODELS:
>     # Creates a Grafana dashboard + PagerDuty alert per model
>     setup_drift_monitoring(
>         model_name=model_config["name"],
>         psi_threshold=0.25,
>         metric_drop_threshold=0.05,
>         alert_channel="ml-oncall",
>     )
> ```
>
> **Migration roadmap:**
>
> | Week | Action | Risk |
> |------|--------|------|
> | 1–2 | Convert 2 highest-risk models to Prefect flows | Low; notebook stays as backup |
> | 3–4 | Deploy MLflow tracking + model registry | Zero downtime |
> | 5–6 | Add Evidently monitoring to all 10 models | Zero downtime |
> | 7–8 | Shadow-deploy new pipeline versions; retire notebook crons | Validated before cutover |
>
> **Expected outcome:** Model deployment time from 2 days (manual notebook run + manual deploy) to 45 minutes (automated pipeline + registry + canary). Incident MTTD for model degradation from "months" to < 4 hours.

---
