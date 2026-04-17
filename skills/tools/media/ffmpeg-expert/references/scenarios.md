# Scenario Examples

## 9.1 Video Optimization for Web

**User:** "How do I optimize a video for web playback?"

**FFmpeg Expert:**
> **Web Optimization:**
>
> ```bash
> # H.264 with good quality
> ffmpeg -i input.mov \
>   -c:v libx264 \
>   -crf 23 \            # Quality (18-28 typical)
>   -preset medium \      # Encoding speed
>   -profile:v high \    # H.264 profile
>   -level 4.0 \         # Compatibility
>   -pix_fmt yuv420p \   # Color space
>   -c:a aac \
>   -b:a 128k \          # Audio bitrate
>   -movflags +faststart \  # Web optimization
>   output.mp4
>
> # Alternative: VP9 for better compression
> ffmpeg -i input.mov \
>   -c:v libvpx-vp9 \
>   -crf 30 \
>   -b:v 0 \            # Constant quality mode
>   -c:a libopus \
>   -b:a 128k \
>   output.webm
> ```

## 9.2 Thumbnail Generation

**User:** "How do I extract thumbnails from a video?"

**FFmpeg Expert:**
> **Thumbnail Extraction:**
>
> ```bash
> # Single frame at specific time
> ffmpeg -i video.mp4 -ss 00:00:05 -frames:v 1 thumb.jpg
>
> # Multiple frames at intervals
> ffmpeg -i video.mp4 \
>   -vf "fps=1,scale=320:-1" \
>   -q:v 2 \
>   thumbs_%03d.jpg
>
> # Sprite sheet for preview
> ffmpeg -i video.mp4 \
>   -vf "fps=1,scale=160:-1,tile=10x10" \
>   -frames:v 100 \
>   sprite.jpg
> ```

## 9.3 Screen Recording

**User:** "How do I record my screen?"

**FFmpeg Expert:**
> **Screen Capture:**
>
> ```bash
> # X11 (Linux)
> ffmpeg -f x11grab -framerate 30 \
>   -video_size 1920x1080 \
>   -i :0.0 \
>   -c:v libx264 -preset ultrafast \
>   screenrecording.mp4
>
> # macOS
> ffmpeg -f avfoundation -framerate 30 \
>   -i "CaptureScreen0:none" \
>   -c:v libx264 -preset ultrafast \
>   screenrecording.mp4
>
> # With audio (macOS)
> ffmpeg -f avfoundation -framerate 30 \
>   -i "CaptureScreen0:none+CaptureAudio1" \
>   -c:v libx264 -preset ultrafast \
>   -c:a aac \
>   screenrecording.mp4
>
> # Windows (GDIGrab)
> ffmpeg -f gdigrab -framerate 30 \
>   -i desktop \
>   -c:v libx264 -preset ultrafast \
>   screenrecording.mp4
> ```

## 9.4 Video Stabilization

**User:** "How do I stabilize shaky footage?"

**FFmpeg Expert:**
> **Stabilization:**
>
> ```bash
> # Two-pass stabilization
> ffmpeg -i shaky.mp4 -vf vidstabdetect=shakiness=10:accuracy=15 -f null -
> ffmpeg -i shaky.mp4 -vf vidstabtransform=smoothing=10:input=transforms.trf output.mp4
>
> # One-pass (less accurate but faster)
> ffmpeg -i shaky.mp4 -vf "deshake" output.mp4
> ```
