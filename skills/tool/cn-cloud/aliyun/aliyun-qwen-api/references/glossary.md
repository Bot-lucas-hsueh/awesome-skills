# Glossary

## 9.1 模型术语

| 术语 | 定义 |
|------|------|
| Token | 模型处理的最小文本单位 |
| Prompt | 输入提示词，引导模型生成 |
| System Prompt | 系统指令，设定AI角色和行为 |
| Temperature | 控制生成随机性的参数(0-2) |
| Top-p | 核采样，控制候选词范围(0-1) |
| Max Tokens | 生成内容的最大Token数 |

## 9.2 API术语

| 术语 | 定义 |
|------|------|
| API-KEY | 调用API的密钥凭证 |
| base_url | API服务接入地址 |
| Chat Completion | 对话补全接口 |
| Embedding | 文本向量化接口 |
| Streaming | 流式输出，边生成边返回 |

## 9.3 消息术语

| 术语 | 定义 |
|------|------|
| message | 对话消息对象 |
| role | 消息角色(system/user/assistant) |
| content | 消息内容 |
| function | 函数调用定义 |
| tool_calls | 函数调用请求 |

## 9.4 计费术语

| 术语 | 定义 |
|------|------|
| 输入Token | 用户提问和对话历史的Token数 |
| 输出Token | 模型生成回复的Token数 |
| 上下文Token | 一次请求中所有messages的总Token数 |
| RPM | Requests Per Minute，每分钟请求数 |
| TPM | Tokens Per Minute，每分钟Token数 |
