# Clinical Trial Design Guide

> **Standard:** ICH E9, ICH E6(R2), FDA Guidance  
> **Application:** Pfizer global clinical development

---

## Trial Design Selection Framework

```
┌─────────────────────────────────────────────────────────────────────────┐
│ STUDY OBJECTIVE → DESIGN SELECTION                                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│ Dose-finding / MTD     →  3+3, Modified Fibonacci, or CRM (Bayesian)   │
│ Safety / Tolerability  →  Single ascending dose (SAD)                   │
│                          Multiple ascending dose (MAD)                  │
│ Pharmacokinetics       →  Crossover, Parallel group                     │
│ Proof of Concept       →  Randomized, placebo-controlled                │
│ Dose-response          →  Parallel dose groups, adaptive allocation    │
│ Registration efficacy  →  RCT, superiority or non-inferiority           │
│ Long-term safety       →  Open-label extension                          │
│                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Phase I Design Considerations

### Single Ascending Dose (SAD)

**Typical Design:**
```
Cohort Structure:
├── Cohort 1: Starting dose (based on NOAEL/MABEL)
├── Cohort 2: 3x starting dose
├── Cohort 3: 10x starting dose
├── Cohort 4: 30x starting dose
└── Continue until MTD reached or sufficient exposure

Dosing Rules:
• Sentinel dosing: 2 subjects (1 active, 1 placebo) first
• If no safety concerns: remaining 4-6 subjects dosed
• Minimum 2-week observation between cohorts
• DMC review before dose escalation
```

**Starting Dose Selection:**
| Method | Application | Calculation |
|--------|-------------|-------------|
| **MABEL** | High-risk biologics | Minimal anticipated biological effect level |
| **NOAEL** | Small molecules | No observed adverse effect level from tox |
| **PK/PD modeling** | Known mechanism | Target engagement at 1/10-1/6 tox exposure |

### Multiple Ascending Dose (MAD)

**Design Elements:**
- Dosing duration: 7-14 days (typical), up to 28 days
- Cohorts: 3-4 dose levels
- PK: Rich sampling Days 1 and 14 (or last day)
- PD: Biomarker assessment at steady-state

---

## Phase II Design Considerations

### Phase IIa: Proof of Concept

**Objectives:**
- Demonstrate pharmacological activity
- Confirm mechanism of action in patients
- Inform dose selection for Phase IIb

**Design Options:**
```
Option A: Single-arm, open-label
• Rapid signal detection
• Small sample size (N=20-40)
• Historical control comparison
• Risk: Bias, no control for placebo effect

Option B: Randomized, placebo-controlled
• Parallel group or crossover
• Sample size: N=40-100
• Can include multiple doses
• Preferred for subjective endpoints

Option C: Adaptive design
• Response-adaptive randomization
• Dose-response modeling
• Seamless Phase IIa/IIb
```

### Phase IIb: Dose-Ranging

**Key Elements:**
- Multiple dose arms + placebo
- Primary endpoint: Efficacy
- Sample size: N=100-300 per arm
- Duration: Sufficient for efficacy assessment

**Dose-Response Analysis:**
```
Emax Model: E = E0 + (Emax × Dose) / (ED50 + Dose)

Where:
• E0 = placebo response
• Emax = maximum drug effect
• ED50 = dose producing 50% of Emax

Analysis Methods:
• MCP-Mod (Multiple Comparisons Procedure - Modeling)
• Bayesian Emax modeling
• Target: Identify dose(s) for Phase III
```

---

## Phase III Design Considerations

### Randomized Controlled Trial (RCT)

**Essential Elements:**
1. **Randomization**
   - Stratified by key prognostic factors
   - Block randomization to ensure balance
   - Dynamic randomization for many centers

2. **Blinding**
   - Double-blind (preferred)
   - Single-blind (if double-blind not feasible)
   - Open-label (with independent endpoint adjudication)

3. **Control Arm**
   - Placebo (if no effective therapy exists)
   - Active comparator (standard of care)
   - Non-inferiority margin justification critical

4. **Primary Endpoint**
   - Clinically meaningful
   - Measurable and objective
   - Pre-specified in protocol

### Sample Size Calculation

**Superiority Trial:**
```
n = 2 × [(Zα/2 + Zβ)² × σ²] / (μ1 - μ2)²

