# Templates, Checklists & Protocols

## 10.1 Data Deposit Checklist

### Pre-Deposit
- [ ] Data collection complete and documented
- [ ] Data quality verified (outliers investigated)
- [ ] Sensitive data identified and de-identified or restricted
- [ ] Consent for sharing verified (IRB, informed consent)
- [ ] Rights to share confirmed (no third-party restrictions)
- [ ] File formats validated (open, no corruption)
- [ ] Checksums calculated

### Metadata Creation
- [ ] Title: descriptive and unique
- [ ] Creator(s): names + ORCIDs
- [ ] Publication year
- [ ] Resource type: Dataset
- [ ] Description: abstract ≥200 words
- [ ] Subjects: controlled vocabulary keywords
- [ ] Rights: license selected
- [ ] Identifier: DOI requested

### Quality Check
- [ ] Required DataCite fields complete
- [ ] Schema validation passes
- [ ] Files readable
- [ ] README included
- [ ] Data dictionary complete
- [ ] No PII in public version

## 10.2 README Template

```markdown
# Dataset Title

**DOI:** [DOI]
**Version:** [X.X]
**Published:** [YYYY-MM-DD]

## Investigator
**PI:** [Name, ORCID]
**Institution:** [Name]
**Funder:** [Grant number]

## Dataset Description
[2-3 sentence description]

## Study Information
**Type:** [Clinical trial, observational, etc.]
**IRB:** [Protocol number]

## Data Summary
| File | Description | Records | Variables |
|------|-------------|---------|-----------|
|       |             |         |           |

## Key Findings
[Summary of main findings]

## Restrictions
[Any access limitations or embargo periods]

## Citation
[Standard citation format]

## Acknowledgments
[Acknowledgment text]
```

## 10.3 Data Dictionary Template

| Variable | Label | Type | Values/Codes | Units | Definition |
|----------|-------|------|--------------|-------|------------|
| SUBJID | Subject ID | TEXT | Unique | — | Study identifier |
| AGE | Age | NUM | 18-85 | years | Age at enrollment |
| SEX | Biological Sex | NUM | 1=Male, 2=Female | — | Recorded at screening |

## 10.4 Data Management Plan Template

```
DATA MANAGEMENT PLAN

1. DATA OVERVIEW
   Types: _______________
   Volume: _______________
   Standards: _______________

2. DATA COLLECTION & DOCUMENTATION
   Collection method: _______________
   Documentation: _______________

3. DATA ORGANIZATION & STORAGE
   Organization: _______________
   Backup procedures: _______________

4. ACCESS & REUSE
   Openly available? Yes/No
   License: _______________
   Restrictions: _______________

5. PRESERVATION
   What data: _______________
   Where archived: _______________
   Duration: _______________
```

## 10.5 Curation Quality Checklist

| Check | Status |
|-------|--------|
| DOI assigned and registered | ☐ |
| Landing page accessible | ☐ |
| Required DataCite fields populated | ☐ |
| License clearly stated | ☐ |
| Files downloadable and uncorrupted | ☐ |
| README sufficient for reuse | ☐ |
| No PII in public version | ☐ |
| Related publications linked | ☐ |
