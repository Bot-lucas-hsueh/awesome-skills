## § 7 · Standards & Reference

### Annotation Quality Metrics by Task Type

| Task Type / 任务类型 | Primary Metric / 主要指标 | Target / 目标 | Secondary Check
|--------------------|--------------------------|--------------|--------------------------|
| Bounding Box | IoU (Intersection over Union) | ≥ 0.85 | Label accuracy (correct class) |
| Semantic Segmentation | Mean IoU (mIoU) | ≥ 0.80 | Boundary precision |
| Instance Segmentation | AP@0.5 (agreement with gold) | ≥ 0.80 | Instance count accuracy |
| NER | F1 vs gold standard | ≥ 0.90 | Span boundary accuracy |
| Sentiment Classification | Cohen's κ | ≥ 0.75 | Consistency on same-text pairs |
| Relation Extraction | F1 vs gold standard | ≥ 0.85 | Argument span accuracy |
| Audio Transcription | Word Error Rate (WER) | ≤ 5% | Speaker diarization accuracy |
| Video Object Tracking | MOTA (Multi-Object Tracking Accuracy) | ≥ 0.80 | ID consistency across frames |

### Bounding Box Quality Standards

```
Tight bbox rules:
- Top edge: at the topmost pixel of the object
- Include: the entire visible object boundary
- Exclude: cast shadows (unless explicitly required)
- Exclude: motion blur beyond the visible object edge
- Tolerance: ±3 pixels from true boundary for non-critical objects
             ±1 pixel for safety-critical (pedestrians, stop signs)

IoU Calculation:
IoU = Area(Intersection)
    = (pred ∩ gt)

Acceptance thresholds:
  IoU ≥ 0.90: Excellent (autonomous driving, medical imaging)
  IoU ≥ 0.85: Good (general object detection)
  IoU ≥ 0.70: Minimum acceptable (large objects only)
  IoU < 0.70: Reject and redo
```

### NER Annotation Schema Example

```
Standard entity types (PERSON, ORG, GPE, DATE, MONEY, PRODUCT):

ANNOTATION RULES:
1. Span selection: include all core components of the entity
   - ✅ [Apple Inc.]_ORG announced → include "Inc."
   - ❌ [Apple]_ORG Inc. announced → missing legal suffix

2. Nested entities: annotate innermost only unless guidelines specify nested
   - "the [University of California]_ORG [Berkeley]_GPE campus"
   - If nested allowed: tag both; if not: tag the larger span

3. Ambiguous entities: annotate based on context, not surface form
   - "Apple" in technology context → ORG
   - "Apple" in recipe context → not an entity (common noun)

4. Abbreviations: tag if entity, even if abbreviated
   - "[NASA]_ORG" → ORG (not GPE even though a government body)
```

---

