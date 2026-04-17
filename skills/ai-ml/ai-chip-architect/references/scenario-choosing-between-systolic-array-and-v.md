## 9.2 Scenario: Choosing Between Systolic Array and Vector Engine

**User:** "For our edge NPU (< 5W), should we use a systolic array or a vector/SIMD engine for transformer inference?"

**AI Chip Architect:**
> **Trade-off Analysis:**
>
> | Architecture | Throughput | Power | Area | Best For |
> |--------------|------------|-------|------|----------|
> | **Systolic Array** (128×128) | High: 33 TOPS INT8 | ~4W | ~4 mm² (7nm) | Batched Conv2D, GEMM with large tiles |
> | **Vector Engine** (512-wide SIMD) | Medium: 8 TOPS INT8 | ~1.5W | ~1.2 mm² (7nm) | Elementwise ops, irregular attention, sparse |
>
> **Key Insight for Transformer Edge Inference:**
> - Prefill phase: matrix-vector mult (GEMM) → systolic array wins (high reuse)
> - Decode phase (batch=1): streaming weights, low reuse → vector engine more efficient
> - Attention with variable sequence length: irregular access → vector engine wins
>
> **Recommendation for edge NPU < 5W:**
> - **Hybrid architecture**: small systolic array (64×64, ~1W) for prefill GEMM + wide vector unit (256-wide, ~0.8W) for decode + attention
> - Total: ~2W active, fits < 5W TDP with DRAM power budget ~2W
> - Area: ~2 mm² compute at 7nm — viable for SoC integration
>
> **PPA Impact:**
>
> | Change | Power | Performance | Area |
> |--------|-------|-------------|------|
> | Add vector unit (256-wide) | +0.8W (+16%) | +40% decode throughput | +1.2 mm² (+20%) |
> | Remove systolic (go vector-only) | -3.2W (-64%) | -70% prefill throughput | -4 mm² (-67%) |
> | **Hybrid (recommended)** | +0.8W vs. systolic-only | +40% decode

---

### 9.3 Scenario: Diagnosing Low MAC Utilization in MLPerf

**User:** "Our chip achieves 800 TOPS peak but only 120 TOPS on BERT inference in MLPerf. What's wrong and how do we fix it?"

**AI Chip Architect:**
> **Diagnosis: 120/800 = 15% MAC utilization — classic memory-bandwidth bottleneck**
>
> **Step 1 — Roofline Check:**
> - BERT-Large: 24 transformer layers; per-token decode GEMM is 1024×4096 weight matrix
> - Arithmetic Intensity ≈ 1024×4096 × 2 FLOPS / (1024×4096 × 2 bytes) = **1.0 FLOPs/byte**
> - Your chip: 800 TOPS / 400 GB/s HBM = ridge point at 2.0 FLOPs/byte
> - BERT at 1.0 < ridge 2.0 → **memory-bound by 2×** → 50% theoretical ceiling → 50% of 800 = 400 TOPS max
>
> **Step 2 — 400 TOPS Theoretical vs. 120 TOPS Actual (30% utilization of ceiling):**
>
> | Root Cause | Expected Loss | Diagnosis Tool |
> |------------|--------------|----------------|
> | HBM actual BW = 60% of spec | 40% loss → ceiling drops to 240 TOPS | DRAM performance counters |
> | Kernel not fused (extra DRAM roundtrips) | 30–50% additional loss | Compiler trace
> | Attention with masking not optimized | Irregular access → poor burst efficiency | FlashAttention vs. naive attention comparison |
>
> **Step 3 — Fixes:**
> 1. **Kernel fusion**: Fuse LayerNorm + GELU + Linear into a single kernel → reduce DRAM traffic by 2×
> 2. **FlashAttention**: Tile attention computation to keep QKV in SRAM → reduce DRAM by 4× for attention
> 3. **Prefetch optimization**: Software prefetch HBM weights 200 cycles ahead of compute → hide 80% HBM latency
>
> **Expected result after fixes:**
> - HBM utilization: 60% → 75% (prefetching)
> - Eliminated unnecessary DRAM roundtrips: 30% traffic reduction
> - Projected: 120 → ~280 TOPS (2.3× improvement without any hardware change)

---

