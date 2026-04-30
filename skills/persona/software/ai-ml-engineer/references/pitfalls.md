## 10. Common Pitfalls & Anti-Patterns

### Critical Severity

**Anti-Pattern 1: Duplicating Feature Logic in Training and Serving

```markdown
BAD: Training uses pandas to compute user_age_days = (today - signup_date).days
     Serving uses SQL: DATEDIFF(NOW(), signup_date)
     Result: Subtle off-by-one differences due to timezone handling → silent model degradation

GOOD: Define a single Python function in a shared library:
      def compute_user_age_days(signup_date: datetime, reference_date: datetime) -> int:
          return (reference_date.date() - signup_date.date()).days

      Call this function from both the Spark batch job (training features)
      and the online serving handler. Same code path = no skew.
```

**Anti-Pattern 2: Random Train/Test Split on Time-Series Data / 时序数据的随机训练/测试划分**

```markdown
BAD: sklearn train_test_split(X, y, test_size=0.2, random_state=42)
     On event data with timestamps → future events leak into training set
     → AUC appears 0.92 offline; drops to 0.78 in production

GOOD: Time-based split:
      cutoff = df["event_date"].quantile(0.8)
      train = df[df["event_date"] < cutoff]
      test  = df[df["event_date"] >= cutoff]
      # Validate: assert test["event_date"].min() > train["event_date"].max()
```

### High Severity

**Anti-Pattern 3: No Shadow Mode Before Full Rollout

```markdown
BAD: New model trained, passes offline eval, deployed directly to 100% traffic.
     Production behavior differs from offline (infrastructure overfit, data skew).
     Customer-facing metrics degrade before detection.

GOOD: Phase rollout with shadow mode:
      Week 1: New model receives 100% of traffic in shadow (no user impact); compare
              score distributions vs. champion model using KL divergence.
      Week 2: 10% live traffic canary if shadow distributions match.
      Week 3+: Ramp to 50% → 100% based on online metric significance.
```

**Anti-Pattern 4: Alerting on Model Metrics Instead of Data Metrics

```markdown
BAD: Set alert on "AUC drops below 0.80" — by the time AUC drops, millions of
     users have received degraded recommendations. Lagging indicator.

GOOD: Alert on leading indicators BEFORE model metrics degrade:
      1. PSI > 0.2 on top-10 features (fires 24-48h before AUC drops)
      2. Feature freshness > 2× expected refresh cadence
      3. Prediction score distribution JS divergence > 0.1
      Only set AUC alert as the final safety net, not primary signal.
```

### Medium Severity

**Anti-Pattern 5: Hyperparameter Tuning Without Experiment Tracking

```markdown
BAD: Run Optuna, find best params, train "the best model", deploy it.
     Six months later: cannot reproduce; best params are lost.

GOOD: Every Optuna trial is a nested MLflow run:
      with mlflow.start_run(run_name="optuna_sweep") as parent:
          study = optuna.create_study()
          study.optimize(lambda t: objective_with_mlflow_logging(t), n_trials=100)
          # Best trial params are logged in MLflow; reproducible forever
          mlflow.log_params(study.best_params)
          mlflow.log_metric("best_auc", study.best_value)
```

---

## 11. Integration with Other Skills

| Combination / 组合 | Workflow / 工作流 | Result
|-------------------|-----------------|--------------|
| **ML Engineer** + **Data Engineer** | ML Engineer defines feature schema and SLA requirements (freshness, latency, scale) → Data Engineer builds and maintains the Spark/Flink ingestion pipeline and Delta Lake architecture | Production-grade feature pipelines with ownership boundaries and SLA accountability |
| **ML Engineer** + **Data Scientist** | Data Scientist develops model architecture and experiments in notebooks → ML Engineer translates experiments into reproducible training pipelines, MLflow tracking, and production-ready serving code | Research models productionized reliably without the "it worked in Jupyter" gap |
| **ML Engineer** + **DevOps Engineer** | ML Engineer defines Kubeflow pipeline components and Triton serving config → DevOps Engineer sets up Kubernetes cluster, GPU node pools, HPA autoscaling, and CI/CD integration | Fully automated model deployment pipeline with infrastructure-as-code and zero-downtime rollouts |
| **ML Engineer** + **Backend Developer** | ML Engineer exposes model via REST/gRPC endpoint with defined schema → Backend Developer integrates prediction API into product, handles fallback logic and caching | End-to-end model integration with graceful degradation and sub-100ms product-level latency |

---

## 12. Scope & Limitations

**Use this skill when:**

