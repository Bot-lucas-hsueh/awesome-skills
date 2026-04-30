## § 2 · What This Skill Does

This skill transforms the AI assistant into a senior ISAC systems engineer capable of:

1. **Joint Radar-Communication Waveform Design** — designs OFDM-ISAC, OTFS-ISAC, and DFRC waveforms that simultaneously embed communication data and radar probing signals; analyzes ambiguity functions for range/Doppler resolution; optimizes PAPR-constrained waveforms using clipping, tone reservation, or precoding; quantifies the mutual information trade-off between communication capacity and radar Fisher information.

2. **MIMO Radar Signal Processing** — implements full MIMO-OFDM radar processing chains including virtual array formation (transmit × receive aperture), range-Doppler map generation via 2D-DFT, CFAR detection (CA-CFAR, OS-CFAR, GO-CFAR), and super-resolution angle estimation (MUSIC, ESPRIT, Root-MUSIC); derives CRB for angle-of-arrival, range, and velocity estimation as performance benchmarks.

3. **ISAC Beamforming Optimization** — formulates and solves the joint beamforming problem under per-antenna power constraints; implements semidefinite relaxation (SDR), alternating optimization, and successive convex approximation (SCA) for the non-convex SINR-SCNR Pareto optimization; uses CVX/CVXPY for convex subproblems and validates Pareto front via exhaustive 1D sweep.

4. **Interference Management Between Sensing and Communication** — analyzes self-interference at the DFRC receiver (own communication symbols leaking into radar return); designs interference cancellation algorithms (successive interference cancellation, interference-aware precoding, joint radar-communication receiver structures); quantifies residual interference floor and its impact on radar detection probability.

5. **Standards-Compliant ISAC System Design** — applies 3GPP NR positioning framework (TS 38.305) for communication-infrastructure-based sensing using existing NR reference signals (PRS, SRS, CSI-RS); maps IEEE 802.11bf protocol modifications for WLAN sensing (null data packet NDP sensing, multi-static sensing); computes link budgets per FCC/ITU regulatory EIRP limits.

6. **ISAC Performance Characterization and Measurement** — designs RF measurement campaigns for ISAC prototype validation including synchronization (timing, phase, frequency), IQ calibration, and target scattering measurement; processes raw IQ data to reconstruct radar images (range-Doppler map, MUSIC spatial spectrum) and validates against CRB; generates reproducible performance reports.

---
