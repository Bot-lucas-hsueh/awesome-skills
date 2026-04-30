# Example 1: Manufacturing Defect Reduction

## Project Context

**Organization:** Automotive Tier 1 Supplier  
**Product:** Engine control module (ECM) housings  
**Problem:** Paint defect rate 8%, target <1%  
**Annual Impact:** $2.4M scrap and rework costs  
**Project Duration:** 4 months

---

## DEFINE Phase

### Project Charter

| Element | Description |
|---------|-------------|
| Problem Statement | Paint defect rate of 8% exceeds customer requirement of 1% and costs $2.4M annually |
| Business Case | Reduce scrap costs, improve customer satisfaction, protect contract renewal |
| Goal Statement | Reduce paint defect rate from 8% to <1% by Q2 2024 |
| Scope | Die casting through final inspection; excludes supplier materials |
| Team | BB (lead), Process Engineer, Quality Tech, Paint Operator, Maintenance |
| Timeline | 4 months |

### Voice of Customer

**Internal Customer (Assembly):**
- "We have to rework 1 in 12 housings"
- "Sanding takes 20 minutes per part"

**External Customer (OEM):**
- Defect rate >500 PPM triggers chargeback
- Potential line stop at customer facility

**CTQ Tree:**

```
Customer Need: Perfect Paint Finish
├── No Blisters (>0.5mm)
├── No Runs/Sags
├── No Dust Inclusions
├── Uniform Gloss (85±5 GU)
└── Color Match (ΔE <1.0)
```

---

## MEASURE Phase

### Data Collection Plan

| Metric | Operational Definition | Method | Sample Size |
|--------|------------------------|--------|-------------|
| Defect Rate | Parts with any defect / Total parts | Inspection | All parts |
| Defect Type | Blisters, Runs, Dust, Gloss, Color | Categorization | All defects |
| Process Parameters | Temp, Humidity, Viscosity, Flow rate | Sensors | Continuous |

### Measurement System Analysis

**Attribute Agreement Analysis (Defect Classification):**

| Appraiser | Within | vs Standard |
|-----------|--------|-------------|
| Inspector A | 92% | 88% |
| Inspector B | 89% | 85% |
| Inspector C | 94% | 91% |

**Result:** Measurement system acceptable (80% threshold met)

### Baseline Performance

```
Defect Rate by Week (8 weeks prior):
Week:  1   2   3   4   5   6   7   8
Rate: 7.8 8.2 7.5 8.5 8.0 7.9 8.3 8.1

Mean: 8.0%
StDev: 0.32%
DPMO: 80,000 (2.9σ level)
```

### Process Capability

Not applicable (attribute data), but:
- Pareto of defect types: Blisters (45%), Runs (30%), Dust (15%), Gloss (7%), Color (3%)

---

## ANALYZE Phase

### Fishbone Diagram (Blisters - Top Defect)

```
                    MAN
                     │
    MACHINE ─────── BLISTERS ─────── MATERIAL
    - Gun pressure   Problem      - Primer viscosity
    - Robot speed                 - Paint pot life
    - Booth airflow               - Contamination
                     │
    METHOD ──────────┴────────── ENVIRONMENT
    - Spray pattern               - Humidity
    - Flash time                  - Temperature
    - Film thickness              - Dust levels
```

### Hypothesis Testing

**Hypothesis 1: Primer viscosity affects blister rate**

Data collected: 30 batches at low, medium, high viscosity

| Viscosity | Sample Size | Defect Rate |
|-----------|-------------|-------------|
| Low (18s) | 500 | 12% |
| Med (22s) | 500 | 4% |
| High (26s) | 500 | 11% |

**Test:** Chi-square test of independence  
**Result:** p-value < 0.001, significant association  
**Conclusion:** Medium viscosity optimal

**Hypothesis 2: Humidity affects blister rate**

| Humidity | Defect Rate |
|----------|-------------|
| <40% RH | 5% |
| 40-60% RH | 6% |
| >60% RH | 14% |

**Test:** ANOVA  
**Result:** p-value < 0.001  
**Conclusion:** High humidity significantly increases blisters

### Regression Analysis

**Multiple Regression: Defect Rate vs Process Parameters**

Predictors:
- X1: Primer viscosity
- X2: Humidity
- X3: Film thickness
- X4: Flash time
- X5: Gun pressure

Results:
- R² = 78%
- Significant factors: X1 (viscosity), X2 (humidity), X4 (flash time)
- Equation: Defect% = 2.1 + 0.4(X1-22)² + 0.12(X2-50) + 0.8(X4-8)

**Key Insight:**
- Viscosity has quadratic effect (optimal at 22s)
- Humidity linear effect (lower is better)
- Flash time critical (insufficient = blisters)

---

## IMPROVE Phase

### Solution Generation

| Root Cause | Solution | Implementation | Cost |
|------------|----------|----------------|------|
| Viscosity variation | Auto-viscosity control | Install viscometer + controller | $15K |
| High humidity | Dehumidification | Upgrade HVAC | $45K |
| Inconsistent flash time | Timer system | Install flash timers | $5K |
| Operator technique | Standard work | Training + visual aids | $2K |

### Pilot Validation

**Pilot Run:** 2 weeks, 2,000 parts

| Metric | Before | Pilot | Improvement |
|--------|--------|-------|-------------|
| Defect Rate | 8.0% | 1.2% | 85% reduction |
| Blisters | 3.6% | 0.4% | 89% reduction |
| Runs | 2.4% | 0.5% | 79% reduction |

**Statistical Validation:**
- 2-proportion test: p-value < 0.001
- Improvement statistically significant

### Full Implementation

Rollout plan:
- Week 1-2: Install equipment
- Week 3: Train all operators
- Week 4: Run at full production

---

## CONTROL Phase

### Control Plan

| Parameter | Measurement | Frequency | Response |
|-----------|-------------|-----------|----------|
| Defect Rate | Inspection | Every part | Stop if >2% |
| Viscosity | Auto-monitor | Continuous | Alarm if outside 21-23s |
| Humidity | Sensor | Continuous | Alarm if >55% RH |
| Flash Time | Timer | Every load | Alert if <7 min |

### Statistical Process Control

**p-Chart for Defect Rate:**
- Center line: 1.0% (new target)
- UCL: 2.5%
- LCL: 0% (by definition)
- Sample size: n=100 per shift

### Standard Work Documentation

- Updated work instructions
- Visual standard at each station
- Training completed for 12 operators
- Certification test: 100% pass rate

---

## RESULTS

### Performance Improvement

| Metric | Before | After | Savings |
|--------|--------|-------|---------|
| Defect Rate | 8.0% | 0.9% | - |
| Scrap Cost | $1.8M/yr | $200K/yr | $1.6M |
| Rework Cost | $600K/yr | $100K/yr | $500K |
| **Total** | **$2.4M/yr** | **$300K/yr** | **$2.1M/yr** |

### Process Sigma Level

- Before: 2.9σ (80,000 DPMO)
- After: 4.6σ (9,000 DPMO)
- **Improvement: 1.7σ**

### Additional Benefits

- Customer PPM reduced from 8,000 to 900
- Chargebacks eliminated
- Operator morale improved
- Reduced overtime for rework

---

## LESSONS LEARNED

1. **Measurement first:** MSA saved us from chasing false signals
2. **Fishbone focus:** Starting with top defect (blisters) accelerated results
3. **Pilot validation:** Small test prevented full-scale implementation failure
4. **Operator involvement:** Their insights on flash time were critical

---

**Project Closure Date:** 2024-03-15  
**Black Belt:** [Name]  
**Financial Validation:** Finance Manager sign-off completed
