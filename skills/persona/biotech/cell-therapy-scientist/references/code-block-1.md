# python Example

```
# CAR-T construct component specification checklist
def car_construct_spec(target_antigen, indication):
    """
    Generate CAR construct specification based on target and indication.
    Returns recommended component choices with rationale.
    """
    spec = {
        'scFv': {
            'orientation': 'VH-linker-VL (preferred) or VL-linker-VH (test both)',
            'linker': '(G4S)3 = GGGGSGGGGSGGGGSGGGGS (15-mer Whitlow linker)',
            'affinity_target': '1-30 nM Kd (lower affinity → reduced on-target/off-tumor)',
            'humanization': 'Required for clinical (CDR-grafting, Kabat numbering)',
        },
        'signal_peptide': 'CD8α signal peptide (MALPVTALLLPLALLLHAARP)',
        'hinge_transmembrane': {
            'hematologic': 'CD8α hinge + CD8α TM (reduces tonic signaling vs. CD28)',
            'solid_tumor': 'CD28 hinge + CD28 TM (enhances clustering, activation)',
        },
        'co_stimulatory_domain': {
            '4-1BB': 'Persistence, memory formation, mitochondrial biogenesis (heme-ALL, DLBCL)',
            'CD28': 'Rapid killing, high peak expansion (solid tumors, aggressive ALL)',
            'OX40': 'Investigational: Th1/Th17 bias, anti-exhaustion',
        },
        'signaling_domain': 'CD3ζ (ITAMs ×3; standard for all approved CARs)',
        'safety_features': ['EGFRt (cetuximab-mediated depletion)', 'iCaspase9 (AP20187-inducible)',
                             'RQR8 (CD34+CD20 epitope, rituximab depletion)'],
    }
    return spec

# Codon optimization and sequence verification
GOLDEN_GATE_ASSEMBLY_CHECK = [
    "Verify no BsaI sites in insert (Golden Gate cloning)",
    "Check Kozak sequence: GCCACC before ATG start codon",
    "Confirm signal peptide cleavage: SignalP 6.0 prediction",
    "Verify CAR surface expression by flow before functional assays",
]
```
