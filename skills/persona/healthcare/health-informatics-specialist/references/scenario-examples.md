## § 7 · Scenario Examples

### Scenario 1: EHR Optimization Project

**Context**: Physician burnout high; EHR satisfaction at 25th percentile.

**Assessment**:
1. **Time Analysis**: 2 hours documentation per 8 hours patient care
2. **Pain Points**: Excessive clicking, redundant data entry, alert fatigue
3. **Workflow Observations**: Inefficient rooming, documentation burden

**Interventions**:
1. **Smart Phrases**: 50 most common diagnoses with pre-populated text
2. **Order Sets**: Specialty-specific order sets (cardiology, orthopedics)
3. **Team Documentation**: Scribes, MA rooming enhancement
4. **Alert Tuning**: Reduce alerts from 50/day to 10/day (high-value only)
5. **InBasket Management**: Team-based triage, auto-routing

**Results**:
- Documentation time: -30%
- EHR satisfaction: 65th percentile
- Physician burnout: Reduced 20%
- Alert override rate: From 95% to 15%

---

### Scenario 2: Clinical Decision Support Implementation

**Context**: Hospital-acquired VTE rates above benchmark.

**Intervention**: VTE Prophylaxis CDS
1. **Risk Assessment**: Automatic calculation on admission
2. **Alert Logic**:
   - High-risk patient without prophylaxis → Interruptive alert
   - Contraindications documented → No alert
   - Pharmacologic prophylaxis ordered → Passive confirmation
3. **Order Set**: One-click VTE prophylaxis order set
4. **Reporting**: Weekly compliance dashboard

**Implementation**:
- Build and test in sandbox
- Pilot on one unit
- Refine based on feedback
- Rollout hospital-wide

**Results**:
- VTE prophylaxis rate: 65% → 92%
- Hosp-acquired VTE: -40%
- Alert acceptance: 85%

---

### Scenario 3: FHIR-Based App Development

**Context**: Patient-facing app for medication adherence.

**Technical Design**:
1. **FHIR Resources**:
   - MedicationRequest: Current prescriptions
   - Patient: Demographics
   - Observation: Adherence tracking

2. **SMART on FHIR Launch**:
   - EHR-integrated launch
   - OAuth2 authentication
   - Patient context passed

3. **Functionality**:
   - Medication list from EHR
   - Dose reminders
   - Refill alerts
   - Adherence tracking
   - Provider messaging

4. **Security**:
   - HIPAA-compliant hosting
   - Encryption at rest and in transit
   - Audit logging

**Integration**: Epic App Orchard, Cerner Code

---

### Scenario 4: Health Information Exchange

**Context**: Regional HIE to improve care coordination.

**Architecture**:
1. **Exchange Methods**:
   - Query-based: Provider queries HIE for patient records
   - Push-based: ADT notifications trigger record sharing
   - Consumer-mediated: Patient-directed exchange

2. **Content**:
   - CCDA documents
   - Lab results
   - Discharge summaries
   - Imaging reports

3. **Governance**:
   - Data sharing agreements
   - Patient consent management
   - Provider access controls

4. **Technical**:
   - FHIR-based exchange
   - Direct messaging for referrals
   - Master patient index (MPI)

**Outcomes**:
- 95% of hospitals connected
- Reduced duplicate testing: 15%
- ED medication reconciliation improved

---

### Scenario 5: Population Health Analytics

**Context**: ACO needs to improve diabetes management quality scores.

**Data Approach**:
1. **Data Sources**:
   - EHR (clinical data)
   - Claims (cost, utilization)
   - HIE (external encounters)
   - Labs (external results)

2. **Registry Development**:
   - Diabetes cohort identification
   - Risk stratification (high/medium/low)
   - Care gap identification

3. **Analytics**:
   - HbA1c control rates by provider
   - Time to therapeutic control
   - Cost per patient
   - Readmission risk prediction

4. **Interventions**:
   - High-risk care management
   - Provider performance feedback
   - Patient outreach (phone, portal)

**Results**:
- HbA1c control (< 8%): 45% → 68%
- Cost per patient: -12%
- ED visits: -20%

---
