# python Example

```
# Scaffold design: PLGA 75:25 (slower degradation than 50:50)
# Manufacturing: solvent casting + particulate leaching (NaCl, 250-425 μm sieved)

# BMP-2 loading via adsorption or heparin immobilization
def bmp2_release_higuchi(t_hours, Q_inf, k_h):
    """
    Higuchi model for drug release from porous matrix.
    Q(t) = k_H * sqrt(t)  (valid while Q < 0.6 * Q_total)
    Q_inf: total BMP-2 loaded (ng)
    k_h: Higuchi constant (ng/h^0.5)
    """
    Q = k_h * np.sqrt(t_hours)
    return min(Q, 0.60 * Q_inf)  # Higuchi valid to 60% release

# Korsmeyer-Peppas for anomalous transport
def bmp2_release_korsmeyer(t_hours, Q_inf, k_kp, n):
    """
    Mt/Minf = k * t^n
    n = 0.5: Fickian diffusion; n = 1.0: Case II transport; 0.5 < n < 1: anomalous
    """
    return Q_inf * k_kp * t_hours**n

# Fit to experimental BMP-2 release data
t_exp = np.array([1, 4, 24, 72, 168, 336])  # hours
Q_exp = np.array([0.08, 0.18, 0.35, 0.52, 0.68, 0.80]) * 5000  # ng (fraction × total)

popt, _ = curve_fit(lambda t, k, n: bmp2_release_korsmeyer(t, 5000, k, n),
                    t_exp, Q_exp, p0=[0.05, 0.5], bounds=(0, [1, 1]))
print(f"Korsmeyer-Peppas fit: k={popt[0]:.4f}, n={popt[1]:.3f}")
print("n < 0.5: sub-Fickian (slow diffusion limited)")
print("n ≈ 0.5: Fickian diffusion")
print("0.5 < n < 1: anomalous (combined diffusion + erosion)")
```
