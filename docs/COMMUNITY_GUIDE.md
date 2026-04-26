# 🤝 社区与贡献指南 | Community & Contributing

## 中文

### 📊 社区数据看板

```
📈 核心指标
├─ 总技能数：943 ✅
├─ PLATINUM 技能：12 ⭐⭐⭐⭐⭐
├─ GOLD 技能：45 ⭐⭐⭐⭐
├─ SILVER 技能：88 ⭐⭐⭐
├─ 社区贡献者：127 人
├─ GitHub Stars：50 ⭐
├─ 月活跃用户：1,200+
└─ 周均新增技能：3-5 个

🌍 地区分布
├─ 北美：35%
├─ 欧洲：25%
├─ 亚洲：30%
├─ 其他：10%

💼 职业分布
├─ 工程师：40%
├─ 产品经理：15%
├─ 企业管理层：15%
├─ 数据科学家：12%
├─ 其他：18%
```

[→ 实时仪表板](https://github.com/theneoai/awesome-skills/graphs/traffic)

### 🏆 社区贡献者排行

**Top 10 Contributors (This Month)**

| 排名 | 贡献者 | 新增技能 | Pull Requests | Issues 解决 | 质量评分 |
|------|--------|--------|-------------|-----------|---------|
| 1 | @alice-tech | 5 | 8 | 3 | ⭐⭐⭐⭐⭐ |
| 2 | @bob-engineer | 4 | 6 | 5 | ⭐⭐⭐⭐ |
| 3 | @carol-pm | 3 | 5 | 2 | ⭐⭐⭐⭐⭐ |
| 4 | @david-data | 3 | 4 | 4 | ⭐⭐⭐⭐ |
| 5 | @eve-ml | 2 | 3 | 6 | ⭐⭐⭐⭐ |

[→ 查看完整排行](./TOP_CONTRIBUTORS.md)

### ✨ 如何贡献？

#### 方式 1: 添加新技能（最欢迎！）

**Step 1: Fork & Clone**
```bash
git clone https://github.com/YOUR_USERNAME/awesome-skills.git
cd awesome-skills
git checkout -b add/my-new-skill
```

**Step 2: 创建技能文件**
```
skills/
  └─ my-category/
       └─ my-role/
            ├─ SKILL.md          # 主文件
            ├─ references/       # 参考资料
            │   ├─ workflows.md
            │   └─ examples.md
            └─ EVALUATION_REPORT.md
```

**Step 3: 用 Skill Writer 优化**

```bash
# 或者在 Claude 中
"Read https://github.com/theneoai/skill-writer and 
help me optimize my skill to GOLD tier"
```

**Step 4: 提交 PR**
```bash
git add skills/
git commit -m "add: new skill for [role] in [category]"
git push origin add/my-new-skill
```

**Step 5: CI/CD 自动检查**
- ✅ 格式验证
- ✅ Token计数
- ✅ 反模式扫描
- ✅ 质量评分

[→ 详细技能创建指南](../CONTRIBUTING.md#添加新技能)

#### 方式 2: 改进现有技能

**最简单的方式：直接 Fork + Pull Request**

```bash
# 发现问题 → Edit → Commit → Push → PR
```

**常见改进方向：**
- 📝 完善文档和示例
- 🔧 添加 references/ 深度内容
- 📊 更新行业最新实践
- 🌍 添加多语言支持
- 🔐 增强安全性检查

[→ 改进指南](../CONTRIBUTING.md#改进现有技能)

#### 方式 3: 报告问题或建议

```bash
# GitHub Issues:
1. 标题要清晰："[BUG] CEO skill 没有 Working Backwards 框架"
2. 描述问题：提供复现步骤
3. 建议解决：如果有想法可以提出
```

[→ Issue 模板](https://github.com/theneoai/awesome-skills/issues/new)

### 🎁 贡献奖励

我们感谢每一个贡献者！

#### 认可方式
- ✅ 被添加到贡献者名单
- ⭐ 获得 "Top Contributor" Badge
- 📣 在月度通讯中宣传
- 🏆 最活跃贡献者有机会成为核心维护者

#### 实际奖励（正在计划）
- 💰 优秀技能有奖金（$100-500）
- 🎓 免费AI课程（Anthropic官方）
- 👔 职位推荐（加入赞助企业）

[→ 了解更多](./REWARDS.md)

### 📋 贡献检查清单

提交前，请确保：

- [ ] 技能符合模板格式
- [ ] 包含 references/ 目录（至少2个参考文件）
- [ ] YAML frontmatter 有 triggers（英文+中文）
- [ ] 包含 Negative Boundaries 部分
- [ ] 代码/示例 没有硬编码密钥
- [ ] 通过 CI 自动检查
- [ ] 用 Skill Writer 做过 LEAN 评估 (≥350分)
- [ ] 添加了自己的 GitHub 个人资料链接

[→ 完整检查清单](./CONTRIBUTION_CHECKLIST.md)

### 💬 社区讨论

#### GitHub Discussions (推荐)
```
📌 Announcements - 官方公告
💡 Ideas - 功能建议
🆘 Q&A - 问答区
🎉 Show and Tell - 展示你的技能
🐛 Troubleshooting - 问题排查
```

[→ 访问讨论区](https://github.com/theneoai/awesome-skills/discussions)

#### Discord 社区（即将开放）
```
#awesome-skills - 技能讨论
#skill-writer - 优化工具讨论
#awesome-mcps - 工具集成讨论
#showcase - 展示作品
#jobs - 职位发布
```

[→ 加入 Discord](https://discord.gg/theneoai)

### 🗺️ 项目路线图

#### Q2 2026 (现在)
- ✅ 基础1000+技能库
- ✅ Skill Writer 优化工具
- ✅ Awesome MCPs 集成
- 🔄 社区讨论启动

#### Q3 2026
- 📊 社区贡献排行榜
- 💰 贡献奖励计划
- 🎓 官方认证体系
- 🌍 多语言支持

#### Q4 2026
- 🏢 企业版本
- 📱 移动应用
- 🔗 第三方集成
- 🤖 自动技能生成

[→ 查看详细路线图](./ROADMAP.md)

### 📞 联系方式

**问题反馈：**
- GitHub Issues: https://github.com/theneoai/awesome-skills/issues
- Discussions: https://github.com/theneoai/awesome-skills/discussions

**直接联系：**
- Twitter: @theneoai
- Email: hello@theneoai.com

**加入社区：**
- Discord: https://discord.gg/theneoai
- Newsletter: [订阅](https://theneoai.substack.com/)

---

## English

### How to Contribute?

#### Method 1: Add a New Skill (Most Welcome!)

**Step 1: Fork & Clone**
```bash
git clone https://github.com/YOUR_USERNAME/awesome-skills.git
cd awesome-skills
git checkout -b add/my-new-skill
```

**Step 2: Create Skill Files**
```
skills/
  └─ my-category/
       └─ my-role/
            ├─ SKILL.md          # Main file
            ├─ references/       # Reference materials
            └─ EVALUATION_REPORT.md
```

**Step 3: Optimize with Skill Writer**

In Claude:
```
"Read https://github.com/theneoai/skill-writer and 
help me optimize my skill to GOLD tier"
```

**Step 4: Submit PR**

**Step 5: CI/CD Auto-checks**
- ✅ Format validation
- ✅ Token counting
- ✅ Anti-pattern scan
- ✅ Quality scoring

[→ Full Skill Creation Guide](../CONTRIBUTING.md)

### Contribution Rewards

We appreciate every contributor!

#### Recognition
- ✅ Added to contributors list
- ⭐ "Top Contributor" Badge
- 📣 Featured in monthly newsletter
- 🏆 Potential core maintainer role

#### Incentives (In Planning)
- 💰 Cash rewards for excellent skills ($100-500)
- 🎓 Free AI courses (Anthropic official)
- 👔 Job referrals (Partner companies)

[→ Learn More](./REWARDS.md)

### Community Discussion Channels

**GitHub Discussions (Recommended)**
- 📌 Announcements
- 💡 Ideas
- 🆘 Q&A
- 🎉 Show and Tell

**Discord Community (Coming Soon)**
- #awesome-skills
- #skill-writer
- #showcase
- #jobs

[→ Join Discord](https://discord.gg/theneoai)
