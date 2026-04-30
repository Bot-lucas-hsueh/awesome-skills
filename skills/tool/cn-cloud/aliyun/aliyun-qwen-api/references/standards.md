# Standards & Reference

## 7.1 Official Documentation

- [DashScope控制台](https://dashscope.console.aliyun.com)
- [通义千问API文档](https://help.aliyun.com/zh/model-studio)
- [模型列表](https://help.aliyun.com/zh/model-studio/getting-started/models)
- [Token计算器](https://help.aliyun.com/zh/model-studio/dev-guide/token-calculate)

## 7.2 模型选择标准

### 7.2.1 模型对比

| 模型 | 上下文 | 输入价格 | 输出价格 | 适用场景 |
|------|--------|---------|---------|---------|
| qwen-max | 32K | ¥0.04/千token | ¥0.12/千token | 复杂推理/专业任务 |
| qwen-plus | 131K | ¥0.004/千token | ¥0.012/千token | 标准对话(推荐) |
| qwen-turbo | 128K | ¥0.001/千token | ¥0.002/千token | 快速响应/高并发 |
| qwen-long | 1000K | ¥0.001/千token | ¥0.002/千token | 长文本处理 |

### 7.2.2 Token计算

| 内容类型 | 估算 |
|---------|------|
| 中文字符 | 1-2字符 ≈ 1 Token |
| 英文字符 | 4字符 ≈ 1 Token |
| 图片(视觉模型) | 按像素和模型定价 |

## 7.3 API配置

### 7.3.1 API Endpoint

```
https://dashscope.aliyuncs.com/compatible-mode/v1
```

### 7.3.2 请求头

```
Authorization: Bearer {DASHSCOPE_API_KEY}
Content-Type: application/json
```

### 7.3.3 Python SDK安装

```bash
pip install dashscope
```

```python
import os
os.environ["DASHSCOPE_API_KEY"] = "sk-xxxxxxxx"
```

## 7.4 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| model | string | 必填 | 模型名称 |
| messages | array | 必填 | 对话消息列表 |
| temperature | float | 0.7 | 创造性(0-2) |
| top_p | float | 0.8 | 核采样 |
| max_tokens | int | - | 最大生成Token数 |
| stream | bool | false | 流式输出 |
| seed | int | - | 随机种子 |

## 7.5 成本优化策略

| 策略 | 节省比例 | 适用场景 |
|------|---------|---------|
| 使用qwen-turbo | 50-80% | 简单问答 |
| 精简prompt | 20-40% | 所有场景 |
| 设置max_tokens | 10-30% | 可预估长度时 |
| 缓存对话 | 按具体方案 | 多轮对话 |
