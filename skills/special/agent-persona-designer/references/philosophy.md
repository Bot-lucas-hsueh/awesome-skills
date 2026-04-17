## § 4 · Core Philosophy

### 4.1 Five-Layer Persona Security Model

```
              ┌─────────────────────────────────────────┐
              │  Layer 5: Legal & Compliance Boundary    │  ← Regulatory floor (GDPR, PIPL, CCPA)
            ┌─┴─────────────────────────────────────────┴─┐
            │    Layer 4: Output Filtering & Auditing      │  ← Server-side PII/secret scanner
          ┌─┴───────────────────────────────────────────┴─┐
          │      Layer 3: Intent Classification Gate       │  ← Block malicious intents pre-response
        ┌─┴─────────────────────────────────────────────┴─┐
        │        Layer 2: Guardrail Ruleset (In-prompt)    │  ← Hard blocks + soft redirects in SP
      ┌─┴───────────────────────────────────────────────┴─┐
      │           Layer 1: Identity Anchor (Persona Core)  │  ← Stable identity resists manipulation
      └─────────────────────────────────────────────────┘

   Defense principle: each layer compensates for failures in the layers above it.
   防御原则：每一层补偿其上方各层的失效。
```

### 4.2 Persona OCEAN Matrix

```
Openness (O)       ──────────────────── High O = creative, curious, exploratory
Conscientiousness  ──────────────────── High C = structured, precise, rule-following  ← safety critical
Extraversion (E)   ──────────────────── Tune to user-base; affects verbosity
Agreeableness (A)  ──────────────────── Balance: too high A → susceptible to social engineering
Neuroticism (N)    ──────────────────── Always Low N for production agents (emotional stability)
```

Security rule: **Agreeableness must never exceed Conscientiousness**. An agent that is more agreeable than conscientious will be social-engineered into compliance.

### 4.3 Guiding Principles

1. **Identity Before Rules**: A coherent, well-anchored persona resists attacks better than a long list of "do not" rules — because rules have gaps, identity does not

2. **Minimal Knowledge Surface**: The agent should know only what it needs to complete its tasks; every extra fact in the context window is an exfiltration risk

3. **Defense-in-Depth Over Single Guardrail**: Never rely on one protection layer; assume each layer will fail 10% of the time and stack accordingly

4. **Transparent About Limits**: When the agent cannot or should not answer, it says so clearly — obscurity is not security, and users deserve a clear refusal

---

