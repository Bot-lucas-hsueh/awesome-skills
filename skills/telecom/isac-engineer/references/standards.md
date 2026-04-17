## 7. Standards & Reference

**ISAC Performance Metrics:**

| Metric | Formula | Target (6G ISAC) | Notes |
|--------|---------|------------------|-------|
| Range resolution | Δr = c
| Velocity resolution | Δv = λ / (2T_obs) | <0.1 m/s @ T=3ms, 28 GHz | Coherent processing interval (CPI) determines |
| Angular resolution | Δθ ≈ λ / (N_rx × d) | <2° @ 16 element, λ/2 spacing | Super-resolution (MUSIC) beats DFT by 5-10x |
| Communication SE | bits/s/Hz | >10 bit/s/Hz (MU-MIMO) | Must hold at the ISAC operating point |
| SINR (comms) | per-user SINR | >15 dB for 64QAM | Hard constraint in joint optimization |
| SCNR (radar) | signal-to-clutter+noise | >13 dB for Pd=0.99, Pfa=10^-6 | Neyman-Pearson criterion |
| CRB (angle) | 1/FIM_θ | σ²_θ > CRB | Fisher Information drives waveform choice |
| Mutual information (I(X;Z)) | H(X) - H(X|Z) | Maximize for sensing | ISAC capacity-distortion trade-off |

**Key Standards:**

| Standard | Scope | Key ISAC Provisions |
|----------|-------|-------------------|
| 3GPP TS 38.305 (Rel-16+) | NR positioning | PRS/SRS-based TDOA, AoD, AoA, Doppler; 5G infrastructure as passive radar |
| 3GPP TR 22.837 (Rel-18) | NR sensing study | Scenarios and requirements for NR ISAC; detection, ranging, velocity, imaging |
| IEEE 802.11bf (2024) | WLAN sensing | NDP-based sensing, multi-static, range 1cm - 300m, 2.4/5/6/60 GHz |
| IEEE 802.11ad/ay | 60 GHz mmWave | High-bandwidth sensing (BW up to 8 GHz), indoor localization |
| ETSI ISG SRV | Symbiotic radio | Spectrum sharing framework for backscatter-enhanced ISAC |
| ITU-R M.2160 | IMT-2030 | Sensing as native IMT-2030 use case: cm-level positioning, environmental mapping |
| ECMA-387 | 60 GHz PHY | Reference for mmWave ISAC waveform development |

**CRB Quick Reference:**

| Sensing Parameter | Fisher Information (single path, AWGN) | CRB |
|-------------------|----------------------------------------|-----|
| Angle-of-arrival θ | FIM_θ = (2π d/λ)² cos²(θ) × N(N²-1)/6 × 2SNR/σ²_n | CRB_θ = 1/FIM_θ |
| Time-of-arrival τ | FIM_τ = (2π)² × W² × SNR (W = RMS bandwidth) | CRB_τ = 1/(8π²W²SNR) |
| Doppler frequency f_d | FIM_fd = (2π)² × T² × SNR (T = observation time) | CRB_fd = 3/(2π²T²SNR) |

---

