## § 5 · Decision Frameworks

### IMA vs Federated Decision Matrix

| Criterion | Federated | IMA | Winner |
|-----------|-----------|-----|--------|
| Weight | Higher (redundant HW) | Lower (shared) | IMA |
| Power | Higher | Lower | IMA |
| Certification | Simpler | Complex | Federated |
| Upgrade | LRU replacement | Software load | IMA |
| Cost (development) | Lower | Higher | Federated |
| Cost (lifecycle) | Higher | Lower | IMA |

### GNSS Accuracy Budget

| Error Source | Typical Value | Mitigation |
|--------------|---------------|------------|
| Ionospheric delay | 5-15m | Dual-frequency, models |
| Tropospheric delay | 0.5-2m | Models, surface met |
| Ephemeris error | 2-5m | Precise ephemeris |
| Clock error | 2-5m | Monitor stations |
| Multipath | 0.5-5m | Antenna design, filtering |
| Receiver noise | 0.1-1m | Narrow correlators |

📄 **Full Details**: [references/09-decision-frameworks.md](references/09-decision-frameworks.md)

---
