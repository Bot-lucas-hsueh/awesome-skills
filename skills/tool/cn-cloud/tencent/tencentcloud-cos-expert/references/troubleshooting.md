# Troubleshooting

## 8.1 上传下载问题

### 8.1.1 上传失败

**常见原因:**
- SecretId/SecretKey配置错误
- Bucket名称不正确(需包含appid)
- 权限不足
- 文件名包含特殊字符

**解决方案:**
```python
from qcloud_cos import CosConfig, CosS3Client

config = CosConfig(
    SecretId='your-secret-id',
    SecretKey='your-secret-key',
    Region='ap-beijing',
    Token=None
)
client = CosS3Client(config)

# 验证连接
try:
    client.list_buckets()
    print("连接成功")
except CosServiceError as e:
    print(f"错误: {e.get_error_code()}")
    print(f"信息: {e.get_error_msg()}")
```

### 8.1.2 下载URL失效

**原因:** 签名URL过期或权限问题

**解决方案:**
```python
# 生成新的预签名URL
url = client.generate_pre_signed_url(
    Bucket='mybucket-1234567890',
    Key='file.txt',
    Expired=3600  # 1小时有效期
)
print(url)
```

## 8.2 权限问题

### 8.2.1 跨域错误

**症状:** 浏览器报CORS错误

**解决方案:**
```python
from qcloud_cos import CosConfig
from qcloud_cos.cos_cos_xml import CosXml

# 配置CORS
config = CosConfig(...)
cos_xml = CosXml(config)

# 设置CORS规则
response = cos_xml.put_bucket_cors(
    Bucket='mybucket-1234567890',
    CORSConfiguration={
        'CORSRule': [
            {
                'AllowedOrigin': ['https://yourdomain.com'],
                'AllowedMethod': ['GET', 'POST', 'PUT'],
                'AllowedHeader': ['*'],
                'ExposeHeader': ['ETag'],
                'MaxAgeSeconds': 3600
            }
        ]
    }
)
```

### 8.2.2 防盗链无效

**排查:**
1. 确认防盗链配置已生效
2. 检查Referer是否在白名单

```python
# 查询防盗链配置
response = cos_xml.get_bucket_referer(Bucket='mybucket-1234567890')
```

## 8.3 费用问题

### 8.3.1 存储费用异常

**原因:** 大量小文件(每个文件都会产生存储请求费用)

**解决方案:**
- 合并小文件
- 使用生命周期规则归档冷数据
- 使用智能分层存储
