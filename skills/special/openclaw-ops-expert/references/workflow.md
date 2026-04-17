## 8. Standard Workflow

### 8.1 Fresh Installation & First-Run

```
Phase 1: Prerequisites (5 min)
├── Verify Node.js: node --version  (must be ≥22)
│   └── If <22: nvm install 22 && nvm use 22 && nvm alias default 22
├── Verify package manager: npm --version (or pnpm --version)
└── [✓ Done]: node -e "console.log(process.version)" shows v22.x.x or higher
    [✗ FAIL]: Older Node → must upgrade before proceeding; openclaw uses native fetch/WebSocket

Phase 2: Install & Onboard (10 min)
├── npm install -g openclaw@latest   (or pnpm add -g openclaw@latest)
├── openclaw onboard --install-daemon
│   ├── Select AI model provider (OpenAI/Anthropic/local)
│   ├── Configure first channel (Telegram recommended for first-time)
│   └── Install initial skills from ClawHub
└── [✓ Done]: Daemon running; `openclaw channels list` shows 1+ channel as "connected"
    [✗ FAIL]: npm EACCES error → use nvm instead of system Node; never `sudo npm install -g`

Phase 3: Gateway Verification (5 min)
├── openclaw gateway --port 18789 --verbose
├── Send a test message via configured channel
└── [✓ Done]: Gateway logs show message received and AI response sent
    [✗ FAIL]: Connection refused → check daemon: `launchctl list | grep openclaw` (macOS)
              or `systemctl status openclaw` (Linux); restart if inactive
```

### 8.2 Adding a New Channel

```
Step 1: Identify channel type
  → Cloud webhook (Telegram, Discord, Slack, Teams) → needs bot token + webhook URL
  → Device-bound (iMessage via BlueBubbles, Signal) → needs device online + bridge running
  → OAuth (WhatsApp) → needs phone number + QR code scan

Step 2: Add channel via onboard wizard or config
  → openclaw onboard --add-channel <type>
  → OR manually add to channels[] array in ~/.openclaw/openclaw.json

Step 3: Restart gateway and verify
  → openclaw gateway --verbose  (check for "[channel] connected" log line)
  → Send test message from the new channel
  → [✓ Done]: Response received in under 10 seconds
  → [✗ FAIL]: Auth error → token/secret may be wrong; webhook URL not yet registered

Step 4: Configure per-channel DM policy (optional)
  → Set channel-level override if global dmPolicy is too restrictive for this channel
```

### 8.3 Enabling Remote Access via Tailscale

```
Step 1: Install and authenticate Tailscale
  → brew install tailscale (macOS)
  → tailscale up --ssh

Step 2: Expose gateway via Tailscale Serve (LAN-only)
  → tailscale serve https / ws://127.0.0.1:18789
  → Access from other Tailscale nodes at https://<device>.ts.net

Step 3: (Optional) Public access via Tailscale Funnel
  → tailscale funnel 443 on
  → WARNING: Combine with dmPolicy=pairing to avoid unauthenticated access

Step 4: Update openclaw.json gateway.url for remote clients
  → "gateway": { "publicUrl": "wss://<device>.ts.net" }
```

---

