# 数据领域职业路径 Data Careers Roadmap

> 覆盖方向：数据分析师 · 数据工程师 · 数据科学家 · BI工程师 · 数据架构师

---

## 职业全景

```
数据领域
├── 分析方向
│   ├── 数据分析师 → 高级分析师 → 数据分析经理 → 数据总监
│   └── BI工程师 → BI架构师
├── 工程方向
│   ├── 数据工程师 → 高级数据工程师 → 数据平台架构师
│   └── 数据架构师 → 首席数据架构师
├── 科学方向
│   ├── 数据科学家 → 高级数据科学家 → 首席数据科学家
│   └── 分析工程师（Analytics Engineer）
└── 管理方向
    ├── 数据产品经理
    └── CDO (首席数据官)
```

---

## 三大方向对比

| 维度 | 数据分析师 | 数据工程师 | 数据科学家 |
|------|-----------|-----------|-----------|
| 核心工具 | SQL · Excel · Tableau | Python · Spark · Airflow | Python · PyTorch · R |
| 核心产出 | 洞察报告、Dashboard | 数据Pipeline、数仓 | 预测模型、算法 |
| 编程要求 | 基础到中级 | 高级 | 中级到高级 |
| 数学要求 | 统计基础 | 较少 | 扎实数学 |
| 业务接触 | 高 | 低 | 中 |

---

## 🌱 第1级 · 入门 (0-12个月)

### 数据分析师入门
- [ ] SQL：SELECT、JOIN、GROUP BY、子查询、窗口函数
- [ ] Excel/Google Sheets：透视表、VLOOKUP、基础图表
- [ ] 基础统计：均值、中位数、方差、相关性
- [ ] 一个BI工具：Tableau Public 或 Power BI（免费版）
- [ ] 学会讲数据故事：从数据到洞察到建议

### 数据工程师入门
- [ ] Python基础（Pandas、文件处理）
- [ ] SQL进阶（窗口函数、CTE、性能优化）
- [ ] 关系型数据库原理（PostgreSQL / MySQL）
- [ ] 基础ETL概念：Extract → Transform → Load
- [ ] Git版本控制

### 数据科学家入门
- [ ] Python数据栈：NumPy、Pandas、Matplotlib、Seaborn
- [ ] 统计学基础：假设检验、置信区间、A/B测试
- [ ] ML入门：线性回归、逻辑回归、决策树
- [ ] Jupyter Notebook工作流
- [ ] Kaggle入门竞赛参与

### 关键里程碑
- ✅ 用真实数据集完成一个分析项目（发布到GitHub/Kaggle）
- ✅ 能独立写出解决业务问题的SQL查询
- ✅ 向非技术人员讲清楚一个数据洞察

---

## 🌿 第2级 · 初级 (1-3年)

### 数据分析师进阶
- [ ] 高级SQL：性能调优、复杂窗口函数、存储过程
- [ ] Python分析：Pandas高级用法、数据清洗技巧
- [ ] 统计深入：回归分析、时间序列分析、方差分析
- [ ] A/B测试设计与统计显著性分析
- [ ] 数据可视化设计原则（选对图表）
- [ ] 业务理解：关键指标定义（DAU/MAU/LTV/Churn）

### 数据工程师进阶
- [ ] Airflow/Prefect：工作流调度与DAG设计
- [ ] 数据仓库：Snowflake/BigQuery/Redshift
- [ ] dbt：数据转换与数据质量测试
- [ ] Spark基础：PySpark、DataFrame API
- [ ] 流式处理入门：Kafka基础概念
- [ ] 数据质量框架：Great Expectations
- [ ] 列存储格式：Parquet、Delta Lake

### 数据科学家进阶
- [ ] 特征工程：创建有意义的特征
- [ ] 模型评估：防过拟合、交叉验证、多指标评估
- [ ] 集成方法：XGBoost、LightGBM
- [ ] 生产环境部署：Flask/FastAPI封装模型
- [ ] 实验框架：统计功效分析、样本量计算

### 关键里程碑
- ✅ 建立并维护团队使用的Dashboard
- ✅ 主导一次A/B测试并驱动产品决策
- ✅ 独立完成数据Pipeline并稳定运行3个月+

---

## 🌳 第3级 · 中级 (3-6年)

### 分析工程师（Analytics Engineer，新兴热门方向）
```
特征：介于数据分析师和数据工程师之间
技能：dbt高级 + SQL精通 + 数据建模 + 数据测试 + 业务理解
工具：dbt · Looker · Snowflake · Git
产出：可复用的数据模型层，供分析师和产品使用
```

**所有方向共同要求**
- [ ] 数据建模：星型模型/雪花模型/Kimball方法论
- [ ] 数据治理：元数据管理、数据血缘
- [ ] 数据质量：SLA定义、异常检测、数据契约
- [ ] 成本优化：数仓查询优化、存储压缩
- [ ] 与业务团队深度协作，影响业务决策

**数据工程中级**
- [ ] 实时数据平台：Kafka + Flink
- [ ] 湖仓一体架构（Lakehouse：Delta Lake / Apache Iceberg）
- [ ] 数据网格（Data Mesh）概念与实践
- [ ] 基础设施即代码：Terraform管理数据基础设施

**数据科学中级**
- [ ] 因果推断：双重差分、倾向得分匹配
- [ ] 贝叶斯统计实践
- [ ] NLP/推荐系统/预测模型垂直方向深入
- [ ] 业务影响量化：ROI测算方法

### 关键里程碑
- ✅ 设计公司级数仓架构或核心数据模型
- ✅ 数据洞察直接驱动一个业务决策（有可量化结果）
- ✅ 建立数据团队的数据质量标准

---

## 🦅 第4级 · 高级 (6-10年)

