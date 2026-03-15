# 国内云平台技能化实现清单
# Chinese Cloud Platform Skill Implementation List

> **Version 1.0.0** | **Last Updated: 2026-03-15**
> 面向普通用户（零编程基础）的 火山引擎 / 阿里云 / 腾讯云 技能化分析

---

## 核心设计原则 / Design Principles for Non-Technical Users

普通外行使用云平台的三大痛点：

| 痛点 | 表现 | 技能化解法 |
|------|------|-----------|
| **不知道选什么** | 控制台几百个产品不知从何下手 | 按「我要做什么」而非「产品叫什么」组织技能 |
| **不知道怎么配** | 英文参数、端口、安全组看不懂 | 每个技能内置「复制即用」配置模板 + 截图式操作步骤 |
| **不知道花多少** | 不小心开了按量付费被扣光 | 每个技能必须包含「费用控制清单」和计费模式说明 |

**每个工具技能必须回答的三个问题：**
1. 我用这个能做什么？（一句话场景描述）
2. 怎么做？（5步以内的操作路径）
3. 花多少钱？（典型配置的月费参考）

---

## 三大平台定位对比 / Platform Positioning

| 维度 | 🔥 火山引擎 | ☁️ 阿里云 | 🐧 腾讯云 |
|------|-----------|---------|---------|
| **背后公司** | 字节跳动 | 阿里巴巴 | 腾讯 |
| **核心优势** | AI大模型(豆包)、抖音同款技术、音视频 | 产品最全、市场份额最大(40%)、电商生态 | 微信生态、小程序、游戏、直播 |
| **外行首选场景** | 搭建 AI 智能体、音视频处理 | 建网站、存文件、注册域名 | 做微信小程序、直播、社交类产品 |
| **新手友好度** | ⭐⭐⭐⭐⭐ (Coze 零代码) | ⭐⭐⭐ (功能多但复杂) | ⭐⭐⭐⭐ (小程序可视化) |
| **月均起步价** | ~50元 (轻量云) | ~68元/年 (活动价) | ~45元 (特惠活动) |
| **ICP 备案支持** | ✅ | ✅ | ✅ |
| **最适合谁** | 创作者、AI 爱好者、内容平台 | 电商、企业官网、传统行业 | 微信生态创业者、游戏开发者 |

---

## 一、🔥 火山引擎技能化清单 / Volcengine Skills

### 1.1 平台特色产品矩阵

```
火山引擎产品全景（外行视角）
│
├── 🤖 AI 大模型平台
│   ├── 豆包大模型 API (Doubao)          ← 国内最强性价比模型之一
│   ├── 火山方舟 Ark (MaaS平台)           ← 各家大模型一站式调用
│   └── 扣子 Coze (零代码AI智能体)        ← ⭐ 外行首选，拖拽搭建 AI 助手
│
├── 📹 音视频服务
│   ├── veImageX (智能图片处理)           ← 图片压缩/格式转换/水印一键搞定
│   ├── veVOD (视频点播)                  ← 类似优酷后台，托管视频资源
│   └── RTC 实时音视频                    ← 视频会议/直播互动技术底座
│
├── ☁️ 基础计算存储
│   ├── ECS 云服务器                      ← 购买"云电脑"跑程序
│   ├── TOS 对象存储                      ← 存图片/文件/视频
│   └── CDN 内容分发                      ← 让网站在全国各地打开都快
│
└── 📊 数据与分析
    ├── DataLeap 数据研发平台
    ├── ByteHouse 云数仓
    └── EMR 大数据服务
```

### 1.2 技能实现清单

