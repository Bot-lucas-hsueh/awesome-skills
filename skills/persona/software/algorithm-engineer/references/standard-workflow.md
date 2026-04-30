## §6. Standard Workflow

### Phase 1: Problem Analysis

1. [ ] Identify constraints: n, m, time limit, memory limit
2. [ ] Clarify input/output formats and data ranges
3. [ ] Create 3+ examples including edge cases (n=0, n=1, max n)

**✓ Done:** Constraints documented, complexity budget defined, problem classified
**✗ Fail:** Constraints unclear, budget undefined

### Phase 2: Algorithm Design

1. [ ] List brute force first; identify bottlenecks
2. [ ] Design optimized approach meeting complexity budget
3. [ ] State invariants; prove via induction or exchange argument
4. [ ] Verify time/space complexity against constraints

**✓ Done:** Approach with proven correctness and complexity ≤ budget
**✗ Fail:** No approach meets budget, correctness unproven

### Phase 3: Implementation

1. [ ] Use `int64_t` for values that may overflow
2. [ ] Add complexity annotation as comment
3. [ ] Handle edge cases explicitly; use meaningful variable names
4. [ ] Add fast IO: `ios::sync_with_stdio(false); cin.tie(nullptr);`

**✓ Done:** Compilable, correct-looking code with O-annotations
**✗ Fail:** Does not compile, missing edge case handling

### Phase 4: Verification

1. [ ] Test provided examples + edge cases (n=0, n=1, max, duplicates)
2. [ ] Trace worst-case manually; re-verify complexity
3. [ ] Check for integer overflow in intermediate calculations

**✓ Done:** All tests pass, complexity verified
**✗ Fail:** Test case fails, complexity exceeds budget

---
