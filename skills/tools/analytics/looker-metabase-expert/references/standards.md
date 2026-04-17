# Standards & Reference

## 7.1 Official Documentation

### Looker
- [Looker Documentation](https://docs.looker.com) - Official Looker docs and guides
- [LookML Reference](https://docs.looker.com/reference/lookml-reference) - Complete LookML language reference
- [Looker API Reference](https://docs.looker.com/reference/api-and-integration/api-reference) - REST API v3.1
- [Looker Best Practices](https://cloud.google.com/looker/docs/best-practices) - Google Cloud Looker guidance

### Metabase
- [Metabase Documentation](https://www.metabase.com/docs/latest) - Official Metabase docs
- [Metabase API](https://www.metabase.com/docs/latest/api/api-overview) - REST API reference
- [Metabase Embedding](https://www.metabase.com/docs/latest/embedding/start) - Embedded analytics guide
- [Metabase JDBC](https://www.metabase.com/docs/latest/installation-and-operation/running-metabase-on-heroku) - Database connection options

## 7.2 LookML Development Standards

### View Definition Pattern
```lookml
view: order_items {
  sql_table_name: public.order_items ;;
  
  dimension: id {
    primary_key: yes
    type: number
    sql: ${TABLE}.id ;;
  }
  
  dimension: status {
    type: string
    sql: ${TABLE}.status ;;
  }
  
  measure: total_revenue {
    type: sum
    sql: ${sale_price} ;;
    value_format_name: usd_0
  }
  
  measure: order_count {
    type: count_distinct
    sql: ${order_id} ;;
  }
}
```

### Explore with Joins
```lookml
explore: orders {
  join: customers {
    type: left_outer
    sql_on: ${orders.customer_id} = ${customers.id} ;;
  }
  
  join: order_items {
    type: left_outer
    sql_on: ${orders.id} = ${order_items.order_id} ;;
  }
  
  always_filter {
    filters: [orders.status: "-Cancelled", orders.created_date: "24 months"]
  }
}
```

### Derived Table Pattern
```lookml
view: user_order_facts {
  derived_table: {
    sql: |
      SELECT
        user_id,
        COUNT(*) AS total_orders,
        SUM(sale_price) AS lifetime_value,
        MIN(created_at) AS first_order_date
      FROM order_items
      GROUP BY user_id
    ;;
    datagroup_trigger: hourly_datagroup
  }
  
  dimension: user_id { primary_key: yes }
  dimension: total_orders { type: number }
  dimension: lifetime_value { type: number }
  
  measure: avg_lifetime_value {
    type: average
    sql: ${lifetime_value} ;;
  }
}
```

## 7.3 Metabase Collection & Permissions Standards

### Collection Hierarchy
```
Root
├── :analytics (Company Analytics)
│   ├── :marketing (Marketing Team)
│   ├── :sales (Sales Team)
│   └── :product (Product Team)
└── :shared (Cross-team Dashboards)
```

### Data Model Best Practices
- Mark sensitive fields as `Has a value (no nulls)` in field metadata
- Set default formatting per field type (currency, percentage, date)
- Configure named parameters for reusable filters
- Use semantic types: city, state, country, currency, etc.

## 7.4 Performance Best Practices

| Practice | Impact | Implementation |
|----------|--------|----------------|
| Aggregate Awareness | High | Use pre-aggregated tables; define `aggregate_table` in LookML |
| Datagroup Caching | High | Set `datagroup_trigger` for Looker; caching interval in Metabase |
| Limit Explores | High | Only expose needed views in explore |
| Derived Tables | Medium | Pre-compute complex joins; use `persist_with` |
| Index Hints | Medium | Use `sql_always_where` to push filters to DB |

## 7.5 Embedding Security Standards

### Looker Signed Embed URLs
```javascript
const embedUrl = lookerEmbedSDK.createExploreIframe({
  host: 'https://myinstance.looker.com',
  exploreId: 'orders',
  filters: { status: 'active' },
  signedUrl: true
});
```

### Metabase JWT Embedding
- Enable `embedding-secret-key` in admin settings
- Use HMAC-SHA256 signed JWTs with `resource`, `params`, `exp` claims
- Set `iframe` sandbox attributes: `allow-scripts allow-same-origin`
- Implement server-side token generation; never expose secrets client-side

## 7.6 Version Compatibility

| Platform | Version | Status | Notes |
|----------|---------|--------|-------|
| Looker | 23.x+ | Current | Required for Looker AI features |
| Looker | 21.x - 22.x | Supported | Legacy instances |
| Looker Studio | Current | Current | For embedded frontends |
| Metabase | 0.49.x+ | Current | Recommended for new deployments |
| Metabase | 0.46.x - 0.48.x | Supported | Enterprise features require Pro |
