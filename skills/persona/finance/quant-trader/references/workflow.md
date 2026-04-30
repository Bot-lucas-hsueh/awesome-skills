# Standard Workflow

## 8.1 Strategy Development Pipeline

```
Phase 1: Research
├── Define hypothesis (e.g., "momentum continues after earnings")
├── Collect data (price, fundamentals, sentiment)
├── Exploratory analysis (correlation, stationarity)
└── Document expected behavior

Phase 2: Backtesting
├── Implement strategy in code
├── Optimize parameters (grid search, Bayesian)
├── Monte Carlo simulation
└── Walk-forward validation

Phase 3: Risk Management
├── Position limits (< 5% per position)
├── Stop-loss rules (2 ATR)
├── Portfolio-level VaR < 2%
└── Correlation checks

Phase 4: Execution
├── Paper trading (1 month minimum)
├── Gradual deployment (10% → 50% → 100%)
├── Real-time monitoring
└── Performance attribution
```

## 8.2 Daily Trading Workflow

1. Pre-market: Review overnight positions, check news
2. Market open: Execute scheduled orders, adjust stops
3. Intraday: Monitor P&L, rebalance if drift > 1%
4. Market close: Square positions, record trade log
5. Post-market: Performance review, strategy update
