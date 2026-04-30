# Slack API Reference

> Complete reference for Slack platform APIs and integration patterns.

---

## API Types Overview

| API Type | Use Case | Protocol |
|----------|----------|----------|
| **Web API** | RESTful operations | HTTPS/JSON |
| **Events API** | Real-time events | HTTP callbacks |
| **Socket Mode** | Firewall-friendly apps | WebSocket |
| **RTM API** | Legacy real-time | WebSocket |
| **SCIM API** | User provisioning | REST |
| **Audit Logs API** | Compliance/Security | REST |
| **Status API** | System status | REST |

---

## Web API Methods

### Core Methods

#### Conversations
```http
POST https://slack.com/api/conversations.list
Content-Type: application/json; charset=utf-8
Authorization: Bearer xoxb-your-token

{
  "types": "public_channel,private_channel",
  "exclude_archived": true,
  "limit": 100
}
```

**Key Methods:**
| Method | Description |
|--------|-------------|
| `conversations.info` | Get channel details |
| `conversations.create` | Create new channel |
| `conversations.join` | Join a channel |
| `conversations.invite` | Invite users |
| `conversations.archive` | Archive channel |
| `conversations.history` | Get message history |

#### Chat
```http
POST https://slack.com/api/chat.postMessage
Content-Type: application/json
Authorization: Bearer xoxb-your-token

{
  "channel": "C1234567890",
  "text": "Hello, world!",
  "blocks": [...],
  "thread_ts": "1234567890.123456"
}
```

**Key Methods:**
| Method | Description |
|--------|-------------|
| `chat.postMessage` | Send message |
| `chat.update` | Update message |
| `chat.delete` | Delete message |
| `chat.getPermalink` | Get message permalink |
| `chat.scheduleMessage` | Schedule message |

#### Users
```http
GET https://slack.com/api/users.info?user=U1234567890
Authorization: Bearer xoxb-your-token
```

**Key Methods:**
| Method | Description |
|--------|-------------|
| `users.info` | Get user details |
| `users.list` | List all users |
| `users.lookupByEmail` | Find by email |
| `users.setPresence` | Set status/presence |
| `users.profile.set` | Update profile |

---

## Events API

### Event Types

```json
{
  "token": "XXYYZZ",
  "team_id": "TXXXXXXXX",
  "api_app_id": "AXXXXXXXXX",
  "event": {
    "type": "message",
    "channel": "CXXXXXXXX",
    "user": "UXXXXXXXX",
    "text": "Hello",
    "ts": "1234567890.123456"
  },
  "type": "event_callback",
  "authed_users": ["UXXXXXXXX"]
}
```

**Common Events:**
| Event | Trigger |
|-------|---------|
| `message` | New message posted |
| `app_mention` | App @mentioned |
| `reaction_added` | Reaction added |
| `channel_created` | New channel created |
| `member_joined_channel` | User joined channel |
| `file_shared` | File shared |
| `app_home_opened` | User opened app home |

### URL Verification
```json
// Incoming challenge
{
  "token": "Jhj5dZrVaK7ZwHHjRyZWjbDl",
  "challenge": "3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P",
  "type": "url_verification"
}

// Response
{
  "challenge": "3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P"
}
```

---

## OAuth Scopes

### Bot Token Scopes

| Scope | Permission |
|-------|------------|
| `chat:write` | Post messages |
| `chat:write.public` | Post to public channels |
| `channels:read` | View public channels |
| `groups:read` | View private channels |
| `im:read` | View DMs |
| `mpim:read` | View group DMs |
| `users:read` | View user info |
| `files:write` | Upload files |
| `reactions:write` | Add reactions |
| `commands` | Add slash commands |

### User Token Scopes

| Scope | Permission |
|-------|------------|
| `channels:history` | Access channel history |
| `groups:history` | Access private channel history |
| `im:history` | Access DM history |
| `search:read` | Search messages |
| `users:read.email` | View email addresses |
| `admin.*` | Admin operations |

---

## Rate Limits

### Tier Limits

| Tier | Requests/Minute | Methods |
|------|-----------------|---------|
| **Tier 1** | 1+ per minute | `conversations.list` |
| **Tier 2** | 20+ per minute | `chat.postMessage` |
| **Tier 3** | 50+ per minute | `users.info` |
| **Tier 4** | 100+ per minute | Most methods |
| **Special** | Varies | Search, SCIM |

### Rate Limit Response
```http
HTTP/1.1 429 Too Many Requests
Retry-After: 10
X-RateLimit-Limit: 50
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1234567890
```

### Handling Strategy
```python
import time
from slack_sdk.errors import SlackApiError

def call_with_retry(client, method, **kwargs):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            return client.api_call(method, **kwargs)
        except SlackApiError as e:
            if e.response.status_code == 429:
                retry_after = int(e.response.headers.get('Retry-After', 1))
                time.sleep(retry_after)
            else:
                raise
    raise Exception("Max retries exceeded")
```

---

## Authentication

### Token Types

| Token Type | Format | Use Case |
|------------|--------|----------|
| **Bot Token** | `xoxb-*` | App actions |
| **User Token** | `xoxp-*` | User-context actions |
| **App-Level Token** | `xapp-*` | Socket Mode |
| **Verification Token** | Static | Request verification |
| **Signing Secret** | `*...` | Request signing |

### Request Signing (Recommended)
```python
import hmac
import hashlib

def verify_request(signing_secret, request_body, timestamp, signature):
    # Check timestamp (prevent replay attacks)
    if abs(time.time() - int(timestamp)) > 60 * 5:
        return False
    
    # Create signature
    sig_basestring = f"v0:{timestamp}:{request_body}"
    my_signature = 'v0=' + hmac.new(
        signing_secret.encode(),
        sig_basestring.encode(),
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(my_signature, signature)
```

---

## Error Handling

### Common Error Codes

| Error | Meaning | Resolution |
|-------|---------|------------|
| `channel_not_found` | Channel doesn't exist | Check channel ID |
| `not_in_channel` | Bot not in channel | Join channel first |
| `rate_limited` | Too many requests | Implement backoff |
| `invalid_auth` | Bad token | Verify token |
| `missing_scope` | Insufficient permissions | Add required scope |
| `account_inactive` | User deactivated | Check user status |
| `msg_too_long` | Message exceeds limit | Split into multiple |

### Error Response Format
```json
{
  "ok": false,
  "error": "channel_not_found",
  "needed": "more_permissions",
  "provided": "existing_permissions"
}
```
