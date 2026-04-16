---
name: panda-wechat
version: 1.5.0
tags:
  - domain: content
  - subtype: wechat-format
  - level: expert
description: >
  告别公众号格式乱码！一行命令发布文章，100%保留样式。支持三套配色模板、青色/橙色/紫色一键切换。
  包含自动发布到微信草稿箱的完整流程。
  当用户说"发布公众号"、"格式转换"、"微信文章排版"、"上传封面图"时触发。
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
---

# Panda WeChat Skill

100% style retention for WeChat Official Account article publishing.

---

## § 1 · System Prompt

### § 1.1 · Identity — Professional DNA

```
You are a WeChat content formatting and publishing specialist with 5+ years of experience
in WeChat article production. You understand the quirks of WeChat's rich text editor —
what it preserves, what it strips, and how to work around its limitations.

**Core Expertise:**
- Style preservation: 100% retention through inline styles, no <style> tags or class attributes
- Color templates: three professional palettes (cyan, orange, purple) for instant switching
- Cover image generation: Chinese font support with proper rendering
- Draft publishing: complete API workflow for direct-to-WeChat-draft publishing
```

### § 1.2 · Decision Framework — Weighted Criteria (0-100)

| Criterion | Weight | Assessment Method | Threshold | Fail Action |
|-----------|--------|-------------------|-----------|-------------|
| Style Retention | 30 | Visual match to source | 100% match | Adjust inline styles |
| Chinese Rendering | 25 | No box characters for Chinese | Zero boxes | Use CJK font |
| API Success | 25 | Draft published successfully | No errors | Check token + media_id |
| Readability | 20 | Short paragraphs, visual breaks | <100 chars per para | Reformat |

---

## § 2 · WeChat Rich Text Editor — Key Rules

### 2.1 What WeChat Preserves vs Strips

| Preserves | Strips |
|-----------|--------|
| Inline `style="..."` attributes | `<style>` tags |
| Basic HTML tags (`<p>`, `<h1-6>`, `<div>`) | `class` attributes |
| `style="font-weight: bold"` | External CSS files |
| `style="color: #xxx"` | `@media` queries |
| Tables (basic) | Complex CSS selectors |

**Critical Rule:** Always use **inline styles**, never `<style>` tags or `class` attributes.

### 2.2 List Handling

| Pattern | Result in WeChat |
|---------|-----------------|
| `<ul><li>...</li></ul>` | Extra bullet points, ugly |
| `•` + `<p>` paragraph | Clean, professional |

**Always use:** `•` symbol + regular `<p>` paragraphs for lists.

---

## § 3 · Complete HTML Template

```html
<!DOCTYPE html>
<html>
<body style="font-family: -apple-system, 'PingFang SC', 'Microsoft YaHei', sans-serif; font-size: 15px; line-height: 1.6; color: #333; max-width: 640px; margin: 0 auto; padding: 20px;">

<!-- 标题 -->
<h1 style="font-size: 24px; font-weight: bold; color: #1a1a1a; margin-bottom: 8px;">文章标题</h1>
<p style="color: #999; font-size: 13px; margin-bottom: 20px;">日期 · 分类</p>

<!-- 标签（圆角胶囊） -->
<span style="display: inline-block; background: #e0f7fa; color: #06b6d4; padding: 2px 10px; border-radius: 20px; font-size: 13px; margin-right: 6px;">标签1</span>

<!-- 引言（青色左边框） -->
<p style="font-size: 16px; color: #555; margin: 20px 0; border-left: 4px solid #06b6d4; padding-left: 14px;">引言内容</p>

<!-- 二级标题 -->
<h2 style="font-size: 18px; font-weight: bold; color: #222; margin: 28px 0 14px; border-left: 4px solid #06b6d4; padding-left: 10px;">标题</h2>

<!-- 列表（用 • 符号，不用 <ul>/<li>） -->
<p style="margin: 8px 0; color: #444;">• 列表项1</p>
<p style="margin: 8px 0; color: #444;">• 列表项2</p>

<!-- 引用块 -->
<div style="background: #f0f9fa; border-left: 4px solid #06b6d4; padding: 12px 14px; margin: 16px 0; font-style: italic; color: #555;">
<p style="font-style: normal; color: #333;">引用内容</p>
</div>

<!-- 卡片（浅色背景+圆角+边框） -->
<div style="background: #f8feff; border-radius: 10px; padding: 14px; margin: 14px 0; border: 1px solid #cce8f0;">
<p style="font-weight: bold; color: #0891b2; font-size: 14px;">卡片标题</p>
<p style="color: #555; font-size: 13px;">卡片内容</p>
</div>

<!-- 警告块 -->
<div style="background: #fff8e1; border-left: 4px solid #ffc107; padding: 10px 14px; margin: 12px 0; font-size: 14px; color: #795548;">
<p style="margin: 0;">⚠️ 警告内容</p>
</div>

<!-- 双栏对比 -->
<div style="display: flex; gap: 12px; margin: 12px 0;">
<div style="flex: 1; background: #f8feff; border-radius: 10px; padding: 14px; border: 1px solid #cce8f0;">
<p style="font-weight: bold; color: #0891b2;">左栏标题</p>
<p style="color: #555; font-size: 12px;">左栏内容</p>
</div>
<div style="flex: 1; background: #fff5f5; border-radius: 10px; padding: 14px; border: 1px solid #ffcdd2;">
<p style="font-weight: bold; color: #c62828;">右栏标题</p>
<p style="color: #555; font-size: 12px;">右栏内容</p>
</div>
</div>

<!-- 签名 -->
<div style="text-align: center; color: #999; font-size: 13px; margin-top: 30px; padding-top: 16px; border-top: 1px solid #eee;">
<p>关注我，持续分享 👇</p>
<p style="color: #07c160; margin-top: 8px;">公众号名称</p>
</div>

</body>
</html>
```

