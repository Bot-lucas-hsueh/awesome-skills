# NVIDIA Performance Benchmarks & Targets

## GPU Performance Specifications

### Peak Compute (TFLOPS)

| GPU | FP64 | FP32 | FP16/BF16 Tensor | FP8 Tensor | FP4 Tensor |
|-----|------|------|------------------|------------|------------|
| A100 | 9.7 | 19.5 | 312 | - | - |
| H100 SXM | 34 | 67 | 989 | 1,980 | - |
| H200 SXM | 34 | 67 | 989 | 1,980 | - |
| B200 | 37 | 75 | 2,200 | 4,500 | 9,000 |
| B300 | 37 | 75 | 2,200 | 4,500 | 15,000-18,000 |

### Memory Specifications

| GPU | Memory | Bandwidth | Bandwidth Efficiency Target |
|-----|--------|-----------|----------------------------|
| A100 | 80GB HBM2e | 2.0 TB/s | 70% (1.4 TB/s effective) |
| H100 | 80GB HBM3 | 3.35 TB/s | 75% (2.5 TB/s effective) |
| H200 | 141GB HBM3e | 4.8 TB/s | 75% (3.6 TB/s effective) |
| B200 | 192GB HBM3e | 8.0 TB/s | 80% (6.4 TB/s effective) |
| B300 | 288GB HBM3e | 8.0 TB/s | 80% (6.4 TB/s effective) |

## LLM Inference Benchmarks

### Throughput (tokens/sec) - Llama 2 70B

| Configuration | FP16 | FP8 | FP4 | Notes |
|--------------|------|-----|-----|-------|
| 1× H100 | 45 | 80 | - | TensorRT-LLM |
| 1× H200 | 70 | 130 | - | 2× batch vs H100 |
| 1× B200 | 150 | 280 | 520 | 5th Gen Tensor Cores |
| DGX H100 (8×) | 360 | 640 | - | Tensor Parallel=8 |
| DGX B200 (8×) | 1,200 | 2,240 | 4,160 | 15× vs DGX H100 |

### Latency (ms/token) - 70B Model

| Target | Batch | GPU | Configuration | Latency |
|--------|-------|-----|---------------|---------|
| Interactive | 1 | B200 | TensorRT-LLM FP8 | 12ms |
| Interactive | 8 | B200 | Continuous batching | 15ms |
| Throughput | 64 | B200 | Max batch | 45ms |
| Real-time | 1 | B200 | Speculative decoding | 6ms |

## Training Performance

### LLM Training (tokens/sec per GPU)

| Model Size | GPUs | H100 FP8 | B200 FP8 | Speedup |
|------------|------|----------|----------|---------|
| 7B | 8 | 4,200 | 9,500 | 2.3× |
| 70B | 64 | 3,800 | 8,800 | 2.3× |
| 405B | 512 | 3,200 | 7,500 | 2.3× |
| 1T | 1,024 | 2,800 | 6,800 | 2.4× |

### Scaling Efficiency

| Scale | Topology | Target Efficiency | Realistic |
|-------|----------|-------------------|-----------|
| 8 GPUs | NVLink domain | 98% | 95-98% |
| 64 GPUs | 8 nodes, IB | 95% | 90-95% |
| 256 GPUs | 32 nodes, IB fat-tree | 92% | 85-92% |
| 1,024 GPUs | 128 nodes, IB dragonfly | 88% | 80-88% |
| 10,000+ GPUs | Multiple pods | 80% | 70-80% |

## Optimization Targets

### GPU Utilization

| Metric | Target | Warning | Critical |
|--------|--------|---------|----------|
| SM Utilization | >85% | 70-85% | <70% |
| Memory Utilization | >80% | 60-80% | <60% |
| Tensor Core Utilization | >70% | 50-70% | <50% |
| PCIe Bandwidth | >80% | 60-80% | <60% |

### Memory Bandwidth

```
Effective Bandwidth = (Bytes Read + Bytes Written) / Kernel Time
Target: >80% of theoretical peak
```

| Access Pattern | Efficiency | Optimization |
|----------------|------------|--------------|
| Fully Coalesced | 90-95% | Optimal |
| Mostly Coalesced | 70-90% | Check alignment |
| Strided | 30-70% | Reorder loops, use shared memory |
| Random | 5-30% | Reorganize data structure |

### Occupancy

| Scenario | Target Occupancy | Registers/Thread |
|----------|------------------|------------------|
| Compute-bound | 50-70% | 128-255 |
| Memory-bound | 70-90% | 64-128 |
| Balanced | 70% | 96-128 |

## Power & Thermal

### TDP Specifications

| GPU | TDP | Typical Power | Thermal Solution |
|-----|-----|---------------|------------------|
| H100 SXM | 700W | 650-700W | Liquid cooling |
| H200 SXM | 700W | 650-700W | Liquid cooling |
| B200 | 1000W | 900-1000W | Liquid cooling required |
| B300 | 1200-1400W | 1100-1300W | Advanced liquid cooling |

### Power Capping

```bash
# Set power limit to 80% of TDP
nvidia-smi -pl 560  # For H100 700W TDP

# Monitor power
dcgm-exporter  # Prometheus metrics
```

## Networking Performance

### NVLink

| Generation | Per-Link BW | Links/GPU | Total BW |
|------------|-------------|-----------|----------|
| NVLink 3 | 50 GB/s | 12 | 600 GB/s |
| NVLink 4 | 100 GB/s | 18 | 900 GB/s |
| NVLink 5 | 100 GB/s | 18 | 1,800 GB/s |

### InfiniBand

| Generation | Per-Port BW | Typical Config | Node BW |
|------------|-------------|----------------|---------|
| HDR | 200 Gbps | 2 ports | 400 Gbps |
| NDR | 400 Gbps | 2-4 ports | 800-1600 Gbps |
| XDR | 800 Gbps | 2-4 ports | 1.6-3.2 Tbps |

### NCCL AllReduce Bandwidth

| GPUs | Topology | Theoretical | Achievable | Efficiency |
|------|----------|-------------|------------|------------|
| 8 | NVLink domain | 900 GB/s | 850 GB/s | 94% |
| 16 | 2 nodes, NVLink+IB | 450 GB/s | 380 GB/s | 84% |
| 64 | 8 nodes, IB fat-tree | 225 GB/s | 180 GB/s | 80% |

## Real-World Workload Benchmarks

### Deep Learning Training

| Workload | Framework | GPUs | Time | Config |
|----------|-----------|------|------|--------|
| GPT-3 175B | Megatron-LM | 1,024 H100 | 24 days | FP8, TP=8, PP=16, DP=8 |
| GPT-3 175B | Megatron-LM | 512 B200 | 10 days | FP8, TP=8, PP=8, DP=8 |
| ResNet-50 | PyTorch | 8 H100 | 3.5 min | Mixed precision |
| BERT-Large | TensorFlow | 64 H100 | 18 min | FP16, XLA |

### Inference Serving

| Model | Batch Size | Throughput | Latency P99 | GPUs |
|-------|------------|------------|-------------|------|
| GPT-4 class (1.8T) | 64 | 2,000 tok/s | 50ms | 8× B200 |
| Claude-3 class | 128 | 5,000 tok/s | 35ms | 8× B200 |
| Llama 3 70B | 256 | 12,000 tok/s | 25ms | 4× B200 |
| CodeLlama 34B | 512 | 25,000 tok/s | 15ms | 2× B200 |

---

*Reference: NVIDIA Datasheets, MLPerf Benchmarks, Published Research Papers*
