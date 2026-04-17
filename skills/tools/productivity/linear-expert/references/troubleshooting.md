# Troubleshooting Guide

## 8.1 API Issues

### Invalid API Key
- Verify key in header: `Authorization: Bearer <key>`
- Check API key permissions
- Verify workspace ID correct

## 8.2 GraphQL Issues

### Query Returns Empty
- Verify ID correct
- Check query variables
- Review error in response

## 8.3 Webhooks

### Webhook Not Received
- Verify endpoint reachable
- Check webhook signing key
- Review event settings