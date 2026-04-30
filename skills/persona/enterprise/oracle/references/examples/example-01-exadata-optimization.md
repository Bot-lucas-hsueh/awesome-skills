# Example 1: Exadata Performance Optimization

## Context

Global financial institution running high-frequency trading analytics on Oracle
Database, experiencing I/O bottlenecks during market hours.

## Current Architecture Issues

```
┌─────────────────────────────────────────────┐
│           Before: Commodity Storage         │
├─────────────────────────────────────────────┤
│  Database Server ──► SAN Storage            │
│  100K IOPS           50K IOPS (bottleneck)  │
│  High CPU wait                              │
└─────────────────────────────────────────────┘
```

## Exadata Solution

```
┌─────────────────────────────────────────────────────────────┐
│                   Exadata X9M-2 Quarter Rack                │
├─────────────────────────────────────────────────────────────┤
│                    Database Servers                          │
│              (2x Intel Xeon, 64 cores each)                  │
├─────────────────────────────────────────────────────────────┤
│                    InfiniBand/RoCE                          │
│               (100 Gbps, sub-microsecond)                    │
├─────────────────────────────────────────────────────────────┤
│                    Storage Servers                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Flash Cache │  │  Smart Flash │  │   PMEM       │      │
│  │   (PCIe 4.0) │  │   Logging    │  │   (Intel)    │      │
│  │   12.8TB     │  │              │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
├─────────────────────────────────────────────────────────────┤
│              Storage Offloading (Smart Scan)                 │
│       WHERE, SELECT, JOIN pushed to storage layer           │
└─────────────────────────────────────────────────────────────┘
```

## Implementation

### Step 1: Storage Index Optimization

```sql
-- Create storage indexes on frequently filtered columns
ALTER TABLE trades STORAGE(BUFFER_POOL KEEP);

-- Partition by trading date for partition pruning
CREATE TABLE trades (
    trade_id NUMBER,
    trade_date DATE,
    symbol VARCHAR2(20),
    quantity NUMBER,
    price NUMBER,
    trader_id NUMBER
) PARTITION BY RANGE (trade_date) (
    PARTITION p2024q1 VALUES LESS THAN (TO_DATE('2024-04-01','YYYY-MM-DD')),
    PARTITION p2024q2 VALUES LESS THAN (TO_DATE('2024-07-01','YYYY-MM-DD')),
    PARTITION p2024q3 VALUES LESS THAN (TO_DATE('2024-10-01','YYYY-MM-DD')),
    PARTITION p2024q4 VALUES LESS THAN (TO_DATE('2025-01-01','YYYY-MM-DD'))
) COMPRESS FOR ARCHIVE HIGH;
```

### Step 2: Smart Scan Optimization

```sql
-- Enable Smart Scan (default on Exadata)
ALTER SESSION SET CELL_OFFLOAD_PROCESSING = TRUE;

-- Verify Smart Scan is being used
SELECT sql_id,
       sql_text,
       ROUND(io_cell_offload_eligible_bytes/1024/1024/1024, 2) as offload_gb,
       ROUND(io_interconnect_bytes/1024/1024/1024, 2) as interconnect_gb
FROM v$sql
WHERE sql_text LIKE '%trades%'
ORDER BY io_cell_offload_eligible_bytes DESC;

-- Expected output:
-- SQL_ID        SQL_TEXT              OFFLOAD_GB  INTERCONNECT_GB
-- ------------- --------------------- ----------- ---------------
-- a1b2c3d4e5f6  SELECT * FROM trades  1250.50     45.20
-- Offload efficiency: 96.4% (data filtered at storage)
```

### Step 3: Flash Cache Configuration

```sql
-- Pin critical tables in flash cache
ALTER TABLE trades STORAGE(CELL_FLASH_CACHE KEEP);
ALTER TABLE market_data STORAGE(CELL_FLASH_CACHE KEEP);

-- Monitor flash cache effectiveness
SELECT object_name,
       cell_flash_hits,
       cell_flash_misses,
       ROUND(cell_flash_hits / (cell_flash_hits + cell_flash_misses) * 100, 2) as hit_ratio
FROM v$cell_global_display
WHERE object_name IN ('TRADES', 'MARKET_DATA');

-- Expected: >95% hit ratio for hot data
```

### Step 4: Resource Management

```sql
-- Create consumer groups for workload prioritization
BEGIN
    DBMS_RESOURCE_MANAGER.create_consumer_group(
        consumer_group => 'HIGH_FREQ_TRADING',
        comment => 'Ultra-low latency trading queries'
    );
    
    DBMS_RESOURCE_MANAGER.create_consumer_group(
        consumer_group => 'REPORTING',
        comment => 'End-of-day reporting'
    );
END;
/

-- Map users to consumer groups
BEGIN
    DBMS_RESOURCE_MANAGER.set_initial_consumer_group(
        user => 'TRADING_APP',
        consumer_group => 'HIGH_FREQ_TRADING'
    );
END;
/

-- Create resource plan
BEGIN
    DBMS_RESOURCE_MANAGER.create_plan(
        plan => 'TRADING_PLAN',
        comment => 'Trading workload prioritization'
    );
    
    DBMS_RESOURCE_MANAGER.create_plan_directive(
        plan => 'TRADING_PLAN',
        group_or_subplan => 'HIGH_FREQ_TRADING',
        mgmt_p1 => 80,
        active_sess_pool_p1 => 50,
        max_est_exec_time => 1
    );
    
    DBMS_RESOURCE_MANAGER.create_plan_directive(
        plan => 'TRADING_PLAN',
        group_or_subplan => 'REPORTING',
        mgmt_p2 => 20,
        active_sess_pool_p1 => 10,
        max_est_exec_time => 3600
    );
END;
/
```

## Performance Results

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| **Average Query Time** | 245ms | 12ms | 95% faster |
| **Peak IOPS** | 50K | 2.5M | 50x increase |
| **Throughput** | 2.1 GB/s | 150 GB/s | 71x increase |
| **CPU Utilization** | 85% | 35% | 59% reduction |
| **Storage Offload** | 0% | 96% | Full Smart Scan |

## SQL Monitoring

```sql
-- Monitor Exadata-specific metrics
SELECT snap_time,
       physical_read_requests_delta as reads,
       physical_read_bytes_delta / 1024 / 1024 / 1024 as read_gb,
       io_offload_return_bytes_delta / 1024 / 1024 / 1024 as offload_gb,
       ROUND(io_offload_return_bytes_delta / physical_read_bytes_delta * 100, 2) as offload_pct
FROM dba_hist_seg_stat
WHERE obj# = (SELECT object_id FROM dba_objects WHERE object_name = 'TRADES')
ORDER BY snap_time DESC
FETCH FIRST 24 ROWS ONLY;
```

## Key Learnings

1. **Storage Offloading is Critical**: 96% of data filtering happens at storage layer
2. **Flash Cache Performance**: Keep hot data in PCIe flash for sub-millisecond latency
3. **Partition Pruning**: Combined with storage indexes, enables massive I/O reduction
4. **Resource Management**: Prioritize latency-sensitive workloads during market hours

---

*Example Version: 5.0.0*
