# Standards & Reference

## 7.1 Official Documentation

- [函数计算FC控制台](https://fc.console.aliyun.com)
- [FC开发指南](https://help.aliyun.com/zh/function-compute)
- [触发器概述](https://help.aliyun.com/zh/function-compute/user-guide/trigger-overview)
- [函数计算定价](https://help.aliyun.com/zh/function-compute/billing/overview)

## 7.2 函数配置标准

### 7.2.1 运行环境

| 运行时 | 版本 | 内存限制 | 超时限制 |
|--------|------|---------|---------|
| Node.js | 18/16/14 | 128M-3G | 600秒 |
| Python | 3.11/3.10/3.9 | 128M-3G | 600秒 |
| PHP | 8.2/8.1/7.4 | 128M-3G | 600秒 |
| Java | 17/11/8 | 512M-3G | 600秒 |
| Go | 1.x | 128M-3G | 600秒 |
| Custom Runtime | 自定义 | 256M-3G | 600秒 |

### 7.2.2 计费维度

| 计费项 | 说明 | 价格 |
|--------|------|------|
| 调用次数 | 函数被触发执行的次数 | ¥0.0133/万次 |
| 执行时长 | 实际运行时间 | ¥0.000111.../GB-秒 |
| 公网流量 | 出方向流量 | ¥0.50/GB |

## 7.3 触发器配置

### 7.3.1 触发器类型

| 触发器 | 事件类型 | 适用场景 |
|--------|---------|---------|
| HTTP触发器 | HTTP请求 | API服务、Webhook |
| OSS触发器 | PutObject/GetObject等 | 文件处理、图片压缩 |
| CDN触发器 | 日志/刷新事件 | 日志分析 |
| 定时触发器 | Cron表达式 | 定时任务 |
| API网关 | HTTP请求 | API暴露 |
| MNS触发器 | 消息队列 | 异步处理 |

### 7.3.2 HTTP触发器路径

```
默认公网访问: https://{service}.{region}.fcapp.run/{functionName}
VPC内网访问: https://{service}.{region}.fcapp.run/{functionName}?token=xxx
```

## 7.4 函数代码规范

### 7.4.1 函数入口格式

```python
# Python handler格式
def handler(event, context):
    # event: 触发事件数据
    # context: 运行时上下文
    return {'statusCode': 200, 'body': 'Hello'}
```

```javascript
// Node.js handler格式
module.exports.handler = async (event, context) => {
    return { statusCode: 200, body: 'Hello' };
};
```

## 7.5 冷启动优化

| 优化策略 | 说明 |
|---------|------|
| 预置并发 | 提前启动实例，避免冷启动 |
| 精简依赖 | 减少镜像大小，缩短加载时间 |
| 轻量框架 | 使用FastAPI替代Django |
| HTTP复用 | 配置HTTP连接池 |
