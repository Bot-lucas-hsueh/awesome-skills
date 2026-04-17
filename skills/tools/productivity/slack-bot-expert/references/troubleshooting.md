# Troubleshooting Guide

## 8.1 Bot Not Responding

### Events Not Received
- Verify URL in Slack settings
- Check challenge verification
- Check signing secret

### Permission Issues
- Check OAuth scopes
- Verify bot in channel

## 8.2 API Errors

### rate_limited
- Add retry with backoff
- Check Slack rate limits
- Queue messages