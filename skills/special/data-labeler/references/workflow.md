## § 8 · Standard Workflow

### Phase 1: Pre-Annotation Setup

```
Input: Annotation task assignment + guidelines document
Output: Ready-to-annotate workspace with verified understanding

Steps:
  1.1 Read guidelines completely before starting first example
  1.2 Complete calibration set: annotate 20 gold examples; review corrections
  1.3 Score calibration exam: must achieve ≥80% agreement with gold before production
  1.4 Set up annotation tool: load correct project, verify label schema, test keyboard shortcuts
  1.5 Review task-specific edge case taxonomy if available
  1.6 Set quality target reminder: note IoU/F1 target for this task

[✓ Done] Calibration ≥80%; tool configured; edge case list reviewed
[✗ FAIL] Calibration <70% → review missed cases with senior reviewer; retry before production
```

### Phase 2: Production Annotation

```
Input: Batch of unannotated examples
Output: Annotated batch meeting quality standards

Steps:
  2.1 Process examples systematically — do not skip; mark skipped explicitly
  2.2 For each example:
    (a) Read entire context before labeling (text) or scan full image (CV)
    (b) Identify all instances to label (completeness check)
    (c) Apply labels per guideline
    (d) Flag edge cases with note: [EDGE CASE: description]
  2.3 Self-QA every 50 examples: review last 10; check for drift or systematic errors
  2.4 Track personal stats: labels/hour, flag rate, self-correction rate

[✓ Done] Batch submitted with all edge cases flagged; self-QA passed
[✗ FAIL] Self-QA reveals systematic error → stop, correct affected examples, re-review last 50
```

### Phase 3: Quality Review & Calibration

```
Input: Annotated batch; QA reviewer assignment
Output: Accepted batch or rework feedback with corrections

Steps:
  3.1 Reviewer samples 10% of batch (minimum 50 examples); reviews against gold criteria
  3.2 Calculate batch quality score: accuracy/IoU per example; aggregate batch score
  3.3 If batch passes (score ≥ threshold): accept and mark complete
  3.4 If batch fails: return to annotator with specific error examples and correction guidance
  3.5 Annotator corrects errors; re-submits for re-review
  3.6 Track patterns: if annotator makes same error 3+ times → schedule calibration session

[✓ Done] Batch accepted; quality score documented; patterns recorded
[✗ FAIL] Batch fails second QA → escalate to project lead for guideline review or annotator reassignment
```

### Phase 4: Edge Case Resolution & Guideline Update

```
Input: Accumulated edge case flags from annotators
Output: Updated guidelines with new edge case coverage

Steps:
  4.1 Senior reviewer categorizes flagged edge cases weekly
  4.2 Determine resolution for each: matches existing rule / needs new rule
  4.3 Write new guideline entries for novel cases with clear examples
  4.4 Version-bump guidelines; notify all annotators; schedule 30-min calibration session
  4.5 Retroactively re-label examples that match new guideline (if high-impact category)

[✓ Done] Guidelines updated; annotators calibrated; retroactive relabeling scoped
[✗ FAIL] Edge cases piling up faster than resolutions → reduce batch size; add dedicated reviewer
```

---

