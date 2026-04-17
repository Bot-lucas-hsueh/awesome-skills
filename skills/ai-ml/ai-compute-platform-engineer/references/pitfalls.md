## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Synchronous Checkpoint Blocking Training

```
❌ BAD: Save full checkpoint every 500 steps → 280 GB LLaMA-70B checkpoint → 56 seconds blocked
        At 20 sec/step: 500 steps = 2.78 hours; 56s checkpoint = 3.4% MFU loss PER checkpoint
        If checkpoint is buggy, you lose 2.78 hours of compute

✅ GOOD: Async checkpoint to background thread; sharded per-rank (DCP)
        Each rank saves only its shard (~280 GB
        Async write: training continues immediately; no blocking
        Verify integrity: compare checkpoint hash vs. saved hash after write
```

**Anti-Pattern 2: Not Validating NCCL Uses InfiniBand

```
❌ BAD: Deploy cluster; NCCL silently falls back to TCP Ethernet (10 Gb/s vs. 200 Gb/s IB)
        Observed MFU: 18% — 2.5× below expectation; team spends 2 weeks debugging

✅ GOOD: On every training start, add NCCL debug logging:
        export NCCL_DEBUG=INFO
        grep "NET/IB" in init logs — if missing, check NCCL_SOCKET_IFNAME
        Run nccl-tests all_reduce_perf: must achieve >120 GB/s busbw for 200 Gb/s IB
```

### 🟡 Medium Severity

**Anti-Pattern 3: Over-Provisioning InfiniBand

```
❌ BAD: "Buy 2× IB NICs per node for redundancy" — costs 40% more than necessary
        For DP-only training, IB BW is rarely the bottleneck beyond 4× NICs

✅ GOOD: Size IB based on gradient traffic:
        Required BW = 2 × grad_size
        For LLaMA-70B, FP16 grads, 20s step: 2 × 140GB / 20s = 14 GB/s per node
        4× 200 Gb/s IB = 4 × 25 GB/s = 100 GB/s — 7× headroom for TP overhead
        Additional IB only needed if pipeline parallelism >8 stages
```

