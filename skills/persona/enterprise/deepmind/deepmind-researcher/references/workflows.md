# Workflows & Code Examples

## AlphaZero Self-Play Pipeline

```
Step 1: Initialization
  Initialize network with random weights or supervised pre-training
  Set up self-play infrastructure (distributed actors)

Step 2: Self-Play Data Generation
  For each game:
    - Run MCTS using current network (800 simulations typical)
    - Sample action from MCTS policy (temperature-based)
    - Store (state, policy, outcome) tuple
  Continue until sufficient games generated

Step 3: Network Training
  Sample batch from recent self-play games
  Minimize: (z - v)² - πᵀlog(p) + c‖θ‖²
  Where z = game outcome, v = value prediction, π = MCTS policy, p = network policy

Step 4: Evaluation
  New network plays 400-game match against previous best
  If win rate > 55%, promote to new best network

Step 5: Iteration
  Return to Step 2 with new best network
  Continue until convergence or resource limit
```

## Anti-Pattern: Benchmark Chasing

```
✗ 99% on benchmark → publish
✓ 99% on benchmark + proper validation + ablations + significance + replication
```

**Required Before Publication:**
- Hold-out test set (never tuned on)
- Statistical significance (p < 0.05)
- Ablation studies
- Proper baselines
- External replication
- Code + data release plan
