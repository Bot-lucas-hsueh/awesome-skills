# DeepSeek-V3 Technical Report

> **Source:** DeepSeek-AI, December 2024  
> **arXiv:** https://arxiv.org/abs/2412.19437  
> **Model:** 671B parameters, 37B activated per token

---

## Executive Summary

DeepSeek-V3 is a strong Mixture-of-Experts (MoE) language model with **671B total parameters** and **37B activated for each token**. It achieves performance comparable to leading closed-source models while requiring only **2.788M H800 GPU hours** for full training (~$5.576M).

### Key Innovations

1. **Multi-Head Latent Attention (MLA)** — 93% KV cache reduction
2. **DeepSeekMoE** — Auxiliary-loss-free load balancing
3. **FP8 Mixed Precision** — First validated at 671B scale
4. **Multi-Token Prediction** — Enhanced data efficiency

---

## Architecture Details

### 1. Multi-Head Latent Attention (MLA)

**Problem:** Standard Multi-Head Attention (MHA) requires storing Key and Value caches that grow linearly with sequence length.

**Solution:** Low-rank compression of Key-Value representations.

```
Standard MHA per layer:
  KV cache = 2 × n_layers × n_heads × d_head × seq_len × batch_size
  
MLA compression:
  1. Compress hidden state to latent vector c_t = W_DKV · h_t
  2. Store only latent vector (much smaller)
  3. Reconstruct K,V on-the-fly during attention
  4. Decouple RoPE for position encoding
```

**Mathematical Formulation:**

```
Given hidden state h_t at position t:

Step 1: Compression
  c_t^KV = W_DKV · h_t
  where W_DKV ∈ R^(d_c × d), d_c << d

Step 2: Key/Value reconstruction  
  k_t^C = W_UK · c_t^KV
  v_t = W_UV · c_t^KV
  where W_UK, W_UV ∈ R^(d × d_c)

Step 3: Decoupled RoPE for position
  k_t^R = RoPE(W_KR · h_t)
  where W_KR ∈ R^(d_h^R × d)

Step 4: Combined key for attention
  k_t = [k_t^C; k_t^R]  (concatenate content and position)
  
KV Cache Comparison:
  Standard: 2 × n_h × d_h × L × B  (grows with heads)
  MLA: 2 × d_c × L × B  (fixed small compression dimension)
```

**Result:** 14× KV cache reduction (93% memory savings)

### 2. DeepSeekMoE Architecture

**Design Principles:**
- Use shared experts to capture common knowledge across tasks
- Use routed experts to capture specialized knowledge
- Fine-grained expert segmentation for better specialization

**Expert Configuration:**
```
Total routed experts: N_r = 256
Shared experts: N_s = 1 (always active)
Activated routed experts per token: K_r = 8

Total parameters: 671B
Activated parameters: N_s·d_ffn + K_r·(d_ffn/N_exp) ≈ 37B
Activation rate: 37/671 ≈ 5.5%
```

**Auxiliary-Loss-Free Load Balancing:**

Traditional MoE uses auxiliary loss for load balancing, which degrades performance. DeepSeek introduces bias-term-based balancing:

```
Routing score with load-balancing bias:
  s_i = Softmax_i(u + b)
  where u = expert affinity scores
  b = learnable bias terms for load balancing
  
Bias update (during training):
  if expert i is overloaded: decrease b_i
  if expert i is underloaded: increase b_i
```

This eliminates auxiliary loss while maintaining balanced expert utilization.

**Device-Limited Routing:**
- Limits routed experts to at most M devices
- Reduces communication overhead in distributed training
- M = 4 in DeepSeek-V3 configuration

### 3. FP8 Mixed Precision Training

**FP8 Format Selection:**
- **E4M3 (4-bit exponent, 3-bit mantissa):** Forward pass activations
- **E5M2 (5-bit exponent, 2-bit mantissa):** Backward pass gradients

**Implementation Strategy:**
```
1. Master weights stored in BF16
2. Forward pass: Cast to FP8-E4M3 for GEMM
3. Backward pass: Cast gradients to FP8-E5M2
4. Weight updates: Computed in BF16 precision
5. Optimizer states: Stored in BF16
```

**Per-Tensor Scaling:**
- Dynamic scaling factors for each tensor
- Prevents underflow/overflow in FP8 range
- Scaling updated per iteration based on gradient statistics

**DeepSeek-V3 Validation:**
- First successful FP8 training at 671B parameter scale
- Zero accuracy degradation vs BF16 baseline
- 1.2× training speedup
- Significant memory savings

### 4. Multi-Token Prediction (MTP)

**Objective:** Predict D additional tokens at each position for better data efficiency.

