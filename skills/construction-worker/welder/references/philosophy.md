## § 4 · Core Philosophy

### 4.1 Weld Selection Framework

```
                    ┌─────────────────────────────────────┐
                    │     DETERMINE LOAD TYPE              │
                    │  (Tension / Compression
                    └──────────────┬──────────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
┌───────▼────────┐      ┌──────────▼──────────┐    ┌────────▼────────┐
│   TENSION      │      │   COMPRESSION       │    │   SHEAR        │
│   (butt weld   │      │   (butt weld       │    │   (fillet weld │
│    preferred)  │      │    preferred)       │    │    most common)│
└───────┬────────┘      └──────────┬──────────┘    └────────┬────────┘
        │                          │                          │
        ▼                          ▼                          ▼
┌───────────────────┐   ┌─────────────────────┐    ┌──────────────────┐
│ Full-pen groove  │   │ Full-pen groove    │    │ Fillet weld     │
│ weld for max     │   │ weld for max       │    │ size per        │
│ strength          │   │ strength           │    │ loading          │
│ -OR-              │   │ -OR-               │    │ -OR-             │
│ Fillet + backing  │   │ Fillet + backing   │    │ Groove weld      │
└───────────────────┘   └─────────────────────┘    └──────────────────┘
```

Match weld type to loading condition—don't use a weak fillet where a groove weld is required.

### 4.2 Guiding Principles

1. **WPS is Law**: The Welding Procedure Specification dictates every parameter—deviation is non-conformance
2. **Cleanliness is Next to Strength**: Contamination causes porosity and cracking—cleanliness is mandatory
3. **Inspection is Required**: Visual inspection of 100% of structural welds is mandatory per AWS D1.1

---

