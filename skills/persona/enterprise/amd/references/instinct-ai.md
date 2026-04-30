# AMD Instinct AI Accelerators Reference

## Product Roadmap

| Product | Architecture | Launch | Memory | FP8 Perf | Status |
|---------|--------------|--------|--------|----------|--------|
| **MI250X** | CDNA 2 | 2021 | 128GB HBM2e | — | Previous gen |
| **MI300X** | CDNA 3 | 2023 | 192GB HBM3 | 2.6 PF | Shipping |
| **MI325X** | CDNA 3 | 2024 | 256GB HBM3E | 2.6 PF | Shipping |
| **MI350** | CDNA 4 | 2025 | 288GB HBM3e | 5.0 PF | Sampling |
| **MI400** | CDNA 5 | 2026 | 432GB HBM4 | 20 PF | Roadmap |

## MI300X Deep Dive

### Architecture
```
┌─────────────────────────────────────────────┐
│  MI300X Chiplet Architecture                │
│  ┌─────────────────────────────────────┐   │
│  │  8 XCDs (Accelerator Complex Dies)  │   │
│  │  • 38 CUs per XCD                   │   │
│  │  • 4MB L2 per XCD                   │   │
│  │  • 304 CUs total                    │   │
│  └─────────────────────────────────────┘   │
│  ┌─────────────────────────────────────┐   │
│  │  256MB Infinity Cache               │   │
│  │  (11.9 TB/s bandwidth)              │   │
│  └─────────────────────────────────────┘   │
│  ┌─────────────────────────────────────┐   │
│  │  8x HBM3 Stacks (192GB total)       │   │
│  │  5.3 TB/s aggregate bandwidth       │   │
│  └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

### Specifications
| Spec | Value |
|------|-------|
| Process | TSMC 5nm/6nm |
| Transistors | 153 billion |
| Die Size | 3D stack |
| XCDs | 8 compute dies |
| Stream Processors | 19,456 |
| Matrix Cores | 1,216 |
| Memory | 192GB HBM3 |
| Memory Bandwidth | 5.3 TB/s |
| TDP | 750W |

### Performance (Theoretical)
| Precision | Performance |
|-----------|-------------|
| FP64 | 1.3 TFLOPS |
| FP32 | 2.6 TFLOPS |
| TF32 | 5.2 TFLOPS |
| BF16 | 10.4 TFLOPS |
| FP16 | 10.4 TFLOPS |
| FP8 | 20.8 TFLOPS |
| INT8 | 41.6 TOPS |

### MI300X vs NVIDIA H100 Comparison

| Specification | MI300X | H100 SXM | Advantage |
|---------------|--------|----------|-----------|
| **Memory** | 192GB HBM3 | 80GB HBM3 | MI300X: 2.4x |
| **Bandwidth** | 5.3 TB/s | 3.35 TB/s | MI300X: 1.6x |
| **FP8 Perf** | 2.6 PF | 4.0 PF | H100: 1.5x |
| **FP16 Perf** | 1.3 PF | 2.0 PF | H100: 1.5x |
| **TDP** | 750W | 700W | Comparable |
| **Price** | ~$15,000 | ~$30,000 | MI300X: 0.5x |
| **Launch** | Late 2023 | 2022 | — |

### Real-World Performance
| Workload | MI300X | H100 | Notes |
|----------|--------|------|-------|
| Llama 2 70B Inference | 21K tok/s | 21.6K tok/s | H100 slightly faster |
| Large Batch Inference | Better | — | MI300X memory advantage |
| Training (small models) | Comparable | Comparable | ROCm gap |
| Training (large models) | — | Better | CUDA ecosystem maturity |

### Memory Advantage Use Cases
- **Llama 70B FP16**: Fits on single MI300X (140GB+ needed)
- **Mixtral 8x22B**: Single GPU inference possible
- **Batch Processing**: Higher batch sizes without spilling to CPU

## CDNA 4 / MI350 Preview

### Expected Improvements
| Feature | MI300X | MI350 | Improvement |
|---------|--------|-------|-------------|
| Memory | 192GB HBM3 | 288GB HBM3e | 1.5x |
| Bandwidth | 5.3 TB/s | ~8 TB/s | 1.5x |
| FP8 Perf | 2.6 PF | 5.0 PF | 1.9x |
| Architecture | CDNA 3 | CDNA 4 | Next-gen |
| Process | 5nm | 3nm | TSMC N3E |

### CDNA 4 Key Features
- 35x AI performance improvement claim vs CDNA 3
- Enhanced matrix cores for transformers
- Improved sparsity support
- Better FP8/FP4 support

## ROCm Software Stack

### Components
| Component | Purpose |
|-----------|---------|
| **ROCm Core** | GPU driver, runtime |
| **HIP** | CUDA portability layer |
| **MIOpen** | Deep learning primitives |
| **RCCL** | Collective communications |
| **rocFFT/BLAS** | Math libraries |

### Framework Support
| Framework | Status |
|-----------|--------|
| PyTorch | Day-zero support |
| TensorFlow | Day-zero support |
| JAX | Supported |
| vLLM | Optimized for MI300X |
| Triton | AMD backend available |

### Software Gap Analysis
| Area | CUDA | ROCm | Gap |
|------|------|------|-----|
| Ecosystem maturity | 20 years | 7 years | Significant |
| Developer count | 4M+ | Growing | Large |
| Optimized models | 3,000+ | Hundreds | Medium |
| Debugging tools | Excellent | Good | Small |
| Production readiness | Proven | Improving | Medium |

## Customer Deployments

### Hyperscalers
| Customer | Deployment | Scale |
|----------|------------|-------|
| Microsoft Azure | ND MI300X v5 VMs | Production |
| Oracle Cloud | OCI Supercluster | 50,000+ GPUs |
| Meta | Llama inference | 100% of 405B traffic |
| OpenAI | Strategic partnership | 6GW capacity |

### Key Endorsements
- **Microsoft Scott Guthrie**: "Most cost-effective GPU out there"
- **Meta**: MI300X runs 100% of live Llama 405B traffic
- **Oracle**: MI300X is "cornerstone of OCI AI infrastructure"

## Competitive Positioning

### AMD Advantages
1. **Memory Capacity**: 192GB vs 80GB (H100)
2. **Cost**: ~50% price of H100
3. **Open Standards**: No vendor lock-in
4. **Availability**: Better supply than NVIDIA

### NVIDIA Advantages
1. **Software Ecosystem**: CUDA maturity
2. **Raw Compute**: Higher FLOPS
3. **Network**: NVLink, InfiniBand integration
4. **Market Share**: 90%+ installed base

### Market Opportunity
- Total Addressable Market: $500B+ by 2028
- AMD Target: 10-15% share by 2027
- Growth Driver: Inference workloads, cost sensitivity

---

*Source: AMD Advancing AI Events, Product Datasheets, Customer Presentations*
*Last Updated: 2026-03-21*
