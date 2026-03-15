# Software Tools Skill Implementation List / 软件工具技能化实现清单

> **Version 1.0.0** | **Last Updated: 2026-03-15** | **Total: 80 Tools**

软件工具技能化（Software Tool Skills）与角色技能（Role Skills）不同：前者让 AI 成为某款工具的专家用户，能够给出最佳实践、命令示例、配置模板和故障排查方案；后者让 AI 模拟职业角色的思维方式。

---

## 分析方法论 / Analysis Methodology

本清单通过以下维度对现有 471 个角色技能（SKILL.md）进行工具交叉分析：

1. **工具引用频次** — 统计各工具在所有角色 SKILL.md 中的出现次数
2. **角色覆盖广度** — 该工具跨越多少个不同角色类别
3. **技能化价值** — 该工具的配置/操作复杂度，是否适合 AI 专家化
4. **优先级评分** — 综合频次 × 广度 × 复杂度

---

## 工具引用频次统计 / Tool Reference Frequency

基于全库 471 个 SKILL.md 文件的统计（Top 40）：

| 排名 | 工具 | 引用次数 | 主要使用角色类别 |
|------|------|----------|----------------|
| 1 | GitHub | 133 | software, devops, ai-ml, research, business |
| 2 | Python | 186 | software, ai-ml, data, research, biotech, finance |
| 3 | SAP | 73 | manufacturing, logistics, finance, admin |
| 4 | React | 57 | software, product, marketing |
| 5 | AWS | 62 | software, devops, ai-ml, data |
| 6 | Kafka | 60 | software, data, ai-ml |
| 7 | Kubernetes | 54 | software, devops, ai-ml |
| 8 | Redis | 53 | software, devops, data |
| 9 | PyTorch | 45 | ai-ml, research, biotech |
| 10 | MATLAB | 44 | research, aerospace, automotive, energy |
| 11 | Azure | 43 | software, devops, enterprise |
| 12 | Vault | 42 | software, devops, cybersecurity |
| 13 | MLflow | 39 | ai-ml, software, data |
| 14 | PostgreSQL | 35 | software, data, finance |
| 15 | Excel | 29 | finance, business, admin, research |
| 16 | Airflow | 27 | data, software, ai-ml |
| 17 | Spark | 25 | data, software, ai-ml |
| 18 | Slack | 24 | business, software, admin |
| 19 | Terraform | 23 | devops, software |
| 20 | ANSYS | 22 | aerospace, automotive, construction, energy |
| 21 | Canva | 17 | marketing, content, education |
| 22 | VS Code | 16 | software, ai-ml, data |
| 23 | GitHub Actions | 19 | software, devops |
| 24 | Prometheus | 17 | devops, software |
| 25 | Grafana | 17 | devops, software, data |
| 26 | TensorFlow | 16 | ai-ml, research |
| 27 | LangChain | 15 | ai-ml, software |
| 28 | Figma | 15 | product, marketing, software |
| 29 | Unity | 14 | entertainment, education, special |
| 30 | Jira | 13 | business, software, product |
| 31 | Helm | 13 | devops, software |
| 32 | GCP | 13 | software, devops, ai-ml |
| 33 | Docker | 13 | software, devops |
| 34 | Notion | 12 | business, software, special |
| 35 | Tableau | 11 | data, finance, marketing |
| 36 | Jupyter | 11 | ai-ml, data, research |
| 37 | Unreal | 9 | entertainment, special |
| 38 | Power BI | 9 | data, finance, business |
| 39 | MongoDB | 9 | software, data |
| 40 | Salesforce | 10 | marketing, business, sales |

---

## 技能化实现清单 / Skill Implementation Checklist

### 分类说明 / Priority Legend

| 标记 | 说明 |
|------|------|
| 🔴 P0 | 立即实现 — 高频引用 + 配置复杂度高 + 跨角色广泛使用 |
| 🟡 P1 | 优先实现 — 中高频引用或特定领域核心工具 |
| 🟢 P2 | 规划实现 — 中低频但有明确需求场景 |
| ✅ 已实现 | 库中已有对应 SKILL.md |

---

### 一、云平台工具 / Cloud Platform Tools

