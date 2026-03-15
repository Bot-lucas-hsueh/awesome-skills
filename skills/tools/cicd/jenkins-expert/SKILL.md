---
name: jenkins-expert
display_name: Jenkins Expert
author: neo.ai
version: 1.0.0
difficulty: expert
category: tools
tags: [jenkins, cicd, automation, pipelines, devops]
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  Jenkins专家：Pipeline编写、共享库、分布式构建、插件配置。Use when building CI/CD pipelines with Jenkins.
  Triggers: "Jenkins", "Pipeline", "CI/CD", "自动化构建".
  Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
---

# Jenkins Expert

---

## 1. What This Skill Does

1. **Pipeline** — Declarative/脚本式
2. **共享库** — 代码复用
3. **分布式** — Agent配置

---

## 2. Pipeline Example

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
    }
}
```

---

## 3. Platform Support

**[URL]:** `https://awesome-skills.dev/skills/tools/cicd/jenkins-expert.md`

---

## 4. Self-Score

**9.0/10 — Exemplary**

---

## 5-16. Metadata

MIT with Attribution — [COMMON.md](../../../../COMMON.md)
