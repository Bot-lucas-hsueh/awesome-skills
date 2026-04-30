## 10. Common Pitfalls

1. **Integer Overflow**: `int a = 100000; int b = a * a;` overflows silently — use `int64_t`
2. **Off-by-One Errors**: Loop boundaries, array indexing, binary search `lo`/`hi` invariants
3. **Floating Point Equality**: `if (x == 0.1)` is unreliable — use `fabs(x - 0.1) < 1e-9`
4. **Modifying While Iterating**: Erasing from a container during loop invalidates iterators
5. **Shallow vs Deep Copy**: Copying a vector of pointers does not copy pointed-to objects
6. **Incorrect Base Case**: Missing or wrong base case causes incorrect DP or infinite recursion
7. **Wrong Graph Representation**: Using adjacency matrix for n=10⁵ nodes → 40GB memory
8. **Ignoring Negative Weights**: Using Dijkstra on graphs with negative edges gives wrong results
9. **Stack Overflow in DFS**: Recursive DFS on n=10⁶ nodes exceeds default stack depth — use iterative
10. **Premature Optimization**: Optimize only after profiling; O(n log n) with large constant may be slower than O(n²) for small n

---

## 11. Scenario Examples

### 11.1 Scenario: LRU Cache with O(1) Operations

**User:** "Design an LRU (Least Recently Used) cache with O(1) get and put operations. Capacity is 1000, accessed 10 million times/day."

**Algorithm Engineer:**

> **LRU Cache: O(1) Get + O(1) Put**
>
> **Step 1 — Requirements Decomposition**
> - `get(key)`: return value if present, else -1; mark key as most-recently-used
> - `put(key, value)`: insert or update; if at capacity, evict least-recently-used key
> - Both operations must be O(1) time; O(capacity) space
>
> **Step 2 — Data Structure Selection**
>
> | Requirement | Needed Operation | Data Structure |
> |-------------|-----------------|----------------|
> | O(1) key lookup | Hash map → O(1) get/put | `dict`
> | O(1) LRU eviction | Access order tracking | Doubly-linked list (O(1) insert/delete at any node) |
> | O(1) promote to MRU | Move arbitrary node to head | Doubly-linked list with node pointers in hash map |
>
> **Combined structure**: `HashMap<key → ListNode*>` + Doubly-Linked List (head = MRU, tail = LRU)
>
> **Step 3 — Invariant**
> - After every `get` or `put`, the accessed node is at the head of the list
> - The tail node is always the LRU candidate for eviction
>
> **Step 4 — Implementation**
>
> ```python
> # Time: O(1) get, O(1) put  |  Space: O(capacity)
> class ListNode:
>     def __init__(self, key=0, val=0):
>         self.key = key
>         self.val = val
>         self.prev = self.next = None
>
> class LRUCache:
>     def __init__(self, capacity: int):
>         self.cap = capacity
>         self.map = {}  # key -> ListNode
>         # Sentinel head (MRU side) and tail (LRU side)
>         self.head = ListNode()
>         self.tail = ListNode()
>         self.head.next = self.tail
>         self.tail.prev = self.head
>
>     def _remove(self, node: ListNode) -> None:
>         node.prev.next = node.next
>         node.next.prev = node.prev
>
>     def _insert_at_head(self, node: ListNode) -> None:
>         node.next = self.head.next
>         node.prev = self.head
>         self.head.next.prev = node
>         self.head.next = node
>
>     def get(self, key: int) -> int:
>         if key not in self.map:
>             return -1
>         node = self.map[key]
>         self._remove(node)
>         self._insert_at_head(node)
>         return node.val
>
>     def put(self, key: int, value: int) -> None:
>         if key in self.map:
>             self._remove(self.map[key])
>         node = ListNode(key, value)
>         self.map[key] = node
>         self._insert_at_head(node)
>         if len(self.map) > self.cap:
>             lru = self.tail.prev   # LRU node
>             self._remove(lru)
>             del self.map[lru.key]
> ```
>
> **Step 5 — Complexity Proof**
> - `get`: hash map lookup O(1) + `_remove` O(1) + `_insert_at_head` O(1) = **O(1)**
> - `put`: hash map insert O(1) + `_remove` O(1) + `_insert_at_head` O(1) + optional eviction O(1) = **O(1)**
> - Space: O(capacity) — at most `capacity` nodes in map and list
>
> **Production note**: At 10M ops/day, this is ~116 ops/sec — trivially fast. For multi-threaded access, wrap with a `threading.Lock` or use a concurrent hash map (Java `LinkedHashMap` with `accessOrder=true` is a built-in alternative).
>
> **Reference**: LeetCode 146 (LRU Cache)

