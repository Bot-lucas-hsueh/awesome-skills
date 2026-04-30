## 7. Fundamental Data Structures

### Arrays & Strings

| Operation | Time | Space |
|-----------|------|-------|
| Access | O(1) | O(1) |
| Search | O(n) | O(1) |
| Insert/Delete | O(n) | O(1) |

**Use Cases**: Fixed-size collections, matrix operations, string manipulation, prefix sums

### Linked Lists

| Type | Pros | Cons |
|------|------|------|
| **Singly** | Simple, memory efficient | Forward traversal only |
| **Doubly** | Bidirectional traversal | Extra memory for prev pointer |
| **Circular** | Round-robin applications | Complex traversal logic |

**Use Cases**: Dynamic size, O(1) front/back operations, implementing LRU cache (combined with hash map)

### Stacks & Queues

| Structure | Order | Use Cases |
|-----------|-------|-----------|
| **Stack** | LIFO | Function calls, undo, expression parsing |
| **Queue** | FIFO | BFS, scheduling, producer-consumer |
| **Deque** | Both ends | Sliding window maximum, palindrome check |
| **Priority Queue** | By priority | Dijkstra, A*, event-driven simulation |

### Trees

| Type | Properties | Use Cases |
|------|------------|-----------|
| **Binary Tree** | 0-2 children | Hierarchical data, expression trees |
| **BST** | Left < Root < Right | Ordered set/map operations |
| **Balanced BST (AVL/RB)** | Height O(log n) | Databases, std::set/map |
| **Heap** | Complete binary tree | Priority queues, heap sort |
| **Trie** | Prefix tree | Autocomplete, spell check, IP routing |
| **Segment Tree** | Range queries with lazy propagation | Range sum/min/max with updates |
| **Fenwick Tree (BIT)** | Prefix sums | Point updates + prefix sum queries |

### Graphs

| Representation | Space | Best For |
|----------------|-------|----------|
| **Adjacency Matrix** | O(V²) | Dense graphs, fast edge lookup O(1) |
| **Adjacency List** | O(V + E) | Sparse graphs (standard BFS/DFS) |
| **Edge List** | O(E) | Kruskal's MST, sorting edges |

**Graph Types**: Directed, Undirected, Weighted, DAG, Bipartite, Planar

### Hash Tables

| Aspect | Complexity | Notes |
|--------|------------|-------|
| Insert | O(1) average | O(n) worst with collisions |
| Lookup | O(1) average | Good hash function critical |
| Delete | O(1) average | Load factor < 0.75 for performance |

**Collision Resolution**: Chaining (linked list per bucket), Open addressing (linear/quadratic/double hashing)

### Advanced Structures

- **Union-Find (DSU)**: Connected components, cycle detection — O(α(n)) with path compression + union by rank
- **Segment Tree with Lazy Propagation**: Range update + range query in O(log n)
- **Sparse Table**: Static RMQ in O(n log n) preprocessing, O(1) query
- **Bloom Filter**: Probabilistic membership testing — O(1) insert/query, false positive rate tunable
- **B-Tree / B+ Tree**: Database indexing, optimized for disk I/O

---
