## §5. Domain Knowledge

### Data Structure Complexity Cheat Sheet

| Structure | Query | Update | Use Case |
|-----------|-------|--------|----------|
| **Array** | O(1) access | O(n) insert | Fixed-size, random access |
| **Hash Map** | O(1) avg | O(1) avg | Key-value lookup |
| **BST / AVL** | O(log n) | O(log n) | Ordered traversal |
| **Segment Tree** | O(log n) | O(log n) | Range min/max/sum |
| **Fenwick Tree** | O(log n) | O(log n) | Prefix sum |
| **Trie** | O(m) | O(m) | Prefix search |
| **Union-Find** | O(α(n)) | O(α(n)) | Connectivity, cycles |

### Graph Representations

| Representation | Space | Edge Lookup | Best For |
|----------------|-------|-------------|----------|
| Adjacency Matrix | O(V²) | O(1) | Dense graphs |
| Adjacency List | O(V+E) | O(degree) | Sparse graphs (standard) |
| Edge List | O(E) | O(E) | Kruskal's MST |

### DP Patterns

| Pattern | State | Examples |
|---------|-------|----------|
| **0/1 Knapsack** | dp[i][w] | Item selection |
| **Unbounded Knapsack** | dp[w] | Coin change |
| **LCS / Edit Distance** | dp[i][j] | String alignment |
| **LIS** | dp[i] | Patience sorting O(n log n) |
| **Interval DP** | dp[i][j] | Matrix chain |
| **Digit DP** | dp[pos][tight] | Number counting |
| **Tree DP** | dp[u] | Tree problems |

📄 **Full algorithms reference** → [references/workflows.md](references/workflows.md)

---
