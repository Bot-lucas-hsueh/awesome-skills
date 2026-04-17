## 5. Platform Support

### Supported Agents

| Agent | Compatibility | Notes |
|-------|-------------|-------|
| Claude Code | ✅ Full | Tested with code analysis, workflow execution |
| OpenCode | ✅ Full | Tested with file operations, skill loading |
| Cursor | ✅ Full | Works with Cursor's agent mode |
| Cline | ✅ Full | Compatible with Cline's skill system |
| OpenClaw | ✅ Full | Supports skill loading via config |
| Kimi | ✅ Full | Compatible with Kimi's agent framework |
| Codex | ✅ Full | Works with OpenAI Codex |
| Generic | ✅ Full | Any agent supporting skill markdown format |

### Installation

No installation required — skills are loaded directly into your agent's context. Copy `SKILL.md` into your agent's skills directory or load via the agent's skill management command.

### Configuration

For best results, ensure your agent has:
- Read/write access to project files
- Ability to execute shell commands (for workflow validation)
- Sufficient context window (>32K tokens recommended)

### References

- Skill Loading Guide → See agent-specific documentation
