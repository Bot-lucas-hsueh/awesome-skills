## 9. Scenario Examples

### Scenario 1: Valuing a Customer Dataset for an M&A Deal

**Context:** Private equity firm acquiring a B2C e-commerce company. Target claims their 50M customer behavioral dataset is worth $200M.

```
USER: We're acquiring DataRetail Co. They claim their 50M customer behavioral
      dataset is worth $200M. How do we validate this?

APPRAISER: That's a significant claim. Let me run this through the 5-gate
           framework before we touch a financial model.

GATE 1 -- EXCLUSIVITY:
First-party behavioral data (purchase history, browsing, preferences) from
50M customers. Assuming owned/operated collection -- this is genuinely first-
party. High exclusivity. Good start.

GATE 2 -- DQI (requires sampling):
Before accepting $200M, you need an independent DQI audit. Request access
to run Great Expectations against a 5% stratified sample (2.5M records).
Key dimensions to probe:
- Completeness: What % of customers have >3 behavioral events? Low behavioral
  depth = low predictive value
- Timeliness: What % of records were active in the past 12 months?
  Dormant customers are worth a fraction of active ones
- Accuracy: Email validation rate? Address verification rate?

Red flag to test: Many e-commerce datasets have 15-30% dormant/invalid
records that inflate apparent scale.

GATE 3 -- LEGAL OWNERSHIP:
Critical question: What does the privacy policy say about consent for data
use beyond fulfillment? Does it permit:
  - Sale/transfer to a buyer?
  - New processing purposes (e.g., if you are in financial services)?
If customers consented to "improving our services" only, you have a GDPR/
CCPA purpose limitation problem.

GATE 4 -- MONETIZATION PATHWAY:
How is this $200M being justified? If it is based on:
  - Current licensing revenue: ask for audited contracts (income approach)
  - "Potential" licensing: discount heavily (speculative)
  - Internal decision value: requires incremental revenue attribution model

GATE 5 -- REGULATORY TRANSFERABILITY:
GDPR/CCPA. You need answers:
  - What % of customers are EU residents? (GDPR Article 4 -- controller change
    in M&A may require fresh consent or Article 6 legitimate interest analysis)
  - US CCPA: Are customers opted out of "sale"? California defines "sale" to
    include M&A data transfers in some contexts.

PRELIMINARY ASSESSMENT:
Their $200M claim likely uses income approach on projected licensing revenue
without DQI or regulatory discounts. Recommended approach:

Income Approach (30% weight): DCF on actual contracted licensing revenue
  only. Speculative pipeline: 50% discount. Estimate: $40-80M range.

Cost Approach (40% weight): Replacement cost to collect 50M behavioral
  profiles. Industry benchmark: $2-8 per quality behavioral profile.
  50M x $5 midpoint x quality factor (DQI-adjusted) = $180M pre-discount.
  Apply 30% freshness/regulatory discount: ~$120M.

Market Approach (30% weight): Comparable e-commerce behavioral data
  acquisitions (Acxiom, LiveRamp comparable transactions): $1-6 per active
  customer profile. 50M x estimated 60% active x $3.50 = $105M.

TRIANGULATED ESTIMATE: P50 = $90-120M range. Their $200M claim appears
20-100% inflated. Recommend $25-30M holdback pending DQI audit results
and GDPR counsel sign-off.

NEXT STEPS:
1. Commission independent DQI audit (2 weeks)
2. Request GDPR/CCPA legal opinion from EU counsel
3. Obtain 3 years of audited data licensing revenue (if any)
4. Renegotiate purchase price or structure earnout tied to DQI >= 80
   and monetization revenue milestones
```

### Scenario 2: Assessing Data Product Marketability

**Context:** Enterprise SaaS company with rich B2B firmographic data wants to list on Snowflake Marketplace.

```
USER: We have 8M B2B company profiles with firmographics, technographic
      install data, and intent signals. Can we list on Snowflake Marketplace?
      What is a realistic revenue estimate?

APPRAISER: Strong asset class -- B2B firmographic + technographic + intent
           is the premium tier of the data market. Let me assess this properly.

DQI QUICK SCAN (run before listing):
B2B data has specific quality thresholds Snowflake buyers expect:
- Completeness: Revenue, employee count, industry (SIC/NAICS) -- need >=90%
  fill rate on core firmographics
- Timeliness: Company records need <180 days since last verification for
  tech install data (companies change stacks frequently)
- Uniqueness: D-U-N-S
  15-25% duplicate parent/subsidiary overlaps
- Accuracy: LinkedIn cross-validation rate for employee count accuracy

Estimated DQI target: >= 82 to compete with Bombora, ZoomInfo, Clearbit tier.

REGULATORY CHECK:
B2B data is generally lower GDPR risk than B2C (legitimate interest basis
is stronger for B2B processing). However:
- Intent signal data sourced from B2C web traffic: GDPR applies to
  individual cookie/IP level signals even in B2B context
- EU companies in dataset: Ensure processing basis documented
- CCPA: B2B data has partial exemption but monitor CPRA developments

MONETIZATION PATHWAY ASSESSMENT:
Snowflake Marketplace is appropriate. Pricing benchmark for this tier:

  Tier     | Records | Price/Enrichment | Monthly ARR Target
  ---------|---------|-----------------|-------------------
  Sample   | 100K    | Free            | Lead gen
  Starter  | 500K    | $0.15-0.25/rec  | $75K-125K
  Growth   | 2M      | $0.10-0.18/rec  | $200K-360K
  Enterprise | 8M+   | $0.06-0.12/rec + intent | $480K-960K

  Intent signal data commands 3-5x premium over base firmographics.
  Technographic installs: 2-3x premium over base.

REALISTIC YEAR-1 ESTIMATE:
  Conservative: $300K ARR (sample + starter tier adoption)
  Base case:    $650K ARR (growth tier traction, 2 enterprise contracts)
  Optimistic:   $1.2M ARR (category leadership, 5 enterprise contracts)

  3-year income approach NPV at 12% discount: $1.4M - $4.8M range.
  This asset is worth productizing -- proceed with listing.

ACTION PLAN:
1. Run DQI audit targeting >= 82 (Informatica or Talend)
2. Build Snowflake Clean Room data sample for buyer evaluation
3. Develop tiered pricing structure with usage metering via Snowflake
4. Register on AWS Data Exchange simultaneously (2x distribution)
5. File GDPR processing basis documentation for EU records
```

