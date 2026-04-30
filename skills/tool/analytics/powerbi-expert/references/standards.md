# Standards & Reference

## 7.1 Official Documentation

- [Power BI Documentation](https://learn.microsoft.com/en-us/power-bi/) - Microsoft Learn
- [DAX Reference](https://learn.microsoft.com/en-us/dax/) - Complete DAX function reference
- [DAX Guide](https://dax.guide/) - Comprehensive DAX resource by SQLBI
- [Power Query M Reference](https://learn.microsoft.com/en-us/powerquery-m/) - M language functions
- [Power BI Best Practices](https://learn.microsoft.com/en-us/power-bi/guidance/) - Microsoft guidance
- [SQLBI DAX Patterns](https://www.sqlbi.com/guides/) - DAX pattern library

## 7.2 Data Modeling Standards

### Star Schema Design
```dax
-- Fact table: transactions with foreign keys
-- Dim tables: one dimension per entity

DimCustomer (CustomerKey, CustomerName, Email, Region, Segment, ...)
DimProduct   (ProductKey, ProductName, Category, Subcategory, Brand, ...)
DimDate      (DateKey, Date, Year, Quarter, Month, DayOfWeek, ...)
DimLocation  (LocationKey, City, State, Country, Latitude, Longitude, ...)

FactSales    (SalesKey, CustomerKey, ProductKey, DateKey, LocationKey, 
              Quantity, UnitPrice, Discount, SalesAmount)
```

### Relationship Types
| Type | Cardinality | Use Case |
|------|-------------|----------|
| One-to-Many | 1:* | Standard (Dim to Fact) |
| Many-to-Many | *:* | Bridge tables, SCD Type 2 |
| One-to-One | 1:1 | Denormalization scenarios |

## 7.3 DAX Standards

### Measure Structure
```dax
// Measure naming: Table[MeasureName]
// Use variables for readability
Total Sales := 
VAR CurrentPeriod = MAX('Date'[Date])
VAR Result =
    CALCULATE(
        SUM(Sales[SalesAmount]),
        REMOVEFILTERS(),
        Sales[OrderDate] <= CurrentPeriod
    )
RETURN Result

// YoY Growth Pattern
YoY Sales :=
VAR CurrentYear = MAX('Date'[Year])
VAR LY = CALCULATE([Total Sales], 'Date'[Year] = CurrentYear - 1)
RETURN
    DIVIDE([Total Sales] - LY, LY, 0)
```

### Common DAX Patterns
```dax
// Running Total
Running Total :=
CALCULATE(
    [Total Sales],
    FILTER(
        ALLSELECTED('Date'),
        'Date'[Date] <= MAX('Date'[Date])
    )
)

// Same Period Last Year
SPLY Sales :=
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR('Date'[Date])
)

// Moving Average (30 days)
MA 30 Days :=
VAR LastDate = MAX('Date'[Date])
VAR StartDate = LastDate - 29
RETURN
    CALCULATE(
        [Total Sales],
        DATESBETWEEN('Date'[Date], StartDate, LastDate)
    ) / 30
```

## 7.4 Power Query M Standards

```m
// Standard table transformations
let
    Source = Sql.Database("server", "database"),
    Table = Source{[Schema="dbo",Item="Sales"]}[Data],
    
    // Filter rows
    FilteredRows = Table 
        |> Table.SelectRows( each [Status] = "Active" and [Amount] > 0 ),
    
    // Change types
    ChangedType = Table.TransformColumnTypes(
        FilteredRows,
        {{"Date", type date}, {"Amount", type number}, {"Quantity", Int64.Type}}
    ),
    
    // Add custom column
    AddedColumn = Table.AddColumn(
        ChangedType,
        "Revenue", 
        each [Amount] * [Quantity], 
        type number
    )
in
    AddedColumn
```

## 7.5 Row-Level Security (RLS)

```dax
// User-based security
[Role: SalesRegion]
Email = USERNAME()
Region = LOOKUPVALUE(
    UserRegion[Region],
    UserRegion[Email], USERNAME(),
    UserRegion[Region], "All"
)

// Dynamic RLS
[Table Filter]
Email = USERPRINCIPALNAME()

// Manager hierarchy
[Employee Region] = 
VAR ManagerEmail = LOOKUPVALUE(
    Employees[ManagerEmail],
    Employees[Email], USERPRINCIPALNAME()
)
RETURN
    CALCULATETABLE(
        VALUES(Employees[Region]),
        Employees[ManagerEmail] = ManagerEmail || Employees[Email] = USERPRINCIPALNAME()
    )
```

## 7.6 Performance Best Practices

| Practice | Impact | Implementation |
|----------|--------|----------------|
| Use calculated columns sparingly | High | Pre-compute in Power Query |
| Disable auto date tables | Medium | Set File > Options > Data Load |
| Choose summarize over cross-join | High | Use SUMMARIZECOLUMNS |
| Avoid bidirectional relationships | High | Use CROSSFILTER with single direction |
| Use SUMX over nested CALCULATE | Medium | SUMX can be more efficient |
| Minimize visual-level filters | Medium | Use page/report level instead |
| Use aggregations for large tables | High | Tables > Properties > Aggregations |

## 7.7 Version Compatibility

| Power BI Version | DAX Features | Notes |
|------------------|--------------|-------|
| 2024 Q1+ | TREATAS, TOPNSKIP improvements | Current |
| 2023 Q3+ | Calculation groups GA | Release mode |
| 2023 Q1+ | Calculation groups preview | Dynamic formatting |
| 2022 Q4+ | Field parameters GA | Dynamic measures |
| 2022 Q1+ | Calculation groups preview | What-if analysis |
