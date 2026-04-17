## § 8 · Scenario Examples

### Example 1: Autonomous Vehicle Perception

**Context**: Real-time object detection for self-driving car.

**System**:
```
Architecture:
├── Multi-camera input (8 cameras, 360°)
├── YOLOv8-large for detection
├── DeepSORT for tracking
├── Sensor fusion with LiDAR

Requirements:
├── Latency: < 50ms end-to-end
├── Range: 200m detection
├── Classes: vehicles, pedestrians, cyclists, traffic signs
├── Weather robustness: rain, fog, night

Optimization:
├── TensorRT optimization
├── Multi-GPU pipeline
├── Temporal filtering
```

---

### Example 2: Retail Shelf Analysis

**Context**: Automated inventory counting from camera feeds.

**Solution**:
```
Pipeline:
├── Image capture from fixed cameras
├── Product detection (YOLOv8-small)
├── OCR for price tag reading
├── Stock level estimation
├── Alert generation for restocking

Challenges:
├── Varying lighting conditions
├── Occluded products
├── New product onboarding
└── Real-time processing for 1000+ SKUs
```

---

### Example 3: Medical Image Segmentation

**Context**: Tumor segmentation in CT scans.

**Implementation**:
```
Model: 3D U-Net with attention
├── Pre-trained on public datasets
├── Fine-tuned on hospital data
├── Uncertainty quantification

Validation:
├── Dice coefficient: 0.89
├── Inter-rater agreement with radiologists
├── Regulatory compliance (FDA)

Deployment:
├── On-premise (privacy)
├── Integration with PACS system
├── Radiologist review workflow
```

---

### Example 4: Industrial Quality Inspection

**Context**: Defect detection on manufacturing line.

**System**:
```
Setup:
├── High-speed camera (1000 FPS)
├── Consistent lighting enclosure
├── YOLOv8-nano for speed
├── Edge deployment (NVIDIA Jetson)

Performance:
├── Detection rate: 99.7%
├── False positive rate: 0.1%
├── Latency: < 10ms
├── Throughput: 100 parts/second
```

---

### Example 5: Document OCR Pipeline

**Context**: Automated document processing for invoices.

**Pipeline**:
```
Stages:
├── Document detection and deskewing
├── Layout analysis (text blocks, tables)
├── OCR with PaddleOCR
├── Field extraction (regex + LLM)
├── Data validation

Optimization:
├── Batch processing for throughput
├── GPU acceleration for OCR
├── Confidence thresholding
├── Human review queue for low confidence
```

---
