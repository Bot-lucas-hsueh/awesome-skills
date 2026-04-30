# X (Twitter) Engineering Workflow

## Daily Workflow (Musk Era)

### Morning (Start 9-10 AM)
1. **Check Metrics** — Review overnight service health
   - Dashboards: Latency, errors, cost
   - On-call alerts: Any unacknowledged pages?
   - Trending issues: Check #incidents channel

2. **Prioritize** — What ships today?
   - Top priority: CEO requests (Musk DMs)
   - Secondary: Feature work
   - Tertiary: Tech debt, optimization

3. **Brief Sync** — If needed (keep under 15 min)
   - Blockers?
   - Cross-team dependencies?
   - Escalations needed?

### Throughout Day
1. **Code** — Ship features, fix bugs
   - No meetings = more coding time
   - Commit early, commit often
   - Small PRs = fast reviews

2. **Review** — Fast code reviews
   - Target: Review within 2 hours
   - Priority: Unblock others
   - Standard: Functionality > style

3. **Deploy** — Continuous deployment
   - Ship when ready (not just at release)
   - Monitor canaries closely
   - Rollback if error rate spikes

4. **Monitor** — Watch dashboards
   - Keep dashboards open
   - Watch for anomalies
   - Proactive incident response

### Evening (End 7-10 PM+)
1. **Ship** — Ensure daily commits
   - Nothing to ship? Fix a bug.
   - Refactor something.
   - Delete unused code.

2. **Document** — Update runbooks
   - Deployed something new? Document it.
   - Fixed an incident? Update playbook.

3. **Plan** — Tomorrow's priorities
   - Quick note on tomorrow's focus
   - Check calendar (hopefully empty)

## Feature Development Flow

```
Idea → Prototype → Ship → Iterate
  ↓        ↓       ↓       ↓
 2hrs    1 day   1 day   Ongoing
```

### Musk-Style Acceleration
- Skip lengthy design docs for small features
- A/B test instead of debating
- Ship to production for real feedback
- Fix forward, don't rollback (unless broken)

### Traditional (Pre-Musk) vs New Flow

| Phase | Pre-Musk | Post-Musk |
|-------|----------|-----------|
| Design | 2-4 weeks | 2-4 hours |
| Review | Multiple rounds | Ship first |
| Testing | Comprehensive | Canary in prod |
| Deploy | Weekly batch | Continuous |
| Feedback | User research | Production metrics |

## Incident Response

### Severity Levels
| Level | Impact | Response | Examples |
|-------|--------|----------|----------|
| SEV1 | Platform down | All hands | Can't tweet, timeline 500s |
| SEV2 | Major feature broken | Team lead | Search down, DMs broken |
| SEV3 | Minor degradation | On-call | Slow timelines, partial outage |
| SEV4 | Cosmetic issues | Backlog | UI glitches, minor bugs |

### Response Steps (SEV1/2)
1. **Detect** — Alert fires, page received
2. **Ack** — Acknowledge within 5 minutes
3. **Assess** — Impact and scope
4. **Mitigate** — Fix or rollback (target: 15 min)
5. **Communicate** — Status update to #incidents
6. **Resolve** — Service restored
7. **Learn** — Brief postmortem within 24h

### Communication Template
```
[INCIDENT] Timeline Service Degraded

Impact: 5% of users seeing slow timelines
Started: 14:32 UTC
Status: Investigating

Updates:
14:35 - On-call investigating
14:45 - Root cause identified: cache overload
14:55 - Mitigation deployed
15:10 - Resolved, monitoring
```

## "Hardcore" Work Patterns

### Expectations
- 60-80 hour weeks during critical periods
- Daily shipping (no zero-commit days)
- Own services end-to-end (no handoffs)
- On-call rotations (24/7 responsibility)
- In-office presence (no permanent remote)

### Success Metrics
| Metric | Good | Great | Exceptional |
|--------|------|-------|-------------|
| Features/week | 2 | 5 | 10 |
| Incidents caused | <2/quarter | 0 | 0 |
| Cost reduction | 10% | 25% | 50% |
| Code deleted | 100 lines | 500 lines | 1000+ lines |
| System availability | 99.9% | 99.95% | 99.99% |

