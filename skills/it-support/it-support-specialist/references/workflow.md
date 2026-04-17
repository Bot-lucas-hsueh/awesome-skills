## § 8 · Standard Workflow

### Phase 1: Intake and Triage

| Step | Activity | Done Criteria [✓] | Fail Criteria [✗] |
|------|----------|-------------------|-------------------|
| 1 | Acknowledge ticket
| 2 | Gather: user, device, OS, error message, reproduction steps, when started, who else affected | All 7 data points captured in ticket | [✗ FAIL] — Starting diagnosis without knowing if multiple users are affected (may be P1 misclassified as P3) |
| 3 | Classify: Incident (unplanned) or Service Request (planned ask) | Classification recorded; correct queue | [✗ FAIL] — SR logged as Incident inflates incident metrics and misroutes |
| 4 | Assign Priority P1–P4 using impact × urgency matrix | Priority set; SLA target noted in ticket | [✗ FAIL] — Default P3 on everything; P1 issues sit in queue |
| 5 | Check Known Error Database and KB | KB match found → apply and cite article; no match → proceed to diagnosis | [✗ FAIL] — Spend 45 min diagnosing a known issue with a documented fix |

**Intake Template (copy into ticket):**
→ See [references/code-block-2.md](references/code-block-2.md)

### Phase 2: Diagnosis and Resolution

| Step | Activity | Done Criteria [✓] | Fail Criteria [✗] |
|------|----------|-------------------|-------------------|
| 1 | Apply systematic elimination (hardware → OS → app → network → identity) | Category narrowed; each eliminated category documented | [✗ FAIL] — Jump to the most familiar fix without ruling out other causes |
| 2 | Test reproduction: does issue occur on another device? another account? | Isolation confirmed; hardware vs. software determined | [✗ FAIL] — Reimage a machine that had a profile corruption fixable in 5 min |
| 3 | Apply fix or workaround; document exact steps and commands in ticket | Resolution steps logged verbatim; user confirms issue resolved | [✗ FAIL] — Fix applied but not documented; next call from same user has no history |
| 4 | Verify fix: ask user to perform their original task successfully | User confirms workflow restored; not just "error gone" | [✗ FAIL] — Close ticket after fix without confirming user can complete their work |
| 5 | Determine escalation need if unresolved after Tier 1 steps | Escalation note includes: issue summary, steps taken, exact output, impact, urgency | [✗ FAIL] — Escalate with "it's broken, please fix" — wasted round-trips |

### Phase 3: Documentation and Follow-up

| Step | Activity | Done Criteria [✓] | Fail Criteria [✗] |
|------|----------|-------------------|-------------------|
| 1 | Write resolution summary in ticket | Clear cause-and-fix summary; reusable by any technician | [✗ FAIL] — "Fixed." as the entire resolution note |
| 2 | Confirm closure with user (email or verbal) | User explicitly confirms issue is resolved before ticket is closed | [✗ FAIL] — Closing ticket without user confirmation; user reopens 2 hours later |
| 3 | Identify KB article opportunity | If no KB article existed → draft one and submit for review | [✗ FAIL] — Solving the same problem for the 5th time with no KB article |
| 4 | Identify problem record need | Recurring issue → open Problem record; link incident tickets | [✗ FAIL] — Treating the 10th occurrence of the same root cause as 10 separate incidents |
| 5 | Close ticket with correct resolution category | Category matches actual fix type; enables trend reporting | [✗ FAIL] — "Other" as resolution category on every ticket |

**Resolution Note Template:**
→ See [references/code-block-2.md](references/code-block-2.md)

---

