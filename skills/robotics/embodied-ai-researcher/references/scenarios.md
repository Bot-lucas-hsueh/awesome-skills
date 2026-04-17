## § 9 — Scenario Examples

### Scenario 1: Choosing Between ACT and Diffusion Policy

**User:** I'm building a bimanual cloth folding policy. I have 80 demonstrations collected with ALOHA. Should I use ACT or Diffusion Policy? What hyperparameters should I start with?

**Expert:** Cloth folding is a canonical case where Diffusion Policy outperforms ACT. Here is the reasoning:

Cloth folding has highly multi-modal action distributions — there are many valid folding trajectories (fold left-to-right versus right-to-left, grab corner A versus corner B) and the demonstrated trajectories encode this ambiguity. ACT with its CVAE latent tends to average over modes, producing a "mean trajectory" that hesitates between options and fails at the critical fold initiation. Diffusion Policy explicitly models multi-modal distributions via the iterative denoising process.

That said, 80 demos is on the lower end for Diffusion Policy. Train both and compare on your held-out validation set (8 episodes).

Starting configuration for Diffusion Policy (Chi et al., 2023):

```python
# config/diffusion_policy_cloth.yaml
policy:
  _target_: diffusion_policy.policy.DiffusionUnetHybridImagePolicy
  shape_meta:
    obs:
      camera0_rgb: {shape: [3, 224, 224], type: rgb}
      robot0_eef_pos: {shape: [3], type: low_dim}
      robot0_eef_quat: {shape: [4], type: low_dim}
      robot1_eef_pos: {shape: [3], type: low_dim}
      robot1_eef_quat: {shape: [4], type: low_dim}
    action: {shape: [14], type: low_dim}  # 7 DOF per arm
  n_action_steps: 16      # predict 16-step chunks
  n_obs_steps: 2          # condition on last 2 observations
  num_inference_steps: 100  # DDIM for faster inference (~20ms)
  obs_encoder_group_norm: true
  crop_shape: [216, 216]  # random crop augmentation during training

training:
  lr: 1.0e-4
  batch_size: 64
  num_epochs: 3000
  lr_warmup_steps: 500
  ema_power: 0.75
```

Starting configuration for ACT (for comparison baseline):
```python
# LeRobot ACT config for ALOHA bimanual
policy.n_action_steps = 50    # action chunk size
policy.chunk_size = 50
policy.dim_model = 512
policy.n_heads = 8
policy.n_encoder_layers = 4
policy.n_decoder_layers = 7
policy.dim_feedforward = 3200
training.lr = 1e-5
training.batch_size = 8
training.num_epochs = 2000
```

Run both for their respective epoch counts and compare validation action prediction MSE and then 30-episode real rollouts with the better performer. Report both in your paper as an ablation row. My prediction: Diffusion Policy will win by 15–25 percentage points on cloth folding specifically.

---

### Scenario 2: Diagnosing a Severe Sim2Real Failure

**User:** My policy achieves 87% success in simulation but only 31% on the real robot for a cup stacking task. What is causing this and how do I debug it systematically?

**Expert:** A 56-point sim2real gap on cup stacking is large and almost certainly multi-factorial. Use this systematic triage protocol, working through causes in order of diagnostic speed:

**Step 1 — Extrinsics calibration error (fastest to check, high impact):**
```bash
# Verify camera calibration immediately
ros2 run camera_calibration cameracalibrator \
  --size 8x6 --square 0.025 \
  image:=/camera/color/image_raw \
  camera:=/camera
# Target: reprojection error below 0.5 pixels (below 1mm at 0.5m depth)
# If above 1.0 pixels, recalibrate before any other debugging
```

**Step 2 — Visual domain gap (most common cause, approximately 60% of sim2real failures):**
```python
# Diagnostic: capture real robot images and check visual similarity to sim frames
import cv2
import numpy as np

real_img = capture_camera_frame()  # your camera capture function
sim_img = load_sim_render()        # rendered frame from same viewpoint

# Compute per-channel statistics
for name, img in [("real", real_img), ("sim", sim_img)]:
    print(f"{name}: mean={img.mean(axis=(0,1))}, std={img.std(axis=(0,1))}")
# Large differences (>30 points) indicate visual domain gap requiring augmentation

# Add these augmentations to sim training to bridge the gap:
import torchvision.transforms as T
sim_augmentation = T.Compose([
    T.RandomResizedCrop(224, scale=(0.75, 1.0)),
    T.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.3, hue=0.05),
    T.RandomGrayscale(p=0.1),
    T.GaussianBlur(kernel_size=5, sigma=(0.1, 2.0)),
    T.RandomErasing(p=0.25, scale=(0.02, 0.15)),
])
```

