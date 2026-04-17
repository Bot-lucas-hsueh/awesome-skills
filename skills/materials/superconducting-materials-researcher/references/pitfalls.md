# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|-------------|----------|-----------|
| 1 | **Using room-temperature Ic to predict cryogenic performance** | 🔴 High | Always test at 4.2K; RT Ic has no correlation with superconducting Ic |
| 2 | **Skipping RRR measurement on incoming wire** | 🔴 High | Measure RRR for every spool; reject if RRR < specification |
| 3 | **Overwinding Nb₃Sn during react&wind** | 🟡 Medium | Limit winding strain < 0.15%; use tension monitoring |
| 4 | **No quench detection on REBCO no-insulation coil** | 🔴 High | Implement voltage tap + temperature sensor detection |
| 5 | **Storing REBCO tapes without humidity control** | 🟡 Medium | Store at < 30% RH; Cu-stabilized tapes are more tolerant |
| 6 | **Assuming Nb₃Sn is stable at strain limit** | 🔴 High | Monitor n-value degradation; reject if n < 15 |

## 10.2 Best Practices

1. **Always verify Ic at operating temperature** — never extrapolate from 77K self-field measurements
2. **Use statistical sampling** — test 5% of each spool minimum; reject entire spool if > 10% fail
3. **Preload coils above Lorentz force** — minimum 1.5× margin for training reduction
4. **Implement multi-layer quench protection** — voltage detection + temperature sensors + heaters
5. **Document every training cycle** — use training curves to detect degradation over magnet lifetime
6. **Control thermal cycling** — each cool-down adds ~0.5–1% training step if not preloaded properly

## 10.3 Quality Checklist

- [ ] Ic measurement at 4.2K, self-field (or relevant field) completed and passed
- [ ] RRR measurement completed and > specification
- [ ] Cross-section analysis: filament uniformity, void fraction < 2%
- [ ] Twist pitch verified (for multifilamentary wire)
- [ ] Coil preload verified with strain gauges before cool-down
- [ ] Quench protection system functional and tested
- [ ] Persistent switch resistance < 10^-8 Ω (if applicable)
- [ ] Field homogeneity < specification (for imaging magnets)
- [ ] Training data documented and within normal range
- [ ] All certifications and test reports archived