```
Standard: Predict token t+1 given t
MTP (D=2): Predict tokens t+1, t+2 given t

Architecture:
  Main model outputs: h_t
  MTP module 1: h_t → h_t^(1) → predict token t+2
  MTP module 2: h_t^(1) → h_t^(2) → predict token t+3
  
Loss: L_main + λ_1·L_MTP1 + λ_2·L_MTP2
```

**Benefits:**
- Improved data efficiency
- Better representation learning
- Enables speculative decoding at inference

---

## Training Details

### Training Data

| Property | Value |
|----------|-------|
| Total tokens | 14.8 trillion |
| Language mix | English + Chinese + multilingual |
| Data ratio | Web, code, math carefully balanced |
| Quality filtering | Multi-stage deduplication and filtering |

### Training Infrastructure

| Property | Value |
----------|-------|
| GPUs | 2,048 NVIDIA H800 |
| GPU hours | 2.788M for full training |
| Duration | ~55 days |
| Framework | HAI-LLM (in-house) |
| Parallelism | Expert, data, and pipeline parallelism |
| Communication | Optimized all-to-all for MoE routing |

### Training Stability

**Remarkable achievement:**
- Zero irrecoverable loss spikes
- Zero training rollbacks
- Smooth convergence throughout 14.8T tokens

This validates the robustness of FP8 training at extreme scale.

### Training Cost Breakdown

| Phase | GPU Hours | Cost (est.) |
|-------|-----------|-------------|
| Pre-training | 2.664M | ~$5.32M |
| Long-context | 0.119M | ~$0.24M |
| Fine-tuning | 0.005M | ~$0.01M |
| **Total** | **2.788M** | **~$5.576M** |

*Note: Cost estimates assume $2/H800 GPU hour. Excludes R&D, salaries, infrastructure.*

---

## Benchmark Results

### English Benchmarks

| Benchmark | Metric | DeepSeek-V3 | GPT-4o | Claude-3.5 |
|-----------|--------|-------------|--------|------------|
| MMLU | EM | 88.5% | 87.2% | 88.7% |
| MMLU-Redux | EM | 89.1% | — | — |
| MMLU-Pro | EM | 75.9% | — | — |
| DROP | F1 | 91.6% | 83.4% | 88.3% |
| ARC-Easy | EM | 97.4% | 98.4% | 97.9% |
| ARC-Challenge | EM | 95.3% | 94.6% | 95.8% |
| HellaSwag | EM | 89.6% | 89.2% | 90.5% |
| WinoGrande | EM | 86.6% | 87.0% | 87.5% |
| RACE-High | EM | 75.0% | 76.5% | 78.6% |
| RACE-Middle | EM | 92.1% | 91.9% | 92.5% |
| GPQA | EM | 59.1% | 53.6% | 59.4% |
| SimpleQA | EM | 24.9% | 39.0% | 28.4% |
| FRAMES | Acc | 73.3% | 80.5% | 72.5% |

### Coding Benchmarks

| Benchmark | Metric | DeepSeek-V3 | GPT-4o | Claude-3.5 |
|-----------|--------|-------------|--------|------------|
| HumanEval | Pass@1 | 92.0% | 90.2% | 92.0% |
| MBPP | Pass@1 | 87.4% | 87.2% | 86.3% |
| LiveCodeBench | Pass1-COT | 36.3% | 33.4% | 32.8% |
| SWE-Bench | Resolved | N/A | N/A | N/A |

### Math Benchmarks

| Benchmark | Metric | DeepSeek-V3 | GPT-4o | Claude-3.5 |
|-----------|--------|-------------|--------|------------|
| GSM8K | EM | 90.0% | 92.9% | 92.6% |
| MATH | EM | 75.7% | 76.6% | 78.3% |
| MGSM | EM | 77.6% | 85.2% | 84.1% |
| CMATH | EM | 91.8% | — | — |

### Chinese Benchmarks

| Benchmark | Metric | DeepSeek-V3 | Qwen2.5 |
|-----------|--------|-------------|---------|
| C-Eval | EM | 86.5% | 86.1% |
| CMMLU | EM | 90.0% | 89.5% |
| C-SimpleQA | EM | 64.8% | 61.6% |

---

## Key Achievements

1. **Cost Efficiency:** 10× cheaper than GPT-4-level models
2. **Open Source:** MIT license, full weights available
3. **Technical Innovation:** First FP8 at 671B, MLA invention
4. **Performance:** Matches GPT-4o and Claude-3.5 on most benchmarks
5. **Training Stability:** No loss spikes or rollbacks

---

## References

- DeepSeek-V3 Technical Report: https://arxiv.org/abs/2412.19437
- HuggingFace: https://huggingface.co/deepseek-ai/DeepSeek-V3
- GitHub: https://github.com/deepseek-ai/DeepSeek-V3
