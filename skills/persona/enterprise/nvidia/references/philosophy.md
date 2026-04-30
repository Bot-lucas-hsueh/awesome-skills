## § 4 · Core Philosophy

### 4.1 NVIDIA Accelerated Computing Stack

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  LAYER 5: AI FACTORIES & APPLICATIONS                                       │
│  ChatGPT, Claude, Gemini, Autonomous Vehicles, Drug Discovery               │
├─────────────────────────────────────────────────────────────────────────────┤
│  LAYER 4: FRAMEWORKS & MODELS                                               │
│  PyTorch, JAX, TensorFlow, NeMo, Megatron-LM, vLLM                          │
├─────────────────────────────────────────────────────────────────────────────┤
│  LAYER 3: OPTIMIZATION & DEPLOYMENT                                         │
│  TensorRT-LLM, CUDA Graphs, Triton Inference Server, NVFlare                │
├─────────────────────────────────────────────────────────────────────────────┤
│  LAYER 2: LIBRARIES & RUNTIME                                               │
│  cuDNN, cuBLAS, cuFFT, NCCL, cuDNN, CUTLASS, NVSHMEM                       │
├─────────────────────────────────────────────────────────────────────────────┤
│  LAYER 1: GPU ARCHITECTURE                                                  │
│  CUDA Cores, Tensor Cores (4th/5th Gen), RT Cores, NVLink 5                 │
├─────────────────────────────────────────────────────────────────────────────┤
│  LAYER 0: SILICON & SYSTEMS                                                 │
│  Blackwell/Hopper GPUs, Grace CPU, BlueField DPU, NVLink Switch             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 GPU Architecture Specifications (2025)

| GPU | H100 SXM | H200 SXM | B200 | B300/Ultra |
|-----|----------|----------|------|------------|
| **Architecture** | Hopper | Hopper | Blackwell | Blackwell Ultra |
| **Process** | TSMC 4N | TSMC 4N | TSMC 4NP | TSMC 4NP |
| **Transistors** | 80B | 80B | 208B (2x reticle) | 208B (2x reticle) |
| **Tensor Cores** | 4th Gen | 4th Gen | 5th Gen | 5th Gen Enhanced |
| **FP64** | 34 TFLOPS | 34 TFLOPS | 37 TFLOPS | 37 TFLOPS |
| **FP32** | 67 TFLOPS | 67 TFLOPS | 75 TFLOPS | 75 TFLOPS |
| **FP16/BF16 Tensor** | 989 TFLOPS | 989 TFLOPS | 2.2 PFLOPS | 2.2 PFLOPS |
| **FP8 Tensor** | 1.98 PFLOPS | 1.98 PFLOPS | 4.5 PFLOPS | 4.5 PFLOPS |
| **FP4 Tensor** | - | - | 9 PFLOPS (18 sparse) | 15-18 PFLOPS (20 sparse) |
| **Memory** | 80 GB HBM3 | 141 GB HBM3e | 192 GB HBM3e | 288 GB HBM3e |
| **Bandwidth** | 3.35 TB/s | 4.8 TB/s | 8 TB/s | 7.7-8 TB/s |
| **NVLink** | 900 GB/s | 900 GB/s | 1.8 TB/s | 1.8 TB/s |
| **TDP** | 700W | 700W | 1000W | 1200-1400W |
| **Transformer Engine** | Gen 1 | Gen 1 | Gen 2 (FP4) | Gen 2 Enhanced |

### 4.3 Jensen Huang Leadership Principles

| Principle | Practice |
|-----------|----------|
| **First-Principles Thinking** | Deconstruct to physics truth. Ask: "Given today's conditions, how would we reinvent this?" |
| **Intellectual Honesty** | Admit mistakes openly. Learn rapidly. No blame, only learning. |
| **Flat Organization** | 60+ direct reports. No 1:1 meetings. Transparent, information-rich environment. |
| **Mission-Driven** | "Accelerate computing to solve the unsolvable." Every decision serves this. |
| **Resilience & Grit** | "No pain, no gain." Embrace challenges. Persistence through setbacks. |
| **Continuous Learning** | Be a perpetual student. Technology moves fast; move faster. |
| **Empowerment** | Hire the best, give them autonomy, hold them accountable. |

---
