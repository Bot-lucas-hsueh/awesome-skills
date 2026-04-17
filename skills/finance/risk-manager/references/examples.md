## § 9 · Examples

### Example 1: VaR Calculation for Equity Portfolio

**Context:** $100M equity portfolio (S&P 500 constituents)

**User:** "Calculate 1-day 99% VaR for our equity portfolio."

**Risk Manager:**

> **VaR Analysis — Multi-Method Comparison:**
>
> | Method | Calculation | 99% VaR | Pros/Cons |
> |--------|-------------|---------|-----------|
> | **Parametric** | sigma = 1.2%, mu ~ 0 → VaR = 2.33 x 1.2% x $100M | $2.80M | Fast; assumes normality |
> | **Historical** | 99th percentile of 2-year daily returns | $3.15M | Captures actual tails |
> | **Monte Carlo** | 10,000 simulations with copula | $3.02M | Flexible; model risk |
>
> **Expected Shortfall (CVaR):**
> - Average loss beyond VaR threshold: $4.20M
> - ES/VaR ratio: 1.33x (indicates moderate tail risk)
>
> **Recommendation:** Use $3.2M as conservative VaR estimate; set limit at $5M

---

### Example 2: Credit Risk Model Development

**Context:** Commercial loan portfolio — $500M, 200 borrowers

**User:** "Build a PD model for our commercial loan portfolio."

**Risk Manager:**

> **PD Model Development Framework:**
>
> **Step 1: Data Preparation**
> - 5-year history: 200 borrowers, 12 defaults (6% observed PD)
> - Financial ratios: DSCR, leverage, current ratio, EBITDA margin
> - Qualitative: Industry, collateral, management quality
>
> **Step 2: Model Selection**
> | Approach | Method | Rationale |
> |----------|--------|-----------|
> | Statistical | Logistic regression | Interpretable, standard practice |
> | Alternative | Machine learning (XGBoost) | Higher accuracy, less interpretable |
>
> **Step 3: Logistic Regression Output**
> ```
> log(PD/(1-PD)) = -2.5 + 1.8x(Leverage) - 2.1x(DSCR) + 0.5x(Industry_Risk)
> ```
>
> **Step 4: Model Validation**
> - AUROC: 0.78 (acceptable discrimination)
> - Calibration test: p-value 0.23 (not significantly miscalibrated)
> - Backtest: Predicted vs. actual defaults within 10%
>
> **Step 5: Rating Buckets**
> | Rating | PD Range | Portfolio % |
> |--------|----------|-------------|
> | 1 (AAA) | 0-0.5% | 15% |
> | 2 (AA) | 0.5-1% | 25% |
> | 3 (A) | 1-2% | 30% |
> | 4 (BBB) | 2-5% | 20% |
> | 5 (BB) | 5-15% | 8% |
> | 6 (B) | >15% | 2% |

---

### Example 3: Stress Testing for CCAR

**Context:** Regional bank preparing for CCAR submission

**User:** "Design a stress test scenario for our commercial real estate exposure."

**Risk Manager:**

> **CCAR Stress Test — Commercial Real Estate:**
>
> **Scenario Parameters (Severely Adverse):**
> | Variable | Baseline | Stress | Change |
> |----------|----------|--------|--------|
> | GDP | +2.5% | -6.0% | -8.5% |
> | Unemployment | 4.0% | 10.0% | +6.0% |
> | CRE Prices | +3% | -35% | -38% |
> | Cap Rates | 6% | 9% | +300bps |
>
> **Transmission to Portfolio:**
> ```
> 1. Property Values: -35% → LTV increases from 65% to 100%
> 2. Debt Service: NOI falls 25%, DSCR < 1.0 for 40% of loans
> 3. Defaults: PD increases from 2% to 12%
> 4. Losses: LGD increases from 35% to 55%
> ```
>
> **Projected Losses:**
> - CRE portfolio: $2.0B
> - Expected loss under stress: $132M (6.6% of portfolio)
> - Pre-provision net revenue offset: $45M
> - Net impact to capital: -$87M
>
> **Capital Ratio Impact:**
> - Starting CET1: 12.0%
> - Post-stress minimum: 9.8%
> - Buffer above minimum: 4.3%
> - **Conclusion:** Bank remains well-capitalized under stress

---

### Example 4: Operational Risk Assessment (RCSA)

**Context:** Retail banking operations — payment processing unit

**User:** "Conduct an operational risk assessment for our payment processing function."

**Risk Manager:**

> **RCSA — Payment Processing Unit:**
>
> **Risk Identification:**
> | Risk Category | Specific Risk | Inherent Risk | Control Rating | Residual Risk |
> |--------------|---------------|---------------|----------------|---------------|
> | Process | Payment misdirection (wrong account) | High | Strong | Medium |
> | People | Insider fraud — unauthorized transfers | Medium | Moderate | Medium |
> | Systems | System downtime — batch failures | Medium | Strong | Low |
> | External | Cyber attack — fraudulent payments | High | Moderate | High |
>
> **Key Risk Indicators:**
> | KRI | Threshold | Current | Status |
> |-----|-----------|---------|--------|
> | Payment errors (ppm) | > 50 | 23 | Green |
> | System uptime | < 99.5% | 99.8% | Green |
> | Failed batches/month | > 2 | 1 | Green |
> | Security incidents | > 0 critical | 0 | Green |
>
> **Control Gaps:**
> 1. **Segregation of Duties:** Same operator can initiate and approve wires >$1M
>    - Recommendation: Dual approval for all wires >$100K
>
> 2. **Disaster Recovery:** DR site untested for 18 months
>    - Recommendation: Quarterly DR drills
>
> **Capital Calculation (Basel SMA):**
> - Business Indicator Component: $45M
> - Internal Loss Multiplier: 1.2
> - Operational Risk Capital: $54M

---

### Example 5: Liquidity Risk Analysis

**Context:** Corporate treasury managing funding risk

**User:** "Assess our liquidity position under a stress scenario."

**Risk Manager:**

> **Liquidity Risk Assessment:**
>
> **Current Position (LCR Components):**
> | Component | Amount ($M) | Factor | HQLA |
> |-----------|-------------|--------|------|
> | Level 1 Assets (Cash, Treasuries) | $500 | 100% | $500 |
> | Level 2A (Agency MBS) | $200 | 85% | $170 |
> | Level 2B (IG Corp Bonds) | $150 | 50% | $75 |
> | **Total HQLA** | | | **$745** |
>
> **Net Cash Outflows (30 days):**
> | Category | Amount ($M) | Run-off Rate | Outflow |
> |----------|-------------|--------------|---------|
> | Unsecured wholesale funding | $400 | 50% | $200 |
> | Operational deposits | $300 | 25% | $75 |
> | Secured funding (non-HQLA) | $250 | 100% | $250 |
> | **Total Outflows** | | | **$525** |
>
> **LCR Calculation:** $745M / $525M = **142%** PASS (above 100% minimum)
>
> **Stress Scenario (Rating downgrade to BB):**
> - Unsecured wholesale funding run-off: 50% → 100% = +$200M outflow
> - Collateral calls: +$150M
> - New LCR: 89% FAIL (below minimum)
>
> **Contingency Plan:**
> 1. Activate committed repo lines ($300M)
> 2. Sell Level 1 assets ($200M)
> 3. Reduce wholesale funding reliance

---
