## §5 · Technical Architecture Patterns

### §5.1 · AWS Well-Architected Framework

| Pillar | Key Question | Amazon Principle |
|--------|--------------|------------------|
| **Operational Excellence** | How do we run and monitor systems? | Dive Deep, Insist on Highest Standards |
| **Security** | How do we protect information? | Earn Trust, Ownership |
| **Reliability** | How do we recover from failures? | Think Big, Deliver Results |
| **Performance Efficiency** | How do we use resources efficiently? | Frugality, Invent and Simplify |
| **Cost Optimization** | How do we minimize costs? | Frugality, Ownership |
| **Sustainability** | How do we minimize environmental impact? | Success and Scale Bring Broad Responsibility |

### §5.2 · The Amazon Flywheel (Retail)

```
        Lower Prices
             ↑
   Better      →    More Customer
   Selection       Traffic
      ↑                ↓
   Third-Party    Higher Sales
   Sellers       Volume
             ↓
        Lower Cost Structure
```

**Key Insight:** Each element drives the next, creating a self-reinforcing growth loop.

### §5.3 · Service-Oriented Architecture

**API Mandate (2002):**
> "All teams will expose their data and functionality through service interfaces. Teams must communicate with each other through these interfaces. No other inter-process communication is allowed."

**Benefits:**
- Teams can innovate independently
- Services can be replaced without system-wide changes
- Scale components independently
- Force clear contracts and boundaries

### §5.4 · Document Types by Purpose

| Document Type | Length | Purpose | Audience |
|---------------|--------|---------|----------|
| **PR/FAQ** | 6 pages | Product definition | Cross-functional teams |
| **6-page narrative** | 6 pages | Strategy/decision | Leadership |
| **2-pager** | 2 pages | Status update | Leadership |
| **1-pager** | 1 page | Quick decision | Immediate team |
| **COE (Correction of Errors)** | 2-5 pages | Post-incident analysis | Affected teams |

---
