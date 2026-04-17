# Standards & Reference

## 7.1 Official Documentation

- [OSS控制台](https://oss.console.aliyun.com)
- [OSS产品文档](https://help.aliyun.com/zh/oss)
- [OSS API文档](https://help.aliyun.com/zh/oss/developer-reference/api-summary)
- [SDK下载](https://help.aliyun.com/zh/oss/developer-reference/overview)

## 7.2 存储类型

### 7.2.1 存储类型对比

| 类型 | 适用场景 | 价格(GB/月) | 最小存储时间 |
|------|---------|------------|-------------|
| 标准存储 | 高频访问 | ¥0.12 | 无 |
| 低频访问 | 较低频率(>30天) | ¥0.08 | 30天 |
| 归档存储 | 长期存档(>90天) | ¥0.033 | 90天 |
| 冷归档存储 | 超长期存档(>180天) | ¥0.0075 | 180天 |

### 7.2.2 区域与Endpoint

| 区域 | 外网Endpoint | 内网Endpoint |
|------|-------------|-------------|
| 华东1(杭州) | oss-cn-hangzhou.aliyuncs.com | oss-cn-hangzhou-internal.aliyuncs.com |
| 华北2(北京) | oss-cn-beijing.aliyuncs.com | oss-cn-beijing-internal.aliyuncs.com |
| 亚太东南(新加坡) | oss-ap-southeast-1.aliyuncs.com | oss-ap-southeast-1-internal.aliyuncs.com |

## 7.3 Bucket配置

### 7.3.1 访问权限

| 权限 | 说明 | 适用场景 |
|------|------|---------|
| 私有 | 仅Owner可读写 | 存储敏感文件 |
| 公共读 | 所有人可读，Owner可写 | 静态网站/图片 |
| 公共读写 | 所有人可读写 | 不推荐 |

### 7.3.2 防盗链配置

```
Referer白名单: https://yourdomain.com
允许空Referer: 否
```

## 7.4 SDK使用

### 7.4.1 Python SDK

```bash
pip install oss2
```

```python
import oss2

auth = oss2.Auth('<AccessKeyId>', '<AccessKeySecret>')
bucket = oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'my-bucket')

# 上传
bucket.put_object('dir/file.txt', 'content')

# 下载
bucket.get_object_to_file('dir/file.txt', 'local.txt')

# 签名URL(私有读写)
url = bucket.sign_url('GET', 'dir/file.txt', 3600)
```

## 7.5 生命周期规则

| 规则 | 前缀/标签 | 目标存储 | 生效天数 |
|------|---------|---------|---------|
| 30天后转低频 | logs/ | 低频访问 | 30天 |
| 365天后转归档 | backup/ | 归档存储 | 365天 |
| 730天后删除 | temp/ | 删除 | 730天 |
