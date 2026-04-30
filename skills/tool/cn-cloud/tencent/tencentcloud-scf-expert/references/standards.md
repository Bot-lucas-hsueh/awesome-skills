# Standards & Reference

## 7.1 Official Documentation

- [腾讯云云函数SCF](https://cloud.tencent.com/product/scf)
- [SCF开发指南](https://cloud.tencent.com/document/product/583)
- [触发器概述](https://cloud.tencent.com/document/product/583/9804)
- [SCF定价](https://cloud.tencent.com/document/product/583/12281)

## 7.2 函数配置

### 7.2.1 运行环境

| 运行时 | 版本 | 超时限制 | 内存范围 |
|--------|------|---------|---------|
| Node.js | 18/16/14/12 | 900秒 | 64-3072MB |
| Python | 3.11/3.10/3.9/3.8/3.7 | 900秒 | 64-3072MB |
| PHP | 8.2/8.0/7.4 | 900秒 | 64-1536MB |
| Go | 1.x | 900秒 | 64-3072MB |
| Java | 11/8 | 900秒 | 256-3072MB |

### 7.2.2 计费维度

| 计费项 | 价格 | 说明 |
|--------|------|------|
| 调用次数 | ¥0.0133/万次 | 函数被触发次数 |
| 费用金额 | ¥0.00001667/GB-秒 | 执行时长×内存 |
| 公网流量 | ¥0.50/GB | 出方向流量 |

### 7.2.3 免费额度

| 项目 | 额度 | 有效期 |
|------|------|--------|
| 调用次数 | 10万次/月 | 每月重置 |
| 资源使用量 | 40万GB-秒/月 | 每月重置 |
| 公网流量 | 1GB/月 | 每月重置 |

## 7.3 触发器

### 7.3.1 触发器类型

| 触发器 | 事件 | 场景 |
|--------|------|------|
| API网关触发器 | HTTP请求 | Web API |
| COS触发器 | 文件上传/删除 | 文件处理 |
| CKafka触发器 | 消息到达 | 消息消费 |
| 定时触发器 | Cron表达式 | 定时任务 |
| CMQ触发器 | 队列消息 | 异步处理 |
| COS联合cos Trigger | 对象事件 | 事件驱动 |

### 7.3.2 API网关配置

```
默认公网URL: https://service-xxxxxx.gz.apigw.tencentcs.com/release/{functionName}
内网VPC URL: https://service-xxxxxx.internal.tencentcs.com/{functionName}
```

## 7.4 函数开发

### 7.4.1 Python入口

```python
# -*- coding: utf-8 -*-
import json

def main_handler(event, context):
    print('Received event:', json.dumps(event))
    
    # 获取请求参数
    if 'requestContext' in event:
        path = event['path']
        method = event['httpMethod']
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Hello SCF'})
    }
```

### 7.4.2 Node.js入口

```javascript
exports.main_handler = async (event, context) => {
    console.log(JSON.stringify(event))
    
    return {
        statusCode: 200,
        body: JSON.stringify({ message: 'Hello SCF' })
    }
}
```

## 7.5 冷启动优化

| 优化策略 | 说明 |
|---------|------|
| 预置并发 | 提前启动实例，避免冷启动 |
| 精简代码包 | 减少依赖，缩短加载时间 |
| 合理内存 | 内存越大启动越快，按需选择 |
| 层( Layers) | 共享依赖，减少单函数大小 |
