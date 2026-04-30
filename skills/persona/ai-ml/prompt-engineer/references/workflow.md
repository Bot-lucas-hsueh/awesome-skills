## § 8 · Standard Workflow

### Phase 1: Prompt Design & Initial Testing

**Objective**: Deliver a working prompt with measured baseline quality

| Step | Activity | Done Criteria | Fail Criteria |
|------|----------|--------------|---------------|
| 1 | Define success criteria: measurable, specific (e.g., "extracts all 4 fields correctly 95% of time") | Criteria written and agreed before writing any prompt | Vague criteria ("should work well") → unmeasurable; redesign |
| 2 | Collect 20+ representative examples (diverse inputs, edge cases, failure modes) | Examples cover full distribution; reviewed by domain expert | < 10 examples or only easy cases → eval is not representative |
| 3 | Write v1 prompt: role + task + constraints + output format + 3-5 few-shot examples | Prompt passes 70%+ of eval set on first pass | < 50% → revisit task definition or increase few-shot count |
| 4 | A/B test: run 3 prompt variations against the eval set | Best variant identified with quantified improvement | Variations all identical → insufficient exploration |
| 5 | Adversarial testing: 20+ edge cases (empty input, injection attempts, out-of-distribution) | All adversarial inputs handled gracefully | Any injection bypass → add defense layer before production |

### Phase 2: Production Hardening

**Objective**: Production-ready prompt with monitoring and security

| Step | Activity | Done Criteria | Fail Criteria |
|------|----------|--------------|---------------|
| 1 | Token budget analysis: prompt tokens × volume × price = monthly cost | Cost estimate provided and approved | No cost estimate → budget surprise at scale |
| 2 | Output schema validation: JSON parsing, length limits, schema enforcement | 100% schema validation coverage | Any unvalidated output path → production parsing errors |
| 3 | Regression test suite: 50+ cases covering known failure modes | All prior failure modes covered in regression suite | Regression suite < 30 cases → changes will break silently |
| 4 | Production monitoring: alert on format compliance < 95%, hallucination rate spike | Monitoring dashboard live before go-live | No monitoring → problems discovered by users, not you |

---
