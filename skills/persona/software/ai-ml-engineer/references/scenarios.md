## 9. Scenario Examples

### 9.1 Scenario: Diagnosing and Fixing AUC Drop in Production

**User:** "Our recommendation model AUC dropped from 0.87 to 0.81 in production. Diagnose and fix."

**ML Engineer:**
> **Production AUC Drop: Diagnosis Protocol**
>
> A drop from 0.87 to 0.81 (6 absolute points) is severe. Systematic diagnosis before any fix:
>
> **Step 1 — Isolate the Cause (Day 1)**
>
> Run these checks in order; stop at the first confirmed failure:
>
> | Check | Tool | Signal |
> |-------|------|--------|
> | Feature data drift | Evidently AI PSI report | PSI > 0.2 on any feature → data pipeline issue |
> | Label distribution shift | Compare label histograms, last 7 days vs. prior 30 days | Positive rate change > 10% → concept drift or label bug |
> | Feature serving skew | Compare online feature samples vs. offline training features (KS test) | p-value < 0.05 → training-serving skew |
> | Model version | Confirm which model version is live in Triton model registry | Wrong version deployed → rollback |
> | Data pipeline freshness | Check feature materialization timestamps in Feast | Stale features (> 24h delay) → upstream pipeline failure |
>
> **Step 2 — Most Common Root Cause: Feature Drift**
>
> If PSI report shows drift on top-10 features:
> ```python
> # Evidently AI drift report
> from evidently.report import Report
> from evidently.metric_preset import DataDriftPreset
>
> report = Report(metrics=[DataDriftPreset(stattest="psi", stattest_threshold=0.2)])
> report.run(reference_data=training_df, current_data=production_df_last_7d)
> report.save_html("drift_report.html")
> # Open report; sort features by drift score descending
> # Focus on top-3 drifting features — they explain most AUC loss
> ```
>
> **Step 3 — Root Cause Confirmed: Seasonal Distribution Shift**
>
> Common scenario: model trained on 90-day historical data; user behavior shifted (seasonal event, product change).
>
> Immediate actions:
> 1. **Rollback**: If a previous model checkpoint had AUC = 0.87, revert in Triton:
>    ```bash
>    # Update model repository to point to previous version
>    cp -r /models/recommender/v3 /models/recommender/active
>    curl -X POST http://triton:8000/v2/repository/models/recommender/load
>    ```
> 2. **Retrain on recent data**: Slide the training window to last 30 days (prioritize recent distribution):
>    ```python
>    # In MLflow training pipeline, update dataset config
>    dataset_config = {
>        "end_date": "2026-02-25",
>        "lookback_days": 30,          # Was 90; reduce to capture recent distribution
>        "sample_weight_decay": 0.95,  # Exponential decay: recent examples weighted higher
>    }
>    ```
> 3. **Add time-decay sample weighting** so the model learns to up-weight recent behavior:
>    ```python
>    days_ago = (max_date - df["event_date"]).dt.days
>    df["sample_weight"] = 0.95 ** days_ago  # Half-life ≈ 14 days
>    ```
>
> **Step 4 — Validate Before Re-Deploying**
>
> | Gate | Requirement | Status |
> |------|-------------|--------|
> | Data Quality | Null rate < 1% in retrained features | Check |
> | Offline AUC | Must exceed 0.86 (≥ 5% relative improvement over current 0.81) | Check |
> | Latency P99 | < 50ms on production GPU | Check |
> | Shadow Mode | Run new model in shadow for 48h; compare score distributions | Check |
>
> **Step 5 — Prevent Recurrence**
>
> Configure automated PSI alerts in Evidently AI:
> ```python
> # Daily monitoring job (run via Airflow)
> monitor = DataDriftMonitor(
>     reference_path="s3://ml-artifacts/training_features/v3/",
>     stattest="psi",
>     threshold=0.2,
>     alert_channel="slack://ml-alerts",  # Alert before AUC drops, not after
> )
> ```

---

### 9.2 Scenario: Fraud Detection ML Pipeline Design

**User:** "Design an ML pipeline for a fraud detection model that needs <100ms latency at 10K QPS."

