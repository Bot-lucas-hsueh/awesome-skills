# code Example

```
AI Drug Design Mental Model
============================================================
   TARGET          ->   POCKET         ->   PHARMACOPHORE
   (Biology)            (Structure)          (3D Features)
      |                    |                     |
      v                    v                     v
  Validation          AlphaFold/             Key H-bond,
  (Genetics,          X-ray/cryo-EM          hydrophobic,
   Clinical)          Druggability            ionic contacts
      |                    |                     |
      +--------------------+---------------------+
                           |
                    GENERATIVE MODEL
               (DiffSBDD / REINVENT
                           |
              +------------+------------+
              |                         |
           DOCKING                  ADMET
        (Vina/Glide/Gnina)    (ADMETlab/pkCSM/SwissADME)
              |                         |
              +------------+------------+
                           |
                    MPO SCORE
                           |
                    ACTIVE LEARNING
                  (Bayesian Optimization)
                           |
                    SYNTHESIS & ASSAY
                    (DMPK, Potency, Selectivity)
                           |
                    CANDIDATE SELECTION
                    (IND-Enabling Studies)
============================================================
```
