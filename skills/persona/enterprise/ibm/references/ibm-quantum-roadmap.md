# IBM Quantum Computing Reference

## Overview

IBM Quantum is leading the development of quantum computing for commercial and scientific applications. The IBM Quantum Roadmap outlines a path to fault-tolerant quantum computing by 2029.

## Quantum Computing Basics

### Qubit Technologies

```yaml
Superconducting Qubits (IBM Approach):
  Technology:
    - Transmon qubits
    - Josephson junctions
    - Dilution refrigeration (~15mK)
    
  Characteristics:
    - Gate times: ~100ns
    - Coherence times: ~100-500μs
    - Gate fidelities: 99.5%+
    - Connectivity: Heavy hex lattice
```

### Key Concepts

| Term | Definition |
|------|------------|
| **Qubit** | Quantum bit - superposition of 0 and 1 |
| **Entanglement** | Correlated quantum states across qubits |
| **Gate** | Quantum operation (analogous to classical logic gate) |
| **Circuit** | Sequence of quantum gates |
| **NISQ** | Noisy Intermediate-Scale Quantum (current era) |
| **Fault Tolerance** | Error-corrected, reliable quantum computing |

## IBM Quantum Roadmap

### Historical Progression

| Year | System | Qubits | Milestone |
|------|--------|--------|-----------|
| 2016 | IBM Quantum Experience | 5 | First public quantum computer |
| 2019 | IBM Q System One | 20 | Commercial quantum system |
| 2020 | Falcon | 27 | Quantum volume 64 |
| 2021 | Hummingbird | 65 | 127-qubit Eagle announced |
| 2022 | Eagle | 127 | First 100+ qubit processor |
| 2023 | Osprey | 433 | 1,121 quantum volume |
| 2024 | Condor | 1,121 | Utility-scale quantum |
| 2024 | Heron | 133 | Best error rates |

### Current Systems (2025)

```yaml
Heron Processor:
  - 133 qubits
  - 3-qubit gate error: <0.1%
  - Tunable couplers
  - Modular architecture
  - Best performance for error mitigation

System Two:
  - Modular quantum architecture
  - Scalable cryogenic infrastructure
  - High-density control electronics
  - Supports multiple processors
```

### Future Roadmap

| System | Year | Capability | Target |
|--------|------|------------|--------|
| **Flamingo** | 2025 | 156 qubits | Enhanced error correction |
| **Loon** | 2025 | Architecture testing | Starling preparation |
| **Kookaburra** | 2026 | 2,000+ physical qubits | First modular processor |
| **Cockatoo** | 2027 | Linked processors | Chip-to-chip communication |
| **Starling** | 2029 | 200 logical qubits | Fault-tolerant quantum |
| **Blue Jay** | Post-2029 | 2,000 logical qubits | Production-scale quantum |

## Qiskit SDK

### Installation & Setup

```bash
# Install Qiskit
pip install qiskit

# Install IBM Quantum provider
pip install qiskit-ibm-runtime

# Authenticate
qiskit-ibm-runtime save-account --token YOUR_TOKEN
```

### Basic Quantum Circuit

```python
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler

# Create a quantum circuit
qc = QuantumCircuit(2)
qc.h(0)           # Hadamard gate (superposition)
qc.cx(0, 1)       # CNOT gate (entanglement)
qc.measure_all()  # Measure all qubits

# Run on IBM Quantum
service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False)
sampler = Sampler(session=backend)
job = sampler.run([qc])
result = job.result()

print(f"Results: {result.quasi_dists}")
```

### Variational Quantum Eigensolver (VQE)

```python
from qiskit.circuit.library import EfficientSU2
from qiskit.primitives import Estimator
from qiskit_algorithms import VQE
from qiskit_algorithms.optimizers import SLSQP
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import JordanWignerMapper

# Define molecular system
driver = PySCFDriver(atom="H2 0 0 0; H2 0 0 0.74", basis="sto-3g")
problem = driver.run()

# Map to qubits
mapper = JordanWignerMapper()
qubit_op = mapper.map(problem.hamiltonian.second_q_op())

# Define ansatz
ansatz = EfficientSU2(qubit_op.num_qubits, reps=2)

# Run VQE
optimizer = SLSQP()
estimator = Estimator()
vqe = VQE(estimator, ansatz, optimizer)
result = vqe.compute_minimum_eigenvalue(qubit_op)

print(f"Ground state energy: {result.eigenvalue}")
```

