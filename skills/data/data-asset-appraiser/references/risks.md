## § 3 · Risk Disclaimer

> This skill provides analytical frameworks and valuation methodologies. Data asset valuations are inherently uncertain and subject to legal, regulatory, and market risks. All valuations should be reviewed by qualified legal counsel and a licensed appraiser before use in M&A transactions, financial statements, or litigation.

| # | Risk | Severity | Mitigation |
|---|------|----------|------------|
| 1 | **Legal Disputes Over Data Ownership** (scraped, licensed, or user-generated data with ambiguous IP rights — e.g., X/Twitter ToS litigation, LinkedIn v. hiQ) | HIGH | Require chain-of-title documentation; recommend IP escrow in M&A; flag UGC and scraped data for legal review before assigning income approach value |
| 2 | **GDPR Non-Transferability in M&A** (personal data assets may require fresh consent or become non-transferable to a buyer in a different jurisdiction or with a different processing purpose) | HIGH | Conduct regulatory encumbrance analysis before financial modeling; apply GDPR transferability discount (0-100%) to personal data asset values; involve EU counsel |
| 3 | **Data Quality Inflation in Seller Representations** (sellers routinely overstate DQI or completeness rates; buyer due diligence rarely samples sufficiently) | HIGH | Independently validate DQI using Great Expectations or Monte Carlo against a stratified random sample (min 5% of records); include quality rep & warranty in purchase agreement |
| 4 | **Privacy Law Changes Devaluing Data Assets Retroactively** (e.g., CPRA expanding opt-out rights, state ADPPA enactment reducing addressable data pools) | MEDIUM | Apply regulatory risk discount (5-20%) to consumer behavioral data assets; model value degradation scenarios under expanded opt-out adoption |
| 5 | **Data Monopoly / Antitrust Regulatory Risk** (FTC/DOJ scrutiny of data-driven acquisitions — e.g., Facebook/Instagram/WhatsApp data network effect concerns) | MEDIUM | Flag when acquired data creates dominant market position; note antitrust risk in valuation; recommend regulatory counsel review for deals with data component >$100M |
| 6 | **Over-Valuation Leading to M&A Write-Downs** (goodwill impairment from overpriced data assets, especially in adtech and data broker acquisitions) | HIGH | Apply IAS 36 impairment testing framework; set performance milestones tied to data monetization revenue before full value recognition; use earnout structures |
| 7 | **Underestimating Data Maintenance and Freshness Costs** (data assets depreciate rapidly without ongoing collection, cleansing, and enrichment; freshness half-life varies by data type) | MEDIUM | Model ongoing data maintenance opex (typically 15-30% of initial collection cost per year); include freshness decay curve in income approach DCF assumptions |

---
