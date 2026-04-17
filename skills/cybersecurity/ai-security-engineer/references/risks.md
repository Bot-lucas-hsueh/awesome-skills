## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation |
|------------|------------------|-------------------|------------|
| **Unauthorized AI red-teaming** | 🔴 Critical | Generating adversarial prompts or jailbreaks against production LLMs without authorization violates platform ToS and potentially computer misuse laws (CFAA, Computer Misuse Act) | Only provide jailbreak guidance for authorized red team exercises; include explicit authorization requirement in every offensive technique discussion |
| **Model theft via API extraction** | 🔴 High | Model extraction attacks using API queries can reconstruct proprietary models, violating IP and trade secret law | Implement query rate limiting + fingerprinting; detect systematic extraction patterns |
| **Differential privacy misconfiguration** | 🔴 High | Setting ε > 10 in DPSGD provides negligible privacy protection; ε = 0.1 with wrong δ may violate GDPR Art. 89 | Use ε ≤ 1.0 for high-privacy requirements; validate delta ≤ 1/n² where n = dataset size |
| **Guardrail false security** | 🟡 Medium | Input/output filters can be bypassed; organizations treating guardrails as complete security provide false assurance | Treat guardrails as one layer; combine with rate limiting, anomaly detection, human review |
| **Data poisoning in fine-tuning** | 🟡 Medium | Accepting untrusted RLHF data without validation introduces backdoor attacks; 1% poisoning can achieve 90%+ ASR | Validate all training data sources; use influence function analysis |
| **EU AI Act non-compliance** | 🟡 Medium | High-risk AI systems require documented risk management; non-compliance carries up to 3% global turnover fines | Audit AI system use case against Annex III; implement conformity assessment |
| **Inference timing side-channels** | 🟢 Low | Inference latency can reveal model architecture or leak cached content | Normalize inference timing with padding/jitter |

**⚠️ IMPORTANT:**
- All offensive AI security guidance is for authorized red-teaming, defensive research, and educational purposes only.
- Implementing privacy-preserving techniques does not guarantee GDPR/HIPAA compliance without legal review.

---
