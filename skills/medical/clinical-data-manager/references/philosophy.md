## § 4 · Core Philosophy

### The Clinical Data Lifecycle

```
                    ┌─────────────────────────┐
                    │   Regulatory Submission   │  ← SDTM/ADaM packages,
                  ┌─┴─────────────────────────┴─┤   define.xml, RG
                  │    Database Lock & Archive    │  ← Clean data, audit
                ┌─┴─────────────────────────────┴─┤   trails preserved
                │      Data Cleaning & Query        │  ← Query generation,
              ┌─┴───────────────────────────────────┴─┤   resolution
              │        Data Collection (EDC)            │  ← eCRF entry,
            ┌─┴─────────────────────────────────────────┴─┤   monitoring
            │              Database Design                  │  ─ CRF specs,
          ┌─┴───────────────────────────────────────────────┴─┤   edit checks
          │                  Protocol Input                     │  ─ Endpoints,
          └───────────────────────────────────────────────────────┘   CRF design
```

### Guiding Principles

1. **ALCOA+ Compliance**: Attributable, Legible, Contemporaneous, Original, Accurate + Complete, Consistent, Enduring, Available
2. **Right First Time**: Design quality in; minimize corrections
3. **Traceability**: Every data transformation documented
4. **Risk Proportionate**: Focus resources on critical data
5. **Collaboration**: Partner with clinical, statistical, regulatory teams

---
