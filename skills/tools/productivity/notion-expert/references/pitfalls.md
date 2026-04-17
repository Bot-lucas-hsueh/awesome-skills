# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Prevention |
|---|---------|----------|------------|
| 1 | **Deeply nested pages** | High | Max 3 levels, use links instead |
| 2 | **No database conventions** | High | Establish naming standards early |
| 3 | **Overlapping databases** | Medium | One source of truth per data type |
| 4 | **No templates** | Medium | Create templates for common pages |
| 5 | **Ignoring permissions** | High | Review sharing settings regularly |
| 6 | **Content in multiple places** | Medium | Single source of truth |
| 7 | **Excessive filters/views** | Low | Clean up unused views |
| 8 | **Not archiving old data** | Medium | Monthly archive routine |

### Anti-Pattern: Page Sprawl

```
Anti-Pattern:
Team Wiki/
├── Projects/
│   ├── Project A/
│   │   └── Notes/
│   │       └── Meeting Notes/
│   │           └── 2024/
│   │               └── January/
│   └── Project B/
│       └── Notes/
│           └── Meeting Notes/
│               └── 2024/
│                   └── January/

Problem: Hard to find things, duplicates

Solution:
- Flat structure with tags
- Single meeting notes database
- Use databases with date properties
```

## 10.2 Anti-Patterns

### 1. The "Everything Database"

```
Anti-Pattern:
One database with 50+ properties
Columns: Name, Status, Type, Priority, Owner, Date1, Date2, 
         Text1, Text2, Tags1, Tags2, Relation1, Relation2...

Problem: Overwhelming, slow queries

Solution:
- Split into focused databases
- Use relations instead of many properties
- Maximum 15 properties per database
```

### 2. No Consistent Naming

```
Anti-Pattern:
- "Q1 goals"
- "Q1 Goals"
- "q1 goals"
- "Goals Q1 2024"

Problem: Search fails, inconsistent

Solution:
Establish conventions:
- Title Case for page names
- Lowercase for tags
- ISO dates: 2024-01-15
- Consistent abbreviations list
```

### 3. Workflow States Not Enforced

```
Anti-Pattern:
Status: "In Progress" | "Inprogress" | "In Progresss" | "Working"

Problem: Can't filter reliably

Solution:
Use Select/Status properties:
- Pre-defined options only
- No free text
- Use colors consistently
```

### 4. Storing Dynamic Content in Text

```
Anti-Pattern:
Status field value: "3 of 5 tasks complete"

Problem: Can't filter, sort, or aggregate

Solution:
Use proper data types:
- Number properties for counts
- Relation properties for linked items
- Formula properties for calculations
```

### 5. Not Using Templates

```
Anti-Pattern:
Creating pages from scratch every time
Copy-pasting old content

Problem: Inconsistency, wasted time

Solution:
Create templates:
- Project page template
- Meeting notes template
- Task template
- Incident template
- Weekly review template
```

## 10.3 Integration Anti-Patterns

| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| API token in public code | Security breach | Use environment variables |
| No rate limit handling | API blocked | Implement exponential backoff |
| Syncing too frequently | Performance issues | Set reasonable intervals |
| No error handling | Data loss | Add try-catch, logging |
| Bidirectional sync loops | Infinite loops | Use webhooks, not polling |

## 10.4 Permission Anti-Patterns

```
Anti-Pattern: 
- Making everything public
- Everyone is admin
- Inheriting parent permissions blindly

Best Practice:
1. Default: Private
2. Share only what's needed
3. Use groups, not individual access
4. Regular permission audits
5. Document sharing conventions
```

## 10.5 Performance Anti-Patterns

```javascript
// BAD: Expensive operations in views
filter(
  property("Tags").contains("A") AND 
  property("Tags").contains("B") AND
  property("Tags").contains("C")
)

// GOOD: Use single select/multi-select properly
filter(
  and(
    contains(prop("Tags"), "A"),
    contains(prop("Tags"), "B")
  )
)

// Limit results
page_size: 25  // Instead of default 100
```
