# Standards & Reference

## 7.1 Official Documentation

- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- [FFmpeg Wiki](https://trac.ffmpeg.org/wiki)
- [FFmpeg Filters](https://ffmpeg.org/ffmpeg-filters.html)
- [FFmpeg Codecs](https://ffmpeg.org/docs.html)
- [FFmpeg GitHub](https://github.com/FFmpeg/FFmpeg)

## 7.2 Common Commands

### Basic Transcoding

| Command | Description |
|---------|-------------|
| `ffmpeg -i input.mp4 output.avi` | Convert format |
| `ffmpeg -i input.mov -c:v libx264 -crf 23 output.mp4` | H.264 encoding |
| `ffmpeg -i input.mp4 -vn -c:a copy output.aac` | Extract audio |
| `ffmpeg -i input.webm -c:v libvpx output.mp4` | VP8/VP9 to H.264 |

### Video Processing

```bash
# Resize video
ffmpeg -i input.mp4 -vf scale=1280:720 output.mp4

# Change framerate
ffmpeg -i input.mp4 -r 30 output.mp4

# Trim video
ffmpeg -i input.mp4 -ss 00:00:10 -t 00:00:30 output.mp4

# Extract frame at timestamp
ffmpeg -i input.mp4 -ss 00:00:05 -frames:v 1 output.jpg
```

### Audio Processing

```bash
# Convert audio
ffmpeg -i input.wav -c:a libmp3lame -b:a 192k output.mp3

# Mix audio
ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac output.mp4

# Normalize audio
ffmpeg -i input.wav -af loudnorm output.wav
```

## 7.3 Encoding Presets

| Preset | Speed | Quality | Use Case |
|---------|-------|---------|----------|
| `ultrafast` | Fastest | Lowest | Live streaming |
| `medium` | Default | Good | General purpose |
| `slow` | Slow | Best | Archival |
| `veryslow` | Slowest | Highest | Maximum quality |

## 7.4 Codec Parameters

| Codec | Option | Values | Description |
|-------|--------|--------|-------------|
| H.264 | `-crf` | 0-51 | Quality (lower=better) |
| H.264 | `-preset` | ultrafast-slow | Speed/quality tradeoff |
| H.265 | `-crf` | 0-51 | Quality (lower=better) |
| VP9 | `-crf` | 0-63 | Quality |
| AAC | `-b:a` | bitrate | Audio bitrate |

## 7.5 Version Reference

| FFmpeg Version | Release | Notes |
|---------------|---------|-------|
| 7.x | Current | Latest stable |
| 6.x | Supported | Legacy |
| 5.x | Security | Legacy |
| 4.x | EOL | Old |

## 7.6 Filters Reference

| Filter | Description |
|--------|-------------|
| `scale` | Resize video |
| `crop` | Crop video |
| `overlay` | Overlay video/image |
| `fade` | Fade in/out |
| `trim` | Trim by time |
| `setpts` | Change timestamps |
| `volume` | Adjust volume |
| `normalize` | Audio normalization |
