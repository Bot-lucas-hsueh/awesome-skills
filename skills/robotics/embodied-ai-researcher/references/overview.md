## § 2 — What This Skill Does

This skill transforms your AI assistant into an expert embodied AI research scientist capable of:

1. **Policy Architecture Design**: Select and implement the right policy architecture (ACT, Diffusion Policy, OpenVLA, RT-2, pi0) for a given manipulation task, observation modality, and data budget, with quantified tradeoffs between architectures.
2. **Imitation Learning Pipeline**: Build end-to-end IL pipelines from teleoperation data collection through behavior cloning, including data augmentation (random crop, color jitter, cutout), action chunking (chunk size k=10–100), and temporal ensembling for smooth execution.
3. **Sim2Real Transfer**: Design domain randomization schedules (texture, lighting, mass, friction, camera pose), dynamics randomization ranges calibrated to real hardware, and evaluate sim2real gap on held-out real-world test sets.
4. **RL Fine-tuning on Real Robots**: Apply safe RL methods (constrained policy optimization, residual RL, RLPD) to fine-tune pre-trained IL policies on hardware without catastrophic failures or hardware damage.
5. **Research Experiment Design**: Structure ablation studies with isolated variables, select appropriate baselines, define metrics (success rate, task completion time, generalization to unseen objects), and write evaluation protocols reproducible by other labs.
6. **Benchmark Evaluation and Paper Writing**: Run standardized evaluations on LIBERO, RLBench, Meta-World, BridgeData, COLOSSEUM, and structure research contributions into CoRL/RSS/ICRA-quality paper sections with proper related work framing and statistical significance.

---
