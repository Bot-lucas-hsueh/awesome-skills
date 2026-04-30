# Intel Process Technology Reference

> **Document:** Process Technology Deep Dive  
> **Last Updated:** 2026-03-21

---

## Overview

Intel's process technology roadmap centers on the ambitious "5 Nodes in 4 Years" initiative, launched under former CEO Pat Gelsinger, now being executed with financial discipline under CEO Lip-Bu Tan. The crown jewel is **Intel 18A** (1.8nm class), featuring RibbonFET gate-all-around transistors and PowerVia backside power delivery.

---

## Process Node Roadmap Detail

### Intel 7 (10nm Enhanced SuperFin)

| Attribute | Specification |
|-----------|---------------|
| Launch Year | 2021 |
| Key Technology | Enhanced SuperFin, improved channel mobility |
| Products | Alder Lake, Raptor Lake, Sapphire Rapids |
| Status | Production (mature) |
| Notes | Intel's last FinFET node before EUV transition |

### Intel 4 (7nm with EUV)

| Attribute | Specification |
|-----------|---------------|
| Launch Year | 2023 |
| Key Technology | First EUV lithography, 7nm equivalent |
| Products | Meteor Lake (Compute Tile) |
| Status | Production |
| Density Improvement | 2x Intel 7 |
| Notes | First Intel node using ASML EUV scanners |

### Intel 3 (Enhanced 7nm)

| Attribute | Specification |
|-----------|---------------|
| Launch Year | 2024 |
| Key Technology | Enhanced EUV, improved transistor performance |
| Products | Granite Rapids, Sierra Forest, Arrow Lake (some tiles) |
| Status | Production |
| Performance | 18% perf/Watt vs Intel 4 |
| Notes | Last FinFET node before RibbonFET transition |

### Intel 20A (2nm RibbonFET Introduction)

| Attribute | Specification |
|-----------|---------------|
| Launch Year | 2024 |
| Key Technology | RibbonFET (GAA), PowerVia |
| Products | Arrow Lake (initial production) |
| Status | Limited production |
| Features | First GAA, first backside power |
| Notes | Transition/risk node before 18A maturity |

### Intel 18A (1.8nm — The Crown Jewel)

| Attribute | Specification |
|-----------|---------------|
| Launch Year | 2025 |
| Key Technology | Optimized RibbonFET, optimized PowerVia |
| Products | Panther Lake, Clearwater Forest, external customers |
| Status | Risk production (Q2 2025), Volume H2 2025 |
| Density | +30% vs Intel 3 |
| Performance | +15% perf/Watt vs Intel 3 |
| PowerVia Benefit | 5-10% area reduction, up to 4% iso-power perf |

**Intel 18A Variants:**
- **Intel 18A**: Standard node for general products
- **Intel 18A-P**: Enhanced performance for HPC/AI
- **Intel 18A-PT**: With Foveros Direct 3D for chiplet stacking

### Intel 14A (1.4nm — Next Generation)

| Attribute | Specification |
|-----------|---------------|
| Launch Year | 2027 (target) |
| Key Technology | PowerDirect, High-NA EUV |
| Products | Future client/server processors |
| Status | Development |
| Risk | Lip-Bu Tan has indicated this is "key risk" if execution slips |

---

## RibbonFET Technology Deep Dive

### What is RibbonFET?

RibbonFET is Intel's implementation of **Gate-All-Around (GAA)** transistor architecture, replacing the FinFET structure used since Intel 22nm.

### FinFET vs RibbonFET

```
FinFET (Current):                    RibbonFET (New):
    ┌───┐                              ╭───╮
    │Gate│ surrounds fin on 3 sides    │Gate│ surrounds ribbon on ALL sides
    └───┘                              ╰───╯
      │                                ═════
    ══╧══ (Fin)                        (Ribbon/Nanosheet)
```

### RibbonFET Advantages

| Advantage | Mechanism | Benefit |
|-----------|-----------|---------|
| Better Electrostatic Control | Gate surrounds channel on 4 sides | Reduced leakage, better switching |
| Variable Width | Ribbons can be made wider/narrower | Flexible drive strength optimization |
| Continued Scaling | Enables scaling beyond 2nm | Future node viability |
| Reduced Variability | Better channel control | Higher yields, better power characteristics |

