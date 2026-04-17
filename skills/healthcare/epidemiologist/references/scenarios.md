# Scenario Examples

## 9.1 Foodborne Outbreak Investigation

**User:** "Local health department reports 45 people with vomiting and diarrhea after attending a community event. Onset 6-48 hours post-event. How do I investigate this outbreak?"

**Expert:**
> **Outbreak Investigation:**
>
> 1. **Confirm Outbreak**: Verify cases meet case definition; assess if above expected baseline
>
> 2. **Descriptive Epidemiology**:
>    - Create line list: age, sex, symptoms, food items consumed, onset time
>    - Build epidemic curve: expect point source (bell-shaped)
>    - Calculate incubation: 6-48h suggests Staphylococcus aureus (1-6h), Bacillus cereus (1-16h), or Salmonella (6-72h)
>
> 3. **Hypothesis Generation**:
>    - Interview cases about food consumption
>    - Calculate attack rates by food item
>    - Identify most likely vehicle
>
> 4. **Analytical Study**:
>    - Case-control study (food-specific ORs)
>    - Expect high OR for implicated food item
>    - Calculate attributable risk
>
> 5. **Control Measures**:
>    - Proper food handling education
>    - Exclude symptomatic food handlers
>    - Environmental assessment of food source
>
> 6. **Communication**: Report to public health authorities; issue press release if needed

## 9.2 Reproductive Number Estimation

**User:** "Hospital reports increasing COVID-19 admissions over 3 weeks. Day 1: 5 cases, Day 21: 40 cases. How do I estimate R0?"

**Expert:**
> **Reproductive Number Estimation:**
>
> 1. **Calculate Growth Rate (r)**:
>    - Using exponential model: Cases = Cases₀ × e^(rt)
>    - r ≈ (ln(40) - ln(5)) / 21 = 2.77 / 21 = 0.132 per day
>
> 2. **Estimate R0**:
>    - Using generation time Tg ≈ 5 days for COVID
>    - R0 = e^(r×Tg) = e^(0.132 × 5) = e^0.66 = 1.93
>
> 3. **Estimate Rt**:
>    - Use EpiEstim with serial interval distribution
>    - Rt >1 indicates growing epidemic
>
> 4. **Uncertainty Assessment**:
>    - Report 95% CI for R0/Rt
>    - Account for superspreading (dispersion parameter k)
>
> 5. **Interpretation**:
>    - R0 = 1.93 means each case infects ~2 others
>    - Intervention goal: reduce Rt below 1

## 9.3 Vaccine Effectiveness Analysis

**User:** "Nursing home outbreak: 80% of residents vaccinated but 20 still got influenza. Is the vaccine working?"

**Expert:**
> **Vaccine Effectiveness Calculation:**
>
> 1. **Calculate Attack Rates**:
>    - Attack rate in vaccinated: Cases_vac / Total_vac
>    - Attack rate in unvaccinated: Cases_unvac / Total_unvac
>
> 2. **Calculate VE**:
>    - VE = 1 - (Attack rate_vac / Attack rate_unvac)
>    - If AR_vac = 5% and AR_unvac = 25%, VE = 1 - 0.05/0.25 = 80%
>
> 3. **Interpretation**:
>    - VE = 80% means vaccine reduces risk by 80%
>    - Some vaccinated cases expected (not 100% efficacy)
>
> 4. **Limitations**:
>    - Misclassification of vaccination status
>    - Match circulating strain to vaccine strain
>    - Consider underlying health status (frailty)
>
> 5. **Recommendations**:
>    - Continue vaccination efforts
>    - Implement additional infection control measures
>    - Offer antiviral prophylaxis to close contacts
