## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| Strategy overfitting | 🔴 High | Curve-fitting to historical data produces poor live performance | Use out-of-sample testing; simplify strategies; limit parameters |
| Execution risk | 🔴 High | Slippage, latency, and market impact erode alpha | Paper trade first; use realistic cost models; implement smart order routing |
| Leverage risk | 🔴 High | Amplified losses can exceed initial capital | Strict position limits; daily VaR checks; margin alerts |
| Black swan events | 🔴 High | Market dislocations can trigger unprecedented losses | Stress testing; tail risk hedges; position sizing controls |
| Model decay | 🟡 Medium | Alpha decays as markets adapt | Continuous monitoring; strategy retirement protocols |
| Regulatory risk | 🟡 Medium | Algorithmic trading regulations require compliance | Maintain audit trails; register as required; monitor for rule changes |
