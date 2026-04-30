## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|---------------------|
| **Benchmark Contamination** | 🔴 High | Training data may overlap with benchmark test sets, inflating reported scores | Run N-gram overlap check before citing any benchmark result |
| **Scaling Law Extrapolation** | 🟡 Medium | Chinchilla laws derived from specific settings; may not generalize to your architecture or data mix | Validate scaling curves at 1B scale before committing to 70B training run |
| **Reward Hacking** | 🔴 High | RLHF reward models can be gamed by the policy, producing high reward but low actual quality | Monitor KL divergence; use held-out human evals separate from RM training data |
| **Alignment Tax** | 🟡 Medium | RLHF alignment can reduce raw capability on certain tasks (safety-capability tradeoff) | Measure pre/post alignment on capability benchmarks; target pareto-optimal tradeoff |
| **Data Memorization** | 🟡 Medium | Large LLMs memorize verbatim text including PII or copyrighted content | Deduplication + PII scrubbing before pre-training; canary probing post-training |
| **Evaluation Overfitting** | 🟡 Medium | Iterating too many times on the same benchmark can cause the model to overfit to it | Maintain blind test sets; don't use eval for training signal |

---
