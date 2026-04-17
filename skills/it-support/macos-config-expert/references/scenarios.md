## 9. Scenario Examples

### 9.1 Enterprise macOS Security Hardening

**User:** "我需要加固100台 macOS Sonoma 设备，要求符合 CIS Level 1 基准，通过 Jamf 部署。"

**macOS Config Expert:**
> **Deployment Strategy: MDM-First, Shell-Assisted**
>
> **Phase 1 — High-Impact mobileconfig Payloads (deploy via Jamf Policy):**
>
> ```xml
> 
> <key>PayloadType</key>
> <string>com.apple.MCX.FileVault2</string>
> <key>Enable</key>
> <string>On</string>
> <key>Defer</key>
> <true/>
> <key>DeferForceAtUserLoginMaxBypassAttempts</key>
> <integer>3</integer>
> ```
>
> **Phase 2 — CIS Level 1 Shell Script (Jamf Script, runs as root):**
>
> ```bash
> #!/bin/zsh
> # CIS macOS Sonoma Level 1 - Critical Controls
> # CIS Control 1.1: Enable Auto Update
> defaults write /Library/Preferences/com.apple.SoftwareUpdate AutomaticCheckEnabled -bool true
> defaults write /Library/Preferences/com.apple.SoftwareUpdate AutomaticDownload -bool true
> defaults write /Library/Preferences/com.apple.SoftwareUpdate AutomaticallyInstallMacOSUpdates -bool false
>
> # CIS Control 2.1.2: Disable Bluetooth when not needed (flag for audit)
> blueutil --power 0 2>/dev/null || true
>
> # CIS Control 5.1.4: Disable Guest account
> sudo defaults write /Library/Preferences/com.apple.loginwindow GuestEnabled -bool false
>
> # CIS Control 6.1.1: Require password immediately after screensaver
> defaults write com.apple.screensaver askForPassword -bool true
> defaults write com.apple.screensaver askForPasswordDelay -int 0
>
> # Verify
> echo "FV Status: $(fdesetup status)"
> echo "Firewall: $(sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate)"
> ```
>
> **Jamf Deployment Checklist:**
> | Step | Action | Verification |
> |------|--------|-------------|
> | 1 | Upload mobileconfig payloads | Scope to "All Managed Computers" smart group |
> | 2 | Upload shell script, set "Run as root" | Test on 5-device pilot group first |
> | 3 | Force policy check | `sudo jamf policy` on pilot → review log |
> | 4 | Confirm FV2 escrow | Jamf console → Computer → Disk Encryption tab |
>
> **Next, I need from you:**
> 1. Are these devices already enrolled in Jamf or is this a fresh enrollment scenario?
> 2. Do you need the full 50+ control CIS script, or just the top 10 critical controls?

### 9.2 Homebrew Dev Environment Reproducibility

**User:** "新同事 Mac 环境搭建每次都不一样，我们用 Homebrew，怎么做到完全一致的开发环境？"

**macOS Config Expert:**
> **Solution: `Brewfile` + `dotfiles` + `mise` (version manager)**
>
> **Step 1 — Generate Brewfile from reference machine:**
> ```bash
> # On the reference ("golden") Mac:
> brew bundle dump --describe --file=./Brewfile --force
> # --describe adds comments explaining each formula
> ```
>
> **Step 2 — Annotated Brewfile structure:**
> ```ruby
> # Brewfile — commit this to your team repo
> tap "homebrew/bundle"
> tap "homebrew/cask-fonts"
>
> # Core CLI tools
> brew "git", args: ["HEAD"]
> brew "gh"            # GitHub CLI
> brew "jq"            # JSON processor
> brew "mise"          # Runtime version manager (replaces nvm/rbenv/pyenv)
>
> # Languages via mise (not brew — avoids PATH conflicts)
> # mise install node@lts python@3.12 go@1.22
>
> # GUI Apps (casks)
> cask "visual-studio-code"
> cask "docker"
> cask "iterm2"
>
> # Mac App Store (requires `mas` CLI)
> mas "Xcode", id: 497799835
> ```
>
> **Step 3 — Onboarding script (`setup.sh`):**
> ```bash
> #!/bin/zsh
> set -e
>
> # 1. Install Homebrew if missing
> if ! command -v brew &>/dev/null; then
>   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
>   eval "$(/opt/homebrew/bin/brew shellenv)"
> fi
>
> # 2. Install all dependencies from Brewfile
> brew bundle install --file=./Brewfile
>
> # 3. Verify
> brew bundle check --file=./Brewfile && echo "✅ All dependencies satisfied"
>
> # 4. Install runtimes via mise
> mise install
> ```
>
> **Step 4 — Verify consistency:**
> ```bash
> brew bundle check --file=./Brewfile
> # Output: "The Brewfile's dependencies are satisfied."
> ```

### 9.3 LaunchAgent Automation

**User:** "我需要每天早上9点自动运行一个Python脚本，怎么用launchd做？"

**macOS Config Expert:**
> **LaunchAgent Plist — correct pattern for user-context scheduling:**
>
> ```bash
> # Create the plist file
> cat > ~/Library/LaunchAgents/com.user.daily-task.plist << 'EOF'
> <?xml version="1.0" encoding="UTF-8"?>
> <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
> <plist version="1.0">
> <dict>
>     <key>Label</key>
>     <string>com.user.daily-task</string>
>     <key>ProgramArguments</key>
>     <array>
>         <string>/usr/bin/python3</string>
>         <string>/Users/yourname/scripts/daily_task.py</string>
>     </array>
>     <key>StartCalendarInterval</key>
>     <dict>
>         <key>Hour</key>
>         <integer>9</integer>
>         <key>Minute</key>
>         <integer>0</integer>
>     </dict>
>     <key>StandardOutPath</key>
>     <string>/tmp/daily-task.log</string>
>     <key>StandardErrorPath</key>
>     <string>/tmp/daily-task-error.log</string>
>     <key>EnvironmentVariables</key>
>     <dict>
>         <key>PATH</key>
>         <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
>     </dict>
> </dict>
> </plist>
> EOF
>
> # Load the agent
> launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.user.daily-task.plist
>
> # Verify it loaded
> launchctl print gui/$(id -u)/com.user.daily-task
>
> # Test run immediately
> launchctl kickstart gui/$(id -u)/com.user.daily-task
>
> # Check logs
> tail -f /tmp/daily-task.log
> ```
>
> **⚠️ Common mistakes:**
> - Use absolute paths everywhere — launchd does NOT inherit your shell PATH
> - Use `bootstrap`/`bootout` (modern), NOT deprecated `load`/`unload`
> - For system-wide scripts: place in `/Library/LaunchDaemons/` and load with `sudo launchctl bootstrap system`

---

