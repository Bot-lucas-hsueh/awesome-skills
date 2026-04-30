## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Automating Broken Processes**

```
❌ BAD: Customer onboarding takes 3 weeks. Team builds an RPA bot to automate
   the 14-step process. Result: wrong outputs produced 10× faster. Customer
   complaints spike. Bot requires constant maintenance. $200K invested; outcome worse.

✅ GOOD: Before automating anything:
   Step 1: Map the process as-is (VSM)
   Step 2: Eliminate NVA steps (reduce 14 → 6 steps)
   Step 3: Test manual To-Be process for 2 weeks
   Step 4: Only automate a validated, clean process
   Rule: Automation amplifies a process's quality — good process → faster; bad process → faster failure.
```

**Anti-Pattern 2: Headcount as Throughput Solution**

```
❌ BAD: Support SLA is being missed. COO says "hire 10 more agents."
   3 months later: more agents, same SLA miss. Root cause was:
   agents spending 40% of time on workarounds for broken internal tools.
   $1.2M in additional salary; problem unchanged.

✅ GOOD: Diagnose root cause before headcount decision.
   Capacity problem = headcount solution
   Process problem = redesign solution
   Tool problem = automation/tooling solution
   Manager problem = org/coaching solution
   Rule: Never solve a process problem with headcount.
```

### 🟡 Medium Severity

**Anti-Pattern 3: OKR as Task List**

```
❌ BAD: Key Result: "Complete 3 training sessions." "Launch new CRM." "Hold 12 town halls."
   These are tasks, not outcomes. 100% completion rate but business unchanged.
   Team celebrates hitting all OKRs; business results are flat.

✅ GOOD: Key Results must be outcomes, not activities.
   ❌ "Launch new CRM" → ✅ "Reduce sales cycle from 45 to 28 days by Q4"
   ❌ "Hold 12 town halls" → ✅ "Employee NPS from +15 to +35"
   Rule: If you can complete the KR without the business changing, it's a task, not a KR.
```

**Anti-Pattern 4: KPI Proliferation**

```
❌ BAD: COO introduces 47 operational KPIs across 8 departments.
   Everyone tracks their own metrics. No one looks at the others.
   Monthly reviews take 4 hours reviewing 47 numbers.
   Leadership can't identify what actually needs attention.

✅ GOOD: 3-5 North Star metrics per team, with at most 2 levels of supporting metrics.
   Each team has: 1 outcome metric (North Star) + 2-3 driver metrics (leading indicators)
   Monthly review should fit on one page: green/yellow/red + action for red items only.
   Rule: If every metric is a priority, none is.
```
