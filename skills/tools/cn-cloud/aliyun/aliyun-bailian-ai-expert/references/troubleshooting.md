# Troubleshooting

## 8.1 知识库常见问题

### 8.1.1 知识库检索不到相关内容

**症状:** 用户提问时，RAG返回"未找到相关信息"

**排查步骤:**
1. 检查文档是否已成功上传并完成解析
2. 验证chunk_size是否过大/过小
3. 检查embedding模型是否与知识库匹配
4. 查看知识库召回日志确认top_k设置

**解决方案:**
- 调整chunk_size至500-800字符
- 降低top_k阈值至3-5
- 重新上传文档确保格式正确(支持PDF/TXT/DOCX/HTML)
- 在控制台预览知识库召回结果

### 8.1.2 文档解析失败

**症状:** 上传PDF后显示"解析失败"

**常见原因:**
- PDF扫描件(无文字层)无法解析
- 文件超过100MB限制
- 文档格式损坏

**解决方案:**
- 将扫描PDF转为可搜索PDF
- 分割大文件为多个小文件
- 转换为TXT/DOCX格式重试

### 8.1.3 回复内容不准确/幻觉

**症状:** 模型生成了知识库中没有的内容

**排查步骤:**
1. 检查system prompt中是否限制了知识库范围
2. 验证召回的文档片段是否与问题相关
3. 查看temperature参数是否过高

**解决方案:**
```json
{
  "temperature": 0.3,
  "system": "你是一个客服助手，只根据提供的知识库内容回答，不要编造信息。"
}
```

## 8.2 API调用问题

### 8.2.1 403 Forbidden错误

**原因:** API-KEY无效或权限不足

**解决方案:**
```bash
# 检查API-KEY是否正确设置
export DASHSCOPE_API_KEY="sk-xxxxxxxx"

# 确认API-KEY已在百炼平台开通对应服务
# 访问: https://bailian.console.aliyun.com -> API-KEY管理
```

### 8.2.2 429 Rate Limit错误

**原因:** 请求频率超出限制

**解决方案:**
- 免费用户: 60次/分钟
- 开通后: 500次/分钟
- 添加请求间隔或实现重试机制

### 8.2.3 Connection Timeout

**原因:** 网络问题或服务端繁忙

**解决方案:**
```python
from dashscope import Generation

response = Generation.call(
    model="qwen-plus",
    messages=[{"role": "user", "content": "你好"}],
    timeout=30,  # 设置超时
    request_timeout=60
)
```

## 8.3 百炼平台问题

### 8.3.1 应用发布后API无法调用

**排查:**
1. 确认应用已发布并生成API
2. 检查应用的QPS限制
3. 验证API-KEY是否属于该应用

### 8.3.2 计费异常

**常见原因:**
- 未设置usage限制
- 使用了高配额模型

**解决方案:**
- 在成本中心设置消费预警
- 使用qwen-turbo替代qwen-max做测试
