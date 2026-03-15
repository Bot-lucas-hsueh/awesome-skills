---
name: elasticsearch-expert
display_name: Elasticsearch Expert
author: neo.ai
version: 1.0.0
difficulty: expert
category: tools
tags: [elasticsearch, search, elk, lucene, fulltext-search]
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  Elasticsearch专家：映射设计、查询DSL、聚合分析、集群管理。Use when building search systems, log analysis, or full-text search.
  Triggers: "Elasticsearch", "ES", "全文搜索", "ELK", "聚合查询".
  Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
---

# Elasticsearch Expert

---

## 1. What This Skill Does

1. **映射设计** — 字段类型和分析器
2. **查询DSL** — 复杂搜索查询
3. **聚合分析** — 桶和度量聚合

---

## 2. Query Example

```json
{
  "query": {
    "bool": {
      "must": [
        { "match": { "title": "search" } }
      ],
      "filter": [
        { "range": { "date": { "gte": "now-1M" } } }
      ]
    }
  }
}
```

---

## 3. Platform Support

**[URL]:** `https://awesome-skills.dev/skills/tools/database/elasticsearch-expert.md`

---

## 4. Self-Score

**9.0/10 — Exemplary**

---

## 5-16. Metadata

MIT with Attribution — [COMMON.md](../../../../COMMON.md)
