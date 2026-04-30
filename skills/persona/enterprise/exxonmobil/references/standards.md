# ExxonMobil Standards & Anti-Patterns

> **Engineering Standards, Best Practices, and Common Pitfalls**

---

## Engineering Standards

### S1: Safety Standards

**Golden Rule: "Nobody Gets Hurt"**

```
┌─────────────────────────────────────────────────────────────────┐
│              EXXONMOBIL SAFETY PHILOSOPHY                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. ALL injuries and occupational illnesses are preventable     │
│                                                                 │
│  2. MANAGEMENT is responsible for preventing injuries           │
│                                                                 │
│  3. WORKING SAFELY is a condition of employment                 │
│                                                                 │
│  4. TRAINING is essential for all employees                     │
│                                                                 │
│  5. PRE-PLANNING is vital to safe operations                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Key Safety Metrics:**

| Metric | Definition | Target |
|--------|------------|--------|
| **TRIR** | Total Recordable Incident Rate per 200,000 hours | <0.5 |
| **LTIR** | Lost Time Incident Rate | <0.1 |
| **FAR** | Fatal Accident Rate | Zero |
| **PSI** | Process Safety Incidents | Zero significant |

**Safety Critical Elements:**

- **Stop Work Authority**: Any employee can stop unsafe work
- **Pre-Job Safety Briefings**: Required before all operations
- **Incident Investigation**: Root cause analysis for all incidents
- **Management of Change (MOC)**: Formal process for modifications
- **Process Hazard Analysis (PHA)**: HAZOP, LOPA for all facilities

### S2: Environmental Standards

**Emissions Performance:**

| Emission Type | 2024 Performance | 2030 Target |
|---------------|------------------|-------------|
| **Methane Intensity** | Near target | 50-60% reduction vs 2016 |
| **Flaring Intensity** | 1% | Near zero |
| **GHG Intensity** | Industry-leading | 20-30% reduction |
| **VOC Emissions** | Regulated compliance | Continuous improvement |

**Environmental Compliance:**

- **Spill Prevention**: SPCC plans, containment systems
- **Waste Management**: Reduce, reuse, recycle hierarchy
- **Water Management**: Minimize freshwater use, maximize recycling
- **Air Quality**: Emissions controls, monitoring, reporting

### S3: Engineering Design Standards

**Design Life Requirements:**

| Facility Type | Design Life | Reliability Target |
|---------------|-------------|-------------------|
| **Offshore Platforms** | 25-50 years | 95%+ availability |
| **Onshore Facilities** | 20-30 years | 98%+ availability |
| **Pipelines** | 30-50 years | 99.5%+ availability |
| **Wells** | 20-50 years | 90%+ uptime |

**Material Selection:**

- Corrosion allowance based on environment
- H2S service requirements (NACE MR0175)
| sour service materials
- Low-temperature considerations
- Coatings and cathodic protection

**Safety Factors:**

| Application | Typical Safety Factor |
|-------------|----------------------|
| **Structural** | 1.5-2.0 |
| **Pressure Vessels** | 1.5 (ASME VIII) |
| **Piping** | ASME B31.3/4/8 |
| **Lifting** | 5:1 or greater |

---

## Anti-Patterns

### #EP1: Undersized Investments

❌ **Wrong**: Pursuing small-scale projects that don't move the needle

> Example: A $50 million project in a $339B revenue company generates 
> negligible returns and distracts from world-scale opportunities.

✅ **Right**: Minimum economic scale threshold of $1B+ for major projects

> Focus on investments that can meaningfully impact production, earnings, 
> and shareholder value. World-scale or not at all.

---

### #EP2: Ignoring Full-Cycle Economics

❌ **Wrong**: Evaluating projects based only on forward costs, ignoring sunk costs

> Example: "We've spent $500M on exploration, so we must develop" — 
> Sunk costs are irrelevant to future investment decisions.

✅ **Right**: Evaluate based on incremental economics from decision point

> If forward costs exceed expected returns, abandon regardless of past spend. 
> Don't throw good money after bad.

---

### #EP3: Technology for Technology's Sake

❌ **Wrong**: Deploying advanced technology without clear value proposition

> Example: Implementing AI/ML solutions without defined use cases or 
> measurable outcomes.

✅ **Right**: Technology must deliver returns or strategic advantage

> Every technology deployment must have clear business case, metrics, and 
> accountability. Drill faster, complete better, produce more per dollar.

---

### #EP4: Underestimating Capital Costs

❌ **Wrong**: Using optimistic cost estimates to get projects approved

> Example: Estimate $2B, actual $3B — destroys project economics and 
> damages credibility.

✅ **Right**: Conservative estimates with appropriate contingency

> Use Class 3 estimates (±15%) for FID. Include 20-30% contingency for 
> new technologies or complex projects. Document assumptions and risks.

---

### #EP5: Neglecting Stakeholder Management

❌ **Wrong**: Focusing only on technical execution, ignoring communities and regulators

> Example: Project delayed 2 years due to community opposition that 
> could have been addressed early.

✅ **Right**: Proactive stakeholder engagement from opportunity identification

> Build relationships with communities, regulators, partners from day one. 
> Social license to operate is as critical as technical execution.

---

### #EP6: Inadequate Risk Assessment

❌ **Wrong**: Focusing only on upside, ignoring downside scenarios

> Example: Project approved at $80/bbl oil price, fails at $50/bbl — 
> no stress testing performed.

✅ **Right**: Comprehensive risk analysis with mitigation planning

> Test projects at $40, $50, $65, $80/bbl scenarios. Identify killer risks 
> early. Have contingency plans for key uncertainties.

---

### #EP7: Poor Integration Planning

❌ **Wrong**: Treating acquisitions as financial transactions, ignoring operational integration

> Example: Acquisition closes but synergy capture fails due to cultural 
> clashes and systems incompatibility.

✅ **Right**: Integration planning begins before deal closes

> Pioneer example: Synergy target $3B+, detailed 100-day plan, retained 
> key talent, blended best practices. Integration is where value is created.

---

### #EP8: Short-Term Thinking

❌ **Wrong**: Optimizing for quarterly results at expense of long-term value

> Example: Cutting maintenance to hit quarterly targets, leading to 
> unplanned outages and higher costs later.

✅ **Right**: Decades-long perspective on asset management

> ExxonMobil thinks in 30-50 year horizons for field development. Maintain 
> assets properly, invest for the long term, create sustainable value.

---

## Best Practices

### BP1: Capital Efficiency Focus

```
Capital Efficiency Metrics:
├── Drilling:
│   ├── Days per 1,000 ft: Target continuous improvement
│   ├── Feet per day: Benchmark against best performers
│   └── Cost per foot: Optimize drilling parameters
│
├── Completions:
│   ├── Stages per day: Maximize fleet utilization
│   ├── Proppant per stage: Optimize design
│   └── Cost per stage: Procurement efficiency
│
└── Production:
    ├── Operating cost per BOE: <$8 target (Permian)
    ├── Uptime: >95% facility availability
    └── Artificial lift optimization: Maximize EUR
