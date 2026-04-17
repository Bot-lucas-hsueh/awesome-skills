# Standards & Reference

## 7.1 Official Documentation

- [腾讯云VOD控制台](https://console.cloud.tencent.com/vod)
- [VOD产品文档](https://cloud.tencent.com/document/product/266)
- [超级播放器](https://cloud.tencent.com/document/product/266/7838)
- [VOD定价](https://cloud.tencent.com/document/product/266/32201)

## 7.2 核心功能

### 7.2.1 视频上传

| 方式 | 说明 | 适用场景 |
|------|------|---------|
| 控制台上传 | 手动上传 | 临时/小文件 |
| 服务端上传 | API/SDK上传 | 批量/自动化 |
| 客户端上传 | 移动端SDK | 用户生成内容 |
| URL拉取 | 从其他地址拉取 | 已存储在其他地方 |

### 7.2.2 转码模板

| 模板 | 分辨率 | 码率 | 格式 | 适用 |
|------|--------|------|------|------|
| 流畅 | 544x306 | 400kbps | HLS/MP4 | 低带宽 |
| 标清 | 854x480 | 1000kbps | HLS/MP4 | 一般设备 |
| 高清 | 1920x1080 | 2500kbps | HLS/MP4 | 高清设备 |
| 2K | 2560x1440 | 5000kbps | HLS/MP4 | 高端设备 |
| 4K | 3840x2160 | 8000kbps | HLS/MP4 | 超高清 |

### 7.2.3 计费

| 计费项 | 价格 | 说明 |
|--------|------|------|
| 存储 | ¥0.004/GB/日 | 按存储量计费 |
| 流量 | ¥0.21/GB | 播放下行流量 |
| 转码 | ¥0.0325/分钟 | 按输出时长 |
| 截图 | ¥0.05/千次 | 智能封面 |

## 7.3 上传SDK

### 7.3.1 Python服务端上传

```bash
pip install vod-sdk-python
```

```python
from vod.vod_upload import VodUploadClient

client = VodUploadClient("SecretId", "SecretKey")

# 上传本地文件
upload_result = client.upload("ap-guangzhou", "video.mp4")

# 上传结果
print(upload_result['FileId'])
print(upload_result['MediaUrl'])
```

### 7.3.2 客户端上传签名

```python
import hashlib
import time

def generate_upload_sign(app_id, user_id, secret_key):
    # 生成客户端上传签名
    current = int(time.time())
    expire = current + 3600  # 1小时后过期
    
    original = f"appId={app_id}&userId={user_id}&time={expire}"
    signature = hashlib.sha256((original + secret_key).encode()).hexdigest()
    
    return {
        "signature": signature,
        "expireTime": expire
    }
```

## 7.4 超级播放器配置

### 7.4.1 Web播放器

```html
<div id="player-container"></div>
<script src="playerjs/vod-sdk.min.js"></script>
<script>
    new TcPlayer('player-container', {
        appID: 'your_app_id',
        fileID: 'your_file_id',
        width: '640px',
        height: '360px',
        autoplay: false,
        controls: 'always',
        logo: 'logo.png'
    });
</script>
```

## 7.5 防盗链

| 类型 | 配置 | 说明 |
|------|------|------|
| Key防盗链 | key+过期时间 | 推荐使用 |
| Referer防盗链 | 允许列表 | 基于HTTP Referer |
| IP黑白名单 | IP过滤 | 特殊场景 |

```
防盗链URL格式:
http://域名/{FileId}?vinfo=1&clip=1&hash=md5(key+timestamp)&t=timestamp
```
