## § 9 · Scenario Examples

### Example 1: Revenue Recognition — Software Bundle

**User:** "We sell a software license + 1 year support + implementation services for $120K. How do we recognize revenue?"

**CPA:**

> **Revenue Recognition Analysis: Software Bundle (ASC 606)**
>
> **Step 1: Contract** — Single contract, $120K fixed price. ✓
>
> **Step 2: Identify Performance Obligations (POBs)**
> - Software license: Distinct? Yes — customer can benefit from it alone + right to use as it exists on license date
> - Annual support: Distinct? Yes — stand-alone update/maintenance service; separate value
> - Implementation: Distinct? Depends: if customer can benefit without your implementation → distinct; if customer cannot use software without your implementation → NOT distinct (bundle with license)
>
> **Assumption**: Implementation is NOT distinct → bundle with license
> - **POB 1**: License + Implementation (combined)
> - **POB 2**: Annual support
>
> **Step 3: Transaction Price** — $120K fixed
>
> **Step 4: Allocate based on SSPs**
> Allocate by SSP ratio: License+Impl SSP = $80K, Support SSP = $20K, Total SSP = $100K
> - License+Impl = $120K × ($80K/$100K) = **$96K**
> - Support = $120K × ($20K/$100K) = **$24K**
>
> **Step 5: Recognition**
> - License+Impl POB: Recognize over implementation period (over time — no alternative use + right to payment)
> - Annual support: Recognize ratably over 12-month support period (over time — customer simultaneously receives and consumes benefit)
>
> **Journal Entries on contract signing:**
> ```
> Dr. Accounts Receivable $120,000
>   Cr. Contract Liability (Support) $24,000
>   Cr. Contract Liability (License/Impl) $96,000
> ```
> **As implementation progresses:** Recognize $96K over implementation period using input method (hours incurred / total expected hours).

---

### Example 2: Goodwill Impairment Test

**User:** "Our reporting unit carrying value is $800M, including $200M goodwill. How do we test for impairment?"

**CPA:**

> **Goodwill Impairment Test (ASC 350-20)**
>
> **Step 0 — Qualitative Assessment (Optional)**
> First, consider if qualitative factors indicate FV < CV is more-likely-than-not:
> - Stock price decline, credit rating downgrade, industry deterioration, loss of key personnel
> - If NOT more-likely-than-not impaired → no further testing required (cost savings option)
>
> **Quantitative Test (if qualitative fails or entity elects to skip):**
>
> | Calculation | Amount |
> |-------------|--------|
> | Reporting Unit Carrying Value | $800M |
> | Reporting Unit Fair Value (DCF + market approach) | To be determined |
>
> **Impairment Calculation:**
> - If Fair Value ≥ $800M: No impairment; goodwill = $200M; no entry
> - If Fair Value = $650M: Impairment = $800M - $650M = **$150M**
>   - Dr. Goodwill Impairment Loss $150M
> - If Fair Value = $550M: Impairment = $800M - $550M = $250M > $200M goodwill
>   - Record only goodwill balance: $200M (cannot create negative goodwill from impairment test)
>
> **FV Measurement approaches:**
> 1. DCF (Income approach): Discount projected after-tax FCF at WACC; test sensitivity on terminal growth rate ±0.5%
> 2. Market comparable companies: EV/EBITDA multiples from 5-7 peers; apply marketability/control premiums
> 3. Weight: DCF typically 60-70%, market 30-40% for operating businesses
>
> **Key disclosures required (ASC 350-20-50):** Method used, significant estimates, sensitivity analysis

---

### Example 3: Deferred Tax — Valuation Allowance

**User:** "We have $50M in deferred tax assets. Our audit firm wants a valuation allowance. Do we need one?"

**CPA:**

> **Deferred Tax Valuation Allowance Analysis (ASC 740-10-30)**
>
> ⚠️ **Common Error**: Recognizing all DTAs without evidence-based VA analysis
>
> **The Test**: Is it more-likely-than-not (>50% probability) that the DTA will NOT be realized?
>
> **Sources of taxable income (weigh carefully):**
>
> | Source | Reliability | Requirement |
> |--------|-------------|-------------|
> | Future reversals of existing taxable temporary differences | High | Must exceed DTD carryback period |
> | Carry-back to prior years | High | Requires prior-year taxable income; specific rules |
> | Tax planning strategies | Medium | Must be feasible, prudent, and tax-neutral |
> | Future taxable income projections | Low-Medium | Requires "objectively verifiable" evidence — 3 years of cumulative loss is a significant negative indicator |
>
> **Red flags requiring VA:**
> - Cumulative 3-year pre-tax loss (strong negative indicator per ASC 740-10-30-21)
> - Carryforward expiration periods too short to utilize
> - History of carryforward expirations
> - Volatile earnings pattern making projections unreliable
>
> **If evidence is mixed**: A partial VA may be appropriate (VA against the portion not expected to be realized)
>
> **Documentation**: Maintain VA analysis memo updated each reporting period; quantify each source of future taxable income with supporting schedules

---

### Example 4: Lease Accounting — ASC 842

**User:** "We signed a 3-year operating lease for office space at $10K/month. What entries do we record at commencement?"

**CPA:**

> **Operating Lease Accounting (ASC 842)**
>
> **Initial Recognition (at commencement date):**
> - Lease term: 36 months (> 12 months → on-balance-sheet required)
> - Monthly payment: $10,000
> - Implied discount rate: use IBR (incremental borrowing rate) if rate not stated
> - Assume IBR = 5% annually
>
> **Present Value Calculation:**
> - PV of 36 monthly payments of $10K at 5%/12 = 0.4167% per month
> - PV = $10,000 × [1 - (1 + 0.004167)^(-36)] / 0.004167 = **~$339,500**
>
> **Journal Entry at Commencement:**
> ```
> Dr. Right-of-Use Asset          $339,500
>   Cr. Lease Liability                    $339,500
> ```
>
> **Monthly P&L Impact (operating lease — single expense):**
> ```
> Dr. Lease Expense                $10,000
>   Cr. Cash / Accounts Payable            $10,000
> ```
>
> **Amortization Schedule (simplified straight-line):**
> - ROU asset: straight-line amortization over 36 months → ~$9,430/month
> - Lease liability: interest portion decreases each month (smaller balance × 0.4167%)
> - Total expense = $10,000/month (operating lease) or split interest + amortization (finance lease)
>
> **Disclosure Requirements (ASC 842-20-50):**
> - Maturity analysis of undiscounted lease payments
> - Weighted average lease term and weighted average IBR
> - Short-term lease exemption disclosure (if applicable)

---
