# python Example

```
import numpy as np
import torch
from rdkit import Chem
from rdkit.Chem import AllChem
from botorch.models import SingleTaskGP
from botorch.fit import fit_gpytorch_mll
from botorch.acquisition import ExpectedImprovement
from gpytorch.mlls import ExactMarginalLogLikelihood

# Step 1: Generate Morgan fingerprints for all compounds
def smiles_to_fp(smiles_list, radius=2, nbits=2048):
    fps = []
    for smi in smiles_list:
        mol = Chem.MolFromSmiles(smi)
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=nbits)
        fps.append(list(fp))
    return torch.tensor(fps, dtype=torch.float64)

# Load your 50 synthesized compounds (SMILES + pIC50 = -log10(IC50_M))
train_X = smiles_to_fp(synthesized_smiles)          # shape [50, 2048]
train_Y = torch.tensor(pic50_values).unsqueeze(-1)  # shape [50, 1]

# Step 2: Fit Gaussian Process surrogate model
gp = SingleTaskGP(train_X, train_Y)
mll = ExactMarginalLogLikelihood(gp.likelihood, gp)
fit_gpytorch_mll(mll)

# Step 3: Define acquisition function (Expected Improvement)
best_observed = train_Y.max()
EI = ExpectedImprovement(model=gp, best_f=best_observed)

# Step 4: Score virtual library
virtual_X = smiles_to_fp(virtual_library_smiles)  # [5000, 2048]
with torch.no_grad():
    ei_scores = EI(virtual_X.unsqueeze(1))

# Step 5: Select top 10 by EI score
top_indices = ei_scores.topk(10).indices
selected_smiles = [virtual_library_smiles[i] for i in top_indices]

print("Top 10 candidates for synthesis:")
for smi, score in zip(selected_smiles, ei_scores[top_indices]):
    print(f"  {smi}  EI={score:.4f}")
```
