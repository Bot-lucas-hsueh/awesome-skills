# Standards & Reference

## 7.1 Official Documentation

- [SSL证书控制台](https://yundun.console.aliyun.com)
- [SSL证书帮助](https://help.aliyun.com/zh/ssl-certificates)
- [证书申请流程](https://help.aliyun.com/zh/ssl-certificates/user-guide/apply-for-a-certificate)
- [Nginx配置指南](https://help.aliyun.com/zh/ssl-certificates/user-guide/install-the-ssl-tls-certificate-on-nginx-servers)

## 7.2 证书类型

### 7.2.1 证书等级对比

| 类型 | 验证级别 | 签发时间 | 适用场景 | 价格 |
|------|---------|---------|---------|------|
| DV | 域名验证 | 10分钟-2小时 | 个人/博客/测试 | 免费 |
| OV | 组织验证 | 1-3天 | 企业官网/内部系统 | ¥200+/年 |
| EV | 增强验证 | 3-7天 | 金融/电商/高信任 | ¥1000+/年 |

### 7.2.2 免费证书限制

| 项目 | 限制 |
|------|------|
| 证书数量 | 同一主体最多20个 |
| 域名数量 | 单证书最多100个SAN |
| 有效期 | 1年，到期自动续签 |
| 支持域名 | 主域名+子域名 |

## 7.3 Nginx配置标准

### 7.3.1 单证书配置

```nginx
server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    ssl_certificate /etc/nginx/cert/yourdomain.com.pem;
    ssl_certificate_key /etc/nginx/cert/yourdomain.com.key;
    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:50m;
    ssl_session_tickets off;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
    ssl_prefer_server_ciphers off;

    add_header Strict-Transport-Security "max-age=63072000" always;

    location / {
        root /var/www/html;
        index index.html;
    }
}
```

### 7.3.2 HTTP跳转HTTPS

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$host$request_uri;
}
```

## 7.4 Apache配置

```apache
<VirtualHost *:443>
    ServerName yourdomain.com
    DocumentRoot /var/www/html

    SSLEngine on
    SSLCertificateFile /etc/httpd/cert/yourdomain.com.pem
    SSLCertificateKeyFile /etc/httpd/cert/yourdomain.com.key
    SSLCertificateChainFile /etc/httpd/cert/ca-bundle.crt
</VirtualHost>
```

## 7.5 证书格式转换

```bash
# PEM转PFX
openssl pkcs12 -export -out certificate.pfx -inkey privateKey.key -in certificate.crt -certfile ca_bundle.crt

# PFX转PEM
openssl pkcs12 -in certificate.pfx -nodes -out certificate.pem

# 检查证书信息
openssl x509 -in certificate.pem -noout -text
```
