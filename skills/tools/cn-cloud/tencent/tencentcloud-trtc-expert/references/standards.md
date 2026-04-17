# Standards & Reference

## 7.1 Official Documentation

- [腾讯云实时音视频TRTC](https://cloud.tencent.com/product/trtc)
- [TRTC开发文档](https://cloud.tencent.com/document/product/647)
- [SDK下载](https://github.com/tencentyun/TRTCSDK)
- [TRTC定价](https://cloud.tencent.com/document/product/647/12283)

## 7.2 核心概念

### 7.2.1 房间与用户

| 概念 | 说明 |
|------|------|
| RoomId | 房间ID，用于区分不同房间 |
| UserId | 用户ID，用于标识参与者 |
| UserSig | 用户签名，用于身份验证 |

### 7.2.2 应用场景

| 场景 | 分辨率 | 帧率 | 码率 | 适用 |
|------|--------|------|------|------|
| 视频通话 | 640x360 | 15fps | 500kbps | 1v1/多人 |
| 互动直播 | 1280x720 | 15fps | 1500kbps | 直播连麦 |
| 语音通话 | - | - | 64kbps | 仅音频 |
| 屏幕分享 | 1920x1080 | 10fps | 1500kbps | 演示 |

## 7.3 SDK集成

### 7.3.1 Flutter

```yaml
# pubspec.yaml
dependencies:
  tencent_trtc_cloud: ^1.0.0
```

```dart
// 初始化
await TRTCCloud.sharedInstance();

// 进入房间
TRTCParams params = TRTCParams();
params.sdkAppId = sdkAppId;
params.userId = userId;
params.userSig = userSig;
params.roomId = roomId;

await TRTCCloud.sharedInstance().enterRoom(params, TRTCScene.TRTCSceneVideoCall);

// 开始推流
await TRTCCloud.sharedInstance().startLocalAudio(TRTCAudioQuality.music);
await TRTCCloud.sharedInstance().startLocalView(view: localView);
```

### 7.3.2 Web

```html
<script src="trtc.js"></script>
```

```javascript
const client = TRTC.createClient({
  sdkAppId: sdkAppId,
  userId: userId,
  userSig: userSig,
  mode: 'videoCall'
});

// 加入房间
await client.join({ roomId: roomId });

// 订阅远端用户
client.on('peer-join', (userId) => {
  console.log(`${userId} joined`);
});

// 创建本地流
const localStream = TRTC.createStream({ userId, audio: true, video: true });
await localStream.initialize();
await client.publish(localStream);
```

## 7.4 关键参数

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| videoEncParams.resolution | 视频分辨率 | 640x360 |
| videoEncParams.frameRate | 帧率 | 15fps |
| videoEncParams.videoBitrate | 视频码率 | 800kbps |
| audioEncParams.audioQuality | 音频质量 | high |
| autoSubscribe | 自动订阅远端流 | true |

## 7.5 房间销毁

```javascript
// 离开房间
await client.leave();

// 销毁本地流
localStream.close();
TRTCCloud.destroySharedInstance();
```
