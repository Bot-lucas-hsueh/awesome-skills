## § 10 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Overlooking Mixture Ratio Shift During Burn
**❌ BAD**: Designing propellant system with matched LOX and fuel tank sizes for nominal O/F, ignoring residuals
**✅ GOOD**: Design for mixture ratio variation over burn and account for residuals
```python
# Wrong: size tanks for exactly nominal O/F × propellant mass
fuel_volume = total_propellant / (1 + OF)
ox_volume = total_propellant * OF / (1 + OF)

# Right: account for mixture ratio uncertainty and residuals
OF_nominal = 2.72  # LOX/RP-1
OF_uncertainty = 0.05  # ±1.8% from nominal
residual_fraction = 0.005  # 0.5% residual per tank

# Design fuel tank for OF_min = 2.67 (more fuel consumed):
fuel_volume = total_propellant / (1 + OF_min)
# Design ox tank for OF_max = 2.77 (more oxidizer consumed):
ox_volume = total_propellant * OF_max / (1 + OF_max)
```
**Why it matters**: An engine that runs LOX-rich at end of burn will cause turbopump damage from hot gas; fuel-rich → reduced Isp + unburned fuel waste.

