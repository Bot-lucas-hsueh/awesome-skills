## § 4 · Supply Chain Frameworks

### 4.1 SCOR Model Overview

```
SCOR (Supply Chain Operations Reference) — 5 Domains:

PLAN  → Balance supply & demand; S&OP, IBP, capacity planning
SOURCE → Procure goods & services; sourcing, purchasing, supplier management
MAKE  → Transform inputs to outputs; manufacturing, assembly, packaging
DELIVER → Fulfill customer orders; warehousing, transportation, last-mile
RETURN → Handle reverse flows; returns, repairs, recycling, disposal

Key Performance Attributes:
  Reliability:   OTIF (On-Time In-Full), perfect order rate
  Responsiveness: Order fulfillment cycle time
  Agility:       Upside/downside supply chain flexibility
  Cost:          COGS, supply chain cost as % of revenue
  Asset Management: Inventory days, cash-to-cash cycle time
```

### 4.2 Inventory Optimization Formulas

```python
[Code block moved to code-block-1.md]
```

### 4.3 ABC/XYZ Segmentation Matrix

| Segment | Volume (ABC) | Variability (XYZ) | Strategy |
|---------|-------------|-------------------|----------|
| **AX** | High value | Low variability | Lean, low safety stock, automated replenishment |
| **AY** | High value | Medium variability | Statistical safety stock, demand sensing |
| **AZ** | High value | High variability | Reserve capacity, flexible supply, VMI |
| **BX** | Medium value | Low variability | EOQ-based replenishment |
| **BY** | Medium value | Medium variability | Standard safety stock |
| **BZ** | Medium value | High variability | Consignment or make-to-order |
| **CX** | Low value | Low variability | Bulk purchasing, annual replenishment |
| **CY/CZ** | Low value | High variability | Standardize, substitute, or eliminate |

### 4.4 Supplier Segmentation (Kraljic Matrix)

```
                    Low Supply Risk ←————————→ High Supply Risk
High Business    ┌─────────────────┬──────────────────────┐
Impact          │   LEVERAGE       │   STRATEGIC           │
                │ (Exploit buying  │ (Long-term            │
                │ power; multiple  │ partnership;          │
                │ suppliers)       │ joint development)    │
                ├─────────────────┼──────────────────────┤
Low Business    │   NON-CRITICAL   │   BOTTLENECK          │
Impact          │ (Automate;       │ (Secure supply;       │
                │ reduce admin     │ hold safety stock;    │
                │ cost)            │ dual-source)          │
                └─────────────────┴──────────────────────┘

Action by Quadrant:
  Leverage:       Competitive bidding; volume consolidation; price benchmarking
  Strategic:      Supplier development; joint forecasting; long-term contracts
  Bottleneck:     Dual sourcing; buffer inventory; qualification of alternatives
  Non-critical:   Catalog purchasing; P-card; tail spend management
```

---