**Step 3 — Contact dynamics gap at the stacking phase:**
Cup-on-cup contact is notoriously hard to simulate. Check whether failures occur specifically at the placement phase by logging which phase each episode fails in.
```python
# Collect 20 "placement-only" real demos starting from pre-grasp pose
# Fine-tune final 500 epochs on mixed data: 80% sim + 20% real
# This simple domain adaptation typically recovers 20-30 percentage points
mixed_dataset = ConcatDataset([
    sim_dataset,                    # 80% weight
    real_dataset * 4,               # 20% real repeated 4x to balance
])
```

**Step 4 — Systematic failure mode breakdown:**

| Failure Mode | Frequency | Root Cause | Fix |
|---|---|---|---|
| Grasp miss on cup 1 | 40% | Visual domain gap | Add color augmentation plus real data |
| Placement drift at stacking | 35% | Contact dynamics gap | Add real placement demos to training |
| Cup tips over after stack | 15% | Gripper release timing | Adjust gripper force threshold |
| Approach collision | 10% | Extrinsics error | Recalibrate camera extrinsics |

Execute in this order: extrinsics first (fast), then 20 real demos for fine-tuning (medium effort), then augmentation expansion (training rerun). This sequence typically recovers 35–45 percentage points of real-world success rate.

---

### Scenario 3: Designing a CoRL Ablation Study

**User:** I'm writing a CoRL paper on a new action representation for dexterous manipulation. How do I structure the ablation study to convince reviewers?

**Expert:** A convincing CoRL ablation isolates exactly one variable per row while fixing everything else. Here is the complete framework:

**Ablation table structure:**
```
Table 2: Ablation on action representation (% task success rate ± SE, N=50 trials each)

Method                         | In-Dist  | OOD Pose | OOD Object | FPS
───────────────────────────────|──────────|──────────|────────────|────
Ours (full method)             | 87.4±3.2 | 74.2±4.1 | 61.8±5.2   | 23
w/o relative action repr.      | 71.2±4.8 | 45.3±6.2 | 33.1±7.1   | 23
w/o action chunking (k=1)      | 82.1±3.9 | 68.4±5.0 | 54.2±6.3   | 23
w/o temporal ensemble          | 85.3±3.5 | 72.1±4.5 | 59.4±5.8   | 31
Diffusion Policy (Chi 2023)    | 79.3±4.2 | 61.2±5.8 | 48.6±6.9   | 18
BC-Transformer (strong base)   | 58.4±5.1 | 32.1±6.8 | 21.4±7.5   | 45
```

**Key ablation design rules:**
1. Each ablation row changes exactly one thing from the full method.
2. OOD columns are mandatory at CoRL — reviewers will reject without them.
3. Include inference FPS as a practical relevance signal for the community.
4. Run each condition with 3 random seeds; report mean ± standard error (not standard deviation).
5. Run N=50 trials minimum per condition; N=100 preferred for the main result rows.

**Standardized evaluation harness for reproducibility:**
```python
def evaluate_policy(policy, env, n_trials=50, seed=42):
    """Standardized evaluation protocol. Document this exactly in the paper."""
    rng = np.random.default_rng(seed)
    results = []
    for trial in range(n_trials):
        env.reset(seed=int(rng.integers(1_000_000)))
        obs = env.get_obs()
        success = False
        for step in range(MAX_STEPS):  # MAX_STEPS defined per task
            action = policy.predict(obs)
            obs, reward, done, info = env.step(action)
            if done:
                success = info.get('success', False)
                break
        results.append(float(success))
    n = len(results)
    return {
        'success_rate': np.mean(results) * 100,
        'se': np.std(results)
        'n_trials': n,
    }

# Statistical significance: two-proportion z-test
from statsmodels.stats.proportion import proportions_ztest
count = np.array([ours_successes, baseline_successes])  # raw counts
nobs = np.array([50, 50])
stat, pval = proportions_ztest(count, nobs)
print(f"Ours vs Baseline: z={stat:.2f}, p={pval:.4f}")
# CoRL reviewers expect p < 0.05 for main claims
```

Reviewers will specifically look for: (1) OOD generalization metrics, (2) statistical significance, (3) isolated ablations, and (4) honest failure analysis. Include a qualitative failure analysis section with video frames showing specific failure modes — this demonstrates scientific rigor and dramatically improves review scores.

---

