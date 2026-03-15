# Skill Writer — Anti-Patterns / 常见陷阱与反模式

Full anti-pattern catalog for §10. Load this file when reviewing a skill for quality issues or when the user asks about common mistakes.

---

## 🔴 High Severity / 高严重度

**#1 Scope Sprawl / 范围蔓延**
```
❌ "This skill covers: software architecture, DevOps, cloud engineering,
    database design, security, and AI/ML systems..."

✅ "This skill focuses on software architecture. For DevOps, see
    devops-engineer.md. For security, see security-engineer.md."
```

**#2 Shallow Depth / 缺乏深度**
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

**#3 Self-Inconsistency / 自身不一致**
```
❌ A skill that teaches "all skills must have complete metadata"
   but its own metadata is missing fields.
   A skill that defines a 16-section checklist but uses a different structure.

✅ The skill is the best exemplar of everything it teaches.
   Run the 16-section checklist against skill-writer itself before each release.
```

---

## 🟡 Medium Severity / 中严重度

**#4 Token Waste / Token 浪费**
```
❌ Full 57-category directory tree (50+ lines of static reference)

✅ Compact domain-grouped table (8 lines) + "browse /skills/ if unsure"
   + heavy reference tables → references/ files (on-demand loading)
```

**#5 Generic Risk Table / 通用风险表**
```
❌ | Risk       | Mitigation   |
   | Accuracy   | Verify outputs |

✅ | Risk                         | Mitigation |
   | Hallucinated Drug Interaction | Cross-reference FDA database; never prescribe without pharmacist review |
```

**#6 HTML Comments in YAML / YAML 中的 HTML 注释**
```
❌ description: >
     Expert skill for X.
     <!-- 专家技能用于 X。 -->

✅ description: >
     Expert skill for X. Use when [trigger conditions].
     Triggers: "keyword1", "keyword2"
   # Bilingual content belongs in the Markdown body only
```

---

## 🟢 Low Severity / 低严重度

**#7 Literal Translation / 直译**
```
❌ "Think outside the box" → "想象在盒子外"
✅ "Think outside the box" → "突破常规思维"
```

**#8 Prose Wall / 大段散文**
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
