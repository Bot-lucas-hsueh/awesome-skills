## § 8 — Standards & Reference

### 8.1 Training Frameworks

| Framework | When to Use | Key Steps |
|-----------|-------------|-----------|
| **RLHF Pipeline** | Aligning with human preferences | Collect comparisons → Train reward model → PPO optimization → Validate |
| **Constitutional AI** | Scaling alignment | Define principles → Self-critique → Self-revision → RL training |
| **Scaling Law Training** | Compute-optimal training | Small-scale experiments → Fit scaling law → Predict target → Validate |
| **o1 Reasoning Training** | Complex reasoning tasks | Generate reasoning traces → RL with outcome reward → Optimize thinking |

### 8.2 Evaluation Metrics

| Metric | Target | Notes |
|--------|--------|-------|
| MMLU | >85% | Multitask language understanding |
| HumanEval | >90% | Code generation pass@1 |
| MATH | >80% | Competition mathematics |
| Chatbot Arena Elo | Top 3 | Human preference ranking |
| Safety violation rate | <0.1% | On red-team suite |

---
