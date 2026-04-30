# code Example

```
┌─────────────────────────────────────────────────────────┐
│              INNODB ARCHITECTURE                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Row Storage                                            │
│  ├── Clustered primary key index                       │
│  ├── Secondary indexes point to PK                    │
│  ├── Variable-length columns stored off-page           │
│  └── COMPACT vs DYNAMIC row format                     │
│                                                         │
│  Tablespaces                                            │
│  ├── System tablespace (ibdata1)                       │
│  ├── File-per-table (default in 5.6+)                  │
│  ├── General tablespace                                │
│  └── Undo tablespace                                   │
│                                                         │
│  Buffer Pool                                            │
│  ├── LRU eviction policy                               │
│  ├── Change buffer for secondary indexes              │
│  └── Adaptive hash index                               │
│                                                         │
│  Transaction Log                                        │
│  ├── Redo log (ib_logfile0/1)                         │
│  └── Undo segments                                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```
