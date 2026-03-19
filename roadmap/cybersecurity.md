# 网络安全职业路径 Cybersecurity Roadmap

> 覆盖方向：安全工程师 · 渗透测试 · SOC分析师 · 安全架构师 · CISO

---

## 职业全景

```
网络安全
├── 攻击方向（红队/渗透）
│   ├── CTF选手 → 安全研究员 → 渗透测试工程师 → 高级渗透 → 红队负责人
│   └── 漏洞研究员 → 0day研究员 → 安全专家
├── 防御方向（蓝队/SOC）
│   ├── SOC分析师L1 → L2 → L3 → SOC经理 → 安全运营总监
│   ├── 事件响应工程师 → 威胁猎手 → 取证专家
│   └── 威胁情报分析师 → 高级威胁情报
├── 安全工程
│   ├── 安全工程师 → 高级安全工程师 → 安全架构师 → 首席安全架构师
│   └── DevSecOps工程师 → 安全平台工程师
├── 合规与风险
│   ├── 安全合规专员 → GRC经理 → 安全合规总监
│   └── 风险分析师 → 安全风险经理
└── 管理层
    └── 安全团队Lead → 安全总监 → VP Security → CISO
```

---

## ⚠️ 伦理声明

网络安全知识具有双重性。所有技术应仅用于：
- 授权的渗透测试和安全评估
- CTF（夺旗赛）竞赛
- 防御性安全建设
- 安全研究和教育

**未授权的攻击行为在任何国家均属违法。**

---

## 🌱 第1级 · 入门 (0-12个月)

### 基础知识体系
- [ ] **计算机网络**：TCP/IP协议栈、OSI模型、DNS、HTTP/HTTPS、TLS
- [ ] **操作系统**：Linux命令行熟练（Kali Linux推荐）、Windows基础
- [ ] **编程基础**：Python（脚本自动化）、Bash脚本
- [ ] **密码学基础**：对称/非对称加密、哈希函数、PKI

### 安全基础概念
- [ ] OWASP Top 10：SQL注入、XSS、CSRF、不安全配置等
- [ ] CIA三元组：保密性/完整性/可用性
- [ ] 攻击生命周期：侦察→武器化→投递→利用→持久化→横向移动→目标达成
- [ ] 基础防御：防火墙、IDS/IPS、WAF、SIEM

### 实践平台
- **TryHackMe**（适合初学者，有引导式学习路径）
- **HackTheBox Starting Point**（入门机器）
- **PicoCTF**（CTF入门）
- **OverTheWire**（Linux和网络挑战）

### 关键里程碑
- ✅ 完成TryHackMe初级学习路径（Pre-Security + Jr Penetration Tester）
- ✅ 在HackTheBox/TryHackMe解决10台Easy机器
- ✅ 参加第一次CTF竞赛（哪怕只解出1道题）
- ✅ 获得CompTIA Security+ 认证

### 常见陷阱 ⚠️
- 跳过网络基础直接学黑客工具：工具没用，知识才有用
- 只用现成工具不理解原理：遇到变化场景就束手无策
- 不建立学习笔记：安全领域知识太多，必须系统记录

---

## 🌿 第2级 · 初级 (1-3年)

### 渗透测试方向

**Web渗透**
- [ ] Burp Suite专业版熟练使用（拦截、重放、Intruder）
- [ ] SQL注入深入：Union注入、盲注、时间盲注
- [ ] XSS攻击链：存储型/反射型/DOM型，结合CSRF
- [ ] 文件包含漏洞（LFI/RFI）、文件上传漏洞
- [ ] 认证绕过：JWT伪造、OAuth攻击
- [ ] API安全测试：REST/GraphQL安全测试

**网络/系统渗透**
- [ ] 扫描工具：Nmap高级用法、Masscan
- [ ] 漏洞利用：Metasploit框架使用
- [ ] 权限提升：Linux本地提权技术（SUID、Cron、内核漏洞）
- [ ] Windows提权：服务漏洞、注册表、UAC绕过
- [ ] 密码攻击：Hashcat、John the Ripper、彩虹表

**报告写作**
- [ ] 渗透测试报告：执行摘要+技术细节+修复建议
- [ ] 漏洞严重性评级：CVSS评分理解

### SOC分析师方向

