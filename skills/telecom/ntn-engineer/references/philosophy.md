## § 4 · Core Philosophy

**NTN Platform Selection — 5-Gate Decision Tree:**

```
Gate 1: Latency requirement?
  ├── Ultra-low latency (< 20 ms): Not achievable with any NTN (min LEO RTT ≈ 4 ms one-way)
  │   → NTN for non-real-time; terrestrial 5G for URLLC
  ├── 20–100 ms RTT → LEO NTN (500–1200 km altitude), viable for most applications
  ├── 100–600 ms RTT → MEO acceptable (video, broadband)
  └── > 600 ms RTT → GEO acceptable (IoT, broadcast, delay-tolerant data)

Gate 2: Coverage area?
  ├── Global or remote (oceanic, polar) → LEO/MEO/GEO constellation
  ├── Regional (single continent) → GEO beam or regional HAPS cluster
  └── Urban hotspot extension → HAPS (200 km footprint per platform)

Gate 3: Data rate requirement per UE?
  ├── IoT (< 100 kbps) → NB-IoT NTN or eMTC NTN (Rel-17), L-band or S-band
  ├── Mobile broadband (1–100 Mbps) → LEO 5G NTN, Ka-band phased array
  └── Backhaul / fixed broadband (> 100 Mbps) → GEO Ka/Q/V-band VSAT or LEO constellation

Gate 4: Terminal type?
  ├── Handheld smartphone (standard power class) → L/S-band LEO NTN (FWA or NB-IoT)
  ├── Vehicle-mounted
  └── Fixed terminal → VSAT dish (90 cm+) or flat panel phased array (Starlink style)

Gate 5: Regulatory
  ├── L-band (1.5/1.6 GHz) → MSS allocations (Inmarsat, Iridium), ITU RR Article 9
  ├── S-band (2 GHz) → MSS + IMT (3GPP Band 256 for NTN)
  └── Ka-band (17.7/27.5 GHz) → NGSO FSS, 3GPP FR2 NTN
```

**Link Budget Philosophy:** Always close the link twice: (1) worst-case (minimum satellite elevation 10°, maximum path length, maximum rain rate at 0.01% exceedance), (2) typical case (45° elevation, median rain). Margin in worst case ≥ 0 dB = link can close. Margin ≥ 3 dB = adequate. Margin < 0 dB = link failure at that availability.

**HARQ Philosophy:** The fundamental NTN challenge is that terrestrial HARQ was designed for 8ms RTT. NTN RTT is 4–560 ms. The 3GPP solution (Rel-17) is: (1) increase HARQ process count N = ceil(RTT/TTI) + processing overhead, (2) enable UE-side HARQ timer extension. For GEO, HARQ can be disabled entirely (HARQ-less mode with RLC retransmissions).
