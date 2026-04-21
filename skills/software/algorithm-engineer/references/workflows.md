## 8. Essential Algorithms

### Sorting

| Algorithm | Time | Space | Stable | Notes |
|-----------|------|-------|--------|-------|
| **Quick Sort** | O(n log n) avg | O(log n) | No | In-place, cache friendly; O(n²) worst case |
| **Merge Sort** | O(n log n) | O(n) | Yes | Stable, optimal for external sorting |
| **Heap Sort** | O(n log n) | O(1) | No | Guaranteed O(n log n), poor cache |
| **Counting Sort** | O(n + k) | O(k) | Yes | Integer range k; not comparison-based |
| **Radix Sort** | O(nk) | O(n + k) | Yes | Fixed-length integers; beats O(n log n) for large n |
| **Tim Sort** | O(n log n) | O(n) | Yes | Python/Java default; exploits natural runs |

### Searching

- **Binary Search**: O(log n) — sorted arrays; also applicable to answer-space search (binary search on answer)
- **Interpolation Search**: O(log log n) expected — uniformly distributed data
- **Exponential Search**: O(log n) — unbounded/infinite arrays

### Graph Algorithms

#### Traversal

| Algorithm | Strategy | Use Case |
|-----------|----------|----------|
| **BFS** | Level by level | Shortest path (unweighted), connected components, bipartite check |
| **DFS** | Depth first | Cycle detection, topological sort, SCC, articulation points |

#### Shortest Path

| Algorithm | Time | Use Case |
|-----------|------|----------|
| **Dijkstra** | O((V+E) log V) | Non-negative weights; binary heap implementation |
| **Dijkstra + Fibonacci Heap** | O(E + V log V) | Dense graphs with non-negative weights |
| **Bellman-Ford** | O(VE) | Negative weights; detect negative cycles |
| **Floyd-Warshall** | O(V³) | All-pairs shortest path; small V (≤500) |
| **A*** | O(E) with admissible heuristic | Pathfinding with domain heuristic |
| **SPFA** | O(VE) worst | Bellman-Ford with queue optimization; unreliable in practice |

#### Minimum Spanning Tree

- **Kruskal's**: O(E log E) — sort edges, union-find for cycle detection; best for sparse graphs
- **Prim's**: O((V+E) log V) — priority queue, vertex-based; best for dense graphs

#### Network Flow

- **Ford-Fulkerson**: O(E × max_flow) — conceptual basis for flow algorithms
- **Dinic's Algorithm**: O(V² × E) — standard for competitive programming; O(E√V) for unit-capacity graphs

#### Strongly Connected Components (SCC)

- **Tarjan's**: O(V + E) — single DFS pass; outputs SCCs in reverse topological order
- **Kosaraju's**: O(V + E) — two DFS passes; conceptually simpler

### Dynamic Programming

#### Pattern Recognition

- **Optimal Substructure**: Optimal solution contains optimal subsolutions — verify with cut-and-paste argument
- **Overlapping Subproblems**: Same subproblems solved multiple times — memoize or tabulate

#### Common Patterns

- **0/1 Knapsack**: O(nW) DP, optimize space to O(W) with rolling array
- **Unbounded Knapsack**: Same recurrence, iterate items in forward direction
- **Longest Common Subsequence (LCS)**: O(nm) time, O(min(n,m)) space with rolling array
- **Edit Distance (Levenshtein)**: O(nm) with three operations (insert, delete, replace)
- **Longest Increasing Subsequence (LIS)**: O(n²) DP or O(n log n) with patience sorting
- **Matrix Chain Multiplication**: O(n³) interval DP
- **Convex Hull Trick**: Optimize DP transitions of form dp[i] = min(dp[j] + b[j]*a[i])
- **Divide & Conquer DP**: Optimize when opt(i, j) ≤ opt(i, j+1) — reduces O(n³) to O(n² log n)

#### Approaches

| Approach | Trade-off | When to Use |
|----------|-----------|-------------|
| **Top-down (Memoization)** | Natural recursion, easy to write | When subproblem structure maps cleanly to recursion |
| **Bottom-up (Tabulation)** | No stack overflow, cache-friendly | When iteration order is clear; enables space optimization |

### Greedy Algorithms

**When valid**: Problems with provable greedy-choice property + optimal substructure
**Proof technique**: Exchange argument — show swapping any non-greedy choice with the greedy choice never worsens the solution

**Classic examples**:
- Activity Selection: O(n log n) — sort by finish time, always pick earliest-finishing
- Huffman Coding: O(n log n) — min-heap, merge two lowest-frequency nodes at each step
- Fractional Knapsack: O(n log n) — sort by value/weight ratio
- Interval Scheduling Maximization: sort by end time; greedy achieves optimal

### String Algorithms

| Algorithm | Time | Use Case |
|-----------|------|----------|
| **KMP** | O(n + m) | Pattern matching; failure function avoids redundant comparisons |
| **Z-function** | O(n) | String matching; Z[i] = length of longest prefix matching substring starting at i |
| **Rabin-Karp** | O(n + m) expected | Multiple pattern matching; rolling hash |
| **Aho-Corasick** | O(n + m + k) | Multi-pattern matching; failure links build automaton |
| **Suffix Array + LCP** | O(n log n) | All suffix operations; substring search, LCS of multiple strings |
| **Manacher's** | O(n) | Longest palindromic substring |

---
