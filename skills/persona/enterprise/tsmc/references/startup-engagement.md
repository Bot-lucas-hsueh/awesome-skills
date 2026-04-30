# Fabless Startup Engagement Guide

> **Last Updated:** 2025-03-21  
> **Target Audience:** Semiconductor Startups, VCs, First-Time Founders

---

## TSMC Startup Ecosystem Overview

TSMC supports the fabless ecosystem through multiple pathways, from proof-of-concept to production scale. This guide outlines practical steps for startups to access TSMC technology.

---

## Engagement Pathways

### Pathway 1: CyberShuttle (Multi-Project Wafer)

**What is CyberShuttle?**
- Shared mask program - multiple designs on one reticle
- Cost-effective way to get first silicon
- Available for mature and advanced nodes

**Available Nodes:**
| Node | Cost Range | Min Feature | Use Case |
|------|------------|-------------|----------|
| N28 | $30K-50K | 28nm | IoT, analog |
| N16 | $50K-80K | 16nm | Cost-sensitive digital |
| N7 | $100K-150K | 7nm | High-performance test |
| N5 | $150K-200K | 5nm | AI/ML validation |
| N4 | $180K-220K | 4nm | Mobile SoC test |

**Process:**
1. Submit design for shuttle slot (quarterly schedule)
2. Pass DRC/LVS verification
3. Pay program fee
4. Receive 10-50 packaged samples
5. Timeline: 6-9 months

**Best For:**
- First silicon bring-up
- IP validation
- Proof-of-concept demonstrations
- University research

---

### Pathway 2: Design Center Alliance (DCA)

**Certified Design Partners:**

| Partner | Location | Specialization | Typical Project Size |
|---------|----------|----------------|---------------------|
| **GUC** | Taiwan, Global | Full-service, advanced nodes | $1M-10M |
| **Alchip** | Taiwan, China | High-performance, AI | $500K-5M |
| **eSilicon** | Global | Networking, HPC | $1M-8M |
| **Faraday** | Taiwan | Mixed-signal, ASIC | $300K-3M |
| **AndesTech** | Taiwan | RISC-V, edge AI | $200K-2M |

**What DCA Partners Provide:**
- RTL-to-GDSII design services
- TSMC relationship management
- Volume aggregation (better pricing)
- IP ecosystem access
- Package design and test

**Business Model:**
- NRE (Non-Recurring Engineering): $500K-5M
- Unit margin: 10-30% on wafer costs
- Tool licenses: Often included

---

### Pathway 3: OIP VCAD (Value Chain Aggregator)

**Qualification Requirements:**
- Series B funding or equivalent
- Demonstrated product-market fit
- Clear production roadmap
- Minimum volume commitment (10K+ wafers annually)

**Benefits:**
- Direct TSMC AE support
- Early PDK access
- EDA partner program discounts
- IP partner pre-negotiated rates

---

## Funding Requirements by Stage

### Stage 1: Proof of Concept (Months 1-12)

**Activities:**
- Architecture validation
- FPGA emulation
- CyberShuttle tape-out

**Budget:** $500K - $2M

| Item | Cost |
|------|------|
| CyberShuttle (2-3 runs) | $200K-400K |
| EDA tools (1-year license) | $100K-300K |
| Packaging & test | $50K-100K |
| Engineering team (3-5 people) | $500K-1M |
| IP licenses (ARM, etc.) | $100K-500K |

**Funding Source:** Seed, Series A

---

### Stage 2: Product Development (Months 13-24)

**Activities:**
- Full-chip design
- Dedicated mask set tape-out
- Bring-up and validation

**Budget:** $3M - $10M

| Item | Cost |
|------|------|
| DCA partner NRE | $1M-3M |
| Mask set (N5-N3) | $3M-5M |
| EDA tools (multi-year) | $500K-1M |
| Initial wafer production | $1M-3M |
| Engineering team (10-15) | $2M-4M |

**Funding Source:** Series A, Series B

---

### Stage 3: Production Ramp (Months 25+)

**Activities:**
- Volume production
- Cost optimization
- Next-gen planning

**Budget:** $10M+ annually

| Item | Cost |
|------|------|
| Wafer production (1K wpm) | $15M-25M/year |
| Advanced packaging (if needed) | $5M-15M/year |
| Test and qualification | $2M-5M/year |
| Operations team | $3M-5M/year |

**Funding Source:** Series C, Revenue

---

## IP Strategy for Startups

### Processor Cores

| Option | Cost | Performance | Use Case |
|--------|------|-------------|----------|
| **ARM Cortex-A** | $500K-2M license | High | Mobile, application processors |
| **ARM Cortex-M** | $50K-200K | Low-power | IoT, embedded |
| **SiFive RISC-V** | $100K-500K | Medium | AI, custom accelerators |
| **Andes RISC-V** | $50K-300K | Medium | Cost-sensitive designs |
| **Open Source RISC-V** | Free | Variable | Research, non-commercial |

### Memory & Interface IP

| IP Type | Vendors | Typical Cost |
|---------|---------|--------------|
| DDR5/4/3 controller | Cadence, Synopsys, Rambus | $200K-800K |
| PCIe Gen5/6 | PLDA, Synopsys, Cadence | $300K-1M |
| HBM2e/3 controller | Aquantia, Northwest Logic | $500K-1.5M |
| Ethernet (100G/400G) | MorethanIP, Cadence | $200K-600K |

---

## Success Factors for Startups

### Technical
1. **Hire experienced physical design engineers** - Foundry relationships matter
2. **Start with proven IP** - Custom IP adds 6+ months
3. **Plan for re-spins** - Budget 2-3 tape-outs for first product
4. **Invest in verification** - 70% of effort should be verification

### Business
1. **Secure anchor customer before full mask set** - De-risks investment
2. **Negotiate volume commitments early** - Better pricing, allocation priority
3. **Consider DCA partner equity** - Some accept equity for NRE
4. **Plan for 18-24 month runway** - Chip development takes time

### Common Pitfalls
- Underestimating mask costs at advanced nodes
- Skipping corner case verification
- Not planning for yield learning
- Over-customizing for first product

---

## Recommended Reading

- TSMC OIP Documentation: https://www.tsmc.com/english/dedicatedFoundry/About/oip
- CyberShuttle Program Guide (contact TSMC sales)
- GUC Startup Program: https://www.guc-asic.com

---

*Document Version: 1.0.0 | Startup Advisory*
