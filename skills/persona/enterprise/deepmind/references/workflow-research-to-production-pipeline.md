## § 3 — Workflow: Research to Production Pipeline

### 3.1 DeepMind Research Lifecycle

```
PHASE 1: HYPOTHESIS & EXPERIMENTAL DESIGN (Weeks 1-4)
├── Literature review across disciplines
├── Falsifiable hypothesis formulation
├── Multi-disciplinary expert consultation
├── Statistical power analysis
├── Pre-registered protocol
├── ✗ SKIP → Vague hypotheses, no controls, p-hacking risk
└── Deliverable: Experimental protocol, IRB if human subjects

PHASE 2: INFRASTRUCTURE & PILOT (Weeks 5-8)
├── Reproducible training pipeline (seed control, versioning)
├── Data pipeline validation
├── Small-scale pilot experiments
├── Ablation study design
├── Checkpointing and monitoring setup
├── ✗ SKIP → Irreproducible code, no version control
└── Deliverable: Validated training infrastructure

PHASE 3: LARGE-SCALE TRAINING (Weeks 9-20)
├── Distributed training on TPU/GPU clusters
├── Real-time monitoring (loss curves, gradient norms)
├── Regular checkpointing to GCS
├── Hyperparameter sweeps with Bayesian optimization
├── Failure mode analysis
├── ✗ SKIP → Single run without ablations
└── Deliverable: Trained model checkpoints

PHASE 4: VALIDATION & ANALYSIS (Weeks 21-28)
├── Statistical significance testing (multiple comparison correction)
├── Independent test set evaluation (never seen during development)
├── Ablation studies (isolate component contributions)
├── Distribution shift evaluation
├── Expert review from domain specialists
├── ✗ SKIP → Test set contamination, cherry-picking results
└── Deliverable: Validated results package

PHASE 5: PUBLICATION & DEPLOYMENT (Weeks 29-40)
├── Nature/Science/NeurIPS submission
├── Open-source release (if applicable)
├── Reproduction package (code, data, trained models)
├── Safety evaluation and red-teaming
├── Product integration (if applicable)
└── Deliverable: Peer-reviewed publication, deployed system
```

### 3.2 AlphaZero-Style Self-Play Pipeline

```
ITERATION CYCLE (repeat until convergence):

1. SELF-PLAY GENERATION
   └── Current policy plays against itself with MCTS
   └── Temperature-based move selection for exploration
   └── Store (state, policy_targets, value_targets) tuples

2. NEURAL NETWORK TRAINING
   └── Loss = (z - v)² - πᵀlog(p) + c||θ||²
   └── z = actual game outcome (MCTS-augmented)
   └── v = value network prediction
   └── π = MCTS policy, p = network policy
   └── Train on most recent 500k-1M games (sliding window)

3. EVALUATION
   └── New network vs current best (400 games, no exploration)
   └── Win rate > 55% → promote to new best
   └── Otherwise → discard, continue training

4. CHECKPOINT & DISTRIBUTE
   └── Update self-play workers with new policy
   └── Archive checkpoint
   └── Log Elo progression
```

### 3.3 AlphaFold Structure Prediction Workflow

```
INPUT: Amino acid sequence

STEP 1: MSA GENERATION
├── Search UniRef, BFD, MGnify databases
├── JackHMMER and HHblits for homolog detection
└── Output: Multiple Sequence Alignment (MSA)

STEP 2: TEMPLATE SEARCH (optional)
├── Search PDB for experimental structures
├── Extract structural templates if available
└── Output: Template features

STEP 3: EVOFORMER PROCESSING
├── MSA representation (rows = sequences, cols = residues)
├── Pair representation (residue-residue relationships)
├── 48 Evoformer blocks with triangular attention
├── Outer product mean updates
└── Output: Processed MSA and pair representations

STEP 4: STRUCTURE MODULE
├── Invariant Point Attention (IPA)
├── Structure updates with FAPE loss
├── Side chain prediction with torsion angles
├── Recycling (iterative refinement)
└── Output: 3D coordinates (N, Cα, C, O + side chains)

STEP 5: CONFIDENCE ESTIMATION
├── pLDDT (per-residue confidence)
├── Predicted Aligned Error (PAE)
└── Output: Confidence metrics per residue
```

---
