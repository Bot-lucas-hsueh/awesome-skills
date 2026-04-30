# Common Workflow Issues & Troubleshooting

## 8.1 Data Quality Issues

| Problem | Symptom | Cause | Solution |
|---------|---------|-------|----------|
| **Inconsistent values** | "Male", "M", "male", "1" | Free-text entry | Implement controlled vocabulary; normalize during ingest |
| **Missing required fields** | Blank Creator, Title | Incomplete submission | Validation rules; rejection workflow |
| **Duplicate records** | Same dataset twice | Multiple submissions | Deduplication algorithm; ORCID matching |
| **Encoding issues** | Gibberish characters | Wrong encoding (UTF-8 vs Latin-1) | Normalize to UTF-8; document original |
| **Outlier values** | Impossible entries | Data entry error | Statistical outlier detection; flag for review |

## 8.2 Metadata Quality Issues

| Issue | Impact | Detection | Resolution |
|-------|--------|----------|-----------|
| Missing required fields | Cannot register DOI | Schema validation | Request completion |
| Inconsistent vocabulary | Poor discoverability | Term frequency | Map to controlled vocabulary |
| Generic title | Undiscoverable | Title length <30 chars | Require descriptive titles |
| Missing units | Data misinterpreted | Variable lacks units | Standardize to SI units |

## 8.3 Sensitive Data Handling Workflow

```
Step 1: Sensitivity Assessment
├── Scan for direct identifiers (names, IDs, SSN)
├── Check quasi-identifiers (ZIP+date+sex can identify ~60%)
├── Assess re-identification risk
└── Level: Public / Controlled / Restricted

Step 2: Remediation
├── Public: No PII, anonymized, aggregate
├── Controlled: Data access agreement required
└── Restricted: Metadata only; data via application

Step 3: De-identification
├── Remove direct identifiers
├── Generalize quasi-identifiers
├── Apply k-anonymity or l-diversity
└── Verify re-identification risk <0.05

Step 4: Access Control
├── Embargo if needed
├── Data access committee review
├── Data use agreement execution
└── Track access for audit
```

## 8.4 Repository Ingest Troubleshooting

| Issue | Symptom | Solution |
|-------|---------|----------|
| Large file upload fails | Timeout, reset | Chunk upload; reduce size |
| Format not supported | "Unknown file type" | Convert to supported format |
| Zip corruption | Extraction errors | Recompress; avoid nested zips |
| DOI not registering | Registration fails | Check DataCite requirements |

## 8.5 Version Control Problems

| Problem | Approach |
|---------|---------|
| Overwrite original data | Create new version with number |
| Lost version history | Implement immutable storage; audit trail |
| Citation of wrong version | Require version ID; persistent URLs per version |
| Orphan versions | Link all versions; maintain relationships |
