# excel Example

```
-- XLOOKUP (Excel 365/2021): Modern replacement for VLOOKUP/HLOOKUP
=XLOOKUP(A2, Names, Prices, "Not Found", 0, 1)
-- Syntax: lookup_value, lookup_array, return_array, if_not_found, match_mode, search_mode

-- INDEX + MATCH (Universal, works in all versions)
=INDEX(Prices, MATCH(A2, Names, 0))
=INDEX(Prices, MATCH(1, (Names=A2)*(Status="Active"), 0))  -- Array formula

-- FILTER (Excel 365): Dynamic filtering
=FILTER(A:D, (B:B>1000)*(C:C="Active"), "No Results")
=FILTER(Sales[Revenue], Sales[Quarter]="Q1")

-- XLOOKUP with multiple criteria
=XLOOKUP(1, (Names=A2)*(Products=B2), Prices, "Not Found")

-- SUMPRODUCT for conditional aggregation
=SUMPRODUCT((Category="Electronics")*(Region="North")*(Revenue))
=SUMPRODUCT((DATE(YEAR(A:A),MONTH(A:A),1)=DATE(2024,1,1))*(Revenue))

-- LET: Name intermediate calculations
=LET(
    total, SUM(A:A),
    count, COUNTA(A:A),
    average, total/count,
    "Total: " & total & ", Avg: " & average
)

-- Dynamic arrays with SORT, UNIQUE
=SORT(UNIQUE(Region))
=SORTBY(Name, Revenue, -1)  -- Sort by Revenue descending

-- Text manipulation
=TEXTJOIN(", ", TRUE, IF(B:B=A2, C:C, ""))  -- Concatenate matching values
=REGEXEXTRACT(A2, "\d{4}-\d{2}-\d{2}")  -- Google Sheets: extract date
=LEFT(A2, FIND(" ", A2)-1)  -- First name extraction
```
