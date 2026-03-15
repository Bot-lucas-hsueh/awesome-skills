# Skill Writer — Installation Guide / 安装指南

> Install once, persist across all sessions. Supports 7 platforms.
> <!-- 安装一次，跨会话持久生效。支持 7 个平台。-->

**Quick install (any platform) / 任意平台快速安装:**
```
Read https://awesome-skills.dev/skills/special/skill-writer/SKILL.md and activate the Skill Writer role from §1
```

---

## OpenCode

```bash
# Install / 安装
/skill install skill-writer

# Auto-persisted to / 自动持久化至:
~/.opencode/skills/skill-writer/
```

---

## OpenClaw

```
Read https://awesome-skills.dev/skills/special/skill-writer/SKILL.md and install as skill
```

Auto-persisted to `~/.openclaw/workspace/skills/`.
<!-- 自动持久化至 ~/.openclaw/workspace/skills/ -->

---

## Claude Code

**Session only / 仅当前会话:**
```
Read https://awesome-skills.dev/skills/special/skill-writer/SKILL.md and activate the Skill Writer role from §1
```

**Persistent — global (all projects) / 全局持久化（所有项目）:**
```bash
echo "Read https://awesome-skills.dev/skills/special/skill-writer/SKILL.md and activate the Skill Writer role from §1." >> ~/.claude/CLAUDE.md
```

**Persistent — project level / 项目级持久化:**
```bash
echo "Read https://awesome-skills.dev/skills/special/skill-writer/SKILL.md and activate the Skill Writer role from §1." >> ./CLAUDE.md
```

> ⚠️ Global install applies to ALL projects. Project install only affects the current repo.
> <!-- ⚠️ 全局安装适用于所有项目；项目级安装仅影响当前仓库。-->

---

## Cursor

**Project-level (.cursorrules):**
```bash
curl -s https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/special/skill-writer/SKILL.md >> .cursorrules
```

**Global (all projects):**
1. Create file: `~/.cursor/rules/skill-writer.mdc`
2. Paste the §1 System Prompt block from `SKILL.md`
<!-- 全局安装：创建 ~/.cursor/rules/skill-writer.mdc，粘贴 SKILL.md 中的 §1 系统提示词 -->

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

## Verification / 验证安装效果

After install, test with any trigger phrase:
<!-- 安装后，使用任意触发短语验证效果：-->

| Test Input / 测试输入 | Expected Behavior / 预期行为 |
|----------------------|------------------------------|
| "write a skill for [domain]" | Phase 1 discovery questions; scope + tier confirmation |
| "review [path/to/skill.md]" | 6-dimension rubric scorecard with weighted score |
| "upgrade [path/to/skill.md]" | Priority fix list ordered by ROI |
| "score this skill" | Tier classification + top 3 improvement suggestions |

---

## Uninstall / 卸载

| Platform | Command / Action |
|----------|-----------------|
| **OpenCode** | `/skill uninstall skill-writer` |
| **Claude Code (global)** | Remove the `Read ...skill-writer/SKILL.md...` line from `~/.claude/CLAUDE.md` |
| **Claude Code (project)** | Remove the line from `./CLAUDE.md` |
| **Cursor** | Delete entry from `.cursorrules` or remove `~/.cursor/rules/skill-writer.mdc` |
| **Cline** | Remove from Custom Instructions or `.clinerules` |
| **Kimi** | Remove the line from `.kimi-rules` |

---

**Trigger words / 触发词:** "write skill" · "create skill" · "review skill" · "score skill" · "upgrade skill"