### RibbonFET Implementation

- **Nanosheet Structure**: Multiple horizontal sheets stacked vertically
- **Gate Material**: Workfunction metal gates
- **Channel Material**: Silicon or Silicon-Germanium depending on application

---

## PowerVia Technology Deep Dive

### What is PowerVia?

PowerVia is Intel's **backside power delivery network (BSPDN)** — an industry-first implementation at Intel 18A that moves power rails to the backside of the wafer.

### Traditional vs PowerVia Power Delivery

```
Traditional (Frontside):            PowerVia (Backside):
┌─────────────────┐                 ┌─────────────────┐
│ Signal + Power  │                 │  Signals Only   │
│   (competing)   │                 │  (more space)   │
├─────────────────┤                 ├─────────────────┤
│    Transistors  │                 │    Transistors  │
├─────────────────┤                 ├─────────────────┤
│    Substrate    │                 │  Power Rails    │
│                 │                 │  (nano-TSVs)    │
└─────────────────┘                 └─────────────────┘
```

### PowerVia Benefits

| Benefit | Mechanism | Quantified Impact |
|---------|-----------|-------------------|
| Reduced Signal Congestion | Power rails off frontside | 5-10% area reduction |
| Better Signal Integrity | Cleaner signal routing | Improved timing closure |
| Lower IR Drop | Dedicated power path | Better voltage delivery |
| Performance Improvement | Reduced power noise | Up to 4% at iso-power |

### PowerVia Implementation

1. **Fabrication**: Transistors built on frontside first
2. **Wafer Flip**: Wafer flipped and thinned
3. **Nano-TSVs**: Through-silicon vias etched to connect backside power to frontside
4. **Power Rail Formation**: Backside metallization for power distribution

---

## Manufacturing & Yield Considerations

### Copy EXACTLY! Philosophy

Intel's manufacturing philosophy requires:
- Identical equipment configurations across fabs
- Identical process recipes
- Identical metrology and quality control

This ensures:
- Predictable yields across sites
- Rapid ramp of new nodes
- Consistent quality

### Yield Metrics

| Node | Target Yield | Current Status |
|------|--------------|----------------|
| Intel 7 | >90% | Mature, exceeding targets |
| Intel 4 | >85% | Production stable |
| Intel 3 | >80% | Production ramping |
| Intel 18A | >70% | Risk production, targeting H2 2025 |

### Key Manufacturing Sites

| Site | Location | Nodes | Notes |
|------|----------|-------|-------|
| Ronler Acres | Hillsboro, OR | All leading-edge | Primary development fab |
| Fab 52 | Chandler, AZ | Intel 18A + | High-volume production |
| Rio Rancho | Albuquerque, NM | Packaging/Testing | Foveros, EMIB |
| New Albany | Ohio | Intel 18A (future) | Under construction |

---

## Competitive Comparison

### Intel vs TSMC vs Samsung

| Node | Intel | TSMC | Samsung |
|------|-------|------|---------|
| 7nm class | Intel 4 (2023) | N7 (2018) | 7LPP (2018) |
| 5nm class | Intel 3 (2024) | N5 (2020) | 5LPE (2020) |
| 3nm class | Intel 18A (2025) | N3 (2022) | 3GAP (2022) |
| 2nm class | Intel 14A (2027) | N2 (2025) | 2nm (2025) |
| GAA Timing | 2025 (18A) | 2025 (N2) | 2022 (3GAP) |
| Backside Power | 2025 (PowerVia) | 2026+ | Unknown |

### Key Competitive Insights

- **Intel Advantage**: PowerVia gives Intel ~1 year lead in backside power
- **TSMC Advantage**: N2 launches 2025 with GAA, earlier volume
- **Samsung Advantage**: First to GAA (3GAP), but struggling with yields

---

## References

- Intel Foundry Direct Connect 2025
- Intel Q2 2025 Earnings Report
- Intel Technology Roadmap (Investor Day 2024)
- IEEE International Electron Devices Meeting (IEDM) Papers
