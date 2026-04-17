## § 4 · Core Philosophy

### Mental Model: The AI Training Data Pipeline

```
┌──────────────────────────────────────────────────────────────┐
│              DEPLOYMENT MODEL BEHAVIOR                       │
│      (what the model does when users interact)               │
└────────────────────────┬─────────────────────────────────────┘
                         │ shaped by
┌────────────────────────▼─────────────────────────────────────┐
│              TRAINING SIGNAL                                 │
│   SFT Dataset  ·  Preference Pairs  ·  Reward Model         │
└────────────────────────┬─────────────────────────────────────┘
                         │ produced by
┌────────────────────────▼─────────────────────────────────────┐
│              ANNOTATION PROCESS                              │
│   Guidelines  ·  Annotators  ·  Quality Control  ·  IAA     │
└────────────────────────┬─────────────────────────────────────┘
                         │ constrained by
┌────────────────────────▼─────────────────────────────────────┐
│              TASK & ALIGNMENT SPECIFICATION                  │
│   Objective  ·  Dimensions  ·  Priority Ordering             │
└──────────────────────────────────────────────────────────────┘
```

### Guiding Principles

1. **Data Quality is Model Quality** — The ceiling of a model's performance on any dimension is set by the quality and consistency of its training data. No amount of algorithmic cleverness compensates for noisy labels.

2. **Annotators are Experts Who Need Structure** — Annotators are capable of nuanced judgment, but only when guidelines provide unambiguous structure for edge cases. Vague guidelines produce vague models.

3. **Every Training Example is a Behavioral Policy** — Think in terms of behavior distribution, not individual examples. Ask: "What policy over all possible inputs does this example imply?"

---

