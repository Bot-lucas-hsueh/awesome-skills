## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Stack Overflow** | 🔴 Critical | Unbounded recursion, large stack arrays | Stack analysis, no recursion, static allocation |
| **Memory Corruption** | 🔴 Critical | Buffer overflows, pointer errors | Bounds checking, static analyzers, MPU |
| **Race Conditions** | 🔴 Critical | Shared resource access without protection | Mutexes, atomic operations, priority ceiling |
| **Power Failures** | 🟠 High | Unexpected shutdown corrupts state | Atomic writes, wear leveling, journaling |
| **EMI/EMC Issues** | 🟠 High | Electromagnetic interference | Proper grounding, shielding, filtering |
| **Timing Violations** | 🟡 Medium | Missing real-time deadlines | WCET analysis, priority tuning |

---
