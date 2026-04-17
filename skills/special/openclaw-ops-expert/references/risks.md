## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|---------------------|
| **DM policy set to `open`** | 🔴 High | Any user on the network can send messages to your OpenClaw instance; on a public IP this means unsolicited access from the internet | Only use `open` on Tailscale-scoped networks or verified private LANs; default to `pairing` |
| **Gateway bound to 0.0.0.0** | 🔴 High | Binding the gateway to all interfaces without a firewall exposes the WebSocket port to the network; combined with `open` DM policy creates full remote control risk | Bind to `127.0.0.1` by default; use Tailscale Funnel for intentional remote access |
| **API keys in openclaw.json** | 🔴 High | `~/.openclaw/openclaw.json` stored in plaintext; contains AI provider API keys and channel credentials; accessible to any process running as the same user | Set `chmod 600 ~/.openclaw/openclaw.json`; use a secrets manager or OS keychain integration |
| **Daemon running as root** | 🟡 Medium | Installing the daemon with `sudo` causes the OpenClaw process to run as root; a compromised skill or agent can execute arbitrary commands with elevated privileges | Run daemon as a dedicated non-root user; use `User=openclaw` in systemd unit |
| **Outdated Node.js runtime** | 🟡 Medium | Node <22 lacks native fetch and WebSocket APIs relied upon by OpenClaw; silent failures rather than clear error messages | Pin `engines.node: ">=22"` in your environment; use nvm or fnm for version management |
| **Channel token expiry not handled** | 🟢 Low | OAuth tokens for Slack/Discord expire; gateway shows the channel as online but messages fail silently | Configure token refresh monitoring; set up `/ping` health-check commands per channel |

**⚠️ IMPORTANT
- OpenClaw agents can execute tools and browser automation on the host system. Only install skills from trusted ClawHub sources; review skill permissions before installation.

- Device pairing (iOS/Android nodes) grants the agent access to camera, notifications, and screen recording. Revoke device pairings from `openclaw` CLI when not in use.

---
