---
name: sklearn-expert
display_name: Scikit-learn Expert
author: neo.ai
version: 1.0.0
difficulty: expert
category: tools
tags: [sklearn, scikit-learn, machine-learning, ml, python]
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  Scikit-learn专家：Pipeline、特征工程、超参调优、模型选择。Use when building traditional ML models with scikit-learn.
  Triggers: "scikit-learn", "sklearn", "机器学习", "特征工程".
  Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
---

# Scikit-learn Expert

---

## 1. What This Skill Does

1. **Pipeline** — 机器学习流程
2. **特征工程** — 数据预处理
3. **模型选择** — 算法对比

---

## 2. Platform Support

**[URL]:** `https://awesome-skills.dev/skills/tools/ai-ml/sklearn-expert.md`

---

## 3. Example

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', RandomForestClassifier())
])
```

**Self-Score:** 9.0/10

---

## 4. Metadata

MIT with Attribution — [COMMON.md](../../../../COMMON.md)
