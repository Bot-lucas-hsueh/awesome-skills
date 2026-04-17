## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Installing with sudo

```markdown
❌ BAD: sudo npm install -g openclaw@latest
# Installs files as root; daemon runs as root; npm/pnpm global dir is /usr/local
# Any skill with shell tool access can execute arbitrary commands as root

✅ GOOD: npm install -g openclaw@latest  (with nvm-managed Node, no sudo needed)
# nvm places global packages in ~/.nvm/versions/node/<ver>/bin/ — writable by user
# If EACCES occurs: use nvm, not sudo
```

**Anti-Pattern 2: Setting dmPolicy to open on public network

```markdown
❌ BAD:
{
  "dmPolicy": "open",
  "gateway": { "bind": "0.0.0.0" }
}
# Result: anyone who discovers the port can control your AI assistant
# Combined with shell/browser tools in skills = full machine compromise risk

✅ GOOD:
{
  "dmPolicy": "pairing",           // Require pairing code from unknown senders
  "gateway": { "bind": "127.0.0.1" }  // Local only; use Tailscale for remote
}
```

### 🟡 Medium Severity

**Anti-Pattern 3: Manually editing daemon files

```markdown
❌ BAD: Directly editing ~/Library/LaunchAgents/ai.openclaw.gateway.plist
# OpenClaw regenerates this file on onboard; manual edits are overwritten
# Inconsistent state between plist and openclaw.json causes silent failures

✅ GOOD: Use openclaw CLI and ~/.openclaw/openclaw.json for all configuration
# openclaw onboard --reinstall regenerates daemon files from config
# Treat plist/systemd unit files as generated artifacts, not config
```

**Anti-Pattern 4: Storing tokens in environment variables without daemon reload

```markdown
❌ BAD: export TELEGRAM_BOT_TOKEN=xxx  (in .bashrc, without daemon restart)
# Daemon process inherits environment at launch time, not at .bashrc source time
# New env vars are invisible to a running daemon

✅ GOOD: Set tokens in ~/.openclaw/openclaw.json directly (chmod 600 the file)
# OR configure systemd EnvironmentFile= in the unit for proper env injection
# Always restart daemon after credential changes: systemctl restart openclaw
```

**Anti-Pattern 5: Running multiple gateway instances

```markdown
❌ BAD: Running `openclaw gateway` manually while daemon is also running
# Two instances compete for port 18789; EADDRINUSE causes both to become unstable
# Channel connections are split between instances unpredictably

✅ GOOD: Use ONE instance only.
# Stop daemon first: launchctl unload .../ai.openclaw.gateway.plist
# Then run manually for debugging: openclaw gateway --verbose
# Or keep daemon running and read logs: tail -f ~/Library/Logs/openclaw/gateway.log
```

---

