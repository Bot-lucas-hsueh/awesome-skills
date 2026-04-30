# NVIDIA GPU Architecture Deep Dive

## Blackwell Architecture (B200/B300)

### Overview
Blackwell represents NVIDIA's most ambitious GPU architecture, built on TSMC 4NP process. It introduces dual-die design (2 reticle limits) connected via high-speed interconnect, appearing as a single GPU to software.

### Key Innovations

| Feature | B200 | B300/Ultra | Impact |
|---------|------|------------|--------|
| Transistors | 208B | 208B | 2.6× Hopper |
| Die Configuration | 2 dies | 2 dies (enhanced) | Unified memory space |
| Memory | 192GB HBM3e | 288GB HBM3e | 3.6× H100 capacity |
| Memory BW | 8 TB/s | 8 TB/s | 2.4× H100 bandwidth |
| NVLink 5 | 1.8 TB/s | 1.8 TB/s | 2× Hopper |
| FP4 Support | Yes | Yes (enhanced) | 2× throughput vs FP8 |
| Transformer Engine | Gen 2 | Gen 2 Enhanced | Automatic precision scaling |
| TDP | 1000W | 1200-1400W | Liquid cooling recommended |

### Microarchitecture

```
┌─────────────────────────────────────────────────────────────────┐
│  BLACKWELL GPU                                                  │
│  ┌─────────────────┐    ┌─────────────────┐                     │
│  │    GPU Die 0    │◄──►│    GPU Die 1    │  ← NV-HBI (10TB/s) │
│  │  ─────────────  │    │  ─────────────  │                     │
│  │  SMs × 80       │    │  SMs × 80       │                     │
│  │  Tensor Cores   │    │  Tensor Cores   │  ← 5th Gen         │
│  │  L2 Cache 60MB  │    │  L2 Cache 60MB  │                     │
│  │  HBM3e Ctrl     │    │  HBM3e Ctrl     │                     │
│  └─────────────────┘    └─────────────────┘                     │
│           │                      │                              │
│           └──────────┬───────────┘                              │
│                      NVLink 5 (1.8TB/s)                        │
└─────────────────────────────────────────────────────────────────┘
```

### Streaming Multiprocessor (SM)
- 128 CUDA cores per SM
- 4 fourth-gen Tensor Cores (or 5th gen in Blackwell)
- 256KB register file
- 228KB shared memory/L1 cache configurable
- Dedicated FP32, FP64, INT32, LD/ST units

### Memory Subsystem

| Level | Size/SM | Bandwidth | Latency | Purpose |
|-------|---------|-----------|---------|---------|
| Registers | 256KB | ~80 TB/s | 1 cycle | Per-thread data |
| Shared/L1 | 228KB | ~19 TB/s | ~20 cycles | Inter-thread communication |
| L2 Cache | 50MB (H100) / 60MB per die (B200) | 12 TB/s | ~200 cycles | Cross-SM data sharing |
| HBM | 80-288GB | 3.35-8 TB/s | ~400 cycles | Global memory |

### NVLink 5
- 900 GB/s per link
- 2 links per GPU = 1.8 TB/s total
- Cache-coherent memory access across GPUs
- Enables 72-GPU NVLink domains

## Hopper Architecture (H100/H200)

### Key Features
- Transformer Engine (first generation)
- DPX instructions for dynamic programming
- TMA (Tensor Memory Accelerator)
- Thread block clusters
- Distributed shared memory

### H100 vs H200
H200 maintains identical compute to H100 but doubles memory:
- H100: 80GB HBM3 @ 3.35 TB/s
- H200: 141GB HBM3e @ 4.8 TB/s

This makes H200 optimal for:
- Large model inference (bigger KV cache)
- Long-context LLMs
- Memory-bound HPC workloads

## Tensor Core Evolution

| Generation | Arch | Supported Precisions | Peak FP16 |
|------------|------|---------------------|-----------|
| 1st Gen | Volta (V100) | FP16 | 125 TFLOPS |
| 2nd Gen | Turing (T4) | FP16, INT8, INT4 | 65 TFLOPS |
| 3rd Gen | Ampere (A100) | FP64, FP16, BF16, TF32, INT8 | 312 TFLOPS |
| 4th Gen | Hopper (H100) | FP8, FP16, BF16, TF32, FP64 | 989 TFLOPS |
| 5th Gen | Blackwell (B200) | FP4, FP6, FP8, FP16, BF16 | 2.2 PFLOPS |

## Roofline Model

The roofline model guides optimization:
```
Performance = min(Peak FLOPS, Arithmetic Intensity × Peak Bandwidth)
```

For H100:
- Peak FP16: 989 TFLOPS
- Peak HBM Bandwidth: 3.35 TB/s
- Ridge Point: 989/3.35 = ~295 FLOPs/byte

For B200:
- Peak FP16: 2.2 PFLOPS
- Peak HBM Bandwidth: 8 TB/s
- Ridge Point: 2200/8 = ~275 FLOPs/byte

**Optimization Strategy:**
- Below ridge: Memory-bound → Improve locality, tiling
- Above ridge: Compute-bound → Increase parallelism, reduce overhead

---

*Reference: NVIDIA Architecture Whitepapers, GTC 2024/2025 Presentations*
