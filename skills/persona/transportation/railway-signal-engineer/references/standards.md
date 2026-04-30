## § 7 · Standards & Reference

### 7.1 Signaling Design Frameworks

| Framework| When to Use| Key Steps|
|-----------------|----------------------|-------------------|
| **Route-Based Interlocking** | Conventional lines with fixed block | 1. Define routes → 2. Identify conflicts → 3. Assign signals → 4. Generate locking table |
| **ETCS Level 1 Design** | Mixed conventional/ERTMS lines | 1. Define balise positions → 2. Configure movement authorities → 3. Design mode transitions |
| **CBTC Design** | High-capacity urban metro | 1. Define ATP boundaries → 2. Design re-routing zones → 3. Configure redundancy |

### 7.2 Key Metrics

| Metric| Formula| Target|
|--------------|--------------|---------------|
| **Safety Integrity Level** | SIL 1-4 per IEC 61508 | SIL 4 for mainline critical functions |
| **Train Detection Reliability** | MTBF > 100,000 hours | Availability > 99.9% |
| **Signal Failure Rate** | < 10^-5 failures/hour | Fail-safe design |
| **Braking Distance Calculation** | d = (v²)/(2a) + reaction_distance | Must match line speed + safety margin |

---
