## § 7 · Standards & Reference

### 7.1 CUDA Compute Capability

| Compute | GPUs | Key Features |
|---------|------|--------------|
| 9.0 | H100/H200 | Hopper, FP8 Tensor Cores, DPX instructions, TMA |
| 10.0 | B200/B300 | Blackwell, FP4 Tensor Cores, 5th Gen, NVLink 5 |
| 12.0 | RTX 50-series | Blackwell consumer, DLSS 4, RT Core gen 4 |

### 7.2 NVIDIA Software Versions (2025)

| Software | Version | Key Features |
|----------|---------|--------------|
| CUDA | 12.8+ | Blackwell support, C++20 |
| cuDNN | 9.5+ | Optimized for Blackwell |
| TensorRT | 10.5+ | FP4 support, LLM optimizations |
| NCCL | 2.23+ | NVLink 5, improved collectives |
| Driver | 550+ | Production Blackwell support |

### 7.3 Competition Landscape

| Competitor | Product | Strengths | NVIDIA Advantage |
|------------|---------|-----------|------------------|
| **AMD** | MI350X/MI355X | 288GB memory, FP4, price | CUDA ecosystem, software maturity, optimizations |
| **Google** | TPU v6e (Trillium) | Cloud integration, scale | Flexibility, on-premise, general-purpose |
| **Intel** | Gaudi3 | Price, x86 integration | Raw performance, ecosystem breadth |
| **Amazon** | Trainium2/Inferentia2 | AWS integration | Performance, developer adoption |
| **Cerebras** | WSE-3 | Wafer-scale, memory bandwidth | General availability, ecosystem |

---
