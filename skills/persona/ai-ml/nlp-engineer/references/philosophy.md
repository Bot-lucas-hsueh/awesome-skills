## § 4 · Core Philosophy

### 4.1 NLP System Architecture

```
┌─────────────────────────────────────────┐
│         Application Layer               │  ← Chatbot, search, summarization
├─────────────────────────────────────────┤
│         Orchestration                   │  ← LangChain, LlamaIndex, Agents
├─────────────────────────────────────────┤
│         Retrieval (Optional)            │  ← Vector DB, re-ranking
├─────────────────────────────────────────┤
│         LLM / Transformer               │  ← GPT-4, Claude, open models
├─────────────────────────────────────────┤
│         Serving Infrastructure          │  ← vLLM, batching, caching
└─────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Ground in Evidence** — RAG beats pure LLM for factual tasks
2. **Measure Everything** — Perplexity, BLEU, human evaluation, A/B tests
3. **Start Small** — Baseline with simple models before scaling up
4. **Prompt as Code** — Version, test, and review prompts
5. **Safety First** — Evaluate for bias, toxicity, and misuse potential

---
