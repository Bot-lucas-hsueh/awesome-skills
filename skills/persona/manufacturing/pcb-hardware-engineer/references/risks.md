## § 3 Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|--------------------|------------|
| Impedance mismatch causing reflection | CRITICAL | Data corruption, system malfunction, field failure | Use controlled impedance stackup; verify with TDR |
| Inadequate decoupling causing PDN noise | CRITICAL | Logic glitches, timing violations, EMI failure | Place decap within 0.5mm of pins; use multiple values |
| Crosstalk exceeding noise margin | HIGH | Bit errors on adjacent signals; functional failure | Maintain 3W spacing to sensitive nets; guard traces |
| EMI radiated emissions failure | HIGH | FCC/CISPR test failure; product cannot ship | Add shielding, ferrites, edge rate limiting |
| Via stub resonance | HIGH | Signal degradation at high frequencies | Back-drill or use blind/buried vias for >1Gbps |
| BGA fanout failure | CRITICAL | Manufacturing impossible; respin required | Use proper fanout pattern; verify with fab house |
| Solder joint reliability failure | HIGH | Field failure from thermal cycling | Follow IPC-610 Class 3; verify DFA clearances |

---
