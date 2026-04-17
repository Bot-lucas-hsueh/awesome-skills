# Standards & Reference

## 7.1 Official Documentation

- [Dassault Systèmes SIMULIA](https://www.3ds.com/products/simulia) - Official Abaqus product page
- [Abaqus Documentation (2024)](https://help.3ds.com/) - Official help documentation
- [Abaqus Learning Edge](https://www.3ds.com/learn-simulia) - Training resources
- [SIMULIA Community](https://www.3ds.com/community) - User forums and knowledge base

## 7.2 Configuration Reference

### Element Types

| Family | Element | Use Case |
|--------|---------|----------|
| Continuum | C3D8R | 8-node brick, reduced integration |
| Continuum | C3D20R | 20-node brick, quadratic |
| Continuum | C3D4 | 4-node tetrahedron |
| Shell | S4R | 4-node shell, reduced integration |
| Shell | S8R5 | 8-node shell, reduced integration |
| Beam | B31 | 2-node beam, Timoshenko |
| Truss | T3D2 | 2-node truss |

### Material Models

| Model | Keyword | Application |
|-------|---------|-------------|
| Linear Elastic | `ELASTIC` | Isotropic/hyperelastic |
| Plastic | `PLASTIC` | Metal plasticity |
| Hyperelastic | `HYPERELASTIC` | Rubber, elastomers |
| Viscoelastic | `VISCOELASTIC` | Time-dependent |
| Creep | `CREEP` | High-temperature |
| Composite | `LAMINATE` | Layered composites |

### Typical Job Submission

```bash
# Submit job from command line
abaqus job=analysis inp=model.inp cpus=8 interactive

# With specific queue (LSF/SLURM)
bsub -q normal -n 8 abaqus job=model inp=model.inp

# Parametric studies
abaqus script=parametric.py
```

## 7.3 Common Commands

### Preprocessing

| Command | Description |
|---------|-------------|
| `abaqus cae` | Launch GUI |
| `abaqus python script.py` | Run Python script |
| `abq2023 python` | Python with Abaqus API |
| `mesh` | Generate mesh |
| `assign material` | Apply material definitions |

### Analysis

| Command | Description |
|---------|-------------|
| `abaqus job=job1 inp=model.inp` | Submit analysis |
| `abaqus interactive` | Interactive submission |
| `abaqus resume` | Resume suspended job |
| `abaqus kill` | Terminate running job |

### Post-Processing

| Command | Description |
|---------|-------------|
| `abaqus viewer` | Launch Visualization module |
| `abaqus odb=job1` | Open output database |
| `abaqus python read_odb.py` | Scripted post-processing |

## 7.4 Version Compatibility

| Version | Status | Notes |
|---------|--------|-------|
| Abaqus 2020 | Supported | LTS |
| Abaqus 2021 | Supported | Enhanced composites |
| Abaqus 2022 | Supported | New contact formulations |
| Abaqus 2023 | Supported | Co-simulation updates |
| Abaqus 2024 | Current | Latest stable release |

### API Changes

- **2022+**: Enhanced `abaqus` Python module
- **2023+**: Native Python 3 support
- **2024+**: Cloud deployment options