# JPMorgan Banker — Pitfalls & Anti-Patterns

## §1 · Valuation Pitfalls

### §1.1 Multiple Expansion Fallacy

```
❌ WRONG: "Company trades at 10x EBITDA. If it grows 20%, 
          stock will go up 20%."

PROBLEM: Ignores multiple compression as growth matures.
         Market prices in growth expectations.

✅ RIGHT: "Current 10x EBITDA embeds 15% growth expectations.
          20% growth = upside surprise = multiple expansion.
          But 25% growth expectation for next year = 
          10x → 12x multiple = 44% upside."
```

**JPMorgan Approach:**
- Reverse engineer implied growth from multiples
- Compare to historical trading range
- Assess achievability of market expectations

---

### §1.2 DCF Sensitivity Blindness

```
❌ WRONG: "DCF says $50/share. Target price $50."

PROBLEM: DCFs are highly sensitive to terminal value 
         and WACC assumptions. Single-point estimates 
         convey false precision.

✅ RIGHT: "Base case: $50 (WACC 8%, 3% terminal growth)
          Bull case: $65 (WACC 7.5%, 4% terminal)
          Bear case: $35 (WACC 9%, 2% terminal)
          Expected value: $50 (probability-weighted)"
```

**Best Practices:**
- Always present sensitivity tables
- Show valuation range, not point estimate
- Disclose key assumptions prominently
- Test against precedent transactions

---

### §1.3 Synergy Overestimation

```
❌ WRONG: "$100M revenue synergies, $50M cost synergies. 
          Deal is accretive."

PROBLEM: Synergies rarely achieved in full. 
         Revenue synergies especially uncertain.
         Integration costs often underestimated.

✅ RIGHT: "Cost synergies: $50M (75% probability, 
          2-year realization) = $37.5M expected
          Revenue synergies: $100M (25% probability, 
          3-year realization) = $25M expected
          Integration costs: -$75M (90% probability)
          Net expected synergy value: -$12.5M"
```

**JPMorgan Synergy Framework:**
| Synergy Type | Probability | Realization Period |
|--------------|-------------|-------------------|
| Cost synergies | 75% | 18-24 months |
| Revenue synergies | 25% | 24-36 months |
| One-time costs | 90% | Year 1 |

---

## §2 · Risk Management Pitfalls

### §2.1 Correlation Assumption Error

```
❌ WRONG: "Portfolio has 20 positions, each with 2% VaR. 
          Total VaR = 2%/√20 = 0.45%."

PROBLEM: Assumes zero correlation. In crisis, 
         correlations → 1.0.

✅ RIGHT: "Base case (normal correlation): 0.45% VaR
          Stress case (high correlation): 1.5% VaR
          Crisis case (correlation → 1): 2.0% VaR
          Use 1.5% for normal risk limits,
          test against 2.0% for stress scenarios."
```

**Historical Correlation Spikes:**
| Event | Normal | Crisis | Change |
|-------|--------|--------|--------|
| 2008 Financial Crisis | 0.3 | 0.8 | +167% |
| 2020 COVID Crash | 0.4 | 0.9 | +125% |
| 2022 Rate Shock | 0.2 | 0.7 | +250% |

---

### §2.2 Liquidity Illusion

```
❌ WRONG: "Position is liquid. Can exit in 1 day 
          at current marks."

PROBLEM: Liquidity evaporates when you need it most. 
         Exit costs rise non-linearly with size.

✅ RIGHT: "Normal liquidity: 1 day exit, 10bps cost
          Stressed liquidity: 1 week exit, 50bps cost
          Crisis liquidity: 1 month exit, 200bps cost
          Position limit sized for 1-week exit."
```

**JPMorgan Liquidity Ladder:**
| Liquidity Category | Exit Horizon | Cost Assumption |
|--------------------|--------------|-----------------|
| Highly liquid | 1 day | 5-10bps |
| Liquid | 1 week | 10-25bps |
| Semi-liquid | 1 month | 25-75bps |
| Illiquid | 3+ months | 100bps+ |

---

### §2.3 Tail Risk Neglect

```
❌ WRONG: "99% VaR is $10M. Risk is controlled."

PROBLEM: 1% probability events happen regularly 
         in financial markets. VaR doesn't capture 
         severity beyond threshold.

✅ RIGHT: "99% VaR: $10M
          99.9% Expected Shortfall: $35M
          Maximum historical loss: $50M
          Stress scenario loss: $75M
          Capital reserved for $75M scenario."
```

---

## §3 · Transaction Execution Pitfalls

### §3.1 Process Leakage

```
❌ WRONG: "Informal conversations with 20 potential buyers. 
          No formal process yet."

PROBLEM: Leaks destroy value. Information asymmetry 
         favors insiders. Rumors impact stock price.

✅ RIGHT: "Controlled process:
          - Signed NDAs before any disclosure
          - Code names for target and buyers
          - Secure datroom with watermarking
          - Staged disclosure (teaser → CIM → detailed)
          - Clear timeline with deadlines"
```

**JPMorgan Confidentiality Protocol:**
1. Code names assigned to all parties
2. Clean room protocols for sensitive data
3. Document watermarking (identifies leakers)
4. Restricted communication channels
5. Legal consequences for breaches

---

### §3.2 Bidder Fatigue

```
❌ WRONG: "6 rounds of bidding. Price keeps increasing."

PROBLEM: Excessive process length exhausts buyers. 
         Final bids may not reflect true value. 
         Winning bidder has buyer's remorse.

✅ RIGHT: "Disciplined process:
          - Round 1: IOI (non-binding range)
          - Round 2: Revised IOI (top 5-7)
          - Round 3: Final bids (3-5 finalists)
          - 8-10 weeks total process
          - Clear communication of timeline"
```

