## § 8 · Standard Workflow

### Phase 1: Analysis Setup

| Step | Activity | Done Criteria | Fail Criteria |
|------|----------|---------------|---------------|
| 1 | Business question framing | "What decision does this analysis support?" answered | "Let's look at the data and see what we find" |
| 2 | Data quality check | Null rates, duplicates, row counts, date gaps verified | Skip QC; assume data is clean |
| 3 | Metric definition | Primary metric + guardrails defined and agreed | Metric ambiguity ("engagement" without definition) |
| 4 | Methodology selection | Appropriate statistical method chosen with rationale | Default to means without checking distribution |
| 5 | Hypothesis statement | If experiment: null/alt hypothesis pre-registered | Analyze first; form hypothesis after seeing data |

### Phase 2: Analysis Execution & Communication

| Step | Activity | Done Criteria | Fail Criteria |
|------|----------|---------------|---------------|
| 1 | EDA complete | Distributions, correlations, outliers documented | Jump to conclusions without EDA |
| 2 | Statistical analysis | Test run with assumptions verified (normality, independence) | Run test without checking assumptions |
| 3 | Effect size reported | Cohen's d
| 4 | Segment analysis | Results broken down by key segments | Aggregate only; Simpson's Paradox risk |
| 5 | Business narrative | "Because of X, we recommend Y" in non-technical language | Data dump without recommendation |

---

