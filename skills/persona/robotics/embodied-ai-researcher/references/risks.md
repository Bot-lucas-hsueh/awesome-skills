## § 3 — Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|-------------------|------------|
| Real-robot policy deployment without collision checking | CRITICAL | Joint limits exceeded causes motor burnout; workspace collisions destroy hardware worth $50,000+ | Always wrap policy output in MoveIt collision checker; set joint torque limits in robot driver config before first trial |
| Overfit policy from small demo dataset (fewer than 20 demos) | HIGH | Zero generalization to unseen object poses; policy memorizes training trajectories exactly | Collect 50+ demos per task; apply aggressive visual augmentation; always evaluate on held-out object poses not seen in training |
| Uncalibrated camera extrinsics in policy input | HIGH | Systematic 2–5 cm perception offset causes near-total grasp failure in real deployment | Verify extrinsics with checkerboard calibration before every real-robot session; target reprojection error under 0.5 pixels |
| Sim2real gap from unmodeled contact dynamics | HIGH | Policy trained in sim fails at contact-rich phases such as insertion and peg-in-hole at rates above 70% | Use contact-rich randomization in MuJoCo; add tactile simulation; validate on real hardware at every major milestone |
| Reward hacking in RL fine-tuning | MEDIUM | Policy learns degenerate behavior satisfying reward metric without completing actual task | Use sparse rewards with minimal shaping; add human-in-the-loop reward labeling; monitor all episode videos for degenerate behaviors |
| Data contamination between train and eval splits | MEDIUM | Inflated benchmark numbers not reproducible by other labs; misleading research claims | Use object-level or scene-level splits, never frame-level; document split methodology precisely in paper and code release |
| Compounding errors in long-horizon policies | HIGH | Single-step 95% accuracy yields only 60% success over 10-step sequence (0.95 to the power of 10 equals 0.60) | Implement recovery behaviors per subtask; add per-subtask success detection; use hierarchical policies for tasks over 5 steps |

---
