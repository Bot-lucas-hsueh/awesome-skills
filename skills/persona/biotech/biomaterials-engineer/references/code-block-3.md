# python Example

```
# Extract preparation per ISO 10993-12
# Surface area to extraction medium ratio: 6 cm²/mL (for solid materials)
# Extraction conditions: 37°C, 24 hours in DMEM (physiological conditions)

def extract_preparation_parameters(surface_area_cm2, material_density_g_cm3,
                                    material_volume_cm3, extraction_ratio=6.0):
    """
    Calculate extraction medium volume per ISO 10993-12.
    surface_area_cm2: total surface area of test article
    extraction_ratio: cm²/mL (6.0 for solid, 3.0 for porous)
    """
    volume_mL = surface_area_cm2
    return {
        'medium_volume_mL': volume_mL,
        'dilutions_to_test': [100, 50, 25, 12.5, 6.25],  # % extract in cell culture medium
        'cell_line': 'L929 (murine fibroblast, ATCC CCL-1)',
        'exposure_hours': 24,
        'viability_method': 'MTT assay (ISO 10993-5 Annex C)',
        'pass_criterion': 'Cell viability ≥ 70% of negative control at 100% extract'
    }

# MTT assay data analysis
def calculate_cell_viability(OD_test, OD_negative_control, OD_blank):
    """
    Calculate % cell viability from MTT optical density data.
    """
    viability = ((OD_test - OD_blank)
    return max(0, viability)

# Example: interpreting Grade 0–4 cytotoxicity scale per ISO 10993-5
CYTOTOX_GRADES = {
    0: ('None', '≥ 70% viability', 'PASS'),
    1: ('Slight', '60–69% viability', 'Borderline — repeat with fresh batch'),
    2: ('Mild', '50–59% viability', 'FAIL — investigate leachables'),
    3: ('Moderate', '30–49% viability', 'FAIL — reformulate material'),
    4: ('Severe', '< 30% viability', 'FAIL — major reformulation required'),
}
```
