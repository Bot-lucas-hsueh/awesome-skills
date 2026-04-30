## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Data Loss During Repair** | 🔴 Critical | Reimaging, disk replacement, or OS reinstallation can permanently destroy user data if backup is not verified first | Verify backup completion and integrity BEFORE any destructive action; document backup location and timestamp in ticket |
| **Accidental Account Lockout or Deletion** | 🔴 Critical | Incorrect AD operations (wrong OU, bulk script errors, accidental disable vs. delete) can lock out users or irrecoverably delete accounts | Use AD Recycle Bin; prefer Disable over Delete; test scripts on a single test account before bulk execution; require peer review for bulk AD operations |
| **Unauthorized Access from Overly Permissive Fixes** | 🔴 Critical | Granting local admin rights, disabling UAC, or turning off firewall/AV to "fix" a problem creates persistent security vulnerabilities | Never grant admin rights as a resolution; escalate to InfoSec for security policy exceptions; document any temporary exceptions with an auto-expiry plan |
| **Change Without Proper Change Management** | 🟡 High | Making infrastructure or configuration changes without CAB approval (e.g., firewall rule changes, server config edits) violates change management controls and can cause outages | Submit a change request for any non-standard change; standard changes (pre-approved) are documented in the change catalog; never improvise on production systems |
| **Warranty Voiding** | 🟡 High | Opening a device, replacing non-user-serviceable parts, or flashing firmware outside manufacturer guidelines voids warranty | Verify warranty status before any hardware intervention; use manufacturer's authorized repair process for in-warranty devices |
| **Phishing

---
