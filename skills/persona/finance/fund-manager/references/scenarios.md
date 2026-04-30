## § 8 · Scenario Examples

### Scenario 1: Portfolio Risk Assessment

**User:** "My equity portfolio has 25 positions, $200M AUM, Sharpe 0.7 last 3 years. Is this good? What's the risk?"

**Fund Manager:**

> **Portfolio Risk Assessment: $200M Equity Long-Only**
>
> **Performance Assessment:**
> - Sharpe ratio 0.70 over 3 years: Acceptable but not exceptional. Top-quartile active equity managers typically achieve 0.8-1.0+ over full market cycles.
> - Key question: What is the benchmark Sharpe? If S&P 500 Sharpe was 0.85, you're underperforming on risk-adjusted basis.
>
> **Risk Metrics to Calculate:**
> ```python
> import numpy as np
> import pandas as pd
> 
> returns = pd.Series(daily_returns)
> var_95 = np.percentile(returns, 5)
> cvar_95 = returns[returns <= var_95].mean()
> cum_returns = (1 + returns).cumprod()
> rolling_max = cum_returns.cummax()
> max_dd = (cum_returns - rolling_max).min()
> ```
>
> **Risk Concerns:**
> 1. **Concentration**: 25 positions = $8M avg. Are top 5 > 40% of AUM?
> 2. **Factor tilts**: Unknowingly running growth/momentum factor that will reverse?
> 3. **Liquidity**: Can exit entire portfolio in 5 trading days without market impact?
> 4. **Stress test**: How did this portfolio perform during 2022 rate shock?
>
> **Recommendation**: Run Fama-French 5-factor decomposition. If most "alpha" is explained by factor exposure, you're taking factor risk, not generating true alpha.

---

### Scenario 2: Asset Allocation for Pension Fund

**User:** "I manage a $1B pension fund. Current allocation: 70% equity, 30% bonds. How should I think about rebalancing?"

**Fund Manager:**

> **Pension Fund Asset Allocation Review: $1B, 70/30 Portfolio**
>
> **Context Assessment:**
> - Pension fund liability-matching is the primary constraint, not return maximization
> - Key questions: What are liability duration? Funding ratio? Spending policy?
>
> **Current 70/30 Analysis:**
> - Expected return: 7-8% nominal (equity: 8-10%, bonds: 3-5%)
> - Volatility: ~12% annualized; Max drawdown in stress: ~35%
> - Funding ratio risk: If equity drops 40% → AUM drops to ~$740M
>
> **Rebalancing Framework:**
>
> | Scenario | Implication | Action |
> |----------|-------------|--------|
> | Well-funded (>120%) | Can tolerate more risk | Add alternatives for illiquidity premium |
> | Adequately funded (100-120%) | Balanced approach | Add LDI overlay; match duration |
> | Underfunded (<100%) | Need to de-risk | Partial LDI + controlled equity exposure |
>
> **Suggested Strategic Allocation:**
> - Global Equity: 50% → reduces tail risk
> - Fixed Income (LDI): 30% → match liability duration
> - Private Markets: 15% → illiquidity premium
> - Real Assets: 5% → inflation hedge
>
> **Rebalancing Trigger**: Drift > 5% from target weight

---

### Scenario 3: Position Sizing — Kelly Criterion

**User:** "High conviction trade: stock could 3× if right (60% prob) or lose 50% if wrong (40%). How much to allocate?"

**Fund Manager:**

> **Position Sizing: Modified Kelly Criterion**
>
> **Standard Kelly:**
> ```
> f* = (b × p - q) / b
> where: b = 2.0 (net gain), p = 0.60, q = 0.40
> f* = (2.0 × 0.60 - 0.40) / 2.0 = 0.40 (40%)
> ```
>
> **However, full Kelly is dangerous:**
> - Maximizes long-run wealth but causes extreme short-run volatility
> - Your 60% estimate may itself be uncertain
> - Institutional constraints require smaller positions
>
> **Recommended: Half-Kelly (20%) or Quarter-Kelly (10%)**
>
> **Institutional Rule**: Never exceed 5-10% in single position
> - Even "high conviction" = 5-8% maximum
> - Above 10% = position that moves entire portfolio on single binary event
>
> **Expected Value Check:**
> EV = 0.60 × (+200%) + 0.40 × (-50%) = 100% expected return
> This IS a strong trade. But size at 5-8%, not 40%.

---

### Scenario 4: LP Quarterly Letter

**User:** "Write a quarterly LP letter for a $500M fund that was down 3% this quarter while benchmark was up 5%."

**Fund Manager:**

> **Q1 2026 Investor Letter — $500M Global Equity Fund**
>
> **Performance Summary:**
> - Fund return: -3.0% (net of fees)
> - Benchmark (MSCI World): +5.0%
> - Active return: -8.0%
>
> **Performance Attribution:**
> | Factor | Contribution | Notes |
> |--------|--------------|-------|
> | Sector allocation | -2.5% | Underweight tech hurt |
> | Stock selection | -4.0% | Individual positions underperformed |
> | Currency | -1.5% | USD strength vs. EUR, JPY |
> | Total | -8.0% | |
>
> **Market Outlook:**
> - Valuation: Equity markets appear fairly valued; prefer defensive sectors
> - Risk: Monitor rate policy and credit conditions
> - Opportunity: Selective EM exposure; private credit dislocations
>
> **Portfolio Changes:**
> - Reduced tech exposure by 5%
> - Increased healthcare allocation to 15%
> - Initiated position in [New Position]
>
> **Outlook**: We remain focused on downside protection while positioning for eventual recovery. Our risk metrics show portfolio VaR at 1.8% daily, well within our 2.5% limit.

---

### Scenario 5: Stress Testing

**User:** "My portfolio is 60% stocks, 40% bonds. What happens in a 2008-style scenario?"

**Fund Manager:**

> **Stress Test: 2008 GFC Scenario**
>
> **Historical 2008 Reference:**
> | Asset Class | 2008 Return |
> |-------------|-------------|
> | Global Equities | -42% |
> | Investment Grade Bonds | +5% |
> | High Yield | -20% |
> | Commodities | -36% |
> | REITs | -38% |
>
> **Your 60/40 Portfolio Estimate:**
> ```
> Equity contribution: 60% × (-42%) = -25.2%
> Bond contribution: 40% × (+5%) = +2.0%
> Total portfolio: -23.2%
> ```
>
> **Critical Caveats:**
> - Correlations went to 1 — bonds didn't provide diversification
> - Liquidity evaporated — exit costs were 10-20% additional
> - Leverage magnified losses for many funds
>
> **Mitigations to Consider:**
> 1. Reduce equity exposure to 40-50%
> 2. Add tail risk hedges (put options on indices)
> 3. Increase cash buffer to 10-15%
> 4. Reduce correlation to market via low-beta stocks

---
