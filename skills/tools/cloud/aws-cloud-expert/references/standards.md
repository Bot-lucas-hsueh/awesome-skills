# Standards & Reference

## 7.1 Official Documentation

- [AWS Documentation](https://docs.aws.amazon.com/) — Full documentation for all AWS services
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/) — Operational excellence, security, reliability, performance, cost, sustainability
- [AWS IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) — Least privilege, MFA, rotation, roles
- [AWS Regional Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) — Services by region
- [AWS Pricing Calculator](https://calculator.aws/) — Estimate costs before deployment
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/) — All AWS CLI commands
- [AWS re:Post](https://repost.aws/) — Community Q&A and official AWS responses
- [AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) — Basic, Developer, Business, Enterprise

## 7.2 IAM Security Best Practices

### 7.2.1 Principle of Least Privilege

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

### 7.2.2 IAM Policy Evaluation Logic

```
Request → Authentcation → Authorization → Deny/Allow

Deny always wins:
1. Explicit Deny (Organization SCP or IAM Policy) → DENY
2. Explicit Allow → ALLOW
3. Default (no statement) → DENY
```

### 7.2.3 IAM Best Practices Checklist

| Practice | Implementation |
|----------|----------------|
| **MFA on root account** | Enable virtual MFA or hardware key |
| **No root access keys** | Delete immediately after account creation |
| **Use IAM roles** | No long-term access keys in applications |
| **Service Control Policies** | SCPs at organization level restrict actions |
| **Password policy** | Min 14 chars, require symbols, rotation 90 days |
| **Access Advisor** | Review last-accessed to remove unused permissions |
| **Credential Report** | Download CSV to audit all users monthly |

### 7.2.4 Secure IAM Role Trust Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/my-role"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": ["10.0.0.0/8"]
        }
      }
    }
  ]
}
```

## 7.3 Region Selection Guide

### 7.3.1 Factors for Region Selection

| Factor | Consideration |
|--------|---------------|
| **Latency** | Choose region closest to majority of users |
| **Compliance** | Data residency laws (GDPR in EU, data sovereignty) |
| **Services** | Not all services available in all regions |
| **Cost** | Same service can vary 2-3x between regions |
| **Availability** | Number of AZs varies (2-6 AZs per region) |

### 7.3.2 AWS Regions and Notable Services

| Region Code | Region Name | Use Case |
|-------------|-------------|----------|
| us-east-1 | US East (N. Virginia) | Most services, lowest cost, largest ecosystem |
| us-west-2 | US West (Oregon) | Multi-AZ, good for West Coast |
| eu-west-1 | Europe (Ireland) | EU workloads, GDPR compliance |
| ap-southeast-1 | Asia Pacific (Singapore) | APAC workloads |
| ap-northeast-1 | Asia Pacific (Tokyo) | Japan, gaming, low latency |

### 7.3.3 Edge Locations

- **CloudFront**: 600+ edge locations globally
- **Global Accelerator**: 275+ edge locations
- **WAF**: Integrated with CloudFront edge locations

## 7.4 Cost Optimization

### 7.4.1 Cost Management Hierarchy

```
Cost Optimization
├── Right-size resources (20-40% savings)
├── Delete unused resources (10-30% savings)
├── Use reserved capacity (30-60% savings)
├── Use Spot instances (60-90% savings)
└── Enable S3 lifecycle policies (20-50% savings)
```

### 7.4.2 Cost Explorer Recommendations

```bash
# View top cost contributors
aws ce get-cost-and-usage \
  --time-period Start=2024-01-01,End=2024-02-01 \
  --granularity MONTHLY \
  --metrics "BlendedCost" "UnblendedCost" "UsageQuantity" \
  --group-by Type=DIMENSION,Key=SERVICE

# Get RI coverage
aws ce get-reservation-coverage \
  --time-period Start=2024-01-01,End=2024-02-01 \
  --granularity MONTHLY
```

### 7.4.3 Reserved Instance Strategy

| Instance Type | 1-Year No Upfront | 1-Year Partial Upfront | 3-Year No Upfront |
|---------------|-------------------|------------------------|-------------------|
| On-Demand | 100% | 100% | 100% |
| Standard | 70% off | 72% off | 72% off |
| Convertible | 54% off | 56% off | 56% off |
| Savings Plan | 72% off | 72% off | 72% off |

### 7.4.4 S3 Cost Tiers

| Storage Class | Cost/GB/mo | Retrieval |
|---------------|-------------|-----------|
| S3 Standard | $0.023 | Immediate |
| S3 IA | $0.0125 | Milliseconds |
| S3 Glacier Instant | $0.004 | Milliseconds |
| S3 Glacier Flexible | $0.007 | Minutes-Hours |
| S3 Glacier Deep Archive | $0.00099 | Hours-12hrs |

## 7.5 AWS Well-Architected Framework Pillars

| Pillar | Key Questions |
|--------|---------------|
| **Operational Excellence** | How do you run your systems? |
| **Security** | How do you protect data? |
| **Reliability** | Does the system recover gracefully? |
| **Performance Efficiency** | Do you use resources efficiently? |
| **Cost Optimization** | Do you avoid unnecessary costs? |
| **Sustainability** | How do you minimize environmental impact? |
