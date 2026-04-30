# Standards & Reference

## 7.1 Official Documentation

- [百炼Model Studio控制台](https://bailian.console.aliyun.com)
- [百炼API文档](https://help.aliyun.com/zh/model-studio)
- [DashScope SDK文档](https://help.aliyun.com/document_detail/2651806.html)
- [阿里云AI开放平台](https://help.aliyun.com/zh/model-studio/developer-reference/use-dashscope)

## 7.2 Core Concepts

### 7.2.1 模型服务

| 模型 | 适用场景 | 输入价格 | 输出价格 |
|------|---------|----------|----------|
| qwen-max | 复杂推理 | ¥0.04/千token | ¥0.12/千token |
| qwen-plus | 标准对话 | ¥0.004/千token | ¥0.012/千token |
| qwen-turbo | 快速响应 | ¥0.001/千token | ¥0.002/千token |
| qwen-long | 长文本处理 | ¥0.001/千token | ¥0.002/千token |
| text-embedding-v3 | 向量嵌入 | ¥0.0001/千token | - |

### 7.2.2 API Endpoint

```
https://dashscope.aliyuncs.com/compatible-mode/v1
```

### 7.2.3 Python SDK安装

```bash
pip install dashscope
```

## 7.3 RAG知识库配置

### 7.3.1 Embedding模型选择

| 模型 | 向量维度 | 适用场景 |
|------|---------|---------|
| text-embedding-v3 | 1536 | 通用场景(推荐) |
| text-embedding-v2 | 1536 | 兼容旧版 |

### 7.3.2 知识库参数

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| chunk_size | 单个文档块字符数 | 500-800 |
| chunk_overlap | 块之间重叠字符 | 50-100 |
| top_k | 召回文档数 | 3-5 |

## 7.4 SDK Version Compatibility

| SDK版本 | 状态 | 备注 |
|---------|------|------|
| dashscope >= 1.14.0 | 推荐 | 支持所有最新模型 |
| dashscope 1.10.x | 兼容 | 遗留系统可用 |
| openai SDK兼容 | 支持 | 设置base_url即可 |
