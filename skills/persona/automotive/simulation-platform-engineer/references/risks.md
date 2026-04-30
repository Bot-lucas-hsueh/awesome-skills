## § 3 Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|-------------------|------------|
| **Sim-to-real gap overconfidence** | Critical | AV stack passes simulation but fails in real deployment; safety incident | Continuously validate sim metrics against real-world driving logs; maintain gap budget <15% on key perception KPIs |
| **Scenario bias
| **Non-deterministic reproduction** | High | Failing scenarios cannot be reproduced for debugging; regression value lost | Always log RNG seeds, scenario parameters, NPC behavior seeds, and simulator version in test artifacts |
| **Physics model inaccuracy** | Medium | Sensor outputs unrealistic; perception model trained on corrupted synthetic data | Validate each sensor model with real-world A/B comparison; document fidelity envelope |
| **Infrastructure scalability failure** | Medium | Nightly regression takes >24 hours; CI bottleneck blocks deployment | Implement horizontal scaling with Kubernetes + CARLA server pool; benchmark at 10x current load before production |

---
