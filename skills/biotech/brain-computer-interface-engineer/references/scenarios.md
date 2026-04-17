## 9. Scenario Examples

### Example 1: Designing a Motor BCI Decoder for Tetraplegic Patient

**User:** We are building a motor BCI for a C4 tetraplegic patient using a 96-channel Utah array in motor cortex. What decoder should we use to control a computer cursor in 2D?

**Engineer:**
For 2D cursor control with a 96-channel Utah array in human motor cortex, here is the full decoder stack I would recommend based on current clinical BCI evidence (BrainGate2, Hochberg et al. Nature 2012; Willett et al. Nature 2021).

**Feature Layer:**
Use binned spike rates (50 ms bins) from well-isolated single units (ISI <2%, isolation distance >20) plus threshold crossing rates (multi-unit activity) as features. Include gamma-band LFP power (70-200 Hz) which is more stable chronically than single units. Total feature dimensionality: ~150-200 features from 96 channels.

**Decoder: Velocity Kalman Filter (VKF) with Online Gain Adaptation:**
```python
import numpy as np

class VelocityKalmanFilter:
    """
    Kalman filter for 2D cursor velocity decoding.
    State: [vx, vy, 1] (velocity + offset)
    Observation: neural firing rate vector z_t (n_units,)
    """
    def __init__(self, n_units, dt=0.05):
        self.dt = dt  # 50 ms bin
        # State transition: velocity is correlated across bins
        self.A = np.array([[0.9, 0,   0],
                           [0,   0.9, 0],
                           [0,   0,   1]])
        self.W = np.diag([0.5, 0.5, 0])  # process noise
        # Observation model: calibrated via OLS regression
        self.H = np.zeros((n_units, 3))   # calibrated from training data
        self.Q = np.eye(n_units) * 10.0  # observation noise (tuned)
        self.P = np.eye(3)               # state covariance
        self.x = np.zeros(3)             # state: [vx, vy, 1]

    def calibrate(self, Z_train, V_train):
        """OLS calibration: Z = V @ H.T + noise"""
        V_aug = np.hstack([V_train, np.ones((len(V_train), 1))])
        self.H = np.linalg.lstsq(V_aug, Z_train, rcond=None)[0].T

    def predict(self):
        self.x = self.A @ self.x
        self.P = self.A @ self.P @ self.A.T + self.W

    def update(self, z_obs):
        """Update with new neural observation z_obs (n_units,)"""
        innovation = z_obs - self.H @ self.x
        S = self.H @ self.P @ self.H.T + self.Q
        K = self.P @ self.H.T @ np.linalg.inv(S)  # Kalman gain
        self.x = self.x + K @ innovation
        self.P = (np.eye(3) - K @ self.H) @ self.P
        return self.x[:2]  # decoded velocity [vx, vy]

    def online_adapt(self, z_obs, z_pred_prev, alpha=0.01):
        """Unsupervised Q/R update to handle neural drift"""
        residual = z_obs - z_pred_prev
        self.Q += alpha * (np.outer(self.x, self.x) - self.Q)
        self.Q[2, 2] = 0  # don't adapt offset covariance
```

**Calibration Protocol:**
Day 1: 10-minute open-loop calibration where patient imagines cursor movements in cued directions (8 directions × 15 repetitions). Calibrate H matrix via OLS. Decode cursor velocity from VKF; integrate to position.

**Online Adaptation:**
Implement unsupervised gain adaptation: use high-confidence decoded states (|velocity| > threshold) to update H incrementally using Recursive Least Squares (RLS, forgetting factor λ=0.9999). This prevents catastrophic accuracy degradation over weeks without requiring daily recalibration sessions.

**Expected Performance:**
BrainGate-class cursor BCI: ~80% target acquisition accuracy in 8-target Fitts' Law task; ~1.5-2.5 bits/min throughput; cross-day accuracy retention >80% at Week 4 with adaptation. Utah array SNR degrades chronically — plan fallback to threshold-crossing (multi-unit) features if single units are lost at Month 6.

### Example 2: Debugging High ISI Violation Rate After Spike Sorting

**User:** Kilosort3 is giving us ISI violation rate of 12% on many units. How do we diagnose and fix this?

**Engineer:**
ISI violation rate of 12% means 12% of detected spike intervals are <3 ms — within the absolute refractory period where a neuron cannot fire. This indicates multi-unit contamination or sorting artifacts. Here is the diagnostic tree:

