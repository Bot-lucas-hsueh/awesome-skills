## § 10 Common Pitfalls

### Anti-Pattern 1 — Oversizing Breakers to Avoid Nuisance Trips

❌ **BAD:**
```
// 100A breaker protecting #12 AWG (20A) wire
// Breaker never trips on 18A motor overload
// Wire overheats → insulation degradation → fire
```

✅ **GOOD:**
```
// Select breaker per NEC 430.52: 150-250% of FLA
// For 65A FLA motor: 100A-162A breaker (use 150A)
// Use adjustable thermal-magnetic breaker
// Add motor overload protection (separate heater)
```

**Why it matters:** Wire ampacity is the maximum current the insulation can handle. Oversized protection defeats the safety margin — fire risk increases before breaker trips.

