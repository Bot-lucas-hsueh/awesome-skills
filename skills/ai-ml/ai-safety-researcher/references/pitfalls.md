## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Alignment Tax Denial

```markdown
❌ BAD: "Our RLHF makes the model safer AND more capable — no trade-offs!"

✅ GOOD: "RLHF typically introduces 2-5% capability regression on coding benchmarks
          in exchange for 60-80% ASR reduction. Document this trade-off explicitly
          in the model card; let stakeholders decide the acceptable trade-off point."
```

**Anti-Pattern 2: Benchmark Overfitting

```markdown
❌ BAD: Optimizing RLHF reward specifically for TruthfulQA prompts → score improves
        but real-world hallucination rate unchanged.

✅ GOOD: Evaluate on held-out datasets unseen during alignment training.
          Use HarmBench categories not in the reward model training set.
          Monthly: rotate 20% of eval suite to catch overfitting early.
```

### 🟡 Medium Severity

**Anti-Pattern 3: Safety Washing

```markdown
❌ BAD: Publishing model card claiming "extensive red-team evaluation" based on 50 prompts
        tested by internal team only.

✅ GOOD: Red-team with ≥200 prompts across ≥5 harm categories, involve external
          evaluators, report ASR per category, and commit to re-evaluation every 6 months.
```

