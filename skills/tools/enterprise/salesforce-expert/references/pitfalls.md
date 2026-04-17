# Common Pitfalls & Anti-Patterns

## 10.1 Apex Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **Queries inside loops** | High | Move SOQL outside loops |
| 2 | **Missing Security Enforced** | High | Add WITH SECURITY_ENFORCED |
| 3 | **DML inside loops** | High | Collect and bulkify DML |
| 4 | **Not handling exceptions** | High | Use try-catch blocks |
| 5 | **Using @future without chain** | Medium | Use Queueable instead |
| 6 | **Hardcoding IDs** | High | Use Custom Settings/Labels |
| 7 | **Ignoring CRUD/FLS** | High | Use Schema methods |
| 8 | **Synchronous long operations** | Medium | Use Batch/Queueable |

## 10.2 SOQL Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Select * | Governor limit | Select only needed fields |
| Nested SOQL in loops | CPU timeout | Pre-fetch data |
| Queries without WHERE | Full table scans | Always filter |
| No LIMIT on large queries | Memory issues | Add reasonable limits |
| Date literals without format | Errors | Use proper format |
| No sharing rules consideration | Security issues | Check WITH sharing |

## 10.3 Governor Limit Violations

| Limit | Default | Mitigation |
|-------|---------|------------|
| SOQL queries | 100 | Use aggregate, limits in code |
| DML statements | 150 | Use Database methods |
| CPU time | 10s | Optimize loops, avoid recursion |
| Heap size | 6MB | Use pagination, streaming |
| Callouts | 100 | Batch callouts |
| Queueable chain | 1 chain | Use Batch for complex flows |

## 10.4 Trigger Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Logic in trigger | Untestable | Use handler pattern |
| No recursion guard | Multiple updates | Use static flag |
| No order of execution | Confusion | Document and test |
| Trigger.new modified | State confusion | Use before triggers |
| Missing null checks | NullPointerException | Validate inputs |

## 10.5 API Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| No pagination | Large payloads | Use pagination |
| No error handling | Silent failures | Check status codes |
| No retry logic | Integration failures | Implement exponential backoff |
| Hardcoded endpoints | Rigidity | Use Named Credentials |
| Not handling timeouts | Hanging requests | Set timeout values |

## 10.6 Lightning Web Component Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| No error boundary | Blank page | Add error handling |
| Large data sets | Slow rendering | Use pagination/infinite |
| Direct Apex calls | Cache misses | Use Lightning Data Service |
| No @wire caching | API limits | Cache with refresh |
| Missing accessibility | Compliance | Use ARIA labels |

## 10.7 Best Practices

1. **Always use with sharing** on classes to enforce record access
2. **Add WITH SECURITY_ENFORCED** to all SOQL queries
3. **Bulkify triggers** - handle lists, not individual records
4. **Use specific field selects** - avoid SELECT *
5. **Implement error handling** - try-catch with meaningful messages
6. **Use Limits class** - check limits before operations
7. **Prefer @wire over Apex** - for simple read operations
8. **Use Custom Metadata** - for configuration over Custom Settings
9. **Test with large data volumes** - not just unit tests
10. **Document complex logic** - inline comments for business rules
11. **Use Schema methods** - for field/permission checks
12. **Implement caching** - for frequently accessed data
13. **Use Platform Events** - for async, reliable messaging
14. **Follow naming conventions** - classes, methods, variables
15. **Keep methods small** - single responsibility principle

## 10.8 Security Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| SOQL injection | Data breach | Use bind variables |
| User input not sanitized | XSS | Encode output |
| Hardcoded credentials | Breach | Use Named Credentials |
| No FLS checks | Unauthorized access | Check field access |
| Exposing IDs | ID enumeration | Validate record access |
| Sensitive data in logs | Compliance | Mask sensitive fields |

## 10.9 Performance Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Large VF pages | Slow load | Use pagination |
| Unoptimized queries | Timeouts | Add indexes, filters |
| Recursive triggers | CPU spike | Use guard flags |
| Large view state | Page size error | Minimize view state |
| No caching | API overuse | Implement caching |
| N+1 queries | CPU timeout | Use aggregate queries |
