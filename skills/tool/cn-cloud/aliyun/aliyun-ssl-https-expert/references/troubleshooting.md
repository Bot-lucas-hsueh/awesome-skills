# Troubleshooting

## 8.1 证书申请问题

### 8.1.1 DV证书申请失败

**症状:** 域名验证超时或失败

**排查步骤:**
1. 确认域名已在阿里云注册
2. 检查TXT记录是否已正确添加
3. 验证记录值是否与CA提供的一致

```bash
# 检查TXT记录
nslookup -qt=txt _acme-challenge.yourdomain.com 223.5.5.5

# 等待时间: DNS传播可能需要5-30分钟
```

**解决方案:**
- 使用DNS验证(推荐)，而非文件验证
- 等待足够时间让DNS生效
- 确认域名实名认证与申请者一致

### 8.1.2 证书状态"待验证"

**原因:** 验证记录未生效或记录值错误

**解决方案:**
```bash
# 查看具体的验证信息
# 控制台 → SSL证书 → 点击证书 → 验证信息

# 常见问题:
# 1. 多个证书同时申请同一域名
# 2. DNS记录被覆盖
# 3. 使用了代理/CDN导致验证失败
```

## 8.2 Nginx配置问题

### 8.2.1 HTTPS访问显示"连接不安全"

**症状:** 浏览器显示证书无效

**排查:**
```bash
# 检查证书是否正确安装
openssl s_client -connect yourdomain.com:443 -servername yourdomain.com

# 查看证书信息
openssl x509 -in /path/to/cert.pem -noout -text | grep -E "Issuer|Subject|Not Before|Not After"
```

**解决方案:**
- 确保证书链完整(包含中间证书)
- 确保证书与域名匹配
- 检查是否有多个SSL证书配置冲突

### 8.2.2 证书链不完整

**原因:** 只配置了服务器证书，未配置中间证书

**解决方案:**
```nginx
ssl_certificate /path/to/cert.pem;         # 服务器证书
ssl_certificate_key /path/to/key.pem;       # 私钥
ssl_trusted_certificate /path/to/ca-bundle.crt;  # 中间证书+根证书
```

### 8.2.3 混合内容警告

**症状:** HTTPS页面加载HTTP资源被阻止

**解决方案:**
```nginx
# 方案1: 强制所有资源HTTPS
add_header Content-Security-Policy "upgrade-insecure-requests";

# 方案2: 检查页面资源
# 使用浏览器F12 → Console查看具体是哪个资源
# 将所有 http:// 改为 https://
```

## 8.3 自动续期问题

### 8.3.1 Let's Encrypt证书到期未自动续期

**排查:**
```bash
# 检查certbot续期状态
certbot certificates
certbot renew --dry-run

# 查看cron任务
crontab -l | grep certbot
```

**解决方案:**
- 手动续期: `certbot renew`
- 检查自动续期cron: `0 0,12 * * * certbot renew`
- 确保80端口可访问(Let's Encrypt续期需http验证)
