# AI Chip Comparison: Ascend vs NVIDIA

## Overview

This reference compares Huawei's Ascend AI chip series with NVIDIA's offerings, particularly relevant given US sanctions and the push for domestic AI training capabilities in China.

## Chip Specifications

### Training Chips

| Spec | NVIDIA H100 | NVIDIA H200 | Ascend 910B | Ascend 910C | Ascend 910D |
|------|-------------|-------------|-------------|-------------|-------------|
| **Process** | 4nm TSMC | 4nm TSMC | 7nm SMIC | 7nm SMIC | 7nm SMIC |
| **FP16 TFLOPS** | 989 | 989 | ~400 | ~650 | ~800 |
| **BF16 TFLOPS** | 989 | 989 | ~400 | ~650 | ~800 |
| **FP8 TFLOPS** | 1,979 | 3,958 | Limited | ~1,200 | ~1,500 |
| **Memory** | 80GB HBM3 | 141GB HBM3e | 64GB HBM2e | 96GB HBM3 | 128GB HBM3 |
| **Memory BW** | 3.35 TB/s | 4.8 TB/s | 1.6 TB/s | 2.4 TB/s | 3.0 TB/s |
| **TDP** | 700W | 700W | 400W | 450W | 500W |
| **Interconnect** | NVLink 900GB/s | NVLink 900GB/s | HCCS 392GB/s | HCCS 600GB/s | HCCS 800GB/s |

### Inference Chips

| Spec | NVIDIA L40S | NVIDIA H100 | Ascend 310P | Ascend 310B |
|------|-------------|-------------|-------------|-------------|
| **Purpose** | Inference | Training/Inference | Edge Inference | Edge Inference |
| **INT8 TOPS** | 732 | 3,958 | 88 | 160 |
| **FP16 TFLOPS** | 366 | 989 | 44 | 80 |
| **Power** | 350W | 700W | 8W | 15W |

## Cluster Performance

### Supercomputer Scale

| System | NVIDIA DGX H100 | Huawei Atlas 900 |
|--------|-----------------|------------------|
| **Nodes** | 8x H100 per DGX | 8x 910C per node |
| **Interconnect** | NVLink + InfiniBand | HCCS + RoCE |
| **Max Cluster** | 10,000+ GPUs | 4,000+ NPUs |
| **Efficiency** | ~70% at scale | ~85% at scale |
| **Cooling** | Air/Liquid | All-liquid |

## Software Ecosystem

### Framework Support

| Framework | NVIDIA | Huawei Ascend |
|-----------|--------|-----------------|
| **PyTorch** | ✅ Native | ✅ Via adapter |
| **TensorFlow** | ✅ Native | ✅ Via adapter |
| **JAX** | ✅ Native | ⚠️ Limited |
| **MindSpore** | ❌ No | ✅ Native |
| **CANN** | ❌ No | ✅ Native |

### Key Software Components

**NVIDIA:**
- CUDA: Compute platform
- cuDNN: Deep learning primitives
- NCCL: Collective communications
- TensorRT: Inference optimization

**Huawei:**
- CANN (Compute Architecture for Neural Networks): Compute platform
- MindSpore: Native AI framework
- HCCL: Huawei Collective Communication Library
- MindIE: Inference engine

## Real-World Training Results

### Large Language Model Training

| Model | Size | Platform | Time | Efficiency |
|-------|------|----------|------|------------|
| GPT-3 like | 175B | 1,024 H100 | ~8 days | Baseline |
| GPT-3 like | 175B | 2,048 910C | ~12 days | +85% vs baseline chip-for-chip |
| DeepSeek-R1 | 671B | 2,048 910C | ~30 days | Optimized for Ascend |
| iFlytek Spark | 130B | 1,024 910B | ~14 days | Fully domestic |

### Cost Comparison (China market)

| Cost Factor | NVIDIA H100 | Ascend 910C | Advantage |
|-------------|-------------|-------------|-----------|
| **Chip cost** | $30,000+ (gray market) | ~$15,000 | Ascend -50% |
| **Cluster TCO** | Baseline | -30% | Ascend |
| **Availability** | ❌ Restricted | ✅ Domestic | Ascend |
| **Support** | Limited | Full | Ascend |
| **Power cost** | Higher | Lower | Ascend |

## Strategic Implications

### For China Market

**Advantages of Ascend:**
- ✅ No export control restrictions
- ✅ Lower total cost of ownership
- ✅ Better software optimization for Chinese models
- ✅ Local support and customization
- ✅ Data sovereignty compliance

**Challenges:**
- ⚠️ Single-node performance gap vs H100
- ⚠️ Ecosystem maturity (catching up rapidly)
- ⚠️ Some framework features not yet supported
- ⚠️ Memory bandwidth limitation

### Global Context

**US BIS Guidance (May 2025):**
- Warning that Ascend chips "anywhere in the world" may violate US export controls
- Creates legal uncertainty for global deployment
- Accelerates bifurcation of global AI infrastructure

**Market Response:**
- Chinese tech companies increasingly standardizing on Ascend
- Baidu, Alibaba, Tencent, ByteDance all deploying Ascend clusters
- International companies in China evaluating compliance risks

## Future Roadmap

### Huawei Ascend

| Generation | Timeline | Expected Spec |
|------------|----------|---------------|
| 910D | 2025 | 800+ TFLOPS FP16 |
| Next-gen | 2026 | EUV if available, else advanced DUV |
| Future | 2027+ | 3D stacking, chiplet architecture |

### Key Technologies in Development

1. **Chiplet Architecture:** Multi-die integration for higher performance
2. **Advanced Packaging:** CoWoS-like technology for HBM integration
3. **Photonics Interconnect:** Optical connections for scale-out
4. **Sparse Computing:** Hardware support for sparse models

---

## Recommendations

### When to Choose Ascend

✅ **Choose Ascend when:**
- Operating in China market
- Training Chinese-language models
- Cost efficiency is priority
- Supply chain security is critical
- Compliance with data localization required

✅ **Choose NVIDIA when:**
- Global deployment required
- Peak single-chip performance critical
- Ecosystem maturity paramount
- Budget unconstrained
- Access to latest technology assured

---
*Sources: Huawei technical documentation, industry benchmarks, third-party analysis*
*Last Updated: 2026-03-21*
