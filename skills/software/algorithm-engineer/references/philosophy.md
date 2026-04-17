## §4. Core Philosophy

### Problem Classification Matrix

| Problem Type | Key Characteristics | First Algorithm to Try |
|--------------|--------------------|------------------------|
| **Graph** | Nodes, edges, paths | BFS (unweighted), Dijkstra (weighted) |
| **DP** | Optimal substructure, overlapping subproblems | Top-down memoization or bottom-up |
| **Greedy** | Greedy choice property | Sort + greedy selection with proof |
| **Binary Search** | Monotonic predicate | Binary search on answer or array |
| **Two Pointers** | Sorted data, pair constraints | Left-right pointer convergence |
| **Sliding Window** | Subarray/substring constraints | Expand/shrink window with hash map |
| **Union-Find** | Connectivity, components | DSU with path compression |
| **String** | Pattern matching, manipulation | KMP, Z-function, Trie |

### Common Pitfalls

| Pitfall | Prevention |
|---------|------------|
| Integer Overflow | Use `int64_t`; check intermediate products |
| Off-by-One | Draw 3-element example; test boundaries |
| Floating Point Equality | Use epsilon or integer arithmetic |
| Wrong Base Case | Prove covers all leaf nodes |
| Stack Overflow | Use iterative for n > 10⁵ |
| TLE with Fast IO | Add `ios::sync_with_stdio(false); cin.tie(nullptr);` |

---
