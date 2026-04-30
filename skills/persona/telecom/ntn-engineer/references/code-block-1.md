# python Example

```
def ntn_harq_analysis(altitude_km, tti_ms=1.0, processing_ms=4.0):
    """
    3GPP Rel-17 NTN HARQ process requirement.
    RTT = 2 × (propagation one-way) + UE processing + gNB processing
    Minimum HARQ processes: N_HARQ = ceil(RTT
    3GPP Rel-17 NTN max HARQ processes: 16 (NR) or 32 (NR NTN extended)
    """
    c = 3e8
    h_m = altitude_km * 1e3
    prop_one_way_ms = h_m
    # At 10° elevation, slant range up to 2000 km → prop delay 6.7 ms
    prop_max_ms = np.sqrt((6371e3 + h_m)**2 - 6371e3**2 * np.cos(np.radians(10))**2)
    prop_max_ms = (prop_max_ms - 6371e3 * np.sin(np.radians(10)))

    RTT_min_ms = 2 * prop_one_way_ms + processing_ms
    RTT_max_ms = 2 * prop_max_ms + processing_ms

    N_HARQ_min = int(np.ceil(RTT_min_ms
    N_HARQ_max = int(np.ceil(RTT_max_ms

    NR_max_HARQ = 16  # standard NR
    NR_NTN_max_HARQ = 32  # 3GPP Rel-17 NTN extension (TS 38.212/213/214)

    return {
        'altitude_km': altitude_km,
        'prop_one_way_min_ms': round(prop_one_way_ms, 2),
        'prop_max_slant_ms': round(prop_max_ms, 2),
        'RTT_min_ms': round(RTT_min_ms, 2),
        'RTT_max_ms': round(RTT_max_ms, 2),
        'N_HARQ_needed_min': N_HARQ_min,
        'N_HARQ_needed_max': N_HARQ_max,
        'NR_standard_sufficient': N_HARQ_max <= NR_max_HARQ,
        'NTN_extended_sufficient': N_HARQ_max <= NR_NTN_max_HARQ,
    }

for alt in [600, 1200, 35786]:
    r = ntn_harq_analysis(alt)
    print(f"Alt={r['altitude_km']:6d}km: RTT={r['RTT_min_ms']:.1f}–{r['RTT_max_ms']:.1f}ms, "
          f"N_HARQ needed={r['N_HARQ_needed_min']}–{r['N_HARQ_needed_max']}, "
          f"NR16 OK={r['NR_standard_sufficient']}, NTN32 OK={r['NTN_extended_sufficient']}")
# Alt=   600km: RTT=4.0–13.3ms, N_HARQ=5–14 → NR16 sufficient for LEO
# Alt=  1200km: RTT=8.0–22.0ms, N_HARQ=9–23 → NTN32 needed at max slant range
# Alt= 35786km: RTT=238ms–550ms, N_HARQ=239–551 → HARQ MUST be disabled for GEO!
```
