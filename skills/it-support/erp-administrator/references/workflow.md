## § 8 · Standard Workflow

See [references/08-workflow.md](references/08-workflow.md)

---

---

### Phase 2: ERP Go-Live Cutover Management

**Input:** Go-live date, cutover window (start/end times), task list from all workstreams (Basis, Finance, MM/SD, Integration, Data Migration).

**Step 1 — Cutover Runbook Finalization [✓ Done: all tasks sequenced with owner, duration, and dependency; critical path identified]**
Compile the master cutover runbook. Every task has: sequence number, description, owner, predecessors, planned start time, planned duration, completion criteria (not "done" — specific verifiable criteria), and actual completion time (blank until execution). Identify the critical path — the sequence of tasks that determines the minimum cutover duration. All critical path tasks have a named backup owner.
[✗ FAIL: any critical path task with no backup owner; runbook total duration exceeds cutover window by > 10%]

**Step 2 — Go/No-Go Criteria Definition [✓ Done: go/no-go criteria approved by steering committee]**
Define explicit go/no-go criteria for the cutover start decision (is the legacy system successfully frozen?), the midpoint decision (are data migration reconciliation results within tolerance?), and the go-live decision (have all business smoke tests passed?). These criteria are approved by the ERP steering committee before the cutover window opens. Criteria are binary (pass/fail), not subjective.
[✗ FAIL: go/no-go criteria are undefined or require judgment calls during the cutover window]

**Step 3 — Cutover Execution [✓ Done: all tasks completed within window; go/no-go criteria met at each checkpoint]**
Execute the cutover runbook with a dedicated cutover command center (or virtual call) open throughout. Every task completion is recorded in real time with timestamp and owner initials. Deviations from the planned schedule are logged immediately. The cutover manager communicates status updates to the steering committee at each checkpoint. No improvisation — if a task is not in the runbook and is required, it is logged, assessed for impact, and the steering committee decides whether to proceed or delay.
[✗ FAIL: any go/no-go checkpoint fails to meet its defined criteria — execute the rollback plan]

**Step 4 — Hypercare and Stabilization [✓ Done: all hypercare issues logged; P1/P2 issues resolved; system stable for 5 business days]**
Enter hypercare mode for the first 30 days post-go-live. All functional workstream leads are available during business hours. P1 issues (complete business process blockage) are resolved within 4 hours. P2 issues (workaround available) are resolved within 24 hours. P3 issues (cosmetic, no business impact) are logged in the backlog for the first patch release.
[✗ FAIL: any P1 issue open > 4 hours without active bridge call; any data integrity issue discovered post-go-live without immediate escalation to Finance and Internal Audit]

---

