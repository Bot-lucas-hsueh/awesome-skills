# Standards & Reference

## 7.1 Official Documentation

- [PortSwigger Web Security Academy](https://portswigger.net/web-security) - Free web security training
- [Burp Suite Enterprise Edition Docs](https://portswigger.net/burp/documentation/enterprise)
- [Burp Suite Professional Docs](https://portswigger.net/burp/documentation/pro)
- [Burp Suite Collaborator](https://portswigger.net/burp/documentation/collaborator)
- [OWASP Testing Guide v4.2](https://owasp.org/www-project-web-security-testing-guide/)
- [Burp Suite Community Edition](https://portswigger.net/burp/communitydownload)

## 7.2 Configuration Reference

### Proxy Listener Configuration

```
# Basic proxy setup
Proxy Listeners -> Add -> Bind to port: 8080
- Bind to address: All interfaces (or specific interface)
- Enable invisible proxying if needed
- Certificate generation: Generate CA-signed host certificate
```

### Project Options - Connections

```yaml
# TLS Pass Through
*.target-domain.com:443

# Hostname Resolution
10.0.0.1    internal-app.local
10.0.0.2    api.internal.local

# Scope Configuration
Scope -> Include in scope -> Add: ^https?://target\.com/.*
Scope -> Exclude from scope -> Add: ^https?://target\.com\/logout.*
```

### User Options - TLS

```yaml
# Client SSL Certificates
Client TLS negotiation:
  - Import PKCS12 keystore
  - Keystore password
  - Certificate alias

# Upstream Proxy
Upstream proxy servers:
  - Proxy host: proxy.corp.com
  - Proxy port: 8080
  - Authentication: Basic/NTLM/Bearer
```

### Burp Suite Preferences (user.yaml)

```yaml
# ~/.BurpSuitePro/UserConfig.yml (2024.1+)
project_options:
  ssl_inferrable_items: true
  highlights:
    scrollbar_color: "#FFFF00"
  tool_names:
    proxy: "Intercept"
    repeater: "Manual Test"
```

## 7.3 Common Commands

| Command | Description |
|---------|-------------|
| `Ctrl+Shift+P` | Open Proxy settings |
| `Ctrl+Shift+T` | Toggle intercept |
| `Ctrl+Shift+O` | Open target sitemap |
| `Ctrl+Shift+I` | Open Intruder |
| `Ctrl+Shift+R` | Open Repeater |
| `Ctrl+Shift+S` | Open Sequencer |
| `Ctrl+Shift+D` | Open Decoder |
| `Ctrl+Shift+C` | Open Comparer |
| `Ctrl+Shift+L` | Send to Logger++ |
| `Ctrl+B` | Add to scope |
| `Ctrl+Shift+Delete` | Remove from scope |

### Command Line Options

```bash
# Start Burp Suite Professional
java -jar burpsuite_pro.jar --project-file=pentest.bup

# Start with no GUI (headless)
java -jar burpsuite_pro.jar --headless --project-file=pentest.bup

# Start with configuration
java -jar burpsuite_pro.jar --config-file=burp-config.json

# Quick scan with Spider
java -jar burpsuite_pro.jar --spider-url=https://target.com
```

## 7.4 Version Compatibility

| Version | Status | Notes |
|---------|--------|-------|
| 2024.x | Current | Latest features, JQL v2, AI features |
| 2023.x | Supported | Stable, QRL Jacking protection |
| 2022.x | Legacy | Still functional, some deprecated APIs |
| Enterprise 2024.x | Current | CI/CD integration, scheduled scans |
| Burp Mobile Assistant | Current | iOS/Android SSL pinning bypass |

### Java Requirements

| Burp Version | Java Version |
|--------------|--------------|
| 2024.x | Java 17+ |
| 2023.x | Java 11+ |
| 2022.x | Java 11+ |

## 7.5 Use Cases

| Use Case | Tools Used | Burp Features |
|----------|------------|---------------|
| Web app testing | Proxy, Spider, Scanner | Intercept,被动扫描, active scan |
| API testing | Repeater, Decoder | JSON/XML editor, JWT handling |
| Mobile testing | Mobile Assistant | Proxy to mobile device |
| Thick client | Intruder, Collaborator | WebSocket, binary protocols |
| SSO/OAuth testing | Repeater, Extender | Request manipulation, token crafting |
| Red team ops | All tools | Payload generation, session handling |
| Bug bounty | Scanner, Proxy | Fast recon, targeted scanning |
