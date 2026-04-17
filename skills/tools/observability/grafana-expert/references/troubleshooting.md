# Troubleshooting Guide

## 8.1 Dashboard Issues

### Panel Not Loading
- Check datasource configured
- Verify query syntax
- Check query timeout
- Review browser console

### Data Missing
- Check time range
- Verify variable values
- Check query results in Explore

## 8.2 Datasource Issues

### Datasource Not Working
- Test datasource: Settings > Data Sources > Test
- Check URL correct
- Verify credentials
- Check proxy settings

## 8.3 Authentication

### Login Failed
- Check auth settings in grafana.ini
- Verify LDAP/ OAuth config
- Check user permissions

## 8.4 Performance

### Slow Dashboard
- Reduce number of panels
- Use lower resolution
- Enable caching
- Use query variables

## 8.5 Alert Issues

### Alert Not Firing
- Check alert configuration
- Verify notification channel
- Check evaluation interval
- Review alert logs