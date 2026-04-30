# notion Example

```
-- Basic math and conditional
prop("Revenue") - prop("Cost")

-- IF statement
if(prop("Status") == "Done", "✅", "⏳")

-- Nested IF with SWITCH (cleaner)
switch(prop("Priority"),
  "High", "🔴",
  "Medium", "🟡",
  "Low", "🟢",
  "⚪"
)

-- Date calculations
dateBetween(prop("Due Date"), now(), "days")  -- Days until due
dateBetween(now(), prop("Start Date"), "days")  -- Days since start

-- Conditional with date
if(dateBetween(prop("Due Date"), now(), "days") < 0,
  "🔴 Overdue",
  if(dateBetween(prop("Due Date"), now(), "days") < 3,
    "🟡 Due Soon",
    "✅ On Track"
  )
)

-- Concatenate with formatting
"Project: " + prop("Name") + " | Status: " + prop("Status")

-- Count related items (Rollup)
-- Use Rollup property on relation, count()
prop("Tasks").length()

-- Boolean conditions
and(prop("Revenue") > 10000, prop("Status") == "Active")

-- Text manipulation
slice(prop("Name"), 0, 50)  -- First 50 chars
contains(prop("Tags"), "urgent")  -- Boolean check
replace(prop("Name"), "old", "new")  -- Find and replace
lower(prop("Name"))  -- Lowercase
```