### Survival Strategies
1. **Automate everything** — No manual toil
2. **Delete code** — Less code = less bugs
3. **Simple solutions** — Complex = failure
4. **Fast feedback** — Ship fast, learn fast
5. **Cost awareness** — Every $ matters
6. **Health maintenance** — Burnout helps no one

## Meeting Culture (Post-Musk)

### Meeting Rules
1. **Default: No meetings**
   - Most communication async
   - Write docs, don't present

2. **If meeting required:**
   - Under 15 minutes
   - Clear agenda
   - Decision maker present
   - Stand-up (no chairs)

3. **Meeting Alternatives:**
   - Doc comments
   - Slack threads
   - Video messages
   - Code review comments

### Meeting Types That Survived
- **Daily standup** — Optional, <15 min
- **Incident response** — As needed
- **Musk reviews** — Unscheduled, mandatory
- **All-hands** — Monthly, information only

## Deployment Workflow

### Standard Deploy
```
1. PR approved → Merge to main
2. CI builds artifact
3. Auto-deploy to staging
4. Canary: 1% for 10 minutes
5. Monitor error rate/latency
6. If healthy: 5% → 25% → 100%
7. If unhealthy: Auto-rollback
```

### Emergency Deploy
```
1. PR approved (1 reviewer ok)
2. Skip staging
3. Canary: 1% for 5 minutes
4. Fast rollout if healthy
5. All-hands on deck during deploy
```

### Rollback Criteria
- Error rate >0.5%
- Latency p99 >2x baseline
- Feature not working
- User complaints spike

## Creator Economy Workflow

### Creator Feature Development
```
1. Identify creator pain point
2. Prototype monetization feature
3. Beta with top creators
4. Measure creator earnings
5. Iterate based on feedback
6. Roll out broadly
7. Monitor creator retention
```

### Success Metrics for Creator Features
- Creator sign-ups
- Revenue per creator
- Content volume increase
- User engagement with creator content
- Creator retention rate

### X Premium Integration
- Features require Premium for monetization
- Track Premium conversion rates
- Monitor revenue pool growth
- Balance free vs paid features

## Community Notes Workflow

### Contributor Onboarding
1. Verify phone number
2. 6 months on platform minimum
3. No recent violations
4. Rate training notes
5. Unlock note-writing

### Note Lifecycle
```
Post published
    ↓
Contributor writes note
    ↓
Other contributors rate
    ↓
Bridging algorithm runs
    ↓
┌─────────┴─────────┐
↓                   ↓
Helpful          Not Helpful
(Shown)          (Hidden)
    ↓
Public sees note
```

### Quality Control
- Rating impact scores
- Writing impact scores
- Algorithmic demotion of low-quality contributors
- Periodic contributor purge

## AI Integration Workflow (Grok Era)

### Grok Feature Development
1. Define use case (chat, search, content)
2. Design prompt engineering
3. Implement with xAI API
4. A/B test engagement
5. Monitor for hallucinations
6. Iterate on prompts

### AI Safety Checklist
- [ ] Hallucination rate measured
- [ ] Harmful content filtered
- [ ] User controls provided
- [ ] Transparency on AI-generated content
- [ ] Feedback mechanism for bad outputs

## Post-Acquisition Survival Guide

### Week 1-2: Assessment
- Understand your service costs
- Identify technical debt
- Meet your users (if any left)
- Find quick wins

### Month 1: Ship Something
- Deliver visible improvement
- Demonstrate "hardcore" commitment
- Build relationships with survivors
- Learn the new tools

### Month 3: Optimize
- Reduce service costs
- Delete unused code
- Improve reliability
- Show ROI

### Month 6+: Lead
- Mentor new hires
- Drive major initiatives
- Influence architecture decisions
- Thrive in chaos

### Warning Signs (Start Updating Resume)
- Multiple missed ship dates
- Service repeatedly fails
- Cost overruns
- Conflict with Musk or inner circle
- Lack of "hardcore" commitment questioned
