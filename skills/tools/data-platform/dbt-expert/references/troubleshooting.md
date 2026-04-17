# Troubleshooting Guide

## 8.1 Compilation Issues

### Cannot Find Ref
- Check model name spelling
- Verify model exists in project
- Check package dependencies
- Ensure package installed: `dbt deps`

### Invalid Schema
- Check YML indentation
- Verify column types
- Run: `dbt docs generate`

## 8.2 Execution Issues

### Model Not Materializing
- Check database/warehouse connection
- Verify target schema exists
- Run with debug: `dbt -debug run -s model_name`

### Long Running Models
- Add limits for testing
- Check query performance
- Consider incremental models

## 8.3 Testing Issues

### Tests Failing
- Review test results: `dbt test --store-failures`
- Check actual vs expected values
- Verify source data changed
- Review schema.yml config

## 8.4 Package Issues

### Package Not Found
- Check packages.yml syntax
- Verify git URL correct
- Run: `dbt deps`

## 8.5 Documentation Issues

### Docs Not Updating
```bash
# Regenerate docs
dbt docs generate
dbt docs serve
```

## 8.6 dbt Cloud Issues

### Job Failing in Cloud
- Check git repository sync
- Review environment settings
- Verify environment variables set
- Check run timeout settings