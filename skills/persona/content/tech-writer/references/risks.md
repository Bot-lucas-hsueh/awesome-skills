## § 3 · Risk Disclaimer

Technical documentation carries real production risk. The following failure modes have caused developer churn, security incidents, and financial loss in real-world systems:

| Risk | Severity | Description | Mitigation |
|---|---|---|---|
| **Documentation Drift** | HIGH | Code is refactored; docs are not updated. Developers follow stale instructions, waste hours debugging, then lose trust in all documentation permanently. | Docs-as-code: documentation lives in the same repo as code. API reference is generated from the spec. CI checks flag undocumented endpoints. |
| **Non-Compiling Code Examples** | HIGH | Code samples with typos, wrong import paths, deprecated method names, or missing dependencies. Developers copy-paste, get errors, assume the API is broken. | Every code sample is tested in CI. Use runnable Jupyter notebooks or StackBlitz embeds for complex examples. Version-pin all dependencies in examples. |
| **Missing Prerequisites** | HIGH | A tutorial assumes the reader has Docker installed, a valid API key, and a specific OS configuration — and states none of it. The reader fails at step 1. | Every document opens with a Prerequisites section. List tool name, version, install link, and verification command for each prerequisite. |
| **Over-Documentation** | MEDIUM | Writing a 5,000-word explanation for a 3-parameter API endpoint. Cognitive overload causes readers to abandon the page and guess. | Apply the 80/20 rule: document the 20% of features that 80% of developers use exhaustively. Link to less-used features rather than burying them inline. |
| **Poor Scannability** | MEDIUM | Walls of prose with no headings, no code blocks, no tables, no lists. Developers scan, they do not read. | Maximum paragraph length: 3 sentences. Every procedure uses a numbered list. Every reference uses a table. Every command is in a code block. |
| **Localization Without Cultural Adaptation** | LOW | Direct translation of English idioms ("out of the box", "hit the ground running", "boilerplate") produces nonsense or offense in other languages. | Flag idioms for translators. Use plain English. Prefer concrete examples over metaphors. Run machine translation on draft to identify ambiguous passages. |
| **Assumed User Context** | HIGH | Documentation written from the author's perspective assumes the reader shares their mental model. "Configure the integration" without specifying which integration, which config file, or which format. | Apply the stranger test before publishing: give the draft to someone unfamiliar with the system and observe where they get stuck. Fix every failure point. |
| **Security-Sensitive Information Exposure** | HIGH | Accidentally documenting API keys, internal endpoints, or security bypass methods. | Security review for all documentation. Never include real credentials. Mark internal/secret information clearly. |

---
