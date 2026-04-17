## § 6 — Professional Toolkit

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **QuTiP** | Quantum toolbox in Python; Lindblad master equation, Bloch-Redfield | Noise modeling, open quantum system simulation, pulse optimization |
| **Qiskit Pulse** | Pulse-level circuit programming for IBM hardware | Custom pulse shaping, DRAG implementation, cross-resonance calibration |
| **QCoDeS** | Data acquisition framework for experimental quantum labs | Instrument control, parameter sweeps, automated characterization |
| **pyGST (pyGSTi)** | Gate Set Tomography library | Rigorous per-gate fidelity characterization beyond RB |
| **cirq + Google QCS** | Google's circuit framework; supports Sycamore pulse control | Google hardware experiments; custom gate sequences |
| **Labber** | Instrument control and measurement automation | LabVIEW-based; used in Dilution refrigerator control systems |
| **Superconducting Qubit Designer (SQDLab)** | Qubit geometry and Josephson parameter design | EJ/EC computation, junction area sizing, coupling capacitor design |
| **SONNET (Anthropic)** | LLM-assisted quantum physics reasoning | Code explanation, paper summarization, literature review |
| **Jupyter + matplotlib** | Data analysis and visualization | T1/T2 fitting, RB decay curve analysis |
| **scipy.optimize** | Curve fitting for coherence and benchmarking data | Exponential T1 fits, RB decay parameter extraction |
| **AWG (Keysight M3202A, Zurich Instruments HDAWG)** | Arbitrary waveform generation for qubit control | Pulse shaping, IQ modulation, multi-channel synchronization |
| **TWPA/JPA amplifiers (Josephson Traveling-Wave/Parametric Amp)** | Near-quantum-limited readout amplification | High-fidelity single-shot readout; reduces measurement backaction |

---
