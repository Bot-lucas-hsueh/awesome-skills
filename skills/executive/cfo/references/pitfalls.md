## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: The EBITDA Fiction

```
❌ BAD: Presenting "Adjusted EBITDA" that adds back:
   - Stock-based compensation ($20M/year)
   - "Restructuring charges" (every single year for 4 years)
   - Customer acquisition costs ("one-time investment")
   Result: Reported EBITDA = $50M. Cash EBITDA = $5M.
   Investors discover this at IPO DD → 40% valuation haircut.

✅ GOOD: Non-GAAP adjustments should be:
   (1) Truly non-recurring (not repeated annually)
   (2) Non-cash (SBC is real dilution; acknowledge it)
   (3) Consistently defined (never change definition to hit targets)
   Disclose GAAP reconciliation prominently, not buried in footnotes.
```

**Anti-Pattern 2: Revenue Recognition Acceleration

```
❌ BAD: Recognizing multi-year contract revenue upfront to hit quarterly number.
   Or booking channel partner "commitments" before actual customer purchase.
   Result: Pull-forward creates future quarter shortfalls. Restatement risk.
   SEC enforcement action; class action lawsuit average settlement $20M+.

✅ GOOD: Follow ASC 606 performance obligation timing rigorously.
   When in doubt, recognize later (conservative). Consult external auditors
   before any non-standard revenue recognition. No deal to hit a quarter
   is worth a securities fraud investigation.
```

### 🟡 Medium Severity

**Anti-Pattern 3: Synergy Overestimation

```
❌ BAD: M&A model projects $50M revenue synergies and $30M cost synergies.
   3 years post-merger: $8M revenue synergies realized, $12M cost synergies.
   Integration costs were $45M (vs. $15M modeled).
   CEO is fired. Goodwill impaired. Board lawsuit.

✅ GOOD: Apply synergy haircuts:
   Revenue synergies: model 30% of identified → 3× harder to realize
   Cost synergies: model 70% of identified → easier but still hard
   Integration costs: 2× your estimate (always underestimated)
   Time to full synergy: 3 years, not 18 months
```

**Anti-Pattern 4: Covenant Surprise

```
❌ BAD: CFO misses that leverage ratio covenant is calculated on LTM EBITDA
   (not next-12-month forecast). Acquisition closes. Q1 EBITDA weak.
   Net Debt/EBITDA at 4.2× vs. 4.0× covenant → technical default.
   Bank calls an emergency meeting. Company in crisis for 3 months.

✅ GOOD: Read every covenant definition carefully (especially EBITDA definition,
   what addbacks are allowed, basket sizes). Model covenant compliance monthly
   for the next 8 quarters in base and bear case. Any quarter within 10%
   headroom → proactive bank conversation immediately.
```

---

