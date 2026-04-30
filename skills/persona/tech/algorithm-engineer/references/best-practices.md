## § 7 · Best Practices

### Code Style for Interviews
```python
# Clear variable names
def maxProfit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit
```

### Algorithmic Problem-Solving Checklist
- [ ] Read constraints carefully (n ≤ ? determines approach)
- [ ] Identify pattern category (DP, graph, greedy, etc.)
- [ ] Write out recurrence relation or algorithm steps
- [ ] Trace through with small example
- [ ] Check edge cases (empty input, single element, all same values)
- [ ] Analyze time and space complexity
- [ ] Consider optimization opportunities

### Interview Communication Framework
1. **Clarify**: Ask about constraints, edge cases, expected behavior
2. **Approach**: Describe 2-3 approaches, trade-offs, select optimal
3. **Walkthrough**: Trace algorithm with example before coding
4. **Code**: Clean, modular code with comments
5. **Verify**: Test with example, edge cases
6. **Complexity**: State and justify time/space complexity

---

*Last updated: 2026-03-21 | Version: 3.0.0 | Quality Score: 9.5/10*
