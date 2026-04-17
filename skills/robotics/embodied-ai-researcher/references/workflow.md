## § 8 — Standard Workflow

### Phase 1 — Task Definition and Data Collection
**Steps:**
1. Define task success criterion precisely (binary success or staged; measurable by robot sensors without human judgment).
2. Set up teleoperation system (ALOHA bimanual, UMI wrist-mounted camera, SpaceMouse plus MoveIt).
3. Collect demonstrations: 50 demos minimum for simple tasks (pick-and-place), 200+ for dexterous tasks (insertion, folding).
4. Annotate all episodes with success/failure labels; discard failed demonstrations.
5. Define train/validation/test split at episode level (80/10/10), not frame level.

- [✓ Done]: Dataset has 50+ episodes, episode-level split defined, success labels verified by replaying episodes.
- [✗ FAIL]: Fewer than 20 demos collected, or no held-out test set defined — stop and collect more data before training.

### Phase 2 — Policy Training
**Steps:**
1. Choose architecture: ACT for bimanual/precise tasks with limited data, Diffusion Policy for multi-modal distributions, OpenVLA for language-conditioned tasks.
2. Configure observation space: RGB at 640x480 or 224x224 cropped, proprioception (joint positions plus velocities plus gripper state), optional depth or tactile.
3. Set action representation: absolute joint angles versus delta EE pose; chunk size k=10–50 for most tasks.
4. Train with documented hyperparameters; monitor train versus validation loss curve for overfitting.
5. Run open-loop action prediction MSE on validation set as sanity check before rollouts.

- [✓ Done]: Validation loss converged, train/val gap below 10%, inference runs at above 10 Hz on deployment hardware.
- [✗ FAIL]: Validation loss diverges, gap above 20%, or inference exceeds 100ms — debug architecture or apply model quantization.

### Phase 3 — Simulation Evaluation
**Steps:**
1. Run 100-episode rollouts in sim on training-distribution scenarios with fixed random seeds.
2. Run 100-episode rollouts on held-out object poses, textures, and lighting conditions.
3. Apply COLOSSEUM perturbations (20 visual variants) to measure robustness systematically.
4. Profile failure modes by category: grasp failure percentage, placement error percentage, trajectory divergence percentage.
5. Iterate on data augmentation or architecture based on structured failure mode analysis.

- [✓ Done]: Above 80% success on held-out sim eval; all failure modes categorized and documented.
- [✗ FAIL]: Below 50% on held-out sim — return to Phase 2 with stronger augmentation or additional training data.

### Phase 4 — Real Robot Deployment
**Steps:**
1. Calibrate camera extrinsics with checkerboard pattern; verify reprojection error below 0.5 pixels.
2. Set conservative joint velocity limits (50% max) and torque limits in robot driver configuration.
3. Run 10 supervised trials with human ready at emergency stop to validate basic behavioral correctness.
4. Run 50 autonomous trials across training-distribution objects; record all episodes on video.
5. Run 20 trials on novel objects for generalization measurement; document per-object success breakdown.
6. Report results: per-object success rate, failure mode breakdown by category, video evidence in paper submission.

- [✓ Done]: Above 80% real-robot success rate; sim2real gap below 20 percentage points; results match sim predictions.
- [✗ FAIL]: Below 60% real-robot success — investigate sim2real gap systematically, recalibrate cameras, add real-world data to training.

---

