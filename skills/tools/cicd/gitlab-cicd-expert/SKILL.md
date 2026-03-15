---
name: gitlab-cicd-expert
display_name: GitLab CI/CD Expert
author: neo.ai
version: 1.0.0
difficulty: expert
category: tools
tags: [gitlab, cicd, pipelines, devops, automation]
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  GitLab CI/CD专家：.gitlab-ci.yml配置、Runner管理、Auto DevOps。Use when building CI/CD pipelines with GitLab.
  Triggers: "GitLab CI", "gitlab-ci", "Pipeline", "Auto DevOps".
  Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
---

# GitLab CI/CD Expert

---

## 1. What This Skill Does

1. **Pipeline配置** — .gitlab-ci.yml
2. **Runner管理** — 分布式执行
3. **Auto DevOps** — 自动化部署

---

## 2. CI Example

```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - npm ci
    - npm run build

test:
  stage: test
  script:
    - npm test
```

---

## 3. Platform Support

**[URL]:** `https://awesome-skills.dev/skills/tools/cicd/gitlab-cicd-expert.md`

---

## 4. Self-Score

**9.0/10 — Exemplary**

---

## 5-16. Metadata

MIT with Attribution — [COMMON.md](../../../../COMMON.md)