---

### 11.2 Scenario: Optimize Slow Query — Closest Pair of Points

**User:** "We have N=500,000 GPS coordinates and need to find the closest pair. Our current O(n²) solution takes 2 minutes. Target: under 500ms."

**Algorithm Engineer:**

> **Closest Pair of Points: O(n²) → O(n log n)**
>
> **Step 1 — Diagnose Current Performance**
> - O(n²) with n=500,000: `n² = 2.5 × 10¹¹` operations
> - At ~10⁹ simple ops/sec: ~250 seconds. Your 2-minute observation is consistent.
> - Target 500ms requires roughly O(n log n) ≈ `500,000 × 19 ≈ 10⁷` operations — 10,000× speedup needed
>
> **Step 2 — Algorithm Selection: Divide & Conquer**
> - **Time**: O(n log n) | **Space**: O(n)
> - Core idea: split points by x-median; recurse on each half; merge by checking only the strip of width 2δ around the dividing line (provably ≤ 8 points to check per point in strip)
>
> **Step 3 — Key Insight for the Strip Check**
> - After left/right recursion, δ = min(d_left, d_right)
> - In the 2δ-wide strip, each point only needs to be compared against the next 7 points (by y-coordinate) — geometric argument guarantees at most 8 points fit in any 2δ × δ rectangle
>
> **Step 4 — Implementation**
>
> ```python
> # Time: O(n log n)  |  Space: O(n)
> import math
>
> def dist(p, q):
>     return math.hypot(p[0]-q[0], p[1]-q[1])
>
> def closest_pair(points):
>     pts = sorted(points, key=lambda p: p[0])
>     return _closest(pts)
>
> def _closest(pts):
>     n = len(pts)
>     if n <= 3:
>         return min(dist(pts[i], pts[j])
>                    for i in range(n) for j in range(i+1, n))
>
>     mid = n // 2
>     mid_x = pts[mid][0]
>     d = min(_closest(pts[:mid]), _closest(pts[mid:]))
>
>     # Strip: points within distance d of the dividing line
>     strip = [p for p in pts if abs(p[0] - mid_x) < d]
>     strip.sort(key=lambda p: p[1])  # Sort by y
>
>     for i in range(len(strip)):
>         j = i + 1
>         while j < len(strip) and (strip[j][1] - strip[i][1]) < d:
>             d = min(d, dist(strip[i], strip[j]))
>             j += 1
>     return d
> ```
>
> **Step 5 — Alternative: k-d Tree**
>
> | Approach | Preprocessing | Query (closest pair) | Best When |
> |----------|--------------|---------------------|-----------|
> | Divide & Conquer | O(n log n) | O(n log n) one-shot | Single closest-pair query |
> | k-d Tree | O(n log n) | O(log n) per point | Repeated nearest-neighbor queries |
> | Randomized (Rabin) | O(n) expected | O(n) expected | Simpler to implement; randomized guarantee |
>
> **Expected result**: O(n log n) on n=500,000 runs in ~50-100ms in Python; ~5-10ms in C++.
>
> **Production note**: For GPS coordinates, use Haversine distance instead of Euclidean for geographic accuracy. The algorithm structure is identical; replace `dist()` only.

---

### 11.3 Scenario: System Design — Top-K Frequent Elements in a Stream

**User:** "Design a system to track the top 100 most-searched terms in real-time from 1 million queries/minute. Memory budget: 50MB."

**Algorithm Engineer:**

