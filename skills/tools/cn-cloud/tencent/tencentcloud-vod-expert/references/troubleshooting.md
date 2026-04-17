# Troubleshooting

## 8.1 上传问题

### 8.1.1 上传失败

**排查:**
```python
# 检查上传凭证
from vod.vod_upload import VodUploadClient

client = VodUploadClient("SecretId", "SecretKey")

# 上传时查看错误信息
try:
    result = client.upload("ap-guangzhou", "video.mp4")
except VodUploadException as e:
    print(f"错误码: {e.code}")
    print(f"错误信息: {e.message}")
```

**常见错误:**
- 10010: 存储桶不存在
- 10011: 上传凭证过期
- 10012: 无上传权限

### 8.1.2 客户端上传失败

**原因:** 签名生成错误或存储权限未开

**解决方案:**
```python
# 服务端生成上传签名
import hashlib
import time

def generate_upload_sign(app_id, user_id, secret_key):
    current = int(time.time())
    expire = current + 3600
    original = f"appId={app_id}&userId={user_id}&time={expire}"
    signature = hashlib.sha256((original + secret_key).encode()).hexdigest()
    return {"signature": signature, "expireTime": expire}
```

## 8.2 转码问题

### 8.2.1 转码失败

**排查:**
1. 查看任务ID和错误信息
2. 检查原始视频格式是否支持

**支持格式:** MP4, AVI, MKV, MOV, FLV, WMV, WebM等

### 8.2.2 视频封面为空

**解决方案:**
- 开启自动截图或使用视频截图API
- 手动在控制台上传封面

## 8.3 播放问题

### 8.3.1 播放器无法加载

**排查:**
1. 确认fileId正确
2. 检查超级播放器配置
3. 确认防盗链URL未过期

```javascript
// 检查播放器初始化
var player = TCPlayer('player-container', {
    appID: 'your_app_id',
    fileID: 'your_file_id'
});

player.on('error', function(e) {
    console.log('播放器错误:', e);
});
```

## 8.4 防盗链问题

### 8.4.1 防盗链URL过期

**症状:** 播放器显示"播放地址已过期"

**解决方案:**
- 在服务端实时生成防盗链URL
- 增加防盗链URL的有效期