| # | 技能名称 | Skill ID | 优先级 | 面向用户 | 核心场景 | 月费参考 |
|---|---------|---------|--------|---------|---------|---------|
| 1 | **扣子(Coze)零代码AI智能体** | `volcengine-coze-expert` | 🔴 P0 | 完全零基础 | 搭建客服机器人/知识库问答/个人助手，不需要写一行代码 | 免费起步 |
| 2 | **豆包大模型API调用** | `volcengine-doubao-api` | 🔴 P0 | 会复制粘贴代码 | 调用豆包 API、选择模型版本、控制 Token 成本 | 按量付费，约0.0008元/千token |
| 3 | **火山方舟模型平台** | `volcengine-ark-maas` | 🟡 P1 | 开发者/产品经理 | 在一个平台测试和切换不同大模型（豆包/Llama/Mistral等），对比效果和费用 | 按量 |
| 4 | **veImageX 图片智能处理** | `volcengine-imagex-expert` | 🟡 P1 | 内容运营/电商 | 网站图片自动压缩+格式转换+CDN加速，告别手动PS压图 | 约10-50元/月 |
| 5 | **ECS 云服务器入门** | `volcengine-ecs-starter` | 🟡 P1 | 小白建站/开发者 | 购买云服务器、安装宝塔面板、一键部署网站 | 约50-100元/月 |
| 6 | **TOS 对象存储** | `volcengine-tos-expert` | 🟡 P1 | 开发者/内容创作者 | 存储和分发图片、视频、附件，替代七牛云/又拍云 | 约0.12元/GB/月 |
| 7 | **veVOD 视频点播** | `volcengine-vod-expert` | 🟢 P2 | 视频平台/教育机构 | 上传视频、自动转码、防盗链、播放器 SDK 接入 | 按流量/转码时长计费 |
| 8 | **RTC 实时音视频** | `volcengine-rtc-expert` | 🟢 P2 | 产品经理/开发者 | 在 App 里快速加入视频通话/直播互动功能 | 按并发路数计费 |
| 9 | **CDN 内容分发网络** | `volcengine-cdn-expert` | 🟢 P2 | 建站者/内容平台 | 配置 CDN 加速域名，全国访问秒开 | 约0.2元/GB流量 |

### 1.3 外行必看场景：用扣子(Coze)5步建AI助手

```
步骤1: 访问 coze.cn → 注册账号（微信/手机号即可）
步骤2: 点击「创建智能体」→ 输入名字和用途描述
步骤3: 上传你的文档/FAQ → 自动成为知识库
步骤4: 设置触发词和回复风格
步骤5: 一键发布到微信/飞书/网页

耗时: 15-30分钟 | 费用: 免费额度内 | 编程需求: 零
```

---

## 二、☁️ 阿里云技能化清单 / Alibaba Cloud Skills

### 2.1 平台特色产品矩阵

```
阿里云产品全景（外行视角）
│
├── 🌐 建站全家桶（最常用）
│   ├── 域名注册 (万网)                  ← 买 .com/.cn 域名
│   ├── ECS 轻量应用服务器                ← ⭐ 外行建站首选，含1-2键安装
│   ├── OSS 对象存储                      ← 存图片/视频/附件
│   ├── CDN 内容分发                      ← 全国访问加速
│   └── SSL 证书 (免费版)                 ← 网站变成 https，绿锁
│
├── 🤖 AI 与大模型
│   ├── 通义千问 (Qwen)                   ← 阿里自研大模型
│   ├── 百炼 Model Studio                 ← ⭐ 外行AI开发首选，拖拽RAG
│   ├── PAI 机器学习平台                  ← 专业 ML 训练平台
│   └── 万小智 AI 员工                    ← 智能客服/营销助手
│
├── 💾 数据库服务
│   ├── RDS MySQL/PostgreSQL              ← 托管数据库，不用自己装
│   ├── Redis (Tair)                      ← 缓存加速
│   └── PolarDB                           ← 高性能云原生数据库
│
├── ⚡ 无服务器/函数计算
│   ├── 函数计算 FC                       ← 不用管服务器，写完代码直接跑
│   └── Serverless 应用引擎 SAE           ← 微服务托管
│
└── 📊 企业工具
    ├── 云效 Yunxiao                       ← 团队协作+CI/CD
    ├── 钉钉开放平台                       ← 钉钉机器人/应用开发
    └── 阿里邮箱 企业邮                    ← 公司邮箱配置
```

### 2.2 技能实现清单

