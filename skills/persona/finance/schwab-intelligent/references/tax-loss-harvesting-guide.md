# Tax-Loss Harvesting (TLH) Deep Dive

> **Comprehensive guide to understanding and optimizing TLH with Schwab Intelligent Portfolios**

---

## What is Tax-Loss Harvesting?

Tax-loss harvesting is a strategy that sells investments at a loss to offset capital gains taxes, potentially reducing your tax bill. The "harvested" losses can:

1. Offset capital gains from other investments (dollar-for-dollar)
2. Offset up to $3,000 of ordinary income per year if losses exceed gains
3. Carry forward indefinitely to future tax years

---

## How Schwab's TLH Works

### Automated Process
```
Daily Monitoring → Loss Identification → Sale Execution → 
Replacement Purchase → Loss Reporting → Tax Form Generation
```

1. **Algorithm Scanning:** Daily review of all holdings for unrealized losses
2. **Threshold Check:** Identifies positions with sufficient losses to harvest
3. **Wash Sale Avoidance:** Sells losing ETF, buys alternate ETF in same asset class
4. **Rebalancing Integration:** Coordinates with portfolio rebalancing needs
5. **Tax Reporting:** Reports losses on Form 1099-B

### Example TLH Transaction

| Step | Action | Result |
|------|--------|--------|
| 1 | Own 100 shares SCHB (US Broad Market) at $50 = $5,000 basis | Current value: $4,500 |
| 2 | SCHB declines to $45/share | Unrealized loss: $500 |
| 3 | Algorithm triggers TLH | Sell 100 shares SCHB at $4,500 |
| 4 | Immediate purchase | Buy 100 shares SPTM (similar US market ETF) at $4,500 |
| 5 | Tax result | $500 realized loss, portfolio exposure maintained |

---

## Eligibility Requirements

### Account Requirements
- ✅ Taxable accounts only (individual, joint)
- ✅ Minimum $50,000 account balance
- ✅ Must opt-in to TLH feature

### Ineligible Accounts
- ❌ IRAs (Traditional, Roth, Rollover)
- ❌ 401(k) or other employer plans
- ❌ 529 plans
- ❌ Custodial accounts (if under $50k)

---

## Tax Benefits Analysis

### Short-Term vs Long-Term Losses

| Type | Holding Period | Offset Priority | Tax Rate |
|------|---------------|-----------------|----------|
| Short-term | < 1 year | First offset short-term gains | Ordinary income rates (up to 37%) |
| Long-term | > 1 year | Then offset long-term gains | Capital gains rates (0%, 15%, 20%) |

### Tax Savings Example

**Scenario:** $100,000 account, harvested $8,000 in losses

| Tax Situation | Savings Calculation | Estimated Benefit |
|--------------|---------------------|-------------------|
| Offset $5,000 short-term gains | $5,000 × 32% bracket | $1,600 |
| Offset $3,000 ordinary income | $3,000 × 32% bracket | $960 |
| **Total Year 1 Benefit** | | **$2,560** |
| Remaining $5,000 loss carryforward | Future offset potential | $750-1,600 |

### Schwab's Published Effectiveness

According to Schwab data from volatile markets:

| Account Type | Harvested Losses (9 months) |
|--------------|----------------------------|
| $100,000 Moderate Growth | $18,000 |
| September 2022 alone | $4,548 |

---

## Wash Sale Rules & Avoidance

### What is a Wash Sale?
The IRS wash sale rule disallows a loss deduction if you buy a "substantially identical" security within 30 days before or after the sale.

### Schwab's Avoidance Strategy
Schwab uses alternate ETFs that track similar but not identical indexes:

| Original ETF (Sold) | Asset Class | Replacement ETF (Bought) |
|--------------------|-------------|-------------------------|
| SCHB (Schwab US Broad Market) | US Large/Mid/Small | SPTM (SPDR Portfolio Total Stock Market) |
| SCHX (US Large-Cap) | US Large Cap | VV (Vanguard Large-Cap) |
| SCHF (International Equity) | Developed Markets | VEA (Vanguard Developed Markets) |
| SCHZ (US Aggregate Bond) | US Bonds | BND (Vanguard Total Bond Market) |

### External Wash Sale Risk
**Critical Limitation:** Schwab's algorithm only monitors Schwab Intelligent Portfolios accounts. It cannot detect:

- Spouse's 401(k) purchases of similar funds
- Your IRA purchases at another brokerage
- Your spouse's IRA trades
- Employer stock purchase plans

**Example Problem:**
- You sell SCHB at a loss in Intelligent Portfolios (harvested)
- Your spouse buys S&P 500 index fund in their 401(k) same day
- IRS may disallow the loss under wash sale rules

**Mitigation:**
- Coordinate with spouse on index fund purchases
- Review all household investment activity
- Consider timing of 401(k) contributions

---

## TLH vs Manual Loss Harvesting

| Factor | Automated (Schwab) | Manual (DIY) |
|--------|-------------------|--------------|
| Monitoring frequency | Daily | When you remember |
| Emotion elimination | Yes | No |
| Wash sale avoidance | Algorithmic | Your responsibility |
| Optimal timing | Systematic execution | Often delayed |
| Time commitment | None | Significant |
| Cost | Included ($0) | Your time + potential mistakes |

---

## When TLH is Most Valuable

### High-Value Scenarios
1. **High-income years:** Offsetting gains during peak earning years
2. **Portfolio transitions:** Converting appreciated assets, rebalancing large accounts
3. **Volatile markets:** 2020, 2022-type markets create harvesting opportunities
4. **Tax bracket management:** Harvesting to stay below IRMAA or NIIT thresholds
5. **Retirement preparation:** Building loss carryforwards before RMDs begin

### Lower-Value Scenarios
1. **Tax-advantaged accounts:** IRAs, 401(k)s don't benefit from TLH
2. **Buy-and-hold investors:** Minimal gains to offset
3. **Low-income years:** Already in 0% capital gains bracket
4. **Small accounts:** Below $50,000 minimum threshold

---

## Integration with Tax Planning

### Annual Tax Planning Checklist

**January-February:**
- [ ] Review 1099-B from Schwab (includes TLH activity)
- [ ] Calculate net capital gains/losses
- [ ] Determine if additional harvesting needed before year-end

**March-April (Tax Season):**
- [ ] Report harvested losses on Schedule D
- [ ] Verify wash sale adjustments
- [ ] Apply losses to gains and up to $3,000 income

**September-December:**
- [ ] Review unrealized gains/losses across all accounts
- [ ] Consider tax-gain harvesting if in 0% bracket
- [ ] Time charitable giving with appreciated securities

---

## Common TLH Mistakes

### 1. Not Opting In
Many eligible investors never enable TLH. **Action:** Log in and opt-in if you have $50k+ in taxable accounts.

### 2. Ignoring External Accounts
Forgetting spouse's retirement accounts or external brokerages can trigger accidental wash sales.

### 3. Over-Focusing on Losses
TLH is valuable but secondary to proper asset allocation and long-term investing.

### 4. Not Using Losses Strategically
Losses can be carried forward. Don't waste them offsetting 0% capital gains in low-income years.

---

## TLH and Premium CFP Access

For Premium clients, CFPs can help with:

- **Loss harvesting coordination** across household accounts
- **Tax bracket optimization** timing of harvesting vs. Roth conversions
- **Charitable strategies** combining TLH with donor-advised funds
- **Retirement distribution planning** using accumulated losses

---

*Disclaimer: This guide is for educational purposes. Consult a tax professional for advice specific to your situation. Tax laws change; verify current regulations.*
