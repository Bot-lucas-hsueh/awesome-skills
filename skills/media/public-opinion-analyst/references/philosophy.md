## § 4 · Core Philosophy

### 4.1 Sentiment Analysis Framework

```
┌─────────────────────────────────────────────────────────────┐
│  SENTIMENT CLASSIFICATION                                   │
│                                                             │
│  POSITIVE (Happy, Praise, Support)                         │
│  ├── Enthusiastic: "This is amazing!"                     │
│  ├── Satisfied: "Works well, would recommend"             │
│  └── Mildly Positive: "Pretty good overall"               │
│                                                             │
│  NEUTRAL (Informational, Factual, Unclear)                │
│  ├── Informational: "Here is the product specs"            │
│  ├── Unclassified: Can't determine sentiment               │
│  └── Contextual: Fact-based without opinion               │
│                                                             │
│  NEGATIVE (Complaint, Criticism, Opposition)              │
│  ├── Angry: "This is unacceptable, I'm suing"              │
│  ├── Frustrated: "Third time broken, never buying again"  │
│  └── Mildly Negative: "Not what I expected"                │
│                                                             │
│  KEY INSIGHT: Binary classification loses nuance          │
│  → Use 5-point scale or emotion tags for precision         │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Crisis Early Warning Matrix

```
                    LOW VELOCITY              HIGH VELOCITY
                 (slow, steady mentions)   (rapid spike in mentions)

HIGH NEGATIVE
VOLUME        → Monitor closely           → ACTIVATE CRISIS PROTOCOL
              Slow, sustained negative    Sudden viral negative
              may indicate systemic      often = single trigger event
              issue                      Immediate response required

LOW NEGATIVE  → No action needed           → PREPARE CONTINGENCY
VOLUME        Background noise            Potential for escalation
              Expected for any brand     Monitor hourly; prepare
                                       statement

NEUTRAL/      → No action needed           → MONITOR TRENDING
POSITIVE      Baseline                    Viral moment = opportunity
                                         for amplification
```

### 4.3 Guiding Principles

1. **Volume is vanity, velocity is sanity**: High volume that grows slowly is manageable; rapid velocity even at lower volume is dangerous.
2. **Sentiment is context-dependent**: "Expensive" means different things from a luxury vs. a budget brand.
3. **Correlation ≠ causation**: Just because sentiment dropped when you launched a campaign doesn't mean the campaign caused it.
4. **Data quality determines insight quality**: Garbage in, garbage out — validate sources before drawing conclusions.
5. **The "so what" test**: Every data point should lead to insight; if you can't recommend action, the data isn't useful yet.

---

