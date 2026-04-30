## § 7 — Anti-Patterns

| # | Anti-Pattern | Why It's Wrong | DeepSeek Solution |
|---|--------------|----------------|-------------------|
| 1 | **Brute Force Scaling** | $100M+ training is wasteful; algorithm > compute | MLA+MoE: 10× cheaper, same capability |
| 2 | **Dense 100B+ Models** | All params active = wasteful inference | MoE: 671B params, 37B active |
| 3 | **Ignoring KV Cache** | MHA quadratic memory kills long context | MLA: 93% cache reduction |
| 4 | **BF16-Only Large Models** | 2× memory overhead, slower | FP8: validated at 671B, 1.2× speedup |
| 5 | **Auxiliary Loss Balancing** | Degrades MoE performance | Aux-loss-free: bias-term routing |
| 6 | **Closed Source Only** | Community can't improve, verify, adopt | MIT license: 1M+ downloads |
| 7 | **PPO for RL Training** | Critic model = 2× memory | GRPO: no critic, group baseline |
| 8 | **Following Without Innovating** | China as "forever follower" | First FP8 at scale, MLA invention |

---
