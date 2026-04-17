## § 5 · Platform Support

| Platform | Session Install | Persistent Config |
|----------|----------------|-------------------|
| **OpenCode** | `/skill install insurance-agent` | Auto-saved to `~/.opencode/skills/` |
| **OpenClaw** | Read `[URL]` and install as skill | Auto-saved to `~/.openclaw/workspace/skills/` |
| **Claude Code** | Read `[URL]` and install as skill | Append to `~/.claude/CLAUDE.md` (global) or `./CLAUDE.md` (project) |
| **Cursor** | Paste §1 into `.cursorrules` | Save to `~/.cursor/rules/insurance-agent.mdc` (global) |
| **OpenAI Codex** | Paste §1 into system prompt | `~/.codex/config.yaml` → `system_prompt:` field |
| **Cline** | Paste §1 into Custom Instructions | Append to `.cursorrules` (project-level) |
| **Kimi Code** | Read `[URL]` and install as skill | Append to `.kimi-rules` |

**[URL]:** `https://awesome-skills.dev/skills/finance/insurance-agent.md`
**Raw URL:** `https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/finance/insurance-agent/SKILL.md`

---