# python Example

```
# Three possible mechanisms for CAR-T loss of persistence:
PERSISTENCE_FAILURE_ANALYSIS = {
    'Mechanism 1: T cell exhaustion': {
        'evidence': 'Early high Cmax (peak >10,000 copies/μg) → rapid collapse',
        'PD1_LAG3_at_peak': 'Check peak timepoint PBMC: PD-1+LAG-3+TIM-3+ triple+',
        'solution': [
            'Switch to 4-1BB co-stimulation (if CD28 was used)',
            'Add ex vivo checkpoint blockade during manufacturing',
            'Consider TET2 KO CAR-T (published: enhanced persistence)',
        ],
    },
    'Mechanism 2: Immune rejection (allogeneic or anti-CAR immune response)': {
        'evidence': 'CAR-T present at Day 28, rapid disappearance after',
        'test': 'Anti-CAR antibody titer (ELISA/bridging assay); host CD8 T cells specific for murine scFv',
        'solution': [
            'Humanize scFv (CDR-grafting) to reduce immunogenicity',
            'Switch from murine FMC63 scFv to humanized version',
        ],
    },
    'Mechanism 3: CD19 antigen escape': {
        'evidence': 'Relapse tumor is CD19-dim or CD19-negative by flow/IHC',
        'test': 'Biopsy flow cytometry: anti-CD19, anti-CD22, anti-CD10 on relapse sample',
        'solution': [
            'Tandem CD19/CD22 CAR for bivalent targeting',
            'Switch to CD22 CAR if CD19 lost but CD22 retained',
        ],
    },
}

# Management: re-challenge with second CAR-T infusion requires prior assessment of:
# 1. Disease burden (tumor lysis syndrome risk with high burden)
# 2. Prior CRS/ICANS history (increased risk with re-challenge)
# 3. Updated antigen profile (tumor evolution)
```
