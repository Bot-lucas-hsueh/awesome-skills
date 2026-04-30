# Constitutional AI & RLAIF Reference

## Overview

Constitutional AI (CAI) is Anthropic's methodology for training harmless AI assistants through self-improvement, without requiring human labels identifying harmful outputs. It was introduced in December 2022 by Bai et al.

## Core Methodology

### Two-Phase Approach

```
┌─────────────────────────────────────────────────────────────────┐
│                   CONSTITUTIONAL AI PIPELINE                     │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 1: SUPERVISED LEARNING (Self-Critique & Revision)        │
│  ├── Generate initial response to potentially harmful prompt    │
│  ├── Critique response against constitutional principle         │
│  ├── Revise response based on critique                          │
│  └── Fine-tune model on revised responses                       │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 2: REINFORCEMENT LEARNING (RLAIF)                        │
│  ├── Generate response pairs from fine-tuned model              │
│  ├── AI evaluator judges which response better follows          │
│  │   constitutional principles                                  │
│  ├── Train preference model on AI-generated labels              │
│  └── RL training with preference model as reward signal         │
└─────────────────────────────────────────────────────────────────┘
```

## Constitutional Principles

Principles are drawn from sources including:
- UN Universal Declaration of Human Rights
- Apple Terms of Service
- Anthropic's research on helpful, honest, harmless AI

Example principles:
- "Choose the response that is most helpful, honest, and harmless"
- "Choose the response that is least likely to be viewed as harmful or offensive"
- "Choose the response that a thoughtful, ethical, and honest person would give"

## RLAIF Advantages

| Aspect | Human Feedback | AI Feedback (RLAIF) |
|--------|----------------|---------------------|
| Cost | ~$1-10 per preference | <$0.01 per preference |
| Scale | Limited by human bandwidth | Scales with compute |
| Consistency | High variance between labelers | Consistent application of principles |
| Harmful Content | Humans exposed to toxic material | AI critiques without human exposure |
| Coverage | Limited to labeled scenarios | Can critique any scenario |

## Critique-Revision Loop Benefits

Research shows:
- Self-supervised critiques can surpass human performance on harm detection
- Multiple revision iterations improve output quality
- The critique process is crucial—critique+revision outperforms revision alone
- Chain-of-thought reasoning improves decision transparency

## Hybrid Approach

Anthropic uses:
- **Human labels** for helpfulness (requires human judgment of quality)
- **AI labels** for harmlessness (scales efficiently; avoids human exposure to harmful content)

This hybrid preference model combines both signals for final RL training.

## Key Papers

- Bai et al. (2022): "Constitutional AI: Harmlessness from AI Feedback" — arXiv:2212.08073
