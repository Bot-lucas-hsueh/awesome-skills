# Common Pitfalls & Anti-Patterns

## 10.1 Safety-Critical Errors

| # | Pitfall | Severity | Consequence | Prevention |
|---|---------|----------|-------------|------------|
| 1 | Working on live signal without authorization | 🔴 Critical | Train collision, death | Permit and test procedure |
| 2 | Bypassing safety systems | 🔴 Critical | Uncontrolled movement | Never bypass, document all |
| 3 | Inadequate track protection | 🔴 Critical | Worker fatality | Full protection protocol |
| 4 | Improper grounding | 🔴 High | Electrical shock | Verify ground before work |
| 5 | Ignoring alarm conditions | 🔴 Critical | System failure | Always investigate alarms |

## 10.2 Installation Mistakes

| Mistake | Result | Correct Approach |
|---------|--------|------------------|
| Wrong flash rate | Non-compliance | Verify FRA requirements |
| Incorrect approach timing | Unsafe warning | Calculate per track speed |
| Poor wire termination | Failure prone | Torque spec, no twist caps |
| Missing surge protection | Equipment damage | Install proper protection |
| Improper bonding | Signal interference | Follow grounding spec |

## 10.3 Maintenance Errors

| Error | Impact | Mitigation |
|-------|--------|------------|
| Skipping scheduled maintenance | Failures | Strict maintenance schedule |
| Incomplete records | Compliance issues | Detailed log maintenance |
| Using wrong replacement parts | Failures | OEM parts only |
| Improper calibration | Safety issues | Follow calibration procedures |
| No pre-job briefing | Safety gaps | Mandatory safety meeting |

## 10.4 Testing Failures

| Pitfall | Result | Protocol |
|---------|--------|----------|
| Not verifying test equipment | False results | Calibrated test equipment |
| Skipping test steps | Missed defects | Follow test procedure exactly |
| Testing while energized without need | Safety risk | De-energize when possible |
| Not documenting results | No evidence | Complete test records |
| Rushing tests | Errors | Allow adequate time |

## 10.5 Design Errors

| Mistake | Impact | Prevention |
|---------|--------|------------|
| Not considering future expansion | Re-work needed | Plan for growth |
| Ignoring interference | False signals | EMF study |
| Inadequate power margin | Failures | Calculate loads properly |
| Poor cable routing | Damage, failure | Follow standards |
| Missing redundancy | Single point failure | Redundant systems |

## 10.6 Documentation Errors

| Error | Consequence | Best Practice |
|-------|-------------|---------------|
| Missing as-builts | Future confusion | As-built must-match actual |
| Incomplete work orders | Compliance issues | Detail all work |
| Not updating drawings | Wrong information | Update immediately |
| Lost maintenance logs | Liability | Secure digital backup |
| Missing permits | Regulatory issues | Permit tracking system |

## 10.7 Communication Failures

- **Not notifying dispatcher** - Can cause accidents
- **Poor shift handoff** - Issues unresolved
- **Not reporting defects** - Hazards persist
- **Inadequate crew briefing** - Safety incidents
- **Delayed incident reporting** - Regulatory violation

## 10.8 Regulatory Compliance Mistakes

| Violation | Risk | Prevention |
|-----------|------|------------|
| Operating without FRA approval | Criminal liability | Get approval first |
| Skipping inspections | Enforcement action | Schedule inspections |
| Expired certifications | Personal liability | Track expiration dates |
| Missing reports | Civil penalties | Automated reminders |
| Unauthorized modifications | System failure | Follow change process |

## 10.9 Technical Errors

| Problem | Result | Solution |
|---------|--------|----------|
| Wrong relay application | Failure | Match spec sheets |
| Incorrect wire gauge | Overheating | Follow load calculations |
| Poor solder joints | Intermittent | Use proper technique |
| Wrong diode orientation | Damage | Mark polarity clearly |
| Forgotten jumpers | Malfunction | Complete checklist |

## 10.10 Project Management Errors

- **Unrealistic timelines** - Quality shortcuts
- **Insufficient testing time** - Missed defects
- **Poor resource planning** - Delays
- **Scope creep** - Overruns
- **No risk assessment** - Unexpected issues
