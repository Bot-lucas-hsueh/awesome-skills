## § 10 · Common Pitfalls

### Pitfall 1: Annotating to the Likely Intent, Not the Actual Content


❌ **BAD:** Text: "The bank was steep." → Labels "bank" as FIN (financial institution) because annotator assumes financial context from surrounding sentences

✅ **GOOD:** Read the token in its literal context. "Bank" in "steep bank" = geographic feature (GPE or O depending on schema), not FIN. Always annotate what is present, not what you infer the author meant.

**Why it matters:** Inference-based annotation teaches models to hallucinate entity meanings; ambiguous word sense disambiguation requires exact literal annotation as ground truth.

---

### Pitfall 2: Loose Bounding Boxes to Save Time


❌ **BAD:** Drawing bbox with 20-pixel margin on all sides "just to be safe" → IoU = 0.72 → fails quality threshold → must redo

✅ **GOOD:**
```
Tight bbox checklist before submitting:
□ Top: touching topmost visible pixel of object
□ Bottom: touching bottommost visible pixel
□ Left: touching leftmost visible pixel
□ Right: touching rightmost visible pixel
□ No more than 2-pixel margin on any side for standard objects

Verify with zoom: zoom to 200% and check each edge
```

**Why it matters:** Loose bboxes degrade object detector precision; models trained on loose annotations have higher false positive rates at inference time.

---

### Pitfall 3: Skipping Small or Difficult Instances


❌ **BAD:** Image has 12 cars, 2 in background that are very small (15×10 pixels) → annotator labels the 10 obvious cars → misses 2 small ones

✅ **GOOD:**
```python
# Completeness check protocol:
# 1. First pass: scan entire image systematically (grid pattern)
# 2. Check guidelines: minimum size threshold for annotation
#    (e.g., "annotate if ≥10px in smallest dimension")
# 3. Label all instances meeting threshold, including difficult ones
# 4. Annotate small instances with reduced confidence if guidelines allow
#    (e.g., add attribute: {"difficult": true, "truncated": false})
```

**Why it matters:** False negatives (missed instances) directly reduce model recall; a model that misses 20% of small objects in training data misses ~20% in production too.

---

### Pitfall 4: Inconsistent Sentiment Calibration Across Session


❌ **BAD:**
- Morning: "The product is okay, but could be better" → NEUTRAL
- Afternoon (fatigue): "The product is okay, but could be better" → NEGATIVE
- Same text, different label = label noise

✅ **GOOD:**
```
Self-calibration protocol every 2 hours:
1. Re-read the scale definitions: Positive/Negative/Neutral criteria
2. Re-annotate 5 calibration examples from your personal calibration set
3. If any differ from your morning annotation: stop and review
4. Write "DRIFT CHECK at [time]: [result]" in your session log
```

**Why it matters:** Intra-annotator inconsistency is often larger than inter-annotator inconsistency for long sessions; it can't be detected by standard IAA measurement.

---

### Pitfall 5: Not Flagging Genuinely Ambiguous Cases


❌ **BAD:** Annotator is 50/50 on a classification → picks one arbitrarily → doesn't flag → inconsistency baked into dataset with no way to identify

✅ **GOOD:**
```
Flag protocol for ambiguous cases:
1. If confidence < 70%: add flag with note explaining the ambiguity
2. Write: [FLAG: "Entity span unclear — 'Federal Reserve Bank' could be ORG or
           a compound of ORG+ORG. Applied larger span rule. Needs guideline clarification."]
3. Submit the annotation WITH the flag — don't leave it blank
4. Reviewer resolves; if novel: guideline gets updated
```

**Why it matters:** Flagged ambiguity becomes guideline improvement; unflagged ambiguity becomes noise. Over 1,000 examples, 50 unresolved ambiguities create ~500 inconsistent labels.

---

### Pitfall 6: Treating Annotation as Mechanical (Not Judgment Work)


❌ **BAD:** Annotating on autopilot — applying pattern matching without actively reading → misses context-dependent entities, misclassifies ambiguous sentiment

✅ **GOOD:** Data annotation is expert judgment work disguised as repetitive tasks. Each example requires:
```
Active reading → guideline matching → conscious decision → quality self-check
```

Not:
```
Pattern recognition → click → next
```

Active reading means: re-read the full context for each entity before tagging, not just the word itself.

**Why it matters:** The quality ceiling of any AI model trained on your data is set by the quality of your judgment. Mechanical annotation produces mechanical models.

---

