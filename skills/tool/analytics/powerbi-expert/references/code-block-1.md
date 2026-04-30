# dax Example

```
-- Basic Measure
Total Sales := 
SUM ( Fact[SalesAmount] )

-- Measure with Filter Context (CALCULATE)
Total Sales PY := 
CALCULATE (
    [Total Sales],
    SAMEPERIODLASTYEAR ( 'Dim_Date'[Date] )
)

-- YoY Growth
YoY Growth % := 
VAR CurrentYear = [Total Sales]
VAR PriorYear = [Total Sales PY]
RETURN
    DIVIDE ( CurrentYear - PriorYear, PriorYear )

-- Running Total (Cumulative)
Cumulative Sales := 
CALCULATE (
    [Total Sales],
    FILTER (
        ALL ( 'Dim_Date' ),
        'Dim_Date'[Date] <= MAX ( 'Dim_Date'[Date] )
    )
)

-- Conditional Formatting in Measure
Sales Health := 
VAR Target = [Sales Target]
VAR Actual = [Total Sales]
RETURN
    SWITCH (
        TRUE (),
        Actual >= Target * 1.1, "🟢 Excellent",
        Actual >= Target, "🟡 On Target",
        Actual >= Target * 0.9, "🟠 At Risk",
        "🔴 Below Target"
    )

-- Time Intelligence: MTD, QTD, YTD
MTD Sales := 
CALCULATE (
    [Total Sales],
    DATESMTD ( 'Dim_Date'[Date] )
)

YTD Sales := 
CALCULATE (
    [Total Sales],
    DATESYTD ( 'Dim_Date'[Date], "12/31" )
)

-- Moving Average (7-day)
7-Day Avg Sales := 
CALCULATE (
    [Total Sales],
    DATESINPERIOD ( 'Dim_Date'[Date], MAX ( 'Dim_Date'[Date] ), -7, DAY )
) / 7
```
