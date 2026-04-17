# Glossary

## 9.1 域名术语

| 术语 | 定义 |
|------|------|
| 域名 | 网站标识符，如yourdomain.com |
| WHOIS | 域名注册信息查询服务 |
| DNS | 域名系统，将域名解析为IP地址 |
| Registrar | 域名注册商 |
| 注册局 | 管理顶级域名的机构(如CNNIC管理.cn) |

## 9.2 DNS记录类型

| 记录类型 | 用途 | 示例 |
|---------|------|------|
| A记录 | 域名指向IPv4地址 | yourdomain.com → 1.2.3.4 |
| AAAA记录 | 域名指向IPv6地址 | yourdomain.com → 2001:db8::1 |
| CNAME | 域名别名，指向另一个域名 | www.yourdomain.com → yourdomain.com |
| MX记录 | 邮件服务器地址 | @yourdomain.com → mail.yourdomain.com |
| TXT记录 | 文本验证(SPF/DKIM) | @yourdomain.com → v=spf1 include:_spf.yourdomain.com ~all |
| NS记录 | 域名服务器 | yourdomain.com → ns1.alidns.com |
| PTR记录 | IP反向解析 | 4.3.2.1.in-addr.arpa → yourdomain.com |

## 9.3 备案术语

| 术语 | 定义 |
|------|------|
| ICP备案 | 中国互联网信息服务管理备案 |
| 备案主体 | 备案申请人(个人或企业) |
| 网站负责人 | 负责网站管理的人员 |
| 接入商 | 提供服务器接入服务的服务商 |
| 管局 | 通信管理局，负责最终审核 |
| 备案服务号 | ECS关联备案的必要凭证 |

## 9.4 SSL证书术语

| 术语 | 定义 |
|------|------|
| CSR | Certificate Signing Request，证书签名请求文件 |
| 证书链 | 从服务器证书到根证书的信任链 |
| DV证书 | Domain Validation，仅验证域名所有权 |
| OV证书 | Organization Validation，验证组织身份 |
| EV证书 | Extended Validation，增强验证，绿色地址栏 |
| 中间证书 | CA签发的中间层证书 |
