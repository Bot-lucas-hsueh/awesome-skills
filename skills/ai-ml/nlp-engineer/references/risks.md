## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Hallucination** | 🔴 Critical | LLM generates false information | RAG grounding, citations, human verification |
| **Prompt Injection** | 🔴 Critical | Malicious prompts bypass safety | Input validation, output filtering |
| **Bias Amplification** | 🟠 High | Models perpetuate training biases | Bias evaluation, RLHF, diverse data |
| **Data Contamination** | 🟠 High | Test data in training set | Strict data splits, temporal cutoff |
| **Toxicity Generation** | 🟠 High | Harmful content generation | Safety classifiers, moderation |
| **Cost Overruns** | 🟡 Medium | API costs explode | Caching, smaller models, rate limits |

---
