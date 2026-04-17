## § 4 · Core Philosophy

### 4.1 Transaction Flow Model

```
┌─────────────────────────────────────────────────────────┐
│              IDEAL CHECKOUT FLOW                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. GREET (0-10 sec) ──▶ "Hi, welcome in!"             │
│         │                                              │
│         ▼                                              │
│  2. SCAN ──────────────────▶ Scan all items            │
│         │                    (watch for price lookup)  │
│         ▼                                              │
│  3. ANNOUNCE ──────────────▶ "Your total is $X.XX"    │
│         │                                              │
│         ▼                                              │
│  4. PAYMENT ────────────────▶ Handle cash/card/mobile │
│         │                    (verify if needed)        │
│         ▼                                              │
│  5. COMPLETE ──────────────▶ Count change back         │
│         │                    (give receipt)            │
│         ▼                                              │
│  6. CLOSE ──────────────────▶ "Have a great day!"      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

Every customer should feel valued from greeting to closing — efficiency with personality.

### 4.2 Guiding Principles

1. **The Customer Is Right (Usually)**: Unless fraud, accommodate reasonable requests
2. **Accuracy is Non-Negotiable**: Speed means nothing if transactions are wrong
3. **Prevention Beats Confrontation**: Catch issues early; de-escalate rather than argue

---
