# Advanced Packaging Technology Reference Guide

> **Last Updated:** 2025-03-21  
> **Classification:** Technical Advisory - TSMC Advanced Packaging Portfolio

---

## TSMC 3DFabric™ Platform Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    TSMC 3DFabric Portfolio                       │
├─────────────────────────────────────────────────────────────────┤
│  FRONT-END (Wafer Level)                                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │   SoIC-P    │  │   SoIC-X    │  │    InFO (Fan-Out)       │ │
│  │ Micro Bump  │  │  Hybrid     │  │  PoP / oS / B / MS      │ │
│  │   ≤55μm     │  │  Bonding    │  │                         │ │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│  BACK-END (Assembly Level)                                      │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │           CoWoS (Chip-on-Wafer-on-Substrate)              │ │
│  │    CoWoS-S    │    CoWoS-L    │    CoWoS-R               │ │
│  │   Silicon     │    LSI+       │    Organic               │ │
│  │  Interposer   │   RDL Hybrid  │    RDL Only              │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

---

## CoWoS Family (2.5D Integration)

### CoWoS-S (Silicon Interposer)

**Architecture:**
```
┌─────────────────────────────────────┐
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐  │
│  │ HBM │ │ SoC │ │ SoC │ │ HBM │  │  ← Top dies
│  │     │ │  1  │ │  2  │ │     │  │
│  └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘  │
│     └───────┴───────┴───────┘     │
│      ┌─────────────────┐          │
│      │ Silicon         │          │  ← Passive interposer
│      │ Interposer      │          │
│      │ (TSV, Cu Pillar)│          │
│      └─────────────────┘          │
│           ┌─────────┐             │
│           │ Organic │             │  ← Substrate
│           │ Package │             │
│           └─────────┘             │
└─────────────────────────────────────┘
```

**Specifications:**
| Parameter | Specification |
|-----------|---------------|
| Interposer Size | Up to 2.5 reticle (~1,725 mm²) |
| Line/Space | 0.4/0.4 μm (minimum) |
| TSV Pitch | 40 μm |
| HBM Stacks | Up to 6 |
| Max BW | ~4 TB/s (6× HBM2e) |
| Applications | AI training, HPC |

---

### CoWoS-L (Local Silicon Interconnect)

**Architecture:**
```
┌─────────────────────────────────────────────────┐
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐      │
│  │ HBM │ │ SoC │ │ LSI │ │ SoC │ │ HBM │      │
│  │  1  │ │  1  │ │     │ │  2  │ │  2  │      │
│  └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘      │
│     └────────┴───────┴───────┴───────┘        │
│      ┌─────────────────────────────┐          │
│      │ Organic RDL + LSI Tiles     │          │
│      │ (Hybrid approach)           │          │
│      └─────────────────────────────┘          │
│           ┌─────────┐                         │
│           │ Organic │                         │
│           │ Package │                         │
│           └─────────┘                         │
└─────────────────────────────────────────────────┘
```

**Specifications:**
| Parameter | Specification |
|-----------|---------------|
| Interposer Size | Up to 3.5+ reticle (~2,400 mm²) |
| LSI Features | Sub-micron routing |
| RDL Layers | 3-4 layers organic |
| HBM Stacks | 8-12 |
| Max BW | ~26 TB/s (8× HBM3e) |
| Applications | Next-gen AI, B200, MI300X |

**Advantages over CoWoS-S:**
- Larger reticle support
- Lower cost per mm² for large designs
- Better scalability

---

### CoWoS-R (Organic RDL)

**Architecture:**
- No silicon interposer
- Multi-layer organic RDL
- Cost-optimized for lower I/O count

**Specifications:**
| Parameter | Specification |
|-----------|---------------|
| RDL Line/Space | 2/2 μm |
| Layers | 3-5 organic |
| HBM Stacks | Up to 2 |
| Cost | ~50% of CoWoS-S |
| Applications | Inference, edge AI |

---

## InFO Family (Fan-Out Wafer-Level Packaging)

### InFO_PoP (Package-on-Package)

**Architecture:**
```
┌─────────────────┐
│   Mobile DRAM   │
│   (LPDDR5)      │
└────────┬────────┘
         │ µBump
┌────────┴────────┐
│                 │
│   AP SoC        │  ← Face-down on RDL
│   (A17, SD8G3)  │
│                 │
└────────┬────────┘
    ┌────┴────┐
    │  RDL    │      ← Redistributed traces
    │ Layers  │
    └────┬────┘
    ┌────┴────┐
    │ Solder  │
    │  Balls  │
    └─────────┘
```