建议分类目录：`skills/tools/cloud/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **AWS CLI + Console** | `aws-cloud-expert` | 🔴 P0 | DevOps, Software Arch, Data Engineer | EC2/S3/Lambda/RDS/VPC/IAM 命令速查、架构选型、成本优化、安全配置 |
| **GCP (gcloud + Console)** | `gcp-cloud-expert` | 🔴 P0 | AI/ML Engineer, DevOps, Data Engineer | GKE/BigQuery/Cloud Run/Vertex AI 配置、IAM策略、费用管控 |
| **Azure (az CLI)** | `azure-cloud-expert` | 🔴 P0 | DevOps, Enterprise Arch, Security | AKS/Functions/CosmosDB/AD 配置、企业混合云架构 |
| **Alibaba Cloud (阿里云)** | `aliyun-cloud-expert` | 🟡 P1 | DevOps (CN), Backend Dev | ECS/OSS/RDS/ACK/CDN，国内合规、备案、内容分发 |
| **Cloudflare** | `cloudflare-expert` | 🟡 P1 | DevOps, Security, Frontend Dev | DNS/CDN/Workers/Pages/Zero Trust/WAF 配置 |
| **Vercel / Netlify** | `frontend-deployment-expert` | 🟢 P2 | Frontend Dev, Full-stack Dev | 边缘部署、预览环境、环境变量管理、A/B 分流 |

---

### 二、容器与编排工具 / Container & Orchestration Tools

建议分类目录：`skills/tools/container/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **Docker** | `docker-expert` | 🔴 P0 | DevOps, Backend Dev, AI/ML | Dockerfile 最佳实践、多阶段构建、compose 编排、网络/卷/安全 |
| **Kubernetes (kubectl)** | `kubernetes-expert` | 🔴 P0 | DevOps, Software Arch, SRE | manifests 编写、RBAC、网络策略、HPA/VPA、故障排查 playbook |
| **Helm** | `helm-expert` | 🟡 P1 | DevOps, Platform Engineer | chart 开发、values 管理、OCI registry、chart 测试、依赖管理 |
| **ArgoCD** | `argocd-gitops-expert` | 🟡 P1 | DevOps, Platform Engineer | GitOps 工作流、Application/AppProject、sync strategies、RBAC |
| **Istio / Service Mesh** | `istio-servicemesh-expert` | 🟢 P2 | DevOps, Backend Arch | 流量管理、mTLS、可观测性集成、VirtualService/DestinationRule |

---

### 三、基础设施即代码 / Infrastructure as Code Tools

建议分类目录：`skills/tools/iac/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **Terraform** | `terraform-expert` | 🔴 P0 | DevOps, Cloud Arch, SRE | HCL 语法、provider 配置、模块化设计、状态管理、workspace/backend |
| **Ansible** | `ansible-expert` | 🟡 P1 | DevOps, SysAdmin, IT Support | playbook 编写、角色/集合、inventory 管理、Vault 加密、幂等性设计 |
| **Pulumi** | `pulumi-expert` | 🟢 P2 | DevOps, Full-stack Dev | TypeScript/Python IaC、与 Terraform 对比、状态后端选择 |

---

### 四、CI/CD 工具 / CI/CD Tools

建议分类目录：`skills/tools/cicd/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **GitHub Actions** | `github-actions-expert` | 🔴 P0 | DevOps, Software Dev, AI/ML | workflow YAML 编写、自定义 action、matrix 构建、secrets 管理、reusable workflows |
| **Jenkins** | `jenkins-expert` | 🟡 P1 | DevOps (Enterprise), Manufacturing IT | Declarative Pipeline、共享库、插件管理、分布式构建、Kubernetes agent |
| **GitLab CI/CD** | `gitlab-cicd-expert` | 🟡 P1 | DevOps, Software Dev | .gitlab-ci.yml 设计、runner 配置、cache/artifact、Auto DevOps |
| **Gerrit** ✅ | `gerrit-permission-manager` | ✅ 已实现 | DevOps, Code Review Admin | 权限管理、访问控制、多仓库批量配置 |

---

### 五、数据库工具 / Database Tools

