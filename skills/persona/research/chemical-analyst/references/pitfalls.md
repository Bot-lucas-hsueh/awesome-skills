# Templates, Checklists & Protocols

## 10.1 Method Validation Protocol Template

```
METHOD VALIDATION PROTOCOL

Method Name: _____________________
Method Number: ____________________
Revision: _____________________
Date: _____________________

1. PURPOSE
   [Brief statement of validation purpose]

2. SCOPE
   [Analytes, matrix, concentration range]

3. REFERENCE STANDARDS
   [ICH Q2(R1), USP <1225>, or other applicable standard]

4. VALIDATION PARAMETERS

4.1 Specificity
   - Test interference from: [list]
   - Acceptance: [criteria]
   - Method: [describe approach]

4.2 Linearity
   - Range: [X to Y units]
   - Number of standards: [n ≥ 5]
   - Acceptance: R² ≥ [0.999]
   - Method: [least squares, weighting]

4.3 Accuracy
   - Matrix: [matrix type]
   - Spike levels: [LOQ, mid, high]
   - Replicates: [n ≥ 6 at each level]
   - Acceptance: Recovery 85-115%

4.4 Precision
   - Repeatability: [n ≥ 6]
   - Intermediate precision: [n ≥ 6, different days/analysts]
   - Acceptance: RSD ≤ [2%]

4.5 LOD/LOQ
   - Method: [S/N, SD method]
   - Acceptance: LOQ validated at [X units]

4.6 Range
   - Confirmed linear range: [LOQ to X]
   - Validated at: [X, Y, Z units]

5. ACCEPTANCE CRITERIA SUMMARY
   | Parameter    | Criterion              |
   |--------------|------------------------|
   | Specificity  | Resolution ≥ 1.5       |
   | Linearity    | R² ≥ 0.999            |
   | Accuracy     | Recovery 85-115%       |
   | Precision    | RSD ≤ 2%              |
   | LOD          | S/N ≥ 3:1             |
   | LOQ          | S/N ≥ 10:1; RSD ≤ 20%|

6. DOCUMENTATION REQUIREMENTS
   - Raw data included: [ ]
   - Calculations shown: [ ]
   - Deviation log: [ ]
```

## 10.2 Instrument Calibration Checklist

### Daily Checks
- [ ] Warm up instrument per manufacturer specification
- [ ] Verify system readiness (pressure within range, baseline stable)
- [ ] Run system suitability test (SST): resolution, tailing, RSD
- [ ] Verify SST results against acceptance criteria
- [ ] Record: Instrument ID, Date, Operator, SST results
- [ ] If SST fails: DO NOT proceed → troubleshoot → re-verify

### Weekly/Monthly Checks
- [ ] Full calibration with certified reference standard
- [ ] Second-source verification (ICV)
- [ ] Blank analysis to confirm no carryover
- [ ] Column performance check
- [ ] Detector performance verification
- [ ] Update calibration log

## 10.3 Sample Analysis Batch Template

```
ANALYTICAL BATCH RECORD

Batch ID: ____________________
Analysis Date: ____________________
Analyst: ____________________
Instrument ID: ____________________
Method: ____________________
Column: ____________________

SAMPLES:
| Sample ID | Description | Matrix | Volume/Weight | Receipt Date |
|-----------|-------------|--------|--------------|--------------|
|           |             |        |              |              |
|           |             |        |              |              |
|           |             |        |              |              |

QC SAMPLES:
| QC Type | ID | Concentration | Acceptance Criteria |
|---------|----|---------------|-------------------|
| Blank   |    | N/A           | <LOQ              |
| LCS     |    | ___ units     | 85-115%           |
| Duplicate|   | ___ units     | RPD ≤20%          |
| Matrix Spike| | ___ units     | 75-125%           |

CALIBRATION:
| Standard Level | Concentration | Response |
|----------------|---------------|----------|
| Level 1        |               |          |
| Level 2        |               |          |
| Level 3        |               |          |
| Level 4        |               |          |
| Level 5        |               |          |
Calibration equation: ____________________
R² = _______

RESULTS:
| Sample ID | Analyte | Result | Units | QC Status |
|-----------|---------|--------|-------|-----------|
|           |         |        |       | Pass/Fail |
|           |         |        |       | Pass/Fail |

Deviations from method: ____________________
Notes: ____________________
```

## 10.4 Corrective Action Report Template

```
CORRECTIVE ACTION REPORT

CAR Number: ____________________
Date Opened: ____________________
Date Closed: ____________________
Analyst: ____________________
Instrument/Method: ____________________

NON-CONFORMANCE DESCRIPTION:
[Detailed description of problem observed]

INVESTIGATION:
[Root cause analysis — 5 Whys or fishbone]

POSSIBLE CAUSES EVALUATED:
| Cause          | Evidence For | Evidence Against | Conclusion |
|----------------|--------------|-----------------|------------|
|                |              |                 |            |
|                |              |                 |            |

CORRECTIVE ACTION TAKEN:
[Specific steps to fix the problem]

PREVENTIVE ACTION:
[Steps to prevent recurrence]

IMPACT ASSESSMENT:
□ Affected results require re-analysis
□ Affected results reported with caveat
□ No impact on reported results
□ Regulatory notification required

BATCHES AFFECTED:
[List affected sample batches]

VERIFICATION:
Verified by: ____________________ Date: ____________________
Effectiveness check date: ____________________
```

## 10.5 Sample Receipt and Login Checklist

- [ ] Verify sample integrity (container intact, no leakage)
- [ ] Confirm sample matches chain of custody documentation
- [ ] Check sample labeling matches submission form
- [ ] Record sample receipt date and time
- [ ] Verify hold time requirements can be met
- [ ] Check sample preservation is appropriate
- [ ] Assign unique laboratory ID
- [ ] Enter into LIMS with all required fields
- [ ] Verify sufficient sample volume/weight for requested analyses
- [ ] Note any discrepancies on submission form
- [ ] Store samples under appropriate conditions (refrigerated/frozen)
- [ ] Communicate any issues to project manager within 24 hours
