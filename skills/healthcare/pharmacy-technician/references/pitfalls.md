## 10. Common Pitfalls & Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **Bypassing pharmacist verification** | 🔴 High | Never dispense without pharmacist initials — it's illegal and dangerous |
| 2 | **Not verifying patient identity** | 🔴 High | Always ask for ID — wrong patient gets wrong medication |
| 3 | **Processing incomplete prescriptions** | 🟡 Medium | If missing information, get it before processing |
| 4 | **Ignoring drug interaction alerts** | 🔴 High | Always flag interactions for pharmacist review |
| 5 | **Discussing patient info where others can hear** | 🔴 High | Move to private area; use low voice; logout screens |
| 6 | **Not checking DEA validity for controlled substances** | 🔴 High | Verify every controlled Rx — fake Rx = criminal liability |
| 7 | **Failing to rotate stock (expiration)** | 🟡 Medium | FIFO rotation prevents expired dispensing |

```
❌ "The pharmacist is busy — I'll just fill this and have them verify later"
✅ No medication can leave the pharmacy without pharmacist verification — it's the law

❌ "I know this patient — no need to check ID"
✅ Always verify identity — mistakes happen, especially with common names

❌ "That interaction alert is probably a false positive"
✅ Every alert must be reviewed by the pharmacist — don't dismiss
```

