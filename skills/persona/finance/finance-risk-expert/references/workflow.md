## § 8 · Standard Workflow

### 8.1 Credit Risk Assessment

```
Phase 1: Borrower Analysis
├── Financial statement analysis (balance sheet, income statement, cash flow)
├── Industry and macroeconomic factors
├── Management quality and governance
├── Credit history and bureau score
└── Output: Borrower risk rating

Phase 2: Facility Analysis
├── Loan structure, tenor, covenants
├── Collateral quality and coverage
├── Transaction purpose and repayment source
└── Output: Facility risk rating

Phase 3: Exposure Calculation
├── Committed amount, outstanding, undrawn
├── Currency and maturity adjustments
├── Netting and collateral offsets
└── Output: EAD calculation

Phase 4: Portfolio View
├── Concentration limits (single name, sector, geography)
├── Correlation and diversification
├── Expected loss vs. actual loss tracking
└── Output: Reserve adequacy, capital allocation
```

### 8.2 Market Risk VaR Calculation

```
Step 1: Position Capture — Get current portfolio positions by asset class
Step 2: Risk Factors — Map positions to risk factors (equity indices, interest rates, FX, commodities)
Step 3: Return Series — Gather historical returns (250+ days minimum)
Step 4: VaR Calculation — Apply historical simulation: find Nth percentile loss
Step 5: Stress Test — Apply historical/ad hoc stress scenarios
Step 6: Backtesting — Compare predicted vs. actual losses
Step 7: Reporting — Present to Risk Committee with commentary
```

---
