## § 6 — Professional Toolkit

| Tool
|----------------|---------|-------------|
| **LeRobot (HuggingFace)** | Unified framework for ACT, Diffusion Policy, TD-MPC2 training and evaluation | Primary training framework for manipulation policies; standardized dataset format |
| **robosuite
| **MuJoCo 3.x** | Physics simulation with accurate contact dynamics and soft body support | Sim training when contact fidelity matters (insertion, assembly, cloth manipulation) |
| **IsaacLab (NVIDIA)** | GPU-accelerated parallel RL training across thousands of environments | Large-scale RL when 1000+ parallel environments needed; locomotion policy training |
| **ACT (Action Chunked Transformers)** | Transformer policy with CVAE for multi-modal action prediction and temporal ensemble | Bimanual tasks and precise manipulation with 50–200 demonstrations |
| **Diffusion Policy** | Denoising diffusion for multi-modal action distributions via UNet or Transformer | Tasks with multiple valid solution paths (cloth folding, pouring, rearrangement) |
| **OpenVLA** | 7B vision-language-action model fine-tuned for robot action prediction | Language-conditioned manipulation requiring broad semantic generalization |
| **RT-2
| **COLOSSEUM benchmark** | Cross-environment benchmark with 20 visual perturbation types for generalization testing | Evaluating policy robustness beyond i.i.d. success rate |
| **Rerun.io** | Real-time robot data visualization with 3D scene, time-series, and image views | Debugging policy rollouts, sensor streams, trajectory visualization during development |
| **lerobot-teleop** | Teleoperation data collection with leader-follower arms and data quality filtering | Building high-quality demonstration datasets with ALOHA or custom bimanual setups |
| **PyBullet** | Lightweight sim for rapid policy prototyping with fast iteration cycles | Quick iteration on reward shaping and policy structure before committing to MuJoCo |

---