## Quantum Applications

### Near-Term (NISQ Era)

```yaml
Optimization:
  - QAOA (Quantum Approximate Optimization Algorithm)
  - Portfolio optimization
  - Supply chain optimization
  - Traffic routing
  
Simulation:
  - VQE (Variational Quantum Eigensolver)
  - Small molecule simulation
  - Material properties
  - Drug discovery preparation
  
Machine Learning:
  - Quantum kernel methods
  - Quantum neural networks
  - Feature mapping
  - Pattern recognition
```

### Fault-Tolerant Era (Post-2029)

```yaml
Drug Discovery:
  - Protein folding
  - Molecular dynamics
  - Drug-target interactions
  - 50-100x speedup for certain problems
  
Materials Science:
  - Battery chemistry
  - Catalyst design
  - Superconductor discovery
  
Financial Modeling:
  - Risk analysis
  - Derivatives pricing
  - Monte Carlo acceleration
  
Cryptography:
  - Shor's algorithm (factoring)
  - Quantum-safe cryptography needs
  - Quantum key distribution
```

## IBM Quantum Network

### Membership Tiers

| Tier | Access | Cost | Best For |
|------|--------|------|----------|
| **Community** | Simulators, limited hardware | Free | Learning, exploration |
| **Open** | Standard queue | Free | Research, experimentation |
| **Explorer** | Expanded access | Subscription | Startups, academics |
| **Premium** | Priority queue, 28+ systems | Contract | Enterprise R&D |

### Enterprise Partners

```yaml
Notable Members:
  Financial Services:
    - JPMorgan Chase
    - Goldman Sachs
    - HSBC
    - Mitsubishi UFJ Financial
    
  Automotive:
    - Mercedes-Benz
    - Boeing
    - Airbus
    
  Energy:
    - ExxonMobil
    - Mitsubishi Chemical
    
  Technology:
    - Samsung
    - Cleveland Clinic
    - University Alliance
```

## Quantum Error Correction

### Error Mitigation (Current)

```yaml
Techniques:
  Zero-Noise Extrapolation:
    - Run circuit at different noise levels
    - Extrapolate to zero noise
    
  Probabilistic Error Cancellation:
    - Randomize errors
    - Statistical cancellation
    
  Dynamical Decoupling:
    - Insert pulses to protect coherence
```

### Error Correction (Future)

```yaml
Surface Code:
  - 2D grid of qubits
  - Data + ancilla qubits
  - Syndrome measurement
  - Logical error suppression
  
Overhead:
  - ~1,000 physical qubits per logical qubit (current estimates)
  - Decoding algorithms (CPU/GPU)
  - Real-time error correction
```

## Quantum-Safe Security

### Threat Timeline

```
Harvest Now, Decrypt Later:
  Today: Adversaries collect encrypted data
  ~2030: Cryptographically-relevant quantum computer
  Post-2030: Decryption of today's data
  
Mitigation: Deploy quantum-safe cryptography now
```

### IBM Quantum-Safe Offerings

| Product | Function |
|---------|----------|
| **IBM Quantum Safe Explorer** | Crypto inventory |
| **IBM Quantum Safe Advisor** | Risk assessment |
| **IBM Quantum Safe Remediator** | Migration support |
| **z16/z17 Quantum Safe** | Hardware-accelerated |

### Algorithms

| Algorithm | Type | Standard |
|-----------|------|----------|
| CRYSTALS-Kyber | Key encapsulation | NIST FIPS 203 |
| CRYSTALS-Dilithium | Digital signatures | NIST FIPS 204 |
| SPHINCS+ | Stateless signatures | NIST FIPS 205 |

## Learning Resources

### Documentation
- [Qiskit Documentation](https://qiskit.org/documentation/)
- [IBM Quantum Learning](https://learning.quantum.ibm.com/)
- [IBM Quantum Network](https://www.ibm.com/quantum/network)

### Courses
- Qiskit Textbook (free)
- IBM Quantum Learning platform
- University partnerships

### Community
- Qiskit Slack
- GitHub repositories
- Quantum User Groups

---

*Source: IBM Quantum Roadmap, Qiskit Documentation, IBM Research Publications, NIST PQC Standards*
