# Troubleshooting

## 8.1 域名解析问题

### 8.1.1 DNS解析不生效

**排查步骤:**
1. 检查域名是否已完成实名认证
2. 确认DNS服务器已修改为DNSPod
3. 等待DNS传播(最长48小时)

```bash
# 检查DNS服务器
whois yourdomain.com | grep "Name Server"

# 本地测试
nslookup yourdomain.com 119.29.29.29
dig yourdomain.com @f1g1ns1.dnspod.net

# 查看解析记录
# DNSPod控制台 → 域名解析 → 查看记录列表
```

### 8.1.2 CNAME冲突

**症状:** 无法同时配置MX和CNAME

**原因:** DNS规范不允许MX记录指向CNAME

**解决方案:**
- MX记录使用A记录指向IP
- 或将邮件服务迁移到其他子域名

## 8.2 SSL证书问题

### 8.2.1 证书申请失败

**常见原因:**
- 域名未完成实名认证
- DNS验证记录未生效
- 域名被CA拉黑

**解决方案:**
```bash
# 确认域名实名认证
whois yourdomain.com | grep "Registrant Name"

# 验证TXT记录
nslookup -qt=txt _dnsauth.yourdomain.com 119.29.29.29
```

### 8.2.2 证书链不完整

**解决方案:**
- 下载完整的证书链(中间证书+根证书)
- Nginx配置添加完整证书链

## 8.3 HTTPS问题

### 8.3.1 HTTPS无法访问

**排查:**
```bash
# 检查443端口是否开放
telnet yourdomain.com 443

# 检查防火墙规则
# 腾讯云控制台 → 安全组 → 出/入站规则
```

**解决方案:**
- 安全组开放443端口
- 云防火墙放行443端口
