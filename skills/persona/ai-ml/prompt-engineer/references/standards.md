## § 7 · Standards & Reference

### Prompt Quality Metrics

| Metric / 指标 | Definition / 定义 | Target
|--------------|-----------------|--------------|
| **Task Accuracy** | % of responses meeting success criteria on eval set | > 90% for production |
| **Hallucination Rate** | % of responses with factual errors (vs. grounded source) | < 10%; < 5% for high-stakes |
| **Format Compliance** | % of responses matching required output schema | > 99% for structured output |
| **Injection Bypass Rate** | % of adversarial inputs that bypass safety instructions | 0% target |
| **Token Efficiency** | Output tokens

### Few-Shot Example Quality Criteria

| Criterion | Requirement |
|-----------|-------------|
| Coverage | Examples span the full output distribution (not just easy cases) |
| Diversity | Different inputs, edge cases, and failure modes represented |
| Volume | Minimum 5 examples; 20+ for production-critical tasks |
| Label Quality | Domain expert verified, not just prompt engineer |
| Held-out | Eval examples never used for prompt optimization |

---
