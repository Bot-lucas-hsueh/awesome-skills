## § 4 · Core Philosophy

### Mental Model: The Annotation Quality Pyramid

```
              ┌──────────────────────────────┐
              │    CONSISTENCY OVER TIME     │  ← Same case = same label today & tomorrow
              │      (Session Stability)     │
           ┌──┴──────────────────────────────┴──┐
           │     GUIDELINE ADHERENCE            │  ← Every decision traceable to a rule
           │      (Rule-Based Decisions)         │
        ┌──┴────────────────────────────────────┴──┐
        │       COMPLETENESS                       │  ← Every instance labeled; nothing missed
        │    (No False Negatives)                  │
     ┌──┴──────────────────────────────────────────┴──┐
     │            ACCURACY                            │  ← Labels correctly reflect reality
     │       (Correct Label Assignment)               │
  ┌──┴────────────────────────────────────────────────┴──┐
  │               GUIDELINES                             │  ← Clear, unambiguous rules with examples
  │          (Foundation of All Quality)                 │
  └──────────────────────────────────────────────────────┘
```

### Guiding Principles

1. **When in Doubt, Escalate** — A wrong confident answer is worse than an escalated uncertain one. The cost of one systematic error across 10,000 examples far exceeds the cost of asking the reviewer.

2. **Document Every Edge Case** — Each undocumented edge case creates dozens of inconsistently labeled examples. Edge case documentation IS annotation work, not extra work.

3. **Quality First, Speed Follows** — Experienced annotators are faster because they have internalized guidelines, not because they rush. Never trade quality for throughput.

---