```

### BP2: Portfolio High-Grading

**Continuous Evaluation:**

| Asset Category | Action Criteria | Examples |
|----------------|-----------------|----------|
| **Advantaged** | Invest for growth | Permian, Guyana, LNG |
| **Core** | Maintain, optimize | Conventional base |
| **Declining** | Harvest, minimize investment | Mature assets |
| **Non-Core** | Divest | International conventional |

### BP3: Technology Deployment

**Prioritization Framework:**

1. **Must Have**: Safety, regulatory compliance, base operations
2. **Competitive Advantage**: Proprietary technology, scale benefits
3. **Efficiency Gains**: Cost reduction, productivity improvement
4. **Optionality**: Strategic flexibility, future opportunities

### BP4: Talent Development

**Engineering Career Progression:**

| Level | Years | Focus | Typical Role |
|-------|-------|-------|--------------|
| **Graduate** | 0-3 | Technical foundation | Engineer |
| **Professional** | 3-8 | Project experience | Senior Engineer |
| **Lead** | 8-15 | Team leadership | Team Lead |
| **Principal** | 15-25 | Technical authority | Principal Engineer |
| **Executive** | 25+ | Strategic leadership | VP/EVP |

---

## Checklists

### Pre-Investment Checklist

- [ ] Strategic fit with corporate priorities
- [ ] Returns exceed hurdle rate (IRR >10-15%)
- [ ] NPV positive at stress prices ($40-50/bbl)
- [ ] Technical risks identified and mitigated
- [ ] Environmental permits obtainable
- [ ] Social license achievable
- [ ] Execution team available and capable
- [ ] Financing secured or available
- [ ] Partner alignment (if applicable)
- [ ] Synergies quantified (for acquisitions)

### Operations Excellence Checklist

- [ ] Safety metrics meeting targets (TRIR <0.5)
- [ ] Environmental compliance maintained
- [ ] Production at or above forecast
- [ ] Operating costs within budget
- [ ] Facility uptime >95%
- [ ] Maintenance schedule on track
- [ ] Workforce trained and competent
- [ ] Regulatory reporting current
- [ ] Community relations positive
- [ ] Continuous improvement initiatives active

---

*Apply these standards and avoid these anti-patterns to achieve 
ExxonMobil-level engineering excellence.*
