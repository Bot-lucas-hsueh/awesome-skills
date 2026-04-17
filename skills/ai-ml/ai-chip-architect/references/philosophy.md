## § 4 · Core Philosophy

### 4.1 The Roofline Model

```
Performance (FLOPS/sec)
        |
Peak    |──────────────────────────────── (Compute Ceiling)
Compute |                          /
        |                        /
        |                      /
        |
        |
        |                /
        |──────────────────────────────────→ Arithmetic Intensity (FLOPS/byte)
        0              Ridge Point

Ridge Point = Peak GFLOPS / Peak GB/s bandwidth
Example (H100 SXM):
  FP8 compute = 3,958 TFLOPS; HBM3 BW = 3.35 TB/s
  Ridge Point = 3,958 / 3,350 ≈ 1.18 FLOPs/byte

Most inference workloads (batch=1): AI < 0.5 → memory-bound
Training with large batches: AI > 5 → compute-bound
```

**Insight**: Optimize memory access patterns before adding more compute units for inference workloads.

### 4.2 Guiding Principles

1. **Bandwidth First, Compute Second**: Identify the roofline ridge point; do not add MAC units if the model is memory-bound.

2. **Co-design by Default**: Hardware ISA and compiler toolchain must be designed simultaneously; an unccompilable instruction is worthless silicon.

3. **PPA Discipline**: Every decision must state all three dimensions (Power, Performance, Area); optimizing one in isolation is architectural malpractice.

---

