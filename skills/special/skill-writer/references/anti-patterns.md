# Skill Writer — Anti-Patterns

Full anti-pattern catalog for §10. Load this file when reviewing a skill for quality issues or when the user asks about common mistakes.

---

## 🔴 High Severity

**#1 Scope Sprawl**
```
❌ "This skill covers: software architecture, DevOps, cloud engineering,
    database design, security, and AI/ML systems..."

✅ "This skill focuses on software architecture. For DevOps, see
    devops-engineer.md. For security, see security-engineer.md."
```

**#2 Shallow Depth**
```
❌ ## Core Philosophy
   1. Write clean code
   2. Follow best practices
   3. Test your code

✅ ## Core Philosophy
   1. Separation of Concerns: Each module has one reason to change
      - Apply at: function (SRP), module (package), service (bounded context)
   2. Fail Fast: Detect errors at compile > startup > request > runtime
      - Use types over runtime checks: `UserId` not `string`
```

**#3 Self-Inconsistency**
```
❌ A skill that teaches "all skills must have complete metadata"
   but its own metadata is missing fields.
   A skill that defines a 16-section checklist but uses a different structure.

✅ The skill is the best exemplar of everything it teaches.
   Run the 16-section checklist against skill-writer itself before each release.
```

---

## 🟡 Medium Severity

**#4 Token Waste**
```
❌ Full 57-category directory tree (50+ lines of static reference)

✅ Compact domain-grouped table (8 lines) + "browse /skills/ if unsure"
   + heavy reference tables → references/ files (on-demand loading)
```

**#5 Generic Risk Table**
```
❌ | Risk       | Mitigation   |
   | Accuracy   | Verify outputs |

✅ | Risk                         | Mitigation |
   | Hallucinated Drug Interaction | Cross-reference FDA database; never prescribe without pharmacist review |
```

**#6 HTML Comments in YAML**
```
❌ description: >
     Expert skill for X.
     <!-- 专家技能用于 X。 -->
✅ description: >
     Expert skill for X. Use when [trigger conditions].
     Triggers: "keyword1", "keyword2"
   # Bilingual content belongs in the Markdown body only
```

**#9 Platform Coverage Miss**
```
❌ ## 5. Platform Support
   | Platform  | Installation             |
   | Claude Code | Read URL and install   |
   | Cursor    | Copy §1 into .cursorrules |
   (Missing: OpenCode, OpenClaw, Codex, Cline, Kimi)
   (No persistent install options for any platform)

✅ ## 5. Platform Support
   | Platform      | Session Install              | Persistent Config               |
   | OpenCode      | /skill install [name]        | Auto-saved to ~/.opencode/skills/ |
   | OpenClaw      | Read [URL] and install       | Auto-saved to ~/.openclaw/...   |
   | Claude Code   | Read [URL] and install       | Append to ~/.claude/CLAUDE.md   |
   | Cursor        | Paste §1 into .cursorrules   | ~/.cursor/rules/[skill].mdc     |
   | OpenAI Codex  | Paste §1 into system prompt  | ~/.codex/config.yaml            |
   | Cline         | Paste §1 into Custom Instr.  | Append §1 to .clinerules        |
   | Kimi Code     | Read [URL] and install       | Append to .kimi-rules           |
   [URL]: https://awesome-skills.dev/skills/[category]/[skill-name].md
   (Rule: §7.11 — all 7 platforms; session + persistent; [URL] defined once)
```

---

## 🟢 Low Severity

**#7 Literal Translation**
```
❌ "Think outside the box" → "想象在盒子外"
✅ "Think outside the box" → "突破常规思维"
```

**#8 Prose Wall**
```
❌ ## Core Philosophy
   As a senior software architect, you should always consider scalability when
   designing systems. It is important to think about performance and make sure
   that the code is clean and maintainable...

✅ ## Core Philosophy
   | Principle           | Rule                         | Litmus Test                          |
   |---------------------|------------------------------|--------------------------------------|
   | Scalability-First   | Design for 10× current load  | Can this fail under peak?            |
   | Security by Default | Auth at every layer boundary | Is any endpoint unauthenticated?     |
   | Fail Fast           | Compile > startup > runtime  | Where does this fail silently?       |
```
