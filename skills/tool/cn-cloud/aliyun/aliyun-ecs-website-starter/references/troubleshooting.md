# Troubleshooting

## 8.1 连接问题

### 8.1.1 SSH无法连接服务器

**排查步骤:**
1. 确认服务器状态是"运行中"
2. 检查安全组是否放行了22端口
3. 确认本地网络没有防火墙阻断

```bash
# 本地测试端口连通性
telnet 服务器IP 22
# 或
nc -zv 服务器IP 22

# Windows使用PowerShell
Test-NetConnection 服务器IP -Port 22
```

**解决方案:**
- 安全组添加入方向规则: TCP 22端口 0.0.0.0/0
- 重置实例密码(控制台 → 实例 → 更多 → 密码/密钥 → 重置密码)
- 使用VNC登录(控制台 → 实例 → 更多 → 远程连接 → VNC登录)

### 8.1.2 宝塔面板打不开

**症状:** http://服务器IP:8888 无法访问

**排查步骤:**
1. 确认宝塔面板服务是否启动
2. 检查8888端口是否被防火墙拦截
3. 确认安全组已放行8888端口

```bash
# SSH登录后检查宝塔状态
bt status
# 如果未运行
bt start

# 查看端口监听
netstat -tlnp | grep 8888

# 重启宝塔服务
bt restart
```

**解决方案:**
- 安全组放行: TCP 8888端口
- 云防火墙放行: 8888端口
- 修改宝塔面板端口: `bt` → 16 → 修改端口

## 8.2 宝塔使用问题

### 8.2.1 数据库连接失败

**排查步骤:**
1. 确认MySQL服务是否运行(宝塔面板 → 服务 → MySQL)
2. 检查phpMyAdmin是否正常访问
3. 确认数据库用户名密码正确

**常见错误:**
- "Access denied" → 用户名密码错误
- "Can't connect to MySQL server" → MySQL服务未启动
- "Unknown database" → 数据库名错误

### 8.2.2 网站显示502 Bad Gateway

**原因:** Nginx/Apache未启动或上游服务异常

**解决方案:**
```bash
# 重启Nginx
bt restart
# 或在宝塔面板: 软件商店 → Nginx → 重启
```

**完整排查:**
1. 确认PHP版本与网站兼容
2. 检查PHP-FPM是否运行
3. 查看错误日志: /www/wwwlogs/

## 8.3 建站问题

### 8.3.1 WordPress固定链接404

**原因:** 伪静态规则未配置

**解决方案:**
1. 宝塔面板 → 网站 → 点击网站 → 设置 → 伪静态
2. 选择"wordpress"规则 → 保存
3. Nginx需重载配置

```nginx
location / {
    try_files $uri $uri/ /index.php?$args;
}
```

### 8.3.2 上传文件大小限制

**原因:** PHP上传限制默认2-8MB

**解决方案:**
宝塔面板 → PHP版本 → 配置修改:
```
upload_max_filesize = 100M
post_max_size = 100M
max_execution_time = 300
```
然后重载PHP配置

## 8.4 SSL证书问题

### 8.4.1 Let's Encrypt证书申请失败

**常见原因:**
- 域名未解析到服务器IP
- 端口80/443被占用
- DNS验证配置错误

**解决方案:**
1. 确认域名已正确解析到服务器
2. 关闭占用80端口的程序
3. 尝试使用DNS验证方式申请
