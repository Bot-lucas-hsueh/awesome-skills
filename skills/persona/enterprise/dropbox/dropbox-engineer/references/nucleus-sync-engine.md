# Nucleus: The Rust Sync Engine

## Overview

Nucleus is Dropbox's rewritten sync engine, built in **Rust** (2020) to replace the legacy C++ engine. It handles file synchronization for 700M+ users.

## Why Rust?

| Benefit | Explanation |
|---------|-------------|
| Memory safety | Eliminates entire classes of bugs |
| Deterministic concurrency | Via ownership model |
| Type system | Encodes complex invariants |
| Single-threaded control | With futures for async |
| Fuzz testing | Reproducible seeds |

## The Three-Tree Model

```
┌──────────────────────────────────────────────────────┐
│                    Nucleus Engine                     │
├──────────────────────────────────────────────────────┤
│                                                       │
│   ┌─────────────┐     ┌─────────────┐               │
│   │  Local Tree │────▶│    Sync     │               │
│   │  (Client)   │     │    Tree     │               │
│   └─────────────┘     │  (Desired)  │               │
│          ▲            └──────┬──────┘               │
│          │                   │                       │
│          │            ┌──────▼──────┐               │
│          │            │  Remote     │               │
│          └────────────│    Tree     │               │
│                       │  (Server)   │               │
│                       └─────────────┘               │
│                                                       │
│   Convergence: All 3 trees eventually match          │
└──────────────────────────────────────────────────────┘
```

### Tree Definitions

| Tree | Description |
|------|-------------|
| Local Tree | Represents local filesystem state |
| Remote Tree | Represents server/cloud state |
| Sync Tree | The converged state we're working toward |

## Key Features

### O(1) Atomic Moves
- Move any file/folder instantly regardless of size
- Metadata operation only
- No data transfer required

### Strong Consistency
- Server and client have identical views before mutations
- Prevents race conditions

### Global Identifiers
- No transient duplicate/missing states
- Each file has a unique, persistent ID

### Protocol-Level Isolation
- Errors caught early, not propagated
- Invalid states rejected at API boundary

## Testing: CanopyCheck & Trinity

### CanopyCheck
- Property-based testing framework
- Tests convergence from arbitrary states
- Millions of random seeds daily in CI

### Trinity
- Data safety monitor
- Watches for invariant violations:
  1. Never lose user data
  2. Never create orphaned files
  3. Never violate causality

### Testing Metrics

| Metric | Value |
|--------|-------|
| Random seeds/day | Millions |
| Reproducibility | 100% (given seed) |
| CI logging | None (just seeds) |
| Local replay | Instant with seed |

## Sync Pipeline

```
┌─────────────────────────────────────────────────────────┐
│              Dropbox Sync Pipeline                       │
├─────────────────────────────────────────────────────────┤
│  1. CHUNKING                                             │
│     ├── Content-Defined Chunking (CDC) or Fixed 4MB     │
│     └── Variable sizing: 512KB-4MB based on entropy     │
│                                                          │
│  2. HASHING                                              │
│     ├── SHA-256 for block identification              │
│     └── Build block list (manifest)                     │
│                                                          │
│  3. DEDUPLICATION                                        │
│     ├── Check server for existing blocks                │
│     └── Only upload NEW blocks                          │
│                                                          │
│  4. DELTA SYNC                                           │
│     ├── Compare local vs remote block lists             │
│     └── Upload only changed chunks                      │
│                                                          │
│  5. CONVERGENCE                                          │
│     ├── Commit batch to server                          │
│     └── Notify other clients via Pub/Sub                │
└─────────────────────────────────────────────────────────┘
```

## Block-Level Sync Benefits

| Scenario | Traditional | Dropbox Delta |
|----------|-------------|---------------|
| Edit 1 page in 200MB PDF | Upload 200MB | Upload ~4MB chunk |
| Same file in 2 folders | Store 2× | Store 1× (dedup) |
| Rename file | Re-upload | Metadata update only |
| LAN sync | Via server | Direct P2P (68% faster) |

## References

- [Dropbox Engineering: Rewriting the Sync Engine in Rust](https://dropbox.tech/infrastructure/rewriting-dropbox-sync-engine-rust)
- [Dropbox Engineering: Testing Our New Sync Engine](https://dropbox.tech/infrastructure/-testing-our-new-sync-engine)
