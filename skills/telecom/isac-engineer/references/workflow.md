## 8. Standard Workflow

### Phase 1 — ISAC System Specification and Trade-off Analysis

**Steps:**
1. Specify the dual use-case: communication link (users, data rate, SINR target) and radar task (range, velocity, angle estimation accuracy, detection probability).
2. Compute fundamental range/Doppler/angular resolution from hardware parameters (bandwidth B, observation time T, aperture N×d).
3. Derive CRB for each sensing parameter at target SNR; establish this as performance floor.
4. Map the SINR-SCNR Pareto front by sweeping the power allocation ratio α (fraction to sensing) from 0 to 1; record achievable communication rate and SCNR at each point.
5. Select the operating point: typically the "knee" of the Pareto front where marginal SCNR gain per dB of SINR sacrifice is equal to 1.

**[✓ Done]** criteria: Pareto front plotted; CRB derived for all sensing parameters; operating point selected with explicit justification of SINR-SCNR trade-off.
**[✗ FAIL]** criteria: Operating point is below the Pareto front (suboptimal) — implement proper joint optimization before proceeding.

### Phase 2 — Waveform and Beamformer Design

**Steps:**
1. Select waveform type: OFDM-ISAC for static/low-mobility targets with communication infrastructure reuse; OTFS-ISAC for high-mobility (V2X, UAV) targets with Doppler spread >100 Hz.
2. Design ambiguity function: compute |χ(τ, f_d)|² for the proposed waveform; verify range and Doppler sidelobes meet the false alarm requirement.
3. Formulate joint ISAC beamforming problem: maximize SCNR subject to per-user SINR ≥ γ_min, per-antenna power ≤ P_max.
4. Solve via alternating optimization: fix radar beamformer W_r, optimize communication beamformer W_c via WMMSE; then fix W_c, optimize W_r via SCA; iterate until convergence (<50 iterations typical).
5. Validate solution via Monte Carlo (1000 realizations): measure achieved SINR distribution and SCNR distribution; verify both meet specifications at 95th percentile.

**[✓ Done]** criteria: Joint beamformer achieves specified SINR ≥ γ_min for all users; SCNR within 3 dB of CRB limit; ambiguity function sidelobes ≤ -30 dB.
**[✗ FAIL]** criteria: SINR constraint infeasible — system is overloaded; reduce user count, increase transmit power, or relax radar SCNR requirement.

### Phase 3 — Prototype Validation and Performance Report

**Steps:**
1. Implement ISAC transceiver on USRP: configure waveform (OFDM parameters, pilot structure), calibrate IQ imbalance, measure noise floor, verify transmit spectrum mask compliance.
2. Conduct sensing measurement: place RF reflector at known range/angle; process received echo through range-Doppler processing and MUSIC/ESPRIT; compare estimated parameters to truth.
3. Conduct communication measurement simultaneously: demodulate received data symbols; measure EVM and compute effective SNR; compare to simulation prediction.
4. Compute achieved CRB operating point from measured SNR; verify algorithm is within 3 dB of CRB.
5. Document reproducibility: hardware config file, calibration data, measurement protocol, analysis code.

**[✓ Done]** criteria: Measured sensing MSE within 3 dB of CRB at specified SNR; communication BER matches simulation within 1 dB; results reproducible across 3 independent measurement runs.
**[✗ FAIL]** criteria: >5 dB gap between measured and simulated performance — investigate calibration errors, synchronization offset, or unmodeled clutter; do not proceed to publication without resolving gap.

---

