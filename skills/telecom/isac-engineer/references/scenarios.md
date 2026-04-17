## 9. Scenario Examples

### Example 1: Designing an OFDM-ISAC Waveform for 5G NR Vehicle Sensing

**User:** We want to use an existing 5G NR base station (28 GHz, 100 MHz BW, 4 TX antennas) as a DFRC system to simultaneously serve 4 UE downlink users and detect vehicles at up to 200m range. How do we design this?

**ISAC Engineer:**
Excellent application — this is precisely the 3GPP TR 22.837 urban vehicular sensing scenario. Let me design it systematically.

**Step 1 — Resolution analysis:**
- Range resolution: Δr = c/(2B) = 3×10⁸/(2×100×10⁶) = 1.5m (adequate for vehicle detection)
- Max unambiguous range: R_max = c×T_OFDM/(2) where the OFDM symbol period is cyclic. Using slot duration T_slot = 0.5ms at 28 GHz numerology 2 (120 kHz SCS): max unambiguous range ≈ 75km (not a constraint)
- Doppler resolution: Δv = λ/(2×T_cpi) = 0.0107/(2×0.005) = 1.07 m/s with 5ms CPI (10 NR slots)
- Angular resolution: Δθ ≈ 0.0107/(4×0.00535) = 50° — poor with 4 antennas; recommend 16 antennas for <15° resolution

**Step 2 — NR reference signals as radar waveform:**
Reuse NR downlink reference signals (CSI-RS or PDSCH DMRS) as the sensing waveform. The OFDM processing pipeline:

```python
import numpy as np

def ofdm_isac_radar_processing(rx_signal, tx_reference, N_fft, N_subcarriers,
                                 N_symbols, subcarrier_spacing_Hz, carrier_freq_Hz):
    """
    OFDM-ISAC radar processing: extract range-Doppler map.
    rx_signal: [N_symbols, N_fft] received time-domain OFDM symbols
    tx_reference: [N_symbols, N_subcarriers] known transmitted OFDM data/pilots
    """
    c = 3e8
    lambda_c = c

    # Step 1: OFDM demodulation — FFT of each received symbol
    Y = np.fft.fft(rx_signal, N_fft, axis=1)[:, :N_subcarriers]  # [N_symbols, N_sc]

    # Step 2: Element-wise division to get channel estimate per symbol per subcarrier
    # H[k, l] = Y[k, l]
    H = Y

    # Step 3: 2D IFFT to get range-Doppler map
    # IFFT over subcarrier axis -> range; FFT over symbol axis -> Doppler
    rd_map = np.fft.fftshift(
        np.fft.fft(np.fft.ifft(H, axis=1), axis=0),
        axes=0
    )  # [N_symbols, N_sc]

    # Step 4: Compute range and Doppler axes
    delta_r = c
    range_axis = np.arange(N_subcarriers) * delta_r  # [m]
    delta_v = lambda_c / (2 * N_symbols
    doppler_axis = np.fft.fftshift(np.arange(N_symbols) - N_symbols//2) * delta_v

    return np.abs(rd_map)**2, range_axis, doppler_axis

# NR numerology 2 at 28 GHz: 120 kHz SCS, 1 slot = 14 OFDM symbols = 0.125 ms
rd_power, ranges, velocities = ofdm_isac_radar_processing(
    rx_signal, tx_ref,
    N_fft=1024, N_subcarriers=66*12,  # 66 RBs × 12 subcarriers
    N_symbols=140,  # 10 slots × 14 symbols/slot
    subcarrier_spacing_Hz=120e3,
    carrier_freq_Hz=28e9
)
```

**Step 3 — Joint beamforming:** With 4 TX antennas serving 4 UE users, all spatial degrees of freedom are consumed for communication. For sensing, embed the radar waveform in the null space of the communication beamformer:
```
W_total = W_comm + W_radar
W_radar: designed such that H_user @ W_radar ≈ 0 (zero forcing to UE directions)
```
This ensures communication SINR is unaffected while the radar beam illuminates the sensing zone.