**L1分析师能力**
- [ ] SIEM使用：Splunk / Elastic / Microsoft Sentinel告警分析
- [ ] 事件分类和优先级评估
- [ ] IOC（失陷指标）识别：IP、域名、哈希值
- [ ] 基础事件响应流程：识别→遏制→清除→恢复

**威胁情报**
- [ ] MITRE ATT&CK框架：TTP映射
- [ ] 威胁情报平台：VirusTotal、Shodan、OSINT工具
- [ ] 网络流量分析：Wireshark、Zeek

### DevSecOps方向
- [ ] SAST工具：SonarQube、Semgrep代码扫描
- [ ] DAST工具：OWASP ZAP自动化扫描
- [ ] 容器安全：Docker镜像扫描（Trivy）、Kubernetes安全
- [ ] 密钥管理：HashiCorp Vault
- [ ] CI/CD安全集成：在Pipeline中嵌入安全检查

### 关键里程碑
- ✅ 获得CEH或eJPT/OSCP（OSCP是渗透测试金牌认证）
- ✅ 在HackTheBox/HTB完成20+中等难度机器
- ✅ 独立完成一次完整的渗透测试报告

---

## 🌳 第3级 · 中级 (3-6年)

### 渗透测试进阶

**高级攻击技术**
- [ ] Active Directory攻击：Kerberoasting、Pass-the-Hash、DCSync
- [ ] 横向移动：PsExec、WMI、SMB relay
- [ ] C2框架使用：Cobalt Strike / Sliver / Havoc（授权环境）
- [ ] 自定义Exploit开发：基础缓冲区溢出
- [ ] 免杀技术：EDR绕过基础

**红队演练**
- [ ] 完整红队项目：从社会工程学→初始访问→持久化→数据泄露模拟
- [ ] 物理安全测试：Badge克隆、社会工程学
- [ ] 紫队协作：红队+蓝队联合演练

### 安全架构方向

**安全架构设计**
- [ ] Zero Trust架构：微分段、最小权限、持续验证
- [ ] 云安全架构（AWS/Azure/GCP）：共享责任模型、云原生安全
- [ ] 身份和访问管理（IAM）：SSO、MFA、PAM
- [ ] 数据安全：DLP、加密策略、数据分类
- [ ] 威胁建模：STRIDE方法论、攻击树

**安全合规（GRC方向）**
- [ ] 主流合规框架：ISO 27001、SOC 2、NIST、等级保护2.0
- [ ] 风险评估方法论：定性/定量风险分析
- [ ] 安全策略制定：安全基线、安全策略文档

### 关键里程碑
- ✅ 获得OSCP认证（渗透测试领域最硬核认证）
- ✅ 独立主导一次完整的红蓝对抗演练
- ✅ 发现并负责任披露（CVE）一个公开漏洞
- ✅ 在安全会议（DEF CON/Black Hat/FreeBuf）发表议题

---

## 🦅 第4级 · 高级 (6-12年)

### 安全总监 / 首席安全架构师

**企业安全能力**
- [ ] 企业安全项目：安全体系评估、路线图制定
- [ ] 安全预算管理：ROI驱动的安全投入决策
- [ ] 供应链安全：第三方风险管理
- [ ] 事件响应能力建设：Playbook制定、团队训练
- [ ] 安全文化建设：全员安全意识培训

**行业影响力**
- [ ] 在DEFCON/BlackHat发表原创研究
- [ ] 开源安全工具（GitHub 1000+ Stars）
- [ ] 参与行业安全标准制定
- [ ] 漏洞研究影响主流软件（获厂商致谢）

### 关键里程碑
- ✅ 管理20+人的安全团队
- ✅ 成功防御一次高级持续性威胁（APT）攻击
- ✅ 获得CISSP、CISM等高级认证

---

## 👑 第5级 · CISO精英

### 核心职责
- 制定公司整体信息安全战略
- 向董事会汇报安全风险和态势
- 平衡安全与业务发展的关系
- 管理监管关系（数据泄露报告、合规审查）
- 危机情况下的指挥和决策

### 精英标志
- 🏆 在重大安全事件中保护公司关键资产
- 🏆 将安全能力转化为公司竞争优势
- 🏆 在DEF CON/RSA Conference发表主旨演讲
- 🏆 培养出多名安全总监/首席安全架构师

---

## 认证路线图

