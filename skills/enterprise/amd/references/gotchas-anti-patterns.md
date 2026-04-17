## § 8 · Gotchas & Anti-Patterns

### #AMD1: Ignoring Chiplet Latency

❌ **Wrong**: Treating multi-chiplet design as monolithic; ignoring CCD-to-CCD latency
✅ **Right**: Thread pinning to minimize cross-CCD communication; NUMA-aware scheduling

### #AMD2: Memory Bandwidth Underestimation

❌ **Wrong**: Designing compute-bound algorithms that are actually memory-bound
✅ **Right**: Roofline analysis first; optimize arithmetic intensity before raw FLOPs

### #AMD3: Neglecting 3D V-Cache Topology

❌ **Wrong**: Spreading gaming threads across both X3D and non-X3D CCDs
✅ **Right**: Pin gaming threads to X3D CCD; background tasks to standard CCD

### #AMD4: ROCm vs CUDA Assumptions

❌ **Wrong**: Assuming CUDA code ports 1:1 to ROCm without optimization
✅ **Right**: Use HIP for portability; profile and optimize for CDNA specifics

### #AMD5: Infinity Fabric Bottlenecks

❌ **Wrong**: Saturating IF links with excessive cross-chiplet traffic
✅ **Right**: Data locality optimization; replicate data vs. sharing when possible

### #AMD6: TDP Headroom Miscalculation

❌ **Wrong**: Designing for sustained boost clocks without thermal headroom
✅ **Right**: Characterize typical workload power; design cooling for 95th percentile

---
