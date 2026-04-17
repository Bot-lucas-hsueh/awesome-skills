## § 4 · Core Philosophy

```
              6G TECHNOLOGY STACK MENTAL MODEL
              ==================================

  Physical World           6G Network Layer              Application Layer
  +-------------+         +------------------+          +------------------+
  | THz Channel |--RIS--->| Holographic MIMO |--OTFS--->| eMBB >1 Tbps     |
  | Near-field  |         | AI-Native PHY    |          | URLLC <0.1ms     |
  | Sub-THz     |         | Semantic Codec   |          | mMTC 10^7/km²    |
  | 100-300 GHz |         +--------+---------+          | Sensing/Locating |
  +-------------+                  |                    +------------------+
                           +-------v--------+
                           |  IMT-2030 KPIs |
                           | Rate: >1 Tbps  |
                           | SE: >100b/s/Hz |
                           | Lat: <0.1ms    |
                           | Rel: 99.99999% |
                           +-------+--------+
                                   |
                    +--------------+--------------+
                    |              |              |
             +------v---+  +-------v--+  +--------v----+
             | AI-Native |  | Semantic |  | Integrated  |
             | Estimator |  | Comms    |  | Sensing     |
             | ChannelNet|  | DeepSC   |  | ISAC        |
             +-----------+  +----------+  +-------------+

  FREQUENCY REGIME LADDER:
        ^ THz (300 GHz+)    — molecular absorption, nano-networks
       ^^ sub-THz (100-300) — 6G access, near-field MIMO
      ^^^ mmWave (24-100)   — 5G NR, 6G mid-band
     ^^^^ sub-6 GHz         — 5G/6G wide-area coverage
```

**Guiding Principles:**

1. **Near-Field is the Default at 6G** — with holographic arrays of hundreds or thousands of antenna elements operating at 140-300 GHz, almost every access scenario falls within the Rayleigh near-field zone. Channel modeling, beamforming optimization, and localization algorithms must be built from spherical wavefront physics, not the plane-wave convenience of 4G/5G theory.

2. **AI is a Protocol Block, Not a Feature** — in IMT-2030's AI-native air interface vision, machine learning models replace explicit mathematical blocks (channel estimation, equalization, channel coding) in the protocol stack rather than serving as an add-on optimizer. This requires rethinking standardization, interpretability, and robustness validation at every layer.

3. **Spectral Efficiency Must Be Traded Systemically** — achieving >100 bit/s/Hz spectral efficiency requires joint optimization across space (massive MIMO/holographic), frequency (wideband THz), and time (OTFS for Doppler resilience); no single dimension achieves the IMT-2030 target; always analyze the 3D capacity cube.

---

