# Troubleshooting Guide

## 8.1 Common AWS Errors and Fixes

### 8.1.1 EC2 Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `InstanceLimitExceeded` | Too many instances in region | Request limit increase or use different instance type |
| `InsufficientInstanceCapacity` | Not enough capacity in AZ | Try different AZ, different instance type, or retry later |
| `InvalidAMIID.notFound` | AMI no longer available | Deregistered or moved to another region |
| `InstanceTerminated` | Spot instance reclaimed | Use persistent request or on-demand |
| `UnauthorizedOperation` | IAM permission denied | Check IAM role/policy permissions |

### 8.1.2 S3 Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `AccessDenied` | No permission to bucket/object | Check bucket policy, IAM policy, or ACL |
| `NoSuchBucket` | Bucket doesn't exist | Verify bucket name (DNS-compatible) |
| `BucketAlreadyExists` | Name taken globally | Use unique bucket name |
| `MalformedXML` | Configuration error | Validate XML syntax in policy/bucket config |
| `PermanentRedirect` | Object in different region | Use correct region endpoint |

### 8.1.3 Lambda Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `AccessDeniedException` | Execution role lacks permission | Attach IAM policy to execution role |
| `InvalidParameterValueException` | Environment variable misconfigured | Check ENI/VPC configuration |
| `ENILimitReached` | Too many Lambdas in VPC | Increase ENI limit or reduce concurrent Lambdas |
| `RequestTooLarge` | Payload > 6MB | Use S3 for large payloads |
| `Unhandled` | Uncaught exception | Check CloudWatch logs |

### 8.1.4 RDS Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `InvalidParameterCombination` | Cannot find DB engine | Check parameter groups |
| `DBInstanceNotFound` | Instance deleted or renamed | Verify instance identifier |
| `InsufficientStorageClusterCapacity` | Storage full | Scale storage or enable auto-scaling |
| `OptionGroupVersionMismatch` | Option group incompatibility | Update option group |
| `IAMAuthNotSupported` | MySQL version doesn't support IAM | Use MySQL 8.0+ |

### 8.1.5 VPC/Networking Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `VpcLimitExceeded` | Max VPCs reached (5 per region) | Request limit increase |
| `DependencyViolation` | Resource still using subnet | Delete resources first |
| `InvalidSubnetID.notFound` | Subnet deleted | Recreate subnet |
| `RouteLimitExceeded` | Too many routes in route table | Use prefix lists, consolidate |
| `InternetGatewayNotAttached` | IGW detached | Attach IGW to VPC |

## 8.2 Diagnostic Commands

### 8.2.1 EC2 Diagnostics

```bash
# Describe instance status
aws ec2 describe-instance-status \
  --instance-ids i-1234567890abcdef0

# Check VPC configuration
aws ec2 describe-vpc-endpoints \
  --filters "Name=vpc-id,Values=vpc-12345678"

# View security group rules
aws ec2 describe-security-groups \
  --group-ids sg-12345678

# Check IAM instance profile
aws ec2 describe-iam-instance-profile-associations \
  --filters "Name=instance-id,Values=i-1234567890abcdef0"
```

### 8.2.2 CloudWatch Logs

```bash
# Get Lambda logs
aws logs filter-log-events \
  --log-group-name /aws/lambda/my-function \
  --start-time 1700000000000 \
  --filter-pattern "ERROR"

# Query logs with Insights
aws logs insights query \
  --log-group-name /aws/lambda/my-function \
  --start-time 1700000000 \
  --end-time 1700100000 \
  --query 'fields @timestamp, @message | filter @message like /ERROR/'
```

### 8.2.3 VPC Connectivity Tests

```bash
# Test VPC connectivity
aws ec2 describe-vpc-peering-connections \
  --filters "Name=status-code,Values=active"

# Check NAT Gateway status
aws ec2 describe-nat-gateways \
  --filter "Name=vpc-id,Values=vpc-12345678"

# Verify route tables
aws ec2 describe-route-tables \
  --route-table-ids rtb-12345678
```

## 8.3 Support and Resources

### 8.3.1 AWS Support Tiers

| Plan | Response Time | Use Case |
|------|---------------|----------|
| **Basic** | N/A (community only) | Learning, personal projects |
| **Developer** | Business hours, <24hr | Development, testing |
| **Business** | 24/7, <1hr critical | Production workloads |
| **Enterprise On-Ramp** | 24/7, <30min critical | Growing businesses |
| **Enterprise** | 24/7, <15min critical, TAM | Mission-critical |

### 8.3.2 Where to Get Help

1. **AWS re:Post** — Community Q&A, AWS expert responses
2. **AWS Health Dashboard** — Service health, personal account issues
3. **AWS Support API** — programmatic access to support
4. **AWS Trusted Advisor** — Cost, security, fault tolerance checks (Business+)
5. **AWS Solutions Architects** — Architecture guidance (Enterprise)

### 8.3.3 AWS Health Commands

```bash
# Check account health
aws health describe-events \
  --filter "eventStatusCodes=open"

# View upcoming changes
aws health describe-upcoming-events \
  --filter "eventTypeCategories=scheduledChange"
```

## 8.4 Debugging Workflow

```
Step 1: Identify the Service
├── Check CloudWatch metrics
├── Review CloudWatch logs
└── Check AWS Health Dashboard

Step 2: Check IAM Permissions
├── Verify execution role
├── Review policy simulation
└── Check resource-based policies

Step 3: Network Debugging
├── Verify VPC configuration
├── Check security groups
├── Validate route tables
└── Test with VPC Reachability Analyzer

Step 4: Service-Specific Debugging
├── EC2: System log, instance status
├── Lambda: CloudWatch logs, X-Ray traces
├── RDS: Database logs, performance insights
└── S3: Server access logs, CloudTrail

Step 5: Engage Support
├── Collect resource ARNs
├── Document timeline
└── Create support case with details
```

## 8.5 Common Debugging Patterns

### 8.5.1 "Access Denied" Debugging

```
1. Check if requester has IAM permission
2. Check if resource policy denies
3. Check if SCP denies at org level
4. Check if bucket ACL denies
5. Check if VPC endpoint policy restricts
6. Use IAM Policy Simulator to test
```

### 8.5.2 "Timeout" Debugging

```
1. Check if security groups allow traffic
2. Check if NACLs allow ephemeral ports
3. Verify route table has correct destination
4. Check if NAT Gateway/Instance is working
5. Verify DNS resolution
6. Check CloudWatch metrics for packet drops
```

### 8.5.3 "High Latency" Debugging

```
1. Check CloudWatch metrics (CPU, network)
2. Review application performance
3. Check if scaling is triggered
4. Verify Load Balancer health
5. Use AWS X-Ray for distributed tracing
6. Check for Hot partitions (DynamoDB/Kinesis)
```
