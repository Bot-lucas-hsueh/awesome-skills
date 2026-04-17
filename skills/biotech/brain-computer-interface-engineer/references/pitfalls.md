## 10. Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Reporting Offline Accuracy Without Cross-Day Validation

**Why it matters:** A BCI decoder trained and tested on data from the same day (or session) overfits to the day-specific neural state. Clinical BCI requires stable performance without daily recalibration.

❌ BAD:
```python
# Train and test on same session — not clinically meaningful
X_train, X_test, y_train, y_test = train_test_split(X_day1, y_day1, test_size=0.2)
decoder.fit(X_train, y_train)
acc = decoder.score(X_test, y_test)
print(f"BCI accuracy: {acc:.1%}")  # 94% — misleading
```

✅ GOOD:
```python
# Train on Days 1-5, test on Days 7, 14, 30 — clinical generalization
decoder.fit(X_days_1_to_5, y_days_1_to_5)
for test_day in [7, 14, 30]:
    acc = decoder.score(X_day[test_day], y_day[test_day])
    print(f"Day {test_day} accuracy (no recalib): {acc:.1%}")
# Day 7: 81%, Day 14: 74%, Day 30: 68% — now you see the true clinical picture
```

### Anti-Pattern 2: Ignoring the EMG Contamination Problem in EEG BCIs

**Why it matters:** Scalp EEG in the gamma band (30-100 Hz) is dominated by facial and scalp EMG, not neural oscillations. Classifiers trained on "gamma EEG" are often classifying muscle artifact.

❌ BAD:
```python
# No EMG rejection — high-gamma "BCI" is likely decoding facial muscles
raw.filter(30, 100)  # gamma band — heavily EMG contaminated
epochs = mne.Epochs(raw, events, tmin=-0.5, tmax=2.0)
features = epochs.get_data().var(axis=-1)  # band power feature
```

✅ GOOD:
```python
import mne
# Step 1: ICA to remove EMG and EOG components
ica = mne.preprocessing.ICA(n_components=20, method='fastica')
ica.fit(raw.copy().filter(1, 100))
eog_indices, _ = ica.find_bads_eog(raw)
muscle_indices, _ = ica.find_bads_muscle(raw)
ica.exclude = eog_indices + muscle_indices
raw_clean = ica.apply(raw.copy())

# Step 2: Avoid gamma band; use mu (8-12 Hz) and beta (18-26 Hz) for motor BCI
raw_clean.filter(8, 12)  # mu rhythm — genuine motor oscillation, EMG-free
```

### Anti-Pattern 3: Skipping the Shannon Curve for Stimulation Safety

**Why it matters:** Electrical stimulation current levels that exceed the Shannon charge density/charge per phase limit cause irreversible tissue and electrode damage.

❌ BAD:
```python
# Arbitrary stimulation parameters — potentially tissue-damaging
stim_params = {
    'amplitude_uA': 500,      # 500 µA
    'pulse_width_us': 500,    # 500 µs → charge = 250 µC
    'electrode_area_cm2': 0.001  # 1 mm² Utah tip
}
# Charge density = 250 µC / 0.001 cm² = 250,000 µC/cm² — DANGEROUS
```

✅ GOOD:
```python
def check_shannon_limit(amplitude_uA, pulse_width_us, electrode_area_cm2):
    """
    Shannon (1992) tissue damage model:
    log(D) = k - log(Q) where D = charge density, Q = charge per phase
    k = 1.7 for "safe" (no damage in 30 min exposure, McCreery 1990)
    """
    charge_uC = (amplitude_uA * pulse_width_us)
    charge_density = charge_uC / electrode_area_cm2     # µC/cm²
    k = 1.7
    import numpy as np
    safe_log_D = k - np.log10(charge_uC)
    is_safe = np.log10(charge_density) < safe_log_D
    print(f"Charge/phase: {charge_uC:.3f} µC, Density: {charge_density:.1f} µC/cm²")
    print(f"Shannon limit: {10**safe_log_D:.1f} µC/cm², Status: {'SAFE' if is_safe else 'UNSAFE'}")
    return is_safe
```

### Anti-Pattern 4: Using Open-Loop Neural Features Without Latency Accounting

**Why it matters:** Neural signals must be aligned to behavior with precise timestamps. A 50 ms decoding latency applied to neural data without accounting for the neural latency to motor output (~100 ms voluntary movement lead time) results in a temporally misaligned decoder trained on wrong input-output pairs.

❌ BAD:
```python
# No latency accounting — decoder learns random noise
neural_features = compute_firing_rates(spikes, bin_ms=50)
cursor_velocity = kinematics['velocity']
# Aligning by index — ignores the ~150 ms neural-to-movement lead time
pairs = zip(neural_features, cursor_velocity)  # WRONG temporal alignment
```

✅ GOOD:
```python
# Correct neural lead time alignment (typically 100-150 ms for motor cortex M1)
NEURAL_LEAD_MS = 150  # M1 → EMG → movement latency
bin_ms = 50

def align_neural_to_kinematics(spikes_df, kin_df, lead_ms, bin_ms):
    """Shift neural data forward by lead_ms to align with movement."""
    neural_bins = bin_spikes(spikes_df, bin_ms=bin_ms)
    # Neural at time t predicts movement at time t + lead_ms
    neural_aligned = neural_bins.iloc[:-int(lead_ms/bin_ms)]
    kin_aligned = kin_df.iloc[int(lead_ms/bin_ms):]
    return neural_aligned.values, kin_aligned.values
```

### Anti-Pattern 5: Claiming BCI "Brain Control" Without Validating Neural Origin

**Why it matters:** Many reported BCIs control devices using EMG, EOG, or impedance changes, not actual neural signals. This is not a BCI in the clinical sense and cannot benefit patients with complete paralysis.

❌ BAD:
```
"Our EEG BCI achieves 95% accuracy controlling a wheelchair —
demonstrating direct brain control of assistive devices."
```

✅ GOOD:
```
"Our motor imagery EEG BCI achieves 85% online accuracy in the left/right hand
motor imagery paradigm (mu-rhythm ERD 8-12 Hz, C3/C4 electrodes). We validated
neural specificity by: (1) EMG rejection via ICA (facial EMG channels excluded);
(2) mu-rhythm ERD confirmed in source space (LCMV beamformer); (3) performance
above chance in complete ALS patients with full motor paralysis (n=3, 82±4%
accuracy), confirming neural not peripheral origin."
```

---

