# python Example

```
# Biomaterials mechanical property reference database
BIOMATERIAL_PROPERTIES = {
    # Polymers
    'PLGA_50_50': {
        'E_GPa': 2.0, 'UTS_MPa': 45, 'elongation_pct': 3,
        'degradation_months': (2, 4), 'Tg_C': 45,
        'application': 'short-term scaffold, drug delivery microspheres'
    },
    'PLGA_75_25': {
        'E_GPa': 2.1, 'UTS_MPa': 50, 'elongation_pct': 5,
        'degradation_months': (4, 8), 'Tg_C': 50,
        'application': 'medium-term scaffold, suture anchors'
    },
    'PCL': {
        'E_GPa': 0.4, 'UTS_MPa': 16, 'elongation_pct': 300,
        'degradation_months': (18, 36), 'Tg_C': -60,
        'application': 'long-term scaffold, electrospun membrane, FDM printing'
    },
    'PEEK': {
        'E_GPa': 3.6, 'UTS_MPa': 100, 'elongation_pct': 30,
        'degradation_months': None,  # non-degradable
        'Tg_C': 143,
        'application': 'spinal cages, dental implants, radiolucent fixation'
    },
    # Ceramics
    'Hydroxyapatite_dense': {
        'E_GPa': 80, 'compressive_MPa': 500, 'tensile_MPa': 40,
        'degradation_months': (12, 24),  # slow resorption
        'application': 'bone substitute, coating on metal implants'
    },
    'TCP_beta': {
        'E_GPa': 30, 'compressive_MPa': 150, 'tensile_MPa': 10,
        'degradation_months': (6, 12),
        'application': 'faster-resorbing bone filler, biphasic HA/TCP'
    },
    # Metals
    'Ti6Al4V_ELI': {
        'E_GPa': 114, 'UTS_MPa': 860, 'yield_MPa': 795,
        'fatigue_MPa': 550,  # 10^7 cycles R=-1, in air
        'application': 'orthopedic implants, dental, spinal rods'
    },
    'CoCr_ASTM_F75': {
        'E_GPa': 210, 'UTS_MPa': 655, 'yield_MPa': 450,
        'fatigue_MPa': 310,
        'application': 'hip femoral heads, knee tibial trays, dental'
    },
    # Reference tissues
    'cortical_bone': {'E_GPa': (15, 25), 'UTS_MPa': (130, 200), 'fatigue_MPa': (60, 100)},
    'cancellous_bone': {'E_GPa': (0.1, 5.0), 'compressive_MPa': (0.1, 30)},
    'articular_cartilage': {'E_GPa': (0.001, 0.01), 'application': 'soft, viscoelastic'},
}

def select_material(E_target_GPa, degradable=True, load_bearing=True):
    """Suggest candidate materials based on modulus and degradability requirements."""
    candidates = []
    for name, props in BIOMATERIAL_PROPERTIES.items():
        if name.startswith('cortical') or name.startswith('cancellous') or name.startswith('articular'):
            continue
        E = props.get('E_GPa', 0)
        if isinstance(E, tuple):
            E = sum(E)/2
        modulus_match = abs(E - E_target_GPa)
        degrades = props.get('degradation_months') is not None
        if modulus_match and (not degradable or degrades):
            candidates.append((name, E, props.get('application', '')))
    return candidates

# Example: seeking match for cancellous bone (E ~ 1 GPa), degradable
matches = select_material(E_target_GPa=1.0, degradable=True)
for m in matches:
    print(f"{m[0]}: E={m[1]} GPa — {m[2]}")
```
