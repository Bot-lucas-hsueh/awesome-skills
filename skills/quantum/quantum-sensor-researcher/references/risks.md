## § 3 — Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|-------------------|------------|
| Systematic error dominates statistical precision at long integration times | CRITICAL | Sensor reports high precision but biased measurements; navigation or geodesy applications corrupted | Characterize all systematic shifts with comparable accuracy to claimed statistical precision; use differential measurements to reject common-mode systematics |
| Quantum advantage overclaim from squeezing | HIGH | Squeezed-state sensitivity gains erased by detection loss/efficiency; misleads quantum sensor roadmaps | Compute effective sensitivity including detection efficiency η: δφ_eff = 1/√(η·N·ξ²); require η > 0.95 for meaningful squeezing benefit |
| Laser phase noise contaminating inertial signal | HIGH | Laser frequency noise aliased into acceleration/gravity measurement; spurious signals at mHz–Hz | Implement differential interferometry (gravity gradiometer) to reject common-mode laser noise; use ultra-stable reference cavities (< 0.01 Hz linewidth) |
| Vibration coupling in field-deployable sensors | HIGH | Platform vibration mimics inertial signal; limits sensitivity to ppm level without isolation | Implement vibration rejection via seismometer feedforward; design common-mode rejection in gradiometer baseline |
| Magnetic field systematic in atom interferometry | MEDIUM | Second-order Zeeman shift biases acceleration measurement; drift in ambient B causes bias drift | Apply bias magnetic field > 1 Gauss to suppress mF = 0 sensitivity; implement magnetic shielding to < 1 nT ambient field |
| Cold atom sample heating and loss | MEDIUM | Three-body recombination and off-resonant scattering reduce atom number below SQL-limited regime | Monitor atom number per cycle; maintain density below 10^12 atoms/cm³; use far-detuned dipole traps for long interrogation times |
| SQUID flux jumps and hysteresis in high fields | MEDIUM | SQUID locks to wrong flux quantum; measurement bias introduced without detection | Implement flux-locked loop with range monitoring; include flux jump detection algorithm; characterize SQUID linearity range |

---