### Scenario 3: GDPR Impact Assessment on Data Asset Portfolio Value

**Context:** German analytics firm assessing their data portfolio value after GDPR enforcement action.

```
USER: We received a EU 2M GDPR fine and the DPA is requiring us to delete
      consumer behavioral profiles for 12M EU residents. How does this
      affect our data asset portfolio valuation?

APPRAISER: This is exactly the regulatory encumbrance scenario that most
           data asset valuations fail to anticipate. Let me model this.

IMPACT ANALYSIS:

1. DIRECT ASSET IMPAIRMENT:
   12M EU resident profiles deleted: immediate reduction in dataset scope.
   If these represented a material % of total dataset:
   - Assess what % of monetization revenue was EU-origin data
   - Delete impact is permanent -- not a temporary impairment
   - Trigger IAS 36

2. GDPR PURPOSE LIMITATION REASSESSMENT:
   The enforcement action signals your consent basis was defective.
   This creates retroactive risk on remaining non-EU data if collected
   under similar consent language (class action risk in US states).
   Run consent basis audit on all remaining records before revaluing.

3. REVISED VALUATION MODEL:
   Pre-enforcement portfolio income approach: $45M
   (revenue from behavioral targeting clients)

   Adjustment factors:
   +-- EU dataset deletion: -12M records (-18% of 66M total)
   +-- Revenue impact: -25% (EU clients had premium CPM rates)
   +-- Regulatory risk premium: +3% discount rate applied
   +-- Remaining consent basis uncertainty: -15% haircut
   +-- Remediation

   Post-enforcement income approach: $28-32M (38-42% reduction)
   Cost approach (unaffected by regulatory action): $22M
   Market approach: Comparable assets post-enforcement: 30-40% discount
                   vs pre-enforcement comps

   REVISED TRIANGULATED VALUE: $22-28M (vs estimated pre-enforcement $42-48M)
   IMPAIRMENT TO RECOGNIZE: ~$18-22M write-down recommended

4. REMEDIATION ROADMAP:
   - Migrate to first-party contextual signals (non-personal, GDPR exempt)
   - Invest in consent management platform (OneTrust
   - Develop privacy-by-design data collection for EU markets
   - Timeline to value recovery: 18-24 months with consent-based rebuild
```

### Scenario 4 (Anti-Pattern): Valuing Data by Volume Alone

```
USER: We have 500TB of customer data. That's worth at least $50M, right?
      Just based on storage costs and volume alone.

APPRAISER: I need to stop you there -- this is the most common and most
           costly mistake in data asset valuation. Volume is not value.

HERE'S WHY THIS REASONING FAILS:

500TB of data could be worth:
  $0       -- if it is all duplicate records, system logs, or junk
  $500K    -- if it is moderate-quality, regulated, commodity data
  $500M    -- if it is exclusive, high-DQI behavioral data with clear
              monetization pathways

THE VOLUME FALLACY IN PRACTICE:
- A data broker collapsed in 2019 with 2 PB of "valuable" data that turned
  out to be 85% duplicates with DQI of 42. Sold for $800K.
- 1M records of exclusive, verified, consented financial behavior data
  routinely sells for $50-500M in licensing deals.
- 100GB of exclusive clinical trial data with proper IRB consent and
  HIPAA de-identification is worth more than 500TB of retail logs.

THE CORRECT APPROACH:
Before any volume-based estimate:
  Step 1: Sample 5% -- compute DQI (DAMA-DMBOK 6 dimensions)
  Step 2: Assess exclusivity (1st/2nd/3rd party? Scraped?)
  Step 3: Regulatory encumbrance analysis
  Step 4: Identify monetization pathway (no pathway = cost floor only)
  Step 5: Then and only then apply a financial model

Your 500TB:
  - What is the DQI? (Unknown = assume 50 until proven otherwise)
  - What % is personal data? (GDPR/CCPA exposure)
  - What is the freshness profile? (Data older than 18 months decays rapidly)
  - Any existing licensing revenue? (Validates income approach)

CORRECT STARTING POINT: Commission a DQI audit. Until then, the defensible
value is replacement cost only -- likely $0.50-5 per GB of usable, quality-
adjusted data. At DQI 50, apply 40% quality discount. Realistic floor: $50-
125M replacement cost before regulatory haircuts. Do not quote $50M without
completing all 5 gates.
```

---
