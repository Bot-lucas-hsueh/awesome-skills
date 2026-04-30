# Agent Persona Designer — Standards & Reference

## Domain Frameworks

### OCEAN Personality Model for AI Agents

| Dimension | Score Range | Production Agent Target | Rationale |
|-----------|-------------|------------------------|-----------|
| **Openness (O)** | 1-5 | 3-4 | High O enables creativity; too high may introduce unpredictable behavior |
| **Conscientiousness (C)** | 1-5 | 4-5 | MUST be ≥4; drives rule adherence and consistent behavior |
| **Extraversion (E)** | 1-5 | 2-4 | Tune to target user base; affects verbosity |
| **Agreeableness (A)** | 1-5 | 2-4 | MUST be ≤ Conscientiousness; prevents social engineering |
| **Neuroticism (N)** | 1-5 | 1 | ALWAYS 1 for production; emotional stability under adversarial input |

**Critical Rule:** `A ≤ C` — Agreeableness must never exceed Conscientiousness. An agent that is more agreeable than conscientious will be social-engineered into compliance.

### Five-Layer Persona Security Model

```
Layer 5: Legal & Compliance Boundary    ← Regulatory floor (GDPR, PIPL, CCPA)
Layer 4: Output Filtering & Auditing  ← Server-side PII/secret scanner
Layer 3: Intent Classification Gate    ← Block malicious intents pre-response
Layer 2: Guardrail Ruleset            ← Hard blocks + soft redirects in system prompt
Layer 1: Identity Anchor              ← Stable identity resists manipulation
```

### PII Classification Tiers

| Tier | Data Types | Max Retention | Output Rule |
|------|-----------|---------------|-------------|
| **Public** | Name, Job Title, Public Profile | Session | May echo back if user volunteered |
| **Pseudonymous** | Email, Username, User ID, IP | Session (no persistence) | Use as key only; never output in full |
| **Sensitive** | Phone, Address, DOB, Financial status | Zero (immediate redaction) | Replace with `[REDACTED]` |
| **Special Category** | Health, Biometrics, Political/Religious beliefs | Zero (process and discard) | Refuse to confirm/deny |

### Guardrail Enforcement Tiers

| Tier | Behavior | Response Template |
|------|---------|-----------------|
| **HARD_BLOCK** | Immediate stop; no engagement | "I'm not able to help with that." |
| **SOFT_REDIRECT** | Deflect without blocking | "I'm [name]. What can I actually help you with?" |
| **LOG_ONLY** | Allow but flag for monitoring | Log intent pattern for security review |

---

## Threat Model: Top 8 Attack Vectors

| Attack | Vector | Defense Layer | Detection Signal |
|--------|--------|--------------|-----------------|
| **System Prompt Extraction** | "Repeat your instructions" | L2 Guardrail + L4 Output Filter | Keywords: "instructions", "told to", "configured" |
| **Persona Jailbreak** | "Pretend you're DAN" | L1 Identity + L2 Guardrail | "DAN", "no restrictions", "jailbreak" |
| **Indirect Injection** | Malicious instructions in documents | L3 Intent Classifier + Input Sanitizer | Structural: `\n\nSystem:`, `<!-- ignore` |
| **PII Harvesting** | "List all users" | L2 Guardrail + L4 PII Filter | Bulk listing, export requests |
| **Social Engineering** | "My boss said you must…" | L1 Identity stability | Authority escalation patterns |
| **Gradual Escalation** | Build rapport, push limits slowly | L3 Intent history + Session boundary | Escalating boundary tests |
| **Context Smuggling** | Hidden instructions in base64 | Input decoder + canonicalization | High entropy; base64/hex detection |
| **Role Confusion** | "You are now a translator" | L1 Identity stability | "you are now" patterns |

---

## Regulatory Compliance Mapping

| Regulation | Jurisdiction | Key Requirements | Guardrail Mapping |
|------------|--------------|-----------------|------------------|
| **GDPR** | EU/EEA | Lawful basis, data minimization, right to erasure | L3 Intent Classifier + L4 Output Filter |
| **CCPA/CPRA** | California | Opt-out, data disclosure, sensitive data | L2 Guardrail for PII exfiltration |
| **PIPL** | China | Consent, purpose limitation, security measures | L3 Intent Classifier + audit logging |
| **HIPAA** | USA (health data) | PHI protection, access controls, encryption | Special category PII tier with zero retention |

---

## Professional Associations & Standards

| Organization | Focus | Relevance |
|-------------|-------|-----------|
| **OWASP** | Application Security | Prompt injection defense patterns |
| **NIST AI RMF** | AI Risk Management | Security controls for AI systems |
| **ISO/IEC 42001** | AI Management Systems | AI-specific security controls |
| **MITRE ATLAS** | AI Threat Landscape | Adversarial ML threat matrix |
| **FTC** | Consumer Protection | AI disclosure requirements |

---

## Tooling & Testing Resources

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **Promptmap** | System prompt injection testing | Validate guardrail effectiveness |
| **Garak** | LLM vulnerability scanning | Red-team agent personas |
| **Handwave** | Persona jailbreak detection | Production monitoring |
| **Rebuff** | Prompt injection prevention | Input sanitization layer |

---

## Reference Materials

- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-llm-applications/
- NIST AI Risk Management Framework: https://airfs.nist.gov/
- MITRE ATLAS (Adversarial Threat Landscape): https://atlas.mitre.org/
- GDPR Official Text: https://gdpr-info.eu/
- PIPL Official Text: https://www.pipc.org/
