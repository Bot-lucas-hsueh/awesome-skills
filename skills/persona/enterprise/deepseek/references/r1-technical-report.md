# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

> **Source:** DeepSeek-AI, January 2025  
> **arXiv:** https://arxiv.org/abs/2501.12948  
> **Release Date:** January 20, 2025  
> **License:** MIT

---

## Executive Summary

DeepSeek-R1 achieves **OpenAI-o1 comparable reasoning performance** through large-scale reinforcement learning (RL), with training costs under **$300K** (vs $10M+ for o1).

### Key Contributions

1. **DeepSeek-R1-Zero:** First open-source research validating that reasoning can emerge purely from RL, without supervised fine-tuning (SFT)
2. **DeepSeek-R1:** Production model combining cold-start data with multi-stage RL
3. **Distillation:** Small models (1.5B-70B) achieving 90%+ of R1's reasoning capability

---

## Architecture Foundation

DeepSeek-R1 builds on DeepSeek-V3:

| Property | Value |
|----------|-------|
| Base architecture | MoE (Mixture-of-Experts) |
| Total parameters | 671B |
| Active parameters per token | 37B (5.5%) |
| Context length | 128K tokens |
| Attention | MLA (Multi-Head Latent Attention) |
| Expert configuration | 1 shared + 256 routed, top-8 |

---

## Training Pipeline

### Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    DEEPSEEK-R1 PIPELINE                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  STAGE 1: COLD START                                        │
│  ├── Input: DeepSeek-V3-Base                                │
│  ├── Process: Small SFT on curated CoT data                 │
│  └── Output: R1-Zero-Cold (readable reasoning)              │
│                          ↓                                  │
│  STAGE 2: REASONING-ORIENTED RL                             │
│  ├── Algorithm: GRPO (Group Relative Policy Optimization)   │
│  ├── Reward: Rule-based (math/code), outcome (general)      │
│  └── Emergence: Self-verification, reflection, long CoT     │
│                          ↓                                  │
│  STAGE 3: REJECTION SAMPLING SFT                            │
│  ├── Generate: 600K reasoning traces from RL checkpoint     │
│  ├── Filter: Correct answers, readable CoT                  │
│  └── Train: SFT on high-quality synthetic data              │
│                          ↓                                  │
│  STAGE 4: FINAL RL (Human Preference)                       │
│  ├── Reward: Helpfulness + Harmlessness + Rule rewards      │
│  └── Output: DeepSeek-R1 (production model)                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Stage 1: Cold Start

**Problem:** R1-Zero (pure RL) suffers from poor readability and language mixing.

**Solution:** Small amount of high-quality CoT data for cold start.

```
Cold Start Data:
  - Size: ~1,000 examples
  - Source: Human annotation + LLM generation with constraints
  - Characteristics:
    ✓ Readable reasoning format
    ✓ Language consistency
    ✓ Structured CoT (step-by-step)
```

**Why It Works:**
- Prevents early training instability
- Establishes human-readable reasoning patterns
- Maintains RL flexibility while improving coherence

### Stage 2: Reasoning-Oriented RL

**Algorithm: Group Relative Policy Optimization (GRPO)**

```
GRPO eliminates the need for a critic model:

For each question q:
  1. Sample G outputs from old policy: {o_1, o_2, ..., o_G}
  2. Compute rewards: {r_1, r_2, ..., r_G}
  3. Compute group baseline: r_baseline = mean({r_i})
  4. Calculate advantages: A_i = r_i - r_baseline
  5. Update policy to maximize: Σ log π(o_i|q) · A_i

No critic model needed → 2× memory savings vs PPO
```

**Reward Design:**

| Task Type | Reward Function |
|-----------|----------------|
| Math | Rule-based: 1 if answer correct, 0 otherwise |
| Code | Rule-based: test case pass rate |
| Logic | Rule-based: symbolic evaluation |
| General | Outcome reward: final answer correctness |

**Emergent Behaviors (observed during training):**

1. **Self-Verification:** Model checks its own work
   ```
   Example: "Let me verify this calculation... 
             23 × 17 = 391? Let me check: 23 × 10 = 230, 
             23 × 7 = 161, 230 + 161 = 391. ✓"
   ```

