## § 3 · Risk Disclaimer

**Educational reference only. Radiology reports require access to original DICOM images, complete clinical history, and board-certified radiologist interpretation. This skill cannot diagnose from descriptions alone.**

| Risk | Mitigation |
|------|-----------|
| Missed diagnosis | Systematic review approach (not satisfaction of search); clinical correlation mandatory |
| Contrast-induced nephropathy | eGFR screening; hydration; iso-osmolar contrast for high-risk patients |
| Radiation exposure | ALARA; clinical indication justified; use lowest dose achieving diagnostic quality |
| Incidental findings | Management frameworks (Fleischner, ACR Incidental Findings Committee); appropriate follow-up |

## 🤖 Core Framework

**Imaging Characterization Metrics:**
```python
def ct_density_characterization(hounsfield_units):
    """
    CT Hounsfield Unit characterization for lesion analysis.
    Reference values for unenhanced CT.
    """
    HU_ranges = {
        'air': (-1000, -700),
        'fat': (-150, -50),
        'simple_fluid_water': (-10, 20),
        'soft_tissue_muscle': (35, 60),
        'acute_blood_hematoma': (50, 80),
        'calcification_bone': (200, 3000),
        'iodinated_contrast_enhanced': (100, 400),
    }
    interpretation = []
    for tissue, (lo, hi) in HU_ranges.items():
        if lo <= hounsfield_units <= hi:
            interpretation.append(tissue)
    return {
        'HU': hounsfield_units,
        'matches': interpretation if interpretation else ['indeterminate — correlate with MRI'],
    }

def radiation_dose_estimate(CTDIvol_mGy, scan_length_cm, body_region):
    """
    Effective dose estimation from CT parameters.
    DLP = CTDIvol × scan_length (mGy·cm)
    Effective dose = DLP × k-factor (mSv per mGy·cm)
    ACR k-factors by region.
    """
    k_factors = {
        'head': 0.0021,        # mSv
        'neck': 0.0059,
        'chest': 0.014,
        'abdomen': 0.015,
        'pelvis': 0.019,
        'spine_lumbar': 0.015,
    }
    DLP = CTDIvol_mGy * scan_length_cm
    k = k_factors.get(body_region.lower(), 0.015)
    effective_dose_mSv = DLP * k
    # Background radiation context: USA average ~3.1 mSv/year
    background_equivalents = effective_dose_mSv
    return {
        'DLP_mGy_cm': round(DLP, 1),
        'effective_dose_mSv': round(effective_dose_mSv, 2),
        'background_radiation_equivalents': round(background_equivalents, 1),
    }

def contrast_safety_screening(eGFR_mL_min_1_73m2, prior_contrast_reaction,
                               metformin_use=False, dialysis=False):
    """
    ACR Manual on Contrast Media — iodinated contrast safety assessment.
    eGFR thresholds per ACR 2023 guidelines.
    """
    recommendations = []
    # Renal function
    if dialysis:
        recommendations.append("Dialysis: iodinated contrast acceptable — coordinate dialysis timing")
    elif eGFR_mL_min_1_73m2 >= 30:
        recommendations.append(f"eGFR {eGFR_mL_min_1_73m2}: iodinated contrast acceptable; standard precautions")
    elif 15 <= eGFR_mL_min_1_73m2 < 30:
        recommendations.append(f"eGFR {eGFR_mL_min_1_73m2}: CAUTION — discuss risk/benefit; consider non-contrast or alternative modality")
    else:
        recommendations.append(f"eGFR {eGFR_mL_min_1_73m2}: HIGH RISK — avoid unless critical; nephrology consult")
    # Prior reaction
    if prior_contrast_reaction == 'mild':
        recommendations.append("Prior mild reaction: premedication (methylprednisolone 32mg PO 12h+2h pre, diphenhydramine 50mg 1h pre)")
    elif prior_contrast_reaction in ('moderate', 'severe'):
        recommendations.append("Prior moderate/severe reaction: mandatory premedication + allergist consult + consider alternative modality")
    # Metformin
    if metformin_use and eGFR_mL_min_1_73m2 < 30:
        recommendations.append("Metformin + low eGFR: hold metformin 48h post-contrast; recheck renal function before resuming")
    return recommendations

# BI-RADS Assessment Categories
BIRADS_CATEGORIES = {
    0: {'description': 'Incomplete — need additional imaging', 'cancer_risk': 'N/A', 'action': 'Additional imaging or prior comparison'},
    1: {'description': 'Negative — no abnormality', 'cancer_risk': '<0.1%', 'action': 'Routine screening (annual)'},
    2: {'description': 'Benign finding', 'cancer_risk': '<0.1%', 'action': 'Routine screening (annual)'},
    3: {'description': 'Probably benign', 'cancer_risk': '>0% but ≤2%', 'action': 'Short-interval follow-up (6 months)'},
    4: {'description': 'Suspicious', 'cancer_risk': '2%–95%', 'action': 'Tissue sampling (biopsy)'},
    5: {'description': 'Highly suggestive of malignancy', 'cancer_risk': '≥95%', 'action': 'Biopsy; surgical consultation'},
    6: {'description': 'Known biopsy-proven malignancy', 'cancer_risk': 'N/A', 'action': 'Staging/treatment planning'},
}

# Fleischner Society Pulmonary Nodule Guidelines (2017)
def fleischner_recommendation(size_mm, morphology, patient_risk):
    """
    Fleischner Society 2017 guidelines for incidental pulmonary nodule management.
    patient_risk: 'low' or 'high' (smoking, family history, occupational exposure)
    morphology: 'solid', 'part-solid', 'ground_glass'
    """
    if morphology == 'solid':
        if size_mm < 6:
            return 'No routine follow-up' if patient_risk == 'low' else 'Optional CT at 12 months'
        elif 6 <= size_mm < 8:
            return 'CT at 6-12 months, then 18-24 months if no change'
        elif 8 <= size_mm < 15:
            return 'CT at 3 months, PET/CT or biopsy'
        else:
            return 'CT at 3 months; PET/CT, biopsy, or resection'
    elif morphology == 'ground_glass':
        if size_mm < 6:
            return 'No routine follow-up'
        else:
            return 'CT at 6-12 months to confirm; if persistent, CT every 2 years until 5 years'
    elif morphology == 'part-solid':
        if size_mm < 6:
            return 'No routine follow-up'
        else:
            return 'CT at 3-6 months; if solid component ≥6mm, PET/CT or biopsy'
```

