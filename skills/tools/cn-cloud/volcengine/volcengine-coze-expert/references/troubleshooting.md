# Troubleshooting

## 8.1 Bot发布问题

### 8.1.1 Bot无法发布到平台

**排查步骤:**
1. 确认该平台已通过认证
2. 检查Bot内容是否合规
3. 验证API Token是否正确

**常见原因:**
- 微信发布: 需要企业认证
- 飞书发布: 需要机器人在飞书开放平台创建

### 8.1.2 API调用返回空

**排查:**
```python
# 检查响应
response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
print(response.text)
```

**确认:**
- Bot已发布(草稿状态API不可调用)
- API Token正确
- 参数格式正确

## 8.2 知识库问题

### 8.2.1 召回不准确

**解决方案:**
- 重新上传文档，确保格式正确
- 调整召回参数(top_k)
- 在Bot提示词中强调使用知识库

### 8.2.2 文档解析失败

**支持格式:** TXT, PDF, DOCX, HTML, Markdown

**不支持:** 扫描件PDF、图片型文档

## 8.3 插件问题

### 8.3.1 插件调用失败

**排查:**
1. 确认插件已启用
2. 检查插件参数配置
3. 查看插件日志

**常见问题:**
- API密钥未配置
- 插件权限不足
- 请求超时