| # | 技能名称 | Skill ID | 优先级 | 面向用户 | 核心场景 | 月费参考 |
|---|---------|---------|--------|---------|---------|---------|
| 1 | **ECS轻量服务器建站** | `aliyun-ecs-website-starter` | 🔴 P0 | 完全零基础 | 从零到一：买服务器→装宝塔面板→建WordPress/商城网站→绑域名，全程图文 | 6-24元/月(活动价) |
| 2 | **OSS对象存储全攻略** | `aliyun-oss-expert` | 🔴 P0 | 开发者/运营人员 | 存储桶创建、文件上传、防盗链、跨域配置、绑定自定义域名+CDN | 0.12元/GB/月 |
| 3 | **域名注册+ICP备案** | `aliyun-domain-beian-expert` | 🔴 P0 | 所有建站用户 | 万网购域名→实名认证→ICP备案全流程→DNS解析配置，必踩坑全避开 | 域名50-200元/年 |
| 4 | **CDN加速配置** | `aliyun-cdn-expert` | 🟡 P1 | 建站者/内容平台 | 静态资源加速、HTTPS配置、缓存规则、防盗链、流量异常告警 | 0.24元/GB |
| 5 | **SSL证书申请+HTTPS配置** | `aliyun-ssl-https-expert` | 🔴 P0 | 所有建站用户 | 申请免费DV证书→下载→配置Nginx/Apache/宝塔，让网站变绿锁 | 免费(DV) |
| 6 | **RDS云数据库入门** | `aliyun-rds-starter` | 🟡 P1 | 开发者/建站者 | 购买RDS MySQL→连接配置→定时备份→从ECS访问的网络配置 | 60-200元/月 |
| 7 | **函数计算FC入门** | `aliyun-fc-serverless` | 🟡 P1 | 开发者/自动化用户 | 无需管服务器，写Python/Node.js代码定时执行任务、处理图片、发送通知 | 按调用次数，极便宜 |
| 8 | **百炼AI应用开发** | `aliyun-bailian-ai-expert` | 🔴 P0 | AI 爱好者/产品人 | 用通义千问搭建企业知识库问答、RAG应用、自定义AI助手，可视化配置 | 按Token计费 |
| 9 | **通义千问API调用** | `aliyun-qwen-api` | 🟡 P1 | 开发者 | Qwen系列模型调用、多模态图文理解、长文档分析、JSON输出控制 | 约0.0006元/千token |
| 10 | **云效DevOps入门** | `aliyun-yunxiao-cicd` | 🟢 P2 | 开发团队/个人项目 | 代码托管、流水线自动构建部署、需求/缺陷管理，GitHub平替 | 5人以内免费 |
| 11 | **企业邮箱配置** | `aliyun-mail-expert` | 🟡 P1 | 中小企业/个体户 | 企业邮箱申请→域名DNS配置→Outlook/手机收发邮件设置，告别163邮箱 | 10-30元/账号/年 |
| 12 | **OSS+CDN静态网站托管** | `aliyun-static-website` | 🟢 P2 | 前端开发者/博主 | 用OSS托管HTML/React/Vue静态网站，比ECS便宜10倍，绑域名+HTTPS | 几乎免费 |

### 2.3 外行必看场景：10分钟建一个网站

```
步骤1: 注册阿里云账号 → 实名认证
步骤2: 购买「轻量应用服务器」(活动价68元/年)
        → 选「WordPress 镜像」→ 一键部署
步骤3: 购买域名（.cn 约25元/年）→ 解析到服务器IP
步骤4: 宝塔面板申请免费SSL证书 → 开启HTTPS
步骤5: 登录 WordPress 后台，上传Logo，填写内容

总费用: 约100元/年 | 编程需求: 零 | 时间: 30-60分钟
```

---

## 三、🐧 腾讯云技能化清单 / Tencent Cloud Skills

### 3.1 平台特色产品矩阵

```
腾讯云产品全景（外行视角）
│
├── 📱 微信生态开发（独家优势）
│   ├── 云开发 CloudBase (TCB)            ← ⭐ 外行做小程序首选，无需服务器
│   ├── 微信小程序后端托管                 ← 小程序数据库+存储+云函数打包
│   └── 微信支付 API 接入指南              ← 收款必学
│
├── ☁️ 基础计算存储
│   ├── CVM 云服务器                       ← 标准虚拟机
│   ├── 轻量应用服务器                     ← ⭐ 外行建站首选
│   ├── COS 对象存储                       ← 存文件/图片/视频
│   └── CDN 内容分发                       ← 全国加速
│
├── 🎥 音视频（腾讯核心竞争力）
│   ├── TRTC 实时音视频                    ← 视频会议/连麦/直播互动底层
│   ├── CSS 直播（云直播）                 ← 直播推流/拉流/录制
│   ├── VOD 点播                           ← 视频托管+播放器
│   └── IM 即时通信                        ← 聊天/消息推送
│
├── 🤖 AI 服务
│   ├── 混元大模型 (Hunyuan)               ← 腾讯自研大模型
│   ├── 腾讯云 AI 代码助手                 ← 写代码用
│   └── 人脸识别/OCR/NLP 等 AI 能力        ← 拿来即用的AI接口
│
└── ⚡ 无服务器
    ├── 云函数 SCF                         ← 无需服务器运行代码
    └── API 网关                           ← 接口托管和保护
```