建议分类目录：`skills/tools/database/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **PostgreSQL** | `postgresql-expert` | 🔴 P0 | Backend Dev, Data Engineer, DBA | 高级 SQL、JSONB、扩展(PostGIS/pgvector)、性能调优、复制/HA |
| **MySQL** | `mysql-expert` | 🟡 P1 | Backend Dev, DBA, Admin | 索引优化、EXPLAIN 分析、主从复制、分区、存储引擎选型 |
| **Redis** | `redis-expert` | 🔴 P0 | Backend Dev, DevOps, Data | 数据结构最佳实践、缓存模式、集群/哨兵、Lua 脚本、持久化策略 |
| **MongoDB** | `mongodb-expert` | 🟡 P1 | Backend Dev, Data Engineer | 文档设计、聚合管道、索引策略、分片架构、Atlas 操作 |
| **Elasticsearch** | `elasticsearch-expert` | 🟡 P1 | Backend Dev, Data Engineer, Security | 映射设计、查询 DSL、聚合分析、索引生命周期管理、集群调优 |
| **ClickHouse** | `clickhouse-expert` | 🟢 P2 | Data Engineer, Data Analyst | 列式存储、MergeTree 引擎族、物化视图、分布式查询优化 |
| **DuckDB** | `duckdb-expert` | 🟢 P2 | Data Analyst, Data Scientist | 嵌入式 OLAP、Parquet/CSV 直查、Python 集成、性能对比 |

---

### 六、数据平台工具 / Data Platform Tools

建议分类目录：`skills/tools/data-platform/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **Apache Kafka** | `kafka-expert` | 🔴 P0 | Data Engineer, Backend Dev, AI/ML | Topic/Partition 设计、Consumer Group、Kafka Streams、Kafka Connect、运维调优 |
| **Apache Spark** | `spark-expert` | 🔴 P0 | Data Engineer, AI/ML, Data Scientist | DataFrame API、Spark SQL、Spark Streaming、调优(内存/shuffle)、部署模式 |
| **Apache Airflow** | `airflow-expert` | 🔴 P0 | Data Engineer, ML Engineer, DevOps | DAG 设计模式、Operator 选型、XCom、动态 DAG、KubernetesPodOperator |
| **dbt (data build tool)** | `dbt-expert` | 🔴 P0 | Data Engineer, Analytics Engineer | 模型设计、ref/source、测试/文档、宏/包、dbt Cloud vs Core |
| **Apache Flink** | `flink-expert` | 🟡 P1 | Data Engineer, AI/ML | 流处理语义、状态管理、CEP、与 Kafka 集成、Flink SQL |
| **Delta Lake / Iceberg** | `lakehouse-expert` | 🟡 P1 | Data Engineer, Data Architect | ACID 事务、时间旅行、Schema 演化、与 Spark/Flink 集成 |

---

### 七、AI/ML 工具 / AI & ML Tools

建议分类目录：`skills/tools/ai-ml/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **PyTorch** | `pytorch-expert` | 🔴 P0 | AI/ML Engineer, Research Scientist | nn.Module 设计、训练循环、分布式训练(DDP)、ONNX 导出、性能调优 |
| **TensorFlow / Keras** | `tensorflow-expert` | 🟡 P1 | AI/ML Engineer, Research | tf.data、Keras API、TF Serving、TFLite、TensorBoard |
| **Jupyter Notebook** | `jupyter-expert` | 🔴 P0 | Data Scientist, Researcher, AI/ML | magic commands、nbconvert、JupyterLab 扩展、远程服务器配置、nbformat |
| **MLflow** | `mlflow-expert` | 🔴 P0 | ML Engineer, AI/ML, Data Scientist | Tracking、Model Registry、Projects、Recipes、与 Spark/Databricks 集成 |
| **Weights & Biases (W&B)** | `wandb-expert` | 🟡 P1 | ML Engineer, Research Scientist | 实验追踪、Sweeps 超参搜索、Artifacts 版本管理、Reports |
| **Hugging Face** | `huggingface-expert` | 🔴 P0 | AI/ML Engineer, LLM Engineer | Transformers/Datasets/PEFT/Accelerate 库使用、模型 Hub 操作、GGUF/量化 |
| **LangChain / LangGraph** | `langchain-expert` | 🔴 P0 | AI App Dev, AI/ML Engineer | Chain/Agent/Memory 设计、RAG 管道、Tool calling、LangSmith 调试 |
| **CUDA / cuDNN** | `cuda-expert` | 🟡 P1 | AI Chip Arch, ML Engineer | GPU 内存管理、kernel 优化、Nsight 调试、混合精度训练 |
| **vLLM / Triton** | `llm-serving-expert` | 🟡 P1 | ML Engineer, AI Platform Eng | PagedAttention、连续批处理、量化部署、性能基准测试 |
| **LlamaIndex** | `llamaindex-expert` | 🟢 P2 | AI App Dev, Backend Dev | 索引类型、查询引擎、多模态 RAG、与向量数据库集成 |

---

### 八、监控与可观测性工具 / Monitoring & Observability Tools

建议分类目录：`skills/tools/observability/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **Prometheus** | `prometheus-expert` | 🔴 P0 | DevOps, SRE, Platform Eng | PromQL 编写、Exporter 选型、Alertmanager 配置、Recording Rules、高可用 |
| **Grafana** | `grafana-expert` | 🔴 P0 | DevOps, SRE, Data Analyst | Dashboard 设计、Panel 类型、告警规则、数据源配置、Loki/Tempo 集成 |
| **ELK Stack** | `elk-stack-expert` | 🟡 P1 | DevOps, Security, Data Eng | Elasticsearch 索引、Logstash Pipeline、Kibana 可视化、Filebeat 配置 |
| **Datadog** | `datadog-expert` | 🟡 P1 | DevOps, SRE | APM/Tracing、Log Management、Synthetics、SLO 配置、Agent 部署 |
| **OpenTelemetry** | `opentelemetry-expert` | 🟡 P1 | Platform Eng, DevOps, Backend Dev | SDK 集成(Python/Java/Go)、Collector 配置、Trace/Metric/Log 三支柱 |
| **PagerDuty** | `pagerduty-expert` | 🟢 P2 | SRE, DevOps, IT Ops | 告警策略、Escalation Policy、Schedule On-call、Runbook 集成 |

