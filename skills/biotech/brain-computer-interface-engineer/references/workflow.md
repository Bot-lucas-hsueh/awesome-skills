## 8. Standard Workflow

### Phase 1 — Neural Recording Setup and Signal Quality Validation

**Steps:**
1. Specify electrode array: Utah array (96-192ch, 1.5mm shanks, 400 µm pitch) for motor cortex; Neuropixels 1.0/2.0 (384-960ch, 20 µm pitch) for rodent research; ECoG grid (8×8 or 4×8, 4mm pitch) for human epilepsy mapping.
2. Validate impedance with EIS at 1 kHz: all channels <100 kΩ before implantation, <500 kΩ at acute post-op (<5% failure rate acceptable).
3. Configure acquisition: 30 kHz sampling for AP band (300 Hz-5 kHz bandpass), 2.5 kHz for LFP band (0.3-300 Hz bandpass), 16-bit ADC resolution with ±6.4 mV range (Intan RHD2164: 0.195 µV/bit).
4. Measure noise floor: short-circuit input and compute RMS in AP band. Target <5 µV RMS; investigate EMI if >10 µV.
5. Run spike sorting (Kilosort3): detect threshold crossings at -4.5× RMS; extract 82-sample waveforms; run template matching with drift correction; post-sort quality metrics (ISI <2%, isolation distance >20).

**[✓ Done]** criteria: >80% channels with SNR >5 dB; ISI violation rate <2% on well-isolated units; noise floor <5 µV RMS.
**[✗ FAIL]** criteria: >30% channels failed impedance (array damage); SNR <3 dB across array — check ground loop, cable shielding, and amplifier power supply.

### Phase 2 — Decoder Development and Offline Validation

**Steps:**
1. Extract neural features: spike firing rates (binned 50-100 ms), LFP band power (theta 4-8 Hz, alpha 8-12 Hz, beta 12-30 Hz, gamma 30-100 Hz), LFP phase, multi-unit activity envelope.
2. Select decoder appropriate to task: Kalman filter (continuous kinematic decoding: position/velocity), SVM/LDA (discrete classification: grasp type, phoneme, direction), LSTM (sequential temporal dependencies), Transformer (long-range temporal context for speech BCI).
3. Split data: train on 70% of sessions; validate on 20%; test on held-out 10% — critically, include sessions from different days in the test set to measure generalization.
4. Quantify performance: R² and RMSE for regression; accuracy, F1, and bits-per-trial for classification; measure latency from neural event to decoded output.
5. Ablation: compare features (spikes only vs. LFP only vs. combined); compare decoder complexity (linear vs. nonlinear); assess channel count dependence (N vs. performance curve).

**[✓ Done]** criteria: Cross-session accuracy >80% on held-out days without recalibration; online decoding latency <50 ms for motor BCI.
**[✗ FAIL]** criteria: >15% accuracy drop Day 1 → Day 7 — non-stationarity is the bottleneck; implement manifold alignment or unsupervised adaptation.

### Phase 3 — Closed-Loop System Validation and Clinical Translation

**Steps:**
1. Implement real-time pipeline: Open Ephys plugin → Python ZMQ socket → decoder inference → actuator command; measure round-trip latency with hardware timestamps.
2. Validate closed-loop stability: run step-response test (command onset to cursor arrival); measure settling time, overshoot; tune decoder output smoothing (exponential weighted moving average, α=0.7-0.9).
3. Run human or NHP closed-loop performance: report online accuracy, throughput (bits/min), task completion time, and compare to offline predictions.
4. Assess long-term stability: daily performance metrics over 30-90 days; apply online adaptation if accuracy drops >10% from Day 1.
5. Prepare regulatory package: define intended use, contraindications, risk analysis (ISO 14971 FMEA), biocompatibility summary, essential performance requirements (EPR), and device description for FDA Pre-Submission.

**[✓ Done]** criteria: Closed-loop performance within 15% of offline prediction; loop latency <50 ms; 30-day performance maintained with adaptation.
**[✗ FAIL]** criteria: Closed-loop worse than random — check latency mismatch, temporal alignment of spike times to kinematics, decoder output saturation.

---

