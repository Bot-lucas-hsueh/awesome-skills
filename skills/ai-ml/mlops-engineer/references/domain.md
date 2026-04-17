## § 6 · Domain Knowledge

### 6.1 MLOps Maturity Levels

| Level | Name | Characteristics |
|-------|------|-----------------|
| **0** | Manual | No automation, ad-hoc |
| **1** | DevOps | CI/CD for code, some automation |
| **2** | Automated Training | Pipelines, experiment tracking |
| **3** | Automated Deployment | CI/CD for ML, model registry |
| **4** | Full MLOps | Auto-retraining, monitoring, governance |

### 6.2 Drift Detection Methods

| Type | Method | When to Use |
|------|--------|-------------|
| **Data Drift** | KS test, PSI, Wasserstein | Input distribution changes |
| **Concept Drift** | Model performance tracking | Relationship changes |
| **Prediction Drift** | Distribution comparison | Output distribution shifts |
| **Feature Drift** | Individual feature monitoring | Specific feature issues |

### 6.3 Model Testing Strategy

| Test Type | Purpose | Tools |
|-----------|---------|-------|
| **Unit** | Code correctness | pytest |
| **Integration** | Pipeline end-to-end | Custom tests |
| **Model Quality** | Performance regression | Great Expectations |
| **Shadow** | Production comparison | Canary deployment |

---
