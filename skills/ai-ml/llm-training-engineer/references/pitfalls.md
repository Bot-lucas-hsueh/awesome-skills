## 10. Common Pitfalls & Anti-Patterns

### High Severity

**Anti-Pattern 1: fp16 for Large Model Training

```
BAD:  training_config.precision = "fp16"
      # At scale, attention logits can overflow fp16 max (65504)
      # → NaN cascade → training crash → wasted compute budget

GOOD: Always use bf16 for LLM training at 7B+ scale.
      bf16 range: ±3.4 × 10^38 (same as fp32 exponent)
      bf16 never overflows on attention logits.
      fp16 is only acceptable for inference, never training.
```

**Anti-Pattern 2: Skipping 1B Proxy Experiment

```
BAD:  "Our 7B architecture design looks good, let's start the 70B run."
      → 70B run fails at 50B tokens due to architecture bug
      → 3 months of GPU time wasted

GOOD: Always validate architecture + data pipeline at 1B scale first.
      1B run takes 1-2 days; identifies:
      - Data pipeline bugs (malformed batches)
      - Architecture instability (loss spikes)
      - Infrastructure issues (NCCL hangs, OOM)
      Never skip the proxy experiment.
```

### Medium Severity

**Anti-Pattern 3: LoRA Only on Attention

```
BAD:  target_modules=["q_proj", "v_proj"]  # Attention only
      # FFN layers account for 2/3 of parameters
      # Instruction following requires FFN adaptation
      # Quality significantly lower than full adaptation

GOOD: target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                       "gate_proj", "up_proj", "down_proj"]
      # Include all attention + FFN gates
      # 3-5% quality improvement for instruction following tasks
```

**Anti-Pattern 4: No Gradient Norm Monitoring

```
BAD:  Train for days without monitoring gradient norms.
      Loss looks fine but model quality is poor.
      (Silent gradient explosions being clipped → effective LR collapsing)

GOOD: Log gradient norm every step:
      wandb.log({"grad_norm": trainer.state.grad_norm})
      Normal range: 0.1 - 2.0
      Warning: > 5.0 (check data, reduce LR)
      Critical: > 10.0 (likely data issue or too high LR)
      NaN: data corruption or fp16 overflow
```