**Optimal Process Timeline:**
| Phase | Duration | Buyers |
|-------|----------|--------|
| Marketing | 4 weeks | 50-100 |
| First round | 2 weeks | 5-7 |
| Final round | 2 weeks | 3-5 |
| Negotiation | 2 weeks | 1-2 |

---

### §3.3 LOI Ambiguity

```
❌ WRONG: "LOI signed! Deal is done."

PROBLEM: LOIs often non-binding and vague. 
         Material terms left for later negotiation. 
         Deal can unravel.

✅ RIGHT: "Binding LOI provisions:
          - Purchase price and adjustment mechanics
          - Exclusivity period (30-45 days)
          - Break fee (2-4% of equity value)
          - Key employment agreements
          - Material deal terms (cash/stock mix)"
```

**LOI Binding vs. Non-Binding:**
| Provision | Usually Binding | Usually Non-Binding |
|-----------|-----------------|---------------------|
| Price | ✓ | |
| Exclusivity | ✓ | |
| Confidentiality | ✓ | |
| Break fees | ✓ | |
| Due diligence access | ✓ | |
| Closing conditions | | ✓ |
| Representations | | ✓ |
| Working capital adjustment | | ✓ |

---

## §4 · Regulatory Pitfalls

### §4.1 HSR Timing Mistake

```
❌ WRONG: "Sign deal today. File HSR tomorrow. 
          Close in 30 days."

PROBLEM: Hart-Scott-Rodino filing requires 30-day 
         waiting period. Second request adds months.

✅ RIGHT: "HSR timeline:
          - Sign definitive agreement
          - File HSR within 15 days
          - 30-day waiting period (can be shortened)
          - If Second Request: 6+ months additional
          - Build timeline with 6-month contingency"
```

**HSR Timeline:**
| Scenario | Timeline | Probability |
|----------|----------|-------------|
| Early termination | 15 days | 25% |
| Standard clearance | 30 days | 60% |
| Second Request | 6-12 months | 15% |

---

### §4.2 Cross-Border Complexity

```
❌ WRONG: "US deal. Just need US approval."

PROBLEM: Global operations trigger multiple 
         jurisdictions. EU, China, UK may all 
         have authority.

✅ RIGHT: "Jurisdictional analysis:
          - US: HSR required (>$101M threshold)
          - EU: Merger Regulation (combined >€5B)
          - China: MOFCOM filing (revenue thresholds)
          - UK: CMA review (if UK nexus)
          
          Parallel filings with coordinated timing.
          Longest jurisdiction drives timeline."
```

---

## §5 · Communication Pitfalls

### §5.1 Over-Promising

```
❌ WRONG: "We'll get this done in 60 days. 
          Price will exceed expectations."

PROBLEM: Creates unrealistic expectations. 
         Client disappointment if not achieved. 
         Damages credibility.

✅ RIGHT: "Base case timeline: 90 days
          Key risks that could extend:
          - Regulatory approval: +30 days
          - Buyer financing: +15 days
          - Due diligence findings: variable
          
          Price range: $45-55 per share
          Factors that determine final price:
          - Competitive dynamics
          - Market conditions
          - Due diligence findings"
```

---

### §5.2 Jargon Overload

```
❌ WRONG: "The pro forma PF LTM EBITDA adjusted for 
          synergies and normalized for one-times 
          implies a 12.5x EV/EBITDA multiple on a 
          TEV basis."

PROBLEM: CFO understands. Board may not. 
         Lose engagement with key decision-makers.

✅ RIGHT: "The company is valued at $500 million.
          That's 12.5x its profits, which is in line 
          with similar companies. The valuation 
          includes expected cost savings from the deal."
```

**Audience-Appropriate Language:**
| Audience | Approach |
|----------|----------|
| Board/CEO | Strategic rationale, key terms, risks |
| CFO | Detailed valuation, accretion/dilution |
| Legal | Contract terms, representations |
| PR/Communications | External messaging, timeline |

---

## §6 · Cultural Pitfalls

### §6.1 Win-At-All-Costs

```
❌ WRONG: "We must win this pitch. Cut corners 
          on due diligence if needed."

PROBLEM: Reputation is everything in banking. 
         One bad deal damages decades of trust.

✅ RIGHT: "We compete with integrity.
          - Thorough diligence protects clients
          - Honest advice builds long-term relationships
          - Walk away from bad deals
          - Quality over quantity"
```

**Dimon Quote:**
> "I'd rather lose a deal than lose our reputation."

---

### §6.2 Short-Term Thinking

```
❌ WRONG: "Maximize fees on this transaction."

PROBLEM: Sacrifices relationship value. 
         Client feels exploited. No repeat business.

✅ RIGHT: "Long-term greedy:
          - Fair pricing builds trust
          - 30-year relationship > one-time fee
          - Referrals from satisfied clients
          - Reputation in market"
```

---

## §7 · Model Error Checklist

### §7.1 Common Excel Errors

| Error Type | Detection | Prevention |
|------------|-----------|------------|
| Hardcoded numbers | Color code audit | Use cell references |
| Circular references | Excel warning | Iterative calc setting |
| Broken links | #REF! errors | Audit links regularly |
| Inconsistent units | Sense check | Standardize units |
| Wrong sign convention | Cash flow check | Document sign convention |
| Copy-paste errors | Line-by-line review | Modular build |

### §7.2 Sanity Checks

```
□ Growth rates < GDP + inflation + market share gain
□ Margins within historical range (unless thesis explains)
□ Working capital/sales ratio stable or explained
□ CapEx > D&A (for growing companies)
□ Tax rate ≈ statutory rate (adjust for NOLs, etc.)
□ Balance sheet balances (Assets = L+E)
□ Cash flow ties to balance sheet changes
```

---

*Last Updated: 2026-03-21*
