# Pit Stop Timing Deep Dive

## Elite Stop Anatomy (2.0-2.3 seconds)

### The Four Phases

**Phase 1: Approach & Engage (0.00 - 0.50s)**

```
Car crosses pit entry line (80 km/h)
↓
Car arrives at pit box marker
↓
Front jack engages under nose cone (0.30s)
↓
Rear jack engages under floor (0.40s)
↓
All 4 wheel gun operators position
```

Key variables: Driver braking precision (early = +0.05s, late = +0.1s). Jack operators train to engage within 0.2s of car arrival.

**Phase 2: Tire Change (0.50 - 1.50s)**

```
Wheel guns fire simultaneously on all 4 corners (0.50s)
↓
Old wheel nuts release (0.60s)
↓
Tire handlers pull old tires off simultaneously (0.70s)
↓
New tires seated on hubs (0.90s)
↓
New wheel nuts start threading (1.00s)
↓
Wheel guns apply torque (1.40s)
↓
Gun operators feel confirmation click (1.45s)
```

The 0.05s between gun release and nut confirmation is critical. Operators are trained to feel the difference between "seated but not torqued" vs. "fully secure."

**Phase 3: Release (1.50 - 2.00s)**

```
All 4 wheel guns disengage simultaneously (1.50s)
↓
Tire handlers step clear (1.60s)
↓
Front jack releases (1.75s)
↓
Rear jack releases (1.80s)
↓
Car begins lowering (1.85s)
↓
Car touches ground (2.00s)
```

**Phase 4: Exit (2.00 - 2.50s)**

```
Traffic light system: continuous monitoring
↓
All wheels confirmed secure (visual + feel)
↓
Car settled on ground
↓
Lollipop man: GREEN LIGHT (2.10s)
↓
Driver accelerates
↓
Car exits pit lane (2.50s)
```

## Timing Benchmarks (2024 Data)

| Team | Average Stop | Best Stop | Std Dev |
|------|-------------|-----------|---------|
| Red Bull | 1.95s | 1.82s | 0.15s |
| McLaren | 2.15s | 1.95s | 0.18s |
| Ferrari | 2.22s | 2.01s | 0.20s |
| Mercedes | 2.28s | 2.05s | 0.22s |
| Aston Martin | 2.35s | 2.12s | 0.25s |

## Bottleneck Analysis

The critical path in a pit stop is the slowest single wheel operation. If one wheel takes 0.55s instead of 0.45s, total stop time increases by 0.1s.

**Bottleneck Identification:**

1. Monitor individual wheel times per stop
2. Flag any wheel > 0.55s
3. Root cause: Operator fatigue? Equipment issue? Nut condition?
4. Training adjustment or equipment maintenance

**Slack Analysis:**

Parallel operations have built-in slack. The goal is to identify where slack exists and where it doesn't:

```
Parallel: All 4 wheels (each 0.45s, staggered 0.05s)
  → Total parallel time: 0.60s (not 1.80s)
  
Sequential: Front jack (0.30s) → Rear jack (0.40s)
  → Total sequential: 0.70s
  
Slack: After front jack (0.30s), 0.10s before rear jack
  → This 0.10s is slack — can absorb small delays
```

## Reaction Time Training

**Target: <0.2s from car arrival to jack engagement**

Drill: Visual cue (car enters box) → Physical response (jack up)
- Pro athletes: 0.15-0.20s
- Elite pit crew: 0.18-0.25s
- Training goal: 0.20s average

Methods:
- Strobe light training (reduce visual processing time)
- Anticipation drills (watch hundreds of car approaches)
- Weighted vest to simulate fatigue
