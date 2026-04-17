# Troubleshooting Guide

## 8.1 SOQL & Query Issues

### Query Timeout
- Add WHERE clause to filter data
- Use selective fields
- Avoid functions in WHERE
- Check index usage

### Empty Results
- Verify field API names
- Check sharing rules
- Use Workbench to test query

## 8.2 Deployment Issues

### Package Upload Failed
- Check code coverage > 75%
- Verify all dependencies included
- Review test class results

## 8.3 Governor Limits

### CPU Timeout
- Move logic to async
- Reduce loop iterations
- Use batch apex

### Heap Size Exceeded
- Use SOQL for loops
- Clear collections in loops
- Send data in chunks

## 8.4 Test Class Issues

### Code Coverage Failed
- Add test methods for each branch
- Use @TestSetup for data
- Test negative cases

## 8.5 Debug Commands

```bash
# Anonymous Apex for debugging
System.debug('Debug: ' + variable);
System.assertEquals(expected, actual);
```

```apex
// Check limits
System.debug('CPU: ' + Limits.getCpuTime() + '/' + Limits.getLimitCpuTime());
System.debug('Heap: ' + Limits.getHeapSize() + '/' + Limits.getLimitHeapSize());
```