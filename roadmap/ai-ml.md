# AI / 机器学习职业路径 AI & ML Roadmap

> 覆盖方向：机器学习工程师 · 数据科学家 · LLM研究员 · AI产品经理 · Prompt工程师 · AI安全研究员

---

## 职业全景

```
AI / ML领域
├── 算法/研究方向
│   ├── ML研究员 → AI研究科学家 → Research Director
│   ├── LLM研究员 → 大模型核心研究员 → AI Lab负责人
│   └── AI安全研究员 → AI对齐研究员
├── 工程方向
│   ├── ML工程师 → 高级ML工程师 → ML平台负责人
│   ├── LLM训练工程师 → 大模型基础设施负责人
│   └── AI应用工程师 → AI架构师
├── 产品方向
│   ├── AI产品经理 → AI产品总监
│   └── Prompt工程师 → Prompt架构师
└── 垂直应用
    ├── CV工程师（计算机视觉）
    ├── NLP工程师（自然语言处理）
    └── 推荐系统工程师
```

---

## 数学基础要求（越早打好越好）

所有AI/ML方向需要的数学基础：

- **线性代数**: 矩阵运算、特征值/特征向量、SVD分解
- **概率统计**: 贝叶斯定理、分布、最大似然估计、假设检验
- **微积分**: 偏导数、链式法则（反向传播的基础）
- **最优化**: 梯度下降、Adam、学习率调度

---

## 🌱 第1级 · 入门 (0-12个月)

### 目标
理解ML基本概念，能运行和修改已有模型，完成第一个端到端ML项目。

### 必备技能
- [ ] Python数据科学生态：NumPy、Pandas、Matplotlib
- [ ] ML基础概念：监督/无监督/强化学习、过拟合、交叉验证
- [ ] Scikit-learn：分类、回归、聚类基础算法
- [ ] 深度学习入门：神经网络、激活函数、反向传播直觉
- [ ] PyTorch或TensorFlow基础用法
- [ ] Jupyter Notebook / Colab工作流

### 第一个项目建议
- 房价预测（回归）
- 图片分类（CNN + CIFAR-10）
- 情感分析（文本分类）

### 学习资源
- fast.ai（强烈推荐，自顶向下学习法）
- Andrew Ng - Machine Learning Specialization (Coursera)
- Deep Learning.AI系列课程
- Kaggle入门竞赛

### 常见陷阱 ⚠️
- 数学焦虑：不需要完全理解所有数学才能开始，边学边补
- 工具焦虑：先掌握PyTorch，不要同时学TF和PyTorch
- 跳过EDA：数据探索是ML项目的核心，不能省略

---

## 🌿 第2级 · 初级 (1-3年)

### 目标
能独立完成ML项目全流程，理解模型选择和调优，开始接触生产环境。

### 必备技能

**机器学习工程**
- [ ] 特征工程：编码、归一化、特征选择、特征创建
- [ ] 模型调优：超参数搜索（Grid Search、Optuna）
- [ ] 模型评估：混淆矩阵、AUC-ROC、NDCG等
- [ ] 集成方法：XGBoost、LightGBM、随机森林
- [ ] 数据不平衡处理：SMOTE、类权重

**深度学习**
- [ ] CNN架构：ResNet、EfficientNet（CV方向）
- [ ] Transformer基础：自注意力机制、BERT/GPT入门
- [ ] 训练技巧：BatchNorm、Dropout、学习率Warmup
- [ ] GPU训练基础（单卡）

**LLM应用方向**
- [ ] Prompt工程基础：few-shot、chain-of-thought
- [ ] LangChain / LlamaIndex基础
- [ ] RAG（检索增强生成）基础实现
- [ ] OpenAI API / Anthropic API调用

**MLOps基础**
- [ ] 实验追踪：MLflow / Weights & Biases
- [ ] 模型版本管理
- [ ] 基础模型部署（FastAPI + Docker）

### 关键里程碑
- ✅ Kaggle竞赛排名进入前30%
- ✅ 在生产环境部署一个ML模型
- ✅ A/B测试验证模型效果提升

---

## 🌳 第3级 · 中级 (3-6年)

### 目标
能设计完整的ML系统，具备MLOps能力，在特定垂直方向有深度。

### 必备技能

**ML系统设计**
- [ ] 特征工程平台（Feature Store）
- [ ] 模型服务：TorchServe / Triton Inference Server
- [ ] 在线学习 vs 批量训练策略
- [ ] 数据飞轮设计
- [ ] 训练/服务一致性（Training-Serving Skew）

