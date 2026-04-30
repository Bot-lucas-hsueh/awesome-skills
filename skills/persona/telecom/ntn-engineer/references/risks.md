## § 3 · Risk Disclaimer

| Risk | Description | Mitigation |
|------|-------------|------------|
| **Doppler-Induced Demodulation Failure** | LEO Doppler shift (±24 kHz at Ka-band 20 GHz for 600 km) exceeds 5G NR subcarrier spacing (15 kHz SCS) → inter-carrier interference | Pre-compensation: UE calculates Doppler from GNSS position + satellite ephemeris; residual Doppler budget ≤ 0.1 × SCS |
| **Timing Advance Overflow** | LEO satellite moving causes TA variation up to ±ms during pass → 3GPP TA range exceeded | Extended TA range in Rel-17 NTN (TA field extended to 64-bit); UE uses GNSS-based self-TA pre-compensation |
| **HARQ Retransmission Timeout** | Terrestrial HARQ RTT = 8 ms; LEO RTT = 4–28 ms; GEO RTT = 476–560 ms → HARQ timeout → throughput collapse | Rel-17 NTN: HARQ processes N increased to match RTT (N ≥ RTT/TTI + processing); optional HARQ disable for GEO |
| **Rain Fade Outage** | Heavy rain at Ka-band (30 GHz uplink): attenuation 10–30 dB at 0.01% availability → link closure failure | Uplink power control (ULPC) +10 dB; ACM (Adaptive Coding Modulation) fallback to BPSK 1/4; rain fade margin in budget ≥ 10 dB |
| **Spectrum Interference** | LEO constellation in Ka-band creates interference to GEO FSS; violates ITU Resolution 55 non-harmful interference | Epfd (equivalent power flux density) compliance per ITU; elevation angle exclusion zones; beam pointing avoidance |
