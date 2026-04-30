# Standards & Reference

## 7.1 Official Documentation

- [腾讯混元大模型](https://cloud.tencent.com/product/hunyuan)
- [混元API文档](https://cloud.tencent.com/document/product/1729)
- [混元SDK下载](https://github.com/TencentCloud/tencentcloud-sdk-cpp-intl)
- [混元定价](https://cloud.tencent.com/document/product/1729/97723)

## 7.2 模型服务

### 7.2.1 模型列表

| 模型 | 适用场景 | 输入价格 | 输出价格 |
|------|---------|----------|----------|
| hunyuan-standard | 标准对话 | ¥0.0009/千token | ¥0.0009/千token |
| hunyuan-pro | 高性能(256K上下文) | ¥0.006/千token | ¥0.006/千token |
| hunyuan-lite | 轻量级 | ¥0.0005/千token | ¥0.0005/千token |
| hunyuan-vision | 多模态图文 | ¥0.0011/千token | ¥0.0011/千token |

### 7.2.2 API Endpoint

```
https://hunyuan.cloud.tencent.com
```

## 7.3 API调用

### 7.3.1 Python SDK

```bash
pip install tencentcloud-sdk-python
```

```python
from tencentcloud.common import credential
from tencentcloud.hunyuan.v20230901 import hunyuan_client

cred = credential.Credential("SecretId", "SecretKey")
client = hunyuan_client.HunyuanClient(cred, "ap-guangzhou")

# 同步调用
req = Models.ChatCompletionsRequest()
req.Model = "hunyuan-standard"
req.Messages = [
    {"Role": "user", "Content": "你好"}
]
resp = client.ChatCompletions(req)
print(resp.Choices[0].Message.Content)
```

### 7.3.2 cURL调用

```bash
curl -X POST https://hunyuan.cloud.tencent.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $SecretId:$SecretKey" \
  -d '{
    "model": "hunyuan-standard",
    "messages": [{"role": "user", "content": "你好"}]
  }'
```

## 7.4 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| model | string | 必填 | hunyuan-standard/pro/lite |
| messages | array | 必填 | 对话消息列表 |
| temperature | float | 0.5 | 创造性(0-2) |
| top_p | float | 0.7 | 核采样 |
| max_tokens | int | 2048 | 最大Token数 |
| stream | bool | false | 流式输出 |
| stream_options | object | - | 流式输出控制 |

## 7.5 多轮对话

```python
messages = [
    {"Role": "system", "Content": "你是一个专业的Python导师"},
    {"Role": "user", "Content": "什么是装饰器?"},
    {"Role": "assistant", "Content": "装饰器是Python中..."},
    {"Role": "user", "Content": "能给个例子吗?"}
]
# 多轮对话只需追加历史消息
```
