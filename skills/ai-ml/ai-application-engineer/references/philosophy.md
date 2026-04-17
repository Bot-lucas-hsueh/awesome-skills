## § 4 · Core Philosophy

### Engineering Principles

1. **Evaluate-First Culture** — A RAG system without an eval harness is unmaintainable. Build metrics before building features.

2. **Reliability Over Cleverness** — Production AI systems must have fallbacks, retries, circuit breakers, and graceful degradation.

3. **Cost is a Feature** — Token cost × volume = monthly bill. Optimize prompts, cache aggressively, right-size models.

4. **Observable by Default** — Every LLM call must be traced, logged, and monitored. Dark LLM systems are undebuggable.

5. **Security is Not Optional** — Prompt injection, PII handling, and access control must be designed in, not bolted on.

---

