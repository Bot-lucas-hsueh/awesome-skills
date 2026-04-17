# Troubleshooting

## 8.1 API调用问题

### 8.1.1 403 Forbidden

**原因:** API-KEY无效或过期

**解决方案:**
```bash
# 确认API-KEY正确
export DASHSCOPE_API_KEY="sk-xxxxxxxx"

# 验证API-KEY有效性
curl -X POST https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"qwen-turbo","messages":[{"role":"user","content":"hi"}]}'
```

### 8.1.2 400 Bad Request

**常见原因:**
- 模型名称错误
- messages格式不正确
- 超过模型上下文限制

**排查:**
```python
# 检查messages格式
messages = [
    {"role": "system", "content": "你是助手"},
    {"role": "user", "content": "问题"}
]
```

### 8.1.3 429 Rate Limit

**原因:** 请求频率超出限制

**解决方案:**
```python
import time
import requests

# 添加重试逻辑
def call_with_retry(messages, max_retries=3):
    for i in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code != 429:
                return response.json()
        except Exception as e:
            print(f"请求失败: {e}")
        time.sleep(2 ** i)  # 指数退避
```

## 8.2 响应质量问题

### 8.2.1 回复过于随机

**症状:** 相同问题得到不同回答

**解决方案:**
```python
# 设置较低的temperature
response = Generation.call(
    model="qwen-plus",
    messages=messages,
    temperature=0.3,  # 更确定性
    top_p=0.8
)
```

### 8.2.2 输出被截断

**症状:** 回复不完整

**解决方案:**
```python
# 增加max_tokens
response = Generation.call(
    model="qwen-plus",
    messages=messages,
    max_tokens=4000  # 增大限制
)
```

## 8.3 成本问题

### 8.3.1 Token费用超预期

**排查:**
1. 检查输入Token: messages总长度
2. 检查输出Token: response.token_usage

```python
response = Generation.call(
    model="qwen-plus",
    messages=messages
)
usage = response.usage
print(f"输入: {usage.input_tokens}, 输出: {usage.output_tokens}")
```

**优化策略:**
- 精简system prompt
- 设置max_tokens上限
- 使用qwen-turbo替代qwen-max做测试
