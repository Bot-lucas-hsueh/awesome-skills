# Standards & Reference

## 7.1 Official Documentation

- [Tableau Documentation](https://help.tableau.com/current/pro/desktop/en-us/default.htm) - Official docs
- [Tableau Functions](https://help.tableau.com/current/pro/desktop/en-us/functions.htm) - All functions
- [Calculated Field Reference](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields.htm) - How to build calculations
- [LOD Expressions](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm) - FIXED/INCLUDE/EXCLUDE
- [Tableau Server Admin](https://help.tableau.com/current/server/en-us/default.htm) - Server management
- [Tableau Public Gallery](https://public.tableau.com/app/discover) - Example visualizations

## 7.2 Calculated Field Reference

### Basic Calculations
```tableau
// Arithmetic
[Sales] * 0.1                    -- 10% of sales
[Sales] - [Cost]                 -- Profit
[Profit] / [Sales]               -- Profit ratio
ROUND([Sales], -3)               -- Round to thousands

// Aggregations
SUM([Sales])
AVG([Profit])
COUNT([Order ID])
COUNTD([Customer ID])            -- Distinct count
MEDIAN([Sales])
STDEV([Sales])

// Running calculations
RUNNING_SUM(SUM([Sales]))
RUNNING_AVG(SUM([Sales]))
WINDOW_SUM(SUM([Sales]), -2, 0)  -- 3-period sum
```

### Logical Functions
```tableau
IF [Sales] > 10000 THEN 'High'
ELSEIF [Sales] > 5000 THEN 'Medium'
ELSE 'Low'
END

IFNULL([Discount], 0)            -- Replace NULL
ZN([Sales])                      -- Zero if NULL
ISNULL([Field])                  -- Check for NULL

CASE [Region]
    WHEN 'West' THEN 'Pacific'
    WHEN 'East' THEN 'Atlantic'
    ELSE 'Other'
END

CONTAINS([Name], 'Corp')         -- String search
STARTSWITH([Email], '@')         -- String starts
ENDSWITH([Email], '.com')        -- String ends
```

## 7.3 Level of Detail (LOD) Expressions

### Syntax Patterns
```tableau
// FIXED: Ignores viz-level filters (respects context filters)
{ FIXED [Region] : SUM([Sales]) }
{ FIXED [Customer ID] : MIN([Order Date]) }

// INCLUDE: Adds to viz-level aggregation
{ INCLUDE [Category] : AVG([Profit]) }

// EXCLUDE: Removes from viz-level aggregation
{ EXCLUDE [Region] : SUM([Sales]) }

// Nested LOD
{ FIXED [Customer ID] : 
    MIN({ FIXED [Customer ID, Order ID] : SUM([Sales]) })
}
```

### Common LOD Use Cases
```tableau
// Customer count (ignore viz dimensions)
{ FIXED : COUNTD([Customer ID]) }

// First purchase date per customer
{ FIXED [Customer ID] : MIN([Order Date]) }

// Percentage of total
SUM([Sales]) / SUM({ FIXED : SUM([Sales]) })

// Average per customer
{ FIXED [Customer ID] : SUM([Sales]) } / COUNTD([Customer ID])
```

## 7.4 Data Blending vs Joins

| Aspect | Blend | Join |
|--------|-------|------|
| Data Source | Multiple sources | Same or different |
| Granularity | Kept separate | Combined |
| Linking | Blending key | Join key |
| Performance | Can be slower | Usually faster |
| Use When | Different detail levels | Same level, need all columns |

### Blend Configuration
```tableau
-- Primary source: Orders
-- Secondary source: Customer Info (linked on Customer ID)

-- Calculation in primary:
{ FIXED [Order ID] : SUM([Sales]) }  -- Fixed to order level

-- Use LOD to handle mismatched detail:
{ INCLUDE [Customer ID] : AVG([Profit Margin]) }
```

## 7.5 Performance Best Practices

| Practice | Impact | Implementation |
|----------|--------|----------------|
| Use Context Filters | High | Right-click filter > Add to Context |
| Limit Extract Data | High | Use filters, hide unused fields |
| Use RAW for complex LOD | Medium | Avoid complexity in calculations |
| Minimize COUNTD | High | Use approximate count or LOD |
| Use data source filters | High | Filter at connection level |
| Limit dashboard size | Medium | Avoid excessive objects |

### Extract Optimization
```tableau
-- Create aggregated extract
-- Hide all unnecessary fields
-- Use incremental refresh

-- Aggregation settings:
-- None (all rows)
-- At the level of: [Date], [Region], [Category]
-- Up to 0.5 million rows
```

## 7.6 Version Compatibility

| Tableau Version | Key Features | Notes |
|-----------------|--------------|-------|
| 2024.x | Ask Data improvements, Einstein Copilot | Current |
| 2023.x | Salesforce integration, Hyper 2.0 | |
| 2022.x | Metrics, Buffer calculations | |
| 2021.x | Explain Data, Prep improvements | |
| 2020.x | Ask Data, Explain Data preview | |

| Tableau Server | Licensing | Notes |
|----------------|-----------|-------|
| 2024.x | Creator/Explorer/Viewer | Role-based |
| 2023.x | Core/User-based | |
| Online | Creator/Explorer/Viewer | Cloud |