**Step 4 — CFAR detection:** Apply 2D CA-CFAR to the range-Doppler map with guard cells [2, 2] and training cells [8, 8] around each cell; target Pfa = 10⁻⁶ yields threshold factor α derived from CFAR theory.

### Example 2: MUSIC Algorithm for Angle-of-Arrival Estimation

**User:** We have an 8-element ULA and want to implement MUSIC for AoA estimation of 2 targets. Show me the full implementation and how to compare against the CRB.

**ISAC Engineer:**
Complete MUSIC implementation with CRB verification:

```python
import numpy as np
import matplotlib.pyplot as plt

def ula_steering_vector(theta_deg, N_elements, d_lambda=0.5):
    """ULA steering vector at angle theta (degrees), N elements, spacing d (in wavelengths)."""
    theta_rad = np.deg2rad(theta_deg)
    n = np.arange(N_elements)
    return np.exp(1j * 2 * np.pi * d_lambda * n * np.sin(theta_rad))

def music_spectrum(R_xx, N_elements, N_sources, theta_search_deg, d_lambda=0.5):
    """
    MUSIC spatial spectrum estimation.
    R_xx: [N, N] sample covariance matrix
    N_sources: number of sources (must be known or estimated via MDL/AIC)
    Returns: MUSIC pseudospectrum (normalized)
    """
    # Eigendecomposition of covariance matrix
    eigenvalues, eigenvectors = np.linalg.eigh(R_xx)
    # Sort in descending order
    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, idx]

    # Noise subspace: eigenvectors corresponding to N-K smallest eigenvalues
    E_noise = eigenvectors[:, N_sources:]  # [N, N-K]

    # MUSIC spectrum: 1
    spectrum = np.zeros(len(theta_search_deg))
    for i, theta in enumerate(theta_search_deg):
        a = ula_steering_vector(theta, N_elements, d_lambda)
        a = a
        projection = a.conj() @ E_noise
        spectrum[i] = 1.0

    return spectrum

def cramer_rao_bound_angle(theta_deg, N_elements, N_snapshots, SNR_linear, d_lambda=0.5):
    """
    CRB for AoA estimation with ULA (single source, AWGN).
    Returns standard deviation in degrees.
    """
    theta_rad = np.deg2rad(theta_deg)
    # Derivative of steering vector w.r.t. theta
    n = np.arange(N_elements)
    a_dot = 1j * 2 * np.pi * d_lambda * np.cos(theta_rad) * n * \
            np.exp(1j * 2 * np.pi * d_lambda * n * np.sin(theta_rad))

    a = np.exp(1j * 2 * np.pi * d_lambda * n * np.sin(theta_rad))

    # FIM element: 2 * SNR * N_snapshots * ||P_perp a_dot||^2
    # where P_perp = I - a*a^H/N
    P_perp_a_dot = a_dot - (a.conj() @ a_dot)
    FIM = 2 * SNR_linear * N_snapshots * np.real(P_perp_a_dot.conj() @ P_perp_a_dot)
    CRB_rad = 1.0
    return np.rad2deg(np.sqrt(CRB_rad))

# Example: 8-element ULA, 2 targets at [-10°, 20°], SNR = 15 dB
N = 8;  N_src = 2;  N_snap = 200;  SNR_dB = 15
SNR = 10**(SNR_dB
true_angles = [-10.0, 20.0]

# Generate synthetic received signal
A = np.column_stack([ula_steering_vector(t, N) for t in true_angles])
S = (np.random.randn(N_src, N_snap) + 1j * np.random.randn(N_src, N_snap))
noise_power = 1.0
X = A @ S + np.sqrt(noise_power/2) * (np.random.randn(N, N_snap) + 1j*np.random.randn(N, N_snap))

# Sample covariance matrix
R_xx = (X @ X.conj().T)

# Compute MUSIC spectrum
theta_grid = np.linspace(-90, 90, 1801)
spectrum = music_spectrum(R_xx, N, N_src, theta_grid)

# CRB for each target
for theta_t in true_angles:
    crb_std = cramer_rao_bound_angle(theta_t, N, N_snap, SNR)
    print(f"Target at {theta_t}°: CRB std dev = {crb_std:.4f}°")

# Typical output: CRB std dev ≈ 0.08° at 15 dB SNR, 8 elements, 200 snapshots
# MUSIC peak location std dev ≈ 0.09-0.11° (within 3 dB of CRB)
```

