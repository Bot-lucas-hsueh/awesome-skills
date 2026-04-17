## 8. Standard Workflow

### 8.1 New macOS Machine Hardening

```
Phase 1: Inventory & Baseline
├── Identify macOS version: sw_vers -productVersion
├── Confirm architecture: uname -m  (arm64 | x86_64)
├── Check MDM enrollment: profiles status -type enrollment
├── Record current SIP/Gatekeeper state: csrutil status && spctl --status
└── Baseline snapshot: defaults domains > ~/Desktop/baseline-domains.txt

Phase 2: Security Configuration
├── Enable FileVault: sudo fdesetup enable -user $(whoami)
│   └── Verify: fdesetup status
├── Enable Firewall: sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on
│   └── Enable stealth mode: sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on
│   └── Verify: sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
├── Disable unnecessary sharing services:
│   sudo systemsetup -setremotelogin off          # SSH
│   sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.smbd.plist  # SMB
├── Lock screen timeout (require password immediately):
│   defaults write com.apple.screensaver askForPassword -bool true
│   defaults write com.apple.screensaver askForPasswordDelay -int 0
└── Disable Handoff (enterprise isolation):
    defaults write ~/Library/Preferences/ByHost/com.apple.coreservices.useractivityd.plist ActivityAdvertisingAllowed -bool false

Phase 3: Verification & Documentation
├── Re-run all verify commands from Phase 2
├── Export applied profiles: profiles list -output /tmp/profiles-applied.plist
├── Run CIS assessment script (if available)
└── Final checkpoint: sysdiagnose -f ~/Desktop/ && open ~/Desktop/sysdiagnose_*.tar.gz
```

### 8.2 Homebrew Environment Setup

```
Step 1: Install Homebrew (Apple Silicon path)
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile && eval "$(/opt/homebrew/bin/brew shellenv)"

Step 2: Verify installation and update
  brew --version && brew update && brew doctor

Step 3: Dump or restore a Brewfile
  # Dump from existing machine:
  brew bundle dump --file=~/Brewfile --force

  # Restore on new machine:
  brew bundle install --file=~/Brewfile

Step 4: Regular maintenance automation (LaunchAgent)
  Create ~/Library/LaunchAgents/com.user.brew-upgrade.plist with weekly StartCalendarInterval
  launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.user.brew-upgrade.plist
```

### 8.3 Troubleshooting Slow macOS Boot

```
Step 1: Check boot time log
  log show --predicate 'eventMessage contains "Boot complete"' --last 2h

Step 2: Identify slow LaunchDaemons
  sudo fs_usage -e -f pathname | grep -E '\.(plist|dylib)' &
  sudo launchctl list | sort -k2 -n | tail -20

Step 3: Check for zombie login items
  osascript -e 'tell application "System Events" to get every login item'
  # Or: open /System/Library/PreferencePanes/Users.prefPane

Step 4: Inspect kernel extension load time [Intel only]
  kextstat | grep -v com.apple

Step 5: Review sysdiagnose for I/O wait
  sudo sysdiagnose -b    # Generates bundle in /var/tmp/
  # Examine: spindump.txt, ps.txt, vm_stat.txt
```

---

