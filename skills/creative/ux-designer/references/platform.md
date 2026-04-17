## § 5 · Platform Support

| Platform | Session Install | Persistent Config |
|----------|-----------------|-------------------|
| **OpenCode** | `/skill install ux-designer` | Auto-saved to `~/.opencode/skills/` |
| **OpenClaw** | `Read [URL] and apply ux-designer skill` | Auto-saved to `~/.openclaw/workspace/skills/` |
| **Claude Code** | `Read [URL] and apply ux-designer skill` | Append to `~/.claude/CLAUDE.md` (global) |
| **Cursor** | Paste §1 into `.cursorrules` | Save to `~/.cursor/rules/ux-designer.mdc` (global) |
| **OpenAI Codex** | Paste §1 into system prompt | `~/.codex/config.yaml` → `system_prompt:` field |
| **Cline** | Paste §1 into Custom Instructions | Append to `.clinerules` (project-level) |
| **Kimi Code** | `Read [URL] and apply ux-designer skill` | Append to `.kimi-rules` |

**[URL]:** `https://awesome-skills.dev/skills/creative/ux-designer.md`

Quick install (Claude Code):
```bash
echo "Read [URL] and apply ux-designer skill." >> ~/.claude/CLAUDE.md
```

---
