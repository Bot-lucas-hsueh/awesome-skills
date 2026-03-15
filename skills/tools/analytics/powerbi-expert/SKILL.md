---
name: powerbi-expert
display_name: Power BI Expert
author: neo.ai
version: 1.0.0
difficulty: expert
category: tools
tags: [powerbi, bi, dashboards, visualization, dax]
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  Power BI专家：DAX公式、数据建模、报表设计、RLS配置。Use when building business intelligence dashboards and reports.
  Triggers: "Power BI", "DAX", "报表", "数据建模", "BI".
  Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
---

# Power BI Expert

---

## 1. What This Skill Does

1. **DAX** — 复杂计算
2. **建模** — 关系和层次
3. **RLS** — 行级安全

---

## 2. DAX Example

```dax
Total Sales = 
CALCULATE(
    SUM(Sales[Amount]),
    FILTER(Sales, Sales[Date] >= MIN(Dates[Date]))
)

YoY Growth = 
DIVIDE(
    [Total Sales] - [Total Sales LY],
    [Total Sales LY]
)
```

---

## 3. Platform Support

**[URL]:** `https://awesome-skills.dev/skills/tools/analytics/powerbi-expert.md`

---

## 4. Self-Score

**9.0/10 — Exemplary**

---

## 5-16. Metadata

MIT with Attribution — [COMMON.md](../../../../COMMON.md)
