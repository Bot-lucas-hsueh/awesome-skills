# Toyota Supplier Management & Development

## Philosophy

### Partnership Approach

Toyota views suppliers as **extensions of the company**, not as adversaries in price negotiations.

**Core Principles:**

| Principle | Application |
|-----------|-------------|
| **Long-term relationship** | Single-source preferred, multi-year contracts |
| **Mutual prosperity** | Fair pricing, shared cost reductions |
| **Genchi Genbutsu** | Engineers visit suppliers regularly |
| **Kaizen together** | Joint improvement activities |
| **Information sharing** | Open books, transparent targets |

### Keiretsu Structure

**Historical Context:**
- Toyota Group includes cross-shareholdings with key suppliers
- Historically included Denso, Aisin, Toyota Boshoku
- Modern approach: Partnership regardless of ownership

**Current Supplier Structure:**

| Tier | Description | Count |
|------|-------------|-------|
| Tier 1 | Direct suppliers to Toyota | ~200 |
| Tier 2 | Sub-assemblies, components | ~4,000 |
| Tier 3+ | Raw materials, basic parts | ~20,000+ |

---

## Supplier Selection

### Criteria

| Category | Weight | Factors |
|----------|--------|---------|
| **Quality capability** | 30% | History, systems, certification |
| **Technical capability** | 25% | Engineering, innovation, patents |
| **Cost competitiveness** | 20% | Pricing, cost structure |
| **Delivery performance** | 15% | Location, capacity, flexibility |
| **Management** | 10% | Leadership, financial health |

### Selection Process

```
Step 1: Initial screening
├── Technical questionnaire
├── Financial review
└── Reference checks
        ↓
Step 2: Detailed evaluation
├── Site visit (gemba)
├── Manufacturing assessment
├── Quality system audit
└── Technical capability review
        ↓
Step 3: Trial/development
├── Prototype supply
├── Process validation
└── Performance evaluation
        ↓
Step 4: Partnership agreement
├── Long-term contract
├── Target pricing
└── Improvement commitments
```

---

## Supplier Development

### Five-Level Capability Model

```
┌─────────────────────────────────────────────────────────────┐
│ LEVEL 5: Self-Directed Improvement                          │
│ • Supplier leads own Kaizen                                 │
│ • Regular improvement suggestions                           │
│ • Benchmark for other suppliers                             │
│ • Minimal Toyota support needed                             │
├─────────────────────────────────────────────────────────────┤
│ LEVEL 4: Process Capability                                 │
│ • SPC fully implemented                                     │
│ • Process management systems                                │
│ • Predictable, capable output                               │
│ • Occasional Toyota support                                 │
├─────────────────────────────────────────────────────────────┤
│ LEVEL 3: Standardized Work                                  │
│ • Work instructions documented                              │
│ • Training program established                              │
│ • Consistent methods across shifts                          │
│ • Regular Toyota support                                    │
├─────────────────────────────────────────────────────────────┤
│ LEVEL 2: Basic Stability                                    │
│ • 5S implemented                                            │
│ • Basic preventive maintenance                              │
│ • Reactive problem-solving                                  │
│ • Frequent Toyota support                                   │
├─────────────────────────────────────────────────────────────┤
│ LEVEL 1: Firefighting                                       │
│ • No standardization                                        │
│ • Frequent quality escapes                                  │
│ • Need intensive Toyota support                             │
│ • Risk of losing business                                   │
└─────────────────────────────────────────────────────────────┘
```

### Development Process

**90-Day Intensive Program:**

| Week | Focus | Toyota Support |
|------|-------|----------------|
| 1-2 | Current state assessment | On-site team (5 days) |
| 3-4 | Problem-solving training | A3 methodology workshop |
| 5-8 | Process stabilization | Daily calls, weekly visits |
| 9-12 | Standardization | Documentation support |
| 13+ | Self-sustaining | Monthly reviews |

### Gemba Visits

**Purpose:** Go to the actual place to understand the actual situation.

**Frequency:**
- High-risk suppliers: Weekly
- Development suppliers: Monthly
- Mature suppliers: Quarterly

**Activities:**
- Shop floor walk
- Process observation
- Quality data review
- Kaizen identification
- Relationship building

