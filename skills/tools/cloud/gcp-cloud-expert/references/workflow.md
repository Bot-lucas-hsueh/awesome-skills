# Troubleshooting Guide

## 8.1 Common GCP Errors and Fixes

### 8.1.1 Compute Engine Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `ZONE_RESOURCE_POOL_EXHAUSTED` | No capacity in zone | Try different zone, different machine type |
| `QUOTA_EXCEEDED` | Resource limit reached | Request quota increase |
| `INSTANCE_GROUP_ERROR` | MIG misconfiguration | Check instance template, health check |
| `PREEMPTED` | Preemptible instance killed | Design for interruptions |
| `FAILED_TO_ATTACH_DISK` | Disk attachment failed | Check disk and instance in same zone |
| `START_PARTIAL_FAILURE` | Some operations failed | Check instance logs |

### 8.1.2 GKE Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `集群错误` | Cluster provisioning failed | Check quota, permissions |
| `NodePoolAutorepairFailed` | Node repair failed | Check node logs, networking |
| `NodePoolAutoscalingFailed` | Auto-scaling failed | Check cluster autoscaler config |
| `ImagePullBackOff` | Cannot pull container image | Check image URL, permissions |
| `CrashLoopBackOff` | Container keeps crashing | Check application logs |
| `OOMKilled` | Out of memory | Increase memory limits |

### 8.1.3 Cloud Storage Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `403 Forbidden` | No permission | Check IAM, ACLs, CORS |
| `404 Not Found` | Object doesn't exist | Verify object name |
| `BucketAlreadyExists` | Name taken globally | Use unique bucket name |
| `Precondition Failed` | Conditional request failed | Check generation/match |
| `rateLimitExceeded` | Too many requests | Exponential backoff |

### 8.1.4 Networking Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `NETWORK_NOT_FOUND` | VPC not found | Verify VPC ID |
| `SUBNETWORK_NOT_FOUND` | Subnet not found | Check subnet exists |
| `INVALID_PORT_RANGE` | Invalid port | Use valid port (1-65535) |
| `INVALID_FIREWALL_TARGET` | Invalid target | Check target tags/service account |
| `ALREADY_EXISTS` | Resource already exists | Delete existing or use different name |

### 8.1.5 IAM Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `PERMISSION_DENIED` | No access | Check IAM bindings |
| `ROLE_NOT_FOUND` | Role doesn't exist | Check role name |
| `SERVICE_ACCOUNT_NOT_FOUND` | SA deleted | Recreate or use different SA |
| `INVALID_POLICY` | Policy malformed | Validate JSON syntax |

## 8.2 Diagnostic Commands

### 8.2.1 gcloud Diagnostic Commands

```bash
# Check current configuration
gcloud config list
gcloud config get-value project
gcloud config get-value account

# List instances with status
gcloud compute instances list --filter="status:RUNNING"

# Get instance serial port output
gcloud compute instances get-serial-port-output INSTANCE_NAME

# Describe instance with details
gcloud compute instances describe INSTANCE_NAME --zone=ZONE

# Check IAM policy
gcloud projects get-iam-policy my-project

# Test IAM permissions
gcloud projects test-iam-permissions my-project \
  --permissions compute.instances.create,storage.buckets.list
```

### 8.2.2 GKE Diagnostics

```bash
# Get cluster credentials
gcloud container clusters get-credentials CLUSTER_NAME \
  --region=REGION

# List pods with status
kubectl get pods -o wide

# Describe pod details
kubectl describe pod POD_NAME

# Get pod logs
kubectl logs POD_NAME --previous

# Check node status
kubectl get nodes -o wide

# Describe node
kubectl describe node NODE_NAME
```

### 8.2.3 Network Diagnostics

