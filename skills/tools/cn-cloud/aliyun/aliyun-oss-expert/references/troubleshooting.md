# Troubleshooting

## 8.1 上传下载问题

### 8.1.1 上传失败

**常见原因:**
- AccessKey权限不足
- Bucket名称错误
- 网络连接问题
- 文件大小超限(单文件最大5GB)

**排查步骤:**
```python
import oss2

auth = oss2.Auth('<AccessKeyId>', '<AccessKeySecret>')
bucket = oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'my-bucket')

# 验证连接
try:
    bucket.get_bucket_info()
    print("连接成功")
except oss2.exceptions.NoSuchBucket:
    print("Bucket不存在")
except oss2.exceptions.RequestError as e:
    print(f"请求错误: {e}")
```

**解决方案:**
- 检查AK是否有效，是否有oss:PutObject权限
- 确认Endpoint与Bucket区域匹配
- 大文件使用断点续传

### 8.1.2 下载的URL过期

**症状:** 签名URL返回403 Forbidden

**排查:**
```python
# 签名URL有效期是否已过
url = bucket.sign_url('GET', 'file.txt', 3600)  # 1小时有效期
print(url)
```

**解决方案:**
- 增加签名URL的有效期
- 私有文件使用更长的有效期
- 考虑使用STS临时凭证

## 8.2 权限问题

### 8.2.1 防盗链无效

**症状:** 其他网站直接引用了OSS资源

**排查步骤:**
1. 确认防盗链已配置
2. 检查Referer是否为空

**解决方案:**
```python
# 设置防盗链
from oss2.models import BucketReferer

# 允许yourdomain.com及其子域名访问
bucket.put_bucket_referer(BucketReferer(
    referers=['https://yourdomain.com', 'https://*.yourdomain.com'],
    allow_empty_referer=False
))
```

### 8.2.2 跨域(CORS)错误

**症状:** 浏览器报"No 'Access-Control-Allow-Origin' header"

**解决方案:**
```python
from oss2.models import BucketCors

rule = CorsRule(
    allowed_origins=['https://yourdomain.com'],
    allowed_methods=['GET', 'POST', 'PUT'],
    allowed_headers=['*'],
    max_age_seconds=3600
)

bucket.put_bucket_cors(BucketCors([rule]))
```

## 8.3 性能问题

### 8.3.1 下载速度慢

**解决方案:**
- 使用CDN加速OSS
- 使用内网Endpoint(同一VPC内)
- 分片上传大文件

```python
# 分片上传(适合大文件)
import oss2

bucket.init_multipart_upload('large_file.zip')

# 分片上传
# bucket.upload_part(...)
```

## 8.4 费用问题

### 8.4.1 存储费用异常

**常见原因:**
- 大量低频访问文件使用了标准存储
- 未设置生命周期规则

**解决方案:**
- 设置生命周期规则，自动转换存储类型
```python
from oss2.models import LifecycleRule, Transition

rule = LifecycleRule(
    rule_id='convert_to_ia',
    prefix='logs/',
    status='Enabled',
    transitions=[Transition(days=30, storage_class=oss2.BUCKET_STORAGE_CLASS_IA)]
)
bucket.put_bucket_lifecycle([rule])
```
