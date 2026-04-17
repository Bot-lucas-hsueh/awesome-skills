# Troubleshooting

## 8.1 连接问题

### 8.1.1 SSH无法连接

**排查步骤:**
```bash
# 检查服务器状态
# 腾讯云控制台 → 轻量应用服务器 → 状态

# 检查防火墙
# 防火墙 → 查看22端口是否放行

# 本地测试
ssh -v root@服务器IP
```

**解决方案:**
- 防火墙放行22端口
- 重置密码: 控制台 → 远程登录 → 重置密码

### 8.1.2 宝塔面板打不开

**症状:** http://IP:8888 无法访问

**解决方案:**
```bash
# SSH登录后
bt status
bt start  # 启动服务

# 检查端口
netstat -tlnp | grep 8888

# 重装宝塔
bt 8  # 修复面板
```

## 8.2 网站问题

### 8.2.1 WordPress后台慢

**解决方案:**
- 安装缓存插件: W3 Total Cache / WP Super Cache
- 使用Redis对象缓存
- 优化图片: 使用TinyPNG压缩

### 8.2.2 固定链接404

**解决方案:**
宝塔 → 网站 → 设置 → 伪静态 → 选择wordpress

```nginx
location / {
    try_files $uri $uri/ /index.php?$args;
}
```

## 8.3 SSL问题

### 8.3.1 Let's Encrypt申请失败

**原因:** 80端口被占用或域名未解析

**解决方案:**
```bash
# 确认域名已解析到服务器IP
nslookup yourdomain.com

# 检查80端口
netstat -tlnp | grep :80
```
