# Standards & Reference

## 7.1 Official Documentation

- [Photoshop Help](https://helpx.adobe.com/photoshop/index.html)
- [Photoshop User Guide](https://helpx.adobe.com/photoshop/user-guide.html)
- [Adobe Camera Raw](https://helpx.adobe.com/camera-raw/using/camera-raw-plug-ins.html)
- [Adobe Lightroom to Photoshop](https://helpx.adobe.com/photoshop/using/photography-features-lightroom.html)
- [Adobe Stock](https://stock.adobe.com)
- [Adobe Exchange](https://exchange.adobe.com)

## 7.2 Keyboard Shortcuts & Configuration

### Essential Keyboard Shortcuts

| Action | Windows | macOS |
|--------|---------|-------|
| New Document | Ctrl+N | Cmd+N |
| Open | Ctrl+O | Cmd+O |
| Save | Ctrl+S | Cmd+S |
| Save As | Ctrl+Shift+S | Cmd+Shift+S |
| Undo | Ctrl+Z | Cmd+Z |
| Step Forward | Ctrl+Shift+Z | Cmd+Shift+Z |
| Free Transform | Ctrl+T | Cmd+T |
| Deselect | Ctrl+D | Cmd+D |
| Select All | Ctrl+A | Cmd+A |
| Inverse Selection | Ctrl+Shift+I | Cmd+Shift+I |
| Layer via Copy | Ctrl+J | Cmd+J |
| Layer via Cut | Ctrl+Shift+J | Cmd+Shift+J |
| Group Layers | Ctrl+G | Cmd+G |
| Ungroup | Ctrl+Shift+G | Cmd+Shift+G |
| Merge Down | Ctrl+E | Cmd+E |
| Merge Visible | Ctrl+Shift+E | Cmd+Shift+E |
| Fill Dialog | Shift+F5 | Shift+F5 |
| Levels | Ctrl+L | Cmd+L |
| Curves | Ctrl+M | Cmd+M |
| Hue/Saturation | Ctrl+U | Cmd+U |
| Black & White | Ctrl+Alt+Shift+B | Cmd+Option+Shift+B |
| Brush Tool | B | B |
| Clone Stamp | S | S |
| Healing Brush | J | J |
| Spot Healing Brush | Shift+J | Shift+J |
| Dodge Tool | O | O |
| Burn Tool | O | O |
| Pen Tool | P | P |
| Direct Selection | A | A |
| Zoom In | Ctrl++ | Cmd++ |
| Zoom Out | Ctrl+- | Cmd+- |
| Fit on Screen | Ctrl+0 | Cmd+0 |
| Actual Pixels | Ctrl+1 | Cmd+1 |
| Toggle Screen Mode | F | F |
| Show Rulers | Ctrl+R | Cmd+R |
| Show Grid | Ctrl+' | Cmd+' |
| Create Clipping Mask | Ctrl+Alt+G | Cmd+Option+G |
| New Fill Layer | Layer > New Fill Layer | Layer > New Fill Layer |

### Workspace Configurations

#### Photography Workspace
- Panel Layout: Essentials > Photography
- Color Settings: North America General Purpose 2
- Histogram: Always visible in the histogram panel
- Tool Presets: Brush, Clone Stamp, Healing Brush

#### Digital Painting Workspace
- Panel Layout: Painting
- Brush Tip Preview: Enabled
- Color Sampler: Show on canvas
- Tablet: Enable pressure sensitivity

#### Print Production Workspace
- Color Mode: CMYK
- Gamut Warning: Enabled
- Overprint Preview: Enabled
- Color Settings: North America Prepress 2

## 7.3 Common Tasks & Workflows

### Layer Management
- **Layer Groups**: Use groups (Ctrl+G) to organize related layers
- **Smart Objects**: Convert to Smart Object (right-click > Convert to Smart Object) for non-destructive scaling
- **Layer Comps**: Use Layer Comps panel for presenting design variations
- **Artboards**: Use Artboards for multi-page layouts and responsive designs
- **Layer Styles**: Use Layer > Layer Style for shadows, strokes, gradients
- **Blending Modes**: Normal, Multiply, Screen, Overlay, Soft Light, Hard Light, Difference

### Export Formats & Methods

| Format | Use Case | Settings |
|--------|----------|----------|
| PSD | Working files, layer preservation | Max compatibility |
| TIFF | Print, high-quality archives | LZW compression |
| PNG-24 | Web with transparency | Interlaced |
| PNG-8 | Web graphics, icons | 256 colors |
| JPEG | Web photos, social media | Quality 80-90 |
| PDF | Print, presentation, review | Press Quality |
| SVG | Web vectors (via Export) | Outlines |

### Export for Web (Legacy)
- File > Export > Export As
- File > Scripts > Export Layers to Files
- Generate Image Assets (CC 2015.5+)

### Batch Processing
- **Image Processor** (File > Scripts > Image Processor)
  - Resize, convert format, add copyright
  - Run actions on multiple files
- **Actions Panel**
  - Record custom workflows
  - Batch command (File > Automate > Batch)
  - Create droplet for drag-and-drop processing

## 7.4 Version Compatibility

| Version | Platform | Key Features |
|---------|----------|--------------|
| 2024 (25.x) | Win/Mac | Generative Fill, Remove Background AI, Contextual Task Bar |
| 2023 (24.x) | Win/Mac | Neural Filters improvements, Object Selection tool |
| 2022 (23.x) | Win/Mac | Super Zoom, Contextual Task Bar |
| 2021 (22.x) | Win/Mac | Neural Filters, Sky Replacement |
| 2020 (21.x) | Win/Mac | Multiple Undo, Pattern Preview |
| CC 2019 (20.x) | Win/Mac | Frame Tool, Content-Aware Fill improvements |
| CC 2018 (19.x) | Win/Mac | Customizable workspaces, Properties panel |

**File Compatibility Notes:**
- Always save in Max Compatibility PSD for cross-version support
- Smart Objects preserve editability across versions
- Some Neural Filters require GPU acceleration
- Camera Raw versions update independently

## 7.5 Performance Tips

### Memory & Performance
- **Purge** (Edit > Purge) to free memory
- **History Log**: Limit to 50 states to reduce file size
- **Scratch Disks**: Set fastest drive as primary scratch disk
- **GPU Settings**: Preferences > Performance > GPU Settings
  - Use GPU for History and Thumbnail rendering
  - 70-80% of RAM allocation recommended

### Large File Handling
- Work at lower resolution, scale up only for final output
- Use Smart Objects to reference high-res sources
- Disable auto-save during heavy editing (Preferences > File Handling)
- Close unused documents
- Use 16-bit or 32-bit for HDR work

### Cache & Performance Settings
- **Tile Size**: 128K or 256K for large files
- **History & Cache**: Balance between performance and undo levels
- **GPU Acceleration**: Enable for smoother painting and zooming
- **Antialiasing**: Artboard and type: Crisp

### Tips
- Use layers efficiently - flatten only when necessary
- Avoid excessive layer styles on large images
- Use layer comps instead of duplicating documents
- Save frequently to prevent data loss
- Use linked Smart Objects over embedded for shared assets
