# OpenAI Safety & Alignment Reference

## Core Safety Philosophy

OpenAI's safety approach is built on three pillars:

1. **Iterative Deployment**: Ship, learn, improve — real-world data is irreplaceable
2. **Alignment Research**: RLHF, Constitutional AI, and mechanistic interpretability
3. **Preparedness Framework**: Systematic tracking and mitigation of catastrophic risks

## Preparedness Framework

Launched in October 2023, the Preparedness Framework formalizes OpenAI's approach to catastrophic risk assessment.

### Track, Evaluate, Forecast, Protect (TEFP)

**Track**: Monitor capability development across risk categories
**Evaluate**: Systematic measurement of potential harm
**Forecast**: Predict capability trajectories before they emerge
**Protect**: Implement safeguards proportional to risk

### Risk Categories

| Category | Definition | Example Concerns |
|----------|------------|------------------|
| **Cybersecurity** | Autonomous hacking, vulnerability exploitation | Zero-day discovery, critical infrastructure attacks |
| **CBRN** | Chemical, biological, radiological, nuclear | Pathogen design, weapon development assistance |
| **Persuasion** | Manipulation at scale | Election interference, mass radicalization |
| **Model Autonomy** | Self-directed action without human oversight | Resource acquisition, self-improvement, deception |

### Risk Levels

| Level | Criteria | Required Actions |
|-------|----------|------------------|
| **Low** | Below human baseline | Standard safety measures |
| **Medium** | Approaching human expert | Enhanced monitoring, access controls |
| **High** | Exceeding human expert, scalable | Conditional deployment, security review |
| **Critical** | Potential for severe harm | Deployment pause, external oversight |

## RLHF (Reinforcement Learning from Human Feedback)

OpenAI's primary alignment methodology, developed through InstructGPT research.

### Three-Stage Pipeline

**1. Supervised Fine-Tuning (SFT)**
- Train on high-quality human demonstrations
- Dataset: ~10K-100K examples
- Goal: Initialize model to follow instructions

**2. Reward Model Training**
- Collect human preference comparisons
- Train model to predict human preferences
- Loss: Cross-entropy on preference pairs

**3. PPO Optimization**
- Optimize policy using reward model
- KL penalty prevents drift: β ≈ 0.1-0.2
- Iterate until convergence

### Key Challenges

| Challenge | Mitigation |
|-----------|------------|
| Reward hacking | Diverse preference data, regularization |
| Distribution shift | Continuous monitoring, online learning |
| Over-optimization | Early stopping, KL constraint |
| Preference aggregation | Democratic inputs, diverse labelers |

## Constitutional AI (CAI)

Scaling alignment without proportional human labeling through self-critique.

### Process

1. **Define Constitution**: High-level principles (helpfulness, harmlessness, honesty)
2. **Self-Critique**: Model evaluates own outputs against constitution
3. **Self-Revision**: Model improves based on critique
4. **RL Training**: Train on revised outputs with RL from AI Feedback (RLAIF)

### Example Constitutional Principles

```
- Please choose the response that is most helpful, honest, and harmless.
- Avoid generating content that could be used to harm others.
- If uncertain, acknowledge limitations rather than speculate.
- Prefer responses that empower humans rather than replace them.
```

## Red Teaming

Systematic adversarial evaluation before deployment.

### Red Team Structure

| Type | Focus | Participants |
|------|-------|--------------|
| Internal | Pre-deployment evaluation | OpenAI safety researchers |
| External | Independent assessment | Partner organizations |
| Domain-specific | CBRN, cybersecurity, etc. | Subject matter experts |
| Community | Open discovery | Bug bounty, researchers |

### Evaluation Areas

- Jailbreaks and prompt injection
- Misinformation and manipulation
- Harmful content generation
- Bias and fairness
- Privacy violations
- Autonomous capabilities

## Safety Evaluations

### Automated Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| Refusal rate | % of harmful requests declined | >99% on test suite |
| False refusal | % of benign requests declined | <1% |
| Jailbreak success | % of adversarial prompts succeed | <0.1% |
| Toxicity score | Perspective API or custom | <0.05 |

### Human Evaluation

- Adversarial testing by trained red teamers
- Real-world user feedback analysis
- A/B testing of safety mitigations

## Superalignment Team

### History

**Formation (July 2023)**:
- Led by Ilya Sutskever and Jan Leike
- Mission: Solve alignment for superintelligent AI
- Resources: 20% of OpenAI compute

**Departure (May 2024)**:
- Ilya Sutskever and Jan Leike resigned
- Disagreements over safety prioritization vs commercialization
- Team disbanded, work distributed to other teams

**Aftermath**:
- Leike joined Anthropic
- Sutskever founded Safe Superintelligence Inc. (SSI)
- OpenAI formed Safety and Security Committee

## Safety and Security Committee

**Formation**: May 2024

**Members**:
- Bret Taylor (Chair)
- Adam D'Angelo
- Nicole Seligman
- Sam Altman
- Additional technical experts

**Responsibilities**:
- Review safety evaluations for frontier models
- Make deployment recommendations
- Oversee Preparedness Framework implementation

## Safety Incidents & Learnings

### GPT-2 Staged Release (2019)
- **Concern**: Potential for misuse (fake news, spam)
- **Action**: Phased release with capability thresholds
- **Outcome**: Established precedent for cautious deployment

### ChatGPT Jailbreaks (2022-2023)
- **Issue**: Users bypassing safety filters (DAN, etc.)
- **Response**: Continuous classifier improvement, prompt injection resistance
- **Ongoing**: Arms race between safety and jailbreaks

### Board Drama (November 2023)
- **Conflict**: Safety vs commercialization priorities
- **Trigger**: Altman fired by board citing communication issues
- **Resolution**: Altman reinstated; board restructured
- **Fallout**: Sutskever departure, Superalignment team dissolution

## Best Practices

### For API Developers

1. **Input Validation**: Sanitize user inputs before API calls
2. **Output Filtering**: Post-process model outputs for your use case
3. **Rate Limiting**: Prevent abuse through usage controls
4. **Monitoring**: Log and review model interactions
5. **Human Review**: High-stakes decisions require human oversight

### Safety Prompting

```
System: You are a helpful assistant. If asked to generate harmful 
content, refuse politely. If uncertain about safety, err on the 
side of caution.
```

## Comparison: OpenAI vs Anthropic Safety

| Aspect | OpenAI | Anthropic |
|--------|--------|-----------|
| Primary Method | RLHF | Constitutional AI |
| Governance | PBC (2025) | PBC from founding |
| Risk Framework | Preparedness | Responsible Scaling Policy |
| Risk Levels | Low/Medium/High/Critical | ASL-1/2/3/4+ |
| Publication | Selective | More open |
| Structure | For-profit subsidiary | PBC with LTBT |

## Key Papers

- **InstructGPT** (2022): RLHF for alignment
- **Constitutional AI** (2022): RLAIF methodology
- **GPT-4 System Card** (2023): Pre-deployment safety evaluation
- **Preparedness Framework** (2023): Catastrophic risk governance

---

*Last Updated: March 2026*
