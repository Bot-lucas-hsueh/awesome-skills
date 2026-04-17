# Standards & Reference

## 7.1 Official Documentation

- [宝塔面板官网](https://www.bt.cn)
- [宝塔Linux面板文档](https://docs.bt.cn)
- [宝塔论坛](https://www.bt.cn/bbs)

## 7.2 功能模块

### 7.2.1 软件管理

| 分类 | 常用软件 | 用途 |
|------|---------|------|
| 网站 | Nginx/Apache/Tengine | Web服务器 |
| 数据库 | MySQL/PostgreSQL/Redis/MongoDB | 数据库服务 |
| PHP | PHP 7.4/8.0/8.1/8.2 | PHP运行环境 |
| FTP | Pure-Ftpd | 文件传输服务 |
| 存储 | OSSFS/SeaFile | 云存储/私有云 |

### 7.2.2 端口占用

| 端口 | 服务 | 说明 |
|------|------|------|
| 8888 | 宝塔面板 | 默认面板入口 |
| 888 | phpMyAdmin | 数据库管理 |
| 22 | SSH | 远程连接 |
| 21 | FTP | 文件传输 |
| 80/443 | Web | HTTP/HTTPS |

## 7.3 目录结构

```
/www/server/nginx      # Nginx安装目录
/www/server/apache     # Apache安装目录
/www/server/mysql      # MySQL安装目录
/www/server/php        # PHP安装目录
/www/wwwroot           # 网站根目录
/www/wwwlogs           # 网站日志目录
/www/backup            # 备份目录
/www/phpinfo           # PHP探针目录
/var/log               # 系统日志
```

## 7.4 常用操作

### 7.4.1 绑定宝塔账号

```bash
# 登录宝塔面板后，在"面板设置"中绑定宝塔账号
# 免费注册: https://www.bt.cn/register.html
```

### 7.4.2 常用命令行

```bash
# 重启Nginx
bt 12

# 重启MySQL
bt 9

# 查看面板日志
cat /www/server/panel/logs/error.log

# 修复面板
wget -O update.sh http://download.bt.cn/install/update.sh && bash update.sh
```

## 7.5 安全配置

| 项目 | 建议值 |
|------|--------|
| 面板端口 | 改为非8888 |
| 面板密码 | 强密码，定期更换 |
| SSH密码登录 | 关闭，改用密钥 |
| 防火墙规则 | 仅开放必要端口 |
| PHP禁用函数 | proc_exec, system等 |
