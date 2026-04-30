# Standards & Reference

## 7.1 Official Documentation

- [扣子Coze平台](https://www.coze.cn)
- [扣子文档](https://www.coze.cn/docs)
- [Bot发布](https://www.coze.cn/docs/guides/publish/bot/publish_bot)
- [扣子API](https://www.coze.cn/docs/guides/overview)

## 7.2 核心概念

### 7.2.1 Bot配置

| 组件 | 说明 | 必填 |
|------|------|------|
| 名称 | Bot名称 | 是 |
| 描述 | Bot功能说明 | 是 |
| 提示词 | AI角色设定 | 是 |
| 开场白 | 首次对话欢迎语 | 否 |
| 开场白预置问题 | 快捷问题 | 否 |

### 7.2.2 技能类型

| 技能 | 说明 | 调用方式 |
|------|------|---------|
| 插件 | 调用外部API | 自动调用/用户触发 |
| 工作流 | 编排流程 | 自动执行 |
| 知识库 | 文档检索 | RAG召回 |
| 变量 | 存储状态 | 跨对话保持 |

### 7.2.3 知识库配置

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| 分段方式 | 智能/自定义 | 智能分段 |
| 分段长度 | 单段字符数 | 500-800 |
| 向量模型 | 嵌入模型 | text-embedding-v2 |

## 7.3 工作流节点

| 节点类型 | 用途 |
|---------|------|
| 大模型 | LLM对话/处理 |
| 代码 | 执行Python/JS代码 |
| 插件 | 调用插件 |
| 知识检索 | RAG召回 |
| 条件分支 | 逻辑判断 |
| 循环 | 循环执行 |
| 结束 | 输出结果 |

## 7.4 发布渠道

| 渠道 | 说明 | 配置 |
|------|------|------|
| 豆包 | 字节AI产品 | 自动同步 |
| 飞书 | 企业IM | 机器人应用 |
| 微信 | 企业微信 | 需企业认证 |
| 网站 | Web嵌入 | iframe嵌入 |
| API | REST API | API调用Bot |

## 7.5 API调用

```python
import requests

url = "https://api.coze.com/v1/chat"

headers = {
    "Authorization": "Bearer pat-xxxxx",
    "Content-Type": "application/json"
}

payload = {
    "bot_id": "7xxxxx",
    "user_id": "user_123",
    "stream": False,
    "messages": [
        {
            "role": "user",
            "content": "你好，请介绍一下自己"
        }
    ]
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```
