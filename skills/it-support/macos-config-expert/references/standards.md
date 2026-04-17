## 7. Standards & Reference

### 7.1 macOS Configuration Frameworks

| Framework / 框架 | When to Use / 使用场景 | Key Steps
|-----------------|----------------------|-------------------|
| **CIS macOS Benchmark** | Hardening a new machine or auditing security posture | 1. Run assessment script → 2. Map failures to CIS control IDs → 3. Apply Level 1 (mandatory) then Level 2 (optional) fixes → 4. Re-run and document score |
| **Brewfile Reproducibility** | Onboarding new developers or cloning dev environment | 1. `brew bundle dump` on reference machine → 2. Commit Brewfile to repo → 3. `brew bundle install` on new machine → 4. Verify with `brew bundle check` |
| **mobileconfig Profile Workflow** | Fleet-deploying any system preference via MDM | 1. Identify preference domain with `defaults domains` → 2. Author XML payload → 3. Sign with `openssl` → 4. Test on pilot → 5. Scope to smart group → 6. Deploy |
| **LaunchAgent Pattern** | Scheduling background tasks without cron | 1. Write plist to `~/Library/LaunchAgents/` → 2. Set `Label`, `ProgramArguments`, `RunAtLoad`/`StartCalendarInterval` → 3. `launchctl bootstrap gui/$(id -u) <plist>` → 4. Verify with `launchctl print gui/$(id -u)/<label>` |
| **FileVault Fleet Management** | Enabling FV2 at scale with key escrow | 1. Pre-create MDM FV payload with institutional recovery key → 2. Deploy via MDM before user enrollment completes → 3. `fdesetup status` check in policy → 4. Verify escrow in MDM console |

### 7.2 macOS Diagnostics Metrics

| Metric / 指标 | Command / 命令 | Healthy Threshold
|--------------|---------------|---------------------------|
| **Memory Pressure** | `vm_stat \| grep -E 'Pages (free\|active\|inactive\|wired\|compressed)'` | Compressed pages < 20% of total; swap_used < 2 GB |
| **Thermal State** | `pmset -g thermlog` or `powermetrics --samplers thermal -n 1` | `CPU_Scheduler_Limit = 100`, `CPU_Speed_Limit = 100`; any value < 100 indicates throttle |
| **Disk Health** | `diskutil info disk0 \| grep -i 'SMART'` | `SMART Status: Verified`; check `iostat -d 1 5` for sustained >200 MB/s write saturation |
| **Startup Duration** | `log show --predicate 'eventMessage contains "Boot complete"' --last 1h` | Boot-to-login < 30s on SSD; > 60s warrants `log show --start … --predicate 'subsystem == "com.apple.xpc"'` investigation |
| **Gatekeeper Policy** | `spctl --status` | `assessments enabled`; `spctl --master-disable` is a red flag in security audit |
| **SIP Status** | `csrutil status` | `System Integrity Protection status: enabled.`; any partial disable requires documented justification |
| **FileVault Status** | `fdesetup status` | `FileVault is On.`; `Deferred enablement awaiting...` means user has not yet completed the process |

---

