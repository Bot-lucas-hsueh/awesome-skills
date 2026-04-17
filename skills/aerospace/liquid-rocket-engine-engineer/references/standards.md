## § 7 Standards & Reference

### Performance Reference by Propellant Combination
| Propellant (O/F) | Pc (bar) | Isp_vac (s) | T_chamber (K) | c* (m/s) | Application |
|-----------------|----------|-------------|--------------|----------|-------------|
| LOX/LH2 (6.0) | 200 | 455 | 3,400 | 2,430 | Upper stages (RL-10, J-2X, Vinci) |
| LOX/LH2 (6.0) | 100 | 442 | 3,350 | 2,420 | Same; lower Pc version |
| LOX/RP-1 (2.72) | 200 | 358 | 3,670 | 1,780 | First stages (Merlin, NK-33) |
| LOX/CH4 (3.6) | 300 | 380 | 3,540 | 1,900 | Raptor 3, BE-4 |
| NTO/MMH (2.1) | 70 | 340 | 3,280 | 1,720 | Spacecraft (Apollo SPS, Draco) |
| N2H4 monoprop | — | 230 | 1,000 | 1,100 | Attitude control thrusters |

### Critical Sizing Equations
```python
# Characteristic velocity (c*)
c_star = sqrt(gamma * R_specific * T_chamber)
         sqrt((2/(gamma+1))**((gamma+1)/(gamma-1)))  # Theoretical

# Thrust coefficient (CF)
CF = sqrt(2*gamma**2/(gamma-1) * (2/(gamma+1))**((gamma+1)/(gamma-1)) * \
     (1 - (Pe/Pc)**((gamma-1)/gamma))) + (Pe-Pa)/Pc * epsilon
# where epsilon = Ae/At (area ratio)

# Specific impulse
Isp_vac = CF * c_star

# Characteristic length (L*)
L_star = V_chamber
# Low L* → incomplete combustion; high L* → excess heat loss
```

