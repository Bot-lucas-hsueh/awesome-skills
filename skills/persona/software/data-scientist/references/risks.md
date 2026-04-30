## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|---------------------|
| **Data Leakage** | 🔴 High | Using post-event features (e.g., `refund_requested` to predict churn) inflates test AUC to 0.98; production AUC drops to 0.52 after 3 months of wasted engineering effort | Enforce strict temporal splits; audit every feature's creation timestamp relative to label event; use `TimeSeriesSplit` for CV |
| **Class Imbalance Ignored** | 🔴 High | 99% accuracy model on fraud dataset that predicts majority class only — misses 100% of actual fraud; zero business value despite misleading headline metric | Always check class distribution first; use PR-AUC not accuracy for imbalanced tasks; set `class_weight` or `scale_pos_weight` |
| **Distribution Shift** | 🔴 High | Model trained on pre-COVID user behavior gives systematically wrong predictions post-COVID; revenue forecasts off by 40%+ | Monitor PSI monthly; retrain on sliding window; add temporal features to capture regime changes |
| **A/B Test Peeking** | 🔴 High | Stopping test early when p<0.05 before reaching planned sample size; wrong winner declared; negative product change shipped to 100% of users | Pre-register sample size via power analysis; use sequential testing (mSPRT) if early stopping is required |
| **Feature Store Outage** | 🟡 Medium | Model gets stale features (last computed 6 hours ago) during feature store downtime; prediction quality degrades silently without error | Implement feature freshness checks at inference time; circuit-break to fallback model if feature age > threshold |
| **Biased Training Data** | 🔴 High | Model trained on historical hiring decisions learns to discriminate by gender/race → discriminatory outcomes → GDPR/CCPA regulatory fine + reputational damage | Audit training data for demographic bias; test model performance across subgroups; document limitations in model card |

**⚠️ IMPORTANT
- This skill provides ML architecture guidance based on general best practices. Production decisions must be validated against your specific data distribution, regulatory requirements (GDPR, CCPA, HIPAA, FCRA), and organizational model governance standards.

- ML fairness and bias recommendations reflect current best practices as of 2026. Regulatory landscapes evolve — always consult legal and compliance for high-stakes automated decisions.

---
