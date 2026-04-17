## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: TOPS Maximization Without Roofline Analysis

```
❌ BAD: "We added 4× more MAC units to double our TOPS. Why is inference not faster?"
         (workload was memory-bound — compute capacity was already idle)

✅ GOOD: Before adding MACs, compute: AI = FLOPS
         If AI < ridge_point → memory-bound; increase HBM BW or improve data reuse first
         Only add MACs when AI > ridge_point (compute-bound)
```

**Anti-Pattern 2: Designing Hardware Before Compiler

```
❌ BAD: "We built a novel ISA with 2D DMA operations, then realized TVM/MLIR can't lower to it.
         Compiler team will figure it out."
         → 18 months later: 15% MAC utilization on production workloads

✅ GOOD: Co-design ISA with MLIR lowering passes from day 1.
         For every new instruction: write the corresponding MLIR pattern before RTL coding.
         Golden rule: if you can't tile + fuse + schedule it in the compiler, don't add the op.
```

### 🟡 Medium Severity

**Anti-Pattern 3: Using Peak Specs for Planning

```
❌ BAD: Planning system capacity using 100% HBM BW utilization
         ("We have 1 TB/s, so we can handle X tokens/sec")

✅ GOOD: Derate memory BW by 30–40% for realistic planning:
         Effective BW = spec_BW × 0.65 (random access patterns, DRAM refresh, bank conflicts)
         H100 HBM3: 3.35 TB/s spec → 2.2 TB/s effective for irregular AI workloads
```