---

### 九、安全工具 / Security Tools

建议分类目录：`skills/tools/security/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **HashiCorp Vault** | `vault-secrets-expert` | 🔴 P0 | DevOps, Security Eng, SRE | KV/PKI/Transit 引擎、动态凭证、Auth Methods、Agent Sidecar、策略语言 |
| **Burp Suite** | `burpsuite-expert` | 🟡 P1 | Security Engineer, Pentest | Proxy 拦截、Scanner、Intruder、Repeater、扩展开发(BApp Store) |
| **Wireshark** | `wireshark-expert` | 🟡 P1 | Security Engineer, Network Eng | 显示过滤器、协议分析、TLS 解密、自定义 Profile、统计功能 |
| **Nmap** | `nmap-expert` | 🟡 P1 | Security Engineer, Network Eng | 扫描类型、NSE 脚本、OS 探测、防火墙规避、输出格式 |
| **Metasploit** | `metasploit-expert` | 🟢 P2 | Pentest, Red Team | msfconsole 操作、exploit 选择、payload 生成(msfvenom)、后渗透模块 |
| **Trivy / Snyk** | `container-security-expert` | 🟢 P2 | DevSecOps, Security Eng | 容器/代码/IaC 漏洞扫描、CI/CD 集成、策略as代码 |

---

### 十、设计工具 / Design Tools

建议分类目录：`skills/tools/design/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **Figma** | `figma-expert` | 🔴 P0 | UX Designer, Product Mgr, Frontend Dev | 组件/变体、Auto Layout、Prototyping、Design Token、Dev Mode、插件 |
| **Adobe Photoshop** | `photoshop-expert` | 🟡 P1 | Designer, Marketing, Content | 图层蒙版、智能对象、批量动作、Camera RAW、合成技术 |
| **Adobe Illustrator** | `illustrator-expert` | 🟡 P1 | Designer, Brand, Marketing | 路径操作、图形样式、文字排版、包装设计、SVG 输出优化 |
| **Canva** | `canva-expert` | 🟡 P1 | Marketing, Content, Education | 品牌套件、模板系统、协作、Brand Hub、批量生成、API |
| **Blender** | `blender-expert` | 🟢 P2 | Creative, Entertainment, Digital Twin | 建模/材质/渲染/动画、几何节点、Python 脚本自动化 |
| **Sketch** | `sketch-expert` | 🟢 P2 | UX Designer (macOS) | Symbols、共享库、Sketch Runner、插件生态 |

---

### 十一、项目协作工具 / Project & Collaboration Tools

