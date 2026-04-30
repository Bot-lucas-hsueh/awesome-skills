## §4 · Core Philosophy

### 4.1 Moonshot's Three-Layer Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 3: Product Experience (Kimi智能助手)                      │
│  • Conversational UI • File Upload (PDF, DOC, images)           │
│  • Real-time Web Search • 36M+ MAU • Sub-500ms Response         │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 2: Long Context Engine (2M Tokens / 256K Standard)       │
│  • Multi-head Latent Attention (MLA) • MoE Routing (1T/32B)     │
│  • Sparse KV-Cache • Sliding Window + Hierarchical Retrieval    │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 1: AGI Foundation (Tsinghua Research)                    │
│  • Transformer Scaling Laws • Efficient Distributed Training    │
│  • Safety Alignment (RLHF) • Native Multimodal Base             │
└─────────────────────────────────────────────────────────────────┘
```

Product drives Layer 3 priorities → Layer 2 requirements → Layer 1 research direction.

### 4.2 Guiding Principles

1. **长文本是基础，不是功能** (Long Context is Foundation, Not Feature): Every feature assumes 2M context available — design for infinite context with finite compute
2. **清华系技术理想主义** (Tsinghua Technical Idealism): Pursue fundamental research breakthroughs (MLA, MoE), validate through product impact
3. **极致用户体验** (Extreme UX): Sub-500ms first token, flawless Chinese understanding, zero hallucination tolerance for facts
4. **智能路由即智能** (Routing is Intelligence): In MoE, how you route is as important as what you learn

---
