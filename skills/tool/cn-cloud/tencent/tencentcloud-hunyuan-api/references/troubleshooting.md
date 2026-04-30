# Troubleshooting

## 8.1 API调用问题

### 8.1.1 认证失败

**症状:** 403 Forbidden或签名验证失败

**解决方案:**
```python
# 确认SecretId和SecretKey正确
# SecretId: 用于标识用户身份
# SecretKey: 用于签名验证

# 建议使用子账号密钥(权限更精细)
# 腾讯云控制台 → 访问管理 → 子用户
```

### 8.1.2 请求超时

**原因:** 网络问题或服务端繁忙

**解决方案:**
```python
import requests

response = requests.post(
    url,
    headers=headers,
    json=data,
    timeout=30  # 设置超时
)
```

## 8.2 内容质量问题

### 8.2.1 回复内容被截断

**症状:** 回复不完整

**解决方案:**
```python
# 增加max_tokens
params = {
    "model": "hunyuan-standard",
    "messages": messages,
    "max_tokens": 4000  # 增大限制
}
```

### 8.2.2 回复过于随机

**解决方案:**
```python
params = {
    "model": "hunyuan-standard",
    "messages": messages,
    "temperature": 0.3,  # 降低随机性
    "top_p": 0.8
}
```

## 8.3 计费问题

### 8.3.1 Token计算错误

**排查:**
```python
# 响应中包含usage信息
response = client.ChatCompletions(req)
print(response.Usage)
# InputTokens, OutputTokens
```
