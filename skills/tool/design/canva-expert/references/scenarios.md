# Scenario Examples

## 9.1 Project Scenarios

### Scenario 1: Multi-Platform Social Media Campaign

**User:** "I need to create content for Instagram, Facebook, and LinkedIn for a product launch. How do I handle multiple sizes efficiently?"

**Expert:**
> **Solution:**
> 
> **Option A: Manual Resize (Canva Pro)**
> 1. Create design in one platform's dimensions (e.g., Instagram square 1080x1080)
> 2. Click "Resize" button in editor
> 3. Select multiple target sizes:
>    - Instagram Post (1080x1080)
>    - Instagram Story (1080x1920)
>    - Facebook Post (1200x630)
>    - LinkedIn Post (1200x627)
> 4. Enable "Magic Resize" to automatically adapt layout
> 5. Review and adjust each sized version
> 
> **Option B: Bulk Create**
> 1. Create one master design
> 2. Connect Google Sheet or CSV with content for each platform
> 3. Map fields: platform_name, headline, image_url
> 4. Generate all variations automatically
> 5. Download as ZIP with organized folders
> 
> **Key Tips:**
> - Lock key elements (logo, brand colors) before resizing
> - Review text placement in each size
> - Save as template for future campaigns

---

### Scenario 2: Brand Consistency for Team

**User:** "How do I ensure my team creates consistent branded content without going off-brand?"

**Expert:**
> **Solution:**
> 
> **1. Brand Kit Setup (Admin)**
> - Navigate to Brand Kit section
> - Add brand colors with hex codes (e.g., #1A73E8 for blue)
> - Upload brand fonts (TTF, OTF files)
> - Upload logo files (PNG with transparency, SVG for vectors)
> - Write brand guidelines in description
> 
> **2. Template Creation**
> - Create templates for each content type:
>   - Social media posts
>   - Presentations
>   - Email headers
>   - Print materials
> - Lock brand elements (logo position, fonts, colors)
> - Save as team template
> 
> **3. Team Training**
> - Share Brand Kit link with team
> - Show how to start from templates
> - Demonstrate locked vs. editable elements
> - Create quick-start guide
> 
> **Key Tips:**
> - Review templates quarterly for updates
> - Use folder permissions to control access
> - Set up folder-level Brand Kits for sub-teams if needed

---

### Scenario 3: Product Catalog Creation

**User:** "I need to create a 50-page product catalog. Is there a way to automate this?"

**Expert:**
> **Solution:**
> 
> **Using Bulk Create:**
> 1. **Prepare Data**
>    - Create Google Sheet with columns: product_name, description, price, image_url, SKU
>    - Include 50 rows (one per product)
>    - Upload product images to Canva
> 
> **2. Create Master Template**
>    - Design one product page layout
>    - Add text placeholders for name, description, price
>    - Add image placeholder
>    - Design page header/footer
> 
> **3. Connect Data**
>    - Click Apps > Bulk Create
>    - Connect Google Sheet or upload CSV
>    - Map each column to design element
> 
> **4. Generate**
>    - Preview first few pages
>    - Click Generate All
>    - Canva creates 50 individual pages
> 
> **5. Finalize**
>    - Review generated pages
>    - Download as single PDF or separate images
>    - Manually add any pages that need special treatment
> 
> **Key Tips:**
> - Keep template simple for bulk creation
> - Check for text overflow in preview
> - Save bulk data for future updates

## 9.2 Client Deliverables

### Social Media Package

| Item | Format | Sizes Included |
|------|--------|----------------|
| All Platform Graphics | PNG | 1080x1080, 1200x630, 1200x627, 1080x1920 |
| Highlight Covers | PNG | 1080x1920 |
| Profile Picture | PNG | 400x400 |
| Story Graphics | PNG | 1080x1920 |
| Source File | Canva | Original editable file |

### Print Marketing Package

| Item | Format | Specs |
|------|--------|-------|
| Business Cards | PDF Print | 3.5x2 inches, 3mm bleed, CMYK |
| Flyers | PDF Print | A5/A4, 3mm bleed, CMYK |
| Posters | PDF Print | A3/A2, 3mm bleed, CMYK |
| Brochures | PDF Print | Tri-fold, CMYK, with crop marks |
| Source Files | Canva | Original files with fonts |

### Presentation Package

| Item | Format | Details |
|------|--------|---------|
| Keynote/PPT | PPTX/PDF | All slides with animations |
| Slide Images | PNG | Individual slides as images |
| Speaker Notes | PDF | Notes extracted from slides |
| Source File | Canva | Editable presentation |

## 9.3 Automation

### Brand Kit Automation

**Setting up automated brand colors:**
```markdown
1. Open Brand Kit
2. Add colors with specific names (Primary, Secondary, Accent)
3. Use color picker or enter hex codes
4. Colors become available in design color picker
5. Team members can access from "Brand Colors" section
```

**Font upload workflow:**
```markdown
1. Go to Brand Kit > Fonts
2. Click "Upload a font"
3. Select TTF or OTF files
4. Set font role (Heading, Body, Accent)
5. Assign usage permissions
6. Fonts available to all team members
```

### Bulk Create Workflow

**Google Sheets Integration:**
```
Columns: name | headline | body_text | image | price
Row 1: Product A | Amazing Widget | High quality... | widget.jpg | $99
Row 2: Product B | Super Gadget | Latest technology... | gadget.jpg | $149

Mapping in Canva:
- name → Text element (Heading)
- headline → Text element (Subhead)
- body_text → Text element (Body)
- image → Image element
- price → Text element (Price)
```

### Design Automation Rules

| Rule | When Applied | Result |
|------|--------------|--------|
| Auto-lock elements | When marking as brand element | Prevents accidental edits |
| Auto-assign colors | When adding brand color | Consistent palette usage |
| Auto-apply fonts | When selecting from Brand Kit | Typography consistency |
| Auto-resize | When duplicating design | Optimizes for new platform |

### Scheduled Publishing (via Canva + Integrations)

1. **Connect Calendar App**
   - Browse Integrations
   - Connect Google Calendar or other

2. **Schedule Design**
   - Click Share > Schedule
   - Pick date and time
   - Select platform (Instagram, Facebook, etc.)

3. **Connect Social Account**
   - Authorize Canva to post
   - Select which account
   - Confirm posting

4. **Track Performance**
   - View scheduled posts in dashboard
   - Connect analytics for post metrics
   - Export scheduling reports

### API Integration (Enterprise)

```markdown
Canva Connect API enables:
- Programmatic design creation
- Automated template population
- Design asset management
- Team permission management
- Analytics integration

Use Cases:
- CRM integration for client deliverables
- E-commerce product image generation
- Automated report generation
- Custom design portals
```