建议分类目录：`skills/tools/productivity/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **Jira** | `jira-expert` | 🔴 P0 | Project Mgr, Product Mgr, Engineering Lead | Issue 工作流、Sprint 规划、JQL 查询、仪表盘/报表、自动化规则 |
| **Confluence** | `confluence-expert` | 🟡 P1 | PM, Tech Writer, Knowledge Mgr | 页面模板、宏使用、空间设计、权限管理、与 Jira 集成 |
| **Notion** | `notion-expert` | 🟡 P1 | Business, Startup, Personal | 数据库设计(关联/汇总)、模板、API 集成、Notion AI、团队协作 |
| **Linear** | `linear-expert` | 🟡 P1 | Software Dev, Product, Startup | Issue/Cycle/Project 管理、工作流自动化、Git 集成、Triage |
| **Miro** | `miro-expert` | 🟢 P2 | Product Mgr, UX, Facilitator | 白板模板、远程研讨、User Journey Map、系统设计图、投票/计时 |
| **Slack** | `slack-bot-expert` | 🟡 P1 | DevOps, Software Dev, IT Admin | Workflow Builder、Bolt SDK Bot 开发、Slash Command、App 配置 |
| **Asana / Monday.com** | `asana-expert` | 🟢 P2 | Project Mgr, Operations | 项目模板、时间线、自动化规则、Portfolio 视图、集成设置 |

---

### 十二、数据分析与可视化工具 / Data Analytics Tools

建议分类目录：`skills/tools/analytics/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **Excel / Google Sheets** | `spreadsheet-expert` | 🔴 P0 | Finance, Business Analyst, Admin, HR | 高级公式(XLOOKUP/ARRAYFORMULA)、数据透视表、Power Query、VBA宏 |
| **Tableau** | `tableau-expert` | 🔴 P0 | Data Analyst, BI Developer | 计算字段、LOD表达式、参数/动作、发布到 Tableau Server/Online |
| **Power BI** | `powerbi-expert` | 🟡 P1 | Data Analyst, Finance, Business | DAX、Power Query M、数据模型设计、报告发布、RLS 行级安全 |
| **Pandas** | `pandas-expert` | 🔴 P0 | Data Scientist, ML Engineer, Analyst | DataFrame 操作、时间序列、merge/join/pivot、性能优化、与 Arrow 集成 |
| **R / RStudio** | `r-statistics-expert` | 🟡 P1 | Statistician, Researcher, Data Analyst | tidyverse、ggplot2、统计建模、Shiny 应用、R Markdown |
| **Looker / Metabase** | `bi-tool-expert` | 🟢 P2 | Data Analyst, BI Developer | LookML 模型设计、嵌入式分析、探索式查询、权限管理 |

---

### 十三、仿真与工程计算工具 / Simulation & Engineering Tools

建议分类目录：`skills/tools/engineering-simulation/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **MATLAB / Simulink** | `matlab-expert` | 🔴 P0 | Research, Aerospace, Automotive, Energy | 数值计算、Simulink 建模、工具箱调用、代码生成(Coder)、Optimization |
| **ANSYS** | `ansys-expert` | 🔴 P0 | Aerospace, Automotive, Construction | FEA/CFD 仿真设置、网格划分、边界条件、结果后处理、参数化分析 |
| **COMSOL Multiphysics** | `comsol-expert` | 🟡 P1 | Research, Energy, Semiconductor, BioTech | 多物理场耦合、几何建模、求解器配置、APP Builder |
| **Abaqus** | `abaqus-expert` | 🟡 P1 | Aerospace, Automotive, Materials | 非线性分析、材料本构、接触/摩擦、脚本自动化(Python) |
| **OpenFOAM** | `openfoam-expert` | 🟢 P2 | Aerospace, Energy, Research | 开源 CFD、网格生成(snappyHexMesh)、湍流模型、并行求解 |
| **LabVIEW** | `labview-expert` | 🟢 P2 | Research, Manufacturing, Automotive | 数据采集(DAQ)、VI 设计、实时系统、仪器控制(GPIB/VISA) |

---

### 十四、CAD/3D 建模工具 / CAD & 3D Modeling Tools

建议分类目录：`skills/tools/cad/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **AutoCAD** | `autocad-expert` | 🟡 P1 | Construction, Mechanical Eng, Architecture | 2D 绘图命令、标注样式、图层管理、块/外部参照、脚本自动化(AutoLISP) |
| **SolidWorks** | `solidworks-expert` | 🟡 P1 | Mechanical Eng, Manufacturing, Robotics | 特征建模、装配约束、工程图、仿真(Simulation)、PDM/PLM 集成 |
| **CATIA V5/V6** | `catia-expert` | 🟡 P1 | Aerospace, Automotive, High-end Mfg | Part/Assembly/Drawing 设计、曲面建模、Digital Mock-Up |
| **Revit** | `revit-bim-expert` | 🟡 P1 | Architecture, Construction, MEP | BIM 建模、族创建、施工图出图、Dynamo 参数化、协同工作(Worksharing) |
| **Rhino / Grasshopper** | `rhino-expert` | 🟢 P2 | Architecture, Product Design, Jewellery | NURBS 建模、Grasshopper 参数化设计、插件生态(Karamba/Ladybug) |
| **Fusion 360** | `fusion360-expert` | 🟢 P2 | Mechanical Eng, Maker, Manufacturing | 集成 CAD/CAM/CAE、参数化设计、3D 打印导出、PCB 布局 |

