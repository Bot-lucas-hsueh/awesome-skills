## § 7 · Scenario Examples

### Scenario 1: EDC Build for Phase III Trial

**Context**: 500-patient oncology study, 50 sites, 18-month enrollment.

**EDC Development Plan**:
1. **Specifications** (Weeks 1-4):
   - aCRF annotated with SDTM mapping
   - Edit check specifications (200+ checks)
   - Data validation rules
   - Derivation specifications

2. **Build** (Weeks 5-8):
   - Database structure (30+ forms)
   - Edit check programming
   - Derivations and calculations
   - Reporting configuration

3. **UAT** (Weeks 9-10):
   - Test scripts (100+ scenarios)
   - Data entry validation
   - Edit check verification
   - Report accuracy

4. **Training** (Week 11):
   - Site training materials
   - System access provisioning
   - Help desk setup

5. **Go-Live** (Week 12):
   - Site activation phased by readiness
   - First patient in milestone

**Post-Launch**:
- Weekly data quality reports
- Query generation and tracking
- Ongoing user support

---

### Scenario 2: Database Lock Preparation

**Context**: Database lock scheduled in 4 weeks for regulatory submission.

**Pre-Lock Checklist**:

**Data Completeness (Week -4)**:
- [ ] All CRFs entered and complete
- [ ] All external data loaded (central labs, ePRO, imaging)
- [ ] All queries resolved
- [ ] Serious adverse events reconciled with safety database

**Quality Review (Week -3)**:
- [ ] Medical review of safety data complete
- [ ] Statistical review of key variables
- [ ] Outlier investigation documented
- [ ] Protocol deviations coded and categorized

**Programming (Week -2)**:
- [ ] SDTM datasets programmed and validated
- [ ] ADaM datasets programmed and validated
- [ ] Define.xml generated
- [ ] Validation rules executed

**Final Checks (Week -1)**:
- [ ] Medical coding complete (MedDRA, WHODrug)
- [ ] Reconciliation reports clean
- [ ] Audit trail review
- [ ] Database freeze (no new data entry)

**Lock (Week 0)**:
- [ ] Final data extraction
- [ ] Database locked (timestamp recorded)
- [ ] Data archival
- [ ] Notification to study team

---

### Scenario 3: CDISC Conversion

**Context**: Legacy study data needs SDTM conversion for pooled analysis.

**Conversion Process**:
1. **Source Data Review**:
   - Legacy dataset structures
   - Variable mappings needed
   - Controlled terminology gaps

2. **Specification Development**:
   - SDTM IG 3.2 compliance
   - Domain specifications (DM, AE, LB, etc.)
   - Supplemental qualifiers mapping
   - Origin metadata documentation

3. **Programming**:
   - SAS macro development
   - Dataset creation
   - Value-level metadata

4. **Validation**:
   - OpenCDISC validator (errors/warnings/notices)
   - Pinnacle 21 validation
   - Manual review of critical variables

5. **Documentation**:
   - Define.xml generation
   - Reviewer's Guide
   - Data definition tables

**Outcome**: Submission-ready SDTM package with zero validator errors

---

### Scenario 4: Risk-Based Monitoring Implementation

**Context**: Transition from 100% SDV to risk-based approach.

**Risk Assessment**:
1. **Study-Level Factors**:
   - Phase III, known safety profile
   - Objective endpoints (OS, PFS)
   - Central lab assessments

2. **Site-Level Factors**:
   - Historical performance
   - Enrollment rate
   - Query rate
   - Protocol deviation rate

3. **Subject-Level Factors**:
   - Early enrollment (learning curve)
   - Key efficacy endpoints
   - Safety signals

**RBM Strategy**:
- Critical data: 100% source verification
- Key data: Statistical sampling (20%)
- Non-critical: Centralized monitoring only
- Triggered: Additional SDV for anomalies

**Centralized Monitoring**:
- Key risk indicators (KRIs) by site
- Statistical thresholds for review
- Cross-site comparison
- Fraud detection algorithms

---

### Scenario 5: Regulatory Inspection Support

**Context**: FDA Pre-Approval Inspection (PAI) scheduled.

**Inspection Preparation**:
1. **Documentation**:
   - Data management plan
   - CRF completion guidelines
   - Edit check specifications
   - Validation documentation

2. **System Access**:
   - EDC demonstration environment
   - Audit trail reports
   - Query management reports

3. **Staff Preparation**:
   - Interview preparation
   - Process walkthroughs
   - Document location

**During Inspection**:
- Accompanied access to systems
- Document requests fulfilled within SLA
- Clarification of processes
- Observation of audit trail review

**Post-Inspection**:
- Response to observations (483)
- CAPA implementation
- Process improvements

---
