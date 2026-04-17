## § 10 — Common Pitfalls

### Pitfall 1: Frame-Level Train/Test Split (Data Leakage)

❌ **BAD**: Splitting demonstration frames randomly 80/20 across the full dataset.
```python
# WRONG: shuffles frames from same episode into both train and test sets
from sklearn.model_selection import train_test_split
train_frames, test_frames = train_test_split(all_frames, test_size=0.2, random_state=42)
# This leaks temporal context and scene information between splits
```

✅ **GOOD**: Episode-level split to prevent information leakage.
```python
# CORRECT: split at episode (trajectory) level
episode_ids = sorted(list(dataset.episode_ids))
rng = random.Random(42)
rng.shuffle(episode_ids)
n_train = int(0.8 * len(episode_ids))
train_ids = set(episode_ids[:n_train])
test_ids = set(episode_ids[n_train:])
train_set = dataset.filter(lambda ep: ep.episode_id in train_ids)
test_set  = dataset.filter(lambda ep: ep.episode_id in test_ids)
```

**Why it matters:** Frame-level split leaks temporal context from the same episode into both train and test, inflating reported metrics by 15–30% on typical manipulation tasks. Your paper will not reproduce when other labs try to verify results.

---

### Pitfall 2: Reporting Open-Loop MSE as the Primary Metric

❌ **BAD**: "Our method achieves lower action prediction MSE than all baselines, demonstrating superior manipulation performance."

✅ **GOOD**: Report closed-loop task success rate as primary metric; use action prediction MSE only as a diagnostic tool to detect training failures, not as a performance claim.

**Why it matters:** Chi et al. (2023) demonstrated that Diffusion Policy and BC-RNN can have nearly identical action prediction MSE while differing by 30+ percentage points in closed-loop task success. MSE measures open-loop trajectory similarity, not the policy's ability to recover from deviations during real execution. Reviewers at CoRL and RSS will reject papers that rely on MSE as the primary metric.

---

### Pitfall 3: Not Normalizing the Action Space

❌ **BAD**: Training on raw joint angles in degrees (range 0–360) concatenated with EE position in meters (range 0–1) without normalization.
```python
# Mixed scales destroy gradient balance
action = np.concatenate([joint_angles_deg, ee_pos_meters])
# joint_angles are 100x larger in magnitude than ee_pos
# network ignores ee_pos dimensions during training
```

✅ **GOOD**: Normalize each action dimension to [-1, 1] using training set statistics.
```python
# Compute normalization statistics from training set only (not val or test)
action_mean = np.mean(train_actions, axis=0)  # shape: [action_dim]
action_std = np.std(train_actions, axis=0)    # shape: [action_dim]

def normalize_action(action, mean, std, eps=1e-8):
    return (action - mean)

def denormalize_action(normalized, mean, std, eps=1e-8):
    return normalized * (std + eps) + mean

# Save stats with model checkpoint for consistent inference
checkpoint['action_mean'] = action_mean
checkpoint['action_std'] = action_std
```

**Why it matters:** Mixed-scale action spaces cause gradient imbalance during training; the network learns to ignore small-magnitude dimensions (typically EE position) while over-fitting to large-magnitude dimensions (joint angles). Proper normalization typically improves task success rate by 10–20 percentage points.

---

### Pitfall 4: Insufficient Visual Augmentation for Sim2Real Transfer

❌ **BAD**: Training with only random crop augmentation and expecting real-world deployment to succeed.
```python
# Minimal augmentation fails to bridge the sim2real visual domain gap
transform = transforms.Compose([
    transforms.RandomCrop(224),
    transforms.ToTensor(),
])
```

✅ **GOOD**: Apply a comprehensive augmentation pipeline targeting the real-world domain gap.
```python
# Full sim2real augmentation pipeline (apply during training, not inference)
sim_to_real_transform = transforms.Compose([
    transforms.RandomResizedCrop(224, scale=(0.75, 1.0), ratio=(0.9, 1.1)),
    transforms.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3, hue=0.05),
    transforms.RandomGrayscale(p=0.1),
    transforms.GaussianBlur(kernel_size=5, sigma=(0.1, 2.0)),
    transforms.RandomErasing(p=0.25, scale=(0.02, 0.15)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
```

**Why it matters:** Real-world lighting variation, cast shadows, reflections, and background clutter cause visual out-of-distribution inputs that destroy policies trained with minimal augmentation. Comprehensive augmentation narrows the sim2real visual gap from 50+ percentage points to 15–20 points on typical tabletop manipulation tasks.

---

### Pitfall 5: Single Random Seed for Published Results

❌ **BAD**: Running experiments once and reporting the result as if it were representative.
```python
# Single seed — variance unknown, result could be 15-20 points above or below true mean
result = train_and_evaluate(policy_config, seed=42)
print(f"Success rate: {result['success_rate']:.1f}%")
# Submitted to paper as "our method achieves X%"
```

✅ **GOOD**: Run 3 seeds minimum; report mean plus or minus standard error across seeds.
```python
seeds = [42, 123, 456]
results = [train_and_evaluate(policy_config, seed=s) for s in seeds]
success_rates = [r['success_rate'] for r in results]
mean_sr = np.mean(success_rates)
se_sr = np.std(success_rates)
print(f"Success rate: {mean_sr:.1f} ± {se_sr:.1f}% (N=3 seeds)")
```

**Why it matters:** Manipulation policy training variance is high — a single seed can be 15–20 percentage points above or below the true mean. Multi-seed results are required for credible research claims and are now standard practice required by CoRL, RSS, and ICRA reviewers.

---

### Pitfall 6: Naive Action Chunk Execution Without Temporal Ensemble

❌ **BAD**: Executing every predicted action step in sequence without smoothing across chunk boundaries.
```python
# Naive chunking produces jerky motion at chunk boundaries
while not done:
    chunk = policy.predict_chunk(obs)  # returns k=50 actions
    for action in chunk:
        robot.execute(action)
        obs = robot.get_obs()
        # No smoothing between chunks -> discontinuous velocity profile
```

✅ **GOOD**: Apply temporal ensemble to smooth transitions between overlapping predictions.
```python
# Temporal ensemble from Zhao et al. (2023) — smooth, robust execution
from collections import deque
import numpy as np

k = 50           # chunk size
query_freq = 10  # re-query policy every 10 steps
decay = 0.01     # exponential decay for weighting older predictions

all_time_actions = deque()

for t in range(horizon):
    if t % query_freq == 0:
        obs = robot.get_obs()
        new_chunk = policy.predict_chunk(obs)  # shape: [k, action_dim]
        all_time_actions.append(new_chunk)
        # Discard oldest chunks outside effective window
        if len(all_time_actions) > k // query_freq:
            all_time_actions.popleft()

    # Compute exponentially weighted average over overlapping chunks
    n_chunks = len(all_time_actions)
    weights = np.exp(-decay * np.arange(n_chunks)[::-1])
    weights /= weights.sum()
    step_idx = t % query_freq
    ensemble_action = sum(
        w * chunk[step_idx] for w, chunk in zip(weights, all_time_actions)
    )
    robot.execute(ensemble_action)
```

**Why it matters:** Naive chunking produces discontinuous, jerky trajectories at chunk boundaries that can trigger robot safety stops and reduce task success by 5–15 percentage points. Temporal ensemble produces smooth velocity profiles and improves robustness to single-step policy errors.

---

