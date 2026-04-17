## § 6 · Domain Knowledge

### EDC Design Best Practices

```
CRF Design Principles:
1. Match protocol schedule of assessments
2. Use CDASH standards where applicable
3. Implement edit checks (range, logic, consistency)
4. Enable partial saves to prevent data loss
5. Design for user efficiency (auto-calculations, defaults)
6. Include query text for common issues
7. Plan for mid-study amendments

Edit Check Examples:
- Range checks: Systolic BP 70-250 mmHg
- Logical checks: If AE = "Death", then outcome = "Fatal"
- Cross-form: If pregnancy test = "Positive", contraception required
- Date sequence: Informed consent ≤ Visit 1 ≤ Visit 2
```

### SDTM Domain Structure

| Domain | Description | Key Variables |
|--------|-------------|---------------|
| **DM** | Demographics | USUBJID, AGE, SEX, RACE, ARM |
| **AE** | Adverse Events | USUBJID, AETERM, AESTDTC, AESEV, AESER |
| **LB** | Laboratory | USUBJID, LBTEST, LBORRES, LBORRESU, LBNRIND |
| **VS** | Vital Signs | USUBJID, VSTEST, VSORRES, VSORRESU, VSBLFL |
| **CM** | Concomitant Meds | USUBJID, CMTRT, CMSTDTC, CMENDTC, CMDOSE |
| **MH** | Medical History | USUBJID, MHTERM, MHBODSYS, MHENRF |
| **EX** | Exposure | USUBJID, EXTRT, EXDOSE, EXSTDTC, EXENDTC |
| **DS** | Disposition | USUBJID, DSTERM, DSCAT, DSDECOD |

### Query Management Workflow

```
1. Data Review
   ├── Automated edit check generation
   ├── Manual data review by DM
   └── Medical monitor review (safety)

2. Query Generation
   ├── Draft query with specific question
   ├── Assign priority (Critical/High/Medium/Low)
   └── Route to site via EDC or site communication

3. Site Response
   ├── Site investigates source data
   ├── Provides clarification or correction
   └── Response within defined timeframe

4. Query Resolution
   ├── DM reviews response
   ├── Approves correction or re-queries
   └── Closes query when resolved

5. Metrics Tracking
   ├── Query rate by site/form
   ├── Response time tracking
   └── Outstanding query reports
```

---
