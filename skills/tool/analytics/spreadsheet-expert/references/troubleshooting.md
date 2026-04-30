# Troubleshooting Guide

## 8.1 Common Formula Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#DIV/0!` | Division by zero | Wrap with IFERROR or IF |
| `#N/A` | Lookup not found | Verify lookup value exists |
| `#REF!` | Invalid cell reference | Check deleted rows/columns |
| `#VALUE!` | Wrong data type | Use VALUE() or check types |
| `#NAME?` | Unrecognized function | Check spelling, add underscore |
| `#NUM!` | Invalid numeric value | Check calculation limits |
| `#NULL!` | Invalid range | Use colon (:) not space |
| `#CALC!` | Calculation engine error | Simplify formula |

## 8.2 VLOOKUP/XLOOKUP Issues

### XLOOKUP vs VLOOKUP Problems
```excel
-- XLOOKUP not available in older Excel
=IFERROR(XLOOKUP(A2, B:B, C:C), "Not Found")

-- For Excel 2016/2019, use INDEX/MATCH
=IFERROR(INDEX(C:C, MATCH(A2, B:B, 0)), "Not Found")
```

### Lookup Returns Wrong Value
- Check if lookup column has duplicates
- Verify exact vs approximate match (0 vs 1)
- Check for extra spaces: `=TRIM(A2)`

### Case-Sensitive Lookup
```excel
-- Excel: Use EXACT in array formula
=INDEX(B:B, MATCH(TRUE, EXACT(A2, A:A), 0))

-- Sheets: FILTER with exact match
=INDEX(FILTER(B:B, A:A=A2))
```

## 8.3 Array Formula Issues

### Array Formula Not Working
```excel
-- Excel 365: Dynamic arrays (no Ctrl+Shift+Enter needed)
=FILTER(A:C, B:B>100)

-- Older Excel: Array formula entry
{=LARGE(IF(A:A>100, B:B), 1)}  -- Enter with Ctrl+Shift+Enter
```

### SPILL Error
- Check for empty cells in spill range
- Remove conflicting data
- Use @ operator to collapse: `=@FILTER(...)`

## 8.4 Performance Issues

### Slow Calculation
```excel
-- Replace volatile functions
=OFFSET(A1, 0, 0)  -- Volatile, slow
=INDEX(A:A, 1)      -- Non-volatile

-- Reduce array size
=FILTER(A1:A10000, B1:B10000>100)  -- Better
```

### Large File Size
1. Remove unused rows/columns
2. Convert formulas to values
3. Use Tables (Ctrl+T) instead of ranges
4. Disable auto-calculation temporarily
5. Save as .xlsx instead of .xls

## 8.5 Data Type Issues

### Numbers Stored as Text
```excel
-- Excel
=VALUE(A2)
=--A2  -- Double unary
=Multiply by 1: =A2*1

-- Sheets
=VALUE(A2)
```

### Dates Interpreted as Numbers
```excel
-- Format as date
=TEXT(A2, "yyyy-mm-dd")

-- Convert to date
=DATEVALUE(TEXT(A2, "0"))
```

## 8.6 Google Sheets Specific

### IMPORTRANGE Issues
```excel
-- First-time connection
=IMPORTRANGE("URL", "Sheet1!A1:Z1000")
-- Grant permission when prompted

-- Re-authorize after URL change
=IMPORTRANGE("new_URL", "Sheet1!A1")
```

### QUERY Syntax Errors
```excel
-- Common mistakes
=QUERY(A:C, "SELECT A, B WHERE B > 100")  -- Wrong: no LABEL
=QUERY(A:C, "SELECT A, SUM(B) GROUP BY A")  -- Wrong: need label for sum

-- Correct
=QUERY(A:C, "SELECT A, SUM(B) GROUP BY A LABEL SUM(B) 'Total'")

-- Date syntax in QUERY
=QUERY(A:C, "SELECT A WHERE A > date '2024-01-01'")
```

### Apps Script Errors
```javascript
// Timeout issue
function processLargeSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName('Data');
  
  // Process in batches
  const startRow = 1;
  const batchSize = 1000;
  const lastRow = sheet.getLastRow();
  
  for (let i = startRow; i < lastRow; i += batchSize) {
    const range = sheet.getRange(i, 1, Math.min(batchSize, lastRow - i + 1), 10);
    // Process range
    SpreadsheetApp.flush();
  }
}
```

## 8.7 Cross-Platform Issues

### Excel vs Google Sheets Differences
| Feature | Excel | Sheets |
|---------|-------|--------|
| Array formula entry | Ctrl+Shift+Enter | Automatic |
| Named ranges | Ctrl+F3 | Data > Named ranges |
| IFS | Excel 2019+ | Always available |
| XLOOKUP | Microsoft 365 | Recent versions |

### Conditional Formatting
```excel
-- Excel: Use FORMULATEXT for complex rules
=AND($A2="Active", $B2>1000, TODAY()>$C2)

-- Sheets: Same formula syntax
=AND(A2="Active", B2>1000, TODAY()>C2)
```

## 8.8 Debugging Formulas

### Excel Formula Evaluator
1. Formulas > Evaluate Formula
2. Step through calculation
3. Check intermediate results

### Sheets Formula Debugging
```excel
=IFERROR(YourFormula, "Error: "&IFERROR(YourFormula, "Unknown"))

-- Break down complex formulas
=LET(
    a, FILTER(A:A, B:B>100),
    b, UNIQUE(a),
    SUM(b)
)
```
