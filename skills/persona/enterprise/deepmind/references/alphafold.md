# AlphaFold Deep Dive

## Overview

AlphaFold is DeepMind's protein structure prediction system that solved the 50-year-old protein folding problem, earning Demis Hassabis and John Jumper the 2024 Nobel Prize in Chemistry.

---

## AlphaFold 2 Architecture (2021)

### Input Representation

**MSA (Multiple Sequence Alignment):**
- Shape: `(N_seq, N_res, 43)` where N_seq ≈ 512, N_res = protein length
- Features: One-hot amino acid (20), deletion matrix (1), cluster profile (22)

**Templates (optional):**
- Experimental structures from PDB with similar sequences
- Provides additional structural information when available

**Target Features:**
- One-hot amino acid type
- Position in sequence
- Target-specific features

### Evoformer (48 blocks)

The Evoformer is the core architectural innovation:

```
MSA Representation ─────────────────────────────┐
     ↓                                          │
  MSA Row-wise Self-Attention                    │
     ↓                                          │
  MSA Column-wise Self-Attention                │
     ↓                                          │ Outer Product Mean
  MSA Transition (FFN)                          │ (MSA → Pair)
     ↓                                          │
     └──────────────────────────────────────────┘
                        ↓
               Pair Representation
                        ↓
     ┌──────────────────┼──────────────────┐
     ↓                  ↓                  ↓
Triangular          Triangular         Pair
Multiplicative       Self-Attention     Transition
Update                                  (FFN)
     ↓                  ↓                  ↓
     └──────────────────┼──────────────────┘
                        ↓
               Updated Pair Representation
                        ↓
     ┌──────────────────┘
     ↓
Back to MSA (via MSA pair bias)
```

**Key Operations:**

1. **MSA Row-wise Attention**: Attention across residues (within each sequence)
2. **MSA Column-wise Attention**: Attention across sequences (at each position) — captures evolutionary covariation
3. **Outer Product Mean**: Aggregates MSA to update pair representation
4. **Triangular Multiplicative Update**: Enforces transitivity in pair relations
5. **Triangular Self-Attention**: Attention over edges in the pair graph

### Structure Module

Translates Evoformer outputs to 3D coordinates:

**Invariant Point Attention (IPA):**
- Operates in 3D space while maintaining SE(3) equivariance
- Queries, keys, values derived from backbone frames
- Attention weights computed based on relative spatial positions

**Backbone Update:**
```
For each residue i:
  1. Predict rotation R_i (3×3) and translation t_i (3)
  2. Update backbone frame: Frame_i = (R_i, t_i)
  3. Place N, Cα, C atoms in local frame coordinates
```

**Side Chain Prediction:**
- Predict torsion angles (χ1, χ2, χ3, χ4) for each residue
- Place side chain atoms based on idealized geometry + predicted angles

### Training Objectives

**FAPE Loss** (Frame Aligned Point Error):
```
L_FAPE = Σ_ij min(d_th, ||T_i⁻¹(x_j) - T_i⁻¹(x̂_j)||)
```
- Measures error in local residue frames
- Robust to global rotation/translation

**Auxiliary Losses:**
- MSA reconstruction (masked language modeling)
- Distogram prediction (binned distance distribution)
- Masked MSA prediction
- Experimentally resolved prediction (confidence)

---

## AlphaFold 3 (May 2024)

### Key Advances

| Capability | AlphaFold 2 | AlphaFold 3 |
|------------|-------------|-------------|
| Proteins | ✓ | ✓ (improved) |
| DNA | ✗ | ✓ |
| RNA | ✗ | ✓ |
| Ligands (small molecules) | ✗ | ✓ |
| Ions | ✗ | ✓ |
| Post-translational modifications | ✗ | ✓ |
| DNA/RNA modifications | ✗ | ✓ |

### Architecture Changes

**Pairformer** (replacing Evoformer):
- Simplified from two-track (MSA + Pair) to single-track (Pair)
- 48 blocks of pair representation processing
- More efficient, better generalization

**Diffusion Module** (replacing Structure Module):
```
Input: Noisy atom positions + conditioning from Pairformer

Iterative denoising (N steps):
  1. Predict noise to subtract
  2. Update atom positions
  3. Apply physical constraints

Output: Refined 3D coordinates
```

**Unified Tokenization:**
- All atoms represented in a single set
- No special treatment for protein vs. DNA vs. ligand
- Simpler, more general architecture

### Performance

- **Protein-ligand complexes**: 50% better than previous methods
- **Protein-nucleic acid**: 2× better than specialized tools
- **Antibody-antigen**: Significant improvement over AlphaFold-Multimer

---

## Training Data & Compute

### Datasets

**Protein Data Bank (PDB):**
- ~170,000 experimental structures
- X-ray crystallography, cryo-EM, NMR

**Uniclust30 / BFD:**
- Sequence databases for MSA generation
- Billions of protein sequences

### Compute Requirements

| Aspect | Specification |
|--------|--------------|
| Training hardware | 128 TPU v3 cores |
| Training time | ~1-2 weeks |
| Inference time | ~1-5 minutes per protein |
| Memory | ~40GB for typical protein |

---

## Impact & Applications

### AlphaFold Protein Structure Database
- 200+ million predicted structures
- Free, open access
- 2+ million users from 190 countries

### Scientific Applications

| Field | Application |
|-------|-------------|
| Drug discovery | Target identification, binding site analysis |
| Enzyme design | Catalytic mechanism understanding |
| Disease research | Variant effect prediction |
| Agriculture | Crop improvement |
| Climate | Plastic-degrading enzymes |

### Isomorphic Labs
- Commercial drug discovery spinoff
- AlphaFold 3 + proprietary models
- Partnerships with Eli Lilly, Novartis
- Targeting "undruggable" proteins

---

## Citations

**AlphaFold 2:**
```
Jumper et al. (2021). Highly accurate protein structure prediction 
with AlphaFold. Nature, 596, 583-589.
```

**AlphaFold 3:**
```
Abramson et al. (2024). Accurate structure prediction of biomolecular 
interactions with AlphaFold 3. Nature, 630, 493-500.
```

**Nobel Prize 2024:**
```
Awarded to Demis Hassabis and John Jumper "for protein structure prediction"
```

---

## Open Source

- **AlphaFold 2**: https://github.com/deepmind/alphafold
- **AlphaFold 3**: Open-sourced November 2024
- **ColabFold**: https://github.com/sokrypton/ColabFold (community implementation)
- **OpenFold**: https://github.com/aqlaboratory/openfold (PyTorch reimplementation)

---

## Key Insights

1. **Evolution is the signal**: MSA column attention captures evolutionary couplings
2. **Equivariance matters**: IPA respects physical symmetries
3. **Recycling helps**: Iterative refinement improves accuracy
4. **Confidence calibration**: pLDDT correlates with actual accuracy
5. **Generality wins**: AlphaFold 3's unified approach beats specialized tools
