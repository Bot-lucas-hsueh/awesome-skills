## § 7 · Standards & Reference

### 7.1 Zen 5 Microarchitecture

| Feature | Specification |
|---------|---------------|
| **Process Node** | TSMC 4nm (CCD), 6nm (IOD) |
| **Front-end** | 8-wide decode, improved branch predictor |
| **Execution** | 6 ALUs, 3 FPUs, 256-bit AVX-512 |
| **Load/Store** | 4 loads + 2 stores per cycle |
| **L1 Cache** | 32KB + 48KB per core |
| **L2 Cache** | 1MB per core |
| **L3 Cache** | 32MB per CCD (CCD-shared) |
| **IPC Uplift** | 16% vs Zen 4 (average) |

### 7.2 Memory Hierarchy Comparison

| Level | Latency | Bandwidth (per core) |
|-------|---------|---------------------|
| L1 Cache | ~4 cycles | 2 TB/s |
| L2 Cache | ~12 cycles | 1 TB/s |
| L3 Cache | ~40 cycles | 400 GB/s |
| DDR5-6400 | ~80ns | 51 GB/s |
| HBM3 (MI300X) | ~500ns | 5.3 TB/s (aggregate) |

### 7.3 AMD vs Competition (2024)

| Segment | AMD | Intel | NVIDIA | AMD Position |
|---------|-----|-------|--------|--------------|
| Desktop CPU | Ryzen 9000 | Core Ultra 200 | — | Leadership (gaming) |
| Server CPU | EPYC 9005 | Xeon 6 | — | Leadership (TCO) |
| Data Center GPU | MI300X | — | H100/H200 | Challenger (value) |
| Gaming GPU | RX 7900 XTX | — | RTX 4090 | Competitive |

---
