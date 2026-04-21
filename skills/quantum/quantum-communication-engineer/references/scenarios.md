## 9. Scenario Examples

### Example 1: Designing a 100-km Metropolitan QKD Link

**User:** We need a QKD link between two data centers 100 km apart using standard telecom fiber. What protocol, hardware, and expected key rate should we plan for?

**Engineer:**

For a 100-km metropolitan QKD link, here is the complete design recommendation.

Protocol selection: Use decoy-state BB84 with biased basis (Z-basis probability 0.9). This is the most mature protocol with production-grade hardware available from ID Quantique and Toshiba. MDI-QKD would add complexity without benefit since you control both endpoints (both are your trusted nodes).

Loss budget calculation:
```python
import numpy as np

# Link parameters
distance_km = 100
fiber_loss_dB_per_km = 0.2         # SMF-28 at 1550 nm
n_connectors = 8                    # splice + connector losses
connector_loss_dB = 0.3 * n_connectors

# Total channel loss
total_loss_dB = distance_km * fiber_loss_dB_per_km + connector_loss_dB
total_loss_linear = 10 ** (-total_loss_dB

# Hardware parameters (SNSPD-based system)
mu = 0.6                            # mean photon number per pulse (signal)
nu = 0.1                            # weak decoy
omega = 0.0                         # vacuum decoy
eta_detector = 0.90                 # SNSPD efficiency at 1550 nm
f_rep = 1e9                         # 1 GHz pulse repetition rate
dark_count_rate = 100               # cps per detector

# Detection probability (signal state)
eta_total = total_loss_linear * eta_detector
P_det_signal = 1 - np.exp(-mu * eta_total)
R_det = f_rep * P_det_signal        # detection rate (Hz)

# QBER estimation (detector dark count + optical noise)
P_dark_per_pulse = dark_count_rate
QBER_estimated = P_dark_per_pulse

print(f"Total loss:        {total_loss_dB:.1f} dB ({total_loss_linear:.2e} linear)")
print(f"Detection rate:    {R_det/1000:.1f} kHz")
print(f"Estimated QBER:    {QBER_estimated*100:.2f}%")

# Secret key rate estimate (Gottesman-Lo-Lütkenhaus-Preskill + decoy)
h = lambda p: -p*np.log2(p+1e-15) - (1-p)*np.log2(1-p+1e-15)
f_EC = 1.10          # error correction efficiency (Shannon limit = 1.0)

# Single-photon contribution via decoy analysis (simplified)
Q1_estimated = 0.55 * R_det   # ~55% of detections from single-photon component
e_phase = QBER_estimated * 1.2   # phase error rate (slightly higher than bit error)

SKR = Q1_estimated * (1 - h(e_phase)) - R_det * f_EC * h(QBER_estimated)
print(f"Estimated SKR:     {SKR/1000:.1f} kbps")
```

Expected results: ~21 dB loss, ~10-15 kHz detection rate, QBER ~1.5%, SKR ~2-5 kbps. This is well above the 1 kbps metropolitan benchmark.

Hardware recommendation:
- Source: ID Quantique Clavis3 or Toshiba QKD system (BB84, 1550 nm, decoy-state)
- Detectors: SNSPD (Photon Spot or Single Quantum) with η > 90%, dark count < 100 cps, jitter < 50 ps
- Classical channel: Dedicated fiber pair or WDM channel (>100 GHz channel spacing from QKD channel)
- KMS: ETSI GS QKD 004 compliant; integrate with existing HSM infrastructure

