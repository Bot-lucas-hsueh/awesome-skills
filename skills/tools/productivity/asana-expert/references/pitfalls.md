# Common Pitfalls & Anti-Patterns

## 10.1 API Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **Not handling pagination** | High | Always iterate over next_page |
| 2 | **Ignoring rate limits** | High | Implement exponential backoff |
| 3 | **Storing tokens in code** | High | Use environment variables |
| 4 | **Not handling 429 errors** | High | Check Retry-After header |
| 5 | **Missing opt_fields** | Medium | Request only needed fields |
| 6 | **Making synchronous calls in loops** | Medium | Use batch requests |
| 7 | **Not caching workspace/project lookups** | Medium | Implement caching layer |
| 8 | **Ignoring webhook signatures** | High | Always verify HMAC signature |

## 10.2 Task Management Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Tasks without due dates | No urgency tracking | Always set due dates |
| Too many subtasks | Complexity bloat | Use linked projects |
| Over-assigning tasks | Accountability loss | Single owner per task |
| No task descriptions | Context loss | Add detailed notes |
| Missing followers | Visibility gaps | Auto-add stakeholders |
| One person owns everything | Bottleneck | Distribute ownership |

## 10.3 Project Structure Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Flat project structure | Hard to navigate | Use sections and milestones |
| No naming conventions | Confusion | Establish naming standards |
| Too many projects | Overhead | Consolidate related work |
| No project templates | Repetition | Create reusable templates |
| Mixing work types | Unclear priorities | Separate project types |
| No project overview | Context loss | Add project briefs |

## 10.4 Automation Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Too aggressive webhooks | Rate limits | Filter events carefully |
| Not handling sync failures | Data loss | Implement dead letter queue |
| Over-automating | Spamming users | Get user consent |
| Creating too many tasks | Noise | Aggregate related items |
| Ignoring task limits | API errors | Check workspace limits |
| Not testing in sandbox | Production issues | Use test workspace |

## 10.5 OAuth Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Storing refresh tokens insecurely | Security breach | Use encrypted storage |
| Not handling token refresh | Auth failures | Implement refresh logic |
| Requesting too many scopes | User trust | Request minimal scopes |
| Hardcoded redirect URIs | Rigidity | Validate dynamically |
| No token rotation | Security risk | Rotate tokens regularly |
| Ignoring token expiry | Sudden failures | Check expiry proactively |

## 10.6 Best Practices

1. **Use Personal Access Tokens** for testing, OAuth 2.0 for production
2. **Always specify `opt_fields`** to reduce response size
3. **Implement pagination** properly using `next_page()` method
4. **Handle rate limits** with exponential backoff (1500 requests/minute)
5. **Verify webhook signatures** before processing events
6. **Store credentials in environment variables**, never in code
7. **Use batch requests** for multiple operations
8. **Add task descriptions** with context, links, and acceptance criteria
9. **Set due dates** and assignees for accountability
10. **Use custom fields** consistently for tracking (priority, estimate, status)
11. **Add followers** to tasks for stakeholder visibility
12. **Use sections** to organize work within projects
13. **Implement proper error handling** with retry logic
14. **Test webhook endpoints** locally with ngrok
15. **Monitor API usage** to avoid hitting limits

## 10.7 Integration Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Direct API calls on every request | Performance | Cache frequently accessed data |
| No retry on transient failures | Reliability | Implement retry with backoff |
| Not handling workspace differences | Broken integrations | Normalize data across workspaces |
| Ignoring custom field types | Data corruption | Handle all custom field types |
| No idempotency | Duplicate data | Use unique identifiers |
| Not handling deleted resources | Stale data | Clean up deleted references |

## 10.8 Security Considerations

| Concern | Mitigation |
|---------|------------|
| Token exposure | Use environment variables, rotate regularly |
| Webhook spoofing | Always verify HMAC signatures |
| Excessive permissions | Request only necessary scopes |
| Data privacy | Don't log sensitive task data |
| API abuse | Implement rate limiting in your app |
| OAuth callback | Validate state parameter |
