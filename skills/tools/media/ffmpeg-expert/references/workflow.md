# Standard Workflow

## 8.1 Video Transcoding Workflow

```
Phase 1: Analyze
├── Get input info: ffmpeg -i input.mp4
├── Check resolution, codec, duration
├── Identify audio/video streams
└── Note target format requirements

Phase 2: Convert
├── Select appropriate codec
├── Set quality parameters
├── Configure audio
└── Add metadata if needed

Phase 3: Verify
├── Check output file
├── Verify duration matches
├── Test playback
└── Check file size
```

## 8.2 Common Transcoding

```bash
# H.264 to WebM
ffmpeg -i input.mp4 -c:v libvpx-vp9 -crf 30 -b:v 0 output.webm

# H.264 to H.265
ffmpeg -i input.mp4 -c:v libx265 -crf 28 -preset medium output.mp4

# Extract and convert audio
ffmpeg -i input.mp4 -vn -c:a libopus -b:a 128k output.opus

# Concatenate videos
ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4
```

## 8.3 Streaming Workflow

```bash
# HLS encoding
ffmpeg -i input.mp4 \
  -c:v libx264 -c:a aac \
  -f hls -hls_time 4 \
  -hls_playlist_type vod \
  -hls_segment_filename 'segment_%03d.ts' \
  output.m3u8

# DASH encoding
ffmpeg -i input.mp4 \
  -c:v libx264 -c:a aac \
  -f dash -dash_segment_type mp4 \
  -init_seg_name 'init_$RepresentationID$.mp4' \
  -media_seg_name 'chunk_$RepresentationID$ _$Bandwidth$_$Time$.m4s' \
  output.mpd
```

## 8.4 Batch Processing

```bash
#!/bin/bash
for file in *.mp4; do
  ffmpeg -i "$file" \
    -c:v libx264 -crf 23 -preset medium \
    -c:a copy \
    "converted/${file%.mp4}_720p.mp4"
done

# With parallel processing
find . -name "*.mp4" -exec ffmpeg -i {} -c:v libx264 -crf 23 {}_output.mp4 \;
```

## 8.5 Quality Testing

```bash
# Check video quality metrics
ffmpeg -i input.mp4 -vf "ssim=output.ssim" -f null -

# Check PSNR
ffmpeg -i input.mp4 -i reference.mp4 -lavfi psnr="output.psnr" -f null -

# Generate thumbnail
ffmpeg -i input.mp4 -ss 00:00:05 -vframes 1 -q:v 2 thumb.jpg
```
