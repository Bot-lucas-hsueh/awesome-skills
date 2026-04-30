# CoWoS Capacity Planning Reference Guide

> **Last Updated:** 2025-03-21  
> **Classification:** TSMC Internal Reference - Customer Advisory

---

## Executive Summary

CoWoS (Chip-on-Wafer-on-Substrate) advanced packaging is currently the most significant bottleneck in the AI semiconductor supply chain. TSMC has doubled capacity annually in 2024 and 2025, yet demand continues to exceed supply by 2-3x.

---

## CoWoS Technology Variants

### CoWoS-S (Silicon Interposer)
- **Technology:** Passive silicon interposer with sub-micron L/S
- **Max Reticle Size:** 2.5 reticles (~1,725 mm²)
- **HBM Capacity:** Up to 6 stacks
- **Applications:** H100, MI250, mainstream AI accelerators
- **Cost:** $$ (Mid-range)
- **Availability:** Moderate constraint

### CoWoS-L (Local Silicon Interconnect)
- **Technology:** Hybrid approach - LSI for HBM routing + organic RDL for power
- **Max Reticle Size:** 3.5+ reticles (~2,400 mm²)
- **HBM Capacity:** 8-12 stacks
- **Applications:** B200, MI300X, next-gen AI training chips
- **Cost:** $$$ (Premium)
- **Availability:** Most constrained

### CoWoS-R (Organic RDL)
- **Technology:** Organic redistribution layer (no silicon interposer)
- **Max Reticle Size:** 2 reticles
- **HBM Capacity:** Up to 2 stacks
- **Applications:** Inference accelerators, cost-optimized AI
- **Cost:** $ (Lowest)
- **Availability:** Less constrained

---

## Capacity Roadmap

| Year | CoWoS-S (wpm) | CoWoS-L (wpm) | CoWoS-R (wpm) | Total (wpm) |
|------|---------------|---------------|---------------|-------------|
| 2023 | 10,000 | 5,000 | 2,000 | 17,000 |
| 2024 | 20,000 | 15,000 | 5,000 | 40,000 |
| 2025 | 22,000 | 45,000 | 10,000 | 77,000 |
| 2026E | 25,000 | 80,000 | 15,000 | 120,000 |
| 2027E | 25,000 | 100,000 | 20,000 | 145,000 |
| 2028E | 25,000 | 125,000 | 25,000 | 175,000 |

*Source: TSMC earnings calls, supply chain estimates, Morgan Stanley research*

---

## Customer Allocation (2025 Estimate)

| Customer | CoWoS-S Share | CoWoS-L Share | Notes |
|----------|---------------|---------------|-------|
| **NVIDIA** | 30% | 70% | B100/B200, Blackwell architecture |
| **AMD** | 25% | 15% | MI300 series, Instinct line |
| **Broadcom** | 15% | 8% | Google TPU, custom ASICs |
| **Amazon** | 10% | 2% | Trainium, Inferentia |
| **Google** | 8% | 3% | Internal TPU (via Broadcom) |
| **Microsoft** | 5% | 1% | Maia 100, Athena |
| **Others** | 7% | 1% | Meta, Tesla, startups |

---

## Securing CoWoS Capacity

### Tier 1 Customers (No Prepayment Required)
- Apple, NVIDIA, AMD, Broadcom
- Long-term strategic partnerships
- Volume-based allocation rights

### Tier 2 Customers (Prepayment Required)
- Cloud hyperscalers (AWS, Google, Azure)
- 10-20% prepayment for capacity reservation
- 12-18 month commitment horizon

### Tier 3 Customers (Full Prepayment)
- Startups, new entrants
- 30-50% prepayment
- Limited to CoWoS-S or overflow capacity

### Alternative Sources

**ASE Technology:**
- CoWoS-equivalent: FOEB (Fan-Out Embedded Bridge)
- Capacity: Expanding rapidly
- Premium: 10-15% vs TSMC
- Quality: Qualified for many designs

**Amkor:**
- SWIFT (Silicon Wafer Integrated Fan-Out Technology)
- Focus: Cost-sensitive applications
- Capacity: Limited leading-edge

---

## Cost Structure

| Component | CoWoS-S | CoWoS-L | CoWoS-R |
|-----------|---------|---------|---------|
| Interposer | $400-600 | $800-1,200 | $100-200 |
| Assembly | $300-400 | $500-700 | $200-300 |
| Test (KGD) | $200-300 | $300-400 | $150-200 |
| **Total Package** | **$900-1,300** | **$1,600-2,300** | **$450-700** |

*Note: Costs exclude HBM and compute die. Based on 2024-2025 pricing estimates.*

---

## Capacity Planning Best Practices

1. **Engage Early:** Submit RFQ 18-24 months before production ramp
2. **Provide Accurate Forecasts:** Monthly wafer volume projections
3. **Commit to Volumes:** Minimum 1K wafers/month for dedicated capacity
4. **Consider Packaging Alternatives:** Evaluate InFO_oS for lower bandwidth needs
5. **Monitor HBM Supply:** CoWoS capacity meaningless without HBM3e allocation

---

## Key Contacts

- **Sales Account Team:** Primary engagement for capacity requests
- **Advanced Packaging Division:** Technical co-design support
- **EDA Partners:** Cadence, Synopsys for package design tools

---

*Document Version: 1.0.0 | For Official Use Only*
