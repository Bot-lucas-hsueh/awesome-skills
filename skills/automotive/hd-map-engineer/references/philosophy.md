## § 4 · Core Philosophy

```
[Code block moved to code-block-1.md]
```

**4.1 Guiding Principles:**

1. **Map is an Enabler, Not a Crutch**: HD maps dramatically improve AV performance in structured environments, but the system must gracefully handle map gaps, staleness, and localization failures. Design every map-dependent feature with a defined fallback to camera-only lane detection.

2. **Vectorized Representation is Non-Negotiable**: Raster maps (PNG heightmaps) may be useful for visualization but are insufficient for autonomous driving consumption. AV planning requires vectorized lane graphs with topology (successor/predecessor relations, lane adjacency) for path routing and regulatory element lookup.

3. **Map Accuracy is Only Half the Story**: A 5cm accurate map combined with 50cm localization error produces 55cm total error — worse than a 30cm accurate map with 5cm localization. Always specify the full map+localization accuracy budget together.

---

