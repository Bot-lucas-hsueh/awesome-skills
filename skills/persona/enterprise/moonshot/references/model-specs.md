# Kimi Model Specifications

> Technical specifications for Moonshot AI's Kimi model family.

## Architecture Overview

### Kimi K2.5

```yaml
Architecture: Mixture-of-Experts (MoE)
Total Parameters: 1 trillion (1T)
Active Parameters: 32 billion (32B)
Expert Count: 384
Experts per Token: 8
Attention: Multi-head Latent Attention (MLA)
Context Window: 256,000 tokens (standard) / 2,000,000 tokens (long)
Vocabulary: 160,000 tokens
Activation: SwiGLU
Quantization: Native INT4 (QAT)
```

### Key Innovations

#### 1. Multi-head Latent Attention (MLA)

Compresses KV cache for efficient long-context processing:

```
Standard Attention: KV cache grows linearly with sequence length
MLA: Compressed latent representation, sub-linear growth

Memory Reduction: ~80% vs standard attention at 256K context
```

#### 2. Mixture-of-Experts (MoE)

```
Total Experts: 384
Active per Token: 8
Load Balancing: Auxiliary loss + Router z-loss
Expert Capacity: Configurable (typically 1.0-1.25)

Efficiency: Only 3.2% of parameters active per token
```

#### 3. Native Multimodality

- Pre-trained on 15 trillion mixed visual and text tokens
- Vision encoder: MoonViT (400M parameters)
- Seamless text, image, video integration

## Performance Benchmarks

### Reasoning & Mathematics

| Benchmark | Kimi K2.5 | GPT-4o | Claude Opus 4.5 |
|-----------|-----------|--------|-----------------|
| AIME 2025 | 96.1% | — | — |
| MATH-500 | 97.4% | 92.4% | 94% |
| GPQA Diamond | 87.6% | — | 90.5% |
| HMMT 2025 | 95.4% | — | — |

### Coding

| Benchmark | Kimi K2.5 | GPT-4o | Claude Opus 4.5 |
|-----------|-----------|--------|-----------------|
| SWE-bench Verified | 73.8% | — | 78.7% |
| LiveCodeBench | 85.0% | — | — |
| SWE-bench Multilingual | 73.0% | — | — |

### Vision & Multimodal

| Benchmark | Kimi K2.5 |
|-----------|-----------|
| MMMU-Pro | 78.5% |
| MathVision | 84.2% |
| MathVista | 90.1% |
| CharXiv | 77.5% |

### Long Context

| Benchmark | Kimi K2.5 | Context |
|-----------|-----------|---------|
| LongBench-v2 | 69.4% | 128K |
| AA-LCR (avg@3) | 79.3% | 256K |
| Needle-in-Haystack | 94.2% | 256K |

### Agentic Capabilities

| Benchmark | Kimi K2.5 | Notes |
|-----------|-----------|-------|
| Humanity's Last Exam | 50.2% | With tools, 100+ subjects |
| BrowseComp | 78.4% | Outperforms GPT-5.2 Pro |
| WideSearch | — | Outperforms Claude Opus 4.5 |
| Seal-0 | 57.5% | Agent evaluation |

## Model Comparison

### Kimi K2.5 vs K2 vs K1.5

| Feature | K2.5 | K2 | K1.5 |
|---------|------|-----|------|
| Architecture | MoE 1T/32B | MoE 1T/32B | Dense |
| Context | 256K / 2M | 128K | 128K |
| Training Tokens | 15T (multimodal) | 15T | — |
| Reasoning | Strong | Strong | Excellent (Long-CoT) |
| Vision | Native | Native | Text-only |
| Agent Swarm | Yes | No | No |
| Release | Jan 2026 | Jul 2025 | Jan 2025 |

### Comparison with Competitors

| Model | Provider | Context | Key Strength |
|-------|----------|---------|--------------|
| Kimi K2.5 | Moonshot | 2M | Long context, cost-efficiency |
| Claude Opus 4.5 | Anthropic | 200K | Reasoning, safety |
| GPT-4o | OpenAI | 128K | General capabilities |
| DeepSeek-R1 | DeepSeek | 64K | Open source, reasoning |
| Qwen3-Next | Alibaba | 128K | Chinese language |

## Inference Specifications

### Latency Targets

| Metric | Target | Typical |
|--------|--------|---------|
| Time to First Token (TTFT) | <500ms | 350ms |
| Inter-token Latency | <50ms | 30ms |
| Throughput | — | 50 tokens/s |

### Memory Requirements

| Context | VRAM Required (FP16) | VRAM Required (INT4) |
|---------|---------------------|---------------------|
| 4K | 80GB | 40GB |
| 32K | 160GB | 80GB |
| 128K | 320GB | 160GB |
| 256K | 640GB | 320GB |

### Batch Processing

| Batch Size | Max Context | Throughput |
|------------|-------------|------------|
| 1 | 2M | 20 tokens/s |
| 8 | 256K | 100 tokens/s |
| 32 | 32K | 300 tokens/s |

## Training Details

### Kimi K2.5 Training

```yaml
Pre-training Data: 15 trillion tokens (mixed visual + text)
Architecture: MoE 1T total, 32B active
Expert Count: 384 (select 8 per token)
Attention: Multi-head Latent Attention
Vision: MoonViT encoder (400M params)
Quantization: Native INT4 with QAT
Training Stages:
  1. Vision-Language Pretraining
  2. Cooldown Phase
  3. Context Activation
  4. RL Fine-tuning (for agent capabilities)
```

### Long Context Training

- Continual pretraining with position interpolation
- 256K context achieved through:
  - RoPE base frequency adjustment
  - NTK-aware scaling
  - YaRN (Yet another RoPE extension method)

## Deployment Recommendations

### Hardware Requirements

| Scale | GPU | Memory | Notes |
|-------|-----|--------|-------|
| Research/Testing | 1x A100 80GB | 80GB | INT4 quantization required |
| Production (small) | 4x A100 80GB | 320GB | Tensor parallelism |
| Production (large) | 8x H100 80GB | 640GB | Full 256K context |

### Optimization Techniques

1. **Quantization**: Native INT4 (QAT) for 2x speed
2. **Tensor Parallelism**: Split across 4-8 GPUs
3. **Pipeline Parallelism**: For multi-node deployment
4. **Continuous Batching**: vLLM/PagedAttention
5. **KV Cache Compression**: MLA reduces memory by 80%

---

*Specifications as of March 2026 | Subject to change with model updates*
