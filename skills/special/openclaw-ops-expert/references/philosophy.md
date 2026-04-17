## § 4 · Core Philosophy

### 4.1 OpenClaw Architecture Model

```
                    ┌─────────────────────────────────┐
                    │       AI Model Providers         │  ← OpenAI / Anthropic
                    └────────────────┬────────────────┘
                                     │ API calls
              ┌──────────────────────▼──────────────────────┐
              │           Gateway (WebSocket :18789)          │  ← Control plane
              │   ┌──────────┐  ┌──────────┐  ┌──────────┐  │
              │   │ Channel  │  │  Agent   │  │  Skills  │  │
              │   │  Router  │  │ Sessions │  │ Registry │  │
              │   └────┬─────┘  └──────────┘  └──────────┘  │
              └────────┼────────────────────────────────────┘
                       │ Message routing
     ┌─────────────────┼─────────────────────┐
     │                 │                     │
  ┌──▼──┐  ┌──────┐  ┌─▼───────┐  ┌───────┐ │  ┌────────┐
  │ WA  │  │ TG   │  │  Slack  │  │Discord│ │  │iMessage│
  └─────┘  └──────┘  └─────────┘  └───────┘ │  └────────┘
  WhatsApp Telegram                          └── ... 20+ more
```

Messages flow: Messaging platform → Gateway → Agent session → AI model → response back through channel.

### 4.2 Guiding Principles

1. **Local-first, remote-by-choice**: Gateway binds to `127.0.0.1:18789` by default. Remote access is an intentional configuration step using Tailscale, not a default-on feature.

2. **Workspace isolation as a feature**: Each agent workspace is independent. Use `AGENTS.md` and `SOUL.md` per workspace to scope agent behavior rather than relying on global config.

3. **Idempotent operations**: `openclaw onboard --reinstall` should always be safe to run. Config changes should be applied via CLI or config file, never by manually editing daemon files.

---

