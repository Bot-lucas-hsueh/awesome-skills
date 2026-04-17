## § 8 · Standard Workflow

### Phase 1: Statistical Design Consultation

| Step | Activity | Done Criteria | Fail Criteria |
|------|----------|---------------|---------------|
| 1 | Research question clarification | Estimand defined (what quantity are we estimating?) | "Analyze the data and find something interesting" |
| 2 | Primary endpoint pre-specification | Primary outcome declared before data collection | Multiple endpoints; "we'll see what's significant" |
| 3 | Method selection | Method justified by: outcome type, design, sample size, distribution | Default t-test for everything |
| 4 | Power analysis | Sample size calculated with effect size, α, and power specified | "We'll use n=50 because that's what we can afford" without power justification |
| 5 | Analysis plan document | Written statistical analysis plan (SAP) before data collection | No SAP; decisions made after seeing data |

### Phase 2: Analysis Execution & Reporting

| Step | Activity | Done Criteria | Fail Criteria |
|------|----------|---------------|---------------|
| 1 | Assumption verification | Normality (Shapiro-Wilk), homoscedasticity (Levene's), independence checked | Run test without checking assumptions |
| 2 | Descriptive statistics | Mean±SD (or median [IQR]), n, % for key variables | Analysis without descriptives |
| 3 | Primary analysis | Pre-specified method applied to pre-specified primary outcome | Run 5 methods; report only the significant one |
| 4 | Effect size + CI | Cohen's d / OR / HR
| 5 | Multiple testing correction | Bonferroni or FDR applied for multiple comparisons | Run 20 tests; report 1 significant; no correction |

---

