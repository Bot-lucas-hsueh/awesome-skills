---
name: slack-bot-expert
display_name: Slack Bot Expert
author: neo.ai
version: 1.0.0
difficulty: expert
category: tools
tags: [slack, bot, automation, chatops, integration]
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  Slack Bot专家：Bolt SDK开发、Slash命令、工作流自动化。Use when building Slack bots, automating notifications, or creating chatops workflows.
  Triggers: "Slack Bot", "Bolt", "Slack集成", "ChatOps".
  Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
---

# Slack Bot Expert

---

## 1. What This Skill Does

1. **Bot开发** — Bolt SDK
2. **命令** — Slash commands
3. **工作流** — Workflow builder

---

## 2. Bolt Example

```python
from slack_bolt import App

app = App(token="xoxb-...")

@app.message("hello")
def message_hello(message, say):
    say(f"Hey <@{message['user']}>!")

app.start()
```

---

## 3. Platform Support

**[URL]:** `https://awesome-skills.dev/skills/tools/productivity/slack-bot-expert.md`

---

## 4. Self-Score

**9.0/10 — Exemplary**

---

## 5-16. Metadata

MIT with Attribution — [COMMON.md](../../../../COMMON.md)
