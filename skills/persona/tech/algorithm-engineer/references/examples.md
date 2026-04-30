## § 4 · Examples

### Example 1: Dynamic Programming - Longest Common Subsequence

**Problem**: Given two strings `text1` and `text2`, return the length of their longest common subsequence.

**Pattern Recognition**:
- "Longest common" → DP with two sequences
- Optimal substructure: LCS(i,j) depends on LCS(i-1,j-1), LCS(i-1,j), LCS(i,j-1)
- Overlapping subproblems: Same subproblems recomputed

**Solution Approach**:
```python
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    # dp[i][j] = LCS of text1[0:i] and text2[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

**Complexity Analysis**:
- Time: O(m × n) - fill m×n table
- Space: O(m × n) - DP table
- Optimized space: O(min(m,n)) using rolling array

**Key Insights**:
1. Base case: dp[0][j] = dp[i][0] = 0 (empty string has LCS 0)
2. Match: extend LCS from diagonal
3. Mismatch: take best from either excluding current char
4. Reconstruction: backtrack from dp[m][n] to find actual subsequence

---

### Example 2: Graph Algorithm - Dijkstra with Path Reconstruction

**Problem**: Find shortest path from node `start` to all other nodes in weighted directed graph with positive weights.

**Pattern Recognition**:
- "Shortest path" + positive weights → Dijkstra's algorithm
- Single source → not Floyd-Warshall
- Need path reconstruction → track predecessors

**Solution Approach**:
```python
import heapq
from typing import List, Tuple, Dict

def dijkstra(n: int, edges: List[Tuple[int,int,int]], start: int) -> Tuple[List[int], Dict[int,int]]:
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
    
    # Distance array
    dist = [float('inf')] * n
    dist[start] = 0
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    
    # For path reconstruction
    parent = {}
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # Skip if we've found better path
        if d > dist[u]:
            continue
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    return dist, parent

def get_path(parent: Dict[int,int], start: int, end: int) -> List[int]:
    """Reconstruct path from start to end using parent map."""
    if end not in parent and end != start:
        return []
    
    path = []
    cur = end
    while cur != start:
        path.append(cur)
        cur = parent[cur]
    path.append(start)
    return path[::-1]
```

**Complexity Analysis**:
- Time: O((V + E) log V) with binary heap
- Space: O(V) for distance array + O(V) for parent map
- Optimization: Fibonacci heap gives O(V log V + E)

**Common Mistakes**:
1. Not checking `d > dist[u]` (stale entries in heap)
2. Using Dijkstra with negative weights
3. Forgetting to initialize distance to infinity

---

### Example 3: Tree Problem - Lowest Common Ancestor with Binary Lifting

**Problem**: Find lowest common ancestor of two nodes in a binary tree. Multiple queries, tree is static.

**Pattern Recognition**:
- Tree queries → LCA with binary lifting
- Preprocess once, answer queries in O(log n)
- Alternative: Euler tour + RMQ

**Solution Approach**:
```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LCA:
    def __init__(self, root: TreeNode):
        self.depth = {}
        self.up = {}  # up[node][k] = 2^k-th ancestor of node
        self.LOG = 20  # Enough for 10^6 nodes
        
        self._dfs(root, None, 0)
    
    def _dfs(self, node: TreeNode, parent: Optional[TreeNode], d: int):
        if not node:
            return
        
        self.depth[node] = d
        self.up[node] = {}
        self.up[node][0] = parent
        
        # Binary lifting preprocessing
        for k in range(1, self.LOG):
            if self.up[node].get(k-1):
                self.up[node][k] = self.up[self.up[node][k-1]].get(k-1)
        
        self._dfs(node.left, node, d + 1)
        self._dfs(node.right, node, d + 1)
    
    def get_lca(self, u: TreeNode, v: TreeNode) -> TreeNode:
        # Ensure u is deeper
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        
        # Lift u up to same depth as v
        diff = self.depth[u] - self.depth[v]
        for k in range(self.LOG - 1, -1, -1):
            if diff >= (1 << k):
                u = self.up[u][k]
                diff -= (1 << k)
        
        if u == v:
            return u
        
        # Lift both up together
        for k in range(self.LOG - 1, -1, -1):
            if self.up[u].get(k) != self.up[v].get(k):
                u = self.up[u][k]
                v = self.up[v][k]
        
        return self.up[u][0]
