# Scenario Examples

## 9.1 Engineering Scenarios

### Nonlinear Static Analysis

**User:** "How to simulate bolt preloading?"

**Expert:**
> **Bolt Preload Setup:**
>
> 1. Create *Step*: Static, General (nonlinear)
> 2. Apply *Bolt Load*:
>    - Method: Apply force
>    - Preload magnitude: e.g., 10 kN
> 3. Use *Interaction* with contact pairs
> 4. Consider *nonlinear geometry* (NLGEOM=YES)
> 5. Define proper convergence settings:
>    - Residual tolerance: 0.5%
>    - Time increment: auto

### Dynamic Explicit

**User:** "How to simulate drop test?"

**Expert:**
> **Drop Test Setup:**
>
> 1. Create *Step*: Dynamic, Explicit
> 2. Set time period (e.g., 0.05 s)
> 3. Define mass scaling if needed:
>    - `*Dynamic Explicit, ELEMENT MATRIX=STATIC`
> 4. Apply gravity (gravity load)
> 5. Define contact:
>    - `*Contact Pair, INTERACTION=contact`
>    - Use penalty or kinematic formulation
> 6. Energy check: ensure EKIN < 10% ETOTAL

### Frequency Analysis

**User:** "How to get natural frequencies?"

**Expert:**
> **Modal Analysis Setup:**
>
> 1. Create *Step*: Frequency
> 2. Specify number of eigenvalues (e.g., 20)
> 3. Use Lanczos or Subspace solver
> 4. Define precondition:
>    - Block Lanczos for large models
>    - Subspace for small/medium
> 5. Post-process: view mode shapes

## 9.2 Industry Applications

| Industry | Application | Typical Analysis |
|----------|-------------|------------------|
| Automotive | Crash simulation | Dynamic Explicit |
| Aerospace | Buckling analysis | Static Riks |
| Manufacturing | Metal forming | Static, Explicit |
| Civil | Seismic analysis | Dynamic, Modal |
| Biomedical | Implant stress | Static, Contact |
| Electronics | Thermal stress | Coupled temp-displacement |

## 9.3 Automation

### Python Script Example

```python
from abaqus import *
from abaqusConstants import *

# Create model
model = mdb.Model(name='FrameAnalysis')

# Create part
part = model.Part(name='Beam', dimensionality=THREE_D, 
                  type=DEFORMABLE_BODY)
part.BaseBeam(r=0.05, l=2.0)

# Create material
model.Material(name='Steel')
model.Material(name='Steel').Elastic(table=((200E9, 0.3),))

# Create section
model.HomogeneousSolidSection(name='Section1', 
                               material='Steel', thickness=1.0)

# Assign section
part.SectionAssignment(sectionName='Section1')

# Mesh
part.seedPart(size=0.1, deviationFactor=0.1)
part.generateMesh()

# Create step
model.StaticStep(name='LoadStep', previous='Initial', 
                 timePeriod=1.0)

# Create job
job = mdb.Job(name='FrameJob', model='FrameAnalysis')
job.submit()
```

### Batch Processing

```bash
#!/bin/bash
# Parametric study

for force in 1000 2000 3000 4000 5000; do
    cp template.inp model_$force.inp
    sed -i "s/FORCE/$force/" model_$force.inp
    abaqus job=model_$force inp=model_$force.inp cpus=4
done
```