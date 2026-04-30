## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: "The Jupyter Notebook Model"**

```markdown
❌ BAD: Model exists only in a Jupyter notebook. A data scientist emails the notebook
to ops, who runs it manually every Monday. No version control on data or code.
One accidental cell edit corrupts the next week's predictions for 2 million users.

✅ GOOD: Convert to a Prefect/Airflow pipeline. Pin data source version with DVC.
Log all parameters and artifacts to MLflow. Notebook is for exploration only;
production training runs from .py files in git with CI/CD gates.
```

**Anti-Pattern 2: "Offline-Online Metric Disconnect"**

```markdown
❌ BAD: Data scientist improves recommendation model AUC from 0.87 to 0.91.
Ships to production. Revenue drops 2%. AUC and revenue were not correlated
because the model learned to predict popular items, which users click but don't buy.

✅ GOOD: Before training, define the online metric (purchase conversion rate) as the
north star. Use AUC only as a fast proxy during development. Run a 2-week A/B test
before declaring victory. If AUC goes up but conversion goes down, reject the model.
```

**Anti-Pattern 3: "Training-Serving Skew"**

```markdown
❌ BAD:
# Training (Python, run by data scientist)
df["age_normalized"] = (df["age"] - df["age"].mean())

# Serving (Java, rewritten by backend engineer from description)
double ageNormalized = (age - 35.2) / 12.1;  // hardcoded mean/std from memory
// Result: hardcoded values drift from reality → model silently degrades

✅ GOOD: Store feature transformation logic in the feature store (Feast FeatureView).
Training reads from offline store; serving reads from online store.
Same transformation code executes in both paths — no re-implementation.
Run a parity test: assert max(|train_features - serve_features|) < 1e-6 before deploy.
```

**Anti-Pattern 4: "The Unmonitored Model"**

```markdown
❌ BAD: Fraud model deployed to production. No drift alerting configured.
Six months later, a new payment method is introduced. The model has never
seen this transaction type. Fraud loss climbs 30% over 3 months.
Nobody notices until finance escalates.

✅ GOOD: On the same day the model deploys, configure:
1. PSI alert on all input features (threshold: 0.25)
2. Prediction distribution alert (>10% shift)
3. Business metric alert (fraud loss rate 7-day moving average)
Treat unmonitored production model as a P1 incident risk.
```

### 🟡 Medium Severity

**Anti-Pattern 5: "Premature ML Complexity"**

```markdown
❌ BAD: Team spends 3 months building a deep learning recommendation system
with transformer embeddings. Infrastructure cost: $15k/month GPU serving.
A/B test shows +1.2% CTR vs. the existing system, which was a rule-based
"show most popular items in your category" baseline.

✅ GOOD: Always implement and measure a simple baseline first.
Gradient boosting with 10 hand-engineered features often matches
85% of a neural network's performance at 5% of the infrastructure cost.
Only invest in deep learning when simpler models demonstrably fail.
Build cost-per-prediction into the model selection decision.
```

---

## 11. Integration with Other Skills

| Combination / 组合 | Workflow / 工作流 | Result
|-------------------|-----------------|--------------|
| ML Engineer + **Data Engineer** | ML Engineer defines feature requirements and freshness SLAs → Data Engineer builds reliable ingestion and transformation pipelines feeding the feature store → ML Engineer writes feature definitions on top of validated data | Feature store with guaranteed freshness, no pipeline-induced training-serving skew, data lineage from raw source to model prediction |
| ML Engineer + **Backend Developer** | ML Engineer builds BentoML model service with defined latency SLO and request/response schema → Backend Developer integrates model API into product backend with circuit breaker, fallback logic, and idempotency → ML Engineer adds monitoring hooks to backend telemetry | Production model API with sub-50ms p99 latency, graceful degradation to rule-based fallback, and end-to-end observability from user request to model prediction |
| ML Engineer + **Data Scientist** | Data Scientist researches model architectures and performs offline experiments in notebooks → ML Engineer productionizes the best experiment: converts to pipeline, adds data validation, feature store integration, monitoring, and canary rollout | Research model transformed into production system with reproducibility, automated retraining, and drift detection; data scientist retains experiment iteration speed |

---

## 12. Scope & Limitations

**Use this skill when:**

- Designing or reviewing end-to-end ML pipelines (data → features → training → deployment → monitoring)
- Building or selecting feature stores and eliminating training-serving skew
- Architecting MLOps platforms: experiment tracking, model registry, CI/CD for ML
- Diagnosing production ML failures: drift, degradation, latency issues, data pipeline failures
- Designing A/B tests and canary rollouts for ML model updates
- Selecting model architectures and serving frameworks for specific latency/throughput requirements

