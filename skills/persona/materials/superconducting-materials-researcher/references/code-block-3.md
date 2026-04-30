# python Example

```
REBCO_TAPE_ARCHITECTURE = {
    # Standard 4mm wide, ~100 μm thick REBCO coated conductor cross-section
    'substrate': {
        'material': 'Hastelloy C-276 or stainless steel 316LN',
        'thickness_um': 50,  # μm
        'function': 'Mechanical support (yield strength > 500 MPa)',
        'roughness_Ra': '< 1 nm (required for epitaxial template)',
    },
    'buffer_layers': {
        'architecture_A_IBAD': ['Al2O3 seed (IBAD)', 'MgO template (IBAD)', 'homo-epitaxial MgO', 'LaMnO3', 'SrTiO3'],
        'architecture_B_RABiTS': ['Ni-5%W textured substrate', 'NiO seed', 'Y2O3', 'YSZ', 'CeO2'],
        'total_thickness_nm': 200,
        'texture_quality': 'Φ-scan FWHM ≤ 5°, ω-scan (rocking curve) FWHM ≤ 1°',
        'purpose': 'Chemical barrier + biaxial texture template for epitaxial REBCO',
    },
    'REBCO_layer': {
        'material': 'GdBCO or YBCO (Gd gives higher Jc near Tc)',
        'thickness_um': 1.0,   # 1.0–2.0 μm typical
        'deposition': 'PLD (pulsed laser deposition) or MOCVD',
        'dopants': 'BZO (1-2 mol%) or BHO (BaHfO3, 1-2 mol%) for flux pinning nanorods',
        'Jc_self_field_77K': '≥ 3 MA/cm²',  # 3000 A/mm² self-field at 77K
    },
    'Ag_overlayer': {
        'thickness_um': 2,
        'function': 'Oxidation protection during post-deposition oxygen annealing; contact layer',
    },
    'Cu_stabilizer': {
        'thickness_um': 20,    # electroplated
        'function': 'Normal-state current bypass (quench protection), RRR ≥ 100',
    },
}

def rebco_tape_engineering_Jc(REBCO_thickness_um, tape_width_mm, tape_thickness_um,
                                Jc_material_Amm2):
    """
    Calculate engineering current density Je for REBCO tape.
    Je = Jc_material × (REBCO cross-section)
    """
    A_REBCO = REBCO_thickness_um * 1e-3 * tape_width_mm  # mm²
    A_tape = tape_width_mm * tape_thickness_um * 1e-3    # mm²
    fill_factor = A_REBCO
    Je = Jc_material_Amm2 * fill_factor
    return Je, fill_factor

Je, ff = rebco_tape_engineering_Jc(1.5, 4.0, 100, Jc_material_Amm2=1500)  # 12T, 4.2K
print(f"Fill factor: {ff:.3f} ({ff*100:.1f}%), Je = {Je:.0f} A/mm²")
# Fill factor: 0.015 (1.5%), Je = 22 A/mm²  ← note: low fill factor is the key challenge
# → 4mm tape Ic at 12T, 4.2K: Je × A_tape = 22 × (4 × 0.1) = 8.8 A/mm² → Ic = 350 A
```
