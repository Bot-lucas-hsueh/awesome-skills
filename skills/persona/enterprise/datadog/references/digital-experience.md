# Datadog Digital Experience Reference

> Guide to Real User Monitoring (RUM), Synthetic Monitoring, Session Replay, and Product Analytics

---

## Real User Monitoring (RUM)

### Browser RUM Setup

**NPM Installation:**
```bash
npm install @datadog/browser-rum @datadog/browser-logs
```

**Basic Initialization:**
```typescript
// datadog.ts
import { datadogRum } from '@datadog/browser-rum';
import { datadogLogs } from '@datadog/browser-logs';

export function initMonitoring() {
  // Initialize RUM
  datadogRum.init({
    applicationId: process.env.REACT_APP_DD_RUM_APP_ID!,
    clientToken: process.env.REACT_APP_DD_RUM_CLIENT_TOKEN!,
    site: 'datadoghq.com',
    service: 'ecommerce-web',
    env: 'production',
    version: process.env.REACT_APP_VERSION!,
    
    // Sampling configuration
    sessionSampleRate: 100,
    sessionReplaySampleRate: 20,
    
    // Privacy settings
    defaultPrivacyLevel: 'mask-user-input',
    
    // Tracking options
    trackUserInteractions: true,
    trackResources: true,
    trackLongTasks: true,
    
    // APM integration
    allowedTracingUrls: [
      {
        match: 'https://api.example.com',
        propagatorTypes: ['datadog', 'tracecontext'],
      },
    ],
  });

  // Initialize Logs
  datadogLogs.init({
    clientToken: process.env.REACT_APP_DD_RUM_CLIENT_TOKEN!,
    site: 'datadoghq.com',
    service: 'ecommerce-web',
    env: 'production',
    version: process.env.REACT_APP_VERSION!,
    forwardErrorsToLogs: true,
    sessionSampleRate: 100,
  });
}
```

**CDN (Async Loading):**
```html
<script>
  (function(h,o,u,n,d) {
    h=h[d]=h[d]||{q:[],onReady:function(c){h.q.push(c)}}
    d=o.createElement(u);d.async=1;d.src=n
    n=o.getElementsByTagName(u)[0];n.parentNode.insertBefore(d,n)
  })(window,document,'script','https://www.datadoghq-browser-agent.com/us1/v5/datadog-rum.js','DD_RUM')
  
  window.DD_RUM.onReady(function() {
    window.DD_RUM.init({
      clientToken: '<CLIENT_TOKEN>',
      applicationId: '<APPLICATION_ID>',
      site: 'datadoghq.com',
      service: 'my-web-app',
      env: 'production',
      sessionSampleRate: 100,
      sessionReplaySampleRate: 20,
      defaultPrivacyLevel: 'mask-user-input',
    });
  })
</script>
```

### Mobile RUM (iOS)

**Swift Initialization:**
```swift
import DatadogRUM
import DatadogTrace

Datadog.initialize(
    appContext: .init(),
    trackingConsent: .granted,
    configuration: Datadog.Configuration
        .builderUsing(
            rumApplicationID: "<RUM_APP_ID>",
            clientToken: "<CLIENT_TOKEN>",
            environment: "production"
        )
        .set(serviceName: "ios-app")
        .set(sampleRate: 100)
        .enableRUM(true)
        .enableTracing(true)
        .enableLogging(true)
        .build()
)

RUM.enable(
    with: RUM.Configuration(
        applicationID: "<RUM_APP_ID>",
        sessionSampleRate: 100,
        uiKitViewsPredicate: DefaultUIKitRUMViewsPredicate(),
        uiKitActionsPredicate: DefaultUIKitRUMActionsPredicate(),
        urlSessionTracking: .init(
            firstPartyHostsTracing: .trace(hosts: ["api.example.com"])
        )
    )
)
```

### Mobile RUM (Android)

**Kotlin Initialization:**
```kotlin
import com.datadog.android.Datadog
import com.datadog.android.core.configuration.Configuration
import com.datadog.android.core.configuration.Credentials
import com.datadog.android.privacy.TrackingConsent
import com.datadog.android.rum.Rum
import com.datadog.android.rum.RumConfiguration
import com.datadog.android.rum.tracking.ActivityViewTrackingStrategy

val configuration = Configuration.Builder(
    logsEnabled = true,
    tracesEnabled = true,
    crashReportsEnabled = true,
    rumEnabled = true
).build()

val credentials = Credentials(
    clientToken = "<CLIENT_TOKEN>",
    envName = "production",
    variant = "release",
    rumApplicationId = "<RUM_APP_ID>",
    serviceName = "android-app"
)

Datadog.initialize(
    context = applicationContext,
    credentials = credentials,
    configuration = configuration,
    trackingConsent = TrackingConsent.GRANTED
)

val rumConfiguration = RumConfiguration.Builder()
    .trackUserInteractions()
    .trackLongTasks(100)
    .useViewTrackingStrategy(ActivityViewTrackingStrategy(true))
    .build()

Rum.enable(rumConfiguration)
```

---

## Synthetic Monitoring

### API Tests

