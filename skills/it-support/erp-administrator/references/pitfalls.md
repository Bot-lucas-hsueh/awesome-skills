## 10. Common Pitfalls

### Anti-Pattern 1: SAP_ALL or Equivalent Superuser Profile to Regular Users

❌ **BAD:**
"The finance director needs access to a few extra reports. Just give them SAP_ALL — it's easier than figuring out which authorization objects to add."

✅ **GOOD:**
Run ST05 or transaction SU53 to identify exactly which authorization object is failing for the finance director's required access. Add the specific authorization object with the specific permitted values to their role. Transport and test. This takes 30 minutes. SAP_ALL takes 2 minutes and creates an unmitigated critical audit finding.

*Why it matters:* SAP_ALL bypasses all application security controls. A user with SAP_ALL can post to any company code, any period, any fiscal year. One accidental (or deliberate) action can destroy financial data that took a quarter to build.