---

## Supplier Performance Management

### Key Metrics

**Quality:**

| Metric | Definition | Target |
|--------|------------|--------|
| PPM (Parts Per Million) | Defects per million parts received | <50 |
| Quality incidents | Line stops or field issues | 0 |
| PPAP approval | First-time pass rate | >95% |
| Warranty claims | Supplier responsibility | <target $ |

**Delivery:**

| Metric | Definition | Target |
|--------|------------|--------|
| On-time delivery | % delivered on schedule | >98% |
| Lead time | Order to delivery | Per agreement |
| Flexibility | Ability to adjust volume | ±20% |

**Cost:**

| Metric | Definition | Target |
|--------|------------|--------|
| Annual reduction | Year-over-year cost improvement | 3-5% |
| VAVE contributions | Value engineering ideas | Quarterly |
| Total cost | Landed cost including quality | Competitive |

### Performance Reviews

**Monthly Scorecard:**

```
SUPPLIER SCORECARD - ABC Manufacturing
Month: January 2025

Quality:     ████████████████████░░░░░  85% (PPM: 45)
Delivery:    ████████████████████████░  96% (OTD: 98%)
Cost:        █████████████████████░░░░  82% (Reduction: 2%)
Technical:   ███████████████████████░░  90% (Support: Excellent)
---------------------------------------------
Overall:     █████████████████████░░░░  88%
```

**Quarterly Business Review (QBR):**

| Agenda Item | Duration | Participants |
|-------------|----------|--------------|
| Performance review | 30 min | Both teams |
| Quality deep-dive | 30 min | Quality teams |
| Cost roadmap | 30 min | Procurement, engineering |
| Technology roadmap | 30 min | Engineering teams |
| Improvement planning | 30 min | Leadership |

---

## Just-in-Time (JIT) with Suppliers

### Milk-Run System

**Concept:**
- Toyota truck visits multiple suppliers
- Picking up small quantities frequently
- Reduces inventory at both ends

**Example Schedule:**

```
Toyota Plant ←───────────────────────────────────────
   ↑                                                  │
   │  ┌─────────┐    ┌─────────┐    ┌─────────┐     │
   └──┤Supplier A├───►Supplier B├───►Supplier C├─────┘
      └─────────┘    └─────────┘    └─────────┘
      8:00 AM        9:30 AM        11:00 AM
      (30 min stop)  (30 min stop)  (30 min stop)
```

**Benefits:**
- Supplier: Known pickup schedule, reduced packaging
- Toyota: Low inventory, frequent deliveries
- Both: Reduced transportation cost per part

### Kanban with Suppliers

**Types:**

| Type | Use Case | Signal |
|------|----------|--------|
| Production Kanban | Trigger supplier production | Card, EDI, web |
| Shipping Kanban | Authorize shipment | Card, label |
| Supplier Kanban | Internal Toyota signal | Barcode, RFID |

**Calculation:**

```
Number of Kanban = (Daily Demand × Lead Time × Safety Factor) / Container Quantity

Example:
- Daily demand: 500 parts
- Lead time: 2 days
- Safety factor: 1.5
- Container: 50 parts

Kanban = (500 × 2 × 1.5) / 50 = 30 kanban
```

### Supplier Production Sequencing

**Purpose:** Match supplier production to Toyota assembly sequence.

**Application:**
- Seats
- Instrument panels
- Bumpers
- Other large/color-matched components

**Process:**

```
Toyota Assembly Sequence: Red→Blue→Red→White→Blue→...
         ↓
Real-time transmission to supplier
         ↓
Supplier builds in exact sequence
         ↓
Delivered just-in-sequence to line
```

---

## Cost Management

### Target Costing Approach

**Process:**

```
Toyota sets target cost for vehicle system
         ↓
Allocate to subsystem targets
         ↓
Negotiate with supplier
         ↓
Supplier commits to target
         ↓
Joint development to achieve target
         ↓
Annual cost reduction (Kaizen)
```

### Cost Breakdown Analysis

**Supplier opens books to Toyota:**

| Cost Element | % of Total | Target |
|--------------|------------|--------|
| Raw materials | 50% | Market price |
| Labor | 15% | Industry benchmark |
| Overhead | 20% | Continuous improvement |
| Profit | 10% | Fair return |
| Logistics | 5% | Optimization |

