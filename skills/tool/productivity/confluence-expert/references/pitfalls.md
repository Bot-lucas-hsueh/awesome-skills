# Common Pitfalls & Anti-Patterns

## 10.1 Content Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **Duplicate content** | Medium | Use CQL to find duplicates before creating |
| 2 | **No naming conventions** | Medium | Establish and enforce naming standards |
| 3 | **Flat structure (no hierarchy)** | Medium | Use parent pages and spaces |
| 4 | **Outdated content without review dates** | High | Add "Last Reviewed" field |
| 5 | **Copy-pasting content between pages** | Medium | Use page includes or links |
| 6 | **Heavy use of attached files** | Low | Embed content directly |
| 7 | **No labels/taxonomy** | Low | Implement label strategy |

## 10.2 API Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Polling for changes instead of webhooks | Performance | Use webhooks for real-time updates |
| Not respecting rate limits | API failures | Implement backoff and caching |
| Ignoring content version conflicts | Data loss | Check ETag/If-Match headers |
| No pagination | Memory issues | Always paginate large result sets |
| Using deprecated endpoints | Breaking changes | Use current API version |
| Storing credentials in code | Security breach | Use environment variables |

## 10.3 Space/Structure Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Too many spaces | Fragmentation | Consolidate or use labels |
| No space hierarchy | Disorganization | Create space categories |
| Copying entire spaces | Maintenance burden | Use page templates |
| No archiving strategy | Clutter | Archive old content regularly |
| Overly restrictive permissions | Collaboration barriers | Use group-based permissions |
| Mixing content types in one space | Confusion | Separate docs, how-tos, policies |

## 10.4 Page/Content Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Very long pages (>5000 words) | Hard to navigate | Split into multiple pages |
| No table of contents | Poor UX | Add TOC macro |
| Missing page descriptions | SEO/UX issues | Add excerpt/introduction |
| Using deprecated macros | Rendering issues | Update to current macros |
| Hardcoded dates that age badly | Staleness | Use dynamic date macros |
| Overly complex storage format | Editor confusion | Simplify to standard format |

## 10.5 Automation Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Automation triggers too frequently | Performance | Set minimum intervals |
| Not handling automation failures | Silent failures | Add error notifications |
| Over-automating content creation | Noise | Human review for quality |
| Automation without audit trail | Compliance risk | Log all automated actions |
| Ignoring automation limits | Failed automations | Check Atlassian limits |

## 10.6 Search Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Not using CQL properly | Poor results | Use proper CQL syntax |
| Searching without filters | Too many results | Add space/type/label filters |
| Ignoring search suggestions | Missed content | Follow suggestion links |
| Not using labels in search | Incomplete results | Include labels in CQL |

## 10.7 Best Practices

1. **Use spaces strategically** - one per team/project, not per document type
2. **Establish naming conventions** - consistent prefixes, dates, versioning
3. **Implement content labeling** - use labels for cross-space organization
4. **Create page templates** - for recurring content types (ADR, runbook, etc.)
5. **Use page includes wisely** - for shared content, not as shortcuts
6. **Set up content health monitoring** - track staleness and gaps
7. **Implement review cycles** - schedule content reviews quarterly
8. **Archive old content** - don't delete, move to archive space
9. **Use automation sparingly** - automate repetitive tasks, not creation
10. **Keep storage format clean** - prefer simple HTML over complex macros
11. **Add metadata** - labels, custom fields, status indicators
12. **Link related content** - use page links, not copy-paste
13. **Test API calls** - use sandbox/dev environment first
14. **Handle rate limits gracefully** - implement exponential backoff
15. **Use version history** - don't be afraid to make changes

## 10.8 Performance Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Large attachments in pages | Slow loading | Use file hosting alternatives |
| Too many embeds per page | Rendering delay | Limit embeds, use links |
| Complex nested page includes | Recursion issues | Flatten structure |
| Unindexed custom content | Slow search | Configure search indexes |
| Too many macros per page | Load time | Optimize macro usage |

## 10.9 Security Considerations

| Concern | Mitigation |
|---------|------------|
| API token exposure | Rotate tokens, use OAuth |
| Sensitive content in pages | Use restricted spaces |
| Public space leaks | Audit space permissions |
| Webhook endpoint security | Verify signatures, use HTTPS |
| Exporting sensitive data | Restrict API access |
| Page permission bypass | Test with different users |
