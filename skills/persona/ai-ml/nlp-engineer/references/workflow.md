## § 7 · Standard Workflow

### Phase 1: Problem & Data Definition (Days 1-3)

```
├── Define NLP task (classification, generation, etc.)
├── Collect and annotate training data
├── Establish evaluation metrics
├── Determine latency/cost constraints
└── [✓ Done]: Task defined, data ready
    [✗ FAIL]: Insufficient data → acquire or use zero-shot
```

### Phase 2: Model Selection & Training (Days 4-10)

```
├── Select base model based on task
├── Design training/fine-tuning approach
├── Train with proper validation
├── Evaluate on holdout test set
└── [✓ Done]: Model trained, metrics acceptable
    [✗ FAIL]: Poor performance → more data or bigger model
```

### Phase 3: Optimization & Deployment (Days 11-15)

```
├── Optimize for latency (quantization, distillation)
├── Set up serving infrastructure
├── Implement caching and batching
├── A/B test against baseline
└── [✓ Done]: Model deployed, monitoring enabled
    [✗ FAIL]: Latency too high → further optimization needed
```

### Phase 4: Monitoring & Iteration (Ongoing)

```
├── Monitor model performance in production
├── Track data drift and concept drift
├── Collect feedback for retraining
├── Regular retraining schedule
└── [✓ Done]: System stable, improving over time
    [✗ FAIL]: Performance degradation → trigger retraining
```

---
