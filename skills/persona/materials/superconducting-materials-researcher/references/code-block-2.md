# python Example

```
import numpy as np

def kim_model_Jc(B, T, Jc0, B0, Tc, n=1.0):
    """
    Modified Kim model for Jc(B,T):
    Jc(B,T) = Jc0 * (1 - T/Tc)^n / (1 + B/B0)
    Jc0: Jc at B=0, T=0 (A/mm²)
    B0: characteristic field (T) — fitted from data
    n: temperature exponent (typically 1.5-2.0 for LTS, 1.0-2.0 for HTS)
    """
    t = T
    return Jc0 * (1 - t)**n / (1 + B

# Fit to experimental NbTi data
from scipy.optimize import curve_fit

# Experimental: Jc at 4.2K vs field (A/mm²)
B_exp = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])  # Tesla
Jc_exp = np.array([3800, 3400, 2900, 2400, 1900, 1400, 900, 450, 150])  # A/mm²

# Fit at T = 4.2 K
T_op = 4.2; Tc_NbTi = 9.2
popt, pcov = curve_fit(
    lambda B, Jc0, B0: kim_model_Jc(B, T_op, Jc0, B0, Tc_NbTi),
    B_exp, Jc_exp, p0=[5000, 2.5]
)
print(f"NbTi Kim fit: Jc0={popt[0]:.0f} A/mm², B0={popt[1]:.2f} T")

# Predict Jc at 5T, 4.2K:
Jc_pred = kim_model_Jc(5, 4.2, popt[0], popt[1], Tc_NbTi)
print(f"Predicted Jc(5T, 4.2K) = {Jc_pred:.0f} A/mm²")
```
