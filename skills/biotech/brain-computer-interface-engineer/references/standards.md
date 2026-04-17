## 7. Standards & Reference

**Key Performance Metrics:**

| Metric | Target | Measurement Method | Notes |
|--------|--------|-------------------|-------|
| Electrode impedance | <100 kΩ at 1 kHz | EIS (Gamry, Autolab) | Higher → worse SNR for recording |
| Input-referred noise | <5 µV RMS (0.3-5 kHz) | Short-circuit input test | INTAN RHD achieves 2.4 µV typical |
| Spike SNR | >5 dB (ratio peak-to-noise) | Spike-triggered average | Threshold units: SNR 3-5 dB |
| ISI violation rate | <2% (<3ms refractory) | Post-sort quality metric | >5% → multi-unit contamination |
| Decoding latency (motor BCI) | <50 ms end-to-end | Hardware timestamp measurement | ECoG: 20-30 ms typical |
| BIT rate (communication BCI) | >25 bits/minute | Wolpaw formula: B×log2(N)×(1-P) | P300 speller: 25-40 bits/min |
| Classification accuracy (n-class) | >85% online | Confusion matrix, k-fold CV | Report chance level explicitly |
| Cross-session accuracy | >80% at Day 7 | Without recalibration | Key clinical viability criterion |
| Charge injection limit | <30 µC/cm² per phase | Platinum; per Shannon curve | PEDOT:PSS allows higher: ~75 µC/cm² |

**Regulatory and Standards Framework:**

| Standard | Scope | Key Requirements |
|----------|-------|-----------------|
| ISO 14708-1 | Active implantable medical devices | Hermeticity, EMC, MRI safety, functional safety |
| ISO 10993-1/5 | Biocompatibility | Cytotoxicity, sensitization, hemocompatibility testing |
| ISO 14971 | Risk management | FMEA, risk acceptability matrix, residual risk evaluation |
| FDA 510(k) | Class II EEG/ECoG devices | Substantial equivalence to predicate; EEG headset = wellness |
| FDA PMA | Class III intracortical BCIs | Clinical trial data; NeuroPort Array (Blackrock) as precedent |
| IEC 60601-1-2 | EMC for medical electrical equipment | Immunity to radiated/conducted interference from MRI, defibrillators |
| IEEE P2510 | Neural interface data quality | Draft standard for neural data format and quality metrics |

---