**Terraform Configuration:**
```hcl
resource "datadog_synthetics_test" "api_health" {
  type    = "api"
  subtype = "http"
  name    = "API Health Check"
  status  = "live"
  
  request_definition {
    method = "GET"
    url    = "https://api.example.com/health"
    
    headers = {
      Accept = "application/json"
    }
  }
  
  assertion {
    type     = "statusCode"
    operator = "is"
    target   = "200"
  }
  
  assertion {
    type     = "responseTime"
    operator = "lessThan"
    target   = "1000"
  }
  
  assertion {
    type     = "body"
    operator = "validatesJSONPath"
    targetjsonpath {
      jsonpath    = "$.status"
      operator    = "is"
      targetvalue = "healthy"
    }
  }
  
  options_list {
    tick_every          = 60
    min_failure_duration = 300
    min_location_failed  = 2
    
    retry {
      count    = 2
      interval = 300
    }
    
    monitor_options {
      renotify_interval = 60
    }
  }
  
  locations = [
    "aws:us-east-1",
    "aws:eu-west-1",
    "aws:ap-southeast-1"
  ]
  
  message = <<-EOT
    API health check failed on {{#is_alert}}{{location.name}}{{/is_alert}}
    
    Error: {{error_message}}
    
    @pagerduty-oncall @slack-alerts
  EOT
  
  tags = ["service:api", "check-type:health", "env:production"]
}
```

### Browser Tests

**Terraform Configuration:**
```hcl
resource "datadog_synthetics_test" "checkout_flow" {
  type = "browser"
  name = "E-commerce Checkout Flow"
  status = "live"
  
  request_definition {
    url = "https://shop.example.com"
  }
  
  browser_step {
    name = "Add item to cart"
    type = "click"
    params {
      element = "button[data-testid='add-to-cart']"
    }
  }
  
  browser_step {
    name = "Go to checkout"
    type = "click"
    params {
      element = "a[href='/checkout']"
    }
  }
  
  browser_step {
    name = "Enter email"
    type = "fill"
    params {
      element = "input[name='email']"
      value   = "test@example.com"
    }
  }
  
  browser_step {
    name = "Complete purchase"
    type = "click"
    params {
      element = "button[type='submit']"
    }
  }
  
  browser_step {
    name = "Verify success"
    type = "assertElementContent"
    params {
      element = ".order-confirmation"
      check   = "contains"
      value   = "Thank you for your order"
    }
  }
  
  options_list {
    tick_every           = 900
    min_failure_duration = 300
    
    retry {
      count    = 1
      interval = 300
    }
  }
  
  locations = [
    "aws:us-east-1",
    "aws:eu-west-1"
  ]
  
  message = <<-EOT
    Checkout flow test failed!
    
    Failed step: {{failed_step.name}}
    Screenshot: {{screenshot_url}}
    
    @pagerduty-oncall @slack-ecommerce
  EOT
  
  tags = ["service:shop", "check-type:transaction", "env:production"]
}
```

### Multi-Step API Tests

```hcl
resource "datadog_synthetics_test" "user_journey" {
  type = "api"
  subtype = "multi"
  name = "User Registration Flow"
  status = "live"
  
  api_step {
    name = "Create user"
    
    request_definition {
      method = "POST"
      url    = "https://api.example.com/users"
      
      body = jsonencode({
        email    = "test-{{ $random }}@example.com"
        password = "SecurePass123!"
      })
      
      headers = {
        Content-Type = "application/json"
      }
    }
    
    assertion {
      type     = "statusCode"
      operator = "is"
      target   = "201"
    }
    
    extraction {
      name  = "USER_ID"
      type  = "json_path"
      value = "$.id"
    }
  }
  
  api_step {
    name = "Verify user"
    
    request_definition {
      method = "GET"
      url    = "https://api.example.com/users/{{ USER_ID }}"
    }
    
    assertion {
      type     = "statusCode"
      operator = "is"
      target   = "200"
    }
  }
  
  api_step {
    name = "Login"
    
    request_definition {
      method = "POST"
      url    = "https://api.example.com/auth/login"
      
      body = jsonencode({
        email    = "test-{{ $random }}@example.com"
        password = "SecurePass123!"
      })
      
      headers = {
        Content-Type = "application/json"
      }
    }
    
    extraction {
      name  = "AUTH_TOKEN"
      type  = "json_path"
      value = "$.token"
    }
  }
  
  options_list {
    tick_every = 300
  }
  
  locations = ["aws:us-east-1"]
  
  tags = ["service:auth", "check-type:user-journey"]
}
```

---

## Session Replay

### Privacy Configuration
```typescript
datadogRum.init({
  // ... other config
  
  defaultPrivacyLevel: 'mask-user-input', // mask | allow | hidden
  
  // Element masking
  maskAllInputs: true,
  maskAllText: false,
  
  // Custom masking
  maskTextSelector: '.sensitive-data, [data-sensitive]',
  unmaskTextSelector: '.public-content',
  
  // Ignore specific elements
  ignoreSelector: '.analytics-only, .admin-panel',
});
```

