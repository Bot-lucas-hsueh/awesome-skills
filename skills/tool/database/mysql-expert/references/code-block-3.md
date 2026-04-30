# sql Example

```
-- Primary configuration
[mysqld]
server-id = 1
log-bin = mysql-bin
binlog_format = ROW
binlog_row_image = FULL
gtid_mode = ON
enforce_gtid_consistency = ON
sync_binlog = 1
innodb_flush_log_at_trx_commit = 1

-- Replica configuration
[mysqld]
server-id = 2
relay-log = relay-bin
read_only = ON
super_read_only = ON
log_replica_updates = ON
replica_parallel_workers = 4
replica_parallel_type = LOGICAL_CLOCK

-- GTID-based replication
CHANGE REPLICATION SOURCE TO
    SOURCE_HOST = 'primary-host',
    SOURCE_USER = 'replication_user',
    SOURCE_PASSWORD = 'password',
    SOURCE_AUTO_POSITION = 1;
```
