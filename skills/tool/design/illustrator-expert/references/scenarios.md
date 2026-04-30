# Scenario Examples

## 9.1 Project Scenarios

### Scenario 1: Responsive Icon Set

**User:** "I need to create a 48-icon set for a mobile app that scales from 16px to 64px."

**Expert:**
> **Solution:**
> 
> **1. Grid Setup**
> - Create 48x48 master artboard
> - Enable Pixel Preview (View > Pixel Preview)
> - Enable Snap to Pixel (View > Snap to Pixel)
> - Set up 1px grid for detail alignment
> 
> **2. Construction Rules**
> - Use 2px strokes for primary elements
> - Keep visual weight consistent across icons
> - Use consistent corner radius (0px, 2px, or 4px)
> - Align to center for optical balance
> - Avoid 1px lines (disappear at small sizes)
> 
> **3. Master File Organization**
> ```
> - Artboard 1: Home
> - Artboard 2: Search
> - Artboard 3: Profile
> ... (48 total)
> ```
> 
> **4. Export Process**
> - File > Export > Export for Screens
> - Select all 48 artboards
> - Choose formats: SVG, PNG
> - Set PNG scales: 1x, 2x, 3x (16px, 32px, 48px)
> - Enable Trim to Artboard
> 
> **5. Optimization**
> - Clean SVG code (remove metadata)
> - Combine paths where possible
> - Test at actual sizes on device
> - Verify accessibility (add title/desc tags)

---

### Scenario 2: Brand Identity System

**User:** "I'm designing a complete brand identity for a new company. What files should I deliver?"

**Expert:**
> **Solution:**
> 
> **Logo Package:**
> - Primary logo (full color, all variants)
> - Logo with tagline
> - Icon-only version
> - Color variations (dark, light, mono)
> - Layout variations (horizontal, stacked)
> 
> **File Formats:**
> | Format | Purpose | Included Elements |
> |--------|---------|-------------------|
> | AI (master) | Editing, future use | Editable layers, fonts outlined |
> | EPS | Legacy print software | Universal compatibility |
> | SVG | Web, digital | Clean, optimized code |
> | PDF | Print, documents | Press-ready |
> | PNG | Digital, screen | Transparency, various sizes |
> 
> **Color Documentation:**
> - Primary palette with values
> - Secondary/accent palette
> - Pantone/CMYK/RGB/HEX codes
> - Usage rules (minimum sizes, backgrounds)
> 
> **Typography Specs:**
> - Primary typeface with weights
> - Secondary typeface
> - Scale and hierarchy
> - Web font files or link
> 
> **Presentation:**
> - Mockup sheets (business card, letterhead, signage)
> - Clear space and minimum size guidelines
> - Don'ts (incorrect usage examples)
> - Brand guidelines PDF

---

### Scenario 3: Complex Pattern Design

**User:** "I need to create a repeating pattern for fabric. How do I ensure seamless tiling?"

**Expert:**
> **Solution:**
> 
> **1. Pattern Tile Setup**
> - Create artboard at pattern repeat size (e.g., 12" x 12")
> - Set up guides at edges (25%, 50%, 75%, 100%)
> - Place design elements so edges align
> 
> **2. Edge Matching Technique**
> ```
> Left edge elements → Copy → Place on right edge
> Top edge elements → Copy → Place on bottom edge
> Corners → Copy to all four corners
> ```
> 
> **3. Test Seamless**
> - Object > Pattern > Make (opens pattern editor)
> - Drag elements to verify seamless tiling
> - Use Tile Preview to see repeat
> - Adjust spacing until clean
> 
> **4. Color Variations**
> - Create pattern swatch for each colorway
> - Edit in Pattern Editor
> - Save each variation as separate swatch
> 
> **5. Export**
> - High-res TIFF for print (300 DPI)
> - Scaled PDF for swatches
> - JPEG for approval
> - Note repeat dimensions and color codes

## 9.2 Client Deliverables

### Print Collateral Package

| Item | Formats | Specs |
|------|---------|-------|
| Business Card | AI, PDF, PNG | 3.5x2", 300 DPI, CMYK, 3mm bleed |
| Letterhead | AI, PDF | 8.5x11", 300 DPI, CMYK |
| Envelope | AI, PDF | #10 or custom, 300 DPI |
| Email Signature | PNG, HTML | 600px wide, transparent |
| Presentation Template | AI, PDF | 16:9 aspect ratio |

### Web Assets Package

| Item | Format | Sizes/Details |
|------|--------|---------------|
| Favicon | ICO, PNG | 16, 32, 48, 64, 256px |
| App Icon | PNG | 1024x1024 master |
| OG Image | PNG, JPG | 1200x630 |
| Social Posts | PNG | Platform-specific sizes |
| Web Graphics | SVG, PNG | Optimized, responsive |

### Large Format / Signage Package

| Item | Format | Specs |
|------|--------|-------|
| Banner | PDF, EPS | Vector, scaled to size |
| Billboard | PDF | 300 DPI at final size |
| Vehicle Wrap | PDF | CMYK, actual size |
| Trade Show Booth | PDF | With bleeds |

## 9.3 Automation

### Actions for Batch Processing

**Batch Rename Artboards:**
```
Action: RenameArtboards
├── Step 1: Document Setup > New Artboard
├── Step 2: Open Artboards panel
├── Step 3: Use script for advanced naming
└── Step 4: Export with artboard names
```

**Export Script (ExportArtboards.jsx):**
```javascript
// Export each artboard as separate file
var doc = app.activeDocument;
for (var i = 0; i < doc.artboards.length; i++) {
    var ab = doc.artboards[i];
    var fname = ab.name.replace(/\s+/g, '_') + '.svg';
    var expFile = new File('~/Desktop/icons/' + fname);
    var expOpts = new ExportOptionsSVG();
    expOpts.artboardClipping = true;
    doc.exportFile(expFile, ExportType.SVG, expOpts);
}
```

### Data-Driven Graphics

**Variable Data Workflow:**
1. **Prepare Data**: CSV or spreadsheet with fields
2. **Create Template**: Design with placeholders
3. **Define Variables**: Edit > Variables > Define
4. **Import Data**: Edit > Variables > Data Set
5. **Generate**: File > Export > Data Files as Graphics
6. **Output**: Batch of personalized files

### Scripts for Common Tasks

**Remove Unused Swatches:**
```javascript
var doc = app.activeDocument;
var swatches = doc.swatches;
for (var i = swatches.length - 1; i >= 0; i--) {
    var swatch = swatches[i];
    if (swatch.name.indexOf("[Registration]") == -1 &&
        swatch.name.indexOf("None") == -1) {
        swatch.remove();
    }
}
```

**Flatten Transparency:**
```javascript
var doc = app.activeDocument;
var selected = doc.selection;
for (var i = 0; i < selected.length; i++) {
    app.executeMenuCommand("Flatten Transparency");
}
```

**Expand All:**
```javascript
// Expand appearance, strokes, fills
app.executeMenuCommand("Expand Appearance");
app.executeMenuCommand("Expand Gradient");
app.executeMenuCommand("Expand锦绣");
```