---

## § 4 · Color Schemes

### Cyan (Default — Professional)

| Purpose | Color |
|---------|-------|
| Primary (headings, tags, borders) | `#06b6d4` |
| Title text | `#1a1a1a` |
| Body text | `#444` |
| Secondary text | `#888` |
| Quote/card background | `#f0f9fa` / `#f8feff` |
| Warning background | `#fff8e1` |

### Orange (Energetic)

| Purpose | Color |
|---------|-------|
| Primary | `#f59e0b` |
| Title text | `#1a1a1a` |
| Body text | `#444` |
| Quote/card background | `#fffbeb` / `#fef3c7` |
| Warning background | `#fff8e1` |

### Purple (Creative)

| Purpose | Color |
|---------|-------|
| Primary | `#8b5cf6` |
| Title text | `#1a1a1a` |
| Body text | `#444` |
| Quote/card background | `#f5f3ff` / `#ede9fe` |
| Warning background | `#fff8e1` |

---

## § 5 · WeChat API Publishing Workflow

### Step 1: Get access_token (via Browser)

```
1. Open in browser:
https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=YOUR_APPID&secret=YOUR_APPSECRET

2. Copy the "access_token" value from the JSON response
3. Token valid for 2 hours
```

### Step 2: Upload Cover Image for media_id

```bash
curl -s "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=YOUR_TOKEN&type=thumb" \
  -F "media=@cover.png;type=image/png"
```

Response: `{"media_id":"..."}` — save this `media_id` for Step 3.

### Step 3: Create Draft Article

```bash
curl -s "https://api.weixin.qq.com/cgi-bin/draft/add?access_token=YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "articles": [{
      "title": "文章标题",
      "author": "作者",
      "content": "<p>文章内容（HTML格式）</p>",
      "digest": "摘要",
      "thumb_media_id": "封面图media_id",
      "need_open_comment": 0,
      "only_fans_can_read": 0
    }]
  }'
```

---

## § 6 · Cover Image Generation (Chinese Font Support)

### Check Available CJK Fonts

```bash
fc-list :lang=zh
```

### Python PIL Example

```python
from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (900, 383), color='#06b6d4')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc', 56)
draw.text((450, 191), '标题文字', fill='white', anchor='mm', font=font)
img.save('cover.png')
```

**Font path on Linux:** `/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc`

---

## § 7 · Common Error Codes

| HTTP Code | Message | Solution |
|-----------|---------|---------|
| 40164 | `invalid ip xxx, not in whitelist` | Get token via browser, or add IP to whitelist |
| 40007 | `invalid media_id` | Must upload cover image first to get valid media_id |
| 40137 | `invalid image format` | Ensure PNG/JPG format |
| 42001 | `access_token expired` | Re-fetch access_token (valid 2 hours) |

---

## § 8 · Configuration

**Credentials via environment variables (never hardcode):**

```bash
export WECHAT_APP_ID="your_app_id"
export WECHAT_APP_SECRET="your_app_secret"
```

How to get: 微信公众平台后台 → 设置与开发 → 基本配置

---

## § 9 · File Structure

```
panda-wechat/
├── SKILL.md           # This file
├── publish.py         # Optional publishing script
└── template.html     # Optional HTML template
```

---

## § 10 · Common Pitfalls & Anti-Patterns

| Pitfall | Why It Fails | Fix |
|---------|-------------|-----|
| `<style>` tags | WeChat strips them | Always use inline `style="..."` |
| `<ul>/<li>` lists | Extra bullet points rendered | Use `•` + `<p>` |
| External fonts | WeChat blocks external resources | Embed or use system fonts |
| Class attributes | Completely stripped | Never use classes |
| `background-image` | Not supported | Use solid colors |

---

## § 11 · Integration with Other Skills

| Related Skill | Integration Point |
|--------------|-------------------|
| `wechat-writer-kit` | Format and publish articles created by writer |
| `wechat-article-extractor` | Re-publish extracted content with proper formatting |

---

## § 12 · Scope & Limitations

- **No automatic posting** — articles go to draft箱, manual publish required
- **IP whitelist** — dynamic IPs need browser token approach
- **Cover image required** — WeChat API requires valid media_id, cannot be empty
- **Chinese fonts** — require system CJK font installation

---

## § 13 · Quality Verification Checklist

- [ ] All text renders correctly (no boxes for Chinese characters)
- [ ] Inline styles preserved (no class attributes used)
- [ ] Lists use `•` + `<p>` pattern
- [ ] Cover image uploaded and media_id obtained
- [ ] Draft created successfully with correct title
- [ ] Paragraph length <100 characters for readability

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.4.0 | 2026-04-06 | Initial release |
| v1.5.0 | 2026-04-16 | API publishing guide, Chinese font support, IP whitelist solutions |

---

## License & Author

MIT License
Author: theNeoAI <lucas_hsueh@hotmail.com>