```bash
# Test connectivity to instance
gcloud compute ssh INSTANCE_NAME --zone=ZONE -- \
  "curl -I https://www.google.com"

# Check firewall rules
gcloud compute firewall-rules list

# Test firewall rule
gcloud compute firewall-rules test-ingress FIREWALL_RULE

# Analyze VPC reachability
gcloud compute networks/vpn/interconnect attachments list

# Check Cloud NAT status
gcloud compute routers get-status ROUTER_NAME \
  --region=REGION
```

### 8.2.4 Logging and Monitoring

```bash
# List recent logs
gcloud logging read "resource.type=gce_instance" --limit=10

# Read specific resource logs
gcloud logging read "resource.type=http_load_balancer" \
  --order=desc --limit=50

# List uptime checks
gcloud monitoring uptime-check-configs list

# Get alert policies
gcloud alpha monitoring policies list
```

## 8.3 Support Resources

### 8.3.1 GCP Support Plans

| Plan | Price | Response Time |
|------|-------|---------------|
| **Basic** | Free | Community only |
| **Developer** | $29-$100/mo | Business hours, <4hr |
| **Production** | $100-$500/mo | 24/7, <1hr critical |
| **Enhanced** | $5,000+/mo | <15min critical |

### 8.3.2 Getting Help

1. **Google Cloud Community** — cloud.google.com/community
2. **Public Issue Tracker** —issuetracker.google.com
3. **Stack Overflow** — tag `google-cloud-platform`
4. **Server Fault** — For operations questions
5. **Cloud Status** — status.cloud.google.com

### 8.3.3 Diagnostic Tools

| Tool | Purpose |
|------|---------|
| **Cloud Console** | Web UI for all services |
| **Cloud Shell** | Browser-based shell |
| **Cloud Logging** | Centralized log viewer |
| **Cloud Monitoring** | Metrics and alerting |
| **Error Reporting** | Automatic error grouping |
| **Cloud Trace** | Distributed tracing |

## 8.4 Debugging Workflows

### 8.4.1 VM Connectivity Debug

```
1. Check instance is running: gcloud compute instances list
2. Verify network tags allow traffic
3. Check firewall rules: gcloud compute firewall-rules list
4. Test from same VPC
5. Check if using external IP vs internal
6. Review VPC Flow Logs
7. Check Cloud NAT if private instance
```

### 8.4.2 GKE Application Debug

```
1. Get cluster credentials: gcloud container clusters get-credentials
2. Check pod status: kubectl get pods
3. Get pod events: kubectl describe pod
4. Check container logs: kubectl logs
5. Check node status: kubectl get nodes
6. Verify RBAC permissions: kubectl auth can-i
7. Check resource quotas: kubectl describe resourcequota
```

### 8.4.3 Storage Access Debug

```
1. Verify bucket exists: gsutil ls gs://bucket-name
2. Check IAM permissions: gcloud storage buckets describe gs://bucket
3. Check ACLs: gsutil acl get gs://bucket
4. Verify service account: gcloud iam service-accounts list
5. Check if uniform bucket-level access enabled
6. Review audit logs for access denied
```

## 8.5 Common Debugging Patterns

### 8.5.1 "Permission Denied" Pattern

```
1. Check resource IAM: gcloud get-iam-policy RESOURCE
2. Verify principal (user/service account)
3. Check for org policies restricting access
4. Check VPC SC (Virtual Private Cloud Service Controls)
5. Use Policy Troubleshooter: gcloud policy Troubleshooter
6. Check if using Workload Identity correctly
```

### 8.5.2 "Timeout" Pattern

```
1. Check if service is running
2. Verify network connectivity
3. Check firewall rules
4. Verify health check configuration
5. Check Cloud NAT if private instance
6. Review Cloud Logging for errors
7. Check quota limits
```

### 8.5.3 "Quota Exceeded" Pattern

```
1. List current quotas: gcloud compute project-info describe
2. Check specific quota: gcloud compute regions describe REGION
3. Identify which quota hit
4. Request increase if legitimate: Support ticket
5. Optimize usage or delete unused resources
6. Set quota alerts via Cloud Monitoring
```
