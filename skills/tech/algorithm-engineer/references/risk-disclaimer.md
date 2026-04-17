## § 6 · Risk Disclaimer

> **Algorithm implementation carries correctness and performance risks. Always verify solutions.**

| # | Risk | Severity | Mitigation |
|---|------|----------|------------|
| 1 | **Integer Overflow** - Intermediate calculations exceed language integer limits causing wrong answers | HIGH | Use 64-bit integers (long long), check constraints, use modular arithmetic when specified |
| 2 | **Time Limit Exceeded** - Algorithm has higher complexity than expected, times out on large inputs | HIGH | Analyze constraints carefully, optimize from O(n²) to O(n log n), use fast I/O in CP |
| 3 | **Off-by-One Errors** - Incorrect loop bounds, index handling causing wrong answers or crashes | HIGH | Test with n=1, n=2 edge cases, verify loop invariants, use 0-based vs 1-based consistently |
| 4 | **Recursion Stack Overflow** - Deep recursion exceeds stack limit on large inputs | MEDIUM | Convert to iterative, increase stack size (if allowed), or use tail recursion |
| 5 | **Floating Point Precision** - Precision loss in geometric or floating-point calculations | MEDIUM | Use epsilon comparisons, prefer integer arithmetic, use decimal types for money |
| 6 | **Hash Collision Attack** - Custom hash vulnerable to collision DoS in competitive scenarios | LOW | Use standard library hashes, use pair hashing with large primes |
| 7 | **Memory Limit Exceeded** - Excessive memory usage from DP tables or data structures | MEDIUM | Use rolling arrays, store only necessary state, optimize data structure overhead |

---
