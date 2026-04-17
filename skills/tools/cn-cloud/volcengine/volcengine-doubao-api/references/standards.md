# Standards & Reference

## 7.1 Official Documentation

- [火山引擎控制台](https://console.volcengine.com)
- [豆包大模型文档](https://www.volcengine.com/docs/82379/1263482)
- [API定价](https://www.volcengine.com/docs/82379/1263482)
- [火山引擎SDK](https://github.com/volcengine)

## 7.2 模型服务

### 7.2.1 豆包模型

| 模型 | 输入价格 | 输出价格 | 上下文 | 适用场景 |
|------|---------|---------|--------|---------|
| doubao-pro-32k | ¥0.0008/千token | ¥0.0024/千token | 32K | 标准对话 |
| doubao-pro-128k | ¥0.0015/千token | ¥0.0045/千token | 128K | 长文本处理 |
| doubao-lite-32k | ¥0.0003/千token | ¥0.0006/千token | 32K | 高并发/简单任务 |
| doubao-lite-128k | ¥0.0005/千token | ¥0.001/千token | 128K | 长文本低成本 |

### 7.2.2 API Endpoint

```
https://ark.cn-beijing.volces.com/api/v3/chat/completions
```

## 7.3 API调用

### 7.3.1 Python SDK

```bash
pip install volcengine-python-sdk
```

```python
from volcengine.ApiInfo import ApiInfo
from volcengine.Credentials import Credentials
from volcengine.base.Service import Service

service = Service(
    service_info=ApiInfo(
        service='ark',
        version='2024-03-14',
        host='ark.cn-beijing.volces.com',
        header={},
        credentials=Credentials('', '', 'Access Key ID', 'Secret Access Key')
    ),
    api_info={}
)

response = service.post(
    '/api/v3/chat/completions',
    {
        'model': 'doubao-pro-32k',
        'messages': [
            {'role': 'user', 'content': '你好'}
        ]
    },
    {}
)
print(response)
```

### 7.3.2 cURL调用

```bash
curl -X POST https://ark.cn-beijing.volces.com/api/v3/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $VOLC_ACCESS_KEY:$VOLC_SECRET_KEY" \
  -d '{
    "model": "doubao-pro-32k",
    "messages": [{"role": "user", "content": "你好"}]
  }'
```

## 7.4 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| model | string | 必填 | 模型名称 |
| messages | array | 必填 | 对话消息 |
| stream | bool | false | 流式输出 |
| max_tokens | int | 4096 | 最大生成Token |
| temperature | float | 0.7 | 创造性(0-1) |
| top_p | float | 0.7 | 核采样 |

## 7.5 Token计算

| 内容类型 | 估算 |
|---------|------|
| 中文字符 | ~1-2字符/Token |
| 英文字符 | ~4字符/Token |
| 1000中文字 | ~800-1500 Token |
