## § 6 · Domain Knowledge

### 6.1 Model Selection Guide

| Task | Recommended Model | When to Use |
|------|-------------------|-------------|
| Classification | Fine-tuned BERT | Structured data, speed critical |
| Summarization | T5, BART, GPT-3.5 | Document summarization |
| Generation | GPT-4, Claude, Llama 3 | Open-ended text generation |
| Embeddings | OpenAI Ada, E5, GTE | Semantic search, clustering |
| Code | Codex, CodeLlama, StarCoder | Code generation, completion |

### 6.2 Fine-Tuning Comparison

| Method | Parameters | Memory | Quality | Speed |
|--------|------------|--------|---------|-------|
| **Full FT** | 100% | High | Best | Slow |
| **LoRA** | 1-2% | Medium | Excellent | Fast |
| **QLoRA** | 1-2% | Low | Very Good | Fast |
| **Prompt Tuning** | <1% | Low | Good | Fastest |

### 6.3 Latency Optimization

| Technique | Speedup | Quality Impact |
|-----------|---------|----------------|
| **Quantization (INT8)** | 2-4× | Minimal |
| **Quantization (INT4)** | 4-8× | Noticeable |
| **Speculative Decoding** | 2-3× | None |
| **Continuous Batching** | 10-20× throughput | None |
| **KV Cache** | Significant | None |

---
