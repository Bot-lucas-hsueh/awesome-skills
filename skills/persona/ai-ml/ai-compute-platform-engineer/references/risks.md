## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|---------------------|
| **Silent Data Corruption (SDC)** | 🔴 Critical | H100/A100 GPUs can silently produce NaN/Inf results without raising errors; detected only by model loss divergence | Enable NVIDIA DCGM health checks; run XID error monitoring; implement loss sanity checks every 100 steps |
| **Checkpoint Data Loss** | 🔴 High | Non-atomic checkpoint writes leave partial files; power failure mid-write corrupts saves from 10+ hours of computation | Use atomic write (write to tmp → rename); keep 3 checkpoints in rolling window; verify checkpoint integrity post-write |
| **NCCL Timeout Cascades** | 🟡 High | A single slow GPU (thermal throttling, PCIe errors) causes all-reduce to timeout, killing the entire job | Set NCCL_TIMEOUT (default 30min → 10min); enable per-rank GPU health monitoring; implement watchdog process |
| **Storage I/O Amplification** | 🟡 Medium | All N ranks writing checkpoint to shared Lustre simultaneously causes bandwidth collapse | Use per-rank sharded checkpoint (PyTorch Distributed Checkpoint); stagger writes across ranks |

**⚠️ IMPORTANT
- A GPU cluster running at 40% MFU is NOT a poorly utilized cluster — it is performing at industry average. World-class clusters (Meta, Google) achieve 55–65% MFU. 40% is acceptable; <30% indicates systemic issues.

- Never run distributed training without checkpoint-and-resume validation before the first production run.

---
