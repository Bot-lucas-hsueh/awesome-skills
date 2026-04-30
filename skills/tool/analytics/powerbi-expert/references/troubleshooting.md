# Troubleshooting Guide

## 8.1 Common DAX Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `Column 'X' in table 'Y' cannot be found` | Missing column reference | Verify table relationship or use RELATED() |
| `A function 'X' has been used in a true/false expression` | Type mismatch | Use explicit comparison operators |
| `Circular dependency detected` | Dependent calculations | Break the cycle; restructure measure |
| `The expression refers to multiple columns` | Multiple column in single-column context | Wrap in CALCULATE or use SUMMARIZE |
| `Token literal expected` | Syntax error | Check brackets, quotes, commas |
| `Function COUNTX expects a table expression` | Wrong argument type | Use COUNTROWS for column count |

## 8.2 Performance Issues

### Slow Report Troubleshooting
```
1. Check performance analyzer (View > Performance)
2. Identify slow visuals
3. Check DAX query timings
4. Look for high cardinality columns
5. Verify relationship direction
```

### Slow DAX Measures
```dax
// Problem: Complex nested CALCULATE
// Solution: Use variables to reduce re-evaluation
BadMeasure :=
CALCULATE(
    SUM(Sales[Amount]),
    CALCULATE(
        SUM(Sales[Amount]),
        FILTER(ALL(Sales), Sales[Category] = "A")
    )
)

// Better: Use single CALCULATE with combined filters
BetterMeasure :=
VAR TotalA = CALCULATE(SUM(Sales[Amount]), Sales[Category] = "A")
RETURN
    SUM(Sales[Amount]) - TotalA
```

### Relationship Troubleshooting
```dax
// Cross-filter direction issues
// Problem: Bidirectional causing blow-up
// Solution: Use CROSSFILTER explicitly
Measure :=
CALCULATE(
    [Total Sales],
    CROSSFILTER(Sales[CustomerKey], Customer[CustomerKey], ONEWAY)
)

// Inactive relationship
MeasureWithInactive :=
CALCULATE(
    [Total Sales],
    USERELATIONSHIP(Sales[ShipDateKey], Date[DateKey])
)
```

## 8.3 Power Query Issues

### Slow Refresh
```m
// Enable query folding
let
    Source = Sql.Database("server", "db"),
    // Let Power Query push operations to SQL
    Filtered = Table.SelectRows(Source, each [Date] > #date(2024,1,1)),
    Grouped = Table.Group(Filtered, {"Category"}, {{"Sum", each List.Sum([Amount]), type number}})
in
    Grouped

// Check folding: right-click step > View Native Query
```

### Column Type Errors
```m
// Safe datetime conversion
FixedDate = Table.TransformColumnTypes(
    Source,
    {{"DateColumn", type text}}
)[DateColumn]
    |> Table.TransformColumnTypes({{"DateColumn", type datetime}})

// Handle mixed formats
CleanedDate = Table.TransformColumnTypes(
    Source,
    {{"DateColumn", 
        type text,
        Culture = "en-US"}}
)
```

## 8.4 Import vs. DirectQuery Issues

### Switching Storage Mode
- DirectQuery: Real-time data, limited DAX
- Import: Fast, full DAX support, memory constraints
- Composite: Mix both with aggregations

### Aggregations Table
```m
// Create aggregation table in Power Query
let
    Source = Sql.Database("server", "db"),
    DailySales = Sql.Database("server", "db"){[Schema="dbo",Item="DailySalesAgg"]}[Data]
in
    DailySales
```

## 8.5 RLS Debugging

### Test RLS in Power BI Desktop
1. View tab > As roles
2. Add your email/username
3. Check what data is visible

### RLS Not Working
```dax
// Add debug measure
DEBUG_User := USERPRINCIPALNAME()

// Check table filter
DEBUG_Access := 
CALCULATETABLE(
    COUNTROWS('UserRegion'),
    'UserRegion'[Email] = USERPRINCIPALNAME()
)

// Verify USERNAME() vs USERPRINCIPALNAME()
// USERNAME() = OLD UPN format
// USERPRINCIPALNAME() = user@domain.com
```

## 8.6 Gateway Issues

### Refresh Failures
```
1. Check gateway status (Manage gateways)
2. Verify credentials (Data sources)
3. Check gateway logs
4. Test connection manually
5. Restart gateway service
```

### On-Premises Data Gateway Commands
```powershell
# Check gateway status
Get-GatewayStatus

# Restart service
Restart-Service -Name "On-premises data gateway"

# View logs
Get-Content "$env:APPDATA\Microsoft\On-premises data gateway\*.log" -Tail 100
```

## 8.7 DAX Performance Checklist

- [ ] Use `SUMMARIZECOLUMNS` instead of `SUMMARIZE` + `ADDCOLUMNS`
- [ ] Avoid `CALCULATE` inside `SUMX`
- [ ] Use `DIVIDE` instead of `/`
- [ ] Minimize context transitions
- [ ] Use `KEEPFILTERS` to control filter behavior
- [ ] Prefer `FILTER(ALL())` over `REMOVEFILTERS()` where needed
- [ ] Check `CrossJoin` usage - often unnecessary
