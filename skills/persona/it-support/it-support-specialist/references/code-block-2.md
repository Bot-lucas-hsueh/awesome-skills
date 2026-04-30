# IT Support Scenario Examples

## Scenario A — VPN + MFA Issue (§9)

**Diagnostic sequence:**

```powershell
# Step 1 — Check Authenticator app:
# User opens Microsoft Authenticator → "Your account needs attention" = stale MFA registration

# Step 2 — Resolution:
# In Entra ID admin portal: User → Authentication methods → Disabled MFA for 10-minute window
# User signs into aka.ms/mfasetup and re-registers Authenticator using QR code flow
# Re-enable MFA in Entra ID

# Verify: VPN connected + Office 365 authenticated → Access confirmed
```

## Scenario B — Laptop Hardware Diagnosis (§9)

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

## Scenario C — Mass Password Reset After Phishing Incident (§9)

**Pre-action checklist:**

```powershell
[ ] Backup: Export current AD state for all 800 accounts (Get-ADUser bulk export)
[ ] Script review: Two-person review of PowerShell before execution
[ ] Communication draft: IT Comms prepares user notification email
[ ] Help desk surge: Alert all available techs — call volume will spike
[ ] ServiceNow: Open major incident MI-2024-0047; link all sub-tickets
[ ] InfoSec sign-off: Confirm scope list is final before execution
```

**PowerShell execution (AD Admin, peer-reviewed):**

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

**User notification email:**
> "Your IT team has detected a security event affecting your account. As a precaution, your password has been reset. When you next sign in, you will be prompted to set a new password. If you need help, call the IT Help Desk at ext. 4357 (HELP) — hold times may be longer than usual today. Do not panic — your data is safe."

**Post-incident status:**
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

## Intake Template (§8)

```
USER:        [Name]
DEVICE:      [Hostname / Asset Tag]
OS:          [Windows 11 22H2 / macOS 14.3]
LOCATION:    [Office / Remote / VPN: Yes/No]
ERROR:       [Exact error message or screenshot reference]
REPRODUCED:  [Yes / No]
STARTED:     [Date/time]
IMPACT:      [User only / Team of X / Department]
PRIORITY:    [P1 / P2 / P3 / P4]
```

## Resolution Note Template (§8)

```
RESOLUTION DATE:  [YYYY-MM-DD HH:MM]
TECHNICIAN:       [Name]
ROOT CAUSE:       [Brief cause description]
FIX APPLIED:      [Exact steps / commands]
WORKAROUND:       [If temp fix, describe; permanent fix ETA: ...]
USER CONFIRMED:   [Yes / No]
KB REFERENCE:     [KB-XXXX or "New KB drafted: [title]"]
PROBLEM RECORD:   [PRB-XXXX or N/A]
TIME SPENT:       [HH:MM]
```
