# Common Pitfalls & Anti-Patterns

## 10.1 Critical Mistakes

| # | Mistake | Severity | Prevention |
|---|---------|----------|------------|
| 1 | **Look-ahead bias** | 🔴 High | Use only data available at trade time |
| 2 | **Survivorship bias** | 🔴 High | Include delisted stocks in backtest |
| 3 | **Overfitting** | 🔴 High | Limit parameters, use walk-forward |
| 4 | **Ignoring transaction costs** | 🔴 High | Include realistic costs in backtest |
| 5 | **Concentrated positions** | 🔴 High | Hard limit: max 10% per position |
| 6 | **No stop-loss** | 🔴 High | Always define max loss per trade |

## 10.2 Strategy Anti-Patterns

| Pattern | ❌ Wrong | ✅ Correct |
|---------|----------|-----------|
| Data snooping | Optimize on full dataset | Split: train/validation/test |
| Cherry picking | Show best strategies | Report all attempts |
| Ignoring slippage | Assume execution at close | Use realistic fills |
| Over-trading | Daily rebalancing | Threshold-based rebalance |

## 10.3 Risk Management Rules

1. **Never risk more than 1% per trade**
2. **Max 20% portfolio in single sector**
3. **Stop-loss is mandatory: 2 ATR default**
4. **Review correlation monthly**
5. **Rebalance when drift > 5% from target**
