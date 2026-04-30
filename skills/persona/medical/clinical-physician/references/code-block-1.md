# python Example

```
def bayesian_update(pretest_probability, sensitivity, specificity, test_positive=True):
    """
    Bayesian diagnostic reasoning: update pre-test to post-test probability.
    LR+ = sensitivity
    LR- = (1 - sensitivity)
    Post-test odds = pre-test odds × LR
    """
    pretest_odds = pretest_probability
    LR_pos = sensitivity
    LR_neg = (1 - sensitivity)
    LR = LR_pos if test_positive else LR_neg
    posttest_odds = pretest_odds * LR
    posttest_prob = posttest_odds
    return {
        'LR_positive': round(LR_pos, 2),
        'LR_negative': round(LR_neg, 3),
        'LR_applied': round(LR, 2),
        'posttest_probability': round(posttest_prob, 3),
        'interpretation': (
            'Strongly rules IN' if LR > 10 else
            'Moderately rules IN' if LR > 5 else
            'Slightly rules IN' if LR > 2 else
            'Strongly rules OUT' if LR < 0.1 else
            'Moderately rules OUT' if LR < 0.2 else 'Minimal change'
        )
    }

def heart_score(history, ecg, age, risk_factors, troponin):
    """
    HEART Score for major adverse cardiac events (MACE) in 6 weeks.
    Each component scored 0-2.
    history: 0=slightly suspicious, 1=moderately suspicious, 2=highly suspicious
    ecg: 0=normal, 1=non-specific repolarization, 2=significant ST deviation
    age: 0=<45, 1=45-65, 2=>65
    risk_factors: 0=no known RF, 1=1-2 RFs or DM/obesity, 2=≥3 RFs or atherosclerosis
    troponin: 0=≤normal limit, 1=1-3× normal, 2=>3× normal
    """
    total = history + ecg + age + risk_factors + troponin
    if total <= 3:
        risk = 'LOW (MACE risk 1.7% → early discharge + outpatient follow-up)'
    elif total <= 6:
        risk = 'MODERATE (MACE risk 12% → observation, serial troponins)'
    else:
        risk = 'HIGH (MACE risk 65% → early invasive strategy)'
    return {'HEART_score': total, 'risk': risk}

def wells_pe_score(dvt_signs, pe_primary_dx, hr_gt100, immobilization,
                   prior_dvt_pe, hemoptysis, malignancy):
    """
    Wells PE Score — clinical pre-test probability for pulmonary embolism.
    """
    score = (dvt_signs * 3.0 + pe_primary_dx * 3.0 + hr_gt100 * 1.5 +
             immobilization * 1.5 + prior_dvt_pe * 1.5 + hemoptysis * 1.0 + malignancy * 1.0)
    if score < 2:
        prob = 'LOW (PE prevalence ~3.6%) → D-dimer; CTPA if positive'
    elif score <= 6:
        prob = 'MODERATE (PE prevalence ~20.5%) → D-dimer or CTPA'
    else:
        prob = 'HIGH (PE prevalence ~66.7%) → CTPA immediately; anticoagulate if no contraindication'
    return {'wells_score': score, 'probability': prob}

# Example: HEART score for ACS evaluation
result = heart_score(history=2, ecg=1, age=2, risk_factors=2, troponin=0)
# Score 7 → HIGH MACE risk 65% → early invasive strategy

# Diagnostic test example: D-dimer for PE
# Sensitivity 95%, Specificity 40%, pre-test probability 20%
bayes_neg = bayesian_update(0.20, sensitivity=0.95, specificity=0.40, test_positive=False)
# LR- = 0.05/0.60 = 0.125 → post-test prob 3% → effectively rules out PE if negative
```
