# Awesome Skills Refs

社区AI Agent Skills收集与评估仓库

## 简介

本仓库收集了来自多个渠道的AI Agent Skills资源，并使用自动化评估工具对每个Skill进行了安全性和质量评估。

## 数据来源渠道

| 渠道 | 仓库/来源 |
|------|-----------|
| **GitHub** | gmh5225/awesome-skills, BehiSecc/awesome-claude-skills, travisvn/awesome-claude-skills |
| **OpenAI** | openai/skills |
| **OpenCode** | awesome-opencode/awesome-opencode, viliamvolosv/n8n-opencode-skill |
| **Claude** | VoltAgent/awesome-claude-skills |
| **Community** | k1lgor/virtual-company |

## 评估结果摘要

- **评估Skills总数**: 81个
- **安全Skills数量**: 81个 (100%)
- **平均得分**: 96.5/100

### 按来源统计

| 来源 | Skills数量 | 平均得分 | 质量评级 |
|------|------------|----------|----------|
| OpenAI | 39 | 98.0 | ⭐⭐⭐⭐⭐ |
| GitHub | 8 | 94.9 | ⭐⭐⭐⭐⭐ |
| Community | 27 | 94.7 | ⭐⭐⭐⭐⭐ |
| OpenCode | 7 | 94.3 | ⭐⭐⭐⭐⭐ |

### Top 10 推荐Skills

| 名称 | 来源 | 得分 |
|------|------|------|
| skill-creator | OpenAI | 100 |
| security-threat-model | OpenAI | 100 |
| sora | OpenAI | 100 |
| spreadsheet | OpenAI | 100 |
| jupyter-notebook | OpenAI | 100 |
| speech | OpenAI | 100 |
| render-deploy | OpenAI | 100 |
| gh-fix-ci | OpenAI | 100 |
| imagegen | OpenAI | 100 |
| pdf | OpenAI | 99 |

## 目录结构

```
external/
├── README.md                          # 本文件
├── SKILLS_EVALUATION_REPORT.md        # 详细评估报告
├── skills_evaluation_data.json        # JSON格式评估数据
├── skill_evaluator.py                 # 评估脚本
│
├── github-awesome-skills/             # GitHub Awesome Skills
├── openai-skills/                     # OpenAI官方Skills
├── opencode-awesome/                  # OpenCode Awesome
├── n8n-opencode-skills/               # n8n OpenCode Skills
├── voltagent-awesome-skills/          # VoltAgent Awesome Skills
├── virtual-company-skills/            # Virtual Company Skills
├── behisecc-awesome-skills/           # BehiSecc Awesome Skills
├── travisvn-awesome-skills/           # TravisVN Awesome Skills
└── skill-evaluator/                   # Skill Evaluator工具
```

## 评估方法论

本仓库使用自定义的`skill_evaluator.py`脚本对Skills进行多维度评估：

### 评估维度

1. **提示注入安全 (Prompt Injection)**: 检测SKILL.md中是否存在试图覆盖系统提示、角色操纵或隐藏指令的恶意模式
2. **代码安全 (Code Safety)**: 分析scripts/目录中的可执行代码，检测恶意代码模式、不安全的系统调用等
3. **数据隐私 (Data Privacy)**: 评估skill是否存在数据收集、外泄或凭证窃取的风险
4. **来源信任 (Source Trust)**: 基于来源的可靠性进行评分（官方>知名公司>社区）
5. **功能性 (Functionality)**: 评估skill的文档完整性、使用说明清晰度等

### 评分标准

- **85-100分 (SAFE)**: 安全，推荐使用
- **70-84分 (USE_WITH_CAUTION)**: 可以使用，但建议审查
- **50-69分 (NOT_RECOMMENDED)**: 不建议使用，存在风险
- **0-49分 (DANGEROUS)**: 危险，请勿使用

## 使用评估工具

```bash
# 运行评估脚本
python3 skill_evaluator.py

# 查看详细报告
cat SKILLS_EVALUATION_REPORT.md
```

## 免责声明

本评估结果基于自动化脚本分析，仅供参考。在使用任何第三方Skill之前，建议进行人工审查。作者不对使用本仓库中任何Skill造成的后果承担责任。

## 许可证

各Skills的许可证以其原始仓库为准。评估脚本采用MIT许可证。

## 贡献

欢迎提交PR来：
- 添加新的Skills来源
- 改进评估脚本
- 更新评估报告

---

**最后更新**: 2026-03-22
