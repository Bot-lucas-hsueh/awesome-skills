# Standards & Reference

## 7.1 Official Documentation

- [腾讯云直播CSS](https://cloud.tencent.com/product/css)
- [直播文档](https://cloud.tencent.com/document/product/267)
- [推流简介](https://cloud.tencent.com/document/product/267/7966)
- [播放简介](https://cloud.tencent.com/document/product/267/7967)

## 7.2 核心概念

### 7.2.1 推流地址

```
rtmp://推流域名/live/{流名称}?签名参数
```

### 7.2.2 播放地址

| 协议 | 格式 | 适用场景 |
|------|------|---------|
| RTMP | rtmp://域名/live/stream | 延迟低(~3秒)，需FFmpeg播放 |
| FLV | http://域名/live/stream.flv | 广泛支持，延迟~3秒 |
| HLS | http://域名/live/stream.m3u8 | Safari/iOS原生支持，延迟5-10秒 |

### 7.2.3 计费

| 计费项 | 价格 | 说明 |
|--------|------|------|
| 直播流量 | ¥0.21/GB | 下行播放流量 |
| 峰值带宽 | ¥0.54/Mbps/日 | 月95峰值带宽计费 |
| 推流费用 | 免费 | 中国大陆 |
| 录制存储 | ¥0.004/GB/日 | 按录制文件大小 |

## 7.3 OBS推流配置

```
推流服务器: rtmp://域名/live
推流密钥: 流的唯一标识(流名称)
编码设置:
  - 视频编码: H.264
  - 音频编码: AAC
  - 输出分辨率: 1920x1080
  - 视频码率: 2500-4000 kbps
  - 音频码率: 128 kbps
```

## 7.4 直播转码

### 7.4.1 转码模板

| 模板 | 分辨率 | 码率 | 适用场景 |
|------|--------|------|---------|
| 流畅 | 320x240 | 400kbps | 移动端低带宽 |
| 标清 | 854x480 | 1000kbps | 一般质量 |
| 高清 | 1920x1080 | 2500kbps | 高清播放 |
| 2K | 2560x1440 | 5000kbps | 高端设备 |

### 7.4.2 直播录制

```
录制格式: HLS/MP4
存储位置: COS对象存储
录制规则: 按时长(30-120分钟分片)或按时打断开录制
```

## 7.5 防盗链配置

| 类型 | 配置 | 说明 |
|------|------|------|
| URL防盗链 | 允许Referer列表 | 基于HTTP Referer |
| 鉴权 | Key+过期时间 | 更安全，推荐 |

```
防盗链播放URL格式:
http://domain/live/stream.flv?txSecret=md5(key+stream+expire)&txTime=expire
```
