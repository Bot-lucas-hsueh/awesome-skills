## §3. Risk Disclaimer

| Risk | Severity | Mitigation |
|------|----------|------------|
| **Integer Overflow** | 🔴 High | Use `int64_t`/`long long`; check product bounds |
| **Time Limit Exceeded** | 🔴 High | Verify O against constraints; optimize constants |
| **Wrong Algorithm** | 🔴 High | Validate with test cases; prove correctness |
| **Off-by-One Error** | 🟡 Medium | Test n=0, n=1, n=2 explicitly |
| **Floating Point Precision** | 🟡 Medium | Use epsilon or integer arithmetic |
| **Stack Overflow** | 🟡 Medium | Convert to iterative for n > 10⁵ |
| **Memory Limit** | 🟡 Medium | Calculate usage: 4n bytes per int array |
| **Edge Case Missed** | 🟡 Medium | Enumerate: n=0, n=1, min, max, duplicates |

⚠️ **Critical:** Dijkstra fails on negative weights — use Bellman-Ford. Recursive DFS on n=10⁶ overflows — use BFS/DFS.

---