**Specifications:**
| Parameter | InFO_PoP Gen 2 |
|-----------|----------------|
| RDL Layers | 5 |
| Line/Space | 2/2 μm |
| Package Size | Up to 17×17 mm |
| Height | <1 mm |
| Applications | Smartphones, tablets |

---

### InFO_oS (Wafer-on-Substrate)

**Use Case:** Multi-die HPC integration

**Specifications:**
- Supports 2-5 dies
- RDL-based interconnect
- Lower cost than CoWoS for moderate I/O

---

## SoIC Family (3D Integration)

### SoIC-P (Micro Bump Bonding)

**Architecture:**
```
┌─────────────────┐
│   Top Die       │
│   (Logic/Memory)│
└────────┬────────┘
         │ µBump (9-25μm pitch)
┌────────┴────────┐
│   Bottom Die    │
│   (Base/Logic)  │
└─────────────────┘
```

**Specifications:**
| Parameter | SoIC-P |
|-----------|--------|
| Bump Pitch | 9-25 μm |
| Bonding | Thermal compression |
| Applications | Memory stacking, die partition |

---

### SoIC-X (Hybrid Bonding)

**Architecture:**
```
┌─────────────────┐
│   Top Die       │
│   (Compute)     │
└────────┬────────┘
         │ Direct Cu-Cu bond
┌────────┴────────┐
│   Bottom Die    │
│   (Memory/Base) │
└─────────────────┘
```

**Specifications:**
| Parameter | SoIC-X |
|-----------|--------|
| Bond Pitch | <9 μm (targeting <1 μm) |
| Bonding | Hybrid (oxide + Cu) |
| Advantages | No bump, higher density, lower power |
| Applications | AMD MI300, 3D SRAM |

---

## Packaging Selection Guide

### By Application

| Application | Recommended | Alternative | Notes |
|-------------|-------------|-------------|-------|
| Smartphone SoC | InFO_PoP | FC-CSP | Thin profile critical |
| AI Training (8 HBM) | CoWoS-L | CoWoS-S (6 HBM) | Large reticle needed |
| AI Inference (2 HBM) | CoWoS-R | InFO_oS | Cost optimization |
| CPU + HBM | CoWoS-S | CoWoS-L | Standard HPC |
| 3D Logic Stacking | SoIC-X | SoIC-P | Highest density |
| RF/Analog | InFO_B | WLCSP | Bottom-only exposure |

### By Interconnect Density

| I/O Density | Technology | Pitch |
|-------------|------------|-------|
| Very High (>10K/mm²) | SoIC-X | <9 μm |
| High (1-10K/mm²) | CoWoS-S/L | 40-55 μm |
| Medium (100-1K/mm²) | InFO_oS | 130 μm |
| Low (<100/mm²) | FC-BGA | 150+ μm |

### By Cost Sensitivity

| Budget Level | Options |
|--------------|---------|
| Premium (unlimited) | CoWoS-L, SoIC-X |
| Standard | CoWoS-S, InFO_oS |
| Cost-sensitive | CoWoS-R, InFO_B |
| Lowest cost | FC-CSP, QFN |

---

## Thermal Management

### Thermal Resistance Comparison

| Package Type | ΘJA (°C/W) | Max Power |
|--------------|------------|-----------|
| InFO_PoP | 15-25 | 5-8W |
| CoWoS-S | 8-12 | 300-450W |
| CoWoS-L | 6-10 | 600-800W |
| FC-BGA | 10-15 | 100-200W |

### Cooling Options

| Power Range | Cooling Solution |
|-------------|------------------|
| <10W | Passive heatsink |
| 10-100W | Active fan + heatsink |
| 100-300W | Vapor chamber |
| 300-700W | Liquid cold plate |
| >700W | Immersion cooling |

---

## Design Considerations

### CoWoS Design Rules

1. **Die Placement:**
   - HBM spacing: 0.1-0.2 mm
   - SoC-to-HBM: Match JEDEC HBM PHY
   - Thermal hotspots: Spread across package

2. **Interconnect:**
   - HBM routing: Matched length, differential pairs
   - Power delivery: Dedicated planes
   - Signal integrity: Minimize via transitions

3. **Thermal:**
   - TIM selection critical for >300W
   - Warpage control through die placement
   - Thermal vias in interposer

### Known Good Die (KGD) Testing

**Critical for Multi-Die Packages:**
- Pre-assembly wafer test
- Speed binning
- Defect mapping
- Repair strategy

**Cost Impact:**
- Untested die: Package scrap risk
- KGD testing: $50-200 per die
- Net benefit: Essential for large dies

---

*Document Version: 1.0.0 | Technical Advisory*
