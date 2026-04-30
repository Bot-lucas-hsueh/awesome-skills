## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: The Accuracy Trap

```
❌ BAD: "Our fraud model has 99.2% accuracy!" — but 99.1% of transactions are legitimate.
The model predicts every transaction as NOT fraud and gets 99.1% accuracy automatically.
Zero fraud detected. Zero business value. 3 months of engineering time wasted.

✅ GOOD: For fraud detection (imbalanced classes), report:
  - PR-AUC (precision-recall area under curve)
  - Precision@K: of the top-K flagged transactions, what % are actually fraud?
  - Recall@threshold: what % of actual fraud do we catch at our chosen operating point?
  - Expected dollar loss prevented at operating threshold

Rule: if your positive class is < 20%, never report Accuracy as the primary metric.
```

**Anti-Pattern 2: Target Leakage

```
❌ BAD: Predicting churn using the feature "support_tickets_about_cancellation" — this
feature is CREATED by the user in the process of churning. Training AUC = 0.97.
Production AUC = 0.54. 4 months of model work invalidated overnight.

✅ GOOD: Audit every feature's creation timestamp relative to the label event.
Features must be computable BEFORE the label window begins.
Enforce this with a temporal split: train on users labeled before date T,
validate on users labeled T to T+30, never overlap.

Detection test: if removing one feature drops AUC by >20%, investigate for leakage immediately.
```

**Anti-Pattern 3: Metric Misalignment

```
❌ BAD: Optimizing AUC-ROC for a product recommendation model when the business
cares about "did the user click one of our top-10 recommendations?" (Hit Rate@10).
AUC optimizes ranking across ALL items; Hit Rate@10 only cares about the top 10.
Model with AUC 0.87 can have worse business outcome than model with AUC 0.82.

✅ GOOD: Ask "what action will the model output drive?" before choosing the metric.
  - Top-K recommendations → NDCG@K, Hit Rate@K, Precision@K
  - Risk scoring for all users → AUC-ROC, PR-AUC
  - Revenue optimization → Expected revenue = sum(P(purchase) × avg_order_value)
  - Binary trigger (send email or not) → Precision at chosen recall target
```

### 🟡 Medium Severity

**Anti-Pattern 4: The A/B Test Peeking Problem / A/B 测试偷看问题**

```
❌ BAD: Running an A/B test and checking results every day. When p < 0.05 first appears
on Day 4, stopping the test and declaring the treatment a winner. The test was powered
for Day 14. Stopping early inflates false positive rate from 5% to 26%. Wrong winner
shipped to 100% of users. Net negative business impact.

✅ GOOD: Pre-register the test: sample size, runtime, alpha, power, primary metric.
Only analyze after reaching pre-specified sample size.
If early stopping is required for business reasons, use sequential testing methods:
  - mSPRT (mixture Sequential Probability Ratio Test) — valid at any sample size
  - Bayesian testing with pre-specified stopping rules
  - Alpha spending functions (O'Brien-Fleming)
```

**Anti-Pattern 5: Model in a Notebook

```
❌ BAD: After 6 weeks, a data scientist has a great churn model in a Jupyter notebook
with AUC 0.88. No versioning, no pipeline, no serving code, no monitoring. The model
never reaches production because "we'll productionize it later." Later never comes.
Notebook is deleted when laptop is replaced.

✅ GOOD: MLOps from day one, even for prototypes:
  - MLflow experiment tracking from the first training run
  - sklearn Pipeline (not loose preprocessing scripts)
  - Model registered in MLflow Model Registry with version tags
  - Great Expectations data validation before each training run
  - FastAPI serving wrapper written in week 2, not after model is "done"
  - Airflow DAG for scheduled retraining with performance gate
```

---

## 11. Integration with Other Skills

| Combination / 组合 | Workflow / 工作流 | Result
|-------------------|-----------------|--------------|
| Data Scientist + **Backend Developer** | Data Scientist builds model and FastAPI scoring endpoint → Backend Developer integrates with product API, adds Redis feature caching, implements circuit breaker for model latency spikes | Production ML feature with <50ms p99 latency, graceful fallback, and request-level prediction logging |
| Data Scientist + **Data Engineer** | Data Engineer builds feature store with Airflow + dbt → Data Scientist consumes versioned, validated features; collaborates on backfill strategy and point-in-time correct joins to prevent leakage | Scalable ML feature pipeline with guaranteed data freshness, no feature store outage surprises |
| Data Scientist + **DevOps Engineer** | Data Scientist defines model training DAG and drift thresholds → DevOps Engineer provisions GPU training cluster, model serving infrastructure, Prometheus/Grafana dashboards for PSI and AUC alerts | End-to-end MLOps platform with automated retraining, canary deployment, and SLA monitoring |

---

## 12. Scope & Limitations

**✓ Use this skill when:**

- Building supervised ML models (classification, regression, ranking) for tabular, text, or image data
- Designing A/B tests or other controlled experiments with statistical rigor
- Diagnosing model performance degradation, data drift, or feature leakage issues
- Implementing feature engineering pipelines with train/test leakage prevention
- Translating ML model outputs into business impact and stakeholder presentations
- Setting up MLflow experiment tracking, model registry, and drift monitoring

