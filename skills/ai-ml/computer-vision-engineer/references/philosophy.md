## § 4 · Core Philosophy

### 4.1 CV System Architecture

```
┌─────────────────────────────────────────┐
│         Application Layer               │  ← Detection, tracking, analysis
├─────────────────────────────────────────┤
│         Post-Processing                 │  ← NMS, tracking, filtering
├─────────────────────────────────────────┤
│         Deep Learning Model             │  ← YOLO, DETR, SAM
├─────────────────────────────────────────┤
│         Inference Engine                │  ← TensorRT, ONNX Runtime
├─────────────────────────────────────────┤
│         Pre-Processing                  │  ← Resize, normalize, augment
└─────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Data Quality First** — Clean, diverse, representative data beats complex models
2. **Measure in Real Conditions** — Lab accuracy ≠ real-world performance
3. **Optimize for Deployment** — Model compression is part of the job
4. **Temporal Consistency** — Video requires tracking and smoothing
5. **Privacy by Design** — Handle visual data with care and consent

---
