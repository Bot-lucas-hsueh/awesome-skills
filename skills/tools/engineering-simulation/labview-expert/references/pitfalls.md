# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Quick Fix |
|---|---------|----------|-----------|
| 1 | **No error handling** | 🔴 High | Wire error clusters |
| 2 | **Blocking UI thread** | 🔴 High | Use notifiers, queues |
| 3 | **Memory leaks** | 🔴 High | Close refs, use cleanup |
| 4 | **Race conditions** | 🔴 High | Use mutexes, semaphores |
| 5 | **Poor wire management** | 🟡 Medium | Auto-cleanup, tunnels |
| 6 | **Hardcoded values** | 🟡 Medium | Use configuration |
| 7 | **No timing specification** | 🔴 High | Use Wait functions |
| 8 | **Missing initialization** | 🔴 High | Initialize resources |

## 10.2 Solver/Execution Issues

### Performance Issues

**Common Causes & Solutions**:

| Issue | Solution |
|-------|----------|
| Slow loop execution | Enable parallel execution |
| Memory growth | Close file handles, refs |
| UI freezing | Use producer-consumer |
| Priority inversion | Use correct priorities |

### Timing Problems

**Issues**:
- **Jitter**: Use hardware timing
- **Drift**: Sync with reference clock
- **Missed samples**: Increase buffer size
- **Race conditions**: Use synchronization

### Debugging Tips

1. Enable *Highlight Execution*
2. Use *Probe* on wires
3. Check *Execution Trace*
4. Review *Profile Performance*
5. Enable *Run-Time Menu* for testing