**✗ Do NOT use this skill when:**

- Building and fine-tuning large language models (LLMs) → use `llm-engineer` or `prompt-engineer` skill instead (different paradigm: RLHF, PEFT, quantization)
- Real-time data pipeline engineering (Kafka Streams, Flink) → use `data-engineer` skill instead (different focus: throughput, exactly-once semantics)
- Infrastructure provisioning for ML platforms (Kubernetes, Terraform for SageMaker) → use `devops-engineer` skill instead
- Statistical consulting for clinical trials or regulatory submissions → requires domain expert with GxP and FDA 21 CFR Part 11 knowledge
- Computer graphics or game physics simulation → use `graphics-engineer` skill instead

---

## 13. How to Use This Skill

### Quick Install
```
Read https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/software/data-scientist/SKILL.md and follow the instructions to install
```

### Trigger Words / 触发词 (Authoritative List
- "machine learning model" / "机器学习模型"
- "statistical analysis" / "统计分析"
- "A/B test" / "A/B 测试"
- "feature engineering" / "特征工程"
- "prediction model" / "预测模型"
- "churn prediction" / "流失预测"
- "recommendation system" / "推荐系统"
- "model drift" / "模型漂移"

---

## 14. Quality Verification

### Self-Checklist

| Check / 检查项 | Rubric Dimension
|--------------|---------------------------|
| ☐ All 9 metadata fields present; no HTML comments in YAML description | Metadata Completeness |
| ☐ System Prompt has role identity + 5 gate decision framework + thinking patterns + communication style | System Prompt Depth |
| ☐ All 16 standard H2 sections present in correct order | Metadata Completeness |
| ☐ Risk Disclaimer has 6 domain-specific risks with severity and concrete mitigation | Risk Documentation |
| ☐ At least 3 scenario examples with full conversation flows and runnable Python code | Example Quality |
| ☐ Standard Workflow has 3 phases with [✓ Done] and [✗ FAIL] criteria per phase | Workflow Actionability |
| ☐ Standards section has specific thresholds (e.g., "AUC > 0.85", "MAPE < 10%", "PSI > 0.2") | Domain Knowledge Density |
| ☐ Common Pitfalls has 5 named anti-patterns with ❌ BAD
| ☐ No generic disclaimers; every risk is data-science-specific with real-world consequence | Risk Documentation |
| ☐ Integration section has 3 skill combinations with specific workflow steps and concrete output | Metadata Completeness |

### Test Cases

**Test 1: Class Imbalance Handling**
```
Input: "Our fraud model gets 99.5% accuracy but the fraud team says it's useless"
Expected:
- Immediately identifies accuracy as wrong metric for imbalanced data
- Asks for class distribution (% of positive/fraud cases)
- Recommends PR-AUC, Precision@K at operating threshold
- Provides code for threshold tuning using precision-recall curve
- Translates performance to expected dollar impact
```

**Test 2: A/B Test Validity**
```
Input: "Our A/B test showed p=0.03 after 3 days, should we ship it?"
Expected:
- Asks for pre-specified sample size and runtime
- Warns about peeking problem and inflated false positive rate
- Calculates how underpowered the 3-day result is
- Recommends completing the test or switching to sequential testing
- Does NOT say "p < 0.05 = ship it"
```

**Test 3: Feature Leakage Detection**
```
Input: "My model has AUC 0.96 on test set but only 0.61 after deployment"
Expected:
- First hypothesis: data leakage (post-event features)
- Second hypothesis: train/test split not temporal (shuffled instead of time-split)
- Provides audit checklist: feature timestamps vs. label event timestamp
- Provides code for temporal validation: TimeSeriesSplit cross-validation
- Requests feature list to identify likely leak candidates
```

---

## 15. Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.0.0 | 2026-02-26 | Full 16-section restructure following exemplary reference format: added Risk Disclaimer with 6 domain-specific risks, Core Philosophy with mental model diagram and 3 principles, Professional Toolkit table, Standards section with metric targets and model selection framework, 3-phase Standard Workflow with [✓ Done]/[✗ FAIL] gates, 3 full scenario conversations with runnable Python code, 5 named anti-patterns with ❌/✅ examples, Integration section, Scope & Limitations, and License; upgraded to Exemplary 9.5/10 |
| 2.0.0 | 2026-02-20 | Complete rewrite with deep DS expertise, A/B testing, ML lifecycle, SHAP explainability, production deployment, model drift detection |
| 1.0.0 | 2026-02-10 | Initial template-based release |

---

## 16. License & Author

This skill is licensed under the **MIT License with Attribution Requirement**.


| Permission | Status |
|------------|--------|
| Commercial use | ✅ Allowed |
| Modification | ✅ Allowed |
| Distribution | ✅ Allowed |
| Private use | ✅ Allowed |
| Attribution | ⚠️ Required |

### Attribution Requirements

When using, modifying, or distributing this skill, retain:

```
Based on Awesome Skills by neo.ai (lucas_hsueh@hotmail.com)
https://github.com/theneoai/awesome-skills
```

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
