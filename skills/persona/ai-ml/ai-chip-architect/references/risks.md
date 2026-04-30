## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|---------------------|
| **Process Node Risk** | 🔴 High | Tape-out at advanced nodes (3nm/5nm) costs $50–300M; a single re-spin adds 6–9 months delay | Gate all architecture decisions through formal Design Rule Check (DRC); freeze architecture 6 months before tape-out |
| **Bandwidth Underestimation** | 🔴 High | Actual HBM BW utilization is typically 60–75% of spec (1 TB/s HBM3 → effective ~650 GB/s) due to random access patterns | Always derate memory BW by 30–40% in roofline calculations; use DRAM access traces from profiling, not marketing specs |
| **Compiler Gap** | 🟡 Medium | Custom ISAs without compiler support deliver 10–30% of peak FLOPS in practice | Co-design ISA and MLIR/TVM lowering passes from day 1; benchmark with production models, not microbenchmarks |
| **Thermal Throttling** | 🟡 Medium | Burst performance may exceed sustained TDP, triggering throttling and killing SLA | Design for sustained throughput at TDP, not burst peak; measure tokens/sec/W, not TOPS alone |

**⚠️ IMPORTANT
- TFLOPS numbers in product specs are peak theoretical — always divide by 3 to estimate real-world AI workload throughput.

- Memory bandwidth bottlenecks cannot be fixed in software; they must be identified in the architecture phase.

---
