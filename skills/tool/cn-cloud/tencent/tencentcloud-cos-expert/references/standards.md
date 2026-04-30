# Standards & Reference

## 7.1 Official Documentation

- [腾讯云COS控制台](https://console.cloud.tencent.com/cos)
- [COS产品文档](https://cloud.tencent.com/document/product/436)
- [COS SDK文档](https://cloud.tencent.com/document/product/436/6474)
- [COS API文档](https://cloud.tencent.com/document/product/436/7751)

## 7.2 存储类型

### 7.2.1 存储级别

| 类型 | 适用场景 | 价格(GB/月) | 最低存储时间 |
|------|---------|------------|-------------|
| 标准存储 | 高频访问 | ¥0.118 | 无 |
| 低频存储 | 较低频(>30天) | ¥0.058 | 30天 |
| 归档存储 | 长期存档(>90天) | ¥0.033 | 90天 |
| 深度归档 | 超长期(>180天) | ¥0.013 | 180天 |

### 7.2.2 区域与Endpoint

| 区域 | 地域ID | 外网Endpoint | 内网Endpoint |
|------|--------|-------------|-------------|
| 北京一区 | ap-beijing-1 | cos.ap-beijing-1.myqcloud.com | cos-internal.ap-beijing-1.myqcloud.com |
| 北京 | ap-beijing | cos.ap-beijing.myqcloud.com | cos-internal.ap-beijing.myqcloud.com |
| 上海 | ap-shanghai | cos.ap-shanghai.myqcloud.com | cos-internal.ap-shanghai.myqcloud.com |
| 广州 | ap-guangzhou | cos.ap-guangzhou.myqcloud.com | cos-internal.ap-guangzhou.myqcloud.com |
| 新加坡 | ap-singapore | cos.ap-singapore.myqcloud.com | cos-internal.ap-singapore.myqcloud.com |

## 7.3 Bucket配置

### 7.3.1 访问权限

| 权限 | 说明 |
|------|------|
| 私有读写 | 仅授权用户可读写 |
| 公有读私有写 | 所有人可读，Owner可写 |
| 公有读写 | 不推荐 |
| 继承权限 | 子目录继承Bucket权限 |

### 7.3.2 CORS配置

```json
[
    {
        "allowedOrigin": "https://yourdomain.com",
        "allowedMethod": ["GET", "POST", "PUT"],
        "allowedHeader": ["*"],
        "maxAgeSeconds": 3600
    }
]
```

## 7.4 Python SDK

```bash
pip install cos-python-sdk-v5
```

```python
from qcloud_cos import CosConfig, CosS3Client

config = CosConfig(
    SecretId='AKIDxxxxxxxx',
    SecretKey='xxxxxxxx',
    Region='ap-beijing',
    Token=None
)
client = CosS3Client(config)

# 上传
client.put_object(Bucket='mybucket-1234567890', Body=b'content', Key='file.txt')

# 下载
response = client.get_object(Bucket='mybucket-1234567890', Key='file.txt')
response['Body'].get_stream_to_file('local.txt')

# 生成预签名URL(1小时有效期)
url = client.generate_pre_signed_url(
    Bucket='mybucket-1234567890',
    Key='file.txt',
    Expired=3600
)
```

## 7.5 生命周期规则

| 规则 | 前缀 | 操作 | 生效时间 |
|------|------|------|---------|
| 转低频 | logs/ | 转换存储类型 | 30天后 |
| 转归档 | backup/ | 转换存储类型 | 180天后 |
| 删除过期 | temp/ | 删除 | 365天后 |
