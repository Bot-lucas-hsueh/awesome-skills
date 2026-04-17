## 10. Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Using OFDM Pilot Symbols Only (Not Data) for Radar

**Why it matters:** OFDM radar using only pilot subcarriers (sparse in frequency) has range resolution limited by pilot grid spacing, not full bandwidth. In 5G NR with 1 pilot per 4 subcarriers, effective bandwidth for radar is 25% of total — range resolution degrades 4x.

❌ BAD:
```python
H_pilots = Y_pilots
# Range resolution = c
range_map = np.fft.ifft(H_pilots, axis=1)
```

✅ GOOD:
```python
# 2D OFDM radar processing using ALL subcarriers (pilot + data)
# Requires known or estimated data symbols (decision-directed approach)
X_all = np.concatenate([X_pilots, X_data_estimated], axis=1)
H_all = Y_all
range_map = np.fft.ifft(H_all, axis=1)  # Full range resolution c/(2B)
```

### Anti-Pattern 2: Neglecting Mutual Coupling in Dense ISAC Arrays

**Why it matters:** In dense antenna arrays (element spacing λ/4 at mmWave), mutual coupling between elements distorts the steering vector and causes 3-5 dB array gain loss and AoA estimation bias of 2-8°. MUSIC/ESPRIT assume ideal steering vectors — coupling violates this.

❌ BAD: Simulate ISAC with λ/2 spacing formula for an array physically realized at λ/4 spacing.

✅ GOOD:
```python
# Include coupling matrix C in signal model
# True received signal: x = C @ A(theta) @ s + n
# Calibrate C from anechoic chamber measurements
x_true = C_measured @ A_ideal @ s + noise
# Use coupling-aware MUSIC or calibration-based correction:
R_calibrated = np.linalg.inv(C_measured) @ R_measured @ np.linalg.inv(C_measured).conj().T
spectrum = music_spectrum(R_calibrated, N, N_src, theta_grid)
```

### Anti-Pattern 3: Ignoring the Doppler-Communication Frame Structure Mismatch

**Why it matters:** 5G NR slots (0.5ms at 120 kHz SCS) are designed for communication latency, not radar coherence. To achieve Δv = 1 m/s at 28 GHz, we need T_cpi ≥ λ/(2Δv) = 5.3ms — requiring 10+ NR slots to be jointly processed. Communication scheduling must freeze user data interleaving for this duration, creating a latency hit.

❌ BAD: Design ISAC assuming radar CPI can arbitrarily span multiple slots without impact on scheduling.

✅ GOOD: Negotiate CPI duration with scheduler; use burst-mode sensing (10 slots dedicated every 50ms) to amortize latency; communicate the radar sensing interrupt interval to upper layers.

### Anti-Pattern 4: Reporting Only Pd at High SNR

**Why it matters:** Detection probability (Pd) at SNR = 20 dB is trivially 1.0 for all detectors. The meaningful range is SNR = -10 to +10 dB. Reporting only high-SNR performance hides threshold behavior and makes all detectors appear equivalent.

❌ BAD: "Our algorithm achieves Pd = 0.99 at Pfa = 10^-6." (Without reporting what SNR this requires.)

✅ GOOD:
```
Table: Detection Performance at Pfa = 10^-6 (1000 Monte Carlo trials)
SNR (dB) | CA-CFAR Pd | OS-CFAR Pd | Proposed ISAC-CFAR Pd
---------|------------|------------|----------------------
-5       | 0.12       | 0.08       | 0.21
0        | 0.45       | 0.38       | 0.56
5        | 0.82       | 0.79       | 0.88
10       | 0.99       | 0.97       | 0.99
Report SNR_50 (SNR for Pd=0.5) as key figure of merit: proposal improves by 1.5 dB
```

### Anti-Pattern 5: Solving the Joint ISAC Problem Sequentially Instead of Jointly

**Why it matters:** Sequential design (first optimize communication beamformer, then fit radar waveform into leftover null space) achieves a suboptimal interior point of the SINR-SCNR trade-off region — typically 3-8 dB below the Pareto-optimal joint solution.

❌ BAD:
```python
W_comm = compute_communication_beamformer(H_users, P_total)  # Step 1: comms
# Step 2: radar waveform in null space of W_comm — constrained, suboptimal
W_radar = null_space_projection(h_radar, W_comm)
```

✅ GOOD:
```python
# Joint alternating optimization — achieves Pareto-optimal SINR-SCNR trade-off
W_comm, W_radar = alternating_isac_optimization(
    H_users, h_radar, P_total, sinr_min_dB=15, n_iter=100
)
# Validated to be within 0.5 dB of global optimum (found by SDR exhaustive search)
```

---

