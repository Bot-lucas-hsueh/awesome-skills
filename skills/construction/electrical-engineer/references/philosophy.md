## § 4 · Core Philosophy

### 4.1 Electrical System Hierarchy

```
┌─────────────────────────────────────────┐
│        UTILITY SERVICE                  │
│    (Grid connection, metering)          │
└─────────────────┬───────────────────────┘
                  │
    ┌─────────────┼─────────────┐
    ▼             ▼             ▼
┌───────┐    ┌───────┐    ┌───────┐
│ MAIN  │    │ MAIN  │    │EMERG. │
│SWITCH-│    │SWITCH-│    │POWER  │
│ GEAR  │    │ GEAR  │    │SYSTEM │
└───┬───┘    └───┬───┘    └───┬───┘
    │             │             │
    ▼             ▼             ▼
┌───────┐    ┌───────┐    ┌───────┐
│DISTRI-│    │DISTRI-│    │TRANSFER│
│BUTION │    │BUTION │    │SWITCH  │
│PANELS │    │PANELS │    │        │
└───┬───┘    └───┬───┘    └───┬───┘
    │             │             │
    ▼             ▼             ▼
┌───────┐    ┌───────┐    ┌───────┐
│BRANCH │    │BRANCH │    │EMERG. │
│CIRCUITS│   │CIRCUITS│   │CIRCUITS│
└───────┘    └───────┘    └───────┘
```

### 4.2 Guiding Principles

1. **Safety Above All**: Design systems that protect people first, equipment second.
2. **Code is Law**: NEC requirements are minimums for life safety.
3. **Grounding is Critical**: A proper ground path saves lives. Never compromise.
4. **Plan for Growth**: Include 25% spare breakers and feeder capacity.
5. **Efficiency Matters**: LEDs, controls, and power factor reduce operating costs.

---
