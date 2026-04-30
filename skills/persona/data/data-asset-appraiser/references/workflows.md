## 8. Standard Workflow

### Phase 1: Data Asset Due Diligence (M&A Context)

```
PHASE 1: DATA ASSET DUE DILIGENCE
==================================

STEP 1.1 -- Data Asset Discovery & Inventory
  Actions:
  - Extract metadata from Collibra / Alation
  - Classify assets: transactional, behavioral, reference, derived/enriched
  - Document source provenance, collection mechanism, retention schedule
  - Identify top-20 data assets by estimated strategic value (Pareto focus)

  [DONE]: Structured data asset register with ownership, provenance, and
          classification for all material assets (>$1M estimated value)
  [FAIL]: Missing lineage for >25% of assets -- escalate to DataHub
          reconstruction; flag in rep & warranty; recommend holdback

STEP 1.2 -- Regulatory Encumbrance Analysis
  Actions:
  - Map each asset to applicable regulations (GDPR, CCPA/CPRA, PIPL, HIPAA, FCRA)
  - Assess cross-border transfer feasibility (SCCs, BCRs, adequacy decisions)
  - Identify assets with purpose-limitation conflicts in buyer use case
  - Quantify transferable scope (% of records legally transferable to buyer)

  [DONE]: Regulatory encumbrance matrix; per-asset transferability score (0-100%)
  [FAIL]: Any asset >$10M estimated value with unclear GDPR consent basis
          -- do not proceed to financial modeling; require legal opinion

STEP 1.3 -- Data Quality Scoring (DQI)
  Actions:
  - Deploy Great Expectations or Informatica IDQ against stratified sample (>=5%)
  - Score 6 DAMA-DMBOK dimensions per asset class
  - Weight dimensions by asset type (e.g., timeliness critical for behavioral;
    accuracy critical for financial data)
  - Document DQI per asset with confidence interval

  [DONE]: Auditable DQI report per asset; quality-adjusted valuation basis confirmed
  [FAIL]: DQI < 60 on any material asset -- apply speculative value designation;
          require seller remediation plan or price adjustment

STEP 1.4 -- Three-Approach Valuation
  Actions:
  - Income Approach: DCF on contractual data licensing revenue; project 5-year
    monetization scenarios; apply quality and regulatory discounts; WACC 10-15%
  - Cost Approach: Estimate replacement cost (data collection, cleansing,
    enrichment, infrastructure); model freshness depreciation at 15-30%/year
  - Market Approach: Identify 3-5 comparable data transactions (Snowflake
    Marketplace listings, disclosed data acquisitions); apply size/quality adjustments
  - Triangulate: weight approaches by monetization maturity and data type

  [DONE]: P10/P50/P90 value range per asset; reconciled triangulated estimate
  [FAIL]: Spread between income and cost approach >300% -- revisit assumptions;
          do not publish single-point estimate; disclose range with caveats
```

### Phase 2: Data Monetization Roadmap

```
PHASE 2: DATA MONETIZATION ROADMAP
=====================================

STEP 2.1 -- Monetization Pathway Assessment
  Actions:
  - Score each high-value asset against 4 pathways:
    (A) Direct licensing to 2nd-party buyers
    (B) Data product development (APIs, dashboards, feeds)
    (C) Marketplace listing (Snowflake Marketplace, AWS Data Exchange)
    (D) Internal decision uplift (quantify as cost savings
  - Apply regulatory feasibility filter (eliminate non-transferable assets)
  - Estimate time-to-revenue and investment required per pathway

  [DONE]: Prioritized monetization roadmap (top 5 assets x 1-2 pathways each)
          with 12-month revenue projection and 3-year ARR target
  [FAIL]: No pathway achieves positive NPV within 3 years -- recommend cost
          approach valuation only; flag for internal capital reallocation

STEP 2.2 -- Data Product Specification & Pricing
  Actions:
  - Define data product schema, delivery mechanism, refresh cadence, SLA
  - Benchmark pricing against Snowflake Marketplace and AWS Data Exchange
  - Model tier pricing (sample, standard, enterprise) with usage-based options
  - Estimate customer acquisition cost and churn for data subscription products

  [DONE]: Data product spec sheet; pricing model; year-1 revenue forecast
  [FAIL]: No comparable market pricing found -- require primary market research
          before income approach monetization value can be established
```

---
