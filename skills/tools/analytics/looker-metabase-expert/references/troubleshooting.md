# Troubleshooting Guide

## 8.1 Looker Error Codes

| Error Code | Meaning | Resolution |
|------------|---------|------------|
| `L0040` | LookML validation error | Check syntax in LookML explorer; validate YAML structure |
| `L0050` | Missing required field | Add dimension or measure to view definition |
| `L0090` | Invalid join | Verify `sql_on` clause references correct fields |
| `L0120` | Circular dependency | Remove cyclic joins in explore definition |
| `L4001` | Permission denied | Check user attributes and model access |
| `L4020` | Explore not found | Verify explore name matches view name |

## 8.2 Looker Query Performance Issues

### Slow Dashboard Troubleshooting

**Step 1: Identify Slow Queries**
```
Admin > Queries > Running Queries
```
Look for queries running > 30 seconds.

**Step 2: Check Query Plan**
```lookml
# Add to derived table for debugging
sql_trigger_value: CURRENT_TIMESTAMP ;;
```

**Step 3: Common Fixes**
- Add index on foreign keys used in joins
- Enable `aggregate_table` for common aggregations
- Use `sql_always_where` to push date filters to database
- Check for N+1 query patterns in nested dimensions

### Explode in Joins
```sql
-- Symptom: Row count explodes unexpectedly
-- Cause: Many-to-many join without deduplication

-- Fix: Add distinct or aggregate before join
SELECT DISTINCT customer_id 
FROM orders 
WHERE status = 'completed'
```

## 8.3 Metabase Troubleshooting

### Dashboard Not Loading
1. Check question query executes successfully in SQL editor
2. Verify field filters are connected to questions
3. Clear Metabase cache: `Admin > Troubleshooting > Logs > Clear cache`
4. Check browser console for iframe sandbox errors (embedding)

### Sync Issues with Database
```bash
# Force resync via API
curl -X POST "https://your-metabase/api/database/1/sync" \
  -H "Cookie: metabase.SESSION=<token>"
```

### Question Returns Wrong Data
- Check filter mappings in SQL preview
- Verify field type settings (string vs number)
- Confirm timezone alignment for date columns
- Look for implicit joins in GUI queries

### Permission Errors
| Error | Cause | Fix |
|-------|-------|-----|
| "You don't have permission" | Collection access | Share collection with group |
| "Not found" | Sandbox restriction | Check row-level permissions |
| "Question not visible" | Sub-collection nesting | Move to parent collection |

## 8.4 Embedding Issues

### Looker Embed Not Rendering
1. Validate embed host is whitelisted in `embed_secret`
2. Check `allow_looker_embedding` is enabled
3. Verify CORS headers on parent page
4. Test with `allow=" *"` initially, then restrict

### Metabase iFrame Blocked
- Ensure parent page sends `X-Frame-Options: ALLOWALL` or CSP `frame-ancestors`
- For Chrome extension embedding, use `sandbox="allow-scripts allow-same-origin"`
- JWT token must include `exp` (expiration) claim

## 8.5 Performance Optimization Checklist

- [ ] Query uses indexes on join keys
- [ ] Date filters pushed to database layer
- [ ] Large aggregations use pre-computed tables
- [ ] Dashboard has < 10 cards to minimize load
- [ ] Caching enabled (datagroup in Looker, caching in Metabase)
- [ ] No `SELECT *` in derived tables
- [ ] Dimension defaults set for common filters

## 8.6 Debug Commands

### Looker CLI (looker-tools)
```bash
# Validate LookML
looker-validate

# Test explore
looker explore test_model.test_explore --generate

# Profile query
looker profile --model=test_model --explore=test_explore
```

### Metabase API Debugging
```bash
# Get query raw SQL
curl "https://metabase/api/card/1/query" \
  -H "Cookie: metabase.SESSION=<token>"

# Check field values
curl "https://metabase/api/field/1234/values"
```
