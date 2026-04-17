# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Prevention |
|---|---------|----------|------------|
| 1 | **Not validating signatures** | Critical | Always verify Slack signing secret |
| 2 | **Missing request acknowledgment** | High | Always return 200 within 3 seconds |
| 3 | **Excessive API calls** | Medium | Batch requests, cache user info |
| 4 | **Ignoring rate limits** | High | Implement backoff, monitor limits |
| 5 | **Storing tokens insecurely** | Critical | Use environment variables, secrets manager |
| 6 | **Not handling duplicates** | Medium | Use event IDs, idempotent handlers |
| 7 | **Long-running handlers** | High | Process async, respond immediately |
| 8 | **Missing error handling** | High | Wrap in try-catch, log errors |

### Anti-Pattern: Sync Response with API Calls

```javascript
// BAD - Too slow
app.command('/search', async ({ ack, client, body }) => {
  await ack();
  const results = await slowDatabaseQuery(); // 5 seconds
  await client.chat.postMessage({ channel: body.channel_id, text: results });
});

// GOOD - Respond immediately
app.command('/search', async ({ ack, body }) => {
  await ack('Searching...');
  // Process in background, send result later
  processSearchAsync(body.user_id, body.text);
});
```

## 10.2 Anti-Patterns

### 1. No Rate Limit Handling

```
Anti-Pattern:
for (const user of users) {
  await client.chat.postMessage({ channel: user.id, text: message });
}

Problem: API rate limit exceeded, bot disabled

Solution:
async function sendBulkMessages(users, message) {
  const batches = chunk(users, 50); // Max 50 per minute
  for (const batch of batches) {
    await Promise.all(batch.map(u => client.chat.postMessage(...)));
    await sleep(60000); // Wait 1 minute between batches
  }
}
```

### 2. Storing State in Memory

```
Anti-Pattern:
let pendingActions = {};

Problem: Bot restart loses state, no horizontal scaling

Solution:
- Use Redis or database for state
- Store complete context in view/option payloads
- Use Slack's built-in state parameter
```

### 3. Hardcoding Channel/User IDs

```
Anti-Pattern:
client.chat.postMessage({ channel: 'C0123456789', ... });

Problem: Works in dev, fails in prod with different workspace

Solution:
- Use conversation name lookup: #general
- Store mappings in config/database
- Use SLACK_CHANNEL_GENERAL env variable
```

### 4. Not Using App Home Properly

```
Anti-Pattern:
Sending all messages to DM channels
No persistent state for users

Solution:
- Use Home tab for persistent UI
- views.publish for user dashboards
- Update on relevant events
```

### 5. Ignoring Message Formatting

```
Anti-Pattern:
text: "Important message! Visit example.com"

Problem: Plain text, no links, hard to read

Solution:
Use Block Kit properly:
{
  type: "section",
  text: {
    type: "mrkdwn",
    text: "*Important!* :warning:\nVisit <https://example.com|our dashboard> for details."
  }
}
```

## 10.3 Security Anti-Patterns

| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Logging tokens/sensitive data | Credential leak | Sanitize logs |
| No request validation | Injection attacks | Validate all inputs |
| Direct database queries from messages | SQL injection | Use parameterized queries |
| Exposing internal APIs via bot | Data breach | Add authentication |
| No permission checks | Privilege escalation | Check scopes before actions |

## 10.4 Performance Anti-Patterns

```javascript
// BAD: N+1 API calls
async function getUserInfo(userId) {
  const user = await client.users.info({ user: userId });
  const presence = await client.users.getPresence({ user: userId });
  const profile = await client.users.profile.get({ user: userId });
  return { ...user, ...presence, ...profile };
}

// GOOD: Single call where possible
async function getUserInfo(userId) {
  const user = await client.users.info({ user: userId });
  // Presence is separate API but still batch if needed
}

// BAD: No caching
async function getTeamMembers() {
  return await client.users.list(); // Called every time
}

// GOOD: Cache with TTL
const cache = new Map();
async function getTeamMembers() {
  if (cache.has('members')) return cache.get('members');
  const result = await client.users.list();
  cache.set('members', result.users);
  setTimeout(() => cache.delete('members'), 3600000); // 1 hour
  return result.users;
}
```

## 10.5 Error Handling Anti-Patterns

```javascript
// BAD: Swallowing errors
try {
  await client.chat.postMessage({ channel, text });
} catch (e) {
  // Nothing
}

// BAD: Catching too broadly
try {
  everything();
} catch (e) {
  console.error(e); // Don't know what failed
}

// GOOD: Specific handling
try {
  await client.chat.postMessage({ channel, text });
} catch (error) {
  if (error.code === 'channel_not_found') {
    await handleInvalidChannel(channel);
  } else if (error.code === 'not_authed') {
    await reAuthenticate();
  } else {
    throw error; // Re-throw unexpected
  }
}
```
