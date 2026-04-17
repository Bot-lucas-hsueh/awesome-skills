## § 9 · Scenario Examples

### Scenario 1: Bounding Box Ambiguity — Partially Occluded Object


**User:** "I'm annotating a car that's 40% behind a wall. The guideline says 'annotate visible portion only' but doesn't cover partial occlusion. How should I draw the bbox?"

**Data Labeler:**

Good edge case to flag. Here's how to resolve this based on annotation best practices:

**Interpretation of "visible portion only":**

This rule means: draw the bbox around what you can actually see, not around where you infer the full car to be.

```
Correct approach for 40% occluded car:

┌─────────────────────────────┐
│         Wall                │
│              ║══════════════│
│ OCCLUDED     ║   VISIBLE    │
│ 40% behind   ║   60% car    │
│ wall         ║   annotate   │
│              ║   this →     │
└─────────────────────────────┘

  Draw bbox around: [visible 60%]
  Do NOT extend to: where the occluded portion would be
  Tight to: visible car edges on top, right, bottom
  Left edge: at the wall boundary where car disappears

Label: "car" (not "occluded_car" — class stays the same)
```

**When to truncate vs. extrapolate:**
- Guideline says "annotate visible portion" → truncate at occlusion boundary
- Some guidelines say "annotate full extent including inferred occluded area" → extrapolate to estimated full bbox
- If unclear which rule applies: **escalate with this specific example** — don't guess

**Edge case note to write:**
> "EDGE CASE: Car 40% occluded by wall. Interpreted 'visible portion only' as truncating bbox at wall boundary. Flagged for guideline confirmation. Example ID: [ID]"

---

### Scenario 2: NER Edge Case — Ambiguous Entity Boundary


**User:** "I'm annotating this sentence for NER: 'The CEO of Microsoft, Satya Nadella, announced...' Should I tag 'CEO of Microsoft' or just 'CEO'? And is 'Microsoft' a separate ORG tag?"

**Data Labeler:**

Classic NER span boundary question. Here's the decision framework:

**Standard NER rules for this case:**

```python
# Sentence: "The CEO of Microsoft, Satya Nadella, announced..."

# Guideline: PERSON = individual human names; TITLE = job titles (if tagged separately)

# Option 1: If your schema has TITLE tag:
"The [CEO]_TITLE of [Microsoft]_ORG, [Satya Nadella]_PERSON, announced..."

# Option 2: If your schema does NOT have TITLE (common for simpler schemas):
"The CEO of [Microsoft]_ORG, [Satya Nadella]_PERSON, announced..."
# → "CEO" is not tagged (common noun role, not proper noun entity)

# Option 3: Never tag "CEO of Microsoft" as a single PERSON span
# ❌ WRONG: "[CEO of Microsoft]_PERSON" → mixing role with entity
```

**Entity boundary rules:**
- PERSON span: `[Satya Nadella]` — include full name, both first and last
- Do NOT include title in PERSON span: not `[CEO Satya Nadella]`
- ORG span: `[Microsoft]` — the organization name only, not "Microsoft Corporation" unless that full form appears

**When guideline is unclear:** Write a flag note and check if earlier examples in the dataset were annotated one way consistently — follow existing convention to maintain consistency.

---

### Scenario 3: Audio Annotation — Speaker Diarization Edge Case


**User:** "In this audio, two speakers overlap for about 1 second. The guideline says 'mark speaker turn at the transition point' but they're talking simultaneously. How do I annotate the overlap?"

**Data Labeler:**

Overlapping speech is the hardest audio annotation edge case. Here's the systematic approach:

**Standard overlap annotation rules:**

```
Timeline representation:
0:00 ─────────────────── 0:10 ─────────────────── 0:20
│    SPEAKER A              │                         │
│    "I think we should"    │"absolutely"             │
│                      ┌────┤                         │
│                      │  ←1s overlap→    SPEAKER B   │
│                      │   "Yes, I agree" ───────────►│
└──────────────────────┘

Option 1: Mark both labels at overlap point (if tool supports multi-label)
  [0:00-0:10] SPEAKER_A
  [0:09-0:20] SPEAKER_B    ← overlap from 0:09 to 0:10

Option 2: Mark dominant speaker at transition (if tool is single-label only)
  [0:00-0:10] SPEAKER_A    ← dominant speaker until clear handoff
  [0:10-0:20] SPEAKER_B    ← full control after overlap ends
  Add note: "OVERLAP 0:09-0:10: both speakers active"
```

**Practical boundary rules for 1-second overlap:**
- Use ±50ms tolerance for speaker turn boundaries (human ear + annotation tool precision)
- If overlap is <200ms: treat as interruption; assign to dominant speaker; add flag
- If overlap is >500ms: try to mark both; if tool doesn't support, mark dominant + flag
- Always write: `[OVERLAP 0:09.0-0:10.1 SPEAKER_A + SPEAKER_B]` in notes field

**Guideline gap → escalate:** This is a clear guideline gap. Flag it:
> "EDGE CASE: 1-second speaker overlap at 0:09. Applied dominant-speaker rule. Tool doesn't support multi-label. Recommend guideline update for overlap handling. Example: audio_042.mp3"

---

