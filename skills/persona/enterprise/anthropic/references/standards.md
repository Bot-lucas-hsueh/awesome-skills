## § 7 · Standards & Reference

### 7.1 Anthropic Frameworks

| Framework | When to Use | Key Steps |
|-----------|-------------|-----------|
| **Constitutional AI (RLAIF)** | Scaling alignment without human feedback bottleneck | 1. Define constitutional principles → 2. Train critique model → 3. Train revision model → 4. RL from AI Feedback → 5. Validate with human evals |
| **Responsible Scaling Policy (RSP)** | Preparing for deployment of capable models | 1. Define ASL levels (1-4+) with thresholds → 2. Specify required safety measures per ASL → 3. Pre-deployment evaluations → 4. Conditional deployment commitments → 5. External oversight for ASL-3+ |
| **Mechanistic Interpretability** | Safety verification through understanding | 1. Identify candidate circuits via activation analysis → 2. Activation patching for causality → 3. Decompose into heads/neurons → 4. Counterfactual validation → 5. Document uncertainty |

### 7.2 AI Safety Levels (ASL)

| Level | Capability Threshold | Required Safeguards | Example Models |
|-------|---------------------|---------------------|----------------|
| **ASL-1** | Narrow/smaller models; minimal risk | Standard software security | Early LLMs (2018), chess engines |
| **ASL-2** | General-purpose models; early hazardous capability signs | Automated monitoring; basic security | Claude 3 family, GPT-4 |
| **ASL-3** | Models that could significantly accelerate misuse or show autonomous behaviors | Strict security; access controls; red-teaming; conditional deployment | Claude Opus 4 (classified ASL-3) |
| **ASL-4** | Models with catastrophic risk potential | Nation-state-level security; external oversight; possible deployment pause | Future frontier models |

### 7.3 Claude Model Specifications

| Model | Context | Strengths | Pricing (per 1M tokens) |
|-------|---------|-----------|------------------------|
| **Claude Opus 4** | 200K | Complex reasoning, coding, long-horizon tasks | $15 input / $75 output |
| **Claude Sonnet 4.5** | 200K | Balanced performance; fast responses; extended thinking | $3 input / $15 output |
| **Claude Haiku 3.5** | 200K | Speed, cost-efficiency; high-volume tasks | $0.80 input / $4 output |

---
