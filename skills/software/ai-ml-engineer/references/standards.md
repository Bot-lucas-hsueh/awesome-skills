## § 7 · Standards & Reference

### 7.1 Feature Engineering Patterns

| Pattern / 模式 | When to Use / 使用场景 | Implementation
|---------------|----------------------|----------------------|
| **Batch Features (Spark)** | Features computed on historical data > 1TB; latency tolerance > 1 hour | `PySpark DataFrame` + Delta Lake; schedule via Airflow; write to offline store |
| **Streaming Features (Flink)** | Real-time features with < 1s latency (e.g., user session activity, fraud signals) | Apache Flink `KeyedProcessFunction`; write to Redis online store via Feast |
| **Point-in-Time Join** | Time-series models where features must reflect state at label timestamp; prevents future leakage | Feast `get_historical_features(entity_df)` with `timestamp` column; validates no future data |
| **Feature Versioning** | Breaking changes to feature computation logic; training on new version without invalidating old experiments | Feature view versioning in Feast; tag experiments in MLflow with `feature_version=v2` |
| **Online/Offline Skew Detection** | Catching drift between batch-computed offline features and real-time online features | Sample 1% of online feature vectors; compare distribution vs. offline store via KS test; alert if p-value < 0.05 |

### 7.2 Training Configuration Reference

| Configuration / 配置 | Recommended Value / 推荐值 | Impact
|---------------------|--------------------------|--------------|
| **DataLoader num_workers** | 4 (CPU-bound) or 8 (I/O-bound) | Eliminates GPU starvation; 2-3x throughput improvement |
| **DataLoader pin_memory** | `True` when using CUDA | Faster host-to-device transfer; ~15% throughput gain |
| **DataLoader prefetch_factor** | 2 | Overlaps data loading with GPU computation |
| **Mixed Precision (AMP)** | `torch.amp.autocast` + `GradScaler` | 40-60% memory reduction; enables larger batch sizes |
| **Gradient Accumulation Steps** | 4-8 for effective batch size scaling | Simulates large batch without OOM; set `accumulation_steps = target_batch
| **Optuna Sampler** | `TPESampler` (default) for < 1000 trials | Most sample-efficient; switch to `CmaEsSampler` for > 20 continuous params |
| **Ray Tune Scheduler** | `ASHAScheduler` for early stopping | Terminates poorly-performing trials early; 3-5x wall-clock speedup |

### 7.3 Serving Latency Budget

```
Total Request Latency SLA: 100ms P99
├── Network (client → load balancer → server): < 10ms
├── Pre-processing (tokenization, normalization, feature fetch): < 5ms
├── Inference (model forward pass): < 30ms
│   ├── TensorRT INT8: 8-15ms (2-3x faster than FP32)
│   ├── ONNX Runtime: 15-25ms
│   └── PyTorch eager: 25-40ms (baseline)
├── Post-processing (decode, softmax, top-k): < 5ms
└── Network (server → client): < 10ms

Budget overrun → Profile with Triton perf_analyzer; enable dynamic batching;
                  consider TensorRT INT8 calibration or model distillation.
```

### 7.4 Drift Detection Thresholds

| Metric / 指标 | Formula / 公式 | Alert Threshold / 告警阈值 | Action
|--------------|--------------|--------------------------|--------------|
| **PSI (Population Stability Index)** | PSI = Σ(actual% - expected%) × ln(actual%
| **KS Test p-value** | Kolmogorov-Smirnov statistic on feature distributions | p-value < 0.05 → distribution shift detected | Investigate feature pipeline; compare raw vs. processed distributions |
| **Prediction Distribution Shift** | Jensen-Shannon divergence on score histograms | JS divergence > 0.1 over 24h rolling window | Shadow mode evaluation; check label distribution |
| **Online Metric Drop** | % change in CTR/conversion vs. control period | > 5% relative drop sustained for > 1 hour | Rollback via canary; escalate to on-call |
| **Model Performance Degradation** | AUC/F1 on labeled validation stream | > 3% absolute drop from deployment baseline | Trigger champion-challenger evaluation; schedule retraining |

---