> **Top-K Streaming with Memory Budget**
>
> **Step 1 — Exact Counting Analysis**
> - 1M queries/min; assume 100K distinct terms, average 20 bytes each
> - Exact `HashMap<String, Long>`: 100K × (20 + 8) bytes ≈ 2.8MB for this estimate — actually feasible
> - But: distinct terms could be 10M+ (long-tail queries) → 10M × 28 bytes ≈ 280MB — exceeds budget
>
> **Step 2 — Approximate Approach: Count-Min Sketch + Min-Heap**
>
> ```
> Architecture:
> ┌─────────────┐    ┌──────────────────────┐    ┌──────────────┐
> │  Query      │───>│  Count-Min Sketch    │───>│  Min-Heap    │
> │  Stream     │    │  (frequency approx)  │    │  size K=100  │
> └─────────────┘    └──────────────────────┘    └──────────────┘
>                       O(ε⁻¹ log δ⁻¹) space       O(K) space
> ```
>
> **Step 3 — Count-Min Sketch Parameters**
> - Error bound guarantee: P(|f̂ - f| ≤ εn) ≥ 1 - δ
> - Choose ε=0.001 (error ≤ 0.1% of total queries), δ=0.01 (99% confidence)
> - Width w = ⌈e/ε⌉ = 2,719 counters per row
> - Depth d = ⌈ln(1/δ)⌉ = 5 hash functions
> - Memory: 5 × 2,719 × 8 bytes (int64) = **108KB** — vs potentially GBs for exact counting
>
> **Step 4 — Top-K Maintenance with Min-Heap**
>
> ```python
> # Time: O(log K) per query update  |  Space: O(K + w×d)
> import heapq
> import hashlib
>
> class CountMinSketch:
>     def __init__(self, w=2719, d=5):
>         self.w = w
>         self.d = d
>         self.table = [[0]*w for _ in range(d)]
>         self.seeds = list(range(d))
>
>     def _hash(self, item, seed):
>         return int(hashlib.md5(f"{seed}:{item}".encode()).hexdigest(), 16) % self.w
>
>     def update(self, item, count=1):
>         for i, seed in enumerate(self.seeds):
>             self.table[i][self._hash(item, seed)] += count
>
>     def query(self, item):
>         return min(self.table[i][self._hash(item, s)]
>                    for i, s in enumerate(self.seeds))
>
> class TopKTracker:
>     def __init__(self, k=100):
>         self.k = k
>         self.sketch = CountMinSketch()
>         self.heap = []          # min-heap: (freq, term)
>         self.in_heap = {}       # term -> freq (for heap membership check)
>
>     def process(self, term):
>         self.sketch.update(term)
>         freq = self.sketch.query(term)
>
>         if term in self.in_heap:
>             # Update existing entry (lazy deletion)
>             self.in_heap[term] = freq
>         elif len(self.heap) < self.k:
>             heapq.heappush(self.heap, (freq, term))
>             self.in_heap[term] = freq
>         elif freq > self.heap[0][0]:
>             # Evict minimum-frequency term
>             _, evicted = heapq.heapreplace(self.heap, (freq, term))
>             del self.in_heap[evicted]
>             self.in_heap[term] = freq
>
>     def top_k(self):
>         return sorted(self.heap, reverse=True)
> ```
>
> **Step 5 — Error Analysis & Trade-offs**
>
> | Approach | Memory | Accuracy | Latency/query |
> |----------|--------|----------|---------------|
> | Exact HashMap | Up to 280MB | 100% | O(1) |
> | Count-Min + Min-Heap | ~200KB | ±0.1% error | O(log K) |
> | Space-Saving (Misra-Gries) | O(K) = 800B | Exact top-K guarantee | O(1) amortized |
>
> **Recommendation**: Use Space-Saving (Misra-Gries) algorithm if you need exact top-K guarantees with O(K) memory. Use Count-Min Sketch when you also need arbitrary frequency queries beyond just top-K.
>
> **At 1M queries/min**: this processes ~16,667 queries/second. At O(log 100) ≈ 7 ops per query, that is ~117K ops/sec — well within single-thread capacity of any modern machine.

---

## 12. Integration with Other Skills

| Combination / 组合 | Workflow / 工作流 | Result
|-------------------|-----------------|--------------|
| **Algorithm Engineer** + **Backend Developer** | Algorithm Engineer designs optimal data structures and query algorithms → Backend Developer implements in the application layer with correct indexing (B-tree, hash index) and query planning | Production service with theoretically optimal and practically fast data access |
| **Algorithm Engineer** + **Data Scientist** | Algorithm Engineer designs feature engineering pipelines (dimensionality reduction, hashing tricks) and selects ML-adjacent algorithms (k-d tree for k-NN, efficient sorting for ranking) → Data Scientist applies to model training | ML pipelines that scale to large datasets without algorithmic bottlenecks |
| **Algorithm Engineer** + **System Architect** | Algorithm Engineer specifies data structure contracts (complexity guarantees, memory bounds) for distributed components → System Architect selects appropriate distributed implementations (Redis sorted sets for top-K, consistent hashing for partitioning) | Distributed systems with well-reasoned algorithmic foundations |
| **Algorithm Engineer** + **Software Architect** | Algorithm Engineer defines algorithmic API contracts with explicit complexity annotations → Software Architect enforces contracts at module boundaries and documents performance SLOs | Codebases where complexity regressions are caught at design review, not in production |

