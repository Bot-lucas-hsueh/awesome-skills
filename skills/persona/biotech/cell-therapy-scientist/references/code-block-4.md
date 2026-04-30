# python Example

```
def multiplex_crispr_design(target_genes, delivery='RNP_electroporation'):
    """
    Design multiplex CRISPR editing strategy for allogeneic cell therapy.
    RNP (ribonucleoprotein): SpCas9 protein + sgRNA — preferred for GMP (no integrating DNA)
    """
    strategy = {}
    for gene in target_genes:
        strategy[gene] = {
            'TRAC': {
                'purpose': 'Prevent GvHD (allogeneic T cell graft-vs-host)',
                'sgRNA_target': 'Exon 1, TRAC locus (constitutive expression)',
                'KO_efficiency_target': '≥ 90% by flow (anti-TCRαβ)',
                'KI_option': 'Insert CAR at TRAC locus via HDR (reduces tonic signaling)',
            },
            'B2M': {
                'purpose': 'Eliminate HLA-I surface expression → prevent host cytotoxic T rejection',
                'sgRNA_target': 'Exon 1, B2M gene (loss of B2M → no HLA-I assembly)',
                'KO_efficiency_target': '≥ 90% by flow (anti-HLA-ABC)',
                'risk': 'B2M-KO activates host NK cells (missing-self) → add HLA-E or CD47 "dont-eat-me"',
            },
            'PDCD1': {
                'purpose': 'Knock out PD-1 → prevent tumor microenvironment exhaustion',
                'sgRNA_target': 'Exon 1, PDCD1',
                'KO_efficiency_target': '≥ 80% by flow (anti-PD-1)',
            },
            'NKG2A': {
                'purpose': 'Knock out NKG2A inhibitory receptor → enhance NK killing of HLA-E+ tumors',
                'sgRNA_target': 'KLRC1 exon 2',
                'KO_efficiency_target': '≥ 75% by flow (anti-NKG2A/CD94)',
            },
        }.get(gene, {'error': f'Gene {gene} not in database'})

    return strategy

genes_to_edit = ['B2M', 'PDCD1', 'NKG2A']
plan = multiplex_crispr_design(genes_to_edit)

# Manufacturing order: edit → select edited cells → transduce CAR → expand
# RNP delivery: 4D-Nucleofector (Lonza), pulse code EN-138 for NK progenitors
# Genotoxicity check: karyotyping, ddPCR for large deletions (chromo translocations)
```
