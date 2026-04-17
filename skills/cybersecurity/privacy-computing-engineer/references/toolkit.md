## § 6 · Professional Toolkit

| Tool | Category | Specific Purpose |
|------|----------|-----------------|
| **Microsoft SEAL** | Homomorphic Encryption | BFV and CKKS scheme implementation; use for integer arithmetic (BFV) and approximate floating-point (CKKS); Microsoft-maintained, well-audited C++ library with Python bindings |
| **HElib** | Homomorphic Encryption | BGV and CKKS with bootstrapping support for deep circuits; developed by IBM; use when multiplicative depth exceeds SEAL practical limits |
| **OpenFHE** | Homomorphic Encryption | Unified library supporting BFV, BGV, CKKS, FHEW, TFHE; use for TFHE gate-by-gate Boolean circuit evaluation and fast bootstrapping |
| **Concrete ML** | Homomorphic Encryption | Zama's framework for ML over HE; converts scikit-learn and PyTorch models to FHE circuits; use when data scientists (not cryptographers) need to deploy HE inference |
| **PySyft** | Federated Learning
| **Flower (flwr)** | Federated Learning | Framework-agnostic FL orchestration; supports TensorFlow, PyTorch, JAX; use for cross-device and cross-silo federation with pluggable aggregation strategies |
| **FATE Framework** | Federated Learning | Industrial-grade FL platform from WeBank; supports SMPC-based federated statistics and ML; preferred for financial sector deployments requiring auditability |
| **OpenDP** | Differential Privacy | Formally verified DP library; use for composable DP measurements with proven correctness; supports zCDP, Renyi DP, approximate DP accountants |
| **TensorFlow Privacy** | Differential Privacy | DP-SGD optimizer for TensorFlow models; use for differentially private deep learning; integrates Renyi accountant for training round composition |
| **Opacus** | Differential Privacy | PyTorch DP training library from Meta; use for DP-SGD with per-sample gradient clipping; supports RDP accountant and privacy amplification by subsampling |
| **Intel SGX SDK** | TEE | C/C++ SDK for writing SGX enclaves; use for sensitive computation requiring hardware-rooted trust; includes attestation library and sealed storage APIs |
| **Enarx** | TEE | Hardware-abstraction layer for TEEs; runs WebAssembly workloads in SGX, SEV-SNP, or TrustZone without code changes; use for portable TEE deployment across cloud providers |

---
