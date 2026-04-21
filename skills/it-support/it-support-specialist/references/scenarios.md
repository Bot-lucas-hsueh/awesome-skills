## § 9 · Scenario Examples

### Scenario A: User Cannot Connect to VPN + Authenticate to Office 365 (MFA Issue)

**Context:** User reports: "I can't connect to VPN from home and my Office 365 keeps asking for verification but my phone app doesn't work."

---

**Technician:** Thanks for reaching out. I have your ticket and I'll help get you back online. Before I start, can you confirm — are you on a company laptop or a personal device right now?

**User:** Company laptop, at home on my home Wi-Fi.

**Technician:** Perfect. And when you try to connect to VPN, what exactly happens — do you see an error message? If so, can you read me exactly what it says?

**User:** It says "Authentication failed. Please check your credentials or multi-factor authentication."

**Technician:** That message tells me this is an MFA issue, not your password. Your password is probably fine. The VPN and Office 365 both use the same Microsoft authentication, which requires your phone app (Microsoft Authenticator) to approve the login. Let's check a few things.

*[Gate 1: Identity/MFA issue. Gate 3: Fully blocked. Gate 4: Not hardware — reproduced on the account, not the device.]*

**Step 1 — Check Authenticator app:**

"Can you open the Microsoft Authenticator app on your phone? What do you see — is the app asking you to approve anything, or does it show an error?"

**User:** The app says "Your account needs attention" and asks me to update something.

**Technician:** That's the problem. Your MFA registration needs to be refreshed — this can happen after a phone replacement, an app update, or if your company's security policy recently changed. Here's what I'll do: I'll temporarily disable the MFA requirement for your account for 10 minutes so you can sign in and re-register your authenticator. This is a standard procedure and is logged in our system.

*[Gate 5: This is a standard Tier 1 procedure — no escalation needed. Documented in ticket.]*

**Resolution steps taken:**
1. Verified user identity via employee ID + manager email confirmation
2. In Entra ID admin portal: User → Authentication methods → Disabled MFA for 10-minute window
3. User signed into Office 365 at aka.ms/mfasetup and re-registered Authenticator using QR code flow
4. Re-enabled MFA in Entra ID
5. User tested VPN connection → Connected successfully
6. User tested Office 365 → Authenticated with MFA prompt → Approved → Access confirmed

**Technician:** You should be all set now. Can you try connecting to VPN and then opening Outlook to confirm everything works?

**User:** Yes! VPN connected and Outlook is open. Thank you!

**Technician:** Excellent. I'll close this ticket now. If you get a new phone in the future, go to aka.ms/mfasetup before setting up the new phone to re-register — same quick process. Take care!

*[Ticket notes: MFA registration stale after Authenticator app update. Re-registered via Entra ID admin MFA reset. No security risk — identity verified prior to action. KB-0241 referenced. FCR: Yes.]*

---

### Scenario B: Laptop Hardware Failure — Diagnosis and Data Recovery

**Context:** User reports laptop will not power on. IT asset tag confirmed. Device is 2 years old, out of warranty.

---

**Technician:** I'm going to walk through a hardware diagnosis. First and most important: do you have any unsaved work or personal files on this laptop that are not backed up to OneDrive or a network drive?

**User:** I have a project folder on the desktop I haven't synced in a week.

**Technician:** That's critical. Before we do anything else, we need to get that data. We will not touch the hard drive or attempt any repair until we have secured your files. Let me walk through this in order.

*[Risk check: Data loss risk identified. Backup before repair — non-negotiable.]*

**Diagnostic sequence:**

```
Step 1 — Power on test:
  → Press power: No LEDs, no fan spin → likely power delivery issue
  → Remove battery (if removable), plug in AC only → still no response
  → Try known-good AC adapter → still no response
  → Conclusion: Possible dead battery AND/OR failed DC jack AND/OR motherboard

Step 2 — External display test (if internal display suspected):
  → Connect HDMI to external monitor → no signal
  → Rules out isolated display failure

Step 3 — Remove and reseat RAM:
  → Remove each DIMM, clean contacts, reseat
  → Power on → still no POST beep, no display
  → Rules out loose RAM as sole cause

Step 4 — Storage preservation (PRIORITY):
  → Remove NVMe/SATA SSD from failed laptop
  → Insert into USB-to-NVMe enclosure (stock item: IT-ENCL-01)
  → Connect to a working loaner laptop
  → Drive appears as external drive: YES → data accessible
  → Copy project folder to user's OneDrive → verified copy complete
```

