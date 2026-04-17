# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Quick Fix |
|---|---------|----------|--------|-----------|
| 1 | **Using wrong dimensions** | 🔴 High | Cropped content, wrong aspect ratio | Check platform specs before starting, use templates |
| 2 | **RGB colors for print** | 🔴 High | Colors shift significantly in print | Export as PDF Print with CMYK conversion |
| 3 | **Low-resolution images** | 🔴 High | Blurry, pixelated output | Upload images at display size or larger |
| 4 | **Unlinked brand assets** | 🟡 Medium | Outdated logos, inconsistent branding | Upload to Brand Kit, link assets |
| 5 | **Too many fonts** | 🟡 Medium | Inconsistent, unprofessional look | Limit to 2-3 fonts from Brand Kit |
| 6 | **Not using templates** | 🟡 Medium | Wasted time recreating basics | Create and save team templates |
| 7 | **Skipping preview** | 🟡 Medium | Embarrassing errors in final | Preview on different devices/platforms |
| 8 | **Overcrowded designs** | 🟡 Medium | Poor readability, cluttered | Follow grid system, limit elements |
| 9 | **Ignoring bleed for print** | 🔴 High | White edges after trimming | Add 3mm bleed to print designs |
| 10 | **Not saving work** | 🔴 High | Lost hours of work | Canva auto-saves, but verify |

## 10.2 Performance Issues

### Common Performance Problems

| Issue | Cause | Solution |
|-------|-------|----------|
| **Slow loading designs** | Large file with many elements | Remove unused elements, simplify |
| **Can't upload images** | File too large (>25MB) | Compress images before upload |
| **Font not loading** | Font not supported | Convert text to curves or use supported font |
| **Video playback lag** | Too many video layers | Reduce video quality or trim length |
| **Resize fails** | Complex elements incompatible | Flatten or simplify before resize |
| **Export stuck** | File too complex | Reduce element count, lower resolution |

### File Size Optimization

| Strategy | Impact | How |
|----------|--------|-----|
| Resize images before upload | High | Use external tool or Canva's resize |
| Remove duplicate images | Medium | Audit uploads, delete unused |
| Use vectors over rasters | High | SVG, PNG, or illustrations |
| Limit animation complexity | Medium | Simplify keyframes |
| Compress final export | Medium | Use standard quality for web |

### Browser Performance Tips

- **Use supported browser**: Chrome recommended
- **Clear cache**: Regularly clear browser cache and cookies
- **Disable extensions**: Some browser extensions interfere
- **Check internet speed**: Slow connection affects cloud saving
- **Try incognito mode**: Disables extensions, tests if extension conflict

## 10.3 Collaboration Issues

### Team Workflow Problems

| Problem | Prevention | Fix |
|---------|-----------|-----|
| **Design overwritten** | Use version history | Restore from Trash or version history |
| **Permission errors** | Check folder settings | Contact admin for access |
| **Brand inconsistencies** | Use Brand Kit | Update Brand Kit, reapply to designs |
| **Lost feedback** | Enable commenting | Check comment notifications |
| **Wrong version shared** | Clear naming convention | Use dates in filenames |

### Sharing & Permissions Checklist

- [ ] Verify recipient has correct permission level
- [ ] Check if design is in shared folder
- [ ] Confirm Brand Kit is available to team
- [ ] Review comment notifications
- [ ] Test link access before sending

## 10.4 Export & Format Issues

### Export Format Pitfalls

| Mistake | Correct Approach |
|---------|------------------|
| JPG for transparency | Use PNG with transparent background |
| Low-res JPG for print | Export at high quality or use PDF Print |
| MP4 without audio | Include audio track or export separately |
| PDF Standard for print | Use PDF Print with bleed and CMYK |
| SVG without curves | Convert text to paths before export |

### Print Export Checklist

- [ ] Design dimensions include 3mm bleed
- [ ] All images are 300 DPI+
- [ ] Colors are CMYK values (or use PDF Print conversion)
- [ ] Text is converted to outlines (optional but safe)
- [ ] Crop marks and bleed marks enabled
- [ ] Preview print colors before export

## 10.5 Brand Kit Pitfalls

### Common Brand Kit Mistakes

| Mistake | Impact | Best Practice |
|---------|--------|---------------|
| **Too many colors** | Diluted brand identity | Limit to 5-7 brand colors |
| **Low-res logo** | Blurry when scaled | Upload high-res PNG/SVG |
| **Inconsistent fonts** | Weak brand recognition | Choose 1-2 font families |
| **Missing logo variations** | Inconsistent sizing | Include horizontal, stacked, icon |
| **No contrast guidelines** | Poor accessibility | Define minimum contrast ratios |
| **Outdated Brand Kit** | Stale branding | Review and update quarterly |

### Brand Kit Maintenance

1. **Quarterly Review**
   - Audit all colors, fonts, logos
   - Remove unused elements
   - Update any outdated assets
   - Document changes

2. **Version Control**
   - Date Brand Kit updates
   - Archive old versions
   - Notify team of changes
   - Update related templates

3. **Access Management**
   - Assign Brand Kit admin
   - Review team access regularly
   - Remove departed team members
   - Audit permission logs
