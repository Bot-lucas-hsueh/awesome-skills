## § 2 — Domain Knowledge

### 2.1 DeepSeek Model Family

| Model | Release | Architecture | Params | Training Cost | Key Innovation |
|-------|---------|--------------|--------|---------------|----------------|
| **DeepSeek-V3** | Dec 2024 | MoE + MLA | 671B / 37B active | $5.576M | First FP8 at extreme scale, aux-loss-free routing |
| **DeepSeek-R1** | Jan 2025 | MoE + GRPO RL | 671B / 37B active | ~$294K | Reasoning rivaling o1, pure RL emergence |
| **DeepSeek-R1-Zero** | Jan 2025 | MoE + pure RL | 671B / 37B active | ~$200K | SFT-free reasoning, self-verification emergence |
| **R1 Distilled** | Jan 2025 | Dense | 1.5B–70B | Synthetic data | 90%+ reasoning at tiny scale |
| **DeepSeek-Coder** | 2024 | Dense/MoE | 1B–33B | Code-focused | Specialized programming tasks |
| **DeepSeek-Math** | 2024 | Dense | Various | 120B math tokens | Advanced mathematical reasoning |

### 2.2 Key Technical Innovations

#### Multi-Head Latent Attention (MLA)

```
Problem: Standard MHA has KV cache growing linearly with sequence length
Solution: Low-rank compression of Key-Value representations

Architecture:
  c_t = W_DKV · h_t                    (compress to latent vector)
  k_t = W_UK · c_t                      (reconstruct key)
  v_t = W_UV · c_t                      (reconstruct value)
  k_R = RoPE(W_KR · h_t)                (decoupled RoPE for position)

Result: KV cache = n × d_c  vs  n × d_h × n_h  (14× reduction = 93% savings)
```

#### DeepSeekMoE Architecture

```
Problem: Dense FFN activates all parameters per token — wasteful
Solution: Sparse expert routing with shared + routed experts

Architecture:
  ┌─────────────────────────────────────┐
  │  Shared Experts (always active)     │ → Capture common knowledge
  │  Routed Experts (top-k selected)    │ → Specialized knowledge
  └─────────────────────────────────────┘
  
  Routing: sigmoid-based, device-limited, aux-loss-free balancing
  
Result: 671B total parameters, only 37B activated per token (5.5%)
```

#### FP8 Mixed Precision Training

```
Problem: BF16 uses 2× memory vs FP8, slower computation
Solution: FP8 matmul with BF16 master weights, validated at scale

Implementation:
  - Forward/backward: FP8 GEMM (E4M3 for forward, E5M2 for backward)
  - Master weights: BF16 (preserves accuracy)
  - Loss scaling: Dynamic per-tensor scaling
  
Result: 1.2× speedup, memory reduction, zero accuracy loss at 671B scale
DeepSeek-V3: First validated FP8 training at extreme scale
```

#### Group Relative Policy Optimization (GRPO)

```
Problem: PPO for RL training requires critic model (2× memory)
Solution: GRPO uses group-relative rewards, no critic needed

Algorithm:
  1. Sample G outputs from old policy for each question
  2. Compute reward for each output
  3. Baseline = mean of group rewards
  4. Policy update maximizes advantage vs baseline

Result: DeepSeek-R1-Zero emerged reasoning via pure RL, no SFT
Phenomena observed: Self-verification, reflection, long CoT emergence
```

### 2.3 Training Infrastructure: Fire-Flyer II

| Component | Specification |
|-----------|---------------|
| GPUs | 10,000+ NVIDIA H800 (China-compliant H100 variant) |
| Efficiency | 96% GPU utilization |
| Tasks Completed | 1.35M+ AI training tasks |
| Framework | HAI-LLM (in-house optimized) |
| Network | High-bandwidth interconnect for MoE all-to-all |

### 2.4 Market Impact

| Event | Date | Impact |
|-------|------|--------|
| DeepSeek-V3 Release | Dec 26, 2024 | GPT-4 parity at $6M cost disclosed |
| DeepSeek-R1 Release | Jan 20, 2025 | o1-level reasoning, MIT license |
| Nvidia Stock Crash | Jan 27, 2025 | -17% (-$589B market cap), worst single-day loss |
| US Tech Rout | Jan 27, 2025 | ~$1T wiped from US tech stocks |
| App Store #1 | Jan 2025 | DeepSeek app tops free charts in 51 countries |
| Meta Reaction | Jan-Feb 2025 | $65B AI investment announced to counter |

---
