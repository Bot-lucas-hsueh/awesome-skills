## 7. Standards & Reference

### 7.1 Installation Workflows

| Workflow / 工作流 | When to Use / 使用场景 | Key Steps
|-----------------|----------------------|-------------------|
| **Fresh Install** | New device, no existing OpenClaw | 1. `node --version` (≥22 required) → 2. `npm install -g openclaw@latest` → 3. `openclaw onboard --install-daemon` → 4. `openclaw gateway --port 18789` |
| **Daemon Only Reinstall** | Daemon removed or service broken | 1. `openclaw onboard --install-daemon` → 2. verify via `launchctl list \| grep openclaw` (macOS) or `systemctl status openclaw` (Linux) |
| **Headless/Server Install** | Linux VPS or CI environment without UI | 1. Install Node 22 via nvm → 2. `npm install -g openclaw@latest` → 3. Create `~/.openclaw/openclaw.json` manually → 4. Write systemd unit file → 5. `systemctl enable --now openclaw` |
| **Node Version Upgrade** | Moving from Node 18/20 to 22+ | 1. `nvm install 22` → 2. `nvm use 22` → 3. `npm install -g openclaw@latest` → 4. restart daemon |

### 7.2 DM Policy Configuration

| Policy / 策略 | Config Value / 配置值 | Behavior / 行为 | When to Use
|--------------|----------------------|----------------|----------------------|
| **Pairing** (default) | `"dmPolicy": "pairing"` | Unknown senders must enter a pairing code; approved senders are allowlisted | All public-facing deployments; default recommended |
| **Open** | `"dmPolicy": "open"` | All senders accepted without verification | Trusted private LAN or Tailscale-only network |
| **Deny** | `"dmPolicy": "deny"` | All DMs rejected; only group/channel messages accepted | When using OpenClaw only in group channels (Slack workspace, Discord server) |

### 7.3 Key Config Fields

| Field / 字段 | Location / 位置 | Example / 示例 | Effect
|-------------|----------------|---------------|--------------|
| `gateway.port` | `openclaw.json` | `18789` | WebSocket port the gateway listens on |
| `gateway.bind` | `openclaw.json` | `"127.0.0.1"` | Network interface binding (use `0.0.0.0` only with firewall) |
| `dmPolicy` | `openclaw.json` | `"pairing"` | Controls who can DM the assistant |
| `model.provider` | `openclaw.json` | `"openai"` | AI provider (openai / anthropic
| `model.endpoint` | `openclaw.json` | `"http://localhost:11434/v1"` | Custom endpoint for local models (Ollama etc.) |
| `channels[].type` | `openclaw.json` | `"telegram"` | Channel integration type |
| `channels[].token` | `openclaw.json` | `"<bot-token>"` | Channel-specific auth token |

---

