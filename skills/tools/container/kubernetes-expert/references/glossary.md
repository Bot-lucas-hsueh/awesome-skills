# Glossary

## Core Concepts

### Kubernetes (K8s)
An open-source container orchestration platform for automating deployment, scaling, and management of containerized applications.

### Cluster
A set of nodes (virtual or physical machines) that run containerized applications managed by Kubernetes.

### Node
A worker machine in Kubernetes (physical or virtual) that runs pods.

### Pod
The smallest deployable unit in Kubernetes. One or more containers that share storage and network.

### Control Plane
The collection of components that manage the cluster (API server, etcd, scheduler, controller manager).

## Workloads

### Deployment
Manages ReplicaSets, providing declarative updates for pods and ReplicaSets.

### ReplicaSet
Ensures a stable set of replica pods are running at any given time.

### StatefulSet
Manages deployment and scaling of stateful applications, providing guarantees about ordering and uniqueness.

### DaemonSet
Ensures that all (or some) nodes run a copy of a specific pod.

### Job
Creates one or more pods and ensures a specified number complete successfully.

### CronJob
Creates jobs on a repeating schedule.

### Service
An abstraction defining a logical set of pods and a policy to access them.

## Networking

### Service Types
- **ClusterIP**: Internal cluster IP (default)
- **NodePort**: Exposes on each node's IP
- **LoadBalancer**: External load balancer
- **ExternalName**: Maps to external DNS name

### Ingress
An API object that manages external access to services, typically HTTP.

### NetworkPolicy
Defines how groups of pods are allowed to communicate with each other and other network endpoints.

### CNI
Container Network Interface - plugin system for configuring network interfaces.

## Storage

### PersistentVolume (PV)
A piece of storage in the cluster that has been provisioned by an administrator.

### PersistentVolumeClaim (PVC)
A request for storage by a user.

### StorageClass
Provides a way to describe different classes of storage.

### EmptyDir
Temporary storage that lives as long as the pod.

### ConfigMap
Configuration data that can be consumed by pods or injected as environment variables.

### Secret
Small amount of sensitive data (passwords, tokens, keys).

## Security

### RBAC
Role-Based Access Control - managing who can do what in the cluster.

### ServiceAccount
Provides an identity for pods to access the API server.

### Role
Namespaced permission to access resources within a specific namespace.

### ClusterRole
Cluster-wide permission, can be used for cluster-scoped resources or non-resources.

### RoleBinding
Binds a role to subjects (users, groups, service accounts).

### Pod Security Standards
- **Privileged**: Unrestricted
- **Baseline**: Minimal restrictions
- **Restricted**: Strong restrictions

### Network Policy
Controls traffic flow at the pod level (ingress/egress rules).

## Configuration

### Label
Key-value pairs attached to objects for identification and selection.

### Annotation
Similar to labels but for non-identifying metadata.

### Selector
Mechanism to identify a set of objects.

### Namespace
Logical cluster partition for resource isolation.

### Resource Quota
Limits total resource consumption per namespace.

### LimitRange
Sets default/limits for resources in a namespace.

## Health & Monitoring

### Liveness Probe
Checks if container needs to be restarted.

### Readiness Probe
Checks if container can receive traffic.

### Startup Probe
Checks if container has started (for slow starting apps).

### Pod Conditions
- **PodScheduled**: Pod has been scheduled
- **Initialized**: Init containers completed
- **ContainersReady**: All containers ready
- **Ready**: Ready to serve requests

### Metrics Server
Collects resource metrics from nodes and pods for HPA.

## Scaling & Updates

### Horizontal Pod Autoscaler (HPA)
Automatically scales number of pods based on CPU/memory metrics.

### Vertical Pod Autoscaler (VPA)
Recommends/automates changes to pod resource requests.

### Deployment Strategies
- **RollingUpdate**: Gradually replace pods
- **Recreate**: Kill all, then create new
- **Blue-Green**: Run both, switch traffic
- **Canary**: Run both, gradually shift

### Probe Failure Actions
- Liveness failure: Restart container
- Readiness failure: Remove from service
- Startup failure: Treated as liveness

## Cluster Components

### kube-apiserver
API server that serves the Kubernetes API.

### etcd
Distributed key-value store for all cluster data.

### kube-scheduler
Assigns pods to nodes based on resource requirements.

### kube-controller-manager
Runs controller processes (Node, Replication, Endpoint, etc.).

### kubelet
Agent running on each node, manages containers.

### kube-proxy
Network proxy that implements service abstraction.

### Container Runtime
Software that runs containers (containerd, CRI-O, Docker).

## Debugging

### Events
Records of what happened in the cluster (scheduling, errors).

### Describe
Command to get detailed information about a resource.

### Logs
Container output (application and system).

### Exec
Execute command in a container for debugging.

### Port-forward
Access pod port from local machine.

### Proxy
Access service via API server.

## Advanced

### Custom Resource Definition (CRD)
Extension of Kubernetes API for custom resources.

### Operator
Software extension using CRDs to manage complex stateful applications.

### Admission Controllers
Plugin that intercepts requests to API server for validation/mutation.

### Mutating Webhook
Can modify objects before persistence.

### Validating Webhook
Can validate objects before persistence.

### Finalizer
Marker on objects that must be cleared before deletion.

### Owner Reference
Establishes parent-child relationships between resources.