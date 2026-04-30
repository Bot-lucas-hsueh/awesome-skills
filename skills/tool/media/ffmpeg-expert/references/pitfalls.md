# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Prevention |
|---|---------|----------|------------|
| 1 | Wrong pixel format | 🔴 High | Use `-pix_fmt yuv420p` |
| 2 | Missing audio codec | 🔴 High | Specify with `-c:a` |
| 3 | Excessive quality | 🟡 Medium | Use CRF 23-28 for web |
| 4 | No faststart | 🟡 Medium | Add `-movflags +faststart` |
| 5 | Wrong framerate | 🟡 Medium | Match source or specify |
| 6 | Not checking input | 🔴 High | Always `ffmpeg -i input` first |

## 10.2 Anti-Patterns

### Quality Settings

```bash
# BAD: Overly large file
ffmpeg -i input.mp4 -crf 18 output.mp4  # Too high quality

# GOOD: Web-optimized
ffmpeg -i input.mp4 -crf 23 -preset medium output.mp4

# BAD: Missing audio
ffmpeg -i input.mp4 -c:v copy output.mp4  # May lose audio

# GOOD: Explicit audio
ffmpeg -i input.mp4 -c:v copy -c:a aac output.mp4
```

### Input/Output Order

```bash
# BAD: Options after input
ffmpeg input.mp4 -i output.avi  # Wrong order

# GOOD: Input first
ffmpeg -i input.mp4 output.avi
```

## 10.3 Codec Compatibility

| Codec | Browser Support | Notes |
|-------|---------------|-------|
| H.264 | All | Universal support |
| H.265 | Limited | Safari only |
| VP8 | Most | WebM fallback |
| VP9 | Most | Better compression |
| AV1 | Growing | Best compression |

## 10.4 Best Practices

```
Encoding:
□ Use H.264 for compatibility
□ CRF 23-28 for web delivery
□ CRF 18-22 for archival
□ Use yuv420p pixel format

Performance:
□ Use hardware acceleration when available
□ Choose appropriate preset
□ Parallel encoding with x265
□ Batch process with scripts

Quality:
□ Check PSNR/SSIM metrics
□ Test on target devices
□ Use two-pass for CBR
□ Include faststart for web
```
