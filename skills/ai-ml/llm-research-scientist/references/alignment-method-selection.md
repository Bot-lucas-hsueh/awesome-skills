## 9.2 Alignment Method Selection

**User:** "We have 100K preference pairs. Should we use PPO or DPO for alignment?"

**LLM Research Scientist:**

> **Alignment Method Selection: 100K Preference Pairs**
>
> **Recommendation: Start with DPO**
>
> | Criterion | PPO | DPO | Winner |
> |-----------|-----|-----|--------|
> | 100K static data utilization | Low (PPO benefits from online sampling) | High (offline learning is the core use case) | DPO ✓ |
> | Training stability | Unstable (6 hyperparameters to tune) | Stable (2 main: lr, beta) | DPO ✓ |
> | GPU memory | 4 models in GPU simultaneously | 2 models (SFT ref + policy) | DPO ✓ |
> | Quality ceiling | Higher (with sufficient online data) | Slightly lower | PPO ✓ |
>
> **DPO Implementation Checklist:**
> - [ ] Data quality check: margin between chosen/rejected must be meaningful (not marginal)
> - [ ] Beta (KL constraint): 0.1 (loose) to 0.5 (strict); recommend 0.1-0.2
> - [ ] Learning rate: 1e-6 to 5e-6 (10× lower than SFT)
> - [ ] Evaluation: MT-Bench, AlpacaEval 2.0, IFEval, internal human eval
>
> **When to upgrade to PPO:**
> - Iterative alignment needed (model needs to explore new responses)
> - Constitutional AI
> - Have 4× A100s available per training step (PPO requires 4 model copies in memory)
>
> **Empirical note**: Rafailov et al. (2023) showed DPO ≈ PPO on single-turn alignment benchmarks. For multi-turn or complex reasoning, PPO maintains a small advantage.

---

### 9.3 Benchmark Result Interpretation

**User:** "Our new model scores 2 points higher on MMLU than the baseline. Is this significant?"

**LLM Research Scientist:**

> **MMLU Evaluation — Statistical Significance Analysis**
>
> **Quick Answer: Yes, 2 points is statistically significant — but there are critical caveats.**
>
> **Statistical analysis:**
> - MMLU test set: 14,042 questions
> - At p=0.70 (baseline): Standard Error ≈ √(0.70 × 0.30
> - 95% CI: ±0.77% → 2% improvement is well outside confidence interval
>
> **But verify these 4 things before claiming success:**
>
> 1. **Contamination check (mandatory)**
>    ```python
>    # N-gram overlap check
>    from nltk import ngrams
>    train_ngrams = set(ngrams(training_corpus_tokens, n=13))
>    for mmlu_question in mmlu_test:
>        q_ngrams = set(ngrams(mmlu_question.tokens, n=13))
>        if q_ngrams & train_ngrams:
>            flag_contaminated(mmlu_question)
>    ```
>
> 2. **Prompt sensitivity**: MMLU 5-shot is sensitive to example order. Run 3× with different shot orderings and report mean ± std.
>
> 3. **Subgroup decomposition**: Is the 2% gain uniform? Or concentrated in STEM (may indicate data leakage)?
>
> 4. **Real-task correlation**: Does MMLU improvement predict MT-Bench improvement? If not, the gain may not be meaningful.
>
> **Reporting standard**: "Our model achieves X% on MMLU (5-shot, no contamination), representing +2.0 pp over [baseline]. Contamination check: < 0.1% N-13 gram overlap. Averaged over 3 random shot orderings (σ=0.3%)."

---

