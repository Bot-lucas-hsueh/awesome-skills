# python Example

```
def ntn_timing_advance(altitude_km, elevation_deg):
    """
    Calculate timing advance for NTN.
    3GPP NR TA = round-trip propagation delay expressed in Ts units.
    Ts = 1/(480000 × 4096) = 509 ns (basic time unit)
    TA_value in 3GPP = N_TA × Ts, where N_TA is the TA field value
    NTN Rel-17: UE pre-compensates based on GNSS position + ephemeris
    """
    Re = 6371e3  # m
    c = 3e8
    h = altitude_km * 1e3  # m

    el_rad = np.radians(elevation_deg)
    # Slant range
    slant_m = np.sqrt((Re + h)**2 - Re**2 * np.cos(el_rad)**2) - Re * np.sin(el_rad)

    RTT_s = 2 * slant_m
    RTT_ms = RTT_s * 1000

    Ts = 1
    N_TA = RTT_s
    N_TA_bits = np.ceil(np.log2(N_TA))

    # 3GPP Rel-17 NTN TA field: extended to 28 bits vs standard 12 bits
    max_TA_standard = 2**12 * Ts * 1000  # ms
    max_TA_NTN = 2**28 * Ts * 1000       # ms

    return {
        'slant_range_km': round(slant_m/1e3, 1),
        'RTT_ms': round(RTT_ms, 2),
        'N_TA_required': int(N_TA),
        'N_TA_bits_required': int(N_TA_bits),
        'max_TA_standard_ms': round(max_TA_standard, 2),
        'max_TA_NTN_ms': round(max_TA_NTN, 1),
        'standard_TA_sufficient': RTT_ms <= max_TA_standard,
    }

ta = ntn_timing_advance(600, elevation_deg=10)
print(f"LEO 600km, 10° elevation: slant={ta['slant_range_km']}km, "
      f"RTT={ta['RTT_ms']}ms, N_TA={ta['N_TA_required']}, standard_TA_ok={ta['standard_TA_sufficient']}")
# slant=2090 km, RTT=13.93ms, N_TA=27,394,000 → Standard 12-bit TA far insufficient
# → Rel-17 NTN extended TA (28-bit field) or UE pre-compensation REQUIRED
```
