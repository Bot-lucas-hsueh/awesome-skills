## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Training-Serving Skew** | 🔴 Critical | Different code paths for train/serve | Unified feature store, same transformation |
| **Model Degradation** | 🔴 Critical | Silent accuracy drop in production | Automated monitoring, drift detection |
| **Pipeline Failures** | 🟠 High | Broken data dependencies | Data validation, lineage tracking |
| **Shadow Deployment** | 🟠 High | Model tested but never validated | Gradual rollout, automated rollback |
| **Reproducibility Loss** | 🟠 High | Can't reproduce results | Version pinning, containerization |
| **Resource Waste** | 🟡 Medium | Unused experiments, large artifacts | Cleanup policies, artifact lifecycle |

---
