# Layer 1: Assessment Engine

## Purpose

Determine user's skill-writing experience and recommend optimal creation path.

## Components

### Experience Detector

| Signal | Experience Level | Recommended Path |
|--------|------------------|------------------|
| "What's a skill?" | Novice | Beginner (30 min tutorial) |
| "I need a simple tool" | Beginner | Quick (15 min) |
| "Create a domain skill" | Intermediate | Standard (1-2 hrs) |
| "Build enterprise methodology" | Expert | Expert (2+ hrs) |

### Scope Analyzer

**Lite Tier Indicators**:
- Single API/tool wrapper
- One primary function
- No complex decision trees
- Simple input/output

**Standard Tier Indicators**:
- Domain knowledge base
- 2-5 related capabilities
- Multi-step workflows
- Some complexity

**Enterprise Tier Indicators**:
- Complete methodology
- 5+ integrated capabilities
- Complex decision frameworks
- Extensive error handling

### Time Estimator

| Tier | Min Time | Typical | Complex |
|------|----------|---------|---------|
| Lite | 10 min | 30 min | 1 hr |
| Standard | 30 min | 1-2 hrs | 4 hrs |
| Enterprise | 2 hrs | 4-8 hrs | 2+ days |

## Assessment Workflow

1. **Ask Experience**: "Have you created skills before?"
2. **Determine Scope**: "What should this skill do?"
3. **Recommend Path**: Based on experience + scope
4. **Load Resources**: Point to appropriate onboarding guide
