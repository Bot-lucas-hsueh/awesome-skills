# Scenario Examples

## 9.1 Project Scenarios

### Scenario 1: Social Media Campaign

**User:** "I need to create 10 social media graphics for a product launch across Instagram, Facebook, and LinkedIn."

**Expert:**
> **Solution:**
> 
> 1. Create a master document with Artboards, one per size requirement:
>    - Instagram Post: 1080x1080 px
>    - Instagram Story: 1080x1920 px
>    - Facebook Post: 1200x630 px
>    - LinkedIn Post: 1200x627 px
> 
> 2. Use Layer Comps to capture variations (light/dark theme, with/without CTA)
> 
> 3. Create reusable elements in a separate document, then Copy/Paste as Smart Objects
> 
> 4. Batch export: File > Export As > Select all artboards > Export
> 
> 5. Use Image Processor (File > Scripts > Image Processor) for additional batch resizing
> 
> **Key Tips:**
> - Set up Color Lookup tables for consistent brand colors
> - Use linked Smart Objects for the product image (swap once, updates all)
> - Export at 2x resolution for retina displays

---

### Scenario 2: Product Photo Retouching

**User:** "I have product photos that need background removal and color correction to match our brand."

**Expert:**
> **Solution:**
> 
> 1. **Background Removal:**
>    - Use Select > Subject for initial selection
>    - Refine with Select and Mask (Refine Edge Brush)
>    - Add layer mask for non-destructive workflow
>    - Clean edges with the Brush tool on the mask
> 
> 2. **Color Matching:**
>    - Sample brand reference colors with Eyedropper
>    - Apply adjustment layers: Hue/Saturation, Color Balance
>    - Use Match Color to transfer tones from reference image
>    - Create clipping masks to apply adjustments to subject only
> 
> 3. **Finishing:**
>    - Add drop shadow via Layer Style
>    - Apply subtle sharpening (High Pass filter)
>    - Create selection from subject layer, inverse, add color background
> 
> **Key Tips:**
> - Work non-destructively with adjustment layers
> - Sample colors from a neutral reference (gray card or Macbeth chart)
> - Save selection as Alpha Channel for reuse

---

### Scenario 3: Photo Composite

**User:** "I need to composite multiple photos into a dramatic landscape scene."

**Expert:**
> **Solution:**
> 
> 1. **Planning:**
>    - Gather reference images matching lighting direction
>    - Determine focal length and camera angle
>    - Plan layer order: sky > mountains > midground > foreground
> 
> 2. **Base Setup:**
>    - Create canvas at final output size
>    - Set color mode (sRGB for web, Adobe RGB for print)
>    - Import background image, scale to fit
> 
> 3. **Element Integration:**
>    - Place each element on separate layers
>    - Use Free Transform (Ctrl+T) to position and scale
>    - Apply perspective corrections as needed
>    - Create layer masks to blend edges
> 
> 4. **Lighting Match:**
>    - Identify main light source in composite
>    - Add dodge/burn layers to adjust local lighting
>    - Apply Color Balance to match color temperature
>    - Add atmospheric haze with Gradient overlay
> 
> 5. **Finishing:**
>    - Add dust, particles, or wildlife elements
>    - Apply overall color grading
>    - Add vignette for focus
>    - Sharpen for output

## 9.2 Client Deliverables

### Web Design Deliverable Package

| Item | Format | Specs |
|------|--------|-------|
| Hero Image | PNG-24 | 1920x1080 @ 2x, sRGB |
| Banner Set | PNG-24 | 1500x500, 1200x628, 800x320 @ 2x |
| Thumbnails | PNG-24 | 400x400, 200x200 |
| Icons | SVG or PNG-24 | 48x48, 32x32, 24x24 @ 2x |
| Working File | PSD | Max compatibility, organized layers |
| Style Guide | PDF | Colors, fonts, usage rules |

### Print Design Deliverable Package

| Item | Format | Specs |
|------|--------|-------|
| Final Artwork | PDF/X-1a or PDF/X-4 | CMYK, embedded profiles, 3mm bleed |
| High-Res Export | TIFF | 300 DPI, CMYK, LZW compression |
| Proof | PDF | Press quality, showing bleed/crop marks |
| Working File | PSD | Max compatibility, all layers |
| Links | Folder | All linked images at full resolution |
| Fonts | Folder | Outlined or embedded fonts |

### Brand Asset Package

| Item | Format | Specs |
|------|--------|-------|
| Logo Variations | SVG, PNG-24, EPS | Color, black, white versions |
| Color Palette | ASE or PDF | CMYK, RGB, HEX values |
| Typography | PDF | Font names, weights, usage |
| Icon Set | SVG | Consistent grid, stroke weight |
| Template Files | PSD, AI | Branded layouts for common uses |

## 9.3 Automation

### Photoshop Actions

**Batch Watermarking:**
```
Action: AddWatermark
├── Step 1: Open Image (let user select)
├── Step 2: Create watermark layer
│   └── Text: "© 2024 Company Name"
│   └── Position: Bottom-right corner
│   └── Opacity: 50%
├── Step 3: Flatten Image
├── Step 4: Save for Web (Quality 80)
└── Step 5: Close (don't save)
```

**Application:**
- Play action on folder: File > Automate > Batch
- Create Droplet for drag-and-drop processing
- Set destination folder for output
- Override "Save As" commands for batch naming

### Contact Sheet Generation

```
File > Automate > Contact Sheet II
├── Source Images: Select folder
├── Document: Width 8.5", Height 11", Columns 4, Rows 5
├── Thumbnails: Fit to Cell, Rotate First Photo unchecked
├── Use Filename as Caption: checked
└── Output: PDF or Multipage TIFF
```

### Scripts for Advanced Automation

**Resize and Export:**
```javascript
// Resize.jsx - Resize document and export
var doc = app.activeDocument;
doc.resizeImage(Width=1920, Height=null, resolution=72);
doc.saveAs(new File("~/Desktop/export.png"), PNGSaveOptions);
```

**Layer Exporter:**
```javascript
// ExportLayers.jsx - Export each layer as PNG
for (var i = 0; i < doc.layers.length; i++) {
    var layer = doc.layers[i];
    layer.visible = true;
    // Export code here
    layer.visible = false;
}
```

### Variables and Data Sets

1. **Define Variables**: Edit > Variables > Variable
2. **Create Data Sets**: Edit > Variables > Data Sets
3. **Apply**: File > Apply Data Set
4. **Batch**: Export to folder with File > Export > Data Sets as Files
