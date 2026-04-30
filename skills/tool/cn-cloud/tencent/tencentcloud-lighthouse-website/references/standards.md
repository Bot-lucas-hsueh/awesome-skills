# Standards & Reference

## 7.1 Official Documentation

- [腾讯云轻量应用服务器](https://cloud.tencent.com/product/lighthouse)
- [Lighthouse文档](https://cloud.tencent.com/document/product/1207)
- [建站教程](https://cloud.tencent.com/document/product/1207/54362)

## 7.2 套餐配置

### 7.2.1 国内套餐

| 套餐 | CPU | 内存 | 带宽 | 流量 | SSD | 价格 |
|------|-----|------|------|------|-----|------|
| 入门型 | 1核 | 1GB | 30Mbps | 1TB | 20GB | ¥24/月 |
| 基础型 | 1核 | 2GB | 30Mbps | 2TB | 50GB | ¥48/月 |
| 通用型 | 2核 | 4GB | 50Mbps | 3TB | 80GB | ¥88/月 |
| 舒适型 | 2核 | 8GB | 50Mbps | 4TB | 100GB | ¥166/月 |

### 7.2.2 应用镜像

| 镜像 | 预装内容 | 适用场景 |
|------|---------|---------|
| WordPress | WordPress + 宝塔 | 博客/网站 |
| LNMP | Nginx + MySQL + PHP | PHP开发 |
| LAMP | Apache + MySQL + PHP | PHP开发 |
| Node.js | Node.js 18 LTS | Node.js应用 |
| Docker | Docker CE | 容器化部署 |

## 7.3 连接配置

### 7.3.1 SSH连接

```bash
ssh root@服务器IP
# 密码登录: 轻量应用服务器默认密码在控制台获取
# 密钥登录: 推荐使用SSH密钥对
```

### 7.3.2 常用端口

| 端口 | 用途 | 防火墙 |
|------|------|--------|
| 22 | SSH | 默认开放 |
| 80 | HTTP | 需手动开放 |
| 443 | HTTPS | 需手动开放 |
| 3389 | Windows RDP | 默认关闭 |
| 8888 | 宝塔面板 | 应用镜像默认开放 |

## 7.4 防火墙规则

```bash
# 在控制台或CLI中放行端口
# 查看防火墙规则
tencent cloud lighthouse DescribeFirewallRules

# 放行HTTP/HTTPS
# 控制台: 防火墙 → 添加规则 → 协议TCP + 端口80/443
```

## 7.5 WordPress配置

### 7.5.1 宝塔部署WordPress

```bash
# 1. 安装宝塔面板
yum install -y wget && wget -O install.sh https://download.bt.cn/install/install_6.0.sh && sh install.sh

# 2. 登录宝塔后一键部署WordPress
# 宝塔面板 → 网站 → 一键部署 → 填入域名

# 3. 配置伪静态(WordPress固定链接)
location / {
    try_files $uri $uri/ /index.php?$args;
}
```

### 7.5.2 SSL配置

```
控制台 → 域名管理 → 申请免费证书 → 下载Nginx格式证书 → 宝塔网站设置 → SSL → 上传证书
```