**CRB interpretation:** At SNR = 15 dB with 8 elements and 200 snapshots, the CRB gives σ_θ ≈ 0.08°. MUSIC typically achieves 0.09-0.11° — within 1.5 dB of CRB, confirming it is an efficient estimator above the threshold SNR (~5 dB for 2 sources, 8 elements).

**Key warning:** MUSIC breaks down below threshold SNR — eigenvector perturbation causes "noise subspace leakage" into signal subspace. Below threshold, use root-MUSIC or SPA (Sparse Bayesian learning) which are more robust.

### Example 3: Anti-Pattern — Maximizing Radar SCNR Without Communication QoS Constraint

**User:** We want to maximize radar SCNR by using all 4 BS antennas as a phased array toward the target, while also transmitting to 2 users. Can we just design the best radar beam and then add communication on top?

**ISAC Engineer:**
No — this approach maximizes SCNR greedily and will violate communication QoS. Here is why and the correct formulation.

**Why the greedy approach fails:**
If you design W_radar to maximize SCNR first (beamform all power toward target at 30°), then the communication beamformer W_comm must operate in the residual null space. With only 4 antennas and 2 users at different angles plus 1 radar direction, the null-space projection leaves insufficient degrees of freedom — communication SINR will drop below QoS threshold.

**The correct formulation (SINR-constrained SCNR maximization):**
```
maximize     SCNR = |h_r^H W_r s_r|^2
subject to   SINR_k = |h_k^H w_c,k|^2
             Σ_k ||w_c,k||^2 + ||W_r||_F^2 ≤ P_total
```

**CVX implementation:**
```python
import cvxpy as cp
import numpy as np

def isac_beamformer_design(H_comm, h_radar, P_total, sinr_min_dB, noise_power=1.0):
    """
    ISAC joint beamformer: maximize SCNR subject to communication SINR constraints.
    H_comm: [N_users, N_tx] communication channel matrix
    h_radar: [N_tx,] radar channel (steering vector toward target)
    """
    N_tx = H_comm.shape[1]
    N_users = H_comm.shape[0]
    gamma = 10**(sinr_min_dB

    # Semidefinite relaxation: W_k = w_k @ w_k^H -> rank-1 PSD matrix
    W_comm = [cp.Variable((N_tx, N_tx), hermitian=True) for _ in range(N_users)]
    W_radar = cp.Variable((N_tx, N_tx), hermitian=True)

    # Radar beampattern: h_r^H W_r h_r (SCNR numerator)
    scnr_numerator = cp.real(h_radar.conj() @ W_radar @ h_radar)

    # Communication SINR constraints
    constraints = []
    for k in range(N_users):
        h_k = H_comm[k, :]
        signal_k = cp.real(h_k.conj() @ W_comm[k] @ h_k)
        interference_k = sum(cp.real(h_k.conj() @ W_comm[j] @ h_k)
                             for j in range(N_users) if j != k)
        # Also include radar interference at communication receiver
        radar_intf_k = cp.real(h_k.conj() @ W_radar @ h_k)
        sinr_k = signal_k
        constraints.append(sinr_k >= gamma)
        constraints.append(W_comm[k] >> 0)  # PSD constraint

    constraints.append(W_radar >> 0)
    constraints.append(
        sum(cp.trace(W_comm[k]) for k in range(N_users)) +
        cp.trace(W_radar) <= P_total
    )

    prob = cp.Problem(cp.Maximize(scnr_numerator), constraints)
    prob.solve(solver=cp.MOSEK)

    return [W_comm[k].value for k in range(N_users)], W_radar.value, prob.value
```

**Pareto front visualization:** Run `isac_beamformer_design` sweeping `sinr_min_dB` from 0 to 25 dB; plot achieved SCNR vs SINR constraint to obtain the Pareto front. This reveals the exact operating point trade-off and prevents greedily sacrificing QoS for sensing gain.

---

