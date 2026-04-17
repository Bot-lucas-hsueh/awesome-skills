## § 4 · Core Philosophy

### 4.1 The MFU Decomposition Model

```
MFU = Compute Efficiency × Communication Efficiency × I/O Efficiency × Scheduling Efficiency

Compute Efficiency = actual_compute
  - Losses: pipeline bubbles (PP), activation recomputation, dtype overhead

Communication Efficiency = compute_time
  - Losses: all-reduce latency, NCCL ring startup overhead, IB congestion

I/O Efficiency = 1 - (storage_stall_time
  - Losses: checkpoint blocking, slow DataLoader, NFS contention

Scheduling Efficiency = actual_GPU_hours
  - Losses: job queue wait, gang scheduling delay, node provisioning time

Example breakdown for 48% MFU:
  Theoretical max:           100%
  Pipeline bubble (PP=4):    -15%  → 85%
  All-reduce overhead:       -20%  → 65%
  Activation recomputation:  -10%  → 55%
  Checkpoint + I/O stalls:   -7%   → 48%
```

**Insight**: Identify the largest MFU loss category before optimizing. Communication overhead is usually the biggest lever.

### 4.2 Guiding Principles

1. **MFU > Everything Else**: All infrastructure decisions should be evaluated by their impact on MFU. A 2% MFU improvement on a 1000-GPU cluster saves ~20 GPU-hours per day.

2. **Design for Failure at Scale**: At 1000 GPUs, expect 4+ hardware failures per day. If your training job cannot survive a single GPU failure, it will never complete a 30-day run.

3. **Network Bandwidth is Never Free**: Every GB/s of IB bandwidth costs ~$3K hardware + $500/month power. Never over-provision without an MFU model showing the ROI.

---

