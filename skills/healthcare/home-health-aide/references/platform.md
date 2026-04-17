## § 5 · Platform Support

| Platform | Session Install | Persistent Config |
|----------|-----------------|-------------------|
| **OpenCode** | `/skill install home-health-aide` | Auto-saved to `~/.opencode/skills/` |
| **OpenClaw** | `Read [URL] and install as skill` | Auto-saved to `~/.openclaw/workspace/skills/` |
| **Claude Code** | `Read [URL] and install as skill` | Append to `~/.claude/CLAUDE.md` (global) |
| **Cursor** | Paste §1 into `.cursorrules` | Save to `~/.cursor/rules/home-health-aide.mdc` |
| **OpenAI Codex** | Paste §1 into system prompt | `~/.codex/config.yaml` → `system_prompt:` field |
| **Cline** | Paste §1 into Custom Instructions | Append to `.clinerules` (project-level) |
| **Kimi Code** | `Read [URL] and install as skill` | Append to `.kimi-rules` |

**[URL]:** `https://awesome-skills.dev/skills/healthcare/home-health-aide.md`
