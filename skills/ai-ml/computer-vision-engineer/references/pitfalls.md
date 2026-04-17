## § 9 · Common Pitfalls

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Train/Test Leakage** | Same image in both sets | Strict splits, check for near-duplicates |
| **Ignoring Aspect Ratio** | Distorted images hurt accuracy | Letterboxing, not stretching |
| **Poor Augmentation** | Overfitting to training conditions | Realistic augmentations only |
| **No Hard Negative Mining** | Many false positives | Include hard negatives in training |
| **Skipping Post-Processing** | Raw model output noisy | NMS, tracking, temporal smoothing |
| **Edge Case Neglect** | Fails on unusual inputs | Extensive edge case testing |

---
