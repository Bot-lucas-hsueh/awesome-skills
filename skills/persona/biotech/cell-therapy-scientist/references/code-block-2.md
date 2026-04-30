# python Example

```
RELEASE_TESTING_PANEL = {
    # Identity
    'CAR_expression': {
        'method': 'Flow cytometry: anti-idiotype or Protein L staining, gate on CD3+',
        'acceptance': '≥ 20% CAR+ within viable CD3+ T cells',
    },
    'CD4_CD8_ratio': {
        'method': 'Flow cytometry',
        'acceptance': 'Report result; target 1:1 to 2:1 (CD4:CD8) for balanced response',
    },
    # Purity
    'viability': {
        'method': 'Flow 7-AAD or DAPI exclusion',
        'acceptance': '≥ 70% viable (ideally ≥ 80%)',
    },
    # Safety
    'sterility': {'method': 'USP <71>', 'acceptance': 'Negative at 14 days'},
    'mycoplasma': {'method': 'PCR (Venor GeM, EZ-PCR)', 'acceptance': 'Negative'},
    'endotoxin': {'method': 'LAL kinetic turbidimetric', 'acceptance': '≤ 5 EU/dose'},
    'VCN': {'method': 'ddPCR (HIV-1 gag / PTBP2)', 'acceptance': '0.5–5 copies/diploid genome'},
    'RCR': {'method': 'qPCR or S+L- amplification', 'acceptance': 'Not detected'},
    # Potency
    'cytotoxicity': {
        'method': 'xCELLigence or LDH: co-culture with antigen+ target line, E:T 5:1, 24h',
        'acceptance': '≥ 20% specific lysis at E:T 5:1 (or EC50 E:T ≤ 10:1)',
    },
    'IFN_gamma': {
        'method': 'ELISA after 24h co-culture with antigen+ target, E:T 2:1',
        'acceptance': '≥ 200 pg/mL above background',
    },
}
```
