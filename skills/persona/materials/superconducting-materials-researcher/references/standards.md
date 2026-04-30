# Standards & Reference

## 7.1 Official Documentation

- [NIST Superconducting Materials Database](https://mgi.nist.gov/material-property-data/superconducting-materials)
- [IOP Superconductor Science and Technology](https://iopscience.iop.org/journal/0953-2048)
- [APS Physical Review Applied — Superconductivity](https://journals.aps.org/prapplied/)
- [arXiv: Condensed Matter — Superconductivity](https://arxiv.org/list/cond-mat.supr-con/recent)
- [US DOE Basic Energy Sciences — Superconducting Materials Research](https://science.osti.gov/bes)

## 7.2 Key Material Standards

| Standard | Scope | Key Requirements |
|----------|-------|------------------|
| **ASTM B713** | Standard specification for Nb₃Sn superconducting wire | RRR >100, non-Cu Jc >690 A/mm² at 12T, 4.2K |
| **ASTM F76** | Measuring residual resistivity ratio of NbTi and Nb₃Sn | RRR measurement protocol for strand quality |
| **IEC 61788** | Superconductivity — Part 4: Persistent current HTS magnets | Stability criteria, quench protection |
| **JEDEC JESD87** | General specification for NbTi superconducting wire | Lot acceptance testing protocols |
| **IRDS (IEEE)** | International Roadmap for Devices and Systems | Superconductor technology projections |
| **IHEP Technical Standards** | High-field magnet specifications | Field quality, training cycles |

## 7.3 Critical Performance Parameters

| Parameter | Low-Tc (Nb₃Sn) | High-Tc (REBCO) | Units |
|-----------|---------------|-----------------|-------|
| Max operating temperature | 4.2 K | 4.2–77 K (depending) | K |
| Upper critical field (Hc2) | 30–35 T | >100 T | T |
| Critical current density (Jc) | 2,000–3,000 A/mm² | 1,000–5,000 A/mm² (4K) | A/mm² |
| Residual resistivity ratio (RRR) | >100 required | >50 recommended | — |
| Filament diameter | 20–100 µm | 2–5 µm (coated conductor) | µm |
| Strain limit (reversible) | 0.2–0.3% | 0.4–0.6% | % |
| Magnet field range | Up to 16 T (react&wind) | Up to 30+ T (no-insulation) | T |

## 7.4 Testing & Certification Protocols

| Test | Method | Acceptance Criteria |
|------|--------|---------------------|
| Critical current (Ic) | 4-probe transport at 4.2K, self-field | Ic > 95% of specification; n-value > 20 |
| RRR | Cryogenic residual resistivity / RT resistivity | RRR > 100 (Nb₃Sn); > 50 (REBCO) |
| Twisted filament test | Ic measurement after twist | < 5% Ic degradation |
| HTS coil quench test | Heat pulse propagation test | Detect quench, protect winding |
| Stress-strain test | Tensile/compressive cycling | Reversible strain < 0.2% |
