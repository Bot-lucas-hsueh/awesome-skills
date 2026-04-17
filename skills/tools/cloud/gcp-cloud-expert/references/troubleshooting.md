# Troubleshooting Guide

## 8.1 Authentication Issues

### gcloud Auth Problems
```bash
# Re-authenticate
gcloud auth login

# List accounts
gcloud auth list

# Activate service account
gcloud auth activate-service-account --key-file=key.json

# Revoke and re-authenticate
gcloud auth revoke
gcloud auth login
```

### ADC (Application Default Credentials) Issues
```bash
# Check ADC
gcloud auth application-default print-access-token

# Set ADC credentials
gcloud auth application-default login

# Use service account
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
```

## 8.2 Resource Deployment Issues

### Deployment Manager Failures
```bash
# List deployments
gcloud deployment-manager deployments list

# Describe deployment
gcloud deployment-manager deployments describe my-deployment

# Delete failed deployment
gcloud deployment-manager deployments delete my-deployment --delete-policy DELETE
```

### Terraform Issues
```bash
# Initialize
terraform init

# Plan
terraform plan -var-file=prod.tfvars

# Apply
terraform apply -var-file=prod.tfvars -auto-approve
```

## 8.3 Compute Engine Issues

### VM Not Starting
1. Check quotas in Cloud Console
2. Verify machine type availability in region
3. Check boot disk space
4. Review operation logs

### SSH Access Issues
```bash
# Regenerate SSH keys
gcloud compute ssh instance-name --project=project-id

# Connect with specific key
gcloud compute ssh instance-name --ssh-key-file=~/.ssh/my_key

# Connect via IAP
gcloud compute ssh instance-name --tunnel-through-iap
```

## 8.4 GKE Cluster Issues

### Cluster Not Ready
```bash
# Describe cluster
gcloud container clusters describe my-cluster --region=us-central1

# Get cluster credentials
gcloud container clusters get-credentials my-cluster --region=us-central1

# Check node pool status
gcloud container node-pools list --cluster=my-cluster --region=us-central1
```

### Pod Issues
```bash
# Describe pod
kubectl describe pod pod-name -n namespace

# Get pod logs
kubectl logs pod-name -n namespace

# Exec into pod
kubectl exec -it pod-name -n namespace -- /bin/bash
```

## 8.5 BigQuery Issues

### Query Errors
- Check table schema matches query
- Verify project/dataset names correct
- Check for Legacy vs Standard SQL syntax

### Permission Denied
```bash
# Add IAM policy binding
gcloud projects add-iam-policy-binding project-id \
  --member=user:email@example.com \
  --role=roles/bigquery.user

# Grant dataset access
gcloud datasets update dataset-id \
  --project=project-id \
  --add-access=user:email@example.com
```

## 8.6 Networking Issues

### Firewall Rules
```bash
# List firewall rules
gcloud compute firewall-rules list

# Create allow rule
gcloud compute firewall-rules create allow-http \
  --allow tcp:80 \
  --source-ranges 0.0.0.0/0 \
  --target-tags=http-server
```

### VPC Peering Issues
- Verify CIDR ranges don't overlap
- Check both projects allow peering
- Verify DNS policy allows resolution

## 8.7 Billing Issues

### Unexpected Costs
```bash
# List resources
gcloud compute instances list
gcloud storage buckets list

# Check billing account
gcloud billing accounts list

# Link billing account
gcloud billing projects link project-id --billing-account=XXXXX
```

## 8.8 Diagnostic Commands

```bash
# List operations
gcloud operations list

# Describe operation
gcloud operations describe operation-id --region=us-central1

# Stackdriver logging
gcloud logging read "resource.type=gce_instance" --limit=10

# Cloud Debugger
gcloud debug snapshots list
```