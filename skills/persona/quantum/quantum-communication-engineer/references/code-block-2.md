# python Example

```
import numpy as np

def finite_key_bb84_skr(R_det, QBER, e_phase, N_block,
                          f_EC=1.10, epsilon=1e-10):
    """
    Finite-key BB84 SKR with composable security (simplified Scarani-Renner).
    N_block: number of pulses per key generation round (must be > 10^6)
    epsilon: composable security parameter (target < 10^-10)
    """
    h = lambda p: -p*np.log2(p+1e-15) - (1-p)*np.log2(1-p+1e-15)

    # Statistical fluctuation correction (Chernoff-Hoeffding bound)
    delta_stat = np.sqrt(-np.log(epsilon/2)

    # Finite-key correction terms
    QBER_upper = QBER + delta_stat   # worst-case QBER with finite statistics
    e_phase_upper = e_phase + delta_stat

    # Privacy amplification compression factor
    leak_EC = f_EC * N_block * h(QBER_upper)    # bits leaked in error correction
    leak_PA = N_block * h(e_phase_upper)          # bits consumed in privacy amplification

    # Finite-key correction: 6*sqrt(N)*log2(1/epsilon) term
    finite_correction = 6 * np.sqrt(N_block) * np.log2(1/epsilon)

    SKR_finite = R_det * (1 - h(QBER_upper) - h(e_phase_upper) - finite_correction)
    return max(0, SKR_finite)

# Compare asymptotic vs finite-key
R_det = 10000   # Hz detection rate
QBER = 0.02
e_phase = 0.025
N = 1e7         # 10 million pulses per block (10 ms at 1 GHz)

skr_asymptotic = R_det * (1 - (-0.02*np.log2(0.02) - 0.98*np.log2(0.98)) * 2)
skr_finite = finite_key_bb84_skr(R_det, QBER, e_phase, N)
print(f"Asymptotic SKR: {skr_asymptotic:.1f} bps")
print(f"Finite-key SKR: {skr_finite:.1f} bps")
print(f"Overestimation: {skr_asymptotic/skr_finite:.1f}x")
```
