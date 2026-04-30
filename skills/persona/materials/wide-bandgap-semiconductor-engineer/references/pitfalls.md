# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|-------------|----------|-----------|
| 1 | **Applying Si IGBT gate drive voltage to SiC MOSFET** | 🔴 High | SiC requires +15V/-3V; +12V causes partial turn-on and overheating |
| 2 | **Ignoring GaN's 0V turn-off vulnerability** | 🔴 High | Always use -3V gate drive off; never leave GaN floating |
| 3 | **Designing SiC gate drive for 10Ω Rg like IGBT** | 🔴 High | SiC needs Rg = 2–10 Ω to control di/dt and overshoot |
| 4 | **Using SiC body diode as primary freewheeling element** | 🔴 High | Add SiC Schottky in parallel; body diode Qrr causes losses and heating |
| 5 | **Mounting GaN without thermal simulation** | 🟡 Medium | GaN has different thermal path; simulate Tj with FEA |
| 6 | **Assuming GaN is immune to avalanche** | 🟡 Medium | Unclamped inductive switch (UIS) destroys GaN — always use ZVS or clamping |

## 10.2 Best Practices

1. **Kelvin source connection** — mandatory for GaN; separates gate and power loops
2. **Separate gate and power inductances** — gate loop inductance < 5 nH
3. **Use AEC-Q101 qualified devices** for automotive/industrial
4. **Double pulse test at operating temperature** — never extrapolate from 25°C data
5. **Snubber design** — RC or RCD snubber across each switch for SiC; RC for GaN
6. **EMI early design-in** — CM filter geometry from day one of schematic
7. **Body diode monitoring** — implement forward voltage sense in redundant systems

## 10.3 Quality Checklist

- [ ] Double pulse test completed at Tj = 25°C and Tj = max operating temp
- [ ] Gate overshoot < 1V above Vgs(on); undershoot > -5V (SiC) or > -4V (GaN)
- [ ] Thermal simulation confirms Tj < 80% Tj_max under worst-case load
- [ ] dv/dt at switch node < device rating (typically 50 V/ns for SiC, 100 V/ns for GaN)
- [ ] EMI pre-compliance test passed at CISPR 32 Class B with 6 dB margin
- [ ] HTRB/HTCG reliability data reviewed from manufacturer qualification report
- [ ] Gate drive isolation verified: 1500V isolation for 800V systems
- [ ] Short-circuit protection verified: 10 µs desaturation detection time
- [ ] Body diode Qrr measured and within design budget (SiC)
- [ ] All SiC/GaN-specific Spice models validated against device datasheet