### Value Analysis/Value Engineering (VA/VE)

**Purpose:** Reduce cost while maintaining function.

**Process:**

| Phase | Activity | Timeline |
|-------|----------|----------|
| Preparation | Select target, assemble team | 1 week |
| Information | Gather data, benchmark | 2 weeks |
| Function | Define required functions | 1 week |
| Creativity | Generate alternatives | 1 week |
| Evaluation | Score alternatives | 1 week |
| Development | Detail winning ideas | 2 weeks |
| Presentation | Recommend to management | 1 week |

**Sharing Benefits:**
- Cost savings shared between Toyota and supplier
- Typically 50-50 split
- Incentivizes supplier participation

---

## Quality Partnership

### Built-in Quality at Supplier

**Expectations:**

| Level | Requirement | Verification |
|-------|-------------|--------------|
| Source | No defects shipped | Self-inspection, Poka-yoke |
| Process | SPC on critical characteristics | Control charts |
| System | ISO/TS 16949 certification | Third-party audit |
| Development | Design FMEA, Process FMEA | Toyota review |

### Supplier Quality Containment

**Border Control:**

```
If supplier quality issues detected:

Level 1: Increased inspection at receiving
Level 2: Sorting at supplier before shipment
Level 3: 100% inspection at Toyota
Level 4: Line stop, containment action
Level 5: Business review, improvement plan
```

### Supplier Quality Awards

**Recognition Categories:**

| Award | Criteria |
|-------|----------|
| Quality Excellence | Zero PPM for 12 months |
| Delivery Excellence | 100% on-time for 12 months |
| Cost Excellence | Exceed reduction targets |
| Technology Excellence | Breakthrough innovation |
| Partnership Award | Overall excellence |

---

## Risk Management

### Risk Assessment

**Categories:**

| Risk | Assessment | Mitigation |
|------|------------|------------|
| **Single source** | Dependency on one supplier | Dual source critical parts |
| **Financial** | Supplier bankruptcy | Financial monitoring |
| **Capacity** | Unable to meet demand | Capacity audits |
| **Geographic** | Natural disaster, political | Geographic diversification |
| **Quality** | Major quality escape | Border inspection, development |

### Supplier Contingency Planning

**Requirements:**

- Backup supplier identified for critical parts
- Tooling ownership clarity
- Emergency response procedures
- Recovery time objectives (RTO)

---

## Digital Supplier Collaboration

### Systems

| System | Function | Access |
|--------|----------|--------|
| EDI | Orders, shipping notices | Electronic |
| Supplier Portal | Performance, forecasts, documents | Web |
| CAD/PLM | Engineering data sharing | Secure access |
| Quality System | Inspection data, SCARs | Shared database |

### Data Sharing

**Transparency:**

| Data | Shared With | Frequency |
|------|-------------|-----------|
| Production forecast | Direct suppliers | Monthly + weekly updates |
| Build sequence | JIT suppliers | Real-time |
| Quality data | All suppliers | Real-time |
| Cost targets | Direct suppliers | Annual |

---

## Best Practices Summary

### Toyota Approach

| Principle | Implementation |
|-----------|----------------|
| **Long-term thinking** | Multi-year relationships, patient development |
| **Genchi Genbutsu** | Regular supplier visits, shop floor focus |
| **Respect** | Fair pricing, shared benefits, no blame |
| **Kaizen** | Joint improvement, continuous learning |
| **JIT** | Frequent deliveries, low inventory |
| **Jidoka** | Built-in quality, no defects passed |

### Lessons for Other Companies

1. **Start with long-term perspective** - Quick wins vs. sustainable partnership
2. **Invest in development** - Help suppliers improve
3. **Share information** - Transparency builds trust
4. **Measure what matters** - Quality, delivery, cost, continuous improvement
5. **Go to gemba** - See actual conditions, build relationships

---

*Reference: Dyer, Jeffrey. "The Relational View" (1996)*
*Liker, Jeffrey. "The Toyota Way" (2004)*
*Takeishi, Akira and Fujimoto, Takahiro. "Modularization and Supplier Relationships" (2001)*
