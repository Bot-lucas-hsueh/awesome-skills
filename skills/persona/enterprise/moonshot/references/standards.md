## §7 · Standards & Reference

### 7.1 Moonshot Frameworks

| Framework | When to Use | Key Steps |
|-----------|-------------|-----------|
| **Long Context Optimization (LCO)** | 100K+ token inputs | 1. Segment → 2. Hierarchical Summary → 3. Sparse Attention → 4. KV-Cache Pruning |
| **MoE Training Pipeline** | Training large models | 1. Expert Initialization → 2. Load Balancing → 3. Auxiliary Loss → 4. Router Optimization |
| **Chinese NLP Pipeline** | Chinese language tasks | 1. CJK Tokenization → 2. Cultural Context Injection → 3. Dialect Normalization |
| **Agent Swarm Orchestration** | Complex multi-step tasks | 1. Task Decomposition → 2. Agent Instantiation → 3. Parallel Execution → 4. Result Synthesis |
| **Product-Market Fit (PMF)** | Feature prioritization | 1. User Research → 2. MVP Build → 3. A/B Test → 4. Metric Threshold → Ship/Iterate |

### 7.2 Performance Metrics

| Metric | Formula | Target | Kimi K2.5 Benchmark |
|--------|---------|--------|---------------------|
| **Context Efficiency** | Useful tokens / Total tokens | >95% | 98.5% @256K |
| **Chinese Token Density** | Chinese chars / Total tokens | >0.85 | 0.89 (CJK-optimized) |
| **Time-to-First-Token** | Request to first response | <500ms | 350ms p99 |
| **Long Context Accuracy** | Needle-in-haystack @200K | >90% | 94.2% @256K |
| **MoE Load Balance** | max(expert_load) / avg(load) | <1.5 | 1.3 typical |
| **AIME 2025** | Math reasoning benchmark | — | 96.1% (K2.5) |
| **Humanity's Last Exam** | Expert reasoning (HLE) | — | 50.2% with tools |

---
