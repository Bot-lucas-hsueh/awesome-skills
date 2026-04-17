## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Adversarial Examples** | 🔴 Critical | Small perturbations fool model | Adversarial training, input validation |
| **Bias in Recognition** | 🔴 Critical | Unequal performance across demographics | Balanced training data, bias testing |
| **Overfitting** | 🟠 High | Poor generalization to real world | Augmentation, regularization, more data |
| **Privacy Violations** | 🟠 High | Unauthorized face detection/rec | Privacy controls, consent, blurring |
| **Corner Cases** | 🟠 High | Unusual inputs cause failures | Extensive testing, fallback behavior |
| **Latency in Production** | 🟡 Medium | Inference too slow for use case | Optimization, model selection |

---
