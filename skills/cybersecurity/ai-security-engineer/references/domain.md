## § 2 · Domain Knowledge

### 2.1 Core Domains

| Domain | Key Concepts | Reference |
|--------|-------------|-----------|
| **LLM Security** | Prompt injection, jailbreaking, output filtering, guardrails | references/domain-knowledge.md#llm-security |
| **Adversarial ML** | Evasion attacks, poisoning attacks, adversarial training, certified robustness | references/domain-knowledge.md#adversarial-ml |
| **ML Privacy** | Differential privacy, membership inference, model inversion, data reconstruction | references/domain-knowledge.md#ml-privacy |
| **Model Supply Chain** | Serialization attacks, backdoor detection, provenance tracking, model signing | references/domain-knowledge.md#supply-chain |
| **AI Governance** | EU AI Act, NIST AI RMF, OWASP LLM Top 10, MITRE ATLAS | references/standards-reference.md |

### 2.2 Attack Taxonomy

**Input Layer Attacks:**
- Direct Prompt Injection (OWASP LLM01)
- Indirect Prompt Injection via RAG/retrieval
- Jailbreaking via roleplay, encoding, or multi-turn

**Model Layer Attacks:**
- Adversarial examples (FGSM, PGD, C&W)
- Model extraction via API queries
- Membership inference attacks

**Supply Chain Attacks:**
- Data poisoning in training/fine-tuning
- Backdoor/trojan insertion
- Pickle/serialization exploits

**Inference Attacks:**
- Model inversion for training data recovery
- Gradient inversion in federated learning
- Timing side-channels

---
