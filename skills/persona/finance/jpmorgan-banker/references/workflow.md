# JPMorgan Banker — Execution Workflows

## §1 · M&A Transaction Workflow

### §1.1 Pre-Mandate Phase

**Weeks -4 to 0: Positioning**

| Activity | Owner | Deliverable |
|----------|-------|-------------|
| Market mapping | VP/Associate | Target/buyer universe |
| Relationship assessment | MD | Client priority ranking |
| Capability showcase | Team | Relevant case studies |
| Fee discussion | MD | Fee structure proposal |

**Decision Gate: Mandate Awarded?**
- Yes → Proceed to Execution
- No → Capture lessons, maintain relationship

### §1.2 Execution Phase — Sell-Side M&A

**Phase 1: Preparation (Weeks 1-4)**

| Week | Activity | Key Deliverable |
|------|----------|-----------------|
| 1 | Kickoff meeting | Project plan, workstream owners |
| 1-2 | Information gathering | Dataroom index, document request |
| 2-3 | Valuation | Trading comps, precedent transactions, DCF |
| 3-4 | Marketing materials | Teaser, Confidential Information Memorandum |
| 4 | Management presentation | Deck for buyer meetings |

**Phase 2: Marketing (Weeks 5-10)**

| Week | Activity | Key Deliverable |
|------|----------|-----------------|
| 5 | NDA distribution | Signed NDAs from potential buyers |
| 5-6 | Teaser distribution | 50-100 qualified buyers contacted |
| 6-7 | CIM distribution | Track buyer interest levels |
| 7-8 | First round bids | Indication of Interest (IOI) received |
| 8-9 | Buyer selection | 3-5 finalists selected |
| 9-10 | Management meetings | Site visits, management Q&A |

**Phase 3: Negotiation (Weeks 11-16)**

| Week | Activity | Key Deliverable |
|------|----------|-----------------|
| 11 | Final bids | Binding Letter of Intent (LOI) |
| 12 | Buyer selection | Signed LOI with exclusivity |
| 12-14 | Confirmatory diligence | Accounting, legal, business diligence |
| 14-15 | Definitive agreement | Purchase agreement negotiation |
| 15-16 | Board approval | Signed definitive agreement |
| 16+ | Closing | Funds transferred, deal closed |

### §1.3 Key Workstreams

**Valuation Workstream:**
```
1. Trading Comparables
   - Select 8-12 public peers
   - Calculate multiples: EV/Revenue, EV/EBITDA, P/E
   - Apply to target metrics
   
2. Precedent Transactions
   - Identify 10-15 comparable deals
   - Analyze control premiums
   - Calculate transaction multiples
   
3. Discounted Cash Flow
   - Build 5-year projection model
   - Determine WACC
   - Calculate terminal value
   - Sensitivity analysis on key assumptions
   
4. LBO Analysis (if financial buyer relevant)
   - Model sponsor returns
   - Determine maximum sponsor price
   - Assess strategic vs. financial buyer dynamics
```

**Marketing Workstream:**
```
1. Teaser (2 pages)
   - Company overview
   - Investment highlights
   - Financial summary
   - Contact information
   
2. Confidential Information Memorandum (50-100 pages)
   - Executive summary
   - Industry overview
   - Business overview
   - Financial performance
   - Growth opportunities
   - Risk factors
   
3. Management Presentation
   - 30-40 slides
   - Walk through business story
   - Q&A preparation
```

---

## §2 · IPO Execution Workflow

### §2.1 Pre-Filing Phase (Weeks -12 to -4)

| Activity | Timeline | Key Deliverable |
|----------|----------|-----------------|
| Underwriter selection | Week -12 | Signed engagement letters |
| Organizational meeting | Week -11 | Project timeline, workstreams |
| Accounting preparation | Weeks -11 to -8 | Audited financials, SOX readiness |
| S-1 drafting | Weeks -10 to -5 | Draft registration statement |
| Due diligence | Weeks -8 to -4 | Legal, accounting, business DD |

### §2.2 SEC Review Phase (Weeks -4 to +2)

| Activity | Timeline | Key Deliverable |
|----------|----------|-----------------|
| S-1 filing | Week -4 | Public/Confidential filing |
| SEC review | Weeks -4 to -1 | Comment letter |
| Response preparation | Weeks -3 to 0 | Amendment filings |
| Clearance | Week 0 | SEC declares effective |

### §2.3 Marketing Phase (Weeks 1-4)

| Activity | Timeline | Key Deliverable |
|----------|----------|-----------------|
| Research analyst education | Week 1 | Analyst day presentation |
| Roadshow preparation | Week 1 | Investor presentation, script |
| Roadshow execution | Weeks 2-3 | 10-12 cities, 80-100 meetings |
| Book building | Weeks 2-3 | Investor orders, demand curve |
| Pricing | Week 3 | Final offer price |
| Trading debut | Week 4 | First day of trading |

### §2.4 Post-IPO (Weeks 5-12)

| Activity | Timeline | Key Deliverable |
|----------|----------|-----------------|
| Stabilization | Weeks 5-8 | Support trading if needed |
| Research initiation | Week 6 | Analyst coverage begins |
| Lock-up expiration | Week 12 | Insider selling restrictions lift |

