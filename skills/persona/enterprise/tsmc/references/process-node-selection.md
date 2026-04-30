# Process Node Selection Reference Guide

> **Last Updated:** 2025-03-21  
> **Classification:** TSMC Technology Advisory

---

## Technology Node Roadmap Overview

```
2024        2025        2026        2027        2028        2029        2030
 |           |           |           |           |           |           |
 N3E --------+--------->
             N2 --------+--------->
                         N2P ----->
                         A16 ----->
                                     A14 ----->
                                                 A10 ----->
```

---

## Detailed Node Specifications

### N3E (3nm Enhanced) - Production Ready

**Technology:**
- FinFET (3rd generation)
- EUV: 25+ layers
- Design Rules: 23nm gate pitch, 45nm metal pitch

**Performance Metrics:**
| Metric | vs N5 | vs N3 (base) |
|--------|-------|--------------|
| Performance | +18% | +5% |
| Power | -34% | -12% |
| Density | 1.6x | 1.05x |

**Applications:**
- Smartphones (Apple A17 Pro, Snapdragon 8 Gen 3)
- Consumer SoCs
- Mid-range AI accelerators

**Cost:** ~$18,000 per 300mm wafer

**Yield Status:** >85% (mature)

---

### N2 (2nm) - Risk Production

**Technology:**
- GAA (Gate-All-Around) Nanosheet transistors
- First node with GAA architecture
- EUV: 30+ layers

**Performance Metrics:**
| Metric | vs N3E |
|--------|--------|
| Performance | +15% |
| Power | -30% |
| Density | 1.15x |

**Key Innovations:**
- Nanosheet width variability for design optimization
- Reduced leakage vs FinFET
- Better electrostatic control

**Applications:**
- High-Performance Computing (HPC)
- AI training accelerators
- Next-gen smartphone SoCs

**Cost:** ~$22,000 per 300mm wafer

**Availability:** H2 2025 (HVM)

---

### N2P (2nm Plus) - Enhanced Performance

**Technology:**
- N2 foundation + Backside Power Delivery Network (BSPDN)
- Power rails moved to wafer backside
- Reduced IR drop, improved power delivery

**Performance vs N2:**
- Performance: +5-10%
- Power: Additional -5-10%
- Area: -5% (better routing)

**Applications:**
- High-frequency server CPUs
- AI accelerators requiring >500W TDP

**Availability:** 2026

---

### A16 (1.6nm) - HPC Optimized

**Technology:**
- Super Power Rail (SPR) technology
- Enhanced BSPDN with power-through-silicon
- Targeting >1kW chips

**Performance vs N2:**
- Performance: +10%
- Power: Comparable
- Target: Maximum power delivery efficiency

**Applications:**
- Data center AI training chips
- Exascale computing
- Cloud TPU/AI accelerators

**Availability:** 2026

---

### A14 (1.4nm) - Next Generation

**Technology:**
- 2nd generation GAA nanosheet
- NanoFlex Pro architecture
- High-NA EUV introduction

**Performance vs N2:**
| Metric | Improvement |
|--------|-------------|
| Performance | +15% |
| Power | -30% |
| Density | 1.23x |

**Variants:**
- **A14:** Standard mobile/HPC
- **A14P:** Performance with backside power
- **A14X:** Extreme performance
- **A14C:** Cost-optimized

**Applications:**
- iPhone 19 Pro (A21 chip)
- Next-gen AI accelerators
- High-performance GPUs

**Availability:** H2 2028

---

## Selection Decision Matrix

### By Application

| Application | Recommended Node | Alternative | Notes |
|-------------|------------------|-------------|-------|
| Smartphone flagship | N3E (now), N2 (2025+) | N2P | Balance PPA |
| Smartphone mid-range | N4, N4P | N3E | Cost optimization |
| AI Training (Data Center) | N2, A16 | N2P | Power efficiency critical |
| AI Inference (Edge) | N4, N3E | N5 | Cost vs performance |
| Automotive (ADAS) | N7A, N5A | N3E | Qualification time |
| Networking (Switch/PHY) | N7, N5 | N4 | Mixed signal friendly |
| Consumer IoT | N28, N22 | N16 | Lowest cost |

### By Power Target

| Power Budget | Recommended Node | Notes |
|--------------|------------------|-------|
| <5W (Mobile) | N3E, N2 | Maximum efficiency |
| 5-50W (Tablet/Laptop) | N3E, N2 | Balanced approach |
| 50-200W (Desktop) | N2, N2P | Performance focus |
| 200-500W (Server) | N2P, A16 | Power delivery critical |
| >500W (AI Training) | A16, A14P | Backside power required |

### By Die Size Economics

| Die Size | Consideration |
|----------|---------------|
| <100mm² | Leading edge justified (high volume) |
| 100-400mm² | Leading edge standard |
| 400-800mm² | Consider chiplet/disaggregation |
| >800mm² | Chiplet architecture mandatory |

---

## Design Cost Estimates

| Node | Design Cost | Mask Cost | EDA Tool Cost |
|------|-------------|-----------|---------------|
| N28 | $40M | $500K | $2M/year |
| N16 | $80M | $1M | $3M/year |
| N7 | $217M | $5M | $5M/year |
| N5 | $416M | $10M | $8M/year |
| N3 | $590M | $15M | $12M/year |
| N2 | $725M+ | $25M | $15M/year |

*Source: IBS, industry estimates*

---

## Migration Considerations

### From N5 to N3E
- **Porting Effort:** Medium (same FinFET)
- **Key Changes:** Updated PDK, new DRC rules
- **Timeline:** 6-9 months redesign
- **Benefit:** 18% performance or 34% power reduction

### From N3E to N2
- **Porting Effort:** High (FinFET → GAA)
- **Key Changes:** New transistor models, layout migration
- **Timeline:** 12-18 months redesign
- **Benefit:** 15% performance + 30% power

### From N2 to A16
- **Porting Effort:** Medium (same GAA base)
- **Key Changes:** Backside power integration
- **Timeline:** 6-12 months redesign
- **Benefit:** Power delivery for high-wattage designs

---

## Node Selection Checklist

- [ ] Define performance, power, area (PPA) targets
- [ ] Calculate cost-per-transistor economics
- [ ] Evaluate design resource requirements
- [ ] Confirm EDA tool readiness
- [ ] Assess IP availability (memory, interface, analog)
- [ ] Validate packaging compatibility
- [ ] Secure capacity allocation
- [ ] Plan for yield learning curve

---

*Document Version: 1.0.0 | Technology Advisory Only*
