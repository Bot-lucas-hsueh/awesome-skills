# python Example

```
def comprehensive_security_check(qber, detection_rate_hz, timing_histogram,
                                 decoy_counts, baseline_detection_rate):
    """
    Multi-indicator QKD security assessment.
    Checks beyond QBER to detect sophisticated attacks.
    """
    alerts = []

    # 1. QBER threshold (primary indicator)
    if qber > 0.11:
        alerts.append("CRITICAL: QBER exceeds BB84 threshold — abort key generation")

    # 2. Detection rate anomaly (photon-number-splitting indicator)
    rate_ratio = detection_rate_hz
    if rate_ratio < 0.7 or rate_ratio > 1.3:
        alerts.append(f"ALERT: Detection rate anomaly ({rate_ratio:.2f}x baseline) "
                      "— possible photon-number-splitting or channel interruption")

    # 3. Decoy-state consistency (PNS attack detection)
    # Ratio of signal to decoy detection should match theoretical prediction
    expected_signal_decoy_ratio = np.exp(mu - nu)  # BB84 decoy theory
    actual_ratio = decoy_counts['signal']
    if abs(actual_ratio - expected_signal_decoy_ratio) > 0.1 * expected_signal_decoy_ratio:
        alerts.append("ALERT: Decoy state statistics inconsistent — possible PNS attack")

    # 4. Timing histogram analysis (time-shift attack detection)
    peak_asymmetry = abs(timing_histogram[0] - timing_histogram[1])
                     (timing_histogram[0] + timing_histogram[1])
    if peak_asymmetry > 0.05:
        alerts.append("ALERT: Timing peak asymmetry detected — possible time-shift attack")

    if not alerts:
        return "SECURE: All security indicators nominal"
    return "\n".join(alerts)
```
