## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: The God Service

```markdown
❌ BAD: Building one "OrderService" that handles orders, inventory, payments,
notifications, reporting, and analytics (15,000 LOC). 6 teams modify the same file
→ constant merge conflicts → 2 deploys/week blocked on team coordination.

✅ GOOD: Split by business capability. OrderService (create/cancel),
InventoryService (reserve/release), PaymentService (charge/refund).
Each deploys independently. Team A ships payment fixes without blocking Team B.
```

**Anti-Pattern 2: Swallowing Exceptions

```markdown
❌ BAD:
try {
  await sendEmail(user.email);
} catch (e) {
  // email failed, whatever, continue
}
// Result: email failures are silent; user never notified; support tickets pile up

✅ GOOD:
try {
  await sendEmail(user.email);
} catch (e) {
  logger.error({ event: 'email_failed', userId: user.id, error: e.message });
  await retryQueue.add('send-email', { userId: user.id }, { attempts: 3, backoff: 'exponential' });
  throw new EmailDeliveryError(`Email queued for retry: ${e.message}`);
}
```

**Anti-Pattern 3: Raw SQL with User Input

```markdown
❌ BAD (SQL Injection vulnerability):
const users = await db.query(`SELECT * FROM users WHERE email = '${req.body.email}'`);
// Attacker input: "'; DROP TABLE users; --"

✅ GOOD (parameterized query):
const users = await db.query('SELECT * FROM users WHERE email = $1', [req.body.email]);
// Or use ORM: db.users.findOne({ where: { email: req.body.email } })
```

### 🟡 Medium Severity

**Anti-Pattern 4: Missing Idempotency on Mutations

```markdown
❌ BAD: POST /orders creates a new order every time it's called.
Mobile app retries on network timeout → user charged 3 times.

✅ GOOD: Accept Idempotency-Key header, store in Redis with TTL.
Second call with same key returns original response (no duplicate processing).
Standard in Stripe, PayPal, and all major payment APIs.
```

**Anti-Pattern 5: Ignoring P99, Optimizing for Average

```markdown
❌ BAD: "Average response time is 50ms, we're good!"
Reality: P99 is 8 seconds → 1% of users experience 8s load time
→ mobile checkout abandonment → revenue loss.

✅ GOOD: Track p50, p95, p99. Alert on p99 > 500ms for critical paths.
Set SLO as p99 latency, not average. Use percentile-based APM dashboards.
```

**Anti-Pattern 6: SELECT * in Production

```markdown
❌ BAD: SELECT * FROM orders → fetches 50 columns including large JSONB blobs
→ 10× network transfer overhead → slow queries, high memory usage.

✅ GOOD: SELECT id, status, total, created_at FROM orders
→ Only fetch what the API response needs.
Add a linting rule or code review gate to reject SELECT * in query files.
```

---

