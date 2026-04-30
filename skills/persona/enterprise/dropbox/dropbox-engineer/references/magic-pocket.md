# Magic Pocket: Exabyte-Scale Storage Architecture

## Overview

Magic Pocket is Dropbox's proprietary exabyte-scale blob storage infrastructure, built to replace AWS S3 and save the company $74.6M over two years. It represents one of the largest cloud-to-onprem migrations in history.

## Key Metrics (2024)

| Metric | Value |
|--------|-------|
| Total Capacity | Exabyte-scale (1 EB = 1 billion GB) |
| Objects Stored | 1+ trillion |
| Repair Rate | 4 extents/second |
| Repair SLA | < 48 hours |
| Storage Overhead (Hot) | 2.0× |
| Storage Overhead (Cold) | 1.4× |

## Architecture Components

### Cell-Based Design
- **Cells** are isolated failure domains
- Multiple racks across different power/network domains
- Thousands of storage nodes (OSDs) per cell
- Self-contained metadata within each cell

### Storage Tiers

```
┌─────────────────────────────────────────────────────────┐
│                    Magic Pocket                          │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐ │
│  │   Hot Tier  │  │   Warm Tier │  │   Cold Storage  │ │
│  │  (SSD/Flash)│  │  (HDD)      │  │  (Erasure Code) │ │
│  └─────────────┘  └─────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

| Tier | Use Case | Redundancy |
|------|----------|------------|
| Hot | Frequently accessed | 2× replication |
| Warm | Moderate access | 2× replication |
| Cold | Archival | Erasure coding (~1.4×) |

### Diskotech Hardware

Custom 1PB storage box:
- Dimensions: 44" × 18"
- Capacity: 1 petabyte per box
- Designed for high-density storage

## Erasure Coding

Dropbox uses XOR-based encoding inspired by Facebook's f4:
- Split blob into 2 halves
- Store XOR of halves in different zones
- Reduces storage from 2× replication to ~1.4×

## Lessons from Magic Pocket

1. **Protect and verify** — End-to-end verification is non-negotiable
2. **Okay to move slow at scale** — Prioritize durability over speed
3. **Keep things simple** — Too many optimizations complicate mental models
4. **Prepare for the worst** — Always have a backup plan

## Cost Impact

| Strategy | Storage Overhead | Cost for 1PB |
|----------|------------------|--------------|
| 3× Replication | 3.0× | $180K/month |
| 2× Replication (Hot) | 2.0× | $120K/month |
| Erasure Coding (Cold) | 1.4× | $84K/month |

## References

- [Dropbox Engineering Blog: Magic Pocket](https://dropbox.tech/infrastructure/magic-pocket-exabyte-scale-blob-storage)
- [InfoQ: Magic Pocket Exabyte-Scale Storage](https://www.infoq.com/articles/dropbox-magic-pocket-exabyte-storage/)
- Wired: "The Epic Story of Dropbox's Exodus from AWS" (2016)