**HTML Attributes:**
```html
<!-- Mask this element's content -->
<div data-dd-privacy="mask">Sensitive information</div>

<!-- Hide this element entirely -->
<div data-dd-privacy="hidden">Internal only</div>

<!-- Allow recording despite default settings -->
<div data-dd-privacy="allow">Public content</div>

<!-- Mask input but record interaction -->
<input type="password" data-dd-privacy="mask-user-input">
```

---

## RUM Analytics

### Core Web Vitals Tracking
```typescript
// Core Web Vitals are tracked automatically
// Access in Datadog: RUM > Performance > Core Web Vitals
```

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | <2.5s | 2.5s-4s | >4s |
| FID (First Input Delay) | <100ms | 100ms-300ms | >300ms |
| CLS (Cumulative Layout Shift) | <0.1 | 0.1-0.25 | >0.25 |
| INP (Interaction to Next Paint) | <200ms | 200ms-500ms | >500ms |
| TTFB (Time to First Byte) | <600ms | 600ms-1000ms | >1000ms |
| FCP (First Contentful Paint) | <1.8s | 1.8s-3s | >3s |

### Custom Timing
```typescript
// Mark custom performance milestones
datadogRum.addTiming('checkout_loaded');

// Later...
datadogRum.addTiming('payment_completed');

// Calculate duration in Datadog:
// @timing.checkout_loaded to @timing.payment_completed
```

### User Actions
```typescript
// Track custom user interactions
datadogRum.addAction('add_to_cart', {
  product_id: 'SKU-12345',
  product_name: 'Premium Widget',
  price: 99.99,
  quantity: 2,
  category: 'widgets'
});

// Track errors with context
datadogRum.addError(new Error('Payment failed'), {
  order_id: 'ORD-67890',
  payment_method: 'credit_card',
  amount: 199.99
});
```

---

## Dashboards

### RUM Performance Dashboard
```json
{
  "title": "Web Performance - RUM",
  "widgets": [
    {
      "definition": {
        "title": "Core Web Vitals Overview",
        "type": "timeseries",
        "requests": [{
          "rum_query": {
            "index": "*",
            "compute": {
              "aggregation": "pc75",
              "metric": "@view.largest_contentful_paint"
            },
            "search": {"query": "@type:view"}
          },
          "display_type": "line"
        }]
      }
    },
    {
      "definition": {
        "title": "Error Rate by Page",
        "type": "toplist",
        "requests": [{
          "rum_query": {
            "index": "*",
            "compute": {
              "aggregation": "count",
              "metric": "@type:error"
            },
            "group_by": [{"facet": "@view.url_path", "limit": 10}]
          }
        }]
      }
    },
    {
      "definition": {
        "title": "User Sessions by Geography",
        "type": "geomap",
        "requests": [{
          "rum_query": {
            "index": "*",
            "compute": {
              "aggregation": "cardinality",
              "metric": "@session.id"
            },
            "group_by": [{"facet": "@geo.country", "limit": 100}]
          }
        }]
      }
    }
  ]
}
```

---

## Alerting

### Performance Alert
```hcl
resource "datadog_monitor" "high_lcp" {
  name = "High LCP Detected"
  type = "rum alert"
  
  query = <<-EOT
    avg(last_5m):avg:rum.web.view.largest_contentful_paint{env:production} by {service} > 4000
  EOT
  
  thresholds {
    critical = 4000
    warning  = 2500
  }
  
  message = <<-EOT
    Large Contentful Paint is high on {{service.name}}
    Current p75: {{value}}ms
    
    Target: <2.5s
    
    Check RUM Explorer: https://app.datadoghq.com/rum/explorer
    
    @slack-performance-alerts
  EOT
  
  tags = ["rum", "performance", "web-vitals"]
}
```

### Error Rate Alert
```hcl
resource "datadog_monitor" "rum_error_rate" {
  name = "RUM Error Rate Alert"
  type = "rum alert"
  
  query = <<-EOT
    sum(last_5m):(
      sum:rum.web.error.count{env:production}.as_rate() / 
      sum:rum.web.view.count{env:production}.as_rate()
    ) * 100 > 5
  EOT
  
  thresholds {
    critical = 5
    warning  = 2
  }
  
  message = <<-EOT
    Error rate is {{value}}% on the web application
    
    Review errors in RUM: https://app.datadoghq.com/rum/error-tracking
    
    @pagerduty-oncall
  EOT
  
  tags = ["rum", "errors", "user-experience"]
}
```

---

## Integration with APM

### Connect Frontend to Backend
```typescript
datadogRum.init({
  // ... other config
  
  allowedTracingUrls: [
    // Match all subdomains
    {match: 'https://*.example.com', propagatorTypes: ['datadog']},
    
    // Specific origin with both propagators
    {
      match: 'https://api.example.com',
      propagatorTypes: ['datadog', 'tracecontext'] // W3C trace context
    },
    
    // Function-based matching
    {
      match: (url) => url.startsWith('https://api'),
      propagatorTypes: ['datadog']
    }
  ]
});
```

This connects RUM sessions to APM traces, enabling:
- Full request waterfall from browser to database
- Correlation of frontend errors with backend issues
- End-to-end latency analysis
