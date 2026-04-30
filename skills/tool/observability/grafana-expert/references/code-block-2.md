# jsonnet Example

```
local grafonnet = import 'grafonnet.libsonnet';

local prometheus = grafonnet.prometheus;
local alertGroup = prometheus.alertGroup;

local myAlert = prometheus.alert.new(
  name='CheckoutErrorRate',
  message='Checkout service error rate is above 1%',
  conditions=[
    prometheus.query.threshold(
      expr='100 * (sum(rate(http_requests_total{service="checkout", status=~"5.."}[$__rate_interval])) / sum(rate(http_requests_total{service="checkout"}[$__rate_interval]))) > 1',
      refID='A',
      operator=prometheus.query.operators.greater_than,
      for='5m',
    ),
  ],
  labels={
    severity: 'critical',
    service: 'checkout',
    team: 'platform',
  },
  annotations={
    summary: 'Checkout error rate exceeds 1%',
    description: 'Current error rate: {{ $values.A }}%',
    runbook_url: 'https://wiki.example.com/runbooks/checkout-error-rate',
  },
);

grafonnet.prometheus.ruleGroup.new(
  name='checkout-alerts',
  rules=[
    myAlert,
  ],
  interval='1m',
)
```