---

### 十五、开发工具与 IDE / Development Tools & IDEs

建议分类目录：`skills/tools/dev-tools/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **Git (Advanced)** | `git-advanced-expert` | 🔴 P0 | All Software Roles | 高级工作流(rebase/cherry-pick/bisect)、hooks 编写、子模块、LFS、故障排查 |
| **VS Code** | `vscode-expert` | 🔴 P0 | All Software Roles | 插件生态、launch.json/tasks.json、Remote SSH/Containers、Extensions API |
| **macOS Config** ✅ | `macos-config-expert` | ✅ 已实现 | IT Support, SysAdmin, DevOps | defaults(1)、MDM、FileVault、Homebrew、launchd |
| **Vim / Neovim** | `neovim-expert` | 🟡 P1 | Backend Dev, SysAdmin, Devops | 配置(init.lua/Lazy.nvim)、LSP 集成、Telescope/Treesitter、键位优化 |
| **Postman / Bruno** | `api-testing-expert` | 🔴 P0 | Backend Dev, QA, API Dev | Collection 组织、Environment/Variable、Pre-request 脚本、Newman CI 集成 |
| **Linux CLI Mastery** | `linux-sysadmin-expert` | 🔴 P0 | DevOps, Backend, SysAdmin | systemd、网络工具(ip/ss/tc)、性能分析(perf/strace/ltrace)、cgroups |
| **JetBrains IDEs** | `jetbrains-expert` | 🟢 P2 | Java/Kotlin/Python Dev | 数据库工具、调试技巧、Live Template、插件配置、远程解释器 |
| **FFmpeg** | `ffmpeg-expert` | 🟢 P2 | Media, Content, Creative | 转码滤镜链、流媒体协议(HLS/RTMP)、批处理脚本、硬件加速 |

---

### 十六、游戏引擎 / Game Engines

建议分类目录：`skills/tools/game-engine/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **Unity** | `unity-expert` | 🟡 P1 | Entertainment, Education, Digital Twin | 组件系统、物理引擎、着色器(URP/HDRP)、XR 开发、Editor脚本(C#) |
| **Unreal Engine** | `unreal-expert` | 🟡 P1 | Entertainment, Aerospace Sim, Architecture | Blueprint/C++ 开发、Nanite/Lumen、数字孪生(Pixel Streaming)、MetaHuman |
| **Godot** | `godot-expert` | 🟢 P2 | Indie Dev, Education | GDScript/C# 脚本、2D/3D 场景、Export、轻量级架构优势 |

---

### 十七、企业应用软件 / Enterprise Application Tools

建议分类目录：`skills/tools/enterprise/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **SAP ERP (S/4HANA)** | `sap-expert` | 🔴 P0 | Manufacturing, Logistics, Finance, Admin | 模块操作(MM/SD/FI/CO/PP)、事务码速查、ABAP 基础、报表配置 |
| **Salesforce CRM** | `salesforce-expert` | 🟡 P1 | Sales, Marketing, Business Dev | 对象模型、Flow 自动化、Apex 基础、报表/仪表板、集成(API/Webhook) |
| **ServiceNow** | `servicenow-expert` | 🟡 P1 | IT Service Mgmt, ITSM Admin | Incident/Change/Problem 流程、Flow Designer、CMDB、REST API |
| **Workday** | `workday-expert` | 🟢 P2 | HR, Finance, Operations | 人力资源模块、薪酬配置、集成(Studio)、Prism Analytics、报告工具 |
| **Zendesk** | `zendesk-expert` | 🟢 P2 | Customer Support, Operations | 工单工作流、宏/触发器、自助服务知识库、Zendesk API、Help Center |
| **Gerrit** ✅ | `gerrit-permission-manager` | ✅ 已实现 | DevOps, Code Review Admin | 权限管理 |
| **OpenClaw** ✅ | `openclaw-ops-expert` | ✅ 已实现 | AI Ops, Personal AI | 网关配置、频道集成 |

---

### 十八、科学计算与数据科学工具 / Scientific Computing Tools

建议分类目录：`skills/tools/scientific/`

| 工具 | 建议 Skill 名称 | 优先级 | 主要使用角色 | 技能化核心价值 |
|------|----------------|--------|------------|--------------|
| **NumPy / SciPy** | `numpy-scientific-expert` | 🟡 P1 | Data Scientist, Researcher, AI/ML | 广播机制、线性代数(linalg)、信号处理(FFT)、优化(optimize)、稀疏矩阵 |
| **scikit-learn** | `sklearn-expert` | 🟡 P1 | ML Engineer, Data Scientist | Pipeline 设计、特征工程、交叉验证、超参调优、模型持久化 |
| **LaTeX** | `latex-expert` | 🟡 P1 | Researcher, Academic, Tech Writer | 文档结构、数学公式、参考文献(BibTeX/biblatex)、期刊模板、TikZ 绘图 |
| **SPSS / SAS** | `statistical-analysis-expert` | 🟢 P2 | Statistician, Researcher, Healthcare | 描述统计、假设检验、回归分析、生存分析、输出解读 |

---

## 实现优先级汇总 / Implementation Priority Summary

### 🔴 P0 — 立即实现 (26 个工具)

| 类别 | 工具清单 |
|------|---------|
| 云平台 | AWS, GCP, Azure |
| 容器编排 | Docker, Kubernetes |
| IaC | Terraform |
| CI/CD | GitHub Actions |
| 数据库 | PostgreSQL, Redis |
| 数据平台 | Kafka, Spark, Airflow, dbt |
| AI/ML | PyTorch, Jupyter, MLflow, Hugging Face, LangChain |
| 监控 | Prometheus, Grafana |
| 安全 | HashiCorp Vault |
| 分析 | Excel/Sheets, Tableau, Pandas |
| 工程仿真 | MATLAB, ANSYS |
| 开发工具 | Git Advanced, VS Code, Postman, Linux CLI |
| 企业应用 | SAP |

### 🟡 P1 — 优先实现 (30 个工具)

Alibaba Cloud, Helm, ArgoCD, Ansible, Jenkins, GitLab CI, MySQL, MongoDB, Elasticsearch, Flink, TensorFlow, W&B, CUDA, vLLM, ELK Stack, Datadog, OpenTelemetry, Photoshop, Illustrator, Canva, Confluence, Notion, Linear, Slack Bot, Power BI, R/RStudio, COMSOL, Abaqus, AutoCAD, SolidWorks, CATIA, Revit, Neovim, Unity, Unreal, Salesforce, ServiceNow, NumPy/SciPy, scikit-learn, LaTeX

### 🟢 P2 — 规划实现 (24 个工具)

Vercel/Netlify, Pulumi, Istio, ClickHouse, DuckDB, Delta Lake, LlamaIndex, PagerDuty, Trivy/Snyk, Metasploit, Blender, Sketch, Miro, Asana, Looker/Metabase, OpenFOAM, LabVIEW, Rhino/Grasshopper, Fusion 360, FFmpeg, Godot, Workday, Zendesk, SPSS/SAS

---

## 建议目录结构 / Suggested Directory Structure

```
skills/
└── tools/                          # 新增顶层分类：软件工具技能
    ├── cloud/                      # 云平台
    │   ├── aws-cloud-expert/
    │   ├── gcp-cloud-expert/
    │   ├── azure-cloud-expert/
    │   ├── aliyun-cloud-expert/
    │   └── cloudflare-expert/
    ├── container/                  # 容器与编排
    │   ├── docker-expert/
    │   ├── kubernetes-expert/
    │   ├── helm-expert/
    │   └── argocd-gitops-expert/
    ├── iac/                        # 基础设施即代码
    │   ├── terraform-expert/
    │   └── ansible-expert/
    ├── cicd/                       # CI/CD
    │   ├── github-actions-expert/
    │   ├── jenkins-expert/
    │   └── gitlab-cicd-expert/
    ├── database/                   # 数据库
    │   ├── postgresql-expert/
    │   ├── mysql-expert/
    │   ├── redis-expert/
    │   ├── mongodb-expert/
    │   └── elasticsearch-expert/
    ├── data-platform/              # 数据平台
    │   ├── kafka-expert/
    │   ├── spark-expert/
    │   ├── airflow-expert/
    │   └── dbt-expert/
    ├── ai-ml/                      # AI/ML 工具
    │   ├── pytorch-expert/
    │   ├── jupyter-expert/
    │   ├── mlflow-expert/
    │   ├── huggingface-expert/
    │   └── langchain-expert/
    ├── observability/              # 监控可观测性
    │   ├── prometheus-expert/
    │   ├── grafana-expert/
    │   └── elk-stack-expert/
    ├── security/                   # 安全工具
    │   ├── vault-secrets-expert/
    │   ├── burpsuite-expert/
    │   └── nmap-expert/
    ├── design/                     # 设计工具
    │   ├── figma-expert/
    │   ├── photoshop-expert/
    │   └── canva-expert/
    ├── productivity/               # 项目协作
    │   ├── jira-expert/
    │   ├── notion-expert/
    │   └── slack-bot-expert/
    ├── analytics/                  # 数据分析
    │   ├── spreadsheet-expert/
    │   ├── tableau-expert/
    │   └── pandas-expert/
    ├── engineering-simulation/     # 工程仿真
    │   ├── matlab-expert/
    │   └── ansys-expert/
    ├── cad/                        # CAD 建模
    │   ├── solidworks-expert/
    │   └── revit-bim-expert/
    ├── dev-tools/                  # 开发工具
    │   ├── git-advanced-expert/
    │   ├── vscode-expert/
    │   ├── linux-sysadmin-expert/
    │   └── api-testing-expert/
    ├── game-engine/                # 游戏引擎
    │   ├── unity-expert/
    │   └── unreal-expert/
    └── enterprise/                 # 企业应用
        ├── sap-expert/
        └── salesforce-expert/
```

---

## 角色 × 工具矩阵 / Role × Tool Matrix

核心工具覆盖的角色类别（Top 20 工具 × 主要使用角色）：

| 工具 | Software | DevOps | AI/ML | Data | Finance | Business | Research | Manufacturing | Security | Design |
|------|----------|--------|-------|------|---------|----------|----------|---------------|----------|--------|
| AWS | ✓ | ✓ | ✓ | ✓ | | | | | | |
| Kubernetes | ✓ | ✓ | ✓ | ✓ | | | | | | |
| Kafka | ✓ | ✓ | ✓ | ✓ | | | | ✓ | | |
| Redis | ✓ | ✓ | ✓ | ✓ | | | | | | |
| PyTorch | ✓ | | ✓ | ✓ | | | ✓ | | | |
| MATLAB | | | ✓ | ✓ | | | ✓ | ✓ | | |
| Terraform | ✓ | ✓ | | | | | | | | |
| dbt | ✓ | | | ✓ | ✓ | ✓ | | | | |
| Airflow | ✓ | ✓ | ✓ | ✓ | | | | | | |
| PostgreSQL | ✓ | ✓ | | ✓ | ✓ | | | | | |
| Excel | | | | ✓ | ✓ | ✓ | ✓ | | | |
| SAP | | | | | ✓ | ✓ | | ✓ | | |
| Figma | ✓ | | | | | ✓ | | | | ✓ |
| Prometheus | ✓ | ✓ | | | | | | | | |
| LangChain | ✓ | | ✓ | | | | | | | |
| Jira | ✓ | ✓ | ✓ | ✓ | | ✓ | | | | |
| Vault | ✓ | ✓ | | | | | | | ✓ | |
| Tableau | | | | ✓ | ✓ | ✓ | ✓ | | | |
| ANSYS | | | | | | | ✓ | ✓ | | |
| GitHub Actions | ✓ | ✓ | ✓ | ✓ | | | | | | |

---

## 技能化实现模板要点 / Key Points for Tool Skill Implementation

软件工具技能与角色技能的结构差异：

### 角色技能 vs 工具技能

| 维度 | 角色技能 (Role Skill) | 工具技能 (Tool Skill) |
|------|---------------------|---------------------|
| **定位** | 模拟某职业角色的思维与决策 | 成为某款工具的专家用户 |
| **System Prompt 核心** | 职业背景、行业经验、决策框架 | 工具架构原理、命令速查、最佳实践 |
| **知识库核心** | 行业知识、方法论、案例 | 配置参数、常见错误、性能调优 |
| **输出形式** | 分析建议、策略文档 | 命令/配置代码片段、Runbook、示例文件 |
| **触发关键词** | 角色名称、行业场景 | 工具名称、操作场景("如何配置X") |

### 工具技能必备内容

1. **快速命令参考 (Quick Command Reference)** — 最常用的 20 个命令/操作
2. **配置模板 (Config Templates)** — 生产级别可直接使用的配置片段
3. **故障排查手册 (Troubleshooting Playbook)** — 常见错误码及解决步骤
4. **最佳实践清单 (Best Practice Checklist)** — 安全、性能、可维护性核查点
5. **版本差异说明 (Version Notes)** — 主要版本之间的重要变更

---

*生成时间: 2026-03-15 | 基于 471 个角色技能的工具交叉分析*
*Generated: 2026-03-15 | Based on cross-analysis of 471 role skills*
