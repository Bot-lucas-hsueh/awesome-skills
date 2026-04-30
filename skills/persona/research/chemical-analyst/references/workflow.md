# Common Workflow Issues & Troubleshooting

## 8.1 HPLC Troubleshooting

| Problem | Symptom | Root Cause | Solution |
|---------|---------|-----------|----------|
| **High back pressure** | Pressure >200 psi above normal | Column contamination, blocked frit, particles | Replace column, backflush frit, filter samples |
| **Pressure fluctuation** | Variable pressure during run | Air bubbles, worn pump seals, leaking seals | Purge system, replace seals, check connections |
| **Peak tailing** | Asymmetric peak | Active sites on column, bad solvent, overloading | Regenerate column, use different solvent, reduce injection volume |
| **Peak broadening** | Wide peaks, loss of resolution | Column degradation, wrong mobile phase, temperature | Replace column, adjust mobile phase, control column temp |
| **No peaks** | Blank chromatogram | Detector issue, wrong wavelength, no analyte | Check detector, verify wavelength, confirm injection |
| **Split peaks** | Double-headed peaks | Column contamination, injection solvent mismatch | Clean column, match injection solvent to mobile phase |
| **Baseline drift** | Rising/falling baseline | Temperature instability, dirty detector, mobile phase issue | Thermostat detector, clean flow cell, fresh mobile phase |
| **Ghost peaks** | Peaks in blank runs | Contaminated solvents, dirty autosampler, carryover | Use fresh HPLC-grade solvents, clean injector, include blank |

## 8.2 GC-MS Troubleshooting

| Problem | Symptom | Root Cause | Solution |
|---------|---------|-----------|----------|
| **No ion source** | No chromatogram, no signal | Filament burnt out, source dirty | Replace filament, clean source |
| **Column bleed** | High baseline at high temp | Column degradation, old column | Condition column, replace if excessive |
| **Poor peak shape** | Broad/tailed peaks | Active sites, overloading, column damage | Deactivate column, reduce injection, install new column |
| **Mass spectrum mismatch** | Library search poor | Co-elution, background interference, scan timing | Improve chromatography, subtract background, adjust scan range |
| **Sensitivity loss** | Reduced response | Dirty source, worn column, contaminated source | Clean source, condition/replace column |
| **Retention time shift** | RT varies between runs | Column aging, temperature variation, flow rate | Trim column, verify temp/flow, recalibrate |
| **Leaks** | Low vacuum, high air/water | Loose fittings, septum wear, ferrule damage | Tighten fittings, replace septum, replace ferrule |

## 8.3 ICP-MS Troubleshooting

| Problem | Symptom | Root Cause | Solution |
|---------|---------|-----------|----------|
| **High oxide levels** | CeO/Ce > 3% | Organic matrix, low plasma temp, high sample load | Add oxygen to plasma, increase RF power, dilute samples |
| **High doubly-charged ions** | Ba++/Ba++ > 3% | Low plasma energy | Increase RF power, adjust torch position |
| **Signal drift** | Response changes over time | Blocked cones, deposition on interface | Clean cones, use internal standard, clean interface |
| **Interferences** | Incorrect quantitation | Isobaric, polyatomic, matrix | Use collision/reaction cell, correct mathematically |
| **Memory effects** | Signal persists after sample | Contaminated uptake, long rinse | Increase rinse time, use internal standard, acid washes |
| **Cone deposits** | Brown/white buildup | Sample matrix, organic material | Clean cones, use matrix matching, dilute |

## 8.4 UV-Vis Spectrophotometer Issues

| Problem | Symptom | Root Cause | Solution |
|---------|---------|-----------|----------|
| **Stray light** | Absorbance too low at high values | Dirty optics, degraded lamp | Clean sample compartment, replace lamp |
| **Baseline noise** | Jittery scan | Lamp aging, electrical noise, poor grounding | Replace deuterium or tungsten lamp, check ground |
| **Wavelength accuracy** | Peaks at wrong wavelength | Lamp misalignment, grating issue | Recalibrate wavelength with standard filter |
| **Photometric accuracy** | Incorrect absorbance readings | Detector nonlinearity, stray light | Verify with NIST SRM, check stray light |
| **Baseline drift** | Rising baseline over time | Lamp warm-up, temperature change, dirty optics | Allow longer warm-up, control temperature, clean optics |

## 8.5 QC Failure Decision Tree

```
QC Failure Detected
        │
        ▼
Is the failure reproducible? ──No──► Rerun sample batch
        │ Yes
        ▼
Is CRM/LCS >15% from expected? ──Yes──► Investigate cause
        │ No                          (contamination, standard,
        ▼                              calculation error)
Is duplicate RPD >20%? ──Yes──► Check sample homogeneity
        │ No                          and instrument precision
        ▼
Is blank contaminated? ──Yes──► Re-extract samples
        │ No                          and rerun with clean
        ▼                              solvents
All other failures ────────────► Document investigation
                                   and corrective action
```

## 8.6 Method Transfer Troubleshooting

| Problem | Cause | Solution |
|---------|-------|---------|
| Results don't match | Differences in instrument, column, reagents | Use same lot numbers; match column dimensions; verify reagents |
| Precision poor at receiving lab | Training gap, instrument differences | Additional training; method optimization at receiving site |
| LOQ higher at receiving lab | Sensitivity differences | Optimize for receiving instrument; may need different approach |
| Different selectivity | Column chemistry differences | Specify exact column lot/manufacturer; validate selectivity |
| Acceptance criteria tight | Method not robust for differences | Re-evaluate acceptance criteria; add robustness testing |
