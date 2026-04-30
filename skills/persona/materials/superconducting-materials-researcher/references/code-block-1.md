# python Example

```
# Superconducting material critical parameters database (4.2 K unless noted)
SUPERCONDUCTOR_PARAMS = {
    'NbTi': {
        'Tc_K': 9.2,
        'Bc2_T': 14.5,  # at 0 K; ~10 T at 4.2 K
        'Jc_typical': {'field_T': 5, 'T_K': 4.2, 'Jc_Amm2': 2500, 'unit': 'A/mm²'},
        'Je_engineering': 500,   # A/mm² (50:50 Cu:NbTi ratio typically)
        'ductile': True,
        'cost_per_kAm': 1.5,     # USD at 5T, 4.2K
        'applications': 'MRI (1.5-3T), accelerator quadrupoles, SMES'
    },
    'Nb3Sn': {
        'Tc_K': 18.3,
        'Bc2_T': 29,   # at 0 K; ~24 T at 4.2 K
        'Jc_typical': {'field_T': 12, 'T_K': 4.2, 'Jc_Amm2': 2000, 'unit': 'A/mm²'},
        'Je_engineering': 700,   # A/mm² in ITER-style strand
        'ductile': False,        # brittle A15 compound → react-and-wind
        'cost_per_kAm': 8,      # at 12T, 4.2K
        'applications': 'NMR (>9T), ITER TF/CS coils, high-field research magnets'
    },
    'REBCO_4K': {  # REBa2Cu3O7-δ coated conductor at 4.2 K
        'Tc_K': 92,
        'Bc2_T': 120,  # essentially no Bc2 limit at 4.2K (>100T)
        'Birr_T_at_77K': 7.0,   # irreversibility field at 77K
        'Jc_typical': {
            'B_parallel_c': {'field_T': 12, 'T_K': 4.2, 'Jc_Amm2': 1500},
            'B_parallel_ab': {'field_T': 12, 'T_K': 4.2, 'Jc_Amm2': 4000},  # intrinsic pinning
        },
        'Je_engineering': 400,   # A/mm² (4mm tape, 1.5 μm REBCO layer, 12T, 4.2K)
        'ductile': 'semi',       # flexible tape but strain-sensitive
        'cost_per_kAm': 35,     # at 12T, 4.2K (2024 market, improving)
        'applications': 'Fusion (SPARC, DEMO), 40T+ research, compact MRI, FCL'
    },
    'MgB2': {
        'Tc_K': 39,   # highest Tc among LTS-like materials
        'Bc2_T': 16,  # at 0K; ~3-4T at 20K
        'Jc_typical': {'field_T': 3, 'T_K': 20, 'Jc_Amm2': 300, 'unit': 'A/mm²'},
        'Je_engineering': 100,
        'ductile': 'moderate',
        'cost_per_kAm': 5,
        'applications': 'MRI (1.5T, cryo-free at 20K), wind power generators'
    },
}

def select_conductor(B_max_T, T_op_K, Je_required_Amm2, ac_loss_critical=False):
    """Select appropriate superconductor based on application requirements."""
    candidates = []
    for name, params in SUPERCONDUCTOR_PARAMS.items():
        # Check if operating field is below Bc2 at operating temperature
        # Simplified: use Bc2 at 4.2K as proxy
        Bc2_T_op = params.get('Bc2_T', 0) * (1 - T_op_K
        if B_max_T < 0.8 * Bc2_T_op:  # 80% Bc2 = practical limit
            if params['Je_engineering'] >= Je_required_Amm2 * 0.7:  # 70% of target
                candidates.append((name, params))
    return candidates
```
