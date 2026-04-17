# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Quick Fix |
|---|---------|----------|--------|-----------|
| 1 | **Not applying modifiers before export** | 🔴 High | Invisible or broken mesh in engine | Ctrl+A > Apply All Modifiers |
| 2 | **Wrong scale** | 🔴 High | Model too small/large in game | Check units, 1 BU = 1 meter |
| 3 | **Non-manifold geometry** | 🔴 High | Breaks boolean, physics, export | Select > Select All by Trait > Non-Manifold |
| 4 | **Ngons and Tris in wrong places** | 🟡 Medium | Issues with subdivision | Keep quads for deformation areas |
| 5 | **Inverted normals** | 🟡 Medium | Black/dark shading | Shift+N to recalculate normals |
| 6 | **Missing UV seams for unwrap** | 🟡 Medium | Distorted textures | Mark seams before unwrapping |
| 7 | **Overlapping UV islands** | 🟡 Medium | Texture bleeding | Repack UVs in UV Editor |
| 8 | **Heavy geometry on hidden objects** | 🟡 Medium | Slow viewport | Hide objects instead of moving off-screen |
| 9 | **Not saving incrementally** | 🔴 High | Lost work on crash | Save versions regularly (v01, v02) |
| 10 | **Using Blender Internal instead of Eevee/Cycles** | 🟡 Medium | Deprecated, inconsistent | Migrate to Eevee or Cycles |

## 10.2 Performance Issues

### Viewport Performance Problems

| Issue | Cause | Solution |
|-------|-------|----------|
| **Slow viewport** | Too many polygons | Enable simplification in Scene properties |
| **Lag when orbiting** | Heavy modifiers | Reduce subdivision preview level |
| **Slow sculpting** | Too many dyntopo polys | Reduce detail percentage |
| **Slow shading** | Complex node setups | Use simple materials in viewport |

### Render Performance Optimization

| Technique | Impact | When to Use |
|-----------|--------|-------------|
| **Viewport Denoising** | High | Always for preview |
| **Adaptive Sampling** | High | Final renders |
| **Light Bounces** | Medium | Reduce to 1-2 for performance |
| **Clamp Indirect** | Medium | Reduce fireflies |
| **Denoise compositor** | High | When samples are limited |

### Large Scene Management

| Problem | Solution |
|---------|----------|
| **Memory issues** | Enable GPU for viewport, reduce undo |
| **Slow selection** | Use collections to organize |
| **Long saves** | Pack into .blend, limit history |
| **Scene load time** | Disable add-ons you don't use |

## 10.3 Modeling Pitfalls

### Topology Issues

| Issue | Prevention | Fix |
|-------|-----------|-----|
| **Poles at deformation areas** | Plan edge flow | Add/remove edge loops |
| **Ngons on curved surfaces** | Keep quad-based | Triangulate or fix |
| **Inconsistent face density** | Use subdivision properly | Decimate or remesh |
| **Double vertices** | Merge by distance | M > Merge by Distance |

### UV Mapping Mistakes

| Mistake | Prevention | Fix |
|---------|-----------|-----|
| **Stretched UVs** | Unwrap properly | Mark seams, use Smart UV Project |
| **Seams on visible areas** | Plan seam placement | Move seams to hidden edges |
| **Tiny islands** | Pack carefully | Scale up small islands |
| **UV outside 0-1** | Keep in bounds | Pack UVs properly |

### Animation Issues

| Problem | Solution |
|---------|----------|
| **Jittery motion** | Increase interpolation or keyframes |
| **Floating feet** | Use IK, adjust hip motion |
| **Sliding contacts** | Check weight painting |
| **Exploded on frame 1** | Clear transform locks |

## 10.4 Rendering Pitfalls

### Common Render Errors

| Issue | Cause | Fix |
|-------|-------|-----|
| **Black render** | No lights, normals inverted | Add lights, recalculate normals |
| **Fireflies** | Caustics, high contrast | Increase samples, use denoiser |
| **Band artifacts** | Insufficient samples | Increase render samples |
| **Noise on glass** | Caustics, not enough bounces | Enable caustics or simplify material |
| **Wrong colors in render** | Color management | Set to Filmic, adjust exposure |

### Color Management Settings

| Setting | Use Case | Notes |
|---------|----------|-------|
| Filmic | Photorealistic | Default, recommended |
| Standard | Stylized | Less dynamic range |
| Raw | Technical/technical | No tone mapping |

### Light Troubleshooting

| Problem | Solution |
|---------|----------|
| **Too harsh shadows** | Soften with area light, increase size |
| **No shadows** | Enable shadow in light settings |
| **No ambient light** | Add environment/world lighting |
| **Inconsistent tones** | Use consistent HDRI, balance lights |

## 10.5 Data Loss Prevention

### Critical Rules

1. **Auto-save**: Enable in Preferences > Save & Load
2. **Incremental saves**: Ctrl+Shift+S to save copy
3. **Pack external**: File > External Data > Pack All
4. **Backup versions**: Keep last 3-5 versions
5. **Cloud sync**: Use Blender Cloud or cloud storage
6. **Verify saves**: Check file opens correctly

### Crash Recovery

| Method | How |
|--------|-----|
| **Auto-recover** | File > Recover Auto Save |
| **Temp files** | Check system temp folder |
| **Crash dump** | Blender creates .blend1 backup |
| **Previous version** | Windows File History, macOS Time Machine |

### Project Backup Checklist

- [ ] Main .blend file saved
- [ ] External textures packed or linked
- [ ] Reference images included
- [ ] Recent versions backed up
- [ ] Add-on state documented
- [ ] Render settings noted
