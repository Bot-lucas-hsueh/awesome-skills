## § 3 · Risk Disclaimer

| Risk | Description | Mitigation |
|------|-------------|------------|
| **Quench** | Superconducting-to-resistive transition propagates thermally → stored magnetic energy (½LI²) dissipated in small volume → thermal runaway, conductor damage | Active quench protection: detect voltage (≥50 mV threshold), fire quench heaters, dump to external resistor in ≤100 ms; ensure minimum propagation velocity (MPV) analysis |
| **Cryogen Loss** | LHe or LN2 boil-off from quench → pressure rise → oxygen enrichment or asphyxiation hazard | Design cryostat with pressure relief valve (safety relief ≥ 3× normal boil-off rate); O2 monitors in confined spaces; establish quench ventilation protocol |
| **Irreversible Strain Damage** | REBCO tape irreversible degradation at tensile strain > 0.4% or compressive > 0.3% (Jc drops >5%) | Stress/strain analysis before winding; use conduit/react-and-wind for Nb3Sn (brittle A15 phase); maximum hoop stress < 150 MPa for REBCO |
| **Flux Jump Instability** | Adiabatic flux jump in large multifilamentary conductors at low field → premature quench | Filamentary geometry (filament diameter ≤ dj_critical = 18 μm for NbTi at 4.2 K); twist pitch ≤ 10 mm for AC applications |
| **Chemical Incompatibility** | Nb3Sn reacts with Cu stabilizer at reaction temperature (650°C) → alloying reduces RRR | Design proper barrier (Ta or Nb diffusion barrier); monitor RRR ≥ 100 after reaction; use internal tin process with Nb barrier |
