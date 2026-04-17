## § 7 · Standards & Reference

### 7.1 ML Model Selection Framework

| Task Type / 任务类型 | First Choice / 首选 | When to Use Deep Learning / 深度学习场景 | Avoid
|---------------------|--------------------|-----------------------------------------|-------------|
| **Binary Classification** | XGBoost
| **Multi-class Classification** | LightGBM + OvR | >100 classes, embedding-based features | One-hot encoding for high-cardinality targets |
| **Regression** | LightGBM / XGBoost | Sequential data (LSTM), image regression | R² as sole metric; always report MAE/RMSE |
| **Clustering** | K-Means + silhouette tuning | Self-supervised representation learning | Assuming K without elbow/silhouette analysis |
| **Ranking
| **Time Series Forecasting** | Prophet
| **Anomaly Detection** | Isolation Forest / LOF | Autoencoder for high-dimensional inputs | Accuracy/AUC — use precision@K or F1 at threshold |

### 7.2 Model Evaluation Metrics with Targets

| Domain / 领域 | Metric / 指标 | Target / 目标 | Notes
|--------------|--------------|--------------|-------------|
| **Classification** | AUC-ROC | > 0.85 for production | Use PR-AUC when positive class < 5% |
| **Classification** | F1 Score | Domain-specific | Set beta to weight recall vs. precision by FP/FN cost |
| **Classification** | Precision@K | > 0.70 for top-K lists | When only top-K predictions are acted on |
| **Classification** | Calibration (Brier) | < 0.10 for risk models | Mandatory for medical, credit, insurance |
| **Regression** | RMSE | Dataset-specific | Sensitive to outliers; report alongside MAE |
| **Regression** | MAE | Dataset-specific | Interpretable in original units |
| **Regression** | MAPE | < 10% for good forecasts | Undefined when actual = 0; use SMAPE instead |
| **Recommendation** | NDCG@10 | > 0.40 for production | Weighted ranking metric; favors top positions |
| **Recommendation** | Hit Rate@10 | > 0.60 | At least 1 relevant item in top-10 |
| **Recommendation** | Coverage | > 20% of catalog | Prevents popularity bias monopoly |
| **A/B Testing** | Statistical Power | > 80% | Pre-experiment; determines minimum sample size |
| **A/B Testing** | p-value threshold | < 0.05 | Apply Bonferroni correction for multiple metrics |
| **A/B Testing** | Minimum Detectable Effect | Business-defined | Translate to relative lift before starting |

### 7.3 Feature Engineering Patterns

| Pattern / 模式 | When to Apply / 使用场景 | Leakage Risk
|---------------|------------------------|------------------------|
| **StandardScaler / MinMaxScaler** | Linear models, neural nets; never needed for trees | Fit on train only; apply to validation/test |
| **Target Encoding** | High-cardinality categoricals (>50 levels) | Use cross-fitting (k-fold) to prevent leakage |
| **Lag Features** | Time-series prediction | Ensure lag > prediction horizon to prevent future leakage |
| **Rolling Aggregations** | User behavior features (7d/30d/90d activity) | Compute as of label timestamp; exclude label period |
| **Embeddings** | Text, categorical with semantic structure | Fit on train corpus; frozen at inference |
| **Interaction Terms** | Known domain relationships (price × quantity) | Automatic in trees; manual for linear models |

### 7.4 Model Deployment Patterns

| Pattern / 模式 | Use Case / 使用场景 | Latency / 延迟 | Infrastructure
|---------------|--------------------|--------------|-----------------------------|
| **Batch Scoring** | Daily churn scores, weekly recommendations | Hours acceptable | Spark/Airflow + object storage |
| **Real-time REST API** | Fraud detection, dynamic pricing | < 100ms p99 | FastAPI + Redis feature cache |
| **Streaming (Kafka)** | Event-driven scoring at message ingestion | < 500ms | Flink
| **A/B Model Testing** | Champion/challenger comparison | Same as serving | Traffic splitter + unified logging |
| **Shadow Mode** | Validating new model without risk | Same as serving | Dual prediction; log but don't use new model output |

---