Key management: At 5 kbps SKR, you can refresh AES-256 keys every 50 seconds (256-bit key

---

### Example 2: Diagnosing High QBER and Security Abort

**User:** Our BB84 QKD link is showing QBER = 9.8% — near the 11% threshold. Is this an eavesdropper or hardware fault?

**Engineer:**

QBER = 9.8% is a serious anomaly requiring systematic diagnosis before attributing to eavesdropping. Here is the decision tree:

```python
def diagnose_qber_anomaly(qber, baseline_qber=0.015, dark_count_rate_cps=100,
                           detection_rate_hz=12000, fiber_distance_km=100):
    """
    Systematic QBER anomaly diagnosis for BB84 QKD link.
    baseline_qber: normal operating QBER (typically 1-3%)
    """
    print(f"=== QBER ANOMALY DIAGNOSIS ===")
    print(f"Current QBER: {qber*100:.1f}% (baseline: {baseline_qber*100:.1f}%)")
    print(f"Threshold:    11.0% (BB84 one-way post-processing)")
    print()

    # Check 1: Dark count contribution
    dc_qber = dark_count_rate_cps
    print(f"Check 1 — Dark count QBER contribution: {dc_qber*100:.3f}%")
    if dc_qber > 0.05:
        print("  ACTION: SNSPD may be warming up or gating electronics fault")

    # Check 2: Polarization/phase drift
    print(f"\nCheck 2 — Polarization/phase drift:")
    print("  ACTION: Run reference frame calibration; check polarization maintaining fiber connectors")
    print("  If QBER drops after recalibration: hardware drift (not eavesdropper)")

    # Check 3: Optical misalignment
    print(f"\nCheck 3 — Optical alignment:")
    print("  ACTION: Check detection count rate vs baseline")
    if detection_rate_hz < 0.5 * 12000:  # >50% drop from baseline
        print("  WARNING: Detection rate drop suggests fiber interruption or connector fault")
        print("  -> Not consistent with eavesdropping (would maintain count rate)")

    # Check 4: Eavesdropping signature
    print(f"\nCheck 4 — Eavesdropping indicators:")
    print("  Intercept-resend attack: QBER rises to ~25% (introduces 25% errors)")
    print("  Optimal individual attack: QBER ≈ 11% (exactly at threshold)")
    print(f"  Current QBER {qber*100:.1f}% is {'SUSPICIOUS (near threshold)' if qber > 0.09 else 'below threshold'}")

    # Recommendation
    print("\n=== RECOMMENDATION ===")
    if qber > 0.11:
        print("ABORT: QBER exceeds BB84 security threshold. No secret key can be generated.")
        print("Initiate full hardware diagnostic before resuming.")
    elif qber > 0.08:
        print("HIGH ALERT: QBER approaching threshold.")
        print("1. Immediately run reference frame recalibration")
        print("2. Check SNSPD temperature and bias current")
        print("3. Inspect fiber connectors and patch panels")
        print("4. If QBER persists after hardware checks: treat as potential eavesdropping")
        print("5. Consult security officer; suspend key delivery to applications")

diagnose_qber_anomaly(qber=0.098)
```

Most likely causes in order of probability: (1) Polarization drift in fiber due to temperature change — recalibration fixes in minutes; (2) SNSPD detector temperature drift — check cryostat temperature; (3) Connector contamination — clean APC connectors with IEC 61300-3-35 compliant tools; (4) Partial fiber fault (microbend, splice degradation); (5) Active eavesdropping — least likely but cannot be ruled out above 8%.

Security policy: Suspend key delivery to applications while QBER > 8%. Log the anomaly, perform hardware checks in sequence. If QBER does not resolve within 15 minutes of recalibration, escalate to security team and treat as potential compromise.

---

### Example 3: TF-QKD for 500-km Long-Haul Link Without Repeaters

**User:** Can we achieve a 500-km QKD link without quantum repeaters? I've seen claims about Twin-Field QKD breaking the repeaterless bound.

**Engineer:**

Yes — Twin-Field QKD (TF-QKD, Lucamarini et al., Nature 2018) overcomes the repeaterless PLOB bound (Pirandola-Laurenza-Ottaviani-Banchi) by achieving SKR that scales as O(sqrt(eta)) rather than O(eta), where eta is the total channel transmissivity.

```python
import numpy as np
import matplotlib.pyplot as plt

def plob_bound(distance_km, loss_dB_per_km=0.2):
    """Pirandola-Laurenza-Ottaviani-Banchi fundamental repeaterless bound."""
    loss_dB = distance_km * loss_dB_per_km
    eta = 10**(-loss_dB/10)
    # PLOB: SKR <= -log2(1 - eta) ≈ eta
    return -np.log2(1 - eta) if eta < 1 else 0

def tf_qkd_skr(distance_km, loss_dB_per_km=0.2,
               mu=0.1, f_rep=1e9, eta_detector=0.85,
               e_d=0.005, misalignment_error=0.005):
    """
    Simplified TF-QKD secret key rate estimate.
    mu: mean photon number per pulse (typically 0.05-0.15)
    e_d: dark count error rate contribution
    """
    loss_dB = distance_km * loss_dB_per_km
    # Each Alice/Bob is distance/2 from middle node
    eta_half = 10**(-loss_dB/20)   # TF-QKD: half the total channel per segment
    eta_total = eta_half * eta_detector

    # Phase-matching events (single-photon clicks at relay)
    Q_pm = mu * eta_total * np.exp(-mu * eta_total)  # single-photon contribution

    # Bit error rate (Z-basis) and phase error rate (X-basis)
    e_bit = e_d + misalignment_error
    e_phase = 0.5   # worst case (privacy amplification handles this)

    # TF-QKD SKR: scales as sqrt(eta) not eta
    h = lambda p: -p*np.log2(p+1e-15) - (1-p)*np.log2(1-p+1e-15)
    SKR = f_rep * Q_pm * (1 - h(e_bit) - h(e_phase))

    return max(0, SKR)

distances = np.linspace(50, 600, 200)
plob_rates = [plob_bound(d) for d in distances]
tf_rates = [tf_qkd_skr(d) for d in distances]

# Print key distances
for d in [200, 300, 400, 500, 550]:
    plob = plob_bound(d)
    tf = tf_qkd_skr(d)
    print(f"Distance {d:3d} km: PLOB bound = {plob:.2e} bits/pulse, "
          f"TF-QKD = {tf:.2e} bits/pulse, "
          f"Overcomes PLOB: {tf > plob}")
```

Key results:
- At 500 km: TF-QKD achieves ~0.1 bps with 1 GHz repetition rate and 85% SNSPD efficiency
- PLOB bound at 500 km: ~10^-20 bits/pulse (essentially zero without repeaters)
- TF-QKD at 500 km: ~10^-13 bits/pulse — overcomes repeaterless bound by ~10^7

Critical requirements for 500-km TF-QKD:
1. Phase stabilization: continuous-wave reference laser phase-locking between Alice and Bob through the 500-km fiber; requires piezo-electric fiber stretchers for active phase feedback (<0.1 rad phase error).
2. Frequency locking: both Alice and Bob laser sources locked to same optical frequency reference (GPS-disciplined optical clock or shared RF reference); frequency deviation < 1 MHz for 1-ns coincidence window.
3. Middle relay node: classical relay with SNSPDs (no quantum memory needed — TF-QKD key strength); untrusted relay is acceptable (MDI-like property).
4. Timing synchronization: <100 ps timing jitter between distant parties; GPS or White Rabbit protocol (sub-ns accuracy over fiber).

Record distance: Toshiba Research demonstrated 600-km TF-QKD at ~0.01 bps (2021). NICT Japan demonstrated 240-km field-deployed TF-QKD (2022) with positive SKR.

Practical advice: TF-QKD at 500 km is laboratory-demonstrated but not yet commercially available as a product. For production deployment today, use a trusted-node chain with BB84 links at 80-100 km spacing. TF-QKD is the right choice if you need to avoid trusted intermediate nodes for security reasons.

---