2. **Reflection:** Model revises previous steps
   ```
   Example: "Wait, I made an error in step 3. 
             Let me recalculate with the correct approach..."
   ```

3. **Long CoT:** Extended reasoning chains for complex problems
   ```
   Average CoT length grows from ~100 tokens to ~2000+ tokens
   during training
   ```

4. **Aha Moments:** Sudden breakthroughs during reasoning
   ```
   Example: "...oh! I see now. The key insight is to 
             substitute x = y + 1, which simplifies 
             the equation dramatically!"
   ```

### Stage 3: Rejection Sampling SFT

**Purpose:** Generate high-quality training data for supervised fine-tuning.

```
Process:
  1. Use RL checkpoint from Stage 2 as generator
  2. For each problem:
     - Generate N candidate solutions (N=16-32)
     - Filter: Keep only correct answers
     - Quality: Select readable, well-structured CoT
  3. Result: 600K high-quality reasoning traces

Data Composition:
  - Reasoning data: 600K (from rejection sampling)
  - Non-reasoning data: 200K (general QA, writing)
  - Total SFT data: 800K examples
```

### Stage 4: Final RL (Human Preference)

**Dual Reward Model:**

```
Reward = λ_1 · R_helpful + λ_2 · R_harmless + λ_3 · R_rule

Where:
  R_helpful: Human preference for helpfulness
  R_harmless: Safety reward (reducing harmful outputs)
  R_rule: Task-specific rule rewards (math correctness, etc.)
```

**Alignment Goals:**
- Maintain reasoning capability from Stage 2
- Improve helpfulness for general queries
- Ensure safety and harmlessness
- Preserve readable CoT format

---

## DeepSeek-R1-Zero: Pure RL Baseline

**Key Innovation:** First demonstration that reasoning can emerge purely from RL, without any supervised fine-tuning.

### Training

```
Starting point: DeepSeek-V3-Base (no SFT!)
Algorithm: GRPO with rule-based rewards
Training: Large-scale RL only
```

### Emergent Behaviors

| Behavior | Description | Emergence Point |
|----------|-------------|-----------------|
| Self-Verification | Model checks intermediate steps | ~20% training |
| Reflection | Model revises incorrect steps | ~30% training |
| Long CoT | Extended reasoning chains | Progressive |
| Aha Moments | Sudden solution insights | Throughout |

### Limitations

1. **Readability:** CoT can be poorly formatted
2. **Language Mixing:** Tends to mix languages (especially Chinese/English)
3. **Coherence:** Occasional incoherent reasoning chains

**Solution:** Cold start data in R1 pipeline addresses these issues.

---

## Distillation: Small Models, Big Reasoning

**Approach:** Transfer R1's reasoning patterns to smaller dense models.

### Method

```
Teacher: DeepSeek-R1 (671B MoE)
  ↓
Generate 800K synthetic reasoning traces
  ↓
Fine-tune student models (Qwen, Llama bases)
```

### Distilled Models

| Model | Base | Params | AIME 2024 | MATH-500 | GPQA |
|-------|------|--------|-----------|----------|------|
| R1-Distill-Qwen-1.5B | Qwen2.5 | 1.5B | 28.3% | 75.4% | 27.5% |
| R1-Distill-Qwen-7B | Qwen2.5 | 7B | 55.5% | 83.9% | 35.3% |
| R1-Distill-Qwen-14B | Qwen2.5 | 14B | 69.3% | 89.1% | 43.1% |
| R1-Distill-Qwen-32B | Qwen2.5 | 32B | 72.6% | 90.0% | 47.0% |
| R1-Distill-Llama-8B | Llama-3.1 | 8B | 50.4% | 80.8% | 33.3% |
| R1-Distill-Llama-70B | Llama-3.3 | 70B | 70.0% | 90.0% | 49.1% |

**Key Insight:** Even 1.5B parameter models show significant reasoning improvement when trained on R1's reasoning traces.

### Comparison with o1-mini