**大模型工程（LLM方向）**
- [ ] 微调技术：LoRA、QLoRA、Instruction Tuning
- [ ] 分布式训练：DDP、FSDP、DeepSpeed
- [ ] 模型量化：INT8/INT4推理优化
- [ ] Evaluation框架设计（LLM评估）
- [ ] RLHF基础理解

**高级RAG**
- [ ] 向量数据库（Pinecone / Weaviate / Milvus）
- [ ] 混合检索（BM25 + 向量检索）
- [ ] Reranking策略
- [ ] Agentic RAG / Self-RAG

**AI产品能力（PM方向）**
- [ ] AI需求分析：能力边界评估
- [ ] 模型选型框架（延迟/成本/质量三角）
- [ ] AI功能评估指标设计
- [ ] 人机协作UX设计

### 关键里程碑
- ✅ 设计并落地一个端到端ML Pipeline
- ✅ 将模型延迟降低50%或成本降低30%
- ✅ 带领3-5人团队完成ML项目

---

## 🦅 第4级 · 高级 (6-10年)

### 目标
行业级技术影响力，能从0到1构建AI基础设施或完成顶级研究。

### 工程方向核心能力
- [ ] 万亿参数模型训练架构设计
- [ ] 自研推理引擎优化（CUDA编程）
- [ ] 大规模数据处理平台（PB级）
- [ ] AI平台产品化（给公司内部提供ML能力）
- [ ] 行业AI解决方案架构

### 研究方向核心能力
- [ ] 在顶级会议发表论文（NeurIPS/ICML/ICLR/ACL）
- [ ] 独立提出新的算法/架构
- [ ] 指导博士生和初级研究员
- [ ] 获得重要科研项目/基金

### AI安全方向
- [ ] Red-teaming大型语言模型
- [ ] Constitutional AI实践
- [ ] 机器学习安全（对抗攻击/后门攻击）
- [ ] AI监管政策理解与参与

### 关键里程碑
- ✅ 主导一个在生产服务亿级用户的AI系统
- ✅ 发表被引用100+的顶级论文（研究方向）
- ✅ 培养出至少2名中级ML工程师/研究员

---

## 👑 第5级 · 精英 (10年+)

### 研究精英标志
- 🏆 谷歌/Anthropic/OpenAI等顶级AI Lab核心研究员
- 🏆 提出改变行业范式的算法（Transformer级别）
- 🏆 Google Scholar H-index 30+
- 🏆 受邀在世界顶级AI会议做主旨演讲

### 工程精英标志
- 🏆 设计了服务10亿+用户的AI系统
- 🏆 带领100+人AI工程团队
- 🏆 主导开源AI项目（GitHub 10K+ Star）
- 🏆 在AI独角兽公司担任CTO/VP of Engineering

### Prompt工程精英路径
```
入门 → 学会基础提示词写作 →
初级 → 掌握Chain-of-Thought、Few-shot等技术 →
中级 → 设计Prompt评估框架、企业级Prompt管理 →
高级 → 提示词工程平台设计、LLM能力边界研究 →
精英 → AI交互范式定义者 / AI产品首席架构
```

---

## 关键技术栈速查

| 方向 | 主要工具栈 |
|------|-----------|
| ML工程 | PyTorch · scikit-learn · XGBoost · MLflow · Kubeflow |
| LLM训练 | DeepSpeed · FSDP · Megatron-LM · vLLM |
| LLM应用 | LangChain · LlamaIndex · Pinecone · Weaviate |
| MLOps | Weights&Biases · Airflow · dbt · Ray |
| 推理优化 | TensorRT · ONNX · vLLM · Triton |

---

## 关联技能文件

- [`skills/ai-ml/ml-engineer/`](../skills/ai-ml/ml-engineer/) — 机器学习工程师
- [`skills/ai-ml/llm-research-scientist/`](../skills/ai-ml/llm-research-scientist/) — LLM研究科学家
- [`skills/ai-ml/ai-application-engineer/`](../skills/ai-ml/ai-application-engineer/) — AI应用工程师
- [`skills/ai-ml/prompt-engineer/`](../skills/ai-ml/prompt-engineer/) — Prompt工程师
- [`skills/ai-ml/ai-product-manager/`](../skills/ai-ml/ai-product-manager/) — AI产品经理
- [`skills/ai-ml/ai-safety-researcher/`](../skills/ai-ml/ai-safety-researcher/) — AI安全研究员
- [`skills/ai-ml/llm-training-engineer/`](../skills/ai-ml/llm-training-engineer/) — LLM训练工程师
- [`skills/data/data-scientist/`](../skills/data/data-scientist/) — 数据科学家
