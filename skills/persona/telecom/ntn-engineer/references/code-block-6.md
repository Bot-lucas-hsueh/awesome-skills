# python Example

```
def leo_handover_analysis(orbital_period_min, beams_per_satellite,
                           cell_diameter_km, satellite_velocity_km_s=7.56):
    """
    Calculate handover frequency and protocol requirements for LEO NTN.
    """
    # Time per cell (Earth-moving cell): cell passes UE in ~cell_diameter
    cell_crossing_time_s = cell_diameter_km
    ho_per_minute = 60

    # 3GPP Rel-17 NTN handover strategies:
    strategies = {
        'Earth-Fixed Cell': {
            'description': 'Cell footprint fixed to Earth; satellite steers beam to maintain',
            'HO_trigger': 'Cell boundary crossing (beam steering limit)',
            'latency_impact': 'Predictable HO timing (ephemeris-based)',
            'cell_crossing_time_s': cell_crossing_time_s,
        },
        'Earth-Moving Cell': {
            'description': 'Cell follows satellite movement; UE stays in same cell for full pass',
            'HO_trigger': 'Satellite handoff to next satellite (every ~orbital_period/n_beams)',
            'cell_crossing_time_s': orbital_period_min * 60
        },
        'Conditional Handover (CHO)': {
            'description': 'Pre-configure target cell; execute when condition met (ephemeris-predictive)',
            'standard': '3GPP Rel-16 CHO extended for NTN predictable movement',
            'benefit': 'Near-zero interruption time vs random access HO',
        },
    }

    print(f"Satellite velocity: {satellite_velocity_km_s} km/s")
    print(f"Cell diameter: {cell_diameter_km} km")
    print(f"Earth-fixed cell crossing: {cell_crossing_time_s:.0f} s ({ho_per_minute:.1f} HO/min)")
    for name, s in strategies.items():
        print(f"\n{name}:")
        if 'cell_crossing_time_s' in s:
            print(f"  Cell dwell time: {s['cell_crossing_time_s']:.0f}s")
        print(f"  Trigger: {s.get('HO_trigger', 'N/A')}")

leo_handover_analysis(orbital_period_min=97, beams_per_satellite=8,
                       cell_diameter_km=400, satellite_velocity_km_s=7.56)
# Earth-fixed cell: crossing ~53s → ~1 HO/minute (too frequent for standard HO)
# Earth-moving cell: satellite pass ~12 min → 1 HO/12min (acceptable)
# → Recommend Earth-moving cell + Conditional HO with ephemeris-based pre-preparation
```
