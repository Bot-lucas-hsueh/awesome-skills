# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Quick Fix |
|---|---------|----------|--------|-----------|
| 1 | **Converting text to paths prematurely** | 🔴 High | Can't edit text later | Keep original AI with live text |
| 2 | **Embedding images instead of linking** | 🔴 High | Massive file size, no updates | Link images, use Links panel to manage |
| 3 | **Using RGB for print** | 🔴 High | Colors shift dramatically | Switch to CMYK, check color values |
| 4 | **Missing bleed for print** | 🔴 High | White edges after trimming | Add 3mm bleed to all print artboards |
| 5 | **Too many anchor points** | 🟡 Medium | Slow performance, poor curves | Simplify paths, use Smooth Tool |
| 6 | **Ignoring overprint settings** | 🟡 Medium | Unexpected color results | Preview with Overprint Preview |
| 7 | **Using raster effects in vectors** | 🟡 Medium | Print quality issues | Minimize raster effects, use vectors |
| 8 | **Mismatched stroke weights** | 🟡 Medium | Inconsistent visual weight | Use consistent stroke values |
| 9 | **Not outlining fonts for handoff** | 🔴 High | Font substitution issues | File > Package includes fonts |
| 10 | **Saving as outdated AI format** | 🟡 Medium | Compatibility issues | Use latest AI format with compatibility |

## 10.2 Performance Issues

### Common Performance Problems

| Issue | Cause | Solution |
|-------|-------|----------|
| **Slow zooming/paning** | Complex paths, many effects | Reduce undo history, simplify paths |
| **Large file size** | Embedded images, many effects | Link images, expand appearances |
| **Crash on save** | Memory issues, corrupt data | Purge, reduce file complexity |
| **Slow rendering** | Raster effects, transparency | Flatten transparency, rasterize effects |
| **Pen tool lag** | Complex artwork | Hide off-screen content |
| **Font menu slow** | Many fonts loaded | Disable unused fonts in System |

### Large File Optimization

| Technique | Impact | How |
|-----------|--------|-----|
| **Link images** | High | Use Links panel, don't embed |
| **Simplify paths** | High | Object > Path > Simplify |
| **Expand appearances** | Medium | Object > Expand Appearance |
| **Flatten transparency** | Medium | Object > Flatten Transparency |
| **Remove unused** | Medium | Select > Object > All Unused |
| **Reduce undo levels** | Medium | Preferences > Performance |

### Tips for Complex Artwork

- [ ] Use symbols for repeated elements
- [ ] Group related objects to reduce selection time
- [ ] Hide layers not currently in use
- [ ] Use Artboards instead of multiple files
- [ ] Avoid using Photoshop effects (Blur, Shadows)
- [ ] Reduce number of gradient stops
- [ ] Use art-directed scaling instead of complex warps

## 10.3 Print Production Issues

### Print-Specific Pitfalls

| Problem | Prevention | Fix |
|---------|-----------|-----|
| **Low resolution images** | Check at 100% in Preview | Replace with 300 DPI images |
| **Missing fonts** | Package document | Embed or outline fonts |
| **Color shifts** | Use CMYK, proof colors | Adjust CMYK values |
| **Over-saturation** | Check ink coverage | Reduce rich black percentage |
| **Registration issues** | Check trapping | Apply slight overprint |
| **Trim issues** | Include bleed | Add 3mm bleed, use crop marks |

### Preflight Checklist

- [ ] All images 300+ DPI at print size
- [ ] Colors are CMYK (not RGB)
- [ ] Bleed is included (3mm)
- [ ] Text is 6pt minimum for small text
- [ ] Fonts are embedded or outlined
- [ ] Spot colors are defined correctly
- [ ] Overprint settings are intentional
- [ ] No transparency issues

## 10.4 Path & Vector Issues

### Common Path Problems

| Issue | Cause | Fix |
|-------|-------|-----|
| **Open paths** | Incomplete shapes | Close paths with Pen tool |
| **Stray anchor points** | Editing artifacts | Select > Object > Stray Points |
| **Crossed paths** | Poor construction | Clean up in Outline mode |
| **Inconsistent joins** | Mixed corner types | Unify with Pathfinder |
| **Hidden paths** | Layer visibility | Show all layers, check Layers panel |

### Path Cleanup

```markdown
1. Object > Path > Clean Up
   - Removes stray points
   - Removes unused objects on hidden layers
   
2. Select > Object > Stray Points
   - Selects isolated anchor points
   
3. Ctrl+Y (Cmd+Y) - Toggle Outline mode
   - See all paths clearly
   
4. Direct Selection to check overlaps
   - A key to select individual points
```

## 10.5 Color & Appearance Issues

### Color Management Pitfalls

| Mistake | Correct Approach |
|---------|------------------|
| **RGB in CMYK document** | Assign and convert colors |
| **Unknown color profiles** | Assign correct profile |
| **Proofing off** | Use Proof Setup for soft proof |
| **Spot/RGB mix** | Use either Spot OR Process |

### Appearance Panel Issues

| Issue | Solution |
|-------|----------|
| Grayed out effects | Expand Appearance first |
| Can't modify stroke | Double-click in Appearance panel |
| Effect not showing | Check stacking order |
| Gradient banding | Increase gradient steps, use noise |
