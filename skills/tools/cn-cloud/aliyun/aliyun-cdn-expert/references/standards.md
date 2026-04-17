# Standards & Reference

## 7.1 Official Documentation

- [阿里云CDN控制台](https://cdn.console.aliyun.com)
- [CDN产品文档](https://help.aliyun.com/zh/cdn)
- [CDN API文档](https://help.aliyun.com/zh/cdn/developer-reference/api-summary)
- [HTTPS配置指南](https://help.aliyun.com/zh/cdn/user-guide/configure-https)
- [CDN最佳实践](https://help.aliyun.com/zh/cdn/best-practices)

## 7.2 Core Concepts

### 7.2.1 计费说明

| 计费项 | 价格(中国内地) | 说明 |
|--------|---------------|------|
| 基础服务费 | ¥0.036/GB | 流量计费 |
| 峰值带宽 | ¥0.54/Mbps/日 | 月95计费 |
| HTTPS请求 | ¥0.05/万次 | 按量计费 |

### 7.2.2 加速区域

| 区域 | 价格系数 |
|------|---------|
| 中国内地 | 1.0x |
| 亚太 | 1.5x |
| 欧洲/北美 | 2.0x |
| 全球 | 3.0x |

## 7.3 CDN域名配置

### 7.3.1 添加加速域名

```
加速域名: assets.yourdomain.com
业务类型: 静态加速 / 下载加速 / 视频加速 / 全站加速
源站类型: OSS域名 / IP / 源站域名 / 函数计算域名
回源协议: HTTP / HTTPS / 协议回源
```

### 7.3.2 常用HTTP头配置

| 头字段 | 说明 | 示例值 |
|--------|------|--------|
| Cache-Control | 缓存控制指令 | max-age=31536000 |
| Expires | 过期时间 | Thu, 31 Dec 2037 23:59:59 GMT |
| Content-Type | 内容类型 | application/json |
| ETag | 资源版本标识 | "abc123" |

## 7.4 SDK Version Compatibility

| SDK | 状态 | 备注 |
|-----|------|------|
| Alibaba Cloud SDK for Python | 推荐 | 完整功能支持 |
| Alibaba Cloud SDK for Go | 推荐 | 高性能场景 |
| CDN OpenAPI | 支持 | 直接调用REST API |
