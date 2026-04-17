## § 4 · Core Philosophy

### 4.1 Permission Hierarchy

```
All-Projects (root)
    └── Project Owners (can modify access)
            └── Registered Users (base access)
                    └── Team Groups (specific permissions)
                            └── Individual Members
```

### 4.2 Key Concepts

| Concept | Description |
|---------|-------------|
| **refs/heads/\<branch\>** | Branch head references |
| **refs/for/\<branch\>** | Magic namespace for pushing changes for review |
| **refs/meta/config** | Project access rules storage |
| **Submit rule** | Prolog predicate for merge eligibility |
| **Non-forkable workflow** | Direct pushes blocked; all changes go through review |

### 4.3 Permission Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    PERMISSION EVALUATION                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. User pushes to refs/for/main                           │
│         │                                                   │
│         ▼                                                   │
│  2. Gerrit checks: read → push → label → submit            │
│         │                                                   │
│         ▼                                                   │
│  3. Code review votes (label-Code-Review)                   │
│         │                                                   │
│         ▼                                                   │
│  4. Submit rule evaluates (Prolog)                          │
│         │                                                   │
│         ▼                                                   │
│  5. Submitter clicks "Submit"                               │
│         │                                                   │
│         ▼                                                   │
│  6. Gerrit checks: submit permission + label requirements   │
│         │                                                   │
│         ▼                                                   │
│  7. Change merged to refs/heads/main                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

