# Skill Writer — Installation Guide

> Install once, persist across all sessions. Supports 7 platforms.
>

**Quick install:**
```
Read https://awesome-skills.dev/skills/special/skill-writer/SKILL.md and activate the Skill Writer role from §1
```

> **`[URL]`** = `https://awesome-skills.dev/skills/special/skill-writer/SKILL.md`
> **`§1`** = `## 1. System Prompt` section in SKILL.md

---

## OpenCode

```bash
# Install
/skill install skill-writer

# Auto-persisted to: ~/.opencode/skills/skill-writer/
```

---

## OpenClaw

```
Read https://awesome-skills.dev/skills/special/skill-writer/SKILL.md and install as skill
```

Auto-persisted to `~/.openclaw/workspace/skills/`.
---

## Claude Code

**Session only:**
```
Read https://awesome-skills.dev/skills/special/skill-writer/SKILL.md and activate the Skill Writer role from §1
```

**Persistent — global (all projects):**
```bash
echo "Read https://awesome-skills.dev/skills/special/skill-writer/SKILL.md and activate the Skill Writer role from §1." >> ~/.claude/CLAUDE.md
```

**Persistent — project level:**
```bash
echo "Read https://awesome-skills.dev/skills/special/skill-writer/SKILL.md and activate the Skill Writer role from §1." >> ./CLAUDE.md
```

> ⚠️ Global install applies to ALL projects. Project install only affects the current repo.
>

---

## Cursor

**Project-level (.cursorrules):**
```bash
curl -s https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/special/skill-writer/SKILL.md >> .cursorrules
```

**Global (all projects):**
1. Create file: `~/.cursor/rules/skill-writer.mdc`
2. Paste the §1 System Prompt block from `SKILL.md`
---

## OpenAI Codex

**Session:** Paste the §1 System Prompt block into the system prompt field.

**Persistent** — add to `~/.codex/config.yaml`:
```yaml
system_prompt: |
  [Paste §1 System Prompt content here]
```

---

## Cline (VS Code)

**Session:** Paste §1 System Prompt into Cline's **Custom Instructions** field (Settings → Cline → Custom Instructions).

**Persistent (project):**
```bash
curl -s https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/special/skill-writer/SKILL.md >> .clinerules
```

---

## Kimi Code

**Session:**
```
Read https://awesome-skills.dev/skills/special/skill-writer/SKILL.md and install as skill
```

**Persistent:**
```bash
echo "Read https://awesome-skills.dev/skills/special/skill-writer/SKILL.md and install as skill." >> .kimi-rules
```

---

## Verification

After install, test with any trigger phrase:
| Test Input| Expected Behavior|
|----------------------|------------------------------|
| "write a skill for [domain]" | Phase 1 discovery questions; scope + tier confirmation |
| "review [path/to/skill.md]" | 6-dimension rubric scorecard with weighted score |
| "upgrade [path/to/skill.md]" | Priority fix list ordered by ROI |
| "score this skill" | Tier classification + top 3 improvement suggestions |

---

## Uninstall

| Platform | Command / Action |
|----------|-----------------|
| **OpenCode** | `/skill uninstall skill-writer` |
| **Claude Code (global)** | Remove the `Read ...skill-writer/SKILL.md...` line from `~/.claude/CLAUDE.md` |
| **Claude Code (project)** | Remove the line from `./CLAUDE.md` |
| **Cursor** | Delete entry from `.cursorrules` or remove `~/.cursor/rules/skill-writer.mdc` |
| **Cline** | Remove from Custom Instructions or `.clinerules` |
| **Kimi** | Remove the line from `.kimi-rules` |

---

**Trigger words:** "write skill" · "create skill" · "review skill" · "score skill" · "upgrade skill"
