## § 4 · Core Philosophy

### 4.1 Development Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                    SKILL DEVELOPMENT PIPELINE                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌────────┐  │
│  │  ISSUE   │───▶│  BRANCH  │───▶│  COMMIT  │───▶│  PR    │  │
│  │  CREATE  │    │  CREATE  │    │  VALIDATE│    │  MERGE │  │
│  └──────────┘    └──────────┘    └──────────┘    └────────┘  │
│       │               │               │               │          │
│       ▼               ▼               ▼               ▼          │
│  [ ] Template   [ ] Naming     [ ] 16-section   [ ] CI Pass   │
│  [ ] Scope      [ ] Base       [ ] YAML valid    [ ] Score≥9   │
│  [ ] Priority   [ ] PR #       [ ] Rubric calc  [ ] Review    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Automated Gates**: Every quality check runs in CI; no manual review can bypass
2. **Score as Contract**: A skill's score is a promise to users; don't break it
3. **Commit Atomicity**: One skill per commit; one logical change per PR
4. **Traceable Decisions**: Every merge links to a tracked issue or RFC

---

