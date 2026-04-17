# Standards & Reference

## 7.1 Official Documentation

- [Illustrator Help](https://helpx.adobe.com/illustrator/user-guide.html)
- [Illustrator Learn & Support](https://helpx.adobe.com/illustrator/tutorials.html)
- [Illustrator API Reference](https://developer.adobe.com/illustrator/api/)
- [Adobe Fonts (Typekit)](https://fonts.adobe.com)
- [Adobe Exchange](https://exchange.adobe.com)
- [Illustrator Keyboard Shortcuts PDF](https://helpx.adobe.com/content/dam/help/en/illustrator/pdf/illustrator_shortcuts.pdf)

## 7.2 Keyboard Shortcuts & Configuration

### Essential Keyboard Shortcuts

| Action | Windows | macOS |
|--------|---------|-------|
| New Document | Ctrl+N | Cmd+N |
| Open | Ctrl+O | Cmd+O |
| Save | Ctrl+S | Cmd+S |
| Save As | Ctrl+Shift+S | Cmd+Shift+S |
| Place | Ctrl+Shift+P | Cmd+Shift+P |
| Export | Ctrl+E | Cmd+E |
| Undo | Ctrl+Z | Cmd+Z |
| Redo | Ctrl+Shift+Z | Cmd+Shift+Z |
| Group | Ctrl+G | Cmd+G |
| Ungroup | Ctrl+Shift+G | Cmd+Shift+G |
| Lock Selection | Ctrl+2 | Cmd+2 |
| Unlock All | Ctrl+Alt+2 | Cmd+Option+2 |
| Hide Selection | Ctrl+3 | Cmd+3 |
| Show All | Ctrl+Alt+3 | Cmd+Option+3 |
| Selection Tool | V | V |
| Direct Selection | A | A |
| Pen Tool | P | P |
| Type Tool | T | T |
| Rectangle | M | M |
| Ellipse | L | L |
| Brush | B | B |
| Pencil | N | N |
| Eraser | Shift+E | Shift+E |
| Gradient | G | G |
| Eyedropper | I | I |
| Rotate | R | R |
| Scale | S | S |
| Reflect | O | O |
| Shape Builder | Shift+M | Shift+M |
| Live Paint Bucket | K | K |
| Swatch Libraries | Shift+F3 | Shift+F3 |
| Stroke Panel | Ctrl+F10 | Cmd+F10 |
| Color Panel | F6 | F6 |
| Align | Ctrl+Shift+7 | Cmd+Shift+7 |
| Pathfinder | Ctrl+Shift+F9 | Cmd+Shift+F9 |
| Artboards | Ctrl+O (in new doc) | Cmd+O |
| Zoom In | Ctrl++ | Cmd++ |
| Zoom Out | Ctrl+- | Cmd+- |
| Fit Artboard in Window | Ctrl+0 | Cmd+0 |
| Actual Size | Ctrl+1 | Cmd+1 |
| Outline Mode | Ctrl+Y | Cmd+Y |
| Overprint Preview | Ctrl+Shift+Alt+Y | Cmd+Shift+Option+Y |
| Toggle Rulers | Ctrl+R | Cmd+R |
| Toggle Grid | Ctrl+' | Cmd+' |

### Workspace Configurations

#### Vector Illustration
- Panel Layout: Essentials Classic
- Snap to Grid: Enabled
- Pixel Preview: On for web work
- Rulers: Visible, set to points or pixels

#### Print Production
- Panel Layout: Printing/Distribution
- Color Mode: CMYK
- Overprint Preview: On
- Pixel Preview: Off

#### Icon Design
- Artboard: 24x24, 48x48, 64x64 grids
- Grid: 1pt = 1px for icons
- Snap to Pixel: Enabled
- Align to Pixel Grid: Enabled

### Color Settings

| Color Mode | Use Case | Configuration |
|------------|----------|---------------|
| RGB | Web, digital | sRGB IEC61966-2.1 |
| CMYK | Print | U.S. Web Coated (SWOP) v2 |
| Spot Color | Professional print | Pantone, DIC, TOYO |
| Grayscale | Black & white print | Dot gain 20% |

## 7.3 Common Tasks & Workflows

### Drawing & Path Editing
- **Pen Tool**: Click for corners, drag for curves, Alt+click to adjust handles
- **Anchor Point Tool**: Convert points, add/remove points
- **Shape Builder**: Click to unite, Alt+click to subtract
- **Pathfinder**: Unite, Minus Front, Intersect, Exclude, Divide
- **Compound Paths**: Object > Compound Path > Make

### Layer Management
- **Layer Panel**: Organize artwork into logical groups
- **Layer Naming**: Use descriptive names for assets
- **Isolate Layer**: Double-click to edit in isolation
- **Paste Remembers Layers**: Keep layers organized when pasting
- **Release to Layers**: Distribute objects to separate layers

### Text Operations
- **Point Text**: Click to create single-line text
- **Area Text**: Click and drag to create text box
- **Type on Path**: Place text on bezier path
- **Outlines**: Type > Create Outlines (converts to paths)
- **Find/Replace**: Edit > Find/Replace Text
- **Glyphs**: Type > Glyphs (special characters)

### Export Formats

| Format | Use Case | Key Settings |
|--------|----------|---------------|
| AI | Native files | Preserve editing, Save with Links |
| EPS | Legacy compatibility | Illustrator EPS 8, 10, or CS |
| PDF | Print, sharing | PDF/X-1a, PDF/X-4 |
| SVG | Web, code | SVG 1.1, Minify, Embed fonts |
| PNG | Web with transparency | 1x, 2x, with/without background |
| JPEG | Web images | Quality 80-100 |
| DXF/DWG | CAD | AutoCAD Interchange |

### Artboard Management
- **Artboard Tool**: Shift+O to activate
- **Multiple Artboards**: File > Document Setup > Artboards
- **Rearrange Artboards**: Use Artboard tool to drag
- **Export All**: File > Export > Export for Screens
- **Print Range**: Use artboard numbers in print dialog

## 7.4 Version Compatibility

| Version | Platform | Key Features |
|---------|----------|--------------|
| 2024 (28.x) | Win/Mac | Generative AI, Retype, Enhanced Vector |
| 2023 (27.x) | Win/Mac | Variable fonts, Shaper improvements |
| 2022 (26.x) | Win/Mac | Cloud Documents enhancements |
| 2021 (25.x) | Win/Mac | Recolor improvements, 3D effects |
| 2020 (24.x) | Win/Mac | Variable fonts, New workspace |
| CC 2019 (23.x) | Win/Mac | Freeform gradients, Global editing |
| CC 2018 (22.x) | Win/Mac | Properties panel, Custom toolbar |

**File Compatibility Notes:**
- Save as AI with PDF compatible for cross-version support
- Embed fonts for portable files
- Use Package (File > Package) to collect all assets
- CS6 and earlier have limited feature support

## 7.5 Performance Tips

### Memory & Performance
- **Purge**: Edit > Purge > All to free memory
- **Reduce file size**: File > Reduce File Size
- **Increase undo levels**: Preferences > Performance > Undo Levels (up to 100)
- **RAM**: Allocate 70% of available RAM to Illustrator

### Large File Handling
- **Simplify paths**: Use Object > Path > Simplify
- **Reduce anchor points**: Path > Simplify (curve precision)
- **Flatten transparency**: For print production files
- **Close unused documents**: Reduce memory footprint

### Cache & GPU Settings
- **GPU Performance**: Preferences > GPU Performance (enable for smoother zoom/pan)
- **Disable thumbnails**: Preferences > General > Disable Auto-Update of Thumbnails
- **Deactivate Rulers**: When not needed
- **Reduce artboard count**: Process fewer artboards at once

### Tips
- Use Symbols for repeated elements
- Use Artboards instead of multiple files for variants
- Turn off GPU for stability issues
- Save incrementally (v1, v2, v3)
- Use linked files for large images (vs. embedded)
