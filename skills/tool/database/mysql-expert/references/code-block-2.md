# code Example

```
┌─────────────────────────────────────────────────────────┐
│              DATA TYPE GUIDELINES                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Integers                                              │
│  ├── TINYINT (1 byte) - 127 / 255 unsigned             │
│  ├── SMALLINT (2 bytes) - 32K / 65K                    │
│  ├── INT (4 bytes) - 2B / 4B                           │
│  └── BIGINT (8 bytes) - huge                          │
│                                                         │
│  Strings                                               │
│  ├── CHAR - fixed length, pad trimmed                  │
│  ├── VARCHAR - variable, 1-2 bytes length prefix     │
│  ├── TEXT - no max, no full index                     │
│  └── ENUM - stored as integer                         │
│                                                         │
│  Dates                                                  │
│  ├── DATETIME - fixed 8 bytes, no timezone             │
│  ├── TIMESTAMP - 4 bytes, UTC, auto-update            │
│  └── DATE - 3 bytes for dates only                    │
│                                                         │
│  Decimals                                              │
│  ├── DECIMAL - exact precision math                    │
│  └── DOUBLE - approximate, faster                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```