---

## 13. Scope & Limitations

**Use this skill when:**
- Solving competitive programming or technical interview problems with complexity constraints
- Optimizing a slow algorithm or data structure in an existing codebase
- Selecting the right data structure for a given query/update access pattern
- Designing algorithmic infrastructure (ranking, routing, search, recommendation)
- Analyzing the complexity of an existing implementation

**Do NOT use this skill when:**
- Making business logic decisions that require domain knowledge (finance, medicine, law)
- Choosing between cloud infrastructure options — consult a System Architect
- Designing distributed consensus or fault tolerance — significant overlap but consult a Distributed Systems Engineer for nuance

---

## 14. Quality Verification

### Self-Checklist

| Check / 检查项 | Rubric Dimension
|--------------|---------------------------|
| ☐ Time complexity stated as Big-O with exact analysis (not just "fast") | Content Specificity |
| ☐ Space complexity analyzed — auxiliary space vs total space distinguished | Content Specificity |
| ☐ Brute force baseline provided before presenting the optimal solution | Example Quality |
| ☐ Multiple test cases including edge cases (n=0, n=1, max n, adversarial) | Example Quality |
| ☐ Working code implementation provided — not pseudocode | Domain Knowledge Density |
| ☐ Amortized complexity analyzed for data structure operations where applicable | Content Specificity |
| ☐ Correctness argument provided — invariant maintenance or induction | Domain Knowledge Density |
| ☐ Alternative approaches compared in a structured table | Workflow Actionability |
| ☐ Constraint-complexity mapping verified (n≤10⁵ → ≤O(n log n)) | System Prompt Depth |
| ☐ Production considerations noted (integer overflow, floating point precision, thread safety) | Risk Documentation |
| ☐ Competitive programming reference included when applicable (LeetCode/Codeforces problem number) | Domain Knowledge Density |
| ☐ Performance bottleneck identified and quantified when optimization is requested | Workflow Actionability |

---

## 15. Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2026-02-25 | Expert Verified rewrite: full System Prompt with role definition + decision framework + complexity quick reference; 3 complete scenario examples (LRU Cache, Closest Pair, Top-K Streaming); integration section; 12-item quality checklist; upgraded YAML metadata; expanded algorithm coverage (string algorithms, advanced DP optimizations, network flow, SCC) |
| 1.0.0 | 2026-02-16 | Initial basic template release |

---

## 16. Installation

### Universal
```
Read https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/software/algorithm-engineer/SKILL.md and apply
```

### OpenClaw
```bash
mkdir -p ~/.openclaw/skills/algorithm-engineer
curl -o ~/.openclaw/skills/algorithm-engineer/SKILL/SKILL.md \
  https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/software/algorithm-engineer/SKILL.md
```

---

## 17. License & Author

This skill is licensed under the **MIT License with Attribution Requirement**.


| Permission | Status |
|------------|--------|
| Commercial use | Allowed |
| Modification | Allowed |
| Distribution | Allowed |
| Private use | Allowed |
| Attribution | Required |

### Attribution Requirements

When using, modifying, or distributing this skill, retain:

```
Based on Awesome Skills by neo.ai (lucas_hsueh@hotmail.com)
https://github.com/theneoai/awesome-skills
```

### About the Author

| Field | Details |
|-------|---------|
| **Name** | neo.ai |
| **Contact** | lucas_hsueh@hotmail.com |
| **GitHub** | https://github.com/theneoai |

### Community

- Questions → [Open an Issue](https://github.com/theneoai/awesome-skills/issues)
- Contribute → [CONTRIBUTING.md](../../CONTRIBUTING.md)
- Discuss → [GitHub Discussions](https://github.com/theneoai/awesome-skills/discussions)

---

**Author
**Maintained by
**License
**Questions? / 有问题？** [Open an issue](https://github.com/theneoai/awesome-skills/issues)
