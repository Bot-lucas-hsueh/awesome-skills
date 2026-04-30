# markdown Example

```


# Incident Post-Mortem: [Short Title]

## Summary
One-paragraph description of the incident.

## Timeline
| Time (UTC) | Event |
|------------|-------|
| HH:MM | Event 1 |
| HH:MM | Event 2 |

## Root Cause
Technical explanation of what went wrong.

## Impact
- Duration: X hours Y minutes
- Users Affected: N
- Services Impacted: A, B, C

## Resolution
Steps taken to resolve the incident.

## Action Items
{{jiraissues: filter="labels = incident-YYYY-MM-DD"}}

## Lessons Learned
- [ ] Lesson 1
- [ ] Lesson 2

## Related Pages
- Runbook that failed: [[Space:Page Name]]
- Monitoring: [[Space:Page Name]]
```
