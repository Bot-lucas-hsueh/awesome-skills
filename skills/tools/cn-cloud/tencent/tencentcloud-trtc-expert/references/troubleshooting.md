# Troubleshooting

## 8.1 通话质量问题

### 8.1.1 视频卡顿

**排查步骤:**
1. 检查网络带宽是否足够
2. 确认客户端性能
3. 检查是否有防火墙阻断

**解决方案:**
```javascript
// 降低视频质量
const localStream = TRTC.createStream({
    userId: userId,
    video: true,
    audio: true,
    videoEncParams: {
        resolution: TRTC.TRTCVideoResolution.TRTCVideoResolution640x360,
        bitrate: 800,
        fps: 15
    }
});
```

### 8.1.2 音频回声

**解决方案:**
- 确保使用TRTC SDK的音频处理(内置AEC)
- 避免使用外放+麦克风同时开启
- 使用耳机

## 8.2 接入问题

### 8.2.1 无法进入房间

**排查:**
1. 检查sdkAppId是否正确
2. 确认userId唯一性
3. 验证UserSig有效性

```javascript
// 检查UserSig是否过期
// UserSig有效期通常1-24小时
```

### 8.2.2 SDK导入失败

**解决方案:**
```bash
# Flutter
flutter pub add tencent_trtc_cloud

# iOS (Podfile)
pod 'TXLiteAVSDK_TRTC'

# Android (build.gradle)
implementation 'com.tencent.liteav:TXLiteAVSDK_TRTC:latest'
```

## 8.3 计费问题

### 8.3.1 费用超出预期

**原因:** 未开启旁路推流却产生了费用

**解决方案:**
- TRTC默认按分钟计费(语音通话分钟数)
- 视频通话按分钟+分辨率计费
- 使用云端混流减少拉流数
