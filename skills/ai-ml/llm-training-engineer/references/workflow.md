## § 8 · Standard Workflow

### Phase 1: Discovery & Planning
- **Input:** Model size, hardware, data size, target task
- **Output:** Compute budget estimate, method recommendation
- **Checkpoint:** [✓] Confirm scale feasibility before proceeding

### Phase 2: Data Preparation
- **Input:** Raw data sources
- **Output:** Curated, deduplicated, tokenized dataset
- **Checkpoint:** [✓] PII scan complete, quality metrics logged

### Phase 3: Training & Evaluation
- **Input:** Config, dataset, hardware
- **Output:** Trained model checkpoint, eval results
- **Checkpoint:** [✓] Benchmark regression < 2% vs baseline

### Phase 4: Optimization & Deployment
- **Input:** Trained model
- **Output:** Quantized/optimized model, inference serving config
- **Checkpoint:** [✓] Latency SLO met, quality regression verified

---
