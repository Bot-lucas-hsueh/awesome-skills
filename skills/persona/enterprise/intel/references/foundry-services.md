# Intel Foundry Services (IFS) Reference

> **Document:** Intel Foundry Business Deep Dive  
> **Last Updated:** 2026-03-21

---

## Overview

**Intel Foundry Services (IFS)** is the foundry arm of Intel Corporation, created as part of the IDM 2.0 strategy to manufacture chips for external customers. This represents a fundamental shift — Intel fabs now serve both internal products and external fabless semiconductor companies.

---

## IFS Value Proposition

### 1. Leading-Edge Technology Access

| Node | Availability | Key Features | External Customer Timeline |
|------|--------------|--------------|---------------------------|
| Intel 16 | Now | 22FFL derivative, RF capable | Production |
| Intel 3 | Now | Enhanced 7nm, high performance | Production |
| Intel 18A | Q3 2025 | RibbonFET + PowerVia | Risk production, volume H2 2025 |
| Intel 18A-P | 2026 | Enhanced 18A for HPC/AI | 2026 |
| Intel 14A | 2027 | 1.4nm, High-NA EUV | Development |

### 2. U.S.-Based Manufacturing

| Fab | Location | Nodes | Status |
|-----|----------|-------|--------|
| Ronler Acres | Oregon | All leading-edge | Operational |
| Fab 52/62 | Arizona | Intel 18A+ | Expanding |
| Ohio One | Ohio | Intel 18A+ | Under construction |
| Rio Rancho | New Mexico | Packaging | Operational |

**Strategic Benefits:**
- Supply chain resilience
- Reduced geopolitical risk (vs. Taiwan concentration)
- CHIPS Act incentives
- "Made in America" for government/military

### 3. Advanced Packaging

| Technology | Capability | Pitch | Use Case |
|------------|------------|-------|----------|
| Foveros | 3D die stacking | 36μm | Client chiplets |
| Foveros Direct | 3D copper-to-copper | <5μm | HBM, logic-on-logic |
| EMIB | 2.5D bridging | 55μm | Multi-die integration |
| EMIB-T | Enhanced EMIB | 45μm | High bandwidth |
| Co-EMIB | Large die assembly | N/A | Multi-reticle designs |

---

## Customer Engagement Model

### Engagement Tiers

| Tier | Description | Commitment | Support Level |
|------|-------------|------------|---------------|
| **Strategic** | Long-term partnership, co-development | Multi-year, high volume | Dedicated team, PDK customization |
| **Volume** | High-volume production | Annual commitments | Priority support |
| **Project** | Specific tape-out | Per-project | Standard support |

### Design Enablement

**Process Design Kits (PDKs):**
- Digital PDK (standard cells, memories)
- Analog/RF PDK (transistor models, passive components)
- IO/ESD PDK (I/O cells, ESD protection)

**EDA Partnerships:**
- Synopsys: Fusion Compiler, Custom Compiler
- Cadence: Innovus, Virtuoso
- Mentor (Siemens): Calibre
- Ansys: RedHawk, Totem

**IP Ecosystem:**
- Arm: Processor IP (Cortex, Neoverse)
- Synopsys: Interface IP, security IP
- Cadence: Memory IP, interface IP
- Alphawave: PCIe, CXL, Ethernet

---

## Notable Customers & Wins

### Announced Customers

| Customer | Product | Node | Status |
|----------|---------|------|--------|
| **Microsoft** | Custom AI chip | Intel 18A | Announced 2025 |
| **Qualcomm** | Mobile/PC SoC | Intel 20A/18A | Announced |
| **MediaTek** | Various | Intel 16 | Production |
| **Amazon/AWS** | Various (rumored) | Intel 18A | In discussion |

### Government Programs