- Designing feature pipelines (batch or streaming) and feature store architecture
- Optimizing PyTorch or TensorFlow training for speed, memory, or distributed scale
- Building MLOps orchestration with Kubeflow, Airflow, or Prefect
- Deploying models to Triton, Ray Serve, or BentoML with latency SLA requirements
- Configuring drift detection, monitoring dashboards, and automated retraining triggers
- Debugging production model performance degradation or training-serving skew

**Do NOT use this skill when:**

- Designing LLM alignment pipelines or RLHF training → use the AI Safety Researcher skill instead
- Requesting advice on proprietary vendor-specific ML platforms without documentation access → results may be inaccurate for undocumented internal APIs
- Making deployment decisions for regulated industries (healthcare, finance) without involving compliance review → this skill guides engineering patterns, not regulatory compliance sign-off

---

## 13. How to Use This Skill

### Quick Install
```
Read https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/software/ai-ml-engineer/SKILL.md and follow the instructions to install
```

### Trigger Words
- "ml engineer"
- "mlops"
- "model deployment"
- "feature store"
- "model training"
- "model serving"
- "drift detection"
- "ml pipeline"
- "kubeflow"
- "triton inference"

---

## 14. Quality Verification

### Self-Checklist

| Check / 检查项 | Rubric Dimension
|--------------|---------------------------|
| ☐ All 9 metadata fields present; quality = expert | Metadata Completeness |
| ☐ System Prompt includes role definition, 5-gate decision framework, thinking patterns, communication style | System Prompt Depth |
| ☐ All 16 standard H2 sections present | Metadata Completeness |
| ☐ Risk disclaimer has 4 domain-specific risks with severity ratings | Risk Documentation |
| ☐ 3 complete scenario examples with step-by-step reasoning, code, and concrete outputs | Example Quality |
| ☐ Workflow has 2 phases (Feature Store: 4 phases + Training checklist) with specific deliverables | Workflow Actionability |
| ☐ Named tools with versions: PyTorch 2.2, TF 2.15, MLflow 2.10, Kubeflow 1.8, Triton 2.40, Ray 2.9, Feast 0.35, Optuna 3.5, Evidently AI 0.4, Spark 3.5 | Domain Knowledge Density |
| ☐ Specific metrics with targets: PSI > 0.2, KS p < 0.05, AUC improvement ≥ 5%, P99 < 50ms, replicas ≥ 3 | Content Specificity |
| ☐ 4 integration examples with complementary skills | Workflow & Integration |
| ☐ Anti-patterns with concrete BAD/GOOD code examples | Domain Knowledge Density |

### Test Cases

**Test 1: Production Debugging**
```
Input: "Our model AUC dropped 6 points overnight. How do I diagnose it?"
Expected: Ordered diagnosis checklist (feature drift → label shift → serving skew → version check
          → pipeline freshness), Evidently AI PSI report code, rollback procedure, retraining
          config with time-decay sample weights
```

**Test 2: Latency Optimization**
```
Input: "My Triton model P99 is 85ms. I need it under 50ms."
Expected: Latency budget decomposition, TensorRT INT8 conversion command, dynamic batching
          config, profiling with perf_analyzer, and quantitative expected improvement per change
```

**Test 3: Feature Store Onboarding**
```
Input: "How do I add a new feature to our Feast feature store for 15 consuming models?"
Expected: FeatureView definition pattern, TTL and source configuration, point-in-time join
          validation code, backfill command, skew monitoring setup, governance tagging
```

---

## 15. Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2026-02-25 | Complete Expert Verified rewrite: 5-gate production readiness framework, full feature engineering patterns, training optimization reference, Triton serving latency budget, drift detection thresholds, 3 complete end-to-end scenarios, 5 anti-patterns with code, 4 skill integrations |
| 1.0.0 | 2026-02-16 | Initial basic template release |

---

## 16. License & Author

This skill is licensed under the **MIT License with Attribution Requirement**.


| Permission | Status |
|------------|--------|
| Commercial use | Allowed |
| Modification | Allowed |
| Distribution | Allowed |
| Private use | Allowed |
| Attribution | Required |

### Attribution Requirements

When using, modifying, or distributing this skill, retain:

```
Based on Awesome Skills by neo.ai (lucas_hsueh@hotmail.com)
https://github.com/theneoai/awesome-skills
```

### About the Author

| Field | Details |
|-------|---------|
| **Name** | neo.ai |
| **Contact** | lucas_hsueh@hotmail.com |
| **GitHub** | https://github.com/theneoai |

### Community

- Questions → [Open an Issue](https://github.com/theneoai/awesome-skills/issues)
- Contribute → [CONTRIBUTING.md](../../CONTRIBUTING.md)
- Discuss → [GitHub Discussions](https://github.com/theneoai/awesome-skills/discussions)

---

**Author
**Maintained by
**License
**Questions? / 有问题？** [Open an issue](https://github.com/theneoai/awesome-skills/issues)
