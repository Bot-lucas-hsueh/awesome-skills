## § 3 · Risk Disclaimer

| Risk | Severity | Mitigation | Escalation |
|------|----------|------------|------------|
| **Numerical Precision Loss** | 🔴 Critical | Careful FP8/FP4 validation, loss scaling, accuracy regression tests | Reject if accuracy drop >0.5% |
| **Memory Exhaustion (OOM)** | 🔴 Critical | Gradient checkpointing, activation checkpointing, ZeRO partitioning | Kill switch before OOM, graceful degradation |
| **NCCL Communication Deadlocks** | 🔴 Critical | Topology-aware rank assignment, async error handling, timeout configs | Abort with NCCL_DEBUG=INFO logs |
| **Thermal Throttling** | 🔴 High | Power capping, thermal design validation, monitoring | Auto-scale down workload |
| **TensorRT Build Failures** | 🟡 Medium | ONNX verification, explicit batch shapes, plugin fallback | Fallback to PyTorch baseline |
| **CUDA Version Compatibility** | 🟡 Medium | Container-based deployment, version pinning | Compatibility matrix validation |
| **Export Control Compliance** | 🟡 Medium | Classification review, regional deployment restrictions | Legal/compliance escalation |

---
