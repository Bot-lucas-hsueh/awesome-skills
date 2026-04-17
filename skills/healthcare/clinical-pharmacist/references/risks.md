## § 3 · Risk Disclaimer

**Educational and reference information only. All clinical decisions require a licensed healthcare provider with access to the patient's complete medical record.**

| Risk | Mitigation |
|------|------------|
| Significant drug interactions | Classify severity; consult prescriber for contraindicated/major interactions |
| Narrow therapeutic index drugs | Therapeutic drug monitoring; conservative dose changes with close follow-up |
| Renal/hepatic dosing errors | Always calculate CrCl with patient-specific weight, age, sex, SCr |
| Beers Criteria medications in elderly | Discuss risk/benefit with prescriber; consider safer alternatives |

## 🤖 Core Framework

**Drug Interaction Assessment — 4-Step:**
```
Step 1: Identify mechanism (PK: CYP450, P-gp, UGT vs. PD: additive/synergistic/antagonistic)
Step 2: Classify severity (Contraindicated | Major | Moderate | Minor)
Step 3: Assess clinical significance (therapeutic index, dose, patient factors)
Step 4: Recommend action (avoid | monitor + specify | dose adjust | no action needed)
```

**Renal Dose Adjustment (Cockcroft-Gault):**
```python
def cockcroft_gault_crcl(age, weight_kg, scr_mg_dL, sex):
    """
    Cockcroft-Gault equation for creatinine clearance (mL/min).
    sex: 'M' for male, 'F' for female (0.85 correction factor)
    """
    sex_factor = 1.0 if sex.upper() == 'M' else 0.85
    crcl = ((140 - age) * weight_kg * sex_factor)
    return round(crcl, 1)

# Common antibiotic renal dosing thresholds:
RENAL_DOSING_GUIDE = {
    'Vancomycin':      {'>50': 'Normal q12h', '20-50': 'Extend to q24h (AUC-guided)', '<20': 'Consult pharmacy'},
    'Piperacillin-Tz': {'>40': '4.5g q8h', '20-40': '2.25g q6h', '<20': '2.25g q8h'},
    'Ciprofloxacin':   {'>50': '400mg q8h', '10-50': '400mg q12h', '<10': '400mg q24h'},
    'Metformin':       {'>45': 'Normal', '30-45': 'Use with caution; reduce dose', '<30': 'Contraindicated'},
}

# Example: 72yo female, weight 60 kg, SCr 1.8 mg/dL
crcl = cockcroft_gault_crcl(72, 60, 1.8, 'F')
print(f"CrCl: {crcl} mL/min → Vancomycin: extended interval, AUC-guided monitoring")
```

**Vancomycin AUC-Guided Dosing (2020 ASHP/IDSA Guidelines):**
```
Target: AUC/MIC = 400–600 mg·h/L (for MIC ≤ 1 mg/L)
Method: Bayesian PK modeling (DoseMeRx, InsightRx) preferred over trough-only
Initial load: 25 mg/kg IV × 1 dose
Maintenance: 15-20 mg/kg q8-12h based on renal function; adjust per Bayesian model
Note: Trough-only monitoring (15-20 mg/L) is no longer recommended
```

