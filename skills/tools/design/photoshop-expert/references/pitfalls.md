# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Quick Fix |
|---|---------|----------|--------|-----------|
| 1 | **Wrong color mode for output** | 🔴 High | Colors shift, print looks wrong | Set to CMYK for print, sRGB for web before starting |
| 2 | **Insufficient resolution** | 🔴 High | Blurry/pixelated output | Check DPI: 300 for print, 72 minimum for web at 100% |
| 3 | **Saving as JPEG multiple times** | 🔴 High | Progressive quality loss | Keep PSD master, export JPEG as final step |
| 4 | **Ignoring color profile** | 🟡 Medium | Color inconsistency | Assign and convert to profile for output |
| 5 | **Non-square pixels (video)** | 🟡 Medium | Distorted graphics | Use Edit > Pixel Aspect Ratio > Square |
| 6 | **No bleed for print** | 🔴 High | White edges after trimming | Add 3mm bleed to all print documents |
| 7 | **Embedded vs. linked Smart Objects** | 🟡 Medium | Large file sizes, update issues | Prefer linked for shared assets, embedded for portability |
| 8 | **Rasterizing text prematurely** | 🟡 Medium | Can't edit text later | Keep text as vector type layers until final output |
| 9 | **Forgetting to outline fonts** | 🟡 Medium | Font substitution on different systems | Outlines or package fonts for handoff |
| 10 | **Not saving as Max Compatibility** | 🟡 Medium | Older PS versions can't read layers | Enable in Preferences > File Handling |

## 10.2 Performance Issues

### Large File Handling Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| **Slow zooming/paning** | Large zoomed-out view | Preferences > Performance > reduce cache levels |
| **Memory exhaustion** | Too many large layers | Flatten or merge unused layers, increase RAM allocation |
| **Scratch disk full** | Insufficient temp space | Preferences > Scratch Disks > use fastest drive |
| **Unable to complete operation** | Out of memory or scratch | Edit > Purge > All, close other apps, reduce document size |
| **Slow filter operations** | Filters not using GPU | Preferences > Performance > GPU Settings > Acceleration |

### GPU Acceleration Troubleshooting

| Issue | Solution |
|-------|----------|
| GPU not recognized | Update graphics drivers, check GPU in Preferences > Performance |
| Artifacts/glitches | Disable GPU acceleration for specific tools |
| Crash on startup | Reset preferences (hold Alt+Ctrl+Shift on launch) |
| Slow 3D features | Ensure GPU meets minimum requirements |

### Optimization Checklist

- [ ] Clear scratch disk space before large sessions
- [ ] Limit history states (50 is usually sufficient)
- [ ] Use 8-bit color for standard work (32-bit for HDR)
- [ ] Enable Auto-save with reasonable intervals (10-15 minutes)
- [ ] Close unused documents
- [ ] Use layer groups to organize (doesn't affect performance much)
- [ ] Avoid excessive layer styles on large images
- [ ] Flatten before applying heavy filters
- [ ] Use adjustment layers instead of destructive edits
- [ ] Purge memory regularly with Ctrl+Alt+Shift+X

## 10.3 File Size Issues

### Common Causes

| Cause | Impact | Solution |
|-------|--------|----------|
| Unoptimized PSD | Large file size | Save as Copy with Max Compatibility disabled for delivery |
| Embedded Smart Objects at full res | Massive file bloat | Use linked Smart Objects for large images |
| Excessive history log | Large PSD size | Limit history to 50 or fewer |
| Hidden layers with large content | Wasted storage | Delete hidden layers before final save |
| Layer styles on off-canvas elements | Unnecessary data | Crop or delete off-canvas content |

### File Size Quick Fixes

1. **Duplicate and flatten**: Image > Duplicate > Flatten Image
2. **Purge all**: Edit > Purge > All (frees memory, doesn't change file)
3. **Reduce history**: Edit > Purge > History
4. **Save as copy**: File > Save a Copy, optimize settings
5. **Clean up temp files**: Preferences > Scratch Disks > Purge Scratch on Quit

## 10.4 Compatibility Issues

| Issue | Prevention | Fix |
|-------|-----------|-----|
| **Mac/Windows file path differences** | Avoid special characters in filenames | Rename files, avoid non-ASCII characters |
| **Missing fonts** | Package fonts or outline before handoff | Install fonts, or convert text to outlines |
| **Missing linked files** | Use File > Package to collect all links | Relink or embed missing assets |
| **Smart Object version mismatch** | Use compatible versions when possible | Update or re-create Smart Objects |
| **Layer style rendering differences** | Avoid uncommon effects | Preview on target platform |

## 10.5 Data Loss Prevention

### Critical Rules

1. **Save early, save often** - Auto-save every 5-10 minutes
2. **Version naming** - Use clear version numbers (filename_v01.psd, v02.psd)
3. **Keep originals** - Never overwrite source files
4. **Backup workflow** - Use Creative Cloud sync or manual backup
5. **Check saves** - Verify files save successfully before closing
6. **Handle crashes** - Use recovery from Temp folder if Photoshop crashes
7. **Export important selections** - Save critical paths to Alpha Channels or Paths panel
8. **Document important settings** - Note color profiles, dimensions, and special settings
