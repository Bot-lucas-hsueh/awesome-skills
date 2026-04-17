# Troubleshooting

## 8.1 API调用问题

### 8.1.1 403 Forbidden

**排查:**
```bash
# 确认AccessKey和SecretKey正确
export VOLC_ACCESS_KEY="your_access_key"
export VOLC_SECRET_KEY="your_secret_key"

# 测试连接
curl -X POST https://ark.cn-beijing.volces.com/api/v3/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $VOLC_ACCESS_KEY:$VOLC_SECRET_KEY" \
  -d '{"model":"doubao-pro-32k","messages":[{"role":"user","content":"hi"}]}'
```

### 8.1.2 400 Bad Request

**常见原因:**
- 模型名称错误
- messages格式错误
- 超过上下文限制

```python
# 正确格式
messages = [
    {"role": "user", "content": "你好"}
]
```

## 8.2 响应问题

### 8.2.1 回复被截断

**解决方案:**
```python
response = service.post(
    '/api/v3/chat/completions',
    {
        'model': 'doubao-pro-32k',
        'messages': messages,
        'max_tokens': 4000  # 增加max_tokens
    },
    {}
)
```

### 8.2.2 响应质量差

**解决方案:**
```python
# 调整temperature
params = {
    'model': 'doubao-pro-32k',
    'messages': messages,
    'temperature': 0.5,  # 降低随机性
    'top_p': 0.9
}
```

## 8.3 计费问题

### 8.3.1 Token计算

```python
# 响应中包含usage
response = service.post(...)
print(response.json())
# {"usage": {"prompt_tokens": 100, "completion_tokens": 200}}
```