---

## §3 · Trading Strategy Development Workflow

### §3.1 Idea Generation

**Sources:**
1. Client order flow patterns
2. Research analyst recommendations
3. Macroeconomic data releases
4. Technical analysis signals
5. Cross-asset correlations

**Screening Criteria:**
| Criterion | Threshold | Rationale |
|-----------|-----------|-----------|
| Expected return | >200bps annualized | Worth risk allocation |
| Sharpe ratio | >1.0 | Risk-adjusted attractiveness |
| Liquidity | <$10M daily volume | Ability to exit |
| Correlation to existing positions | <0.7 | Diversification benefit |

### §3.2 Strategy Structuring

**Position Sizing:**
```
Position Size = (Portfolio VaR × Strategy Allocation) / Position VaR

Example:
- Portfolio VaR limit: $10M
- Strategy allocation: 20%
- Position VaR: $50K
- Position size = ($10M × 20%) / $50K = 40 positions max
```

**Hedging Decisions:**
| Hedge Type | Use Case | Cost |
|------------|----------|------|
| Delta hedge | Directional risk | Low (futures) |
| Gamma hedge | Convexity risk | Medium (options) |
| Credit hedge | Default risk | Medium (CDS) |
| Correlation hedge | Systematic risk | High (index options) |

### §3.3 Execution

**Order Types:**
| Type | Use Case | Best For |
|------|----------|----------|
| Market | Immediate execution | High liquidity, time-sensitive |
| Limit | Price improvement | Patient execution |
| TWAP | Minimize market impact | Large orders over time |
| VWAP | Track benchmark | Benchmark-sensitive execution |
| Iceberg | Hide order size | Large blocks |

### §3.4 Risk Monitoring

**Daily Monitoring:**
- P&L attribution
- Position VaR
- Scenario stress tests
- Liquidity metrics

**Weekly Review:**
- Strategy performance vs. benchmark
- Correlation changes
- Risk limit utilization
- Exception reporting

---

## §4 · Risk Management Workflow

### §4.1 Credit Risk Assessment

**New Loan Evaluation:**
```
1. Obligor Analysis
   - Financial statement analysis (3 years)
   - Industry and competitive position
   - Management assessment
   - Historical credit performance

2. Facility Structuring
   - Security/collateral analysis
   - Covenant package design
   - Pricing relative to risk

3. Approval Process
   - Credit officer recommendation
   - Risk rating assignment
   - Committee approval (if above authority limit)

4. Documentation
   - Legal review
   - Collateral perfection
   - Insurance verification
```

**Risk Rating Scale:**
| Rating | PD (1-year) | Description |
|--------|-------------|-------------|
| AAA | 0.01% | Virtually no risk |
| AA | 0.05% | Extremely low risk |
| A | 0.20% | Very low risk |
| BBB | 0.50% | Low risk |
| BB | 2.00% | Moderate risk |
| B | 5.00% | Elevated risk |
| CCC | 15.00% | High risk |
| CC | 30.00% | Very high risk |
| C | 50.00% | Near default |
| D | 100.00% | Default |

### §4.2 Market Risk Monitoring

**Daily Risk Report:**
| Metric | Limit | Current | Utilization |
|--------|-------|---------|-------------|
| Firm VaR | $100M | $85M | 85% |
| Trading VaR | $50M | $42M | 84% |
| Stress Loss (99%) | $500M | $420M | 84% |
| Largest Position | $1B | $850M | 85% |

**Weekly Stress Testing:**
- Historical scenarios (2008, 2020, 2023)
- Hypothetical scenarios
- Reverse stress tests
- Liquidity stress tests

### §4.3 Operational Risk Framework

**Risk Identification:**
- Event data collection
- Risk control self-assessments
- Key risk indicators
- Scenario analysis

**Capital Calculation:**
```
Operational Risk Capital = Business Indicator × Internal Loss Multiplier

Business Indicator = Interest, leases, dividends + Fees, commissions + Other income
```

---

## §5 · Regulatory Compliance Workflow

### §5.1 CCAR/DFAST Preparation

**Annual Timeline:**
| Month | Activity |
|-------|----------|
| January | Fed releases scenarios |
| February-March | Model updates, data preparation |
| April | Submission to Fed |
| May-June | Fed review, additional data requests |
| June | Results published |
| July-December | Response planning, capital actions |

**Key Components:**
1. Balance Sheet and RWA projections
2. Loss estimation models
3. Revenue and expense forecasting
4. Capital ratio projections
5. Capital action assumptions

### §5.2 Basel III Reporting

**Monthly Reports:**
- Capital ratios
- RWA by risk type
- Leverage ratios
- Liquidity metrics

**Quarterly Reports:**
- Pillar 3 disclosures
- G-SIB indicators
- Recovery plan updates

### §5.3 Regulatory Examination

**Pre-Examination:**
- Document preparation
- Staff briefing
- Issue log review

**During Examination:**
- Information requests
- Management interviews
- Sample testing

**Post-Examination:**
- Findings review
- Remediation planning
- Commitment letter response

---

*Last Updated: 2026-03-21*
