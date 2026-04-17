# Troubleshooting Guide

## 8.1 DNS Resolution Issues

### Zone Not Resolving
```bash
# Check zone status
curl -s -H "Authorization: Bearer $CF_TOKEN" \
  "https://api.cloudflare.com/client/v4/zones/$ZONE_ID" | jq .

# Verify nameservers
dig +short NS yourdomain.com
dig +short @f1g1ns1.dnspod.net yourdomain.com
```

### Record Propagation
- DNS changes can take up to 24 hours (usually minutes)
- Use Cloudflare Dashboard > DNS > Status to check
- Purge resolver cache: `dnsflush` (macOS) or `ipconfig /flushdns` (Windows)

### CNAME Flattening
- CNAME to root domain requires flattening enabled
- Check Proxy status in dashboard
- Use "Resolve Override" for apex CNAME

## 8.2 SSL/TLS Issues

### SSL Not Working
1. Check SSL/TLS mode in dashboard (should be Full or Flexible)
2. Verify origin certificate valid
3. Check "Always Use HTTPS" enabled
4. Check Mixed Content issues

### Certificate Errors
```bash
# Check certificate details
openssl s_client -connect yourdomain.com:443 -servername yourdomain.com

# Test SSL score
curl -vI https://yourdomain.com
```

### Mixed Content
- Enable "Automatic HTTPS Rewrites"
- Update resources to HTTPS
- Use CSP to identify issues

## 8.3 Performance Issues

### Slow Response Times
- Enable "Brotli" compression
- Review cache settings
- Check Origin response time
- Use Cloudflare Analytics

### Cache Not Hitting
- Verify Page Rules cache settings
- Check Cache-Control headers
- Use "Dev Mode" to bypass cache
- Verify cache status in response headers (CF-Cache-Status)

## 8.4 Firewall & Security Issues

### Legitimate Traffic Blocked
- Review Security Events in dashboard
- Check "Challenge" settings
- Add IP to allowlist
- Disable JavaScript challenge for API

### WAF Rules Blocking
```bash
# List WAF rules
curl -H "Authorization: Bearer $CF_TOKEN" \
  "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/firewall/rules"
```

### Rate Limiting
- Adjust rule thresholds
- Whitelist API endpoints
- Use Tiered Cache to reduce origin requests

## 8.5 Workers Issues

### Worker Not Running
- Check Worker logs in Dashboard
- Verify script syntax
- Check execution limits
- Test in playground

### KV/ Durable Objects Issues
- Check for regional restrictions
- Verify binding configuration
- Test with small payloads first

## 8.6 Access Issues

### Zero Trust Gatekeeper Blocked
- Verify Access policy configuration
- Check session cookies
- Review Audit Logs
- Test with incognito window

## 8.7 Dashboard Issues

### API Token Not Working
- Verify token has required permissions
- Check token expiration
- Regenerate token if needed
- Test with: `curl -H "Authorization: Bearer $TOKEN" https://api.cloudflare.com/user/tokens/verify`

## 8.8 Diagnostic Commands

```bash
# Test from multiple locations
curl -I https://yourdomain.com

# Check headers
curl -I -H "Host: yourdomain.com" http://ORIGIN_IP

# Purge cache
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/purge_cache" \
  -H "Authorization: Bearer $CF_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"purge_everything":true}'
```