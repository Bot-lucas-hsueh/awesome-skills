# Troubleshooting

## 8.1 小程序云开发问题

### 8.1.1 云数据库权限错误

**症状:** "权限不足"或数据读取失败

**排查:**
```javascript
// 检查集合权限配置
// 微信开发者工具 → 云开发控制台 → 数据库 → 选择集合 → 权限设置

// 常见权限配置
{
  "read": true,           // 所有用户可读
  "write": "doc._openid == auth.openid"  // 仅创建者可写
}
```

**解决方案:**
- 使用数据库引导(安全规则)
- 服务端调用云函数(函数有管理员权限)
- 设置正确的权限表达式

### 8.1.2 云函数调用失败

**排查:**
```javascript
// 云函数日志
// 云开发控制台 → 云函数 → 日志 → 选择函数查看

// 检查函数代码
exports.main = async (event, context) => {
    try {
        // 代码逻辑
    } catch (e) {
        console.error('错误:', e)
        return { error: e.message }
    }
}
```

## 8.2 云存储问题

### 8.2.1 文件上传失败

**原因:** 存储权限未配置

**解决方案:**
```javascript
// 检查存储权限设置
// 云开发控制台 → 存储 → 权限设置

// 推荐配置: 允许所有用户上传
{
  "addVoiceOnly": true,
  "addVideoOnly": true,
  "addImageOnly": true,
  "addFileOnly": true,
  "downloadFile": true
}
```

### 8.2.2 下载URL为空

**排查:**
```javascript
const cloud = require('wx-server-sdk')
cloud.init()

const fileID = 'cloud://xxx/xxx.jpg'

// 获取临时链接
const result = await cloud.downloadFile({
    fileID: fileID
})
console.log(result.fileID, result.tempFileURL)
```

## 8.3 用户登录问题

### 8.3.1 自定义登录失败

**排查:**
1. 检查匿名登录是否开启
2. 确认邮箱密码登录配置
3. 查看登录日志

**解决方案:**
- 在云开发控制台 → 设置 → 登录设置中配置
- 确保anonymous_access_enabled为true(匿名登录)
