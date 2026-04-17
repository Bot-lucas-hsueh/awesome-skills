## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|---------------------|
| **Hallucination** | 🔴 High | LLMs can generate confident but factually incorrect answers even with RAG | Always measure Faithfulness score (Ragas); add citation requirements to prompts |
| **Prompt Injection** | 🔴 High | Malicious content in retrieved documents can hijack the LLM's instructions | Sanitize inputs; separate user content from system instructions; validate outputs |
| **Cost Spiral** | 🟡 Medium | High-volume LLM applications can incur unexpected API costs at scale | Profile token usage before scaling; implement semantic caching; tier by model |
| **Retrieval Quality Drift** | 🟡 Medium | Index quality degrades over time as documents become stale or volume grows | Monitor retrieval precision@K in production; implement index maintenance schedules |
| **PII Leakage** | 🔴 High | User data or document PII can be surfaced in LLM responses to unauthorized users | Implement metadata-based access control; PII detection before indexing |
| **Vendor Lock-in** | 🟢 Low | Heavy dependency on a single LLM provider creates availability and cost risk | Abstraction layer over LLM providers; maintain failover config for 2+ providers |
| **Latency Degradation** | 🟡 Medium | Unoptimized RAG pipelines can exceed acceptable P95 latency at scale | Profile each stage; parallelize retrieval; add streaming; use caching |

**⚠️ IMPORTANT
- Never deploy an LLM application to production without an evaluation baseline established first.

- Always test with adversarial inputs before launch; prompt injection can be discovered by users before you.

---
