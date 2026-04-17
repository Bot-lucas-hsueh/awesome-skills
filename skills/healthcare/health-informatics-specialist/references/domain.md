## § 6 · Domain Knowledge

### Clinical Decision Support Architecture

```
Data Input
├── Patient demographics
├── Problem list
├── Medications
├── Allergies
├── Lab results
├── Vital signs
└── Documentation

Rules Engine
├── Arden Syntax
├── GEM (Guideline Element Model)
├── Custom logic (if-then)
└── Machine learning models

Intervention
├── Hard stop (cannot proceed)
├── Interruptive alert (must acknowledge)
├── Passive alert (visible but not blocking)
└── Informational (reference)

Action
├── Order suggestion
├── Documentation prompt
├── Reference information
└── Care team notification
```

### FHIR Resource Examples

| Resource | Description | Key Elements |
|----------|-------------|--------------|
| **Patient** | Demographics | name, birthDate, gender, address |
| **Observation** | Measurements | code, value, effectiveDateTime |
| **Condition** | Diagnoses | code, clinicalStatus, onsetDate |
| **MedicationRequest** | Prescriptions | medication, dosageInstruction |
| **AllergyIntolerance** | Allergies | code, criticality, reaction |
| **Encounter** | Visits | status, class, period, location |

### Quality Measure Calculation

**eCQM (electronic Clinical Quality Measures)**:
```
Measure Components:
├── Initial population: Who is being measured?
├── Denominator: Subset of initial population
├── Numerator: Those meeting criteria
├── Denominator exclusions: Remove from denominator
├── Denominator exceptions: Legitimate reasons not met
└── Stratification: Subgroups of interest

Example: Diabetes HbA1c Control (< 8%)
- Initial: Diabetes patients 18-75
- Denominator: Same as initial
- Numerator: Most recent HbA1c < 8%
- Exclusion: Hospice, pregnancy
- Exception: Patient refusal
```

---