**Technician:** Your files are now safely copied to your OneDrive — I've confirmed 23 files transferred successfully. You can access them right now from any device.

With data secured: the laptop diagnosis indicates a likely motherboard failure (no POST with known-good power adapter and reseated RAM). Because this device is out of warranty, repair cost will exceed the device value. I'm recommending a replacement rather than repair.

**Next steps:**
1. Issue loaner laptop (from IT stock) today so user can resume work immediately
2. Submit hardware replacement request via ServiceNow RITM workflow — approval required from user's manager
3. When replacement arrives: transfer the SSD to the new device (if same interface) or migrate via USB enclosure
4. Update CMDB: retire old asset tag; assign new asset tag to user record

*[Ticket notes: Laptop failed POST — suspected motherboard failure. Data recovered to OneDrive before any repair attempt (23 files, project folder confirmed intact). Loaner ISSUEd: Asset TAG-8821. Replacement request: RITM-00441. No data loss.]*

---

### Scenario C: Mass Password Reset After Phishing Incident (Coordinated Response)

**Context (Edge Case — Security Incident):** Information Security team notifies the help desk at 09:15 that a phishing campaign successfully harvested credentials from an estimated 800 users who clicked a malicious link and entered credentials. Security has isolated the malicious domain. IT Director instructs: force-reset all 800 affected accounts immediately and coordinate with the business to minimize disruption.

*[Gate 1: Security Incident. Gate 5: Immediate escalation + coordinated response. This is NOT a standard Tier 1 action — it is an incident response operation.]*

**Incident response coordination:**

**09:15 — Incident Bridge Call Opened**
- Attendees: IT Director, InfoSec Lead, Help Desk Manager, AD Admin, Comms Lead
- InfoSec provides: list of 800 affected SAMAccountNames (exported from phishing platform logs)
- Decision: Force-reset all 800 passwords + force MFA re-registration; notify users by email before reset to minimize panic calls

**09:20 — Pre-action checklist:**
```
[ ] Backup: Export current AD state for all 800 accounts (Get-ADUser bulk export)
[ ] Script review: Two-person review of PowerShell before execution
[ ] Communication draft: IT Comms prepares user notification email
[ ] Help desk surge: Alert all available techs — call volume will spike
[ ] ServiceNow: Open major incident MI-2024-0047; link all sub-tickets
[ ] InfoSec sign-off: Confirm scope list is final before execution
```

**09:35 — PowerShell execution (AD Admin, peer-reviewed):**
```powershell
# Import affected user list
$affectedUsers = Import-Csv -Path "C:\Incident\affected_accounts.csv"

# Force password reset at next logon for all affected accounts
foreach ($user in $affectedUsers) {
    try {
        Set-ADUser -Identity $user.SamAccountName `
                   -ChangePasswordAtLogon $true
        # Revoke all active sessions (Entra ID — requires MgGraph module)
        Revoke-MgUserSignInSession -UserId $user.UserPrincipalName
        Write-Log "RESET OK: $($user.SamAccountName)"
    } catch {
        Write-Log "ERROR: $($user.SamAccountName) — $($_.Exception.Message)"
    }
}
```

**09:40 — User notification email sent (all 800 users):**
> "Your IT team has detected a security event affecting your account. As a precaution, your password has been reset. When you next sign in, you will be prompted to set a new password. If you need help, call the IT Help Desk at ext. 4357 (HELP) — hold times may be longer than usual today. Do not panic — your data is safe."

**09:40–13:00 — Help Desk surge response:**
- All available techs on call queue
- Standard script for phishing reset calls created and distributed to all agents
- Users assisted with: new password setup, MFA re-registration, VPN reconnection
- Ticket template pre-filled for speed: linked to MI-2024-0047

**13:30 — Status to IT Director:**
```
Accounts reset:     798
User calls handled: 312 calls; avg handle time 4.2 min
Tickets opened:     298 (14 users self-served via KB)
Open escalations:   6 (users who cannot access personal phone for MFA — scheduled callbacks)
Estimated resolution of all accounts: by 15:00
```

**Lessons captured in Problem Record PRB-2024-0031:**
- Root cause: Phishing simulation gap — 800 users not in security awareness training cohort
- Corrective action: Mandatory phishing training + simulated phishing program expansion
- KB-0318 created: "What to do if you clicked a phishing link"

---
