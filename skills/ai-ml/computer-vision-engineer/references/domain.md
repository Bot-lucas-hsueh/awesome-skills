## § 6 · Domain Knowledge

### 6.1 Model Selection for Detection

| Model | Speed (FPS) | mAP | Best For |
|-------|-------------|-----|----------|
| **YOLOv8-nano** | 1000+ | 37.3 | Edge, real-time |
| **YOLOv8-small** | 500 | 44.9 | Mobile, fast |
| **YOLOv8-medium** | 250 | 50.2 | Balanced |
| **YOLOv8-large** | 150 | 52.9 | Accuracy |
| **DETR** | 30 | 42.0 | Complex scenes |

### 6.2 Optimization Techniques

| Technique | Speedup | Accuracy Loss | When to Use |
|-----------|---------|---------------|-------------|
| **INT8 Quantization** | 2-4× | 1-2% | Edge deployment |
| **FP16 Mixed** | 2× | < 1% | GPU inference |
| **Pruning** | 2-3× | 2-5% | Model too large |
| **Distillation** | 2-4× | 1-3% | Train smaller model |
| **TensorRT** | 5-10× | Minimal | NVIDIA GPUs |

### 6.3 Evaluation Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| **mAP** | Mean Average Precision | > 0.50 for production |
| **IoU** | Intersection over Union | > 0.75 for tight boxes |
| **FPS** | Frames per second | > 30 for real-time |
| **F1** | Precision-Recall balance | Use when class imbalance |

---
