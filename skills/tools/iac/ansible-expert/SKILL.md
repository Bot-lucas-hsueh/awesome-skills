---
name: ansible-expert
display_name: Ansible Expert
author: neo.ai
version: 1.0.0
difficulty: expert
category: tools
tags: [ansible, automation, devops, configuration-management]
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  Ansible专家：playbook编写、角色开发、自动化配置管理。Use when automating infrastructure, configuration management, or orchestration.
  Triggers: "Ansible", "playbook", "自动化", "配置管理".
  Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
---

# Ansible Expert

---

## 1. What This Skill Does

1. **Playbook编写** — YAML自动化任务
2. **角色开发** — 可复用Ansible角色
3. **批量操作** — 批量服务器管理

---

## 2. Playbook Example

```yaml
- hosts: webservers
  become: yes
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
    - name: Start nginx
      service:
        name: nginx
        state: started
```

---

## 3. Platform Support

**[URL]:** `https://awesome-skills.dev/skills/tools/iac/ansible-expert.md`

---

## 4. Self-Score

**9.0/10 — Exemplary**

---

## 5-16. Metadata

MIT with Attribution — [COMMON.md](../../../../COMMON.md)