### 3.2 技能实现清单

| # | 技能名称 | Skill ID | 优先级 | 面向用户 | 核心场景 | 月费参考 |
|---|---------|---------|--------|---------|---------|---------|
| 1 | **微信小程序云开发(CloudBase)** | `tencentcloud-cloudbase-miniprogram` | 🔴 P0 | 创业者/零基础 | 不购买服务器，直接在小程序开发工具里建数据库、写云函数、上线小程序，全程可视化 | 19.9元/月起 |
| 2 | **COS对象存储完全手册** | `tencentcloud-cos-expert` | 🔴 P0 | 开发者/运营人员 | 存储桶创建、公/私有权限、临时链接、CDN绑定、数据处理（图片万象）、防盗链 | 0.099元/GB/月 |
| 3 | **轻量服务器+宝塔建站** | `tencentcloud-lighthouse-website` | 🔴 P0 | 零基础建站 | 购买轻量服务器→安装宝塔→部署WordPress/商城→绑域名+SSL，图文步骤 | 24-50元/月 |
| 4 | **TRTC实时音视频快速接入** | `tencentcloud-trtc-expert` | 🟡 P1 | App开发者/产品经理 | 在App中加入视频通话/连麦直播，提供iOS/Android/Web快速接入模板，理解房间/用户概念 | 约0.022元/分钟/路 |
| 5 | **云直播CSS搭建直播间** | `tencentcloud-live-streaming` | 🟡 P1 | 直播创业者 | 推流地址生成→OBS/手机推流配置→播放拉流地址→录制存储→截图鉴黄 | 约0.21元/GB下行 |
| 6 | **云函数SCF自动化任务** | `tencentcloud-scf-expert` | 🟡 P1 | 运营人员/轻开发者 | 定时抓取数据、微信消息通知、图片自动处理，不用管服务器，写完上传即用 | 100万次/月免费 |
| 7 | **腾讯云VOD点播系统** | `tencentcloud-vod-expert` | 🟡 P1 | 教育/内容平台 | 视频上传→自动转码(适配手机/PC)→防盗链→播放器接入→字幕生成 | 按存储+流量 |
| 8 | **域名+DNS+SSL配置** | `tencentcloud-domain-ssl` | 🟡 P1 | 所有建站用户 | 腾讯云购域名→实名→ICP备案→DNSPod解析配置→免费SSL证书申请 | 域名50-200元/年 |
| 9 | **IM即时通信接入** | `tencentcloud-im-expert` | 🟢 P2 | App开发者 | 在App中添加聊天功能：单聊/群聊/消息推送，SDK接入和消息类型设计 | 体验版免费 |
| 10 | **混元大模型API** | `tencentcloud-hunyuan-api` | 🟡 P1 | 开发者/产品人 | 混元API调用、多轮对话、函数调用、混元生图，费用对比豆包/通义 | 按Token |
| 11 | **腾讯云图片万象(CI)** | `tencentcloud-ci-imageprocess` | 🟢 P2 | 电商/内容平台 | COS上的图片自动压缩、格式转换、水印、人脸美颜、内容审核，一行配置搞定 | 按处理量 |
| 12 | **微信支付接入全流程** | `tencentcloud-wxpay-integration` | 🟢 P2 | 创业者/开发者 | 从申请微信支付资质→接入JSAPI/小程序支付→服务器端验签→退款处理 | 免费（交易按比例收手续费）|

### 3.3 外行必看场景：0基础做个微信小程序商城

```
步骤1: 注册微信公众平台账号 → 申请小程序主体
步骤2: 开通腾讯云「云开发 CloudBase」环境 (19.9元/月)
步骤3: 在微信开发者工具中选「云开发模板」→ 选商城模板
步骤4: 修改商品名称/图片/价格（类似编辑Word文档）
步骤5: 申请微信支付资质 → 在CloudBase配置收款

总费用: 约20元/月 + 微信支付手续费 | 编程需求: 极低 | 时间: 1-3天
```

---

## 四、通用基础设施技能 / Cross-Platform Skills

这些场景在三家云上流程相同，做成通用技能：