Where:
• Zα/2 = 1.96 (for α=0.05, two-sided)
• Zβ = 0.84 (for 80% power) or 1.28 (for 90% power)
• σ = standard deviation
• μ1 - μ2 = expected treatment difference
```

**Non-Inferiority Trial:**
```
n = 2 × [(Zα + Zβ)² × σ²] / (M - δ)²

Where:
• M = margin (must preserve 50% of effect vs placebo)
• δ = expected difference between treatments
```

### Interim Analyses

**Types:**
| Analysis | Purpose | Impact |
|----------|---------|--------|
| **Futility** | Stop for lack of efficacy | Type I error preserved |
| **Efficacy** | Stop for compelling benefit | Spending function required |
| **Safety** | Protect patient welfare | Protocol-defined stopping rules |
| **Sample size re-estimation** | Adjust for observed variance | Blinded or unblinded |

**Alpha Spending:**
```
O'Brien-Fleming: Conservative early, liberal late
• Early analyses: Very stringent (α ≈ 0.001)
• Final analysis: Near nominal α

Pocock: Equal spending across analyses
• Each analysis: Same significance level

Lan-DeMets: Flexible spending functions
• Can change number/timing of analyses
```

---

## Adaptive Trial Designs

### Seamless Phase II/III

**Concept:** Combine dose selection and confirmatory efficacy in one trial

**Design:**
```
Stage 1 (Dose Selection):
• Multiple dose arms vs placebo
• Interim analysis after X patients
• Select 1-2 doses for Stage 2

Stage 2 (Confirmatory):
• Selected dose(s) + placebo
• Additional patients randomized
• Combined analysis for final efficacy

Statistical Considerations:
• Closed testing procedure
• Combination test (Cui-Hung-Wang or inverse normal)
• Type I error control mandatory
```

### Platform Trials

**Characteristics:**
- Multiple treatments evaluated against common control
- Can add/drop arms during trial
- Shared infrastructure and data
- Efficient for rare diseases or emergency settings

**Example (COVID-19):**
- Master protocol design
- Multiple therapeutic arms
- Adaptive randomization based on response

---

## Special Populations

### Oncology Trials

**Phase I Oncology (Patients, not Healthy Volunteers):**
- Accelerated titration designs
- Continual reassessment method (CRM)
- Time-to-event CRM (TITE-CRM)
- Rolling 6 design

**Expansion Cohorts:**
- Following MTD determination
- Disease-specific cohorts
- Biomarker-selected populations

### Pediatric Trials

**Regulatory Requirements:**
- Pediatric Investigation Plan (PIP) in EU
- Pediatric Study Plan (PSP) in US
- Age-appropriate formulations
- Dosing based on PK/PD modeling

**Extrapolation:**
- If disease and treatment effect similar to adults
- Can extrapolate efficacy with PK match
- Still require safety data in pediatrics

---

## Data Management Best Practices

### Case Report Form (CRF) Design
- CDISC CDASH standards
- ePRO/eCOA for patient-reported outcomes
- Edit checks programmed in EDC
- Query management within 30 days

### Data Quality Metrics
| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Query rate | <5% of fields | >10% |
| Query resolution time | <14 days | >30 days |
| Protocol deviations | <5% of patients | >10% |
| Missing data | <10% primary endpoint | >20% |

### Interim Analysis Preparation
1. **Independent Statistical Analysis Center (ISAC)**
2. **Data Monitoring Committee (DMC) Charter**
3. **Analysis plan finalized before database lock**
4. **Code review and validation**
5. **DMC recommendations documented**

---

## Regulatory Interactions

### End-of-Phase 2 Meeting (EOP2)

**Agenda Items:**
- Phase 3 design proposal
- Dose selection rationale
- Primary endpoint acceptability
- Statistical analysis plan outline
- CMC readiness for Phase 3

**Deliverables:**
- Briefing document (sent 30 days prior)
- Presentation slides
- Proposed Phase 3 protocol synopsis
- Questions for FDA input

### Special Protocol Assessment (SPA)

**When to Request:**
- Novel trial design
- Surrogate endpoint
- Complex statistical methodology
- Risk of regulatory disagreement

**Benefit:**
- FDA agreement on design = reduced review risk
- Not binding if circumstances change
- Highly recommended for Phase 3

---

*Reference: ICH E9(R1) Addendum on Estimands and Sensitivity Analysis*
