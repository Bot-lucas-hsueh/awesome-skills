## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| THz hardware immaturity | 🔴 Critical | Sub-THz transceivers (>100 GHz) have PA efficiency <5%, phase noise >10 dBc/Hz at 1 MHz offset, and maximum EIRP limited by regulatory constraints; link budget calculations ignoring these impairments overestimate achievable rates by 10-20 dB | Always include hardware impairment models in link simulation; use measured PA/PA+RFchain NF figures from published hardware; do not extrapolate sub-6 GHz PA models |
| Near-field model invalidation | 🔴 Critical | Using plane-wave (far-field) channel models for large arrays above 60 GHz causes severe beam prediction errors; Rayleigh distance at 300 GHz with 20cm aperture is 80m — most indoor deployments are near-field | Compute 2D²/λ before selecting model; use spherical wavefront models (XL-MIMO, near-field RIS) for all arrays >16 elements above 100 GHz |
| Molecular absorption blind spot | 🟡 High | Specific absorption bands (183 GHz, 325 GHz water vapor) cause 10-100 dB/km excess attenuation — deployments near these bands fail in humid conditions | Compute ITU-R P.676 molecular absorption for target frequency; choose bands at 140 GHz, 220 GHz, or 300 GHz (low-absorption windows) |
| AI channel estimator generalization | 🟡 High | Neural network channel estimators trained on DeepMIMO A1 scenario fail on outdoor UMa channels without retraining; domain mismatch causes 3-5 dB estimation loss | Train and test on matched scenarios; implement online adaptation or meta-learning; always compare to classical MMSE baseline |
| Semantic comms security vulnerability | 🟡 High | Semantic codecs trained on specific task distributions are vulnerable to adversarial semantic noise injection that preserves bit integrity but corrupts semantic meaning | Evaluate semantic robustness under adversarial perturbations; design semantic encryption layer for sensitive applications |
| IMT-2030 timeline overconfidence | 🟢 Medium | 6G standardization (3GPP Release 21+) targets 2028-2030; THz components, AI air interface, and global RIS standards are not commercially available — avoid claiming near-term deployment readiness in research framing | Use "IMT-2030 candidate technology" framing; distinguish lab demonstration from deployment readiness |

---
