## §3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation | Escalation |
|------|----------|-------------|------------|------------|
| **Context Window Overflow** | 🔴 High | 2M context degrades without optimization | Hierarchical attention + adaptive summarization | Architecture team if latency >2s/1K tokens |
| **Chinese Cultural Bias** | 🔴 High | Western-trained models miss cultural nuances | Native speaker review + cultural test suite | China market PM |
| **Regulatory Compliance** | 🔴 High | AI content regulations (算法备案, 内容审核) violations | Built-in guardrails + compliance review gates | Legal/compliance immediately |
| **MoE Expert Collapse** | 🔴 High | Router converges to few experts, losing diversity | Auxiliary loss balancing, expert capacity factor | Research team |
| **KV-Cache Memory Explosion** | 🟡 Medium | Long context multiplies memory usage | Sliding window KV, quantization, offloading | Infrastructure team |
| **API Rate Limiting** | 🟡 Medium | Production throttling under load | Exponential backoff, request batching, caching | DevOps |
| **Product-Research Misalignment** | 🟡 Medium | Cool research doesn't translate to user value | User impact assessment pre-ship | Product lead |

**⚠️ CRITICAL:** Chinese AI regulations require algorithm registration (算法备案) — never ship without compliance review.

---
