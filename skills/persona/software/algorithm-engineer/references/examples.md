## §7. Examples

### Example 1: Two Sum → O(n) Hash Map
```cpp
// O(n) time, O(n) space
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> seen;
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (seen.count(complement)) return {seen[complement], i};
        seen[nums[i]] = i;
    }
    return {};
}
```

### Example 2: LIS → O(n log n) Patience Sorting
```cpp
// O(n log n) time, O(n) space
vector<int> tails;
for (int x : nums) {
    auto it = lower_bound(tails.begin(), tails.end(), x);
    if (it == tails.end()) tails.push_back(x);
    else *it = x;
}
return tails.size();
```

### Example 3: Dijkstra → Shortest Path
```cpp
// O((V+E) log V) time, O(V+E) space
vector<int> dijkstra(int n, vector<vector<pair<int,int>>>& adj, int src) {
    vector<int> dist(n, INT_MAX);
    dist[src] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, src});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : adj[u])
            if (dist[u] + w < dist[v])
                pq.push({dist[v] = dist[u] + w, v});
    }
    return dist;
}
```

### Example 4: KMP → Pattern Matching
```cpp
// O(n+m) time, O(m) space
vector<int> kmp(const string& text, const string& pattern) {
    int n = text.size(), m = pattern.size();
    vector<int> fail(m, 0);
    for (int i = 1, j = 0; i < m; i++) {
        while (j > 0 && pattern[i] != pattern[j]) j = fail[j-1];
        if (pattern[i] == pattern[j]) fail[i] = ++j;
    }
    vector<int> matches;
    for (int i = 0, j = 0; i < n; i++) {
        while (j > 0 && text[i] != pattern[j]) j = fail[j-1];
        if (text[i] == pattern[j]) j++;
        if (j == m) { matches.push_back(i - m + 1); j = fail[j-1]; }
    }
    return matches;
}
```

### Example 5: Segment Tree with Lazy Propagation
```cpp
// O(log n) range update and range query
class SegTree {
    vector<long long> tree, lazy;
    void push(int n, int l, int r) {
        if (lazy[n]) {
            tree[n] += lazy[n] * (r - l + 1);
            if (l != r) { lazy[2*n] += lazy[n]; lazy[2*n+1] += lazy[n]; }
            lazy[n] = 0;
        }
    }
public:
    SegTree(int n) : tree(4*n), lazy(4*n) {}
    void range_add(int qL, int qR, long long v) { /* full implementation in references/ */ }
    long long range_sum(int qL, int qR) { /* full implementation in references/ */ }
};
```

📄 **Full example implementations** → [references/scenarios.md](references/scenarios.md)

---
