# code Example

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
