# mRNA Technology Fundamentals

## What is mRNA?

Messenger RNA (mRNA) is a single-stranded RNA molecule that carries genetic information from DNA to ribosomes, where proteins are synthesized. In therapeutics, we use synthetic mRNA to instruct cells to produce specific proteins.

```
DNA ──► Transcription ──► mRNA ──► Translation ──► Protein
        (in nucleus)      (in cytoplasm)        (at ribosome)
```

## mRNA Structure for Therapeutics

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ MODIFIED mRNA STRUCTURE                                                     │
└─────────────────────────────────────────────────────────────────────────────┘

5' Cap ──► 5' UTR ──► Coding Sequence ──► 3' UTR ──► Poly(A) Tail
  │          │              │              │            │
  │          │              │              │            └── 100-150 nt
  │          │              │              │                (stability)
  │          │              │              │
  │          │              │              └── Alpha-globin 3' UTR
  │          │              │                   + stabilizing elements
  │          │              │
  │          │              └── Optimized codons
  │          │                   (human-preferred)
  │          │
  │          └── Kozak sequence
  │              (GCCGCCRCCatgG)
  │
  └── Cap1 structure
      (CleanCap - TriLink)
```

## Component Details

### 5' Cap Structure
- **Cap0**: Basic 7-methylguanosine (m7G)
- **Cap1**: Additional 2'-O-methylation (Moderna uses this)
- **Function**: Protects from exonucleases, enables translation initiation
- **Benefit**: 10x increase in translation efficiency vs uncapped

### 5' Untranslated Region (5' UTR)
- **Kozak sequence**: GCCGCCRCCatgG
- **Purpose**: Ribosome binding and translation initiation
- **Moderna advantage**: Proprietary UTR library optimized for expression

### Coding Sequence (CDS)
Optimization strategies:
1. **Codon optimization**: Match human tRNA abundance
2. **GC content**: 45-55% for optimal stability
3. **Avoid**: Cryptic splice sites, internal TATA boxes
4. **Secondary structure**: Minimize in 5' region for translation efficiency

### 3' Untranslated Region (3' UTR)
- **Alpha-globin 3' UTR**: Naturally stable mRNA
- **Moderna elements**: Proprietary stabilizing sequences
- **Function**: mRNA stability, localization, translation regulation

### Poly(A) Tail
- **Length**: 100-150 nucleotides
- **Function**: Protects from degradation, enhances translation
- **Quality**: No heterogeneity (uniform length critical)

## Lipid Nanoparticle (LNP) Delivery

### Why LNP?
- mRNA is large, negatively charged, and degrades quickly
- LNP protects mRNA from nucleases
- Enables cellular uptake and endosomal escape
- Targetable to specific tissues

### LNP Composition

| Component | Typical % | Function |
|-----------|-----------|----------|
| Ionizable lipid | 50% | Encapsulation, endosomal escape |
| Helper lipid (DSPC) | 38.5% | Bilayer structure |
| Cholesterol | 10% | Membrane stability |
| PEG-lipid | 1.5% | Longevity, reduced immunogenicity |

### Ionizable Lipids
- **pH-dependent charge**: Neutral at physiological pH, positive in acidic endosomes
- **Examples**: SM-102 (Moderna), ALC-0315 (Pfizer)
- **Mechanism**: Protonated in endosome → disrupts membrane → releases mRNA

### LNP Quality Attributes

| Attribute | Target | Measurement |
|-----------|--------|-------------|
| Size | 80-100 nm | Dynamic Light Scattering |
| PDI | <0.2 | DLS |
| Zeta potential | -10 to +10 mV | Electrophoretic light scattering |
| Encapsulation | >90% | RiboGreen assay |

## Design-Build-Test-Learn Cycle

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    mRNA DBTL CYCLE                                          │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────┐
    │    DESIGN    │◄─────────────────────────────────────────┐
    │              │                                          │
    │ • Sequence   │                                          │
    │   optimization                                          │
    │ • UTR selection                                         │
    │ • LNP design                                            │
    └──────┬───────┘                                          │
           ↓                                                  │
    ┌──────────────┐                                          │
    │     BUILD    │                                          │
    │              │                                          │
    │ • Gene       │                                          │
    │   synthesis                                             │
    │ • IVT production                                        │
    │ • LNP formulation                                       │
    └──────┬───────┘                                          │
           ↓                                                  │
    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐│
    │     TEST     │────►│   ANALYZE    │────►│    LEARN     │┘
    │              │     │              │     │              │
    │ • In vitro   │     │ • Data       │     │ • Update     │
    │   expression │     │   integration│     │   algorithms │
    │ • In vivo    │     │ • Pattern    │     │ • Platform   │
    │   studies    │     │   recognition│     │   knowledge  │
    └──────────────┘     └──────────────┘     └──────────────┘

CYCLE TIME TARGETS:
• Respiratory programs: <4 weeks
• Novel targets: <8 weeks
```

## Moderna Platform Advantages

1. **Speed**: 63 days from sequence to Phase 1 (COVID-19 record)
2. **Flexibility**: Same process for any mRNA sequence
3. **Scalability**: From small personalized batches to billions of doses
4. **Digital-native**: AI/ML optimization, cloud infrastructure

## Applications

| Application | Example | Status |
|-------------|---------|--------|
| Infectious disease | COVID-19 (Spikevax) | Approved |
| Respiratory | RSV (mRESVIA) | Approved |
| Cancer | Personalized neoantigen (mRNA-4157) | Phase 3 |
| Rare disease | Enzyme replacement (MMA) | Phase 3 |
| Autoimmune | Immune tolerance | Phase 2 |

---
*Source: Moderna scientific publications, patent filings, investor presentations*
