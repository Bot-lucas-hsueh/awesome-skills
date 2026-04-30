## § 3 · Algorithm Knowledge Base

### 3.1 Time Complexity Cheat Sheet

| Data Structure | Access | Search | Insert | Delete | Notes |
|----------------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | Cache friendly |
| Linked List | O(n) | O(n) | O(1)* | O(1)* | *at position |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | AVL, Red-Black |
| Hash Table | N/A | O(1)* | O(1)* | O(1)* | *average case |
| Heap | O(n) | O(n) | O(log n) | O(log n) | Min/max access O(1) |
| Trie | O(m) | O(m) | O(m) | O(m) | m = string length |
| Segment Tree | O(log n) | O(log n) | O(log n) | O(log n) | Range queries |
| Fenwick Tree | O(log n) | N/A | O(log n) | O(log n) | Prefix sums |
| Union-Find | N/A | O(α(n))* | O(α(n))* | N/A | *amortized |

### 3.2 Sorting Algorithms Comparison

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |
| Radix Sort | O(d×(n+k)) | O(d×(n+k)) | O(d×(n+k)) | O(n+k) | Yes |

### 3.3 Graph Algorithm Selection Guide

| Problem Type | Algorithm | Time Complexity |
|--------------|-----------|-----------------|
| Unweighted shortest path | BFS | O(V + E) |
| Weighted shortest path (positive) | Dijkstra (heap) | O((V+E) log V) |
| Weighted shortest path (negative) | Bellman-Ford | O(V × E) |
| All-pairs shortest path | Floyd-Warshall | O(V³) |
| Minimum spanning tree | Prim/Kruskal | O(E log V) |
| Cycle detection | DFS/Union-Find | O(V + E) / O(α(V)) |
| Topological sort | Kahn's/DFS | O(V + E) |
| Strongly connected components | Kosaraju/Tarjan | O(V + E) |
| Bipartite check | BFS/DFS coloring | O(V + E) |
| Maximum flow | Dinic/Edmonds-Karp | O(V²E) / O(VE²) |

---
