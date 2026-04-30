# Troubleshooting

## 8.1 安装问题

### 8.1.1 宝塔安装失败

**症状:** 安装脚本报错或长时间无响应

**排查步骤:**
```bash
# 查看系统版本
cat /etc/os-release

# 确认Python版本
python --version
# 宝塔需要Python 2.7或3.x

# 检查端口是否被占用
netstat -tlnp | grep -E "8888|888|80|443"
```

**解决方案:**
- CentOS 7.x执行: `yum update && yum install -y wget`
- Ubuntu执行: `apt update && apt install -y wget`
- 国内服务器使用阿里云镜像安装

### 8.1.2 忘记宝塔面板密码

**解决方案:**
```bash
# 重置面板密码
bt 5
# 输入新密码

# 或重置所有面板设置
bt 8
```

## 8.2 性能问题

### 8.2.1 面板响应慢

**原因:** 内存不足，swap未开启

**解决方案:**
```bash
# 查看内存使用
free -m

# 开启swap
dd if=/dev/zero of=/swap bs=1M count=1024
mkswap /swap
swapon /swap
echo "/swap swap swap defaults 0 0" >> /etc/fstab
```

### 8.2.2 PHP-FPM占用内存高

**解决方案:**
宝塔面板 → PHP版本 → 设置 → 配置修改:
```
pm.max_children = 30
pm.start_servers = 5
pm.min_spare_servers = 5
pm.max_spare_servers = 20
```

## 8.3 安全问题

### 8.3.1 面板被扫描/攻击

**症状:** 大量登录失败日志

**解决方案:**
- 修改默认面板端口(8888)
- 设置强密码，定期更换
- 开启SSH密钥登录
- 安装[安全日志插件]监控登录

```bash
# 禁用密码登录SSH
sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
systemctl restart sshd
```

## 8.4 网站问题

### 8.4.1 网站打不开

**排查步骤:**
1. 检查网站服务状态(Nginx/Apache)
2. 查看网站错误日志
3. 检查配置语法

```bash
# 检查Nginx
nginx -t
systemctl status nginx

# 查看错误日志
tail -100 /www/wwwlogs/yourdomain.com.error.log
```

### 8.4.2 502 Bad Gateway

**原因:** 上游服务(PHP-FPM)未启动

**解决方案:**
```bash
# 重启PHP-FPM
systemctl restart php-fpm-74  # 对应PHP版本

# 或在宝塔中操作
# 宝塔 → 软件商店 → PHP → 重启
```
