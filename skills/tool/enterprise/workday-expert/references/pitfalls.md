# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Pitfall | Severity | Quick Fix |
|---|---------|----------|-----------|
| 1 | **Hardcoding tenant ID in integration scripts** | 🔴 High | Use environment variables / vault |
| 2 | **Ignoring API rate limits (1000 req/min default)** | 🔴 High | Implement exponential backoff; batch requests |
| 3 | **Using v1 REST API in new integrations** | 🔴 High | Migrate to v2+ (required from v38.0+) |
| 4 | **Storing OAuth tokens in plaintext** | 🔴 High | Use credential vault; rotate regularly |
| 5 | **Not pinning API version in production** | 🔴 High | Lock to `v41.0`; test new versions in sandbox first |
| 6 | **Missing null/empty checks on optional fields** | 🔴 Medium | Always check `wd:Field[text()] != ''` in XSLT |
| 7 | **EIB large file loads during business hours** | 🔴 High | Schedule off-peak (2-5 AM); use delta loads |
| 8 | **Not using Workday's built-in retry for transient failures** | 🟡 Medium | Configure EIB retry: 3 attempts, exponential backoff |
| 9 | **Modifying Delivered Business Processes without cloning** | 🔴 High | Always clone before customization |
| 10 | **Granting System Implementer role to service accounts** | 🔴 High | Use least-privilege: Integration System User role |

### OAuth / API Security Mistakes

```python
# BAD: Hardcoded secrets
CLIENT_SECRET = "super-secret-password-123"

# GOOD: Environment variables / vault
import os
CLIENT_SECRET = os.environ["WORKDAY_CLIENT_SECRET"]
# Or use: from workday_vault import get_secret

# BAD: Token never refreshed
access_token = get_token()  # used forever

# GOOD: Token caching with expiration check
import time
class WorkdayClient:
    def __init__(self):
        self._token = None
        self._token_expires = 0
    
    def get_token(self):
        if time.time() < self._token_expires - 60:
            return self._token  # still valid
        # Refresh
        resp = self._request_token()
        self._token = resp["access_token"]
        self._token_expires = time.time() + resp["expires_in"]
        return self._token
```

### XSLT Null Handling Mistakes

```xml
<!-- BAD: No null check → empty string passed to required field -->
<wd:Primary_Work_Email>
    <xsl:value-of select="//Email"/>
</wd:Primary_Work_Email>

<!-- GOOD: Null-safe with default -->
<wd:Primary_Work_Email>
    <xsl:choose>
        <xsl:when test="string(//Email)">
            <xsl:value-of select="//Email"/>
        </xsl:when>
        <xsl:otherwise>
            <xsl:value-of select="concat(//Employee_ID, '@company.com')"/>
        </xsl:otherwise>
    </xsl:choose>
</wd:Primary_Work_Email>
```

## 10.2 Performance & Configuration Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **Fetching full worker list every sync** | 🔴 High | Use Change Event + Delta sync; track `last_modified` |
| 2 | **EIB transformation with excessive string manipulation** | 🟡 Medium | Use XSLT 2.0 functions; pre-validate source data |
| 3 | **No error queue / dead-letter handling** | 🟡 Medium | Configure EIB error output → SFTP `/errors/` folder |
| 4 | **Single-threaded EIB processing** | 🟡 Medium | Enable parallel processing in Integration Cloud settings |
| 5 | **No monitoring on long-running EIB jobs** | 🟡 Medium | Set alerts for jobs > 30 minutes; SLA breach warning |
| 6 | **Overlapping EIB schedules (file contention)** | 🟡 Medium | Stagger schedules by 15-minute windows |
| 7 | **Large payload in single REST call (no pagination)** | 🟡 Medium | Use `limit=100` + `offset` for > 100 records |
| 8 | **Not using Workday's schema validation pre-submit** | 🟡 Medium | Test XSD validation in sandbox before production |
| 9 | **Business process loops (approval → reject → resubmit → loop)** | 🟡 Medium | Add "rejection count" guard; escalate after 2 rejections |
| 10 | **Compensating for missing Workday features via custom code** | 🟡 Medium | Raise enhancement request; custom code breaks on upgrade |

### Delta Sync Instead of Full Load

```python
# BAD: Full load every time → slow, expensive
workers = requests.get(
    f"{BASE}/workers?limit=1000",
    headers=auth_headers
).json()["data"]

# GOOD: Incremental delta sync
import datetime
LAST_SYNC_FILE = "/data/last_sync_timestamp.txt"

def get_last_sync():
    try:
        with open(LAST_SYNC_FILE) as f:
            return f.read().strip()
    except FileNotFoundError:
        # First run: 30 days ago
        return (datetime.now() - timedelta(days=30)).isoformat()

def update_last_sync(timestamp):
    with open(LAST_SYNC_FILE, "w") as f:
        f.write(timestamp)

last_sync = get_last_sync()
workers = requests.get(
    f"{BASE}/workers?limit=100&updated=gt[{last_sync}]",
    headers=auth_headers
).json()["data"]

# Process workers...

# Save the latest updated timestamp
if workers:
    update_last_sync(workers[-1]["updated"])
```

### Batch Processing for Large Loads

```python
# Process in batches of 100
def get_all_workers(base_url, token, batch_size=100):
    all_workers = []
    offset = 0
    
    while True:
        resp = requests.get(
            f"{base_url}/workers?limit={batch_size}&offset={offset}",
            headers={"Authorization": f"Bearer {token}"},
            params={"fields": "WID,Employee_ID,Legal_Name,Primary_Work_Email"}
        )
        resp.raise_for_status()
        batch = resp.json()["data"]
        
        if not batch:
            break
            
        all_workers.extend(batch)
        offset += batch_size
        print(f"Fetched {len(all_workers)} workers...")
        
        # Respect rate limits between batches
        if len(batch) == batch_size:
            time.sleep(1.1)  # Stay under 60 req/min if needed
    
    return all_workers
```

### EIB Error Handling Configuration

```
Integration System: "HCM Worker Inbound"
    Error Handling:
        ├── On Parse Error: → /errors/worker_[timestamp]_parse.txt
        ├── On Validation Error: → /errors/worker_[timestamp]_validation.txt
        ├── On Transformation Error: → /errors/worker_[timestamp]_transform.txt
        ├── On Submit Error: → /errors/worker_[timestamp]_submit.txt
        │
        Retry Policy:
        ├── Attempts: 3
        ├── Backoff: Exponential (30s, 60s, 120s)
        │
        Notification:
        └── Email: integration-team@company.com (on final failure)
```