```

**Complexity Analysis**:
- Preprocessing: O(n log n) time, O(n log n) space
- Per query: O(log n) time
- Compare to naive: O(n) per query

**Key Insights**:
1. Binary lifting enables jumping 2^k ancestors at a time
2. Bring deeper node to same level first
3. Then lift both until just before LCA
4. Works for any tree (not just binary)

---

### Example 4: Advanced DP - Edit Distance with Space Optimization

**Problem**: Given two strings `word1` and `word2`, return minimum number of operations to convert word1 to word2. Operations: insert, delete, replace.

**Pattern Recognition**:
- "Minimum operations" → DP
- Two strings → 2D DP
- Space can be optimized → only need previous row

**Solution Approach**:
```python
def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    
    # Space-optimized: only need previous row
    prev = list(range(n + 1))  # dp[0][j] = j (delete all)
    
    for i in range(1, m + 1):
        curr = [i] + [0] * n  # dp[i][0] = i (insert all)
        
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                curr[j] = prev[j-1]  # No operation needed
            else:
                # Replace: prev[j-1] + 1
                # Delete: prev[j] + 1 (delete word1[i-1])
                # Insert: curr[j-1] + 1 (insert word2[j-1])
                curr[j] = 1 + min(prev[j-1], prev[j], curr[j-1])
        
        prev = curr
    
    return prev[n]
```

**Complexity Analysis**:
- Time: O(m × n)
- Space: O(n) with rolling array (vs O(m × n) naive)

**Recurrence Relation**:
```
if word1[i] == word2[j]:
    dp[i][j] = dp[i-1][j-1]  # Characters match
else:
    dp[i][j] = 1 + min(
        dp[i-1][j],    # Delete from word1
        dp[i][j-1],    # Insert into word1  
        dp[i-1][j-1]   # Replace
    )
```

---

### Example 5: Segment Tree - Range Sum Query with Point Updates

**Problem**: Implement a data structure that supports range sum queries and point updates on an array.

**Pattern Recognition**:
- "Range query + point update" → Segment tree or Fenwick tree
- Fenwick simpler for sum, segment tree more flexible
- Both give O(log n) per operation

**Solution Approach** (Segment Tree):
```python
class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        # 4 * n is safe upper bound for segment tree size
        self.tree = [0] * (4 * self.n)
        self.nums = nums
        self._build(0, 0, self.n - 1, nums)
    
    def _build(self, node: int, left: int, right: int, nums: List[int]):
        if left == right:
            self.tree[node] = nums[left]
            return
        
        mid = (left + right) // 2
        self._build(2 * node + 1, left, mid, nums)
        self._build(2 * node + 2, mid + 1, right, nums)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def update(self, index: int, val: int) -> None:
        """Update nums[index] = val"""
        diff = val - self.nums[index]
        self.nums[index] = val
        self._update(0, 0, self.n - 1, index, diff)
    
    def _update(self, node: int, left: int, right: int, index: int, diff: int):
        if left > index or right < index:
            return
        
        self.tree[node] += diff
        
        if left != right:
            mid = (left + right) // 2
            self._update(2 * node + 1, left, mid, index, diff)
            self._update(2 * node + 2, mid + 1, right, index, diff)
    
    def query(self, left: int, right: int) -> int:
        """Return sum of nums[left..right]"""
        return self._query(0, 0, self.n - 1, left, right)
    
    def _query(self, node: int, nl: int, nr: int, left: int, right: int) -> int:
        # No overlap
        if nl > right or nr < left:
            return 0
        
        # Complete overlap
        if left <= nl and nr <= right:
            return self.tree[node]
        
        # Partial overlap
        mid = (nl + nr) // 2
        return (self._query(2 * node + 1, nl, mid, left, right) +
                self._query(2 * node + 2, mid + 1, nr, left, right))


# Fenwick Tree (simpler alternative for sum)
class FenwickTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        for i, num in enumerate(nums):
            self.update(i, num)
    
    def _lowbit(self, x: int) -> int:
        return x & (-x)
    
    def update(self, index: int, delta: int) -> None:
        """Add delta to nums[index]"""
        i = index + 1  # 1-indexed
        while i <= self.n:
            self.tree[i] += delta
            i += self._lowbit(i)
    
    def query(self, index: int) -> int:
        """Return prefix sum nums[0..index]"""
        i = index + 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= self._lowbit(i)
        return res
    
    def range_query(self, left: int, right: int) -> int:
        """Return sum nums[left..right]"""
        return self.query(right) - self.query(left - 1)
```

**Complexity Analysis**:
- Build: O(n)
- Update: O(log n)
- Query: O(log n)
- Space: O(n)

**Segment Tree vs Fenwick Tree:**
| Feature | Segment Tree | Fenwick Tree |
|---------|--------------|--------------|
| Code complexity | More complex | Simpler |
| Space | ~4n | n+1 |
| Range sum | Yes | Yes (prefix difference) |
| Range min/max | Yes | No |
| Lazy propagation | Yes | Limited |

---
