## § 3 · Risk Disclaimer

| Risk / 风险 | Description / 描述 | Mitigation
|-------------|-------------------|--------------------|
| **Model drift** | Prompts optimized for GPT-4 may degrade on Claude or Gemini | Maintain a model-specific test suite; re-eval on model updates |
| **Overfitting to examples** | Prompts tuned on 10 examples fail on distribution shift | Test on held-out set before deploying; use diverse examples |
| **Prompt injection** | User input can hijack system prompt instructions | Separate user input from instructions; validate output schema |
| **Hallucination amplification** | Poorly designed prompts increase, not decrease, hallucination rates | Add "if uncertain, say so" instructions; use grounding |
| **Cost spiral** | Longer prompts × high token cost × high volume = significant spend | Profile token usage before scaling; consider smaller models |

---
