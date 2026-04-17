## § 4 · Core Philosophy

```
              ISAC SYSTEM MENTAL MODEL
              =========================

  Transmit Side                 Channel              Receive Side
  +---------------+         +----------+         +------------------+
  | Communication |--beamf->| Wireless |--comm-->| Communication Rx |
  | Data Symbols  |  W_c    | Multipath|         | OFDM Demod       |
  +-------+-------+         +----+-----+         | Channel Estimate |
          |                      |               +------------------+
  +-------v-------+              |
  | ISAC Precoder |              | Target
  | (Joint W_c+W_r)              | Reflection
  +-------+-------+         +----v-----+         +------------------+
          |                 | Radar    |--echo-->| Radar Rx         |
  +-------v-------+         | Targets  |         | Range-Doppler    |
  | Radar Probing |         +----------+         | MUSIC/ESPRIT     |
  | Waveform      |                              | CFAR Detection   |
  +---------------+                              +------------------+

  PARETO TRADE-OFF REGION:
    SCNR (dB)
    ^
    |  *  <- Radar-optimal (all power to sensing)
    | * *
    |*   *
    |     * *
    |         * <- Comms-optimal (all power to comm)
    +-----------> SINR (dB)
    The curve is the achievable Pareto front;
    any operating point below-left is suboptimal.
    ISAC beamformer design = choosing a point ON the front.

  RANGE-DOPPLER RESOLUTION:
    Range resolution    Δr = c
    Velocity resolution Δv = λ / (2 × T_obs)  [m/s]
    Angular resolution  Δθ = λ
```

**Guiding Principles:**

1. **The Fundamental ISAC Trade-off is Physical, Not Algorithmic** — the SINR-SCNR Pareto front is determined by physics (transmit power, bandwidth, aperture, noise figure); clever algorithms shift the operating point on the front but cannot move beyond it. Always establish the theoretical Pareto front before evaluating any algorithm's position relative to it.

2. **CRB is the North Star for Sensing** — the Cramér-Rao Bound defines the minimum achievable estimation variance for any unbiased estimator, given the waveform and signal model. Designing below the CRB is impossible; designing within 3 dB is excellent engineering. CRB drives waveform selection — maximize Fisher Information for the sensing parameters of interest.

3. **Waveform Orthogonality Enables Joint Processing** — MIMO-ISAC systems achieve the highest spatial degrees of freedom when transmit waveforms are orthogonal (across antennas, subcarriers, or time slots); this enables full virtual aperture formation for radar while maintaining independent communication streams; trade-off: fully orthogonal waveforms have lower per-stream SINR.

---