### 数据平台架构师
- [ ] 端到端数据平台设计（采集→存储→计算→服务→治理）
- [ ] 多云数据架构（AWS/GCP/Azure跨云）
- [ ] 数据安全与隐私合规（GDPR/CCPA）
- [ ] 数据平台成本治理（FinOps for Data）
- [ ] 数据产品化：内部数据API/数据市场

### 首席数据科学家
- [ ] 建立企业ML平台方法论
- [ ] 模型风险管理框架
- [ ] AI伦理与公平性实践
- [ ] 向董事会汇报数据战略

### 数据分析总监
- [ ] 团队建设（招聘、培训、文化）
- [ ] 数据驱动文化推广
- [ ] 公司级关键指标体系设计（North Star Metric）
- [ ] 数据产品路线图制定

### 关键里程碑
- ✅ 主导整个公司数据战略制定
- ✅ 带领10+人数据团队
- ✅ 数据分析直接贡献可量化的业务价值（千万级别）

---

## 👑 第5级 · 精英 — CDO首席数据官

### 核心职责
- 制定公司数据战略和治理策略
- 数据资产货币化（Data Monetization）
- 建立数据文化和数据驱动决策体系
- 监管合规与数据隐私保护
- 代表公司参与行业数据标准制定

### 精英标志
- 🏆 领导超过50人的数据组织
- 🏆 将数据能力转化为公司核心竞争力
- 🏆 在数据领域顶级会议（Strata/dbt Coalesce）发表主旨演讲
- 🏆 主导过数据相关的并购或战略合作

---

## 工具生态速查

```
数据采集: Airbyte · Fivetran · Stitch · Kafka
数据存储: Snowflake · BigQuery · Redshift · Delta Lake
数据转换: dbt · Spark · Flink
数据编排: Airflow · Prefect · Dagster
数据质量: Great Expectations · Monte Carlo · dbt tests
数据目录: DataHub · Alation · Collibra
可视化: Tableau · Looker · Power BI · Metabase · Superset
```

---

## 🤖 AI时代的数据职业规划

### AI对数据领域的重塑

```
正在发生的变化：
  - Text-to-SQL：业务人员可直接用自然语言查询数据，绕过分析师
  - AI生成报告：初级数据报告正在被自动化
  - AutoML：模型调参工作被大量自动化
  - 数据治理+AI：数据血缘、数据质量可以AI辅助检测
  - LLM数据应用：LLM理解非结构化数据，打通文本与结构化数据
```

### 各角色AI转型路径

**数据分析师 → AI增强分析师**
```
现在必学：
  - 自然语言分析工具（Metabase AI / Tableau AI / Power BI Copilot）
  - 用 Claude/GPT 辅助撰写分析叙事（数据故事）
  - 学会设计 AI 分析Agent（让 AI 自动分析周报数据）

核心差异化：
  - 业务洞察判断力（AI给数据，你给意义）
  - 分析框架设计（知道分析什么比怎么分析更重要）
  - 向决策者的沟通和说服力
```

**数据工程师 → AI数据工程师**
```
现在必学：
  - 非结构化数据处理：PDF/图片/音频的嵌入化（Embedding Pipeline）
  - 向量数据库运维：Pgvector / Milvus / Weaviate
  - LLM数据流水线：文档解析→Chunking→Embedding→检索
  - AI数据质量：LLM辅助异常检测、数据修复

代码提效：
  - 用 Cursor/Copilot 写 dbt 模型，速度提升3-5倍
  - 让 AI 生成数据质量测试用例
```

**数据科学家 → AI科学家**
```
转型重点：
  - 从训练自定义模型 → 工程化调用Foundation Models
  - 掌握 LLM Evaluation：建立语言模型的评估Benchmark
  - 因果推断+LLM：用LLM辅助因果发现和反事实分析
  - 多模态数据科学：文本+图像+时序联合分析
```

### AI时代数据人的核心护城河

| 能力 | AI能做 | 人必须做 |
|------|--------|---------|
| 数据查询 | ✅ Text-to-SQL | 验证结果、发现异常 |
| 图表生成 | ✅ 自动可视化 | 选择正确的叙事方式 |
| 数据管道 | ⚠️ 部分自动生成 | 架构设计、性能优化 |
| 业务洞察 | ❌ 不理解业务语境 | 深度业务理解 |
| 数据战略 | ❌ 无法战略决策 | CDO级别的数据战略 |

### 新兴热门方向（抢先布局）

```
🔥 AI/LLM数据工程师：专门构建LLM数据基础设施
   - Embedding Pipeline · RAG数据层 · 向量检索优化

🔥 AI评估工程师（Evals Engineer）：
   - 设计LLM评估框架 · 构建Benchmark · 对齐测试

🔥 数据+AI产品经理：
   - 设计AI功能的数据需求 · 数据飞轮策略

🔥 Real-time AI数据工程：
   - 流式数据+实时向量更新 · Flink+向量数据库
```

### 行动建议

1. **立即**: 在工作中用 Claude 帮你分析数据、写SQL注释、生成报告草稿
2. **1个月内**: 完成一个 Text-to-SQL 或 RAG over documents 的小项目
3. **3个月内**: 学会用向量数据库处理非结构化数据（文本/PDF）
4. **6个月内**: 建立"AI增强分析"工作流，向团队演示效率提升

---

## 关联技能文件

- [`skills/data/data-analyst/`](../skills/data/data-analyst/) — 数据分析师
- [`skills/data/data-engineer/`](../skills/data/data-engineer/) — 数据工程师
- [`skills/data/data-scientist/`](../skills/data/data-scientist/) — 数据科学家
- [`skills/research/statistician/`](../skills/research/statistician/) — 统计学家
