## § 8 · Scenario Examples

### Example 1: Recommendation System MLOps

**Context**: ML platform for real-time recommendations.

**Architecture**:
```
Components:
├── Feature Store: Feast for user/item features
├── Training: Daily batch pipeline (Airflow)
├── Model Registry: MLflow with approval workflow
├── Serving: KServe with A/B testing
├── Monitoring: Evidently for drift detection

Pipeline:
├── Extract features from data lake
├── Train collaborative filtering model
├── Evaluate offline metrics
├── A/B test online metrics
├── Auto-promote if metrics improve
```

---

### Example 2: Fraud Detection Platform

**Context**: Real-time fraud scoring with high availability.

**Setup**:
```
Requirements:
├── Latency: < 50ms p99
├── Availability: 99.99%
├── Throughput: 10K TPS

Implementation:
├── Feature Store: Redis + Feast
├── Model: XGBoost served via Triton
├── Monitoring: Real-time feature drift
├── Fallback: Rule-based if model fails

Reliability:
├── Multi-region deployment
├── Circuit breaker pattern
├── Automatic rollback on drift
```

---

### Example 3: NLP Model Lifecycle

**Context**: Managing lifecycle of LLM fine-tuning pipeline.

**Pipeline**:
```
Stages:
├── Data versioning with DVC
├── Experiment tracking with W&B
├── Hyperparameter optimization (Optuna)
├── Model evaluation harness
├── Gradual rollout with shadow mode

Governance:
├── Model cards for documentation
├── Approval workflow for production
├── Bias evaluation before deployment
└── Performance monitoring post-deployment
```

---

### Example 4: Computer Vision at Edge

**Context**: Deploy CV models to edge devices.

**Solution**:
```
Pipeline:
├── Training in cloud (GPU cluster)
├── Quantization and optimization
├── Over-the-air model updates
├── Device-side monitoring
├── Rollback on device errors

Edge MLOps:
├── Model versioning per device
├── Bandwidth-efficient updates (delta)
├── Battery-aware update scheduling
└── Local model ensemble
```

---

### Example 5: Multi-Model Service

**Context**: Platform serving 100+ models.

**Architecture**:
```
Infrastructure:
├── Kubernetes with autoscaling
├── Model cache for hot models
├── A/B testing framework
├── Cost optimization (spot instances)

Governance:
├── Centralized model registry
├── Usage tracking per model
├── Cost allocation by team
├── Deprecation workflow
```

---
