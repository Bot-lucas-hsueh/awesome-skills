## § 6 · Professional Toolkit

### Simulation & Analysis Software
- **Systems Tool Kit (STK
- **MATLAB/Octave** — Link budget scripting, Doppler profile calculation, HARQ process analysis
- **GNU Radio** — Waveform simulation, NTN channel emulation (Doppler, delay spread)
- **ns-3 with NTN module** — End-to-end protocol simulation (TCP, QUIC, NR scheduler)
- **OPNET
- **ITU-R Software (GRWAVE, REC-P)** — Rain attenuation, troposcatter, propagation calculations

### Standards & Reference Documents
- **3GPP TR 38.811** — Study on NR NTN channel model (path loss, Doppler, delay spread)
- **3GPP TS 38.821** — Solutions for NR NTN
- **3GPP TR 36.763** — IoT NTN (NB-IoT/eMTC over satellite)
- **3GPP TS 38.101-5** — NR UE radio transmission for NTN (Rel-17)
- **ITU-R P.618-14** — Propagation data for Earth-space paths
- **ITU-R P.838-3** — Specific attenuation model for rain
- **ITU-R S.1503** — Functional description for Epfd calculation
- **ETSI TR 103 611** — 5G satellite integration in SBA architecture

## Phase 1: System Requirements & Link Budget (Weeks 1–3)

**Free-Space Path Loss & Link Budget:**
```python
[Code block moved to code-block-1.md]
```

**Doppler Shift Calculation:**
```python
def doppler_shift_ntn(altitude_km, frequency_GHz, elevation_deg):
    """
    Maximum Doppler shift for LEO satellite pass at given elevation.
    v_sat ≈ sqrt(GM/r) where r = Re + h (circular orbit)
    Doppler: fD = (v_sat/c) * f * cos(angle_from_velocity_vector)
    Maximum: when satellite passes overhead (zenith) for 90° elevation
    At elevation angle θ: fD_max ≈ (v_sat/c) * f * sin(θ_approach)
    """
    GM = 3.986e14   # m³/s² (Earth gravitational constant)
    Re = 6.371e6    # m
    c = 3e8         # m/s
    f = frequency_GHz * 1e9  # Hz

    r = Re + altitude_km * 1e3  # orbital radius (m)
    v_sat = np.sqrt(GM / r)    # satellite velocity (m/s)

    # Maximum Doppler (at satellite horizon approach, elevation → 0°)
    # More precisely: fD_max at elevation 0° = v_sat * f
    fD_max_Hz = v_sat * f

    # At a given elevation angle (approximate for circular orbit):
    # fD(elevation) = fD_max * cos(elevation)  (simplified)
    fD_at_elevation = fD_max_Hz * np.cos(np.radians(elevation_deg))

    return {
        'v_sat_km_s': round(v_sat
        'fD_max_kHz': round(fD_max_Hz
        'fD_at_elevation_kHz': round(fD_at_elevation
        '5G_NR_SCS_15kHz_ratio': round(fD_max_Hz
        'pre_compensation_required': fD_max_Hz > 0.1 * 15e3,  # >10% SCS → pre-comp required
    }

# LEO 600 km, Ka-band 20 GHz, elevation 10°
doppler = doppler_shift_ntn(600, 20, elevation_deg=10)
print(f"LEO 600km Ka-band 20GHz: v_sat={doppler['v_sat_km_s']} km/s, "
      f"fD_max={doppler['fD_max_kHz']} kHz, Ratio to 15kHz SCS: {doppler['5G_NR_SCS_15kHz_ratio']}x")
# v_sat=7.56 km/s, fD_max=504 kHz (33× SCS!) → MANDATORY pre-compensation
```

✓ Link budget closes at worst-case elevation (10°) with ≥ 0 dB margin
✓ Doppler pre-compensation capability confirmed in UE (GNSS + ephemeris)
✓ Timing advance range sufficient for orbital altitude (3GPP extended TA field)
✗ Do not claim link closure without rain margin at target availability (99.9% or 99.99%)

### Phase 2: 3GPP NTN Protocol Adaptation Design (Weeks 4–8)

**HARQ Process Count for NTN RTT:**
```python
[Code block moved to code-block-1.md]
```

**Timing Advance Pre-Compensation (3GPP NTN):**
```python
[Code block moved to code-block-2.md]
```

✓ HARQ process count configured correctly for orbital altitude and TTI
✓ TA pre-compensation enabled (GNSS-based, ephemeris broadcast)
✓ Doppler pre-compensation residual error ≤ 0.1 × SCS
✗ Do not deploy standard terrestrial 5G gNB for NTN without Rel-17 protocol adaptations

### Phase 3: End-to-End Performance Optimization (Weeks 9–16)

**TCP Throughput Over NTN — Buffer Sizing:**
```python
[Code block moved to code-block-3.md]
```

**NB-IoT NTN Coverage Extension:**
```python
[Code block moved to code-block-4.md]
```

✓ TCP window scaling enabled (RFC 7323) for all NTN connections
✓ NB-IoT REP count set per coverage class based on link budget
✓ Adaptive Coding and Modulation (ACM) fallback chain specified
✗ Do not use standard 4G/5G terrestrial congestion control algorithms for GEO (buffer bloat disaster)

## 🔬 Scenario Examples

### 🚫 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Ignoring Doppler Pre-Compensation Requirement
**Wrong:** Deploy 5G NR gNB with standard 15 kHz SCS for LEO 600 km Ka-band NTN without Doppler compensation.
**Why it fails:** LEO Doppler at Ka-band 20 GHz: fD_max = 504 kHz = 33× SCS. Random access preamble phase rotates 33 times per slot → PRACH detection failure. PDCCH demodulation fails → no connection.
**Correct:** UE must pre-compensate Doppler using GNSS position + satellite ephemeris (broadcast in SIB) before transmission. Residual Doppler budget ≤ 0.1 × SCS = 1.5 kHz.

### Anti-Pattern 2: Using Terrestrial HARQ Configuration for GEO NTN
**Wrong:** Configure 5G gNB with standard HARQ RTT = 8 ms for GEO satellite (RTT = 476 ms).
**Why it fails:** HARQ processes time out before ACK/NACK returns from UE. gNB retransmits unnecessarily, causing self-interference and spectral waste. Throughput collapses to near zero for TCP-like traffic.
**Correct:** For GEO: disable HARQ (Rel-17 HARQ-less mode), rely on outer ARQ (RLC/PDCP). For LEO >1200 km: extend HARQ to 32 processes (Rel-17 NTN). Always verify RTT/TTI ratio before HARQ configuration.

### Anti-Pattern 3: Neglecting BDP for TCP Throughput Over GEO
**Wrong:** Provision 50 Mbps Ka-band GEO link; assume TCP will achieve 50 Mbps throughput.
**Why it fails:** GEO RTT = 550 ms. TCP BDP = 50 Mbps × 0.55 s = 3.44 MB. Standard TCP window = 64 KB → max throughput = 64KB
**Correct:** Enable TCP window scaling (RFC 7323) to 4 MB+ window; use BBR or CUBIC congestion control; or switch to QUIC (UDP-based, no head-of-line blocking, better NTN performance). Performance-Enhancing Proxy (PEP) at gateway for legacy TCP connections.

### Anti-Pattern 4: Rain Margin Calculated at Temperate Climate for Tropical Deployment
**Wrong:** Use rain attenuation margin of 3 dB (temperate, London) for Ka-band VSAT in Singapore or Mumbai (tropical).
**Why it fails:** Tropical rain rate at 0.01% exceedance: 95–120 mm/h vs 30–50 mm/h temperate. Ka-band attenuation in tropical region: 10–20 dB at 0.01% vs 3–5 dB temperate. Link closure failure during heavy rain events, exactly when reliability matters (emergency communications, aviation).
**Correct:** Use ITU-R P.837 rain rate maps for local location. Apply ACM with fallback to BPSK 1/4 (lowest MODCOD) or increase rain margin to 15–20 dB for tropical Ka-band systems.

### Anti-Pattern 5: Failing to Account for Feeder Link Delay in End-to-End Latency Budget
**Wrong:** Quote LEO NTN latency as "4 ms one-way" for user experience.
**Why it fails:** 4 ms is only the service link (UE → satellite). Total end-to-end latency includes: service link (4–7 ms one-way) + feeder link (satellite → gateway, 4–7 ms) + gateway processing (1–5 ms) + internet transit (5–50 ms). Actual round-trip latency: 28–120 ms for LEO NTN (not 8 ms).
**Correct:** Always budget all latency components: service_link_up + service_link_down + feeder_up + feeder_down + gateway_processing + internet_transit. Quote end-to-end RTT (typically 30–50 ms for well-designed LEO NTN vs. 500–600 ms for GEO).

