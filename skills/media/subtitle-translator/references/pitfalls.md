## 10. Common Pitfalls & Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **Translating from transcript only** | 🔴 High | Always reference video; transcript lacks timing and context |
| 2 | **Exceeding reading speed** | 🔴 High | Check CPS for every line; use QA tools |
| 3 | **Splitting sentences mid-word** | 🟡 Medium | Line break should occur at natural pause |
| 4 | **Inconsistent character names** | 🟡 Medium | Create glossary; use search/replace to fix |
| 5 | **Missing speaker IDs in SDH** | 🟡 Medium | Every speaker change needs ID tag |
| 6 | **Orphan words on line 2** | 🟢 Low | If line 2 has single word, combine with line 1 or split differently |

```
❌ "He's going to the store to buy some milk for the kids because"
✅ Split at natural pause: "He's going to the store

❌ [All dialogue, no speaker ID in SDH]
✅ [JOHN] I thought you were coming yesterday.
   [SARAH] I was, but the flight was delayed.

❌ 52 characters in one line for Netflix
✅ Split: "The government has announced new regulations
```

