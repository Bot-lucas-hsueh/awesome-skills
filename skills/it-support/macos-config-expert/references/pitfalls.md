## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Incorrect `defaults write` type

```markdown
❌ BAD: defaults write com.apple.dock autohide true
# Writes the STRING "true", not boolean — dock ignores it silently

✅ GOOD: defaults write com.apple.dock autohide -bool true
         defaults read com.apple.dock autohide  # Verify: output should be "1"
         killall Dock                            # Apply immediately
```

**Anti-Pattern 2: Scripting Secure Token without recovery plan

```markdown
❌ BAD: sysadminctl -secureTokenOn newadmin -password adminpass
# If this fails mid-execution on Apple Silicon, the machine may not boot

✅ GOOD: 1. Verify existing token holder: sysadminctl -secureTokenStatus $(whoami)
         2. Test on a VM or non-production machine
         3. Have bootable macOS USB recovery ready
         4. Use MDM Bootstrap Token instead when available
```

**Anti-Pattern 3: Disabling SIP for a trivial operation

```markdown
❌ BAD: Rebooting to Recovery Mode to disable SIP just to move a file to /usr/

✅ GOOD: Use /usr/local/ (not SIP-protected) for custom binaries
         Or deploy via MDM pkg to /Library/ (MDM has SIP bypass for /Library writes)
         csrutil status — if already enabled, find an alternative path
```

### 🟡 Medium Severity

**Anti-Pattern 4: Using `cron` instead of `launchd`

```markdown
❌ BAD: crontab -e  → */5 * * * * /usr/bin/python3 /scripts/check.py
# cron jobs don't inherit GUI session, don't survive sleep, and produce no logs

✅ GOOD: Create ~/Library/LaunchAgents/com.user.check.plist with StartInterval 300
         Includes StandardOutPath, EnvironmentVariables, and ThrottleInterval
         Survives sleep/wake cycles and integrates with unified logging
```

**Anti-Pattern 5: Hardcoding `/usr/local/bin` on Apple Silicon

```markdown
❌ BAD: #!/bin/bash
        /usr/local/bin/python3 script.py  # Fails on Apple Silicon — brew is at /opt/homebrew

✅ GOOD: #!/usr/bin/env python3            # env resolves from PATH
         Or explicitly: /opt/homebrew/bin/python3
         Add to LaunchAgent EnvironmentVariables: /opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin
```

---

