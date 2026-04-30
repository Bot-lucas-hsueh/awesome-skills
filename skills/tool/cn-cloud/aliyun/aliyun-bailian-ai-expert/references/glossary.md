# Glossary

## 9.1 核心概念

| 术语 | 英文 | 定义 |
|------|------|------|
| 百炼 | Bailian | 阿里云一站式大模型开发平台，提供Model Studio、API服务、知识库等 |
| 通义千问 | Qwen | 阿里云自研大语言模型系列 |
| DashScope | - | 阿里云模型服务API的统一接入地址 |
| Token | - | 模型处理的最小文本单位，中文约1-2字符/Token |

## 9.2 RAG相关

| 术语 | 英文 | 定义 |
|------|------|------|
| RAG | Retrieval-Augmented Generation | 检索增强生成，结合知识库检索与LLM生成 |
| Embedding | - | 将文本转为向量的技术，用于语义检索 |
| Chunk | - | 文档分块，将长文档切分为可检索的小段落 |
| 向量数据库 | Vector DB | 存储文本向量表示的数据库，支持相似度检索 |
| 召回 | Recall | 从知识库中检索与问题相关的文档片段 |
| 幻觉 | Hallucination | 模型生成知识库中不存在的内容 |

## 9.3 API相关

| 术语 | 定义 |
|------|------|
| API-KEY | 调用百炼API的凭证，需要妥善保管 |
| base_url | DashScope API接入地址: `https://dashscope.aliyuncs.com/compatible-mode/v1` |
| temperature | 控制生成随机性，0最确定，2最随机 |
| top_p | 核采样参数，控制候选词范围 |
| max_tokens | 生成内容的最大Token数上限 |

## 9.4 定价相关

| 术语 | 定义 |
|------|------|
| 输入Token | 用户提问和对话历史的Token数 |
| 输出Token | 模型生成回复的Token数 |
| 预置模型 | 模型已在云端加载，不收取模型加载费 |
| 后付费 | 按实际调用量计费，按月结算 |
