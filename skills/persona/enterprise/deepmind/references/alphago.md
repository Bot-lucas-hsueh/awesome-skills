# AlphaGo / AlphaZero Deep Dive

## Overview

AlphaGo (2016) was the first computer program to defeat a professional human Go player, and subsequently the world champion. AlphaZero (2017) generalized this approach to master Go, Chess, and Shogi from self-play without human data.

---

## Historical Context

### The Challenge of Go

- **19×19 board**: 361 positions
- **Branching factor**: ~250 legal moves per position
- **Game tree complexity**: 10^170 possible games
- **Compare to chess**: 10^47 possible games
- **Previous state**: Best programs at amateur level

### Key Milestones

| Date | Event |
|------|-------|
| Oct 2015 | AlphaGo defeats Fan Hui (2-dan pro) 5-0 |
| Mar 2016 | AlphaGo defeats Lee Sedol (9-dan) 4-1 |
| May 2017 | AlphaGo defeats Ke Jie (#1 ranked) 3-0 |
| Oct 2017 | AlphaZero paper published |
| Dec 2017 | AlphaZero masters Chess and Shogi |

---

## AlphaGo Architecture

### Two-Stage Training

```
Stage 1: Supervised Learning
├── Data: 30 million positions from KGS Go server
├── Target: Human expert moves
├── Network: 13-layer CNN
├── Output: Policy (move probabilities)
└── Result: Policy network p_σ

Stage 2: Reinforcement Learning
├── Initialize: θ = σ (from Stage 1)
├── Method: Policy gradient with self-play
├── Opponent: Randomly selected past versions
├── Reward: +1 win, -1 loss
└── Result: RL policy network p_ρ
```

### Value Network

Separate network trained to predict game outcomes:
```
Training data: Self-play games from RL policy network
Input: Board position
Output: v(s) ∈ [-1, +1] (expected outcome from position)
```

### Monte Carlo Tree Search (MCTS)

**Algorithm (per move):**

```
for simulation = 1 to N:
    # Selection
    node = root
    while node is fully expanded:
        node = argmax_a [Q(s,a) + U(s,a)]
    
    # Expansion
    if node not terminal:
        expand node with policy network prior P(s,a)
    
    # Evaluation
    value = value network v(s_L) + random rollout
    
    # Backup
    update visit counts and action-values for all visited nodes

# Play
select move with maximum visit count N(s,a)
```

**PUCB Formula:**
```
U(s,a) = c_puct × P(a|s) × √N(s) / (1 + N(s,a))
```

---

## AlphaGo Zero Architecture

### Key Innovation: No Human Data

| Component | AlphaGo | AlphaGo Zero |
|-----------|---------|--------------|
| Human games | 30M positions | None |
| Policy network | Separate SL + RL | Single network |
| Value network | Separate | Single network |
| Rollouts | Fast rollout policy | None |
| Features | Handcrafted | Raw board only |

### Unified Neural Network

```
Input: 19×19×17 tensor
├── 8 past board positions (16 planes: black + white stones)
├── 1 current color plane
└── No handcrafted features

Neural Network (ResNet):
├── 40 or 80 residual blocks
├── Each block: Conv → BatchNorm → ReLU → Conv → BatchNorm → Add → ReLU
├── Policy head: Conv → FC → softmax over 19×19+1 moves
└── Value head: Conv → FC → tanh → scalar in [-1, 1]

Loss function:
L = (z - v)² - πᵀlog(p) + c||θ||²
    │      │      │
    │      │      └── L2 regularization
    │      └── Cross-entropy with MCTS policy
    └── MSE with actual outcome
```

### Self-Play Training Loop

```
ITERATION:
1. GENERATE GAMES
   for game = 1 to 25,000:
       play game using MCTS with current network
       store (s_t, π_t, z) for each position
       where π_t = MCTS visit count distribution
             z = ±1 (game outcome)

2. TRAIN NETWORK
   Sample batch from most recent 500k-1M positions
   SGD on loss L for 1,000 steps
   Learning rate: annealed from 0.02 to 0.00002

3. EVALUATE
   New network vs current best (400 games, no exploration)
   if win rate > 55%:
       promote new network to current best
```

### Training Efficiency

| Metric | Value |
|--------|-------|
| Training time | ~40 hours on TPU v1 |
| Games generated | ~5 million positions per iteration |
| Network updates | 1,000 steps per iteration |
| Iterations to superhuman | ~20 iterations |
| Hardware | 64 GPU workers + 1,920 CPU workers |

---

## AlphaZero: Generalization

### Same Algorithm, Three Games

| Game | Board Size | Result |
|------|------------|--------|
| Go | 19×19 | Superhuman in 40 hours |
| Chess | 8×8 | Superhuman in 9 hours |
| Shogi | 9×9 | Superhuman in 12 hours |

### Chess Performance

- **Evaluated against**: Stockfish 8 (2016 TCEC champion)
- **Result**: 28 wins, 72 draws, 0 losses (100-game match)
- **Training**: 4 hours starting from random weights
- **No opening book, no endgame tablebase**

### Key Insights from AlphaZero

1. **Zero-human-data learning is possible**
2. **Self-play provides unlimited training data**
3. **MCTS acts as a powerful policy improvement operator**
4. **The same architecture generalizes across games**
5. **Sample efficiency beats scale alone**

---

## MuZero: Model-Based Extension

### Extension to Unknown Dynamics

MuZero learns the game dynamics from experience:

```
Learned Model:
├── Representation: h(o) → s₀ (observation to hidden state)
├── Dynamics: g(s, a) → s', r (state transition + reward)
└── Prediction: p(s) → policy, v(s) → value (same as AlphaZero)

MCTS in learned model:
├── Plan in latent space (not actual game states)
├── Use learned dynamics to simulate trajectories
└── Select actions based on MCTS visit counts
```

### Performance

| Domain | Achievement |
|--------|-------------|
| Go | Matched AlphaZero without game rules |
| Chess | Matched AlphaZero without game rules |
| Shogi | Matched AlphaZero without game rules |
| Atari | SOTA on 57 games, competitive with model-free |

---

## Key Algorithms

### Policy Gradient (REINFORCE)

```
∇_θ J(θ) = E[∇_θ log π_θ(a|s) × R]

Update: θ ← θ + α × ∇_θ log π_θ(a|s) × (R - baseline)
```

### MCTS with Neural Networks

```
Class Node:
    def __init__(self, prior):
        self.prior = prior          # P(s,a) from network
        self.visit_count = 0
        self.value_sum = 0
    
    @property
    def Q(self):
        return self.value_sum / self.visit_count if self.visit_count > 0 else 0
    
    def U(self, parent_visit_count, c_puct):
        return c_puct * self.prior * sqrt(parent_visit_count) / (1 + self.visit_count)
    
    def select_child(self, c_puct):
        return argmax(child.Q + child.U(self.visit_count, c_puct) for child in self.children)
```

---

## Impact

### Scientific
- First superhuman Go play without human knowledge
- Demonstrated power of self-play and MCTS
- Influenced RL research direction

### Cultural
- 280 million viewers for Lee Sedol match
- "Move 37" in Game 2 — creative, never seen before
- "Move 78" in Game 4 — Lee Sedol's divine move

### Subsequent Research
- AlphaZero applied to mathematics (AlphaTensor)
- MuZero for planning without models
- General game-playing systems

---

## Citations

**AlphaGo:**
```
Silver et al. (2016). Mastering the game of Go with deep neural 
networks and tree search. Nature, 529, 484-489.
```

**AlphaGo Zero:**
```
Silver et al. (2017). Mastering the game of Go without human 
knowledge. Nature, 550, 354-359.
```

**AlphaZero:**
```
Silver et al. (2018). A general reinforcement learning algorithm 
that masters chess, shogi, and Go through self-play. Science, 362, 1140-1144.
```

**MuZero:**
```
Schrittwieser et al. (2020). Mastering Atari, Go, chess and shogi 
by planning with a learned model. Nature, 588, 604-609.
```

---

## Key Insights

1. **Self-play scales indefinitely**: No human data bottleneck
2. **MCTS as policy improvement**: Tree search amplifies network knowledge
3. **Unified architecture**: Same design works across diverse games
4. **Simple is better**: Raw board beats handcrafted features
5. **Sample efficiency**: Zero-human-data superhuman in hours
