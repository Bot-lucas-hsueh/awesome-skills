# Standards & Reference

## 7.1 Official Documentation

- [腾讯云域名控制台](https://console.cloud.tencent.com/domain)
- [DNSPod文档](https://docs.dnspod.cn)
- [SSL证书控制台](https://console.cloud.tencent.com/ssl)
- [免费证书申请](https://cloud.tencent.com/document/product/400/6814)

## 7.2 域名注册

### 7.2.1 常用域名后缀

| 后缀 | 首年价格 | 续费价格 | 说明 |
|------|---------|---------|------|
| .com | ¥55 | ¥60 | 全球最常用 |
| .cn | ¥18 | ¥35 | 中国域名 |
| .net | ¥58 | ¥68 | 网络服务 |
| .org | ¥58 | ¥68 | 组织机构 |
| .cc | ¥38 | ¥120 | 短域名 |
| .vip | ¥28 | ¥50 | 会员专用 |

### 7.2.2 实名认证

| 主体类型 | 个人所需材料 | 企业所需材料 |
|---------|------------|-------------|
| 个人 | 身份证正反面 | 营业执照+法人身份证 |

## 7.3 DNSPod解析

### 7.3.1 记录类型

| 记录类型 | 用途 | 典型值 |
|---------|------|--------|
| A | IPv4地址 | 1.2.3.4 |
| AAAA | IPv6地址 | 2001:db8::1 |
| CNAME | 域名别名 | www.yourdomain.com → yourdomain.com |
| MX | 邮件交换 | 10 mail.yourdomain.com |
| TXT | SPF/验证 | v=spf1 include:spf.mailcloud.com ~all |
| NS | 域名服务器 | f1g1ns1.dnspod.net |

### 7.3.2 TTL设置

| 值 | 适用场景 | 生效时间 |
|------|---------|---------|
| 600 | 常规记录 | ~10分钟 |
| 120 | 频繁变更 | ~2分钟 |
| 3600 | 长期稳定 | ~1小时 |

## 7.4 SSL证书

### 7.4.1 免费证书

| 项目 | 限制 |
|------|------|
| 证书数量 | 同一主体50个 |
| 有效期 | 1年 |
| 支持类型 | DV单域名 |
| 验证方式 | DNS验证/文件验证 |

### 7.4.2 申请流程

```
1. 进入SSL证书控制台
2. 选择"免费证书" → "DV单域名"
3. 填写域名信息
4. 选择验证方式(DNS验证推荐)
5. 添加DNS记录
6. 等待CA签发(5-30分钟)
7. 下载证书
```

## 7.5 DNS API

```python
from tencentcloud.common import credential
from tencentcloud.dnspod.v20210323 import dnspod_client

cred = credential.Credential("SecretId", "SecretKey")
client = dnspod_client.DnspodClient(cred, "")

# 添加记录
client.DescribeDomainList(cred, "")
```