| Program | Description | Value |
|---------|-------------|-------|
| **RAMP-C** | Rapid Assured Microelectronics Prototypes - Commercial | DOD program for secure chips |
| **CHIPS Act** | U.S. government funding | Up to $8.5B grants + $11B loans |
| **Secure Enclave** | U.S. government-only capacity | Intel 18A for defense |

---

## Financial Performance

### IFS Revenue Progression

| Quarter | Revenue | YoY Change | Notes |
|---------|---------|------------|-------|
| Q2 2024 | $4.3B | - | Baseline |
| Q3 2024 | $4.2B | - | Slight decline |
| Q4 2024 | $4.5B | - | Recovery |
| Q1 2025 | $4.3B | - | Stable |
| Q2 2025 | $4.4B | +3% | Growth returning |

### Foundry Business Model (Lip-Bu Tan Era)

**Key Changes Under New CEO:**
1. **Separate P&L**: Foundry has its own profit/loss statement
2. **Arm's Length Pricing**: Internal products pay market rates
3. **Customer Commitments Required**: No capacity expansion without external commitments
4. **Financial Discipline**: Focus on profitable growth, not just volume

**Targets:**
- Foundry revenue: $10B+ by 2026
- External customer ratio: Target 50%+ of leading-edge capacity
- Capacity utilization: >90% mature nodes, >70% leading edge

---

## Competitive Comparison

### IFS vs TSMC vs Samsung Foundry

| Dimension | Intel IFS | TSMC | Samsung |
|-----------|-----------|------|---------|
| **Leading Node** | Intel 18A (2025) | N3E (2023), N2 (2025) | 3GAP (2022), 2nm (2025) |
| **Technology Edge** | PowerVia (backside power) | N2 GAA, volume leadership | First GAA |
| **U.S. Manufacturing** | Yes (OR, AZ, OH) | No (planned in AZ) | No (planned in TX) |
| **Government Support** | CHIPS Act ($8.5B+) | Limited | Limited |
| **Advanced Packaging** | Foveros, EMIB | CoWoS, InFO | I-Cube, H-Cube |
| **Customer Track Record** | Growing | Established leader | Limited leading-edge |

### Competitive Positioning

**IFS Advantages:**
- U.S.-based leading-edge capacity
- Backside power (1 year ahead)
- Government/military programs
- Advanced packaging integration
- CHIPS Act funding

**IFS Challenges:**
- Proving yield/reliability at scale
- Building customer trust (new to foundry)
- Ecosystem maturity vs. TSMC
- Internal product conflicts

---

## Service Offerings

### Wafer Fabrication

| Service | Description |
|---------|-------------|
| **Full Mask** | Standard production masks |
| **Multi-Project Wafer (MPW)** | Shared masks for prototyping |
| **Shuttle** | Regular MPW runs for test chips |

### Packaging Services

| Service | Description |
|---------|-------------|
| **Wafer Sort** | Testing at wafer level |
| **Assembly** | Die packaging |
| **Test** | Final testing |
| **Full Turnkey** | Design → wafer → package → test |

### Design Services

| Service | Description |
|---------|-------------|
| **Design Consultation** | Architecture guidance |
| **IP Integration** | Third-party IP support |
| **Sign-off Support** | Physical verification |
| **Yield Learning** | Post-silicon optimization |

---

## Key Metrics & SLAs

### Manufacturing Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Cycle Time** | Industry competitive | Fab entry to wafer out |
| **Yield** | >70% (leading edge) | Good die per wafer |
| **On-Time Delivery** | >95% | To committed dates |
| **Quality** | <100 DPM | Defects per million |

### Customer Satisfaction

| Metric | Target |
|--------|--------|
| **NPS Score** | >50 (world-class) |
| **Design Win Rate** | >60% of qualified opportunities |
| **Repeat Business** | >80% customer retention |

---

## References

- Intel Foundry Direct Connect 2025
- Intel Q2 2025 Earnings Report
- Intel Foundry Services Website
- Semiconductor Industry Association Reports
