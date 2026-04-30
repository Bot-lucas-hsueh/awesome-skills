# python Example

```
def nbiot_ntn_link_budget_mce(
    altitude_km, freq_GHz=1.5, satellite_eirp_dBW=40, satellite_gt_dBK=5,
    ue_tx_power_dBm=23, ue_antenna_gain_dBi=-3, noise_figure_dB=6
):
    """
    NB-IoT NTN link budget with coverage extension (REP = repetition).
    Coverage Class 0: single transmission (normal)
    Coverage Class 1: 2 repetitions (+3 dB combining gain)
    Coverage Class 2: 4 repetitions (+6 dB)
    Coverage Class 3: 8 repetitions (+9 dB)
    NB-IoT system BW: 180 kHz
    """
    k_B = 1.38e-23
    BW_Hz = 180e3  # NB-IoT bandwidth
    noise_power_dBW = 10 * np.log10(k_B * 290 * BW_Hz) + noise_figure_dB

    FSPL = fspl_dB(
        distance_km=(6371e3 + altitude_km*1e3 - 6371e3 * np.sin(np.radians(10)))
        frequency_GHz=freq_GHz
    )

    # Uplink (UE → satellite):
    ue_eirp_dBW = ue_tx_power_dBm - 30 + ue_antenna_gain_dBi
    C_N0_uplink = ue_eirp_dBW - FSPL + satellite_gt_dBK - (-228.6)
    SNR_uplink = C_N0_uplink - 10 * np.log10(BW_Hz)

    # NB-IoT SNR requirement: -12.6 dB for NPDSCH, -15.3 dB with 4 REP
    REP_gains = {1: 0, 2: 3, 4: 6, 8: 9, 16: 12, 32: 15, 64: 18, 128: 21}
    results = []
    for rep, gain in REP_gains.items():
        effective_snr = SNR_uplink + gain
        npdsch_threshold = -12.6 - (3.0 * np.log2(rep))  # coverage extension threshold
        margin = effective_snr - npdsch_threshold
        results.append({'REP': rep, 'SNR_dB': round(effective_snr, 1),
                         'threshold_dB': round(npdsch_threshold, 1),
                         'margin_dB': round(margin, 1), 'passes': margin >= 0})
    return results

reps = nbiot_ntn_link_budget_mce(altitude_km=600)
print("NB-IoT NTN repetition analysis:")
for r in reps[:5]:
    status = "✓" if r['passes'] else "✗"
    print(f"  REP={r['REP']:3d}: SNR={r['SNR_dB']:+.1f}dB, threshold={r['threshold_dB']:+.1f}dB, "
          f"margin={r['margin_dB']:+.1f}dB {status}")
```
