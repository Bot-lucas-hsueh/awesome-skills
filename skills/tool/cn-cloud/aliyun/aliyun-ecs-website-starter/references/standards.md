# Standards & Reference

## 7.1 Official Documentation

- [轻量应用服务器文档](https://help.aliyun.com/zh/simple-application-server)
- [建站最佳实践](https://help.aliyun.com/zh/simple-application-server/getting-started/building-a-website)
- [WordPress建站教程](https://help.aliyun.com/zh/simple-application-server/getting-started/deploy-wordpress)

## 7.2 轻量服务器规格

### 7.2.1 可选配置

| 套餐 | CPU | 内存 | 带宽 | 流量包 | SSD | 价格 |
|------|-----|------|------|--------|-----|------|
| 入门型 | 1核 | 1GB | 30Mbps | 1TB | 40GB | ¥24/月 |
| 基础型 | 1核 | 2GB | 30Mbps | 2TB | 60GB | ¥48/月 |
| 通用型 | 2核 | 4GB | 50Mbps | 3TB | 100GB | ¥88/月 |

### 7.2.2 镜像类型

| 镜像 | 操作系统 | 预装软件 |
|------|---------|---------|
| 应用镜像 | CentOS/Ubuntu | 宝塔面板/LAMP/LNMP |
| WordPress | Ubuntu/CentOS | WordPress+宝塔 |
| Node.js | Ubuntu | Node.js环境 |
| 官方系统镜像 | CentOS/Debian/Ubuntu | 仅系统 |

## 7.3 常用端口

| 端口 | 用途 | 防火墙 |
|------|------|--------|
| 22 | SSH远程连接 | 默认开放 |
| 80 | HTTP网站 | 需手动开放 |
| 443 | HTTPS网站 | 需手动开放 |
| 3389 | Windows RDP | 默认关闭 |
| 8888 | 宝塔面板 | 默认开放 |
| 21 | FTP | 需手动开放 |

## 7.4 宝塔面板安装命令

```bash
# CentOS
yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh && sh install.sh

# Ubuntu/Debian
wget -O install.sh http://download.bt.cn/install/install-ubuntu_6.0.sh && sudo bash install.sh

# 安装完成后访问: http://服务器IP:8888/bt-panel
```

## 7.5 WordPress伪静态规则

```nginx
location / {
    try_files $uri $uri/ /index.php?$args;
}

location ~ \.php$ {
    fastcgi_pass unix:/tmp/php-cgi.sock;
    fastcgi_index index.php;
    include fastcgi_params;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
}
```