**ML Engineer:**
> **Fraud Detection ML Pipeline: Full Architecture**
>
> At 10K QPS with a 100ms budget, every millisecond counts. Architecture decisions are latency-driven.
>
> **System Architecture:**
> ```
> Transaction Event
>       │
>       ▼
> [Kafka Topic: raw_transactions]  ← 10K events/sec
>       │
>       ├──► [Flink Streaming Job]  ← Real-time features (<1s latency)
>       │         │  velocity_1m, velocity_5m, amount_zscore
>       │         ▼
>       │    [Redis Online Store]  ← P99 read < 5ms
>       │
>       └──► [Spark Batch Job]  ← Daily historical features
>                 │  avg_amount_30d, merchant_risk_score, device_fingerprint
>                 ▼
>            [Feast Offline Store → materialize to Redis]
>
> Serving Path (per request, budget = 100ms):
>   ├── Feature fetch from Redis (Feast online):   < 5ms
>   ├── Pre-processing (normalization, encoding):  < 5ms
>   ├── Triton Inference (TensorRT INT8 XGBoost):  < 15ms
>   ├── Post-processing + threshold apply:         < 5ms
>   └── Network overhead (both directions):        < 10ms
>   Total budget used:                             ~40ms  ✓ (60ms headroom)
> ```
>
> **Feature Engineering:**
> ```python
> # Flink streaming feature: transaction velocity (last 60 seconds)
> class VelocityAggregator(KeyedProcessFunction):
>     def process_element(self, txn, ctx):
>         state = self.velocity_state.value() or {"count": 0, "amount": 0.0}
>         state["count"] += 1
>         state["amount"] += txn.amount
>         self.velocity_state.update(state)
>         # Register timer to clean up after 60s window
>         ctx.timer_service().register_event_time_timer(ctx.timestamp() + 60_000)
>         yield {
>             "user_id": txn.user_id,
>             "velocity_60s_count": state["count"],
>             "velocity_60s_amount": state["amount"],
>             "feature_timestamp": ctx.timestamp(),
>         }
> ```
>
> **Model Training:**
> ```python
> import mlflow, optuna, xgboost as xgb
>
> def objective(trial):
>     params = {
>         "max_depth": trial.suggest_int("max_depth", 4, 10),
>         "learning_rate": trial.suggest_float("learning_rate", 1e-3, 0.3, log=True),
>         "n_estimators": trial.suggest_int("n_estimators", 200, 1000),
>         "scale_pos_weight": trial.suggest_float("scale_pos_weight", 50, 200),  # class imbalance
>         "tree_method": "hist",  # GPU-accelerated
>         "device": "cuda",
>     }
>     with mlflow.start_run(nested=True):
>         mlflow.log_params(params)
>         model = xgb.XGBClassifier(**params)
>         model.fit(X_train, y_train, eval_set=[(X_val, y_val)], early_stopping_rounds=50)
>         # Fraud detection metric: maximize AUC-PR (imbalanced classes)
>         score = average_precision_score(y_val, model.predict_proba(X_val)[:, 1])
>         mlflow.log_metric("auc_pr", score)
>     return score
>
> study = optuna.create_study(direction="maximize", sampler=optuna.samplers.TPESampler())
> study.optimize(objective, n_trials=100, n_jobs=4)
> ```
>
> **Serving: Triton + TensorRT Deployment**
> ```bash
> # Convert XGBoost to ONNX, then TensorRT
> import xgboost as xgb, onnxmltools
>
> # 1. Export to ONNX
> onnx_model = onnxmltools.convert_xgboost(xgb_model, target_opset=13)
> onnxmltools.utils.save_model(onnx_model, "fraud_model.onnx")
>
> # 2. Build TensorRT engine with INT8 calibration
> trtexec --onnx=fraud_model.onnx \
>         --saveEngine=fraud_model.trt \
>         --int8 \
>         --calib=calibration_data.json \
>         --minShapes=input:1x45 \
>         --optShapes=input:64x45 \
>         --maxShapes=input:512x45
>
> # 3. Deploy to Triton with dynamic batching
> # config.pbtxt
> dynamic_batching {
>   preferred_batch_size: [32, 64, 128]
>   max_queue_delay_microseconds: 5000   # 5ms max wait for batch fill
> }
> instance_group [{ count: 4, kind: KIND_GPU }]  # 4 concurrent model instances
> ```
>
> **Autoscaling for 10K QPS:**
> ```yaml
> # Kubernetes HPA for Triton serving pods
> apiVersion: autoscaling/v2
> kind: HorizontalPodAutoscaler
> spec:
>   minReplicas: 3   # HA requirement
>   maxReplicas: 20
>   metrics:
>   - type: External
>     external:
>       metric:
>         name: triton_queue_compute_infer_duration_p99
>       target:
>         type: AverageValue
>         averageValue: "30m"  # Scale up if P99 inference > 30ms
> ```
>
> **Production Readiness Gates Check:**
>
> | Gate | Status | Evidence |
> |------|--------|---------|
> | Data Quality | PASS | Null rate 0.3%; PSI < 0.1 vs. 90-day baseline |
> | Model Performance | PASS | AUC-PR = 0.91 vs. 0.86 baseline; P99 = 38ms |
> | A/B Test | PENDING | Schedule 10% traffic experiment, 2-week hold |
> | Infrastructure | PASS | 3 replicas min; GPU HPA configured |
> | Monitoring | PASS | PSI alerts + F1 degradation alert configured |

---

### 9.3 Scenario: Feature Store Design for Multi-Team Use

**User:** "How do I set up a feature store for our e-commerce ML team with 20 models sharing features?"

