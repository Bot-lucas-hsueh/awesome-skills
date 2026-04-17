## § 4 Core Philosophy

### Mental Model: Satellite Link as a Chain

```
SPACE SEGMENT                    GROUND SEGMENT
┌─────────────┐   Downlink       ┌──────────────────────┐
│  Satellite  │ ─────────────── │  Earth Station
│  Transponder│ ◄─────────────  │  or User Terminal     │
│  (Payload)  │   Uplink         └──────────────────────┘
└─────────────┘
      │
      ▼ The link is only as strong as the weakest margin:

  EIRP(dBW) - FSPL(dB) - Atm_Loss(dB) + G/T(dB/K) - Noise_Factor(dB) = C/N0(dBHz)

  C/N0 → C/N (in bandwidth) → Eb/N0 (at bit rate) → BER → Service quality
```

### Guiding Principles

1. **Margin is Engineering Humility**: Calculated performance is based on models and assumptions; real systems have pointing errors, component tolerances, and interference; design minimum 3 dB margin over requirements
2. **Spectrum is Shared and Finite**: Every Hz of spectrum used carries interference obligations; design for minimum interference footprint, not maximum EIRP — efficiency is both regulatory and economic
3. **Ground Segment Defines System Economics**: Satellite hardware is the glamorous part; ground segment (gateways, terminals, OSS/BSS) is 60-70% of system cost and the determinant of commercial success

---

