## § 7 · Standard Workflow

### Phase 1: Problem & Data (Days 1-5)

```
├── Define detection/segmentation task
├── Collect and annotate images/videos
├── Analyze class distribution
├── Split train/validation/test
└── [✓ Done]: Dataset ready, annotations validated
    [✗ FAIL]: Insufficient data → collect or use synthetic
```

### Phase 2: Model Development (Days 6-15)

```
├── Select architecture based on speed/accuracy needs
├── Configure training pipeline
├── Train with augmentation
├── Validate and iterate
└── [✓ Done]: Model trained, accuracy acceptable
    [✗ FAIL]: Poor accuracy → more data or different architecture
```

### Phase 3: Optimization & Deployment (Days 16-20)

```
├── Export to deployment format (ONNX, TensorRT)
├── Quantize if edge deployment
├── Optimize preprocessing pipeline
├── Test on target hardware
└── [✓ Done]: Model deployed, meets latency targets
    [✗ FAIL]: Too slow → further optimization or smaller model
```

### Phase 4: Monitoring (Ongoing)

```
├── Track accuracy drift
├── Monitor inference latency
├── Collect failure cases for retraining
├── Regular model updates
└── [✓ Done]: System stable, improving
    [✗ FAIL]: Performance degradation → trigger retraining
```

---
