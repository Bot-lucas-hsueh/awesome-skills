# Glossary

## 9.1 SSL证书术语

| 术语 | 定义 |
|------|------|
| SSL | Secure Sockets Layer，安全套接层 |
| TLS | Transport Layer Security，TLS是SSL的升级版 |
| HTTPS | HTTP over SSL/TLS，加密HTTP |
| 证书 | 包含公钥和身份信息的数字文件 |
| 私钥 | 与证书配对的密钥，用于解密 |

## 9.2 证书类型

| 术语 | 定义 |
|------|------|
| DV | Domain Validation，域名验证型 |
| OV | Organization Validation，组织验证型 |
| EV | Extended Validation，增强验证型(绿色地址栏) |
| 通配符 | 绑定主域名及其所有子域名 |
| SAN | Subject Alternative Name，支持多个域名 |

## 9.3 验证方式

| 术语 | 定义 |
|------|------|
| DNS验证 | 通过添加TXT记录验证域名所有权 |
| 文件验证 | 在网站根目录放置验证文件 |
| 自动验证 | 云服务自动完成验证流程 |

## 9.4 Nginx相关

| 术语 | 定义 |
|------|------|
| ssl_certificate | 服务器证书配置指令 |
| ssl_certificate_key | 私钥文件路径 |
| ssl_protocols | 支持的TLS版本 |
| ssl_ciphers | 支持的加密算法 |
| HSTS | HTTP Strict Transport Security，强制HTTPS |