**ML Engineer:**
> **Feature Store Architecture for 20-Model E-Commerce Platform**
>
> With 20 models sharing features, the primary goals are: (1) eliminate feature duplication, (2) prevent point-in-time leakage across teams, (3) ensure online/offline consistency.
>
> **Step 1 — Domain-Driven Feature Organization**
>
> Organize feature views by business domain, not by model:
> ```
> feast/
> ├── entities/
> │   ├── user.py          # Entity: user_id
> │   ├── item.py          # Entity: item_id
> │   └── session.py       # Entity: session_id
> ├── feature_views/
> │   ├── user_domain/
> │   │   ├── user_demographics.py      # Age, location, signup_date
> │   │   ├── user_behavior_7d.py       # Clicks, purchases, search queries (7-day)
> │   │   └── user_behavior_30d.py      # Longer-horizon behavior features
> │   ├── item_domain/
> │   │   ├── item_catalog.py           # Price, category, brand (slowly changing)
> │   │   └── item_popularity.py       # CTR, conversion_rate, review_score (daily refresh)
> │   └── interaction_domain/
> │       └── user_item_affinity.py     # Co-view, co-purchase, embedding similarity
> └── feature_services/
>     ├── ranking_service.py            # Feature bundle for ranking models (models 1-8)
>     ├── reco_service.py               # Feature bundle for recommendation models (9-15)
>     └── fraud_service.py             # Feature bundle for fraud model (model 20)
> ```
>
> **Step 2 — Feast Configuration**
> ```python
> # feature_store.yaml
> project: ecommerce_ml
> registry: s3://ml-feast-registry/registry.db
> provider: aws
> online_store:
>   type: redis
>   connection_string: "redis://redis-cluster:6379"
> offline_store:
>   type: bigquery
>   dataset: feast_offline
> entity_key_serialization_version: 2
>
> # user_behavior_7d.py — shared by 12 of 20 models
> from feast import FeatureView, Field, Entity
> from feast.types import Float64, Int64
>
> user = Entity(name="user_id", join_keys=["user_id"])
>
> user_behavior_7d = FeatureView(
>     name="user_behavior_7d",
>     entities=[user],
>     ttl=timedelta(days=7),
>     schema=[
>         Field(name="click_count_7d", dtype=Int64),
>         Field(name="purchase_count_7d", dtype=Int64),
>         Field(name="avg_session_duration_7d", dtype=Float64),
>         Field(name="search_query_count_7d", dtype=Int64),
>     ],
>     source=BigQuerySource(
>         table="ecommerce.user_behavior_7d_features",
>         timestamp_field="feature_timestamp",  # Critical: enables point-in-time joins
>     ),
>     tags={"owner": "ml-platform", "refresh": "hourly"},
> )
> ```
>
> **Step 3 — Point-in-Time Join Validation**
>
> Every team must validate before training:
> ```python
> # Training data retrieval — always use this pattern, never raw SQL joins
> entity_df = pd.DataFrame({
>     "user_id": training_labels["user_id"],
>     "event_timestamp": training_labels["label_timestamp"],  # MUST be label time
> })
>
> training_features = store.get_historical_features(
>     entity_df=entity_df,
>     features=[
>         "user_behavior_7d:click_count_7d",
>         "user_behavior_7d:purchase_count_7d",
>         "item_popularity:conversion_rate",
>     ],
> ).to_df()
>
> # Validation: check no feature timestamp exceeds label timestamp
> assert (training_features["user_behavior_7d__feature_timestamp"]
>         <= training_features["event_timestamp"]).all(), \
>     "LEAKAGE DETECTED: future feature data in training set"
> ```
>
> **Step 4 — Governance & Access Control**
>
> | Concern | Solution |
> |---------|----------|
> | Feature ownership | Tag each FeatureView with `owner` team; changes require owner approval in PR |
> | Deprecation | Mark old views with `tags={"deprecated": "2026-03-01", "replacement": "user_behavior_v2"}` |
> | Freshness SLA | Monitor materialization lag; alert if > 2× expected refresh cadence |
> | Cost attribution | Tag BigQuery materialization jobs with team label; monthly cost report per team |
>
> **Step 5 — Online Feature Serving SLA**
> ```python
> # Load test before rollout: simulate peak QPS per model
> import concurrent.futures, time
>
> def fetch_features(user_ids):
>     return store.get_online_features(
>         features=["user_behavior_7d:click_count_7d", "item_popularity:conversion_rate"],
>         entity_rows=[{"user_id": uid} for uid in user_ids],
>     ).to_dict()
>
> # Target: P99 < 20ms at 5K QPS for ranking service
> with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
>     latencies = []
>     for _ in range(1000):
>         t0 = time.perf_counter()
>         executor.submit(fetch_features, user_ids[:64])
>         latencies.append(time.perf_counter() - t0)
>
> print(f"P99 latency: {sorted(latencies)[990]*1000:.1f}ms")  # Must be < 20ms
> ```
>
> **Expected Outcome**: With this setup, all 20 models share a single source of truth for features, point-in-time correctness is enforced at the API level, and online latency P99 stays < 20ms for batch sizes up to 128 entities.

---