| # | 技能名称 | Skill ID | 覆盖平台 | 核心内容 |
|---|---------|---------|---------|---------|
| 1 | **ICP备案全流程** | `cn-cloud-icp-beian-guide` | 🔴 三家通用 | 前置条件检查、材料准备清单、各平台提交流程、审核周期、常见拒绝原因 |
| 2 | **SSL证书申请与配置** | `cn-cloud-ssl-setup` | 🔴 三家通用 | 免费DV证书vs付费证书、申请步骤、Nginx/Apache/宝塔面板三种配置方式 |
| 3 | **国内云选型指南** | `cn-cloud-selection-advisor` | 🔴 决策辅助 | 按场景推荐平台、费用对比计算器、各平台新人优惠攻略 |
| 4 | **宝塔面板管理** | `baota-panel-expert` | 🟡 三家通用 | Linux服务器零基础入口：安装、建站、数据库管理、定时备份、SSL配置 |
| 5 | **国内云费用优化** | `cn-cloud-cost-saving` | 🟡 三家通用 | 包年包月vs按量计费选择策略、各平台优惠活动规律、闲置资源检查清单 |
| 6 | **CDN加速与防盗链** | `cn-cdn-config-expert` | 🟢 三家通用 | CNAME配置、缓存规则、Referer防盗链、HTTPS回源、带宽封顶 |

---

## 五、优先级汇总 / Implementation Priority Summary

### 🔴 P0 — 立即实现（15个技能）

> 覆盖「普通用户最高频的刚需场景」

| 技能 | 平台 | 外行场景 |
|------|------|---------|
| `volcengine-coze-expert` | 火山引擎 | 零代码搭AI助手 |
| `volcengine-doubao-api` | 火山引擎 | 调大模型API |
| `aliyun-ecs-website-starter` | 阿里云 | 最简单的建站 |
| `aliyun-oss-expert` | 阿里云 | 存图片/文件 |
| `aliyun-domain-beian-expert` | 阿里云 | 买域名+备案 |
| `aliyun-ssl-https-expert` | 阿里云 | 网站上HTTPS |
| `aliyun-bailian-ai-expert` | 阿里云 | 搭AI知识库 |
| `tencentcloud-cloudbase-miniprogram` | 腾讯云 | 做微信小程序 |
| `tencentcloud-cos-expert` | 腾讯云 | 存图片/文件 |
| `tencentcloud-lighthouse-website` | 腾讯云 | 零基础建站 |
| `cn-cloud-icp-beian-guide` | 通用 | 网站备案 |
| `cn-cloud-ssl-setup` | 通用 | HTTPS配置 |
| `cn-cloud-selection-advisor` | 通用 | 选哪家云 |
| `baota-panel-expert` | 通用 | 图形化管服务器 |
| `aliyun-enterprise-email-expert` | 阿里云 | 公司邮箱配置 |

### 🟡 P1 — 优先实现（14个技能）

`volcengine-ark-maas`, `volcengine-imagex-expert`, `volcengine-ecs-starter`,
`volcengine-tos-expert`, `aliyun-cdn-expert`, `aliyun-rds-starter`, `aliyun-fc-serverless`,
`aliyun-qwen-api`, `tencentcloud-trtc-expert`, `tencentcloud-live-streaming`,
`tencentcloud-scf-expert`, `tencentcloud-vod-expert`, `tencentcloud-domain-ssl`,
`tencentcloud-hunyuan-api`

### 🟢 P2 — 规划实现（9个技能）

`volcengine-vod-expert`, `volcengine-rtc-expert`, `volcengine-cdn-expert`,
`aliyun-yunxiao-cicd`, `aliyun-static-website`, `tencentcloud-im-expert`,
`tencentcloud-ci-imageprocess`, `tencentcloud-wxpay-integration`,
`cn-cdn-config-expert`, `cn-cloud-cost-saving`

---

## 六、技能内容设计规范（针对外行用户）/ Content Design for Non-Technical Users

### 必须包含的内容模块

