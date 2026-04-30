# Zen Architecture Reference

## Zen Architecture Evolution

| Generation | Year | Process | IPC Uplift | Key Innovation |
|------------|------|---------|------------|----------------|
| **Zen** | 2017 | 14nm | Baseline | SMT return, new uArch |
| **Zen+** | 2018 | 12nm | +3% | Process refinement |
| **Zen 2** | 2019 | 7nm | +15% | Chiplet design debut |
| **Zen 3** | 2020 | 7nm | +19% | Unified CCX (8C) |
| **Zen 4** | 2022 | 5nm | +13% | DDR5, PCIe Gen5 |
| **Zen 5** | 2024 | 4nm | +16% | AVX-512, improved frontend |
| **Zen 5c** | 2024 | 4nm | ~Zen 5 | Density-optimized variant |

## Zen 5 Microarchitecture Details

### Front-End
| Feature | Specification |
|---------|---------------|
| Decode Width | 8 instructions/cycle |
| Branch Predictor | Improved TAGE-based |
| L1I Cache | 32KB, 8-way |
| L1I TLB | 64 entries |
| Op Cache | 6K uops |

### Execution Engine
| Feature | Specification |
|---------|---------------|
| Dispatch Width | 8 uops/cycle |
| Integer Units | 6 ALUs |
| FP/SIMD Units | 3 FPUs |
| AVX-512 Support | 256-bit datapath |
| Reorder Buffer | ~448 entries |

### Memory Subsystem
| Feature | Specification |
|---------|---------------|
| L1D Cache | 48KB, 12-way |
| L1D Load | 4 loads/cycle |
| L1D Store | 2 stores/cycle |
| L2 Cache | 1MB per core, 8-way |
| L3 Cache | 32MB per CCD |

## Chiplet Architecture

### CCD (Core Complex Die)
```
┌─────────────────────────────────────┐
│  CCD Layout (Zen 5)                 │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐   │
│  │ CCX │ │ CCX │ │ CCX │ │ CCX │   │
│  │(2C) │ │(2C) │ │(2C) │ │(2C) │   │
│  └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘   │
│     └───────┴───────┴───────┘      │
│           32MB L3 Cache             │
│        (Shared across CCD)          │
└─────────────────────────────────────┘
```

- 8 cores per CCD (standard Zen 5)
- 16 cores per CCD (Zen 5c density variant)
- 32MB L3 cache per CCD
- TSMC 4nm process

### IOD (I/O Die)
| Feature | Desktop IOD | Server IOD (SP5) |
|---------|-------------|------------------|
| Process | 6nm | 6nm |
| Memory Channels | 2x DDR5 | 12x DDR5 |
| PCIe Lanes | 28x Gen5 | 128x Gen5 |
| Graphics | RDNA 2 (2 CUs) | None |
| USB4 | Optional | No |

### 3D V-Cache
| Generation | Tech | Capacity | Position |
|------------|------|----------|----------|
| 1st Gen X3D | SRAM stack | 64MB | On top of CCD |
| 2nd Gen X3D | SRAM stack | 64MB | Under CCD |

**2nd Gen Improvement**: Better thermals → higher clocks, full overclocking support

## Infinity Fabric

### IF Links
| Generation | Speed | Usage |
|------------|-------|-------|
| IF Gen 3 | 2400 MT/s | Zen 4/5 CCD-IOD |
| IF Gen 4 | 3200 MT/s | Future platforms |

### Topology
- Ring-based for intra-CCD
- Star topology for CCD-IOD
- Up to 12 CCDs per IOD (server)

## Product Specifications

### Ryzen 9000 Series (Desktop)
| SKU | Cores | Threads | Base | Boost | L3 | TDP | Price |
|-----|-------|---------|------|-------|----|-----|-------|
| 9950X3D | 16 | 32 | 4.3 | 5.7 | 128MB | 170W | $699 |
| 9950X | 16 | 32 | 4.3 | 5.7 | 64MB | 170W | $599 |
| 9900X3D | 12 | 24 | 4.4 | 5.5 | 128MB | 120W | $599 |
| 9900X | 12 | 24 | 4.4 | 5.6 | 64MB | 120W | $469 |
| 9800X3D | 8 | 16 | 4.7 | 5.2 | 96MB | 120W | $479 |
| 9700X | 8 | 16 | 3.8 | 5.5 | 32MB | 65/105W | $329 |
| 9600X | 6 | 12 | 3.9 | 5.4 | 32MB | 65W | $249 |

### EPYC 9005 Series (Server)
| SKU | Cores | Threads | TDP | L3 | Target |
|-----|-------|---------|-----|----|--------|
| 9965 | 192 | 384 | 500W | 384MB | Cloud density |
| 9755 | 128 | 256 | 500W | 512MB | HPC/Enterprise |
| 9655 | 96 | 192 | 400W | 384MB | General server |
| 9455 | 48 | 96 | 300W | 256MB | Enterprise |

## Performance Benchmarks

### IPC Progression
| Workload | Zen 4 | Zen 5 | Uplift |
|----------|-------|-------|--------|
| SPECint | Baseline | +16% | 16% |
| SPECfp | Baseline | +15% | 15% |
| Gaming | Baseline | +8% | 8% |
| Cinebench | Baseline | +18% | 18% |

### 3D V-Cache Impact (Gaming)
| Metric | Standard | X3D | Improvement |
|--------|----------|-----|-------------|
| L3 Hit Rate | 65% | 85% | +30% |
| Avg FPS | 280 | 340 | +21% |
| 1% Lows | 180 | 240 | +33% |

---

*Source: AMD Tech Day 2024, HotChips, ISSCC, Product Datasheets*
*Last Updated: 2026-03-21*
