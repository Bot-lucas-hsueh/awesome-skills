# Standards & Reference

## 7.1 Quantitative Trading Frameworks

### Momentum Strategies
- **Mean Reversion**: Bollinger Bands (2σ), RSI < 30, VWAP deviation > 5%
- **Trend Following**: 50/200 MA crossover, ADX > 25, ATR position sizing
- **Statistical Arbitrage**: Pairs trading, cointegration z-score > 2.0

### Risk Metrics
| Metric | Formula | Threshold |
|--------|---------|-----------|
| Sharpe Ratio | (Rp - Rf) / σp | > 1.5 |
| Sortino Ratio | (Rp - Rf) / σ_down | > 1.0 |
| Max Drawdown | Peak - Trough | < 20% |
| Calmar Ratio | Annual Return / Max DD | > 1.0 |
| VaR (95%) | Percentile 5 | < 2% daily |

## 7.2 Backtesting Standards

### Data Requirements
- Minimum 2 years daily data
- Transaction costs: 0.1% round-trip
- Slippage: 0.05% for liquid, 0.2% for illiquid
- Walk-forward validation required

### Overfitting Prevention
- In-sample:out-sample ratio 60:40 minimum
- Parameter count < sqrt(N_samples)
- Monte Carlo simulation for robustness

## 7.3 Execution Algorithms

| Algorithm | Use Case | Key Parameters |
|-----------|----------|----------------|
| TWAP | Large orders, low urgency | Time slice, max participation |
| VWAP | Benchmark tracking | Lookback window, risk aversion |
| POV | Minimal market impact | Participation rate (10-25%) |
| IS | Urgency-driven | Aggression factor |
