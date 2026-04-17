## § 6 · Professional Toolkit

### Sourcing & ATS Platforms
- **LinkedIn Recruiter** — Boolean search, InMail campaigns, talent pipeline building
- **GitHub
- **Greenhouse / Lever
- **HireVue
- **Gem

### Compensation Benchmarking
- **Radford/McLagan** — Tech/financial services compensation surveys
- **Mercer** — Cross-industry compensation data
- **LinkedIn Salary
- **Levels.fyi** — Tech industry equity and total compensation benchmarks

### Reference Standards
- **EEOC Guidelines** — Prohibited interview questions (US)
- **GDPR Article 9** — Special category data handling for candidate records
- **SHRM Competency Model** — Talent acquisition competency benchmarks
- **LinkedIn Talent Insights** — Labor market supply/demand analysis

## Phase 1: Job Intake & Search Strategy (Days 1–3)

```
Job Intake Template:
□ Role title, level (IC3/IC4/Staff/Manager), team, reporting manager
□ Top 3 must-have qualifications (deal-breakers for screening)
□ Top 3 nice-to-have qualifications (differentiate strong from exceptional)
□ 30/60/90 day success metrics ("what does 'great' look like in 3 months?")
□ Compensation band (approved): Base $X–$Y, Equity $Z–$W RSU, Bonus X%
□ Target start date → back-calculate deadline for offer stage
□ Interview panel: who, what each person evaluates, decision authority
□ Culture add: what team dynamics, working style, values matter
□ Red flags specific to this role (not generic)
```

**Boolean Search String Construction:**
```
LinkedIn Recruiter example — Senior Data Engineer:
("data engineer" OR "data platform engineer" OR "analytics engineer")
AND ("Spark" OR "Databricks" OR "dbt" OR "Snowflake")
AND ("Python" OR "Scala")
NOT ("junior" OR "intern" OR "entry")

GitHub sourcing: language:Python location:San Francisco followers:>50
  → Find active open-source contributors

Diversity sourcing: Post on Lesbians Who Tech, Blacks in Technology,
  Women Who Code; target HBCUs and HSIs for campus recruiting
```

✓ Intake form completed and signed off by hiring manager
✓ Compensation band confirmed with HR/comp team
✓ Interview panel identified with schedules blocked
✗ Do not open requisition without approved headcount and comp band

### Phase 2: Sourcing, Screening & Pipeline (Days 4–21)

**Phone Screen Framework (30 min):**
```
Opening (5 min):
- Build rapport; set agenda ("I'll ask you a few questions, then leave time for yours")
- Confirm current role, location, visa/authorization status

Motivation (5 min):
- "What's prompting you to explore new opportunities now?"
- "What does your ideal next role look like?"

Qualification check (10 min) — 3 must-have skills:
- For each: "Tell me about your experience with [must-have]. What was your role and the outcome?"
- Apply STAR probe: Situation → Task → Action → Result (quantified)

Logistics (5 min):
- Current
- Notice period, relocation, start date flexibility
- Other active processes (multiple offers = urgency signal)

Close (5 min):
- Pitch the role (3 unique value propositions)
- "On a scale of 1-10, how interested are you after this call? What would make it a 10?"
- Set clear next step with specific timeline
```

**Scorecard Design:**
```
Competency        | Weight | Interviewer | Pass Criteria
Technical skill A | 30%    | Eng mgr     | Demonstrates X at target level (example rubric)
Technical skill B | 20%    | Sr IC       | Can solve Y type problem independently
Collaboration     | 20%    | PM          | Evidence of cross-functional impact
Problem-solving   | 15%    | HM          | Structured reasoning under ambiguity
Culture add       | 15%    | Panel       | Brings perspective team currently lacks

Hire thresholds: ≥4/5 on all weighted scores; no "Strong No" from any interviewer
```

✓ ≥10 qualified candidates sourced per week for specialist roles
✓ Phone screen notes documented in ATS within 24h
✓ Candidates moved or rejected within 5 business days (candidate experience)
✗ Do not advance candidate with a "Strong No" from any panel member

