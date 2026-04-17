## § 4 · Core Philosophy

### 4.1 Strategy Development Lifecycle

```
┌─────────────────────────────────────────────────────────────┐
│                    STRATEGY LIFECYCLE                        │
├─────────────────────────────────────────────────────────────┤
│  1. Hypothesis  ──►  2. Research  ──►  3. Backtest          │
│       │                   │                  │               │
│       │    Literature     │   Data           │  In-sample    │
│       │    Review         │   Collection     │  Testing      │
│       │                   │                  │               │
│       ▼                   ▼                  ▼               │
│  4. Out-of-Sample  ──►  5. Paper Trade  ──►  6. Deploy     │
│       │                   │                  │               │
│       │    Walk-forward   │  Live simulated  │  Small cap    │
│       │    validation     │  execution        │  first        │
│       │                   │                  │               │
│       ▼                   ▼                  ▼               │
│                    7. Monitor & Iterate                       │
│                    (continuous improvement)                  │
└─────────────────────────────────────────────────────────────┘
```

The strategy lifecycle is iterative: hypothesize from market observation, research thoroughly, backtest rigorously, validate out-of-sample, paper trade, then deploy with small capital. Never skip steps.

### 4.2 Guiding Principles

1. **Evidence over intuition.** Every trading decision should be supported by statistical evidence from data, not gut feel.
2. **Expect the unexpected.** Markets can remain irrational longer than you can remain solvent. Size positions appropriately.
3. **Simplicity wins.** Complex strategies are harder to understand, debug, and maintain. Start simple; add complexity only when justified.
4. **Risk first, returns second.** Preserve capital first; alpha opportunities will always exist.
5. **Never stop learning.** Markets evolve; strategies decay; continuous research is essential.

---

