---
name: wechat-publisher
version: 1.6.0
description: |
  告别公众号格式乱码！一行命令发布文章，100%保留样式。支持三套配色模板、青色/橙色/紫色一键切换。
  包含自动发布到微信草稿箱的完整流程。
---

# WeChat Publisher Skill

## 核心发现（2026-04-06 初版）
## 实战经验（2026-04-16 更新）
## 去敏更新（2026-04-16 v1.6.0）

---

## 一、微信公众号 API 发布实战经验（2026-04-16）

### 1.1 IP 白名单问题

**问题描述**：
- 妙搭云电脑使用动态 IP（阿里云），IP 会变化
- 微信公众号 API 调用需要 IP 在白名单中
- 服务器直接调用 API 会失败：`invalid ip 39.102.54.62, not in whitelist`

**解决方案**：

**方案 A：通过浏览器获取 access_token（推荐）**
```bash
# 在浏览器中打开以下 URL（替换 appid 和 secret）：
https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=你的AppID&secret=你的AppSecret

# 浏览器会返回 JSON 格式的 access_token
# 复制返回结果中的 access_token 值
```

**方案 B：配置 IP 白名单**
- 在公众号后台添加可能的 IP 地址
- 注意：服务器 IP 可能是动态的，需要添加多个可能的 IP
- 妙搭云电脑当前 IP：`39.102.54.62`、`39.97.255.102`（可能变化）

### 1.2 封面图生成（中文支持）

**问题描述**：
- 服务器默认字体不支持中文，导致生成的封面图文字是方块乱码
- 需要使用支持中文的字体

**解决方案**：
```bash
# 1. 先检查可用中文字体
fc-list :lang=zh

# 2. 推荐使用 Noto Sans CJK 字体
# 字体路径：/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc

# 3. Python PIL 示例代码
from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (900, 383), color='#06b6d4')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc', 56)
draw.text((450, 191), '标题文字', fill='white', anchor='mm', font=font)
img.save('cover.png')
```

### 1.3 草稿箱发布完整流程

**步骤 1：获取 access_token（通过浏览器）**
```
1. 浏览器打开：https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=你的AppID&secret=你的AppSecret
2. 复制返回的 access_token（有效期 2 小时）
```

**步骤 2：上传封面图获取 media_id**
```bash
# 使用 curl 上传图片
curl -s "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=你的TOKEN&type=thumb" \
  -F "media=@cover.png;type=image/png"

# 返回示例：
# {"media_id":"vMrq-mSP3SIFyZbOzk_6TkpzzT22KaGPI6r5tTivqFzaskMCnN_U5F4-54CQ38VU",...}
```

**步骤 3：创建草稿箱文章**
```bash
curl -s "https://api.weixin.qq.com/cgi-bin/draft/add?access_token=你的TOKEN" \
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

### 1.4 常见错误处理

| 错误码 | 错误信息 | 解决方案 |
|-------|---------|---------|
| 40164 | invalid ip not in whitelist | 通过浏览器获取 token，或添加 IP 到白名单 |
| 40007 | invalid media_id | 必须先上传封面图获取 media_id，不能为空 |
| 40137 | invalid image format | 图片格式问题，确保是 PNG/JPG 格式 |

---

## 二、微信公众号文章格式标准

### 2.1 格式保留关键

**微信公众号文章格式保留关键：**
- ❌ 微信编辑器过滤 `<style>` 标签
- ❌ 微信编辑器过滤 `class` 属性
- ✅ 微信编辑器保留**内联样式** `style="..."`
- ✅ 微信编辑器保留基础 HTML 标签

**列表格式关键：**
- ❌ 不用 `<ul>/<li>` 列表（会产生多余黑点）
- ✅ 用 `•` + 普通 `<p>` 段落

### 2.2 完整模板结构

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

## 三、配置（首次使用）

**安全提示：凭证通过环境变量传递，不要硬编码！**

```bash
export WECHAT_APP_ID="你的AppID"
export WECHAT_APP_SECRET="你的AppSecret"
```

获取方式：微信公众平台后台 → 设置与开发 → 基本配置

---

## 四、配色方案（固定风格）

| 用途 | 颜色 |
|------|------|
| 主色（标题、标签、边框） | #06b6d4（青色） |
| 标题文字 | #1a1a1a |
| 正文文字 | #444 |
| 次要文字 | #888 |
| 引用/卡片背景 | #f0f9fa / #f8feff |
| 警告背景 | #fff8e1 |
| 代码块背景 | #1a1a2e |
| 代码文字 | #a5f3fc |

---

## 五、文件结构

```
panda-wechat/
├── SKILL.md           # 本文档（已更新 v1.5.0）
├── publish.py         # 发布脚本（可选）
└── template.html     # 文章模板（可选）
```

---

## 六、注意事项

1. **封面图**：必须先上传到微信永久素材，获取 `media_id`，不能为空
2. **列表**：永远用 `•` + `<p>`，不用 `<ul>/<li>`
3. **行距**：固定 1.6
4. **段落间距**：正文 `margin: 12px 0`，列表 `margin: 8px 0`
5. **中文字体**：生成封面图时使用 `/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc`

---

## 七、版本历史

| 版本 | 日期 | 更新内容 |
|-----|------|---------|
| v1.4.0 | 2026-04-06 | 初版发布 |
| v1.5.0 | 2026-04-16 | 新增 API 发布实战经验、中文字体支持、IP 白名单解决方案 |
