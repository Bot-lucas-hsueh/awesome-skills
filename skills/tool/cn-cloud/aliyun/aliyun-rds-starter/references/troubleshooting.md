# Troubleshooting

## 8.1 连接问题

### 8.1.1 无法连接RDS

**症状:** ERROR 2003 (HY000): Can't connect to MySQL server

**排查步骤:**
1. 确认RDS状态是"运行中"
2. 检查白名单设置
3. 确认连接地址正确

```bash
mysql -h rm-xxxxx.mysql.rds.aliyuncs.com -P 3306 -u username -p

# 常见错误:
# ERROR 2003: 白名单未包含本地IP或网络不通
# ERROR 1045: 用户名密码错误
# ERROR 1044: 该账号无权访问该数据库
```

**解决方案:**
- 白名单添加: 0.0.0.0/0 (测试环境) 或 本地公网IP
- 内网访问: 确保ECS与RDS在同一VPC
- 外网访问: 开启RDS外网地址

### 8.1.2 连接数过多

**症状:** ERROR 1040: Too many connections

**解决方案:**
- 检查是否有连接未关闭
- 修改max_connections参数
- 重启应用连接池
- 升级RDS规格

## 8.2 性能问题

### 8.2.1 查询慢

**排查:**
```sql
-- 查看当前连接
SHOW PROCESSLIST;

-- 查看慢查询日志
SHOW variables LIKE 'slow_query_log%';
SHOW variables LIKE 'long_query_time%';

-- 查看索引使用情况
SHOW INDEX FROM your_table;

-- 分析查询
EXPLAIN SELECT * FROM your_table WHERE column = 'value';
```

**解决方案:**
- 添加合适的索引
- 优化SQL语句
- 使用读写分离分担负载
- 开启查询缓存(MySQL 5.7)

### 8.2.2 磁盘空间不足

**症状:** ERROR 1062 (23000): Duplicate entry 或 表损坏

**解决方案:**
```sql
-- 查看数据库大小
SELECT table_schema, SUM(data_length + index_length) / 1024 / 1024 AS MB
FROM information_schema.tables
GROUP BY table_schema;

-- 清理Binlog
PURGE BINARY LOGS BEFORE '2024-01-01 00:00:00';
```

## 8.3 备份恢复问题

### 8.3.1 自动备份失败

**排查:**
1. 检查备份存储空间是否充足
2. 查看备份任务的执行日志
3. 确认备份时间段设置合理

**解决方案:**
- 手动执行一次备份
- 调整备份时间到业务低峰期
- 检查实例状态是否正常

### 8.3.2 恢复数据失败

**原因:** 备份文件损坏或实例状态异常

**解决方案:**
```bash
# 下载备份文件
# 控制台 → 数据库备份 → 下载备份

# 使用mysqldump恢复
mysql -h rm-xxxxx.mysql.rds.aliyuncs.com -u username -p dbname < backup.sql
```

## 8.4 高可用问题

### 8.4.1 主从切换

**症状:** 应用短暂连接失败

**原因:** RDS高可用版自动进行主从切换

**解决方案:**
- 使用RDS连接地址(自动解析到新主库)
- 应用添加重连机制
- 确认连接超时设置合理
