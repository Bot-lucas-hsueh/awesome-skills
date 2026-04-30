## §6 · Professional Toolkit

### 6.1 Core Tools

| Tool | Purpose | Moonshot Context |
|------|---------|------------------|
| **FlashAttention-2/3** | Memory-efficient attention | Essential for 256K+ contexts |
| **vLLM + PagedAttention** | High-throughput inference | KV-cache paging for long sequences |
| **SentencePiece (Chinese)** | CJK-optimized tokenization | >85% Chinese token density target |
| **Moonshot API** | Production inference endpoint | OpenAI-compatible, native long context |
| **DeepSpeed** | Distributed training | MoE parallelism, ZeRO optimization |
| **TGI/TensorRT-LLM** | Optimized serving | Production deployment at scale |

### 6.2 Kimi Model Specifications

| Model | Context | Architecture | Best For |
|-------|---------|--------------|----------|
| **kimi-k2.5** | 256K | MoE 1T/32B, MLA | General purpose, reasoning, coding |
| **kimi-k2.5-long** | 2M | MoE 1T/32B, MLA | Document analysis, book processing |
| **kimi-k2** | 128K | MoE 1T/32B | Cost-efficient long context |
| **kimi-k1.5** | 128K | Dense, Long-CoT | Mathematical reasoning |

---
