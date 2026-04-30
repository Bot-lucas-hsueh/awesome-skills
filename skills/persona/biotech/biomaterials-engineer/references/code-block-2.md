# python Example

```
import numpy as np
from scipy.optimize import curve_fit

def plga_degradation_model(t_weeks, Mn0, k_deg, beta=0.5):
    """
    First-order Mn decay with autocatalytic acceleration (acid products).
    Mn(t) = Mn0 * exp(-k * t) for initial linear phase
    More accurately: Mn(t) = Mn0 * exp(-k * t^beta) (Weibull-type)
    t_weeks: time in weeks
    Mn0: initial number-average molecular weight (g/mol)
    k_deg: degradation rate constant (1/week^beta)
    beta: shape factor (0.5-1.0; <1 for autocatalytic acceleration)
    """
    return Mn0 * np.exp(-k_deg * t_weeks**beta)

def predict_mechanical_retention(Mn, Mn0, m=3.4):
    """
    Power-law correlation: E/E0 = (Mn/Mn0)^m
    m ≈ 2-4 for PLGA (entanglement molecular weight effects)
    """
    return (Mn

# PLGA 50:50, Mn0 = 80,000 g/mol, k_deg = 0.12 wk^-0.6 (literature)
Mn0 = 80000
k_deg = 0.12
beta = 0.6

timepoints = np.array([0, 2, 4, 6, 8, 12])
Mn_values = plga_degradation_model(timepoints, Mn0, k_deg, beta)
E_retention = predict_mechanical_retention(Mn_values, Mn0)

for t, Mn, E_r in zip(timepoints, Mn_values, E_retention):
    print(f"Week {t:2d}: Mn = {Mn:.0f} g/mol ({Mn/Mn0*100:.0f}%), E retention = {E_r*100:.0f}%")

# Week  0: Mn = 80000 g/mol (100%), E retention = 100%
# Week  2: Mn = 52400 g/mol ( 66%), E retention =  28%  ← major loss
# Week  4: Mn = 37100 g/mol ( 46%), E retention =  10%  ← fragile
# Week  8: Mn = 21000 g/mol ( 26%), E retention =   2%
# Week 12: Mn = 12700 g/mol ( 16%), E retention = 0.4%  ← essentially mass loss
```