### Phase 3: Offer Construction & Close (Days 22–30)

```python
# Compensation package analysis
def build_offer_summary(candidate_current, market_p50, market_p75, budget_max):
    """
    Structure a competitive offer and anticipate counter.
    market_p50: median for this role/level in this market
    market_p75: 75th percentile (stretch target)
    budget_max: hiring manager approved max
    """
    target_base = min(market_p75 * 0.95, budget_max)  # Aim slightly below P75, within budget
    counter_reserve = budget_max - target_base          # Reserve for counter-offer

    total_comp_offer = target_base + (equity_value

    return {
        'offer_base': target_base,
        'vs_current': f"{((target_base - candidate_current)/candidate_current * 100):.0f}% increase",
        'vs_market_p50': f"{((target_base - market_p50)/market_p50 * 100):.0f}% above market",
        'counter_reserve': counter_reserve,
        'recommendation': 'Lead with $X; prepare to move to $Y if counter',
    }

# Offer close sequence:
# Day 0: Verbal offer call (hiring manager + recruiter) — make it personal
# Day 1: Written offer letter with 72-hour response window
# Day 3: Check-in call "Do you have any questions about the offer?"
# Day 5: Counter-offer management if needed
# Reneges: ~7% rate; reduce by pre-boarding manager call on acceptance day
```

✓ Offer competitive vs. market data (within P50–P75 for level)
✓ Verbal offer call before written offer (not email-only)
✓ Counter-offer response prepared before call
✗ Never pressure candidate with artificial deadlines < 48 hours

## 🔬 Scenario Examples

### 🚫 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Writing Job Descriptions as Wish Lists
**Wrong:** "Requirements: 10+ years Python, 7+ years Java, 5+ years Kubernetes, PhD preferred, ML experience..."
**Why it fails:** Overloaded JDs filter out qualified candidates (particularly women who don't apply unless meeting 90%+ of criteria vs. men who apply at 60%). Time-to-fill increases; diversity decreases.
**Correct:** Separate must-have (≤5 criteria) from nice-to-have. Lead with impact ("you'll own X, which drives Y") not requirements. Use inclusive language (avoid "ninja," "rockstar," "aggressive").

### Anti-Pattern 2: Single-Threading (Only One Finalist)
**Wrong:** Identify one exceptional candidate early, stop sourcing, advance to final.
**Why it fails:** If that candidate declines or accepts another offer, the pipeline is empty. Average restart time: 3–6 weeks. Role stays open.
**Correct:** Always maintain ≥3 qualified candidates in parallel. Don't stop sourcing until offer accepted and background check passed.

### Anti-Pattern 3: Skipping Reference Checks
**Wrong:** Fast-track reference checks or skip when hiring manager is eager to close.
**Why it fails:** References reveal performance issues, management style problems, and culture fit red flags that interviews miss. A bad hire at senior level costs $500K–$1.5M in recruitment + productivity + severance.
**Correct:** Always complete ≥2 references, at least 1 direct supervisor. Ask: "On a scale of 1-10, would you re-hire? What would make it a 10?" — the hesitation between 7 and 8 is the most revealing data.

### Anti-Pattern 4: Ignoring Candidate Experience for Rejected Candidates
**Wrong:** No-reply ATS rejection email weeks after phone screen; leaving candidates in "under review" limbo.
**Why it fails:** Rejected candidates become ambassadors or adversaries on Glassdoor. Poor candidate experience reduces future applicant pool and employer brand NPS.
**Correct:** Respond to all applications within 5 business days (even if automated). Provide brief human feedback to all phone-screened candidates. Close every open req status within 2 business days of a hire decision.

### Anti-Pattern 5: Comp Anchoring Too Early in Process
**Wrong:** "What is your current salary?" as first phone screen question; anchoring offer to prior salary.
**Why it fails:** Perpetuates pay inequity (EEOC risk in many jurisdictions); anchors offer below market; illegal in CA, NY, WA, and other states.
**Correct:** Share compensation band upfront ("We're targeting $150K–$180K base for this role — does that align with your expectations?"). Never ask for prior salary in states/jurisdictions where prohibited.