```
入门: CompTIA Security+ / CEH / eJPT
中级: OSCP（渗透必备）/ CySA+ / AWS Security Specialty
高级: OSCE3 / GXPN / CISSP / CISM / CISA
架构: SABSA / TOGAF（安全架构）
管理: CISO认证 / ISACA相关认证
```

---

## 🤖 AI时代的网络安全规划

### AI对安全领域的双刃剑效应

```
AI增强攻击（威胁升级）：
  ⚠️ AI生成的钓鱼邮件：语言完美，个性化，规避传统过滤
  ⚠️ AI辅助漏洞发现：自动化代码审计，CVE发现速度提升10x
  ⚠️ AI生成恶意代码：降低攻击者技术门槛
  ⚠️ Deepfake社会工程：声音/视频伪造用于欺骗验证

AI增强防御（机会升级）：
  ✅ AI威胁检测：行为分析，异常识别速度和准确率大幅提升
  ✅ AI辅助代码审计：自动扫描代码漏洞
  ✅ AI事件响应：自动化告警分类、初步响应
  ✅ AI渗透测试辅助：自动化侦察和漏洞关联
```

### 各阶段AI融合建议

**初级安全人员 — AI是学习加速器**
```
立即使用：
  - 用 Claude 解释漏洞原理（CVE详解、PoC分析）
  - 用 AI 生成 CTF 解题思路（但自己要理解每一步）
  - 用 ChatGPT 写 Python 安全脚本的基础框架

学习AI安全知识：
  - Prompt Injection：LLM应用的新型漏洞
  - AI Model 逃逸：Jailbreak技术原理
  - LLM数据投毒：训练数据的安全性
```

**中级安全工程师 — AI是效率倍增器**
```
渗透测试方向：
  - AI辅助侦察：用LLM分析OSINT数据并关联攻击面
  - AI生成Payload变体：绕过WAF的自动化变形
  - AI报告生成：渗透测试报告草稿（节省70%写报告时间）
  工具：PentestGPT / ReconAI / AI-Assisted Burp Extensions

SOC分析方向：
  - AI告警分类：减少告警疲劳（Alert Fatigue）
  - AI辅助溯源：自动关联IOC，生成攻击链时间线
  - AI生成IR报告：快速输出事件响应摘要
  工具：Microsoft Security Copilot / Elastic AI Assistant
```

**高级安全架构师 — AI原生安全设计**
```
新的安全挑战（必须掌握）：
  - LLM应用安全架构：Prompt Injection防护 · 输出过滤 · 权限边界
  - AI供应链安全：模型文件（.pkl/.safetensors）的安全验证
  - AI监控体系：检测AI系统的异常行为
  - Deepfake防御：多因素认证、活体检测集成

安全评估新维度：
  - 对公司的AI应用进行红队测试（AI Red Teaming）
  - 为LLM系统设计威胁模型（AI Threat Modeling）
```

### AI安全新职业方向（2025-2030最热）

```
🔥 AI红队工程师（AI Red Teamer）
   - 专门测试和攻击AI系统的弱点
   - Anthropic/OpenAI/Google等大厂有专职团队

🔥 LLM应用安全工程师
   - 设计防止Prompt Injection的架构
   - AI应用的安全代码审查

🔥 AI威胁情报分析师
   - 追踪AI辅助攻击组织的战术
   - 监控AI工具在暗网的滥用

🔥 Deepfake检测专家
   - 开发媒体真实性验证技术
   - 为金融/法律/政府提供鉴别服务
```

### 保持不被AI取代的核心能力

```
✅ 创意型攻击思维（AI无法真正"创新"攻击思路）
✅ 社会工程学判断（理解人性的欺骗逻辑）
✅ 复杂APT溯源（需要上下文理解和情报关联）
✅ 安全架构的业务权衡（安全vs体验的决策）
✅ AI系统的安全设计（你本身是AI安全的保护者）
```

### 行动建议

1. **立即**: 研究 OWASP Top 10 for LLM Applications（LLM应用安全标准）
2. **1个月**: 尝试对一个公开的AI聊天应用进行Prompt Injection测试
3. **3个月**: 学习如何将AI工具集成进渗透测试工作流
4. **6个月**: 考取 AI Security 相关新兴认证或发表 AI 安全研究

---

## 关联技能文件

- [`skills/cybersecurity/security-engineer/`](../skills/cybersecurity/security-engineer/) — 安全工程师
- [`skills/software/devops-engineer/`](../skills/software/devops-engineer/) — DevOps工程师（含安全）