| Model | AIME 2024 | MATH-500 | Cost |
|-------|-----------|----------|------|
| o1-mini | 63.6% | 90.0% | $10M+ training |
| R1-Distill-Qwen-32B | 72.6% | 90.0% | ~$10K training |

**32B distilled model outperforms o1-mini at fraction of cost.**

---

## Benchmark Results

### Reasoning Benchmarks

| Benchmark | Metric | DeepSeek-R1 | OpenAI o1 | Claude-3.5 |
|-----------|--------|-------------|-----------|------------|
| AIME 2024 | Pass@1 | 79.8% | 79.2% | 16.0% |
| MATH-500 | Pass@1 | 97.3% | 96.4% | 78.3% |
| GPQA Diamond | Pass@1 | 71.5% | 75.0% | 59.4% |
| Codeforces | Rating | 2029 (96.3%) | 2061 (96.6%) | ~1400 |
| SWE-Bench | Resolved | 49.2% | 48.9% | 16.0% |

### Code Benchmarks

| Benchmark | Metric | DeepSeek-R1 | o1 | GPT-4o |
|-----------|--------|-------------|-------|--------|
| HumanEval | Pass@1 | 97.3% | 92.4% | 90.2% |
| LiveCodeBench | Pass1-COT | 65.4% | 63.4% | 33.4% |
| SWE-Bench Verified | Resolved | 42.0% | 41.0% | — |

### Knowledge Benchmarks

| Benchmark | Metric | DeepSeek-R1 | o1 | GPT-4o |
|-----------|--------|-------------|-------|--------|
| MMLU | EM | 90.8% | 91.8% | 87.2% |
| MMLU-Pro | EM | 84.0% | — | — |
| IF-Eval | Prompt Strict | 87.2% | 84.3% | 84.3% |

### Reading/Writing Benchmarks

| Benchmark | Metric | DeepSeek-R1 | o1 | GPT-4o |
|-----------|--------|-------------|-------|--------|
| DROP | F1 | 92.2% | 88.6% | 83.4% |
| FRAMES | Acc | 82.5% | 80.5% | 80.5% |
| AlpacaEval 2.0 | Win Rate | 87.6% | — | — |

---

## Training Costs

| Component | Cost Estimate |
|-----------|---------------|
| DeepSeek-V3 Base | $5.576M (sunk cost) |
| R1 RL Training | ~$200K GPU hours |
| Distillation | ~$50K GPU hours |
| **Total Incremental** | **~$250K** |

**vs OpenAI o1: ~$10M+ → 40× cheaper**

---

## Key Insights

1. **RL Can Emerge Reasoning:** No supervised data needed for basic reasoning capability
2. **Cold Start Matters:** Small amount of quality data dramatically improves readability
3. **GRPO > PPO:** Eliminating critic model saves memory without sacrificing performance
4. **Distillation Works:** Small models can inherit large model reasoning patterns
5. **Rule Rewards Sufficient:** Simple correctness-based rewards drive complex behaviors

---

## Limitations

1. **General Capability:** Slightly behind on some general language tasks vs V3
2. **Language Consistency:** Occasional mixing in non-English/Chinese contexts
3. **Prompt Sensitivity:** Performance varies with prompt formatting
4. **Software Engineering:** Strong but not yet at human expert level
5. **Long Outputs:** Can be verbose; slower than non-reasoning models

---

## Open Source Release

**MIT License:** Maximum freedom for research and commercial use

**Released:**
- DeepSeek-R1 (full 671B MoE)
- DeepSeek-R1-Zero checkpoint
- All distilled models (1.5B-70B)
- Technical report with full methodology

**Impact:**
- 10M+ downloads in first month
- Enabled hundreds of research projects
- Proved open-source can match closed frontier models

---

## References

- DeepSeek-R1 Technical Report: https://arxiv.org/abs/2501.12948
- GitHub: https://github.com/deepseek-ai/DeepSeek-R1
- HuggingFace: https://huggingface.co/deepseek-ai/DeepSeek-R1
- API Docs: https://api-docs.deepseek.com/guides/reasoning_model
