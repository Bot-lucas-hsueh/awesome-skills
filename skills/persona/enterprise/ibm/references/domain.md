## § 4 · Domain Knowledge

### § 4.1 · Red Hat OpenShift Deep Dive

**Architecture**:
```yaml
OpenShift Container Platform:
  Control Plane:
    - Kubernetes API server
    - etcd (distributed key-value store)
    - OpenShift Controller Manager
    - OpenShift Scheduler
  
  Worker Nodes:
    - CRI-O container runtime
    - Kubelet node agent
    - OpenShift SDN (OVN-Kubernetes)
    - Multus CNI for multi-network
  
  Platform Add-ons:
    - OpenShift Pipelines: Tekton-based CI/CD
    - OpenShift GitOps: ArgoCD-based deployment
    - OpenShift Service Mesh: Istio-based
    - OpenShift Serverless: Knative-based
    - OpenShift Virtualization: KubeVirt for VMs
  
  Developer Experience:
    - OpenShift Dev Spaces: Cloud-based IDE
    - Developer Hub: Backstage-based portal
    - Helm, Kustomize support
```

**Hybrid Cloud Patterns**:
| Pattern | Solution | Use Case |
|---------|----------|----------|
| Cloud Bursting | OpenShift + cloud autoscaling | On-prem baseline, cloud peak |
| DR/HA | Multi-cluster OpenShift | Business continuity |
| Edge Computing | OpenShift Edge (3-node) | Manufacturing, retail, telco |
| Dev/Test/Prod | Namespace isolation | Environment management |
| VM + Container | OpenShift Virtualization | Gradual modernization |

### § 4.2 · watsonx Platform Technical Guide

**watsonx.ai Architecture**:
```python
# watsonx.ai deployment configuration
watsonx_config = {
    "foundation_models": {
        "granite_3_8b": {
            "context_window": 128000,
            "use_cases": ["chat", "summarization", "code"],
            "license": "apache_2"
        },
        "granite_code_20b": {
            "languages": ["python", "java", "javascript", "go"],
            "use_cases": ["code_gen", "code_explain", "modernization"]
        }
    },
    "deployment_options": {
        "saas": "ibm_cloud_watsonx",
        "software": "cp4d_watsonx (on-prem)",
        "dedicated": "single_tenant_cloud"
    },
    "integrations": {
        "vector_db": ["milvus", "pgvector", "elastic"],
        "rag_framework": "watsonx_assistant",
        "langchain": "supported",
        "llamaindex": "supported"
    }
}
```

**AI Governance (watsonx.governance)**:
```markdown
Governance Capabilities:
├── Model Cards: Document model purpose, performance, limitations
├── Bias Detection: Monitor protected attributes across demographics
├── Drift Detection: Track data and model drift over time
├── Explainability: SHAP-based explanations for predictions
├── Risk Scoring: Assign risk levels to AI use cases
├── Lifecycle Management: Version control, A/B testing, rollback
└── Regulatory Reporting: EU AI Act, FDA, financial regulations
```

### § 4.3 · IBM Z Mainframe Modernization

**z16/z17 Technical Specifications**:
| Feature | z16 | z17 |
|---------|-----|-----|
| Processor | Telum (7nm) | Next-gen Telum |
| AI Inference | 300B requests/day | Enhanced capacity |
| Latency | <1ms per inference | Sub-millisecond |
| Encryption | Quantum-safe (CRYSTALS) | Quantum-safe + |
| Availability | 99.99999% | 99.99999%+ |

**Modernization Strategies**:
```
┌─────────────────────────────────────────────────────────────────┐
│               Mainframe Modernization Approaches                 │
├──────────────┬──────────────────────────────────────────────────┤
│ REHOST       │ Lift-and-shift to Linux on IBM Z                │
│              │ • z/OS containers (zCX)                          │
│              │ • Minimal code changes                           │
├──────────────┼──────────────────────────────────────────────────┤
│ REFACTOR     │ Incremental modernization                        │
│              │ • COBOL to Java services                         │
│              │ • API enablement (z/OS Connect)                  │
├──────────────┼──────────────────────────────────────────────────┤
│ REPLATFORM   │ Containerize with OpenShift                      │
│              │ • Microservices architecture                     │
│              │ • Gradual strangler fig pattern                  │
├──────────────┼──────────────────────────────────────────────────┤
│ REPLACE      │ Cloud-native rebuild                             │
│              │ • For select workloads only                      │
│              │ • Preserve core transaction processing           │
└──────────────┴──────────────────────────────────────────────────┘
```

### § 4.4 · IBM Quantum Computing

**Qiskit Runtime Example**:
```python
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Estimator, Options

# Initialize IBM Quantum service
service = QiskitRuntimeService(channel="ibm_quantum")

# Create quantum circuit for VQE (Variational Quantum Eigensolver)
def create_uccsd_circuit(num_qubits, num_electrons):
    """
    Unitary Coupled Cluster circuit for molecular simulation.
    Used in drug discovery and materials science.
    """
    qc = QuantumCircuit(num_qubits)
    # Hartree-Fock initial state
    for i in range(num_electrons):
        qc.x(i)
    # UCCSD ansatz
    # ... (circuit construction)
    return qc

# Execute on IBM Quantum hardware
options = Options(optimization_level=3, resilience_level=1)
estimator = Estimator(session=service.backend('ibm_sherbrooke'), options=options)

# Run hybrid classical-quantum algorithm
result = estimator.run(circuits=[circuit], observables=[hamiltonian]).result()
```

**IBM Quantum Network Tiers**:
| Tier | Access | Use Case |
|------|--------|----------|
| Premium | Priority queue, 28+ systems | Enterprise research |
| Explorer | Standard queue | Academic, startup |
| Community | Simulators, limited hardware | Learning, experimentation |

---