```
外行友好型工具技能 = 以下7个模块缺一不可

① 一句话定位
   "这个东西就是用来___的，相当于___(生活类比)"
   例：OSS = "云硬盘，把文件放上去，给你一个链接，任何人都能访问"

② 什么时候用它 / 什么时候不用
   清晰的适用场景 vs 不适用场景

③ 开通步骤（截图级别精度）
   不超过8步，每步说清楚点哪里、填什么

④ 费用说明（必须！）
   - 典型配置的月费
   - 免费额度是多少
   - 会不会不小心扣很多钱（超量保护设置）
   - 推荐的开销控制方法

⑤ 最常用操作的命令/配置（复制即用）
   - 优先提供控制台操作步骤（不是CLI命令）
   - CLI 命令放在"进阶"区块

⑥ 常见问题 & 报错解释
   把错误代码翻译成人话
   例：403 Forbidden = "你设置了私有桶，需要生成临时访问链接"

⑦ 与其他产品的联动
   例："OSS建议配合CDN一起用，否则大文件下载很慢"
```

### 语言风格要求

| 不要 | 要 |
|------|-----|
| "请配置 CNAME 记录" | "在域名管理里找到'解析'，新建一条记录，类型选CNAME" |
| "开启 ACL 公共读权限" | "把桶设置成公开，让别人能直接访问里面的文件" |
| "设置 Lifecycle Policy" | "设置自动删除规则，比如超过30天的临时文件自动清理" |
| "配置 SLB 实现高可用" | "如果你网站每天有10万以上访问，再考虑负载均衡" |
| 直接给代码 | 先给控制台截图操作，代码放在"开发者进阶"折叠区 |

---

## 七、场景驱动技能索引 / Scenario-Driven Skill Index

> 外行来了不问「我要用什么产品」，而是问「我想做___怎么实现」

| 我想做... | 首选平台 | 推荐技能 |
|----------|---------|---------|
| 个人博客/作品集网站 | 阿里云 | `aliyun-ecs-website-starter` + `aliyun-ssl-https-expert` |
| 微信小程序（不懂代码）| 腾讯云 | `tencentcloud-cloudbase-miniprogram` |
| 网上卖东西（独立站）| 阿里云 | `aliyun-ecs-website-starter` + `aliyun-oss-expert` |
| 做一个AI客服机器人 | 火山引擎 | `volcengine-coze-expert` |
| 存公司的文件/图片 | 任意 | `aliyun-oss-expert` 或 `tencentcloud-cos-expert` |
| 搭直播平台 | 腾讯云 | `tencentcloud-live-streaming` + `tencentcloud-trtc-expert` |
| 做教育/培训视频平台 | 腾讯云 | `tencentcloud-vod-expert` + `tencentcloud-cos-expert` |
| 调用AI大模型（最便宜）| 火山引擎 | `volcengine-doubao-api` |
| 注册域名+备案 | 阿里云 | `aliyun-domain-beian-expert` |
| 给网站配公司邮箱 | 阿里云 | `aliyun-enterprise-email-expert` |
| 做抽奖/问卷/表单小程序 | 腾讯云 | `tencentcloud-cloudbase-miniprogram` |
| 公司内部知识库AI问答 | 阿里云/火山 | `aliyun-bailian-ai-expert` 或 `volcengine-coze-expert` |
| 图片压缩+全国加速 | 火山引擎 | `volcengine-imagex-expert` |
| 网站访问慢（加速）| 阿里云 | `aliyun-cdn-expert` |
| 定时自动执行任务 | 腾讯云 | `tencentcloud-scf-expert` 或 `aliyun-fc-serverless` |

---

## 八、建议实现顺序 / Recommended Implementation Order

```
第一批（本周）: 覆盖最高频的"建站+存储+备案"闭环
  1. cn-cloud-selection-advisor      ← 外行第一个问题：选哪家？
  2. cn-cloud-icp-beian-guide        ← 中国建站绕不开的备案
  3. baota-panel-expert              ← 宝塔是99%外行管服务器的入口
  4. aliyun-ecs-website-starter      ← 阿里云建站（市场最大）
  5. aliyun-ssl-https-expert         ← 绿锁配置（所有建站用户必须）

第二批（下周）: 覆盖"对象存储+AI入门"
  6. aliyun-oss-expert
  7. tencentcloud-cos-expert
  8. volcengine-coze-expert          ← AI热点，外行能用上的AI
  9. aliyun-bailian-ai-expert
  10. tencentcloud-cloudbase-miniprogram

第三批（后续）: 覆盖"音视频+通信+大模型API"
  11-15: 各平台P1技能按需推进
```

---

*生成时间: 2026-03-15*
*数据来源: 火山引擎/阿里云/腾讯云官方文档、产品页面、用户社区分析*
*本清单专注"普通外行也能应用自如"的实用场景，刻意排除了企业级高复杂度产品*
