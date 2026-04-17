## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|---------------------|
| **Training-Serving Skew** | Critical | Feature computation logic differs between offline training and online serving — the model silently receives different inputs than it was trained on, causing unexplained production degradation | Implement feature skew monitoring (compare training feature distributions to online serving logs); enforce a single feature computation library used in both paths |
| **Data Leakage** | Critical | Future information leaks into training features via point-in-time join errors, target encoding, or improper cross-validation splits → offline metrics overestimated by 20-50%; model fails in production | Always use point-in-time correct joins in time-series features; audit all feature timestamps; validate by checking that removing the target column does not improve accuracy |
| **Model Staleness** | High | Production model trained on a stale data distribution decays silently without alerting; KPI metrics degrade gradually over weeks before detection | Configure automated drift detection (PSI > 0.2 triggers alert); set a maximum model age policy; implement weekly retraining on recent data |
| **Infrastructure Overfit** | Medium | Model behavior is optimized or validated for staging environment; GPU driver version, batch size, and memory constraints differ in production, causing subtle prediction differences | Run shadow mode evaluation in the production environment before full rollout; validate TensorRT-compiled model output vs. PyTorch reference on production hardware |

**IMPORTANT
- Production ML systems require ongoing monitoring investment proportional to model business impact; this skill guides architecture and implementation but cannot replace operational runbooks specific to your infrastructure

- Data quality issues are the most common root cause of production ML failures; always instrument data pipelines before model pipelines

---
