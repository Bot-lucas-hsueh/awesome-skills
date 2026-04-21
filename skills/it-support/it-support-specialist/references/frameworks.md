## § 7 · Standards & Reference

### ITIL 4 Priority Matrix and SLA Targets

```
┌───────────┬──────────────────────────────┬──────────────┬────────────────┐
│ Priority  │ Definition                   │ Response SLA │ Resolution SLA │
├───────────┼──────────────────────────────┼──────────────┼────────────────┤
│ P1 – Crit │ Complete service outage;     │ 15 minutes   │ 4 hours        │
│           │ multiple users or business-  │              │                │
│           │ critical system down         │              │                │
├───────────┼──────────────────────────────┼──────────────┼────────────────┤
│ P2 – High │ Significant degradation;     │ 1 hour       │ 8 hours        │
│           │ single user fully blocked or │              │                │
│           │ group partially impacted     │              │                │
├───────────┼──────────────────────────────┼──────────────┼────────────────┤
│ P3 – Med  │ Partial impact; user can     │ 4 hours      │ 24 hours       │
│           │ work with workaround;        │              │                │
│           │ non-critical service         │              │                │
├───────────┼──────────────────────────────┼──────────────┼────────────────┤
│ P4 – Low  │ No immediate impact;         │ 8 hours      │ Next business  │
│           │ service request or           │              │ day            │
│           │ enhancement                  │              │                │
└───────────┴──────────────────────────────┴──────────────┴────────────────┘
```

### Service Desk KPI Targets

| Metric | Target | Definition |
|--------|--------|------------|
| First Contact Resolution (FCR) | > 80% | Tickets resolved without escalation or callback |
| Customer Satisfaction (CSAT) | > 4.2
| Ticket Backlog Age | < 3 business days | No open ticket older than 3 days without an update |
| Mean Time to Resolve – P1 | < 4 hours | Clock starts at ticket creation |
| Mean Time to Resolve – P2 | < 8 hours | Clock starts at ticket creation |
| Mean Time to Resolve – P3 | < 24 hours | Business hours only |
| Abandoned Call Rate | < 5% | Calls dropped before agent answer |
| Knowledge Base Utilization | > 40% | Tickets resolved by referencing a KB article |

### Network Diagnostic Command Reference

```bash
# Connectivity test (Windows)
ping -n 20 8.8.8.8                     # packet loss, latency baseline
tracert corporate-server.domain.com     # hop-by-hop routing
nslookup internal-app.domain.com        # DNS resolution check
ipconfig /all                           # adapter config, DHCP lease
netstat -an | findstr :443              # active HTTPS connections
Test-NetConnection -ComputerName host -Port 443  # PowerShell port test

# Connectivity test (macOS/Linux)
ping -c 20 8.8.8.8
traceroute internal-app.domain.com
dig internal-app.domain.com
ip addr show
curl -vI https://internal-app.domain.com 2>&1 | head -30

# Active Directory (PowerShell)
Get-ADUser -Identity jsmith -Properties *           # full user detail
Search-ADAccount -LockedOut | Select Name,SamAccountName  # all locked accounts
Unlock-ADAccount -Identity jsmith                   # unlock account
Set-ADAccountPassword -Identity jsmith -Reset       # force password reset
Get-ADGroupMember -Identity "VPN-Users" -Recursive  # group membership
```

---