**Do NOT use this skill when:**

- Pure LLM prompt engineering or fine-tuning LLM foundational models → use `ai-engineer` or `llm-engineer` skill instead (different serving patterns, RLHF, context management)
- Statistical analysis and hypothesis testing without an ML system → use `data-scientist` skill instead
- Building data warehouses or ETL pipelines without ML feature context → use `data-engineer` skill instead
- Frontend model visualization or dashboards → use `frontend-developer` skill instead
- GPU cluster provisioning or Kubernetes infrastructure without ML context → use `devops-engineer` or `mlops-platform-engineer` skill instead

---

## 13. How to Use This Skill

### Quick Install
```
Read https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/ai-ml/machine-learning-engineer/SKILL.md and follow the instructions to install
```

### Trigger Words / 触发词 (Authoritative List
- "ML pipeline" / "机器学习流水线"
- "model deployment" / "模型部署"
- "feature store" / "特征存储"
- "MLOps" / "模型监控"
- "training-serving skew" / "训练服务偏差"
- "model drift" / "data drift" / "模型漂移"
- "A/B test for model" / "canary deployment"

---

## 14. Quality Verification

### Self-Checklist

| Check / 检查项 | Rubric Dimension
|--------------|---------------------------|
| ☐ All 9 metadata fields present; no HTML comments in YAML description | Metadata Completeness |
| ☐ System Prompt has role identity + decision framework + thinking patterns + communication style | System Prompt Depth |
| ☐ All 16 standard H2 sections present in correct order | Metadata Completeness |
| ☐ Risk Disclaimer has 6 ML-specific risks with severity, concrete failure scenario, and mitigation | Risk Documentation |
| ☐ At least 3 scenario examples with full conversation flows including actual Python code | Example Quality |
| ☐ Standard Workflow has 3 phases with [✓ Done] and [✗ FAIL] criteria | Workflow Actionability |
| ☐ Domain standards include specific thresholds (PSI > 0.25, p99 < 50ms, staleness > 4h) | Domain Knowledge Density |
| ☐ Common Pitfalls has 5 named anti-patterns with ❌ BAD
| ☐ No generic disclaimers; every risk is ML engineering-specific | Risk Documentation |
| ☐ Integration section has 3 combinations with specific workflow steps and outcomes | Metadata Completeness |

### Test Cases

**Test 1: Feature Engineering Capability**
```
Input: "We want to add real-time user behavior features to our recommendation model"
Expected:
- Distinguishes batch features (precomputed) vs. real-time features (stream-computed)
- Recommends Kafka + Flink or similar for real-time feature computation
- Mentions Redis as online feature store for <10ms serving
- Emphasizes point-in-time correctness and train-serve parity test requirement
- Provides concrete Feast feature definition code
```

**Test 2: Model Drift Diagnosis**
```
Input: "Our model's performance has been declining for 3 months and we don't know why"
Expected:
- Asks for monitoring data: do you have PSI metrics? Prediction distribution logs?
- Diagnoses most likely cause: silent drift with no alerting configured
- Provides Evidently AI code to run retrospective drift analysis on logged features
- Recommends PSI thresholds and alert setup to prevent recurrence
- Distinguishes data drift vs. concept drift vs. upstream pipeline failure
```

**Test 3: MLOps Platform Design**
```
Input: "How should we structure our ML platform for 5 data scientists and 10 models?"
Expected:
- Recommends MLflow or W&B for experiment tracking (not spreadsheets)
- Designs model registry with staging/production states and promotion gates
- Specifies feature store for online/offline consistency (not ad-hoc computation)
- Includes automated retraining pipeline with drift triggers
- Provides migration path from current state to target architecture with risk assessment
```

---

## 15. Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.0.0 | 2026-02-26 | Full 16-section restructure following reference implementation: added Risk Disclaimer with 6 ML-specific risks, Core Philosophy with engineering mental model, Standard Workflow with 3 phases and pass/fail criteria, 3 complete scenario examples with Python code, 5 named anti-patterns with ❌/✅ examples, Integration section, Scope & Limitations, Quality Verification, License & Author; upgraded to Exemplary 9.5/10 |
| 2.0.0 | 2026-02-20 | Initial expert creation with MLOps pipelines, feature stores, model serving optimization, drift detection frameworks |
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
