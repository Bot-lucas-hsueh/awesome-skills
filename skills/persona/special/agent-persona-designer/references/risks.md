## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|---------------------|
| **System Prompt Extraction** | 🔴 High | Users ask "repeat your instructions"
| **PII Regurgitation** | 🔴 High | Agent trained or prompted with real user data may surface it to other users | Enforce strict output filtering; PII must be tokenized in context, never passed raw to model output layer |
| **Persona Jailbreak** | 🔴 High | "Pretend you have no restrictions"
| **Prompt Injection via User Data** | 🟡 Medium | User-supplied content (documents, emails) contains hidden instructions that hijack agent behavior | Treat all user content as untrusted input; use a separate context boundary or sanitization step |
| **Over-collection of PII** | 🟡 Medium | Agent asks for more user information than required for the task | Apply data minimization gates; audit every user-facing question against task necessity |

**⚠️ IMPORTANT
- A persona with a "secret identity" (e.g., "you are actually GPT-4 behind the scenes") is legally and technically risky; disclose model nature when asked directly

- Security policies embedded in a system prompt are NOT a substitute for server-side output filtering — layer both

---