**Step 1: Visualize Waveforms and Autocorrelogram**
```python
import spikeinterface as si
import spikeinterface.postprocessing as spost
import spikeinterface.qualitymetrics as sqm

# Load Kilosort3 output
sorting = si.read_kilosort(kilosort_output_folder)
recording = si.read_openephys(data_folder)

# Compute quality metrics
analyzer = si.create_sorting_analyzer(sorting, recording, sparse=True)
analyzer.compute(['noise_levels', 'templates', 'spike_amplitudes'])
metrics = sqm.compute_quality_metrics(
    analyzer,
    metric_names=['isi_violation', 'isolation_distance', 'l_ratio', 'snr']
)

# Filter high-ISI units
bad_units = metrics[metrics['isi_violations_ratio'] > 0.05].index
print(f"Units with ISI >5%: {len(bad_units)}/{len(metrics)}")
print(metrics.loc[bad_units, ['isi_violations_ratio', 'isolation_distance', 'snr']])
```

**Common Causes and Fixes:**

Cause 1 — Template collision: Two nearby neurons with similar waveforms merged into one unit. Fix: increase `nPCs` in Kilosort3 (default 3 → 6); enable `do_correction = True`; re-run with tighter merge threshold (`merge_threshold = 0.90` from default 0.95).

Cause 2 — High recording noise: Electrode noise creates threshold crossings that appear as spikes. Fix: check electrode impedance >500 kΩ (degraded); apply narrower bandpass (500-5000 Hz instead of 300-5000 Hz) to reduce low-frequency artifact; verify ground electrode placement.

Cause 3 — Motion artifact: Mechanical vibration causes correlated across-channel threshold crossings sorted as spikes. Fix: check for ISI violations concentrated at specific times (mechanical events); apply motion detection and rejection epochs; improve probe mechanical fixation.

Cause 4 — Insufficient data for template estimation: With <20 min of recording, template estimation is unreliable. Fix: run Kilosort3 on minimum 60 min of stable recording.

**Manual Curation with Phy:**
Units with ISI >5% should be marked as MUA (multi-unit activity) and excluded from single-unit analyses, but can still be used as features in LFP-like multi-unit BCI decoders.

### Example 3: Planning FDA Regulatory Pathway for Novel Intracortical BCI

**User:** We've developed a new 1024-channel polymer intracortical probe with wireless transmission for a motor BCI. What is the FDA pathway?

**Engineer:**
A 1024-channel intracortical polymer probe with wireless neural recording and motor decoding for tetraplegic patients is almost certainly a Class III medical device requiring a Pre-Market Approval (PMA) — not a 510(k). Here is the regulatory analysis:

**Device Classification:**
Intracortical recording electrodes for brain-computer interfaces are classified as Class III (21 CFR Part 870.3610 and Part 882) because they pose high risk (implanted in the brain, direct neural stimulation/recording capability). The predicate device pathway is limited: Blackrock Neuroport Array (HDE approval 2004) and BrainGate2 Investigational Device Exemption (IDE) exist as precedents but a PMA with clinical data is the standard path.

**Regulatory Pathway:**

Phase 1 — Pre-Submission Meeting (Q-Sub):
Request a Pre-Sub meeting with FDA CDRH Office of Neurological and Physical Medicine Devices (ONPMD). Present: device description, proposed intended use, preliminary biocompatibility and bench data, proposed clinical protocol. FDA will provide written feedback within 90 days. This is the most valuable step — do not skip it.

Phase 2 — Investigational Device Exemption (IDE):
Submit IDE application to conduct a first-in-human study. Required elements: device description and manufacturing, preclinical data (bench testing, animal study data), proposed clinical protocol, informed consent, IRB approval, risk analysis (ISO 14971 FMEA). IDE approval takes 30 days; FDA can impose significant risk (SR) conditions.

**Bench Testing Required Before Human Study:**
- Electrical safety: IEC 60601-1 (dielectric strength, leakage current)
- Biocompatibility: ISO 10993-1, cytotoxicity (10993-5), sensitization (10993-10), subchronic systemic toxicity (10993-11)
- Mechanical reliability: insertion force, buckling load, chronic flex fatigue (>10M cycles)
- Wireless: FCC Part 15 (MICS band 401-406 MHz for implants), SAR testing
- MRI compatibility: ASTM F2182 (heating), F2503 (MR conditional labeling)
- Hermeticity: MIL-STD-883 fine/gross leak; IIR <10⁻⁸ atm·cc/sec for Class 3 hermeticity

**Timeline Estimate:**
Bench testing: 18-24 months. IDE submission to approval: 6-12 months. Phase 1 safety study (n=5-10 patients, 12-month follow-up): 24-36 months. PMA submission: 12+ months review. Total: 6-8 years to market. Budget $10-50M for full PMA pathway.

---

