## 10. Common Pitfalls & Anti-Patterns

### High Severity

**Anti-Pattern 1: Training Without Scaling Laws

```
BAD:  "Let's train a 13B model on 200B tokens because that's what the competition did."

GOOD: Apply Chinchilla: 13B model → compute-optimal = 260B tokens.
      If inference is important (production deployment), train longer:
      Mistral-7B trained on 8T tokens (significantly over-compute budget)
      for better inference efficiency.
      Always derive from your compute budget, not copying competitors.
```

**Anti-Pattern 2: Reporting Benchmark Without Contamination Check

```
BAD:  "We scored 82% on MMLU — our model is better than GPT-4."
      (No contamination check performed)

GOOD: Before ANY benchmark report:
      1. Run 13-gram overlap check between training data and test set
      2. If overlap > 0.1%, report with caveat or remove from paper
      3. Use decontamination tools (Pythia
      Contaminated benchmarks are not peer-reviewable and damage credibility.
```

### Medium Severity

**Anti-Pattern 3: Reward Hacking in RLHF

```
BAD:  PPO training continues for 3 epochs; reward goes from 2.1 → 4.8.
      But human evaluators rate quality as WORSE.
      (Reward model has been gamed; KL not constrained)

GOOD: Monitor KL(policy ‖ SFT_ref) throughout training.
      Set hard KL budget: stop or reduce LR when KL > 10 nats.
      Use held-out human evals (separate from RM training data) as ground truth.
      High RM score ≠ high human quality.
```

**Anti-Pattern 4: Architecture Cargo-Culting

```
BAD:  "LLaMA uses SwiGLU so we should too, no need to ablate."

GOOD: Run a 1B proxy experiment comparing your target choice against alternatives.
      Ablation takes 1-2 days at 1B scale vs. 3+ months at 70B scale.
      SwiGLU IS better than GeLU (empirically proven in PaLM paper),
      but your specific data mix and tokenizer may interact differently.
      Trust, but verify.
```

