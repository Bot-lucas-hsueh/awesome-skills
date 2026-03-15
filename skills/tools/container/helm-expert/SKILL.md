---
name: helm-expert
display_name: Helm Expert
author: neo.ai
version: 1.0.0
difficulty: expert
category: tools
tags: [helm, kubernetes, k8s, package-manager, devops]
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  Helm专家：chart开发、values配置、模板化Kubernetes部署。Use when managing Kubernetes applications with Helm.
  Triggers: "Helm", "Helm chart", "kubernetes部署", "helm template".
  Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
---

# Helm Expert

---

## 1. What This Skill Does

1. **Chart开发** — 创建Helm charts
2. **模板编写** — Go模板语法
3. **发布管理** — 版本和发布流程

---

## 2. Chart Structure

```
chart/
├── Chart.yaml
├── values.yaml
├── templates/
│   └── deployment.yaml
└── charts/
```

---

## 3. Platform Support

**[URL]:** `https://awesome-skills.dev/skills/tools/container/helm-expert.md`

---

## 4. Commands

```bash
helm create mychart
helm install myapp ./chart
helm upgrade myapp ./chart
helm rollback myapp 1
```

---

## 5-16. Metadata

**Self-Score:** 9.0/10 — Exemplary

MIT with Attribution — [COMMON.md](../../../../COMMON.md)
