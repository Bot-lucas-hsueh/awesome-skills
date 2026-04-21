## 9. Problem-Solving Process

### Step 1: Understand

- [ ] Read problem carefully; identify all constraints (n, m, time limit, memory limit)
- [ ] Identify inputs and outputs; clarify data types and ranges
- [ ] Create 3+ examples including edge cases (n=0, n=1, all-same, adversarial)
- [ ] Ask: what is the theoretical lower bound for this problem?

### Step 2: Strategy

- [ ] Map constraint to complexity budget (n ≤ 10⁵ → O(n log n) max)
- [ ] Classify problem type: graph, DP, greedy, divide & conquer, data structure, math
- [ ] List 2-3 candidate approaches from brute force to optimal
- [ ] Analyze each candidate's complexity and correctness at a high level

### Step 3: Design

- [ ] Write pseudocode for chosen approach
- [ ] Identify all invariants the algorithm maintains
- [ ] Handle edge cases explicitly in design (not as afterthought)
- [ ] Prove or argue correctness (loop invariant, induction, exchange argument)

### Step 4: Implement

- [ ] Write clean, readable code with meaningful variable names
- [ ] Add complexity annotation as comment at function header
- [ ] Check for integer overflow: use `long long`
- [ ] Avoid floating-point equality; use epsilon comparison or integer arithmetic

### Step 5: Verify

- [ ] Test with provided examples; then with edge cases designed in Step 1
- [ ] Trace through worst-case input manually
- [ ] Re-analyze complexity after implementation; confirm it matches design
- [ ] Look for constant-factor optimizations if needed (e.g., avoid unnecessary copies)

---
