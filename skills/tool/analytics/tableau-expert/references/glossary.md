# Glossary

## Tableau Core Concepts

| Term | Definition |
|------|------------|
| **Workbook** | Tableau file containing sheets and dashboards |
| **Sheet** | Individual worksheet with visualizations |
| **Dashboard** | Collection of sheets and objects |
| **Story** | Sequential narrative with sheets/dashboards |
| **Data Source** | Connection to database, file, or cloud |
| **Extract** | Local copy of data for performance |

## Visualization Terms

| Term | Definition |
|------|------------|
| **Mark** | Individual data point on visualization |
| **Mark Card** | Interface for configuring marks (color, size, etc.) |
| **Shelf** | Area for dragging fields (Columns, Rows, etc.) |
| **Pill** | Field dragged to shelf or card |
| **Axis** | Reference line for measure values |
| **Legend** | Guide for encoding (colors, sizes) |
| **Tooltip** | Information shown on hover |

## Data Model Terms

| Term | Definition |
|------|------------|
| **Dimension** | Categorical field (string, date, boolean) |
| **Measure** | Numeric field for aggregation |
| **Discrete** | Categorical, blue pills |
| **Continuous** | Numeric/date, green pills |
| **Hierarchies** | Drill-down structure |
| **Groups** | Manually combined dimension values |
| **Sets** | Custom subset of data |
| **Bins** | Numeric range grouping |

## Calculation Terms

| Term | Definition |
|------|------------|
| **Calculated Field** | Custom field using formulas |
| **LOD Expression** | Level of Detail aggregation |
| **Table Calculation** | Computation across table |
| **Quick Table Calculation** | Pre-built table calcs |
| **Parameter** | Interactive user input |
| **Total** | Grand total or subtotal |

## LOD Terms

| Term | Definition |
|------|------------|
| **FIXED LOD** | Aggregation at specified granularity, ignores filters |
| **INCLUDE LOD** | Adds dimensions to current viz level |
| **EXCLUDE LOD** | Removes dimensions from current viz level |
| **Detail** | The dimensions specified in LOD |
| **Scope** | The aggregation within LOD |

## Filter Terms

| Term | Definition |
|------|------------|
| **Context Filter** | Processes first, creates temporary table |
| **Data Source Filter** | Applies at connection level |
| **Extract Filter** | Applies when creating extract |
| **Dimension Filter** | Filters discrete values |
| **Measure Filter** | Filters by numeric threshold |
| **Top N Filter** | Shows only top/bottom N values |

## Join Terms

| Term | Definition |
|------|------------|
| **Join** | Combine tables on related columns |
| **Inner Join** | Only matching rows |
| **Left Join** | All from primary + matching |
| **Right Join** | All from secondary + matching |
| **Full Join** | All rows from both |
| **Union** | Stack tables vertically |
| **Blend** | Combine from different sources |

## Server & Sharing Terms

| Term | Definition |
|------|------------|
| **Tableau Server** | On-premises sharing platform |
| **Tableau Online** | Cloud sharing platform |
| **Tableau Public** | Free public visualization hosting |
| **Project** | Container for workbooks |
| **Workbook Owner** | Creator/manager of workbook |
| **Site** | Separate workspace on Server |
| **Schedules** | Automated refresh times |

## Visualization Types

| Term | Definition |
|------|------------|
| **Bar Chart** | Horizontal/vertical bars |
| **Line Chart** | Connected points over time |
| **Scatter Plot** | Two measures at data point level |
| **Gantt Chart** | Timeline with duration bars |
| **Box Plot** | Distribution with quartiles |
| **Treemap** | Hierarchical rectangles |
| **Heat Map** | Matrix with color intensity |
| **Highlight Table** | Cross-tab with color |
| **Bubble Chart** | Scatter with size dimension |

## Calculation Functions

| Category | Functions |
|----------|-----------|
| **Number** | ABS, CEILING, FLOOR, ROUND, SQRT, POWER |
| **String** | LEFT, RIGHT, MID, LEN, TRIM, CONTAINS, REPLACE |
| **Date** | TODAY, NOW, DATEADD, DATEDIFF, DATETRUNC |
| **Logical** | IF, IIF, CASE, AND, OR, NOT |
| **Aggregate** | SUM, AVG, MIN, MAX, COUNT, COUNTD |
| **Table Calc** | RUNNING_SUM, WINDOW_AVG, TOTAL, LAST |

## Performance Terms

| Term | Definition |
|------|------------|
| **Extract** | Local data copy (.hyper) |
| **Refresh** | Update extract with new data |
| **Incremental Refresh** | Add new rows only |
| **Full Refresh** | Rebuild entire extract |
| **Hyper** | Tableau's fast data engine |
| **Aggregation** | Pre-computed summary tables |
