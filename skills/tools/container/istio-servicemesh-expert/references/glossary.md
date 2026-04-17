# Glossary

## Core Concepts

### Service Mesh
A dedicated infrastructure layer for handling service-to-service communication, providing observability, traffic management, and security.

### Sidecar Proxy
A Envoy-based proxy injected alongside each service instance, intercepting all inbound and outbound traffic.

### Control Plane
The Istiod component that manages the service mesh configuration, certificate issuance, and pilot for traffic management.

### Data Plane
The collection of sidecar proxies (Envoy) that handle traffic between services.

## Traffic Management

### VirtualService
Defines routing rules for traffic within the mesh, controlling how requests are routed to services.

### DestinationRule
Defines policies for traffic to a specific destination (load balancing, connection pools, outlier detection).

### Gateway
Configures ingress and egress traffic for the mesh, operating at the edge of the mesh.

### ServiceEntry
Adds external services to the mesh registry, allowing traffic to external services to be managed by Istio.

### Sidecar
Configures the scope of traffic capture for sidecar proxies, limiting which services a pod can reach.

### EnvoyFilter
Allows customizing Envoy configuration through patches, enabling advanced scenarios.

## Security

### PeerAuthentication
Defines mTLS mode for workloads: STRICT (require mTLS), PERMIT (allow both), or DISABLE.

### AuthorizationPolicy
Defines access control for services (ALLOW or DENY rules with conditions).

### RequestAuthentication
Defines JWT token validation rules for workloads.

### Certificate Management
Istiod automatically provisions and rotates mTLS certificates for workloads.

## Observability

### Metrics
Prometheus metrics exposed by Envoy sidecars and control plane.

### Distributed Tracing
Tracing support via Jaeger, Zipkin, or other compatible backends.

### Access Logging
Envoy access logs for request/response details.

## Networking Terms

### Sidecar Injection
Automatic injection of Envoy sidecar into pods when namespace has istio-injection=enabled.

### Egress Gateway
Gateway for controlling outbound traffic from the mesh to external services.

### Ingress Gateway
Gateway for inbound traffic from outside the mesh.

### mTLS
Mutual TLS - bidirectional authentication between client and server.

### ALPN
Application-Layer Protocol Negotiation - used in Istio for protocol detection.

## Configuration Types

### MeshConfig
Global configuration for the entire mesh (tracing, metrics, default policies).

### Telemetry
Configuration for observability (metrics, logs, traces) collection.

### ProxyConfig
Configuration for sidecar proxy behavior (resource limits, concurrency).

## Deployment Modes

### Ambient Mesh
Sidecar-less mesh mode using ztunnel for zero-trust networking. Uses waypoint proxies for L7 features.

### Sidecar Mode
Traditional mode with Envoy sidecar injected into each pod.

### Revision
Istiod version deployment, enabling canary upgrades of control plane.

## Common Abbreviations

### CDS
Cluster Discovery Service - Envoy config for clusters (backends).

### LDS
Listener Discovery Service - Envoy config for listeners (ports, filters).

### EDS
Endpoint Discovery Service - Envoy config for endpoints (IP addresses, ports).

### RDS
Route Discovery Service - Envoy config for routes (path-based routing).

### SDS
Secret Discovery Service - Envoy config for certificates.

## Troubleshooting Terms

### istiod
The main Istio control plane component (formerly "pilot").

### ztunnel
Lightweight per-node proxy for ambient mesh data plane.

### waypoint proxy
Per-service L7 proxy in ambient mesh mode.

### Envoy
The underlying proxy technology used by Istio.

### XDS
Unified discovery API used by Envoy (CDS, LDS, EDS, RDS, SDS).

### mTLS mode: STRICT
Traffic must be mTLS encrypted.

### mTLS mode: PERMISSIVE
Both mTLS and plain text traffic allowed.

## Traffic Patterns

### Canary Deployment
Gradually shifting traffic to a new version (e.g., 10% → 50% → 100%).

### Blue-Green Deployment
Running two identical environments, switching all traffic at once.

### A/B Testing
Routing based on user characteristics (cookies, headers) for testing.

### Mirroring
Duplicating traffic to a test version without affecting production.

### Circuit Breaker
Automatically failing fast when a service is unhealthy.

### Retry Policy
Automatic retry on failure with configurable attempts and backoff.

### Timeout
Time limit for waiting for a response.

### Rate Limiting
Limiting the number of requests per time period.