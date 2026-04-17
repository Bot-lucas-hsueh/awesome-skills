# Troubleshooting Guide

## 8.1 Calculation Errors

| Error | Cause | Solution |
|-------|-------|----------|
| "Cannot mix aggregate and non-aggregate" | Mixing row-level and aggregate | Use LOD or aggregate both sides |
| "Expected boolean" | IF condition not boolean | Check expression returns TRUE/FALSE |
| "Unknown function" | Typo or unsupported function | Check Tableau function list |
| "Nested aggregations not allowed" | Aggregated function in aggregation | Use LOD instead |
| "Level of detail expressions cannot be nested" | LOD inside LOD | Restructure calculation |

## 8.2 Calculation Issues

### Mixing Aggregate and Non-Aggregate
```tableau
-- Problem: Cannot aggregate and non-aggregate in same calc
SUM([Sales]) / [Profit Ratio]  -- Profit Ratio is non-aggregate

-- Solution 1: Use LOD
SUM([Sales]) / { FIXED : SUM([Sales] / [Cost]) }

-- Solution 2: Make both aggregate
SUM([Sales]) / SUM([Sales] / [Cost])

-- Solution 3: Attribute instead of measure
ATTR([Category]) / [Measure]  -- ATTR converts to aggregate
```

### LOD Aggregation Errors
```tableau
-- Problem: Nested aggregations
{ FIXED [Customer] : SUM({ FIXED [Order] : SUM([Sales]) }) }

-- Solution: Simplify
{ FIXED [Customer] : MIN({ FIXED [Customer], [Order] : SUM([Sales]) }) }
```

### Date Calculation Issues
```tableau
-- Problem: Date arithmetic
[Order Date] + 30  -- Returns serial number, not date

-- Solution: Use DATEADD
DATEADD('day', 30, [Order Date])

-- Problem: Date comparison
[Date] = #2024-01-01#  -- String vs Date

-- Solution: Use DATE function
[Date] = DATE(#2024-01-01#)
```

## 8.3 Performance Issues

### Slow Dashboard Load
```
1. Check performance recorder (Help > Settings & Performance > Start Performance Recording)
2. Identify slow queries
3. Check for:
   - Too many marks (try filtering)
   - Complex LOD expressions
   - Live vs Extract connection
   - Too many context filters
```

### Too Many Marks
```tableau
-- Add aggregation to reduce marks
{ FIXED : COUNTD([Order ID]) }  -- Per order level

-- Use data source filter
-- Right-click measure > Filter > At Most

-- Use context filter (processes first)
-- Drag filter to Context
```

### Extract Performance
```tableau
-- Slow refresh
-- 1. Limit data with filters
-- 2. Hide unused fields
-- 3. Use incremental refresh
-- 4. Consider aggregation

-- Create performance-optimized extract:
-- Data > Extract > Filters > Add
-- Data > Hide All Unused Fields
```

## 8.4 Join & Blend Issues

### Incorrect Join Results
```tableau
-- Check join type: many-to-many causes row explosion
-- Right-click data source > View Data

-- Use data blending for different granularity
-- Primary: Orders (many rows)
-- Secondary: Target (one row per salesrep)
-- Link on: [Sales Rep ID]
```

### Null Values in Blends
```tableau
-- Problem: Secondary source shows NULL
-- Cause: No matching value or NULL in link field

-- Solution 1: Use IFNULL in link
-- Edit relationship > Use calculated field

-- Solution 2: Create merged field
-- Data > Edit Relationships > Custom > COALESCE([A], [B])
```

### Data Blending Not Working
```tableau
-- Check indicator colors
-- Blue = Primary source
-- Orange = Secondary source
-- Ensure linking field has matching values

-- Use only one linking field if possible
-- Multiple links can cause issues
```

## 8.5 Filter Issues

### Filter Not Working as Expected
```tableau
-- Context filter vs regular filter
-- Context filters process first (WHERE in SQL)
-- Regular filters process after (HAVING in SQL)

-- For top N by measure:
-- 1. Add to Context
-- 2. Use FIXED LOD in Top N filter
```

### Filter Scope Problems
```tableau
-- Problem: Filter affects calculation incorrectly
-- Solution: Use FIXED LOD to "fix" the calculation
{ FIXED [Customer] : SUM([Sales]) }  -- Fixed before filter

-- Or use INCLUDE/EXCLUDE LOD
{ INCLUDE [Region] : SUM([Sales]) }
```

## 8.6 Date Handling Issues

### Date Comparison Problems
```tableau
-- Strings vs Dates
DATETIME([Date String])  -- Convert string to datetime
DATE([Date String])      -- Convert to date only

-- Fiscal year calculation
IF MONTH([Date]) >= 7 THEN YEAR([Date]) + 1
ELSE YEAR([Date])
END
```

### Fiscal Year Date Filtering
```tableau
-- Create fiscal date parameter
// Fiscal Year Start: 7 (July)

// Fiscal Year
DATEADD('month', 7-[Fiscal Year Start], [Order Date])

-- Or use custom fiscal date
MAKEDATE(YEAR([Date]), 
    IF MONTH([Date]) >= 7 THEN MONTH([Date]) - 6 ELSE MONTH([Date]) + 6 END,
    DAY([Date])
)
```

## 8.7 Debugging Checklist

- [ ] Verify data source connection
- [ ] Check calculated field syntax
- [ ] Test LOD expressions in isolation
- [ ] Review filter order (context vs regular)
- [ ] Check join/cardinality issues
- [ ] Validate date formats match
- [ ] Use performance recorder for slow issues
- [ ] Test in Tableau Desktop before Server
