# Standards & Reference

## 7.1 Official Documentation

### Excel
- [Excel Documentation](https://support.microsoft.com/en-us/excel) - Microsoft support
- [Excel Functions](https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-2550-498e-93bf-6962b971999b) - Full function list
- [Power Query](https://learn.microsoft.com/en-us/power-query/) - Data transformation
- [DAX Reference](https://learn.microsoft.com/en-us/dax/dax-function-reference) - Power Pivot formulas

### Google Sheets
- [Google Sheets Help](https://support.google.com/docs) - Official help center
- [Google Sheets Functions](https://support.google.com/docs/table/25273) - Function list
- [Apps Script](https://developers.google.com/apps-script) - Automation
- [Google Sheets API](https://developers.google.com/sheets/api) - API reference

## 7.2 Excel Core Formulas

### Lookup Functions
```excel
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])

=VLOOKUP(A2, Products!A:D, 3, FALSE)  -- Legacy equivalent

=INDEX(B2:B100, MATCH("Product Name", A2:A100, 0))

=XLOOKUP(A2, Names!A:A, Names!B:B, "Not Found", 0, -1)
```

### Conditional Functions
```excel
=IF(condition, value_if_true, value_if_false)

=IFS(A1>=90, "A", A1>=80, "B", A1>=70, "C", TRUE, "F")

=IFERROR(formula, fallback_value)

=SWITCH(A2, "A", 100, "B", 200, "C", 300, 0)

=SUMIF(range, criteria, sum_range)
=COUNTIF(range, criteria)
=AVERAGEIF(range, criteria, average_range)
```

### Array Formulas
```excel
=FILTER(A:C, (B:B>1000)*(C:C="Active"))

=SORT(A2:D100, 2, -1)  -- Sort by column 2 descending

=UNIQUE(A2:A100)

=SORTBY(A2:A100, B2:B100, -1)

=XLOOKUP(A2, B:B, C:C) & " - " & XLOOKUP(A2, B:B, D:D)
```

## 7.3 Google Sheets Specific

### ARRAYFORMULA Patterns
```excel
=ARRAYFORMULA(IF(A:A="", "", B:B*C:C))

=ARRAYFORMULA(IF(ROW(A:A)=1, "Total", SUMIF(B:B, B:B, C:C)))

=QUERY(A:E, "SELECT A, SUM(C) GROUP BY A PIVOT B")
```

### QUERY Function
```excel
=QUERY(A:D, "SELECT A, SUM(B), AVG(C) WHERE A IS NOT NULL GROUP BY A ORDER BY SUM(B) DESC LABEL SUM(B) 'Total'")

=QUERY(A:C, "SELECT A, B, C WHERE B > "&DATE(2024,1,1)&" AND C < 1000")

=QUERY(A:E, "SELECT * PIVOT A WHERE B = 'Active'")
```

### Import Functions
```excel
=IMPORTRANGE("spreadsheet_url", "Sheet1!A:Z")

=IMPORTDATA("https://example.com/data.csv")

=IMPORTXML("https://example.com", "//div[@class='price']")
```

## 7.4 Pivot Tables

### Excel Pivot Table Fields
| Area | Purpose |
|------|---------|
| Filters | Filter entire pivot |
| Columns | Column headers |
| Rows | Row labels |
| Values | Aggregated data |

### Calculated Fields
```excel
-- In Pivot Table > Analyze > Fields > Items > Calculated Field
=Quantity * 0.1  -- 10% of quantity
=Revenue - Cost  -- Profit
```

### Power Query M (Excel)
```m
let
    Source = Excel.CurrentWorkbook(){[Name="SalesData"]}[Content],
    GroupedRows = Table.Group(Source, {"Category"}, {
        {"Total", each List.Sum([Amount]), type number},
        {"Count", each Table.RowCount(_), Int64.Type}
    })
in
    GroupedRows
```

## 7.5 Data Validation

```excel
=AND(A2>=0, A2<=100)  -- Number range

=LEFT(A2,4)="INV-"  -- Text starts with

=COUNTIF(A:A, A2)=1  -- No duplicates

=ISNUMBER(MATCH(A2, B:B, 0))  -- Value exists in another column

=OR(A2="Pending", A2="Approved", A2="Complete")  -- One of list
```

## 7.6 Version Compatibility

| Excel Version | New Functions | Notes |
|----------------|---------------|-------|
| Microsoft 365 | XLOOKUP, FILTER, SORT, UNIQUE, LET | Current |
| Excel 2019 | IFS, CONCAT, MAXIFS, MINIFS | |
| Excel 2016 | Slicer connection, Timelines | |
| Excel 2013 | PowerPivot, Power View | Legacy |

| Sheets Version | New Functions | Notes |
|----------------|---------------|-------|
| Current | LAMBDA, MAP, REDUCE | |
| Recent | XLOOKUP, FILTER, SORT | |
| Standard | QUERY, IMPORTRANGE, ARRAYFORMULA | |
