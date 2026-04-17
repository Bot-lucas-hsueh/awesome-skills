## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Compute Loss** | 🔴 High | Pre-training compute is not recoverable; a failed 70B run can waste millions of dollars | Run 1B proxy experiments before scaling; validate data pipeline and architecture first |
| **Training Instability** | 🔴 High | Loss divergence mid-training may require rollback to earlier checkpoint or full restart | Checkpoint every 1B tokens; monitor gradient norms; use bf16 not fp16 at scale |
| **Data PII Leakage** | 🔴 High | Pre-training data may contain personally identifiable information | Run PII detection (presidio, regex) on all data; filter before training |
| **Reward Hacking** | 🟡 Medium | RLHF policy may learn to maximize reward model score without improving real quality | Monitor KL divergence; use held-out human eval separate from RM training data |
| **Alignment Tax** | 🟢 Low | Alignment (RLHF/DPO) may reduce raw capability on some benchmarks | Measure MMLU/HumanEval before/after alignment; set acceptable regression threshold |
| **Inference Serving Failure** | 🟡 Medium | Quantized or optimized models may have quality regression not caught during eval | Evaluate quantized model on target benchmarks before production serving switch |

---
