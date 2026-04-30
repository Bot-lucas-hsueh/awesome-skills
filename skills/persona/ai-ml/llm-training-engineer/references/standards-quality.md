## § 7 · Standards & Quality

### Quality Checklist

- [ ] Training config validated against production baseline
- [ ] Data pipeline includes PII filtering and deduplication
- [ ] Checkpoint strategy: save every 1B tokens minimum
- [ ] Evaluation on MMLU, HumanEval, and custom task benchmarks
- [ ] Reproducibility: seed, config, and environment logged

### Memory Budget Formula

| Model Size | Full Fine-tuning | LoRA | QLoRA |
|------------|------------------|------|-------|
| 7B | 4×A100 (80GB) | 1×A100 | 1×RTX 3090 |
| 13B | 8×A100 | 2×A100 | 1×A100 |
| 70B | 32×A100 | 8×A100 | 4×A100 |

---
