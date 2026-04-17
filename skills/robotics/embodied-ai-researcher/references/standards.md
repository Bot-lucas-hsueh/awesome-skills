## § 7 — Standards & Reference

### Key Frameworks

- **Behavior Cloning (BC)**: Supervised learning on (observation, action) pairs from expert demonstrations. Suffers from covariate shift (compounding errors at test time). Required baseline for all IL comparisons. Implementation: standard cross-entropy or MSE loss on action prediction.
- **DAgger (Ross et al., 2011)**: Dataset Aggregation interactive IL that queries expert on policy-visited states. Reduces compounding errors by closing the distribution shift gap but requires online expert availability at training time.
- **ACT (Zhao et al., 2023)**: Action Chunked Transformers with CVAE encoder for multi-modal action prediction. Predicts k-step action chunks to reduce compounding errors. Temporal ensemble at inference for smooth control. State-of-the-art for bimanual manipulation with limited data.

### Performance Metrics

| Metric | Formula | Target Range | Notes |
|--------|---------|--------------|-------|
| Task Success Rate | successes divided by total_episodes | Above 80% research, above 95% production | Primary metric; always report with 95% confidence interval |
| Generalization Rate | success_novel divided by success_train | Above 0.7 for strong generalization claim | Tests true policy capability beyond memorization |
| Trajectory Length Ratio | L_policy divided by L_expert | 0.9 to 1.3 | Measures efficiency relative to expert demonstration |
| Action Prediction MSE | mean of squared differences between predicted and ground truth actions | Below 1e-3 for joint space, below 5mm for Cartesian | Diagnostic metric only; not proxy for task success |
| Policy Inference FPS | steps divided by wall_time_seconds | Above 10 Hz for real-time control | Policy inference must not bottleneck control loop |
| Sim2Real Gap | success_real divided by success_sim | Above 0.6 acceptable, above 0.8 excellent | Quantifies domain randomization quality |
| Data Efficiency | Minimum demos required for 80% task success | Below 50 for simple tasks, below 200 for dexterous | Key practical deployability metric |

---

