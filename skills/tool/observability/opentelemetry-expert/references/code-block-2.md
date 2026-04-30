# python Example

```
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

# Setup meter provider
meter_provider = MeterProvider(
    resource=resource,
    metric_readers=[
        PeriodicExportingMetricReader(
            OTLPMetricExporter(endpoint="http://otel-collector:4317"),
            export_interval_millis=60000,
        )
    ],
)
metrics.set_meter_provider(meter_provider)

# Get meter and create instruments
meter = metrics.get_meter("checkout-api")

# Counter for request count
request_counter = meter.create_counter(
    name="http.requests",
    description="Total HTTP requests",
    unit="1",
)

# Histogram for request duration
request_histogram = meter.create_histogram(
    name="http.request.duration",
    description="HTTP request duration in milliseconds",
    unit="ms",
)

# Gauge for active connections
active_connections = meter.create_up_down_counter(
    name="checkout.active_connections",
    description="Number of active connections",
    unit="1",
)

# Use instruments in code
def handle_request(request):
    active_connections.add(1)
    request_counter.add(1, {"http.method": request.method, "http.status_code": 200})
    
    with request_histogram.record_time():
        result = process(request)
    
    active_connections.add(-1)
    return result
```
