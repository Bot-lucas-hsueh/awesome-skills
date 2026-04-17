# Standards & Reference

## 7.1 Official Documentation

- [RDS控制台](https://rdsnext.console.aliyun.com)
- [RDS产品文档](https://help.aliyun.com/zh/ads)
- [RDS API文档](https://help.aliyun.com/zh/ads/developer-reference/api-summary)
- [连接数据库](https://help.aliyun.com/zh/ads/user-guide/connect-to-an-apsaradb-rds-for-mysql-instance)

## 7.2 数据库类型与规格

### 7.2.1 支持的数据库引擎

| 引擎 | 版本 | 说明 |
|------|------|------|
| MySQL | 5.7/8.0 | 社区版/企业版 |
| PostgreSQL | 14/13/12/11 |
| SQL Server | 2019/2017/2012 | 企业/标准/Web版 |
| MariaDB | 10.3/10.6 |
| PolarDB | MySQL/PostgreSQL兼容 | 存算分离 |

### 7.2.2 RDS实例规格

| 规格族 | CPU/内存 | 适用场景 | 最大连接数 |
|--------|---------|---------|-----------|
| 通用型 | 2核4G起 | 中小型应用 | 2000 |
| 独享型 | 独享CPU和内存 | 核心业务 | 按规格 |
| 内存型 | 大内存配比 | 数据库密集 | 按规格 |
| 入门级 | 1核1G | 测试/学习 | 200 |

## 7.3 连接配置

### 7.3.1 连接地址类型

| 类型 | 说明 | 适用场景 |
|------|------|---------|
| 内网地址 | VPC内访问，延迟最低 | 生产环境 |
| 外网地址 | 需单独开启，有流量费 | 开发调试/临时 |
| 读写分离地址 | 自动读写分离 | 有读负载的场景 |
| 数据库代理地址 | 连接池/安全增强 | 高并发场景 |

### 7.3.2 连接参数

```bash
# MySQL连接示例
Host: rm-xxxxx.mysql.rds.aliyuncs.com
Port: 3306
Database: myapp
Username: myuser
Password: ****

# Java JDBC连接串
jdbc:mysql://rm-xxxxx.mysql.rds.aliyuncs.com:3306/myapp?useSSL=false
```

## 7.4 备份恢复标准

### 7.4.1 自动备份策略

| 设置项 | 推荐值 | 说明 |
|--------|--------|------|
| 备份频率 | 每天1次 | RDS自动执行 |
| 备份保留 | 7天 | 可配置7-730天 |
| 备份时间 | 低峰时段 | 建议02:00-06:00 |
| 日志备份 | 开启 | 恢复点精确 |

### 7.4.2 恢复能力

| 恢复方式 | RTO | RPO |
|---------|-----|-----|
| 按时间点恢复 | 30-60分钟 | 最近5分钟 |
| 按备份集恢复 | 10-30分钟 | 备份时刻 |
| 库表级恢复 | 5-15分钟 | 特定表 |

## 7.5 白名单配置

```sql
-- MySQL设置白名单(允许10.0.0.0/8网段)
SET rav_name = 'aliyun_db_rdp';
CALL mysql.rds_set_instance_flag('aliyun_db_rdp', 'ENABLE_IP_WHITELIST', '10.0.0.0/8', 'mask');
```
