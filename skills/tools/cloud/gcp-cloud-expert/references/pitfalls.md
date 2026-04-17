# Examples

## 10.1 gcloud CLI Commands

### 10.1.1 Compute Engine Commands

```bash
# Create instance
gcloud compute instances create my-instance \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=debian-12 \
  --image-project=debian-cloud \
  --boot-disk-size=50GB

# List instances
gcloud compute instances list

# Start/Stop instance
gcloud compute instances start my-instance --zone=us-central1-a
gcloud compute instances stop my-instance --zone=us-central1-a

# SSH into instance
gcloud compute ssh my-instance --zone=us-central1-a

# Create instance template
gcloud compute instance-templates create my-template \
  --machine-type=e2-medium \
  --image-family=debian-12 \
  --image-project=debian-cloud

# Create managed instance group
gcloud compute instance-groups managed create my-mig \
  --zone=us-central1-a \
  --template=my-template \
  --size=2

# Resize managed instance group
gcloud compute instance-groups managed resize my-mig \
  --zone=us-central1-a \
  --size=5
```

### 10.1.2 Cloud Storage Commands

```bash
# Create bucket
gsutil mb -l us-central1 gs://my-unique-bucket

# Copy files to bucket
gsutil cp ./files/* gs://my-unique-bucket/

# Set lifecycle policy
gsutil lifecycle set lifecycle-config.json gs://my-unique-bucket

# lifecycle-config.json example
# {"rule": [{"action": {"type": "Delete"}, "condition": {"age": 30}}]}

# Make bucket publicly readable
gsutil iam ch allUsers:objectViewer gs://my-unique-bucket

# Sync local directory
gsutil rsync -r ./dist gs://my-unique-bucket/dist
```

### 10.1.3 GKE Commands

```bash
# Create cluster
gcloud container clusters create my-cluster \
  --zone=us-central1-a \
  --num-nodes=3 \
  --machine-type=e2-medium

# Get credentials
gcloud container clusters get-credentials my-cluster \
  --zone=us-central1-a

# Scale cluster
gcloud container clusters resize my-cluster \
  --zone=us-central1-a \
  --num-nodes=5

# Set node pool autoscaling
gcloud container clusters update my-cluster \
  --zone=us-central1-a \
  --enable-autoscaling \
  --min-nodes=1 \
  --max-nodes=10 \
  --node-pool=default-pool
```

### 10.1.4 Cloud Functions Commands

```bash
# Deploy function
gcloud functions deploy my-function \
  --runtime=python311 \
  --trigger-http \
  --allow-unauthenticated \
  --region=us-central1

# List functions
gcloud functions list

# View logs
gcloud functions logs read my-function --region=us-central1

# Call function
gcloud functions call my-function \
  --region=us-central1 \
  --data '{"name":"World"}'
```

### 10.1.5 IAM Commands

```bash
# Add IAM policy binding
gcloud projects add-iam-policy-binding my-project \
  --member=user:user@example.com \
  --role=roles/editor

# Create service account
gcloud iam service-accounts create my-sa \
  --display-name="My Service Account"

# Create service account key
gcloud iam service-accounts keys create key.json \
  --iam-account=my-sa@my-project.iam.gserviceaccount.com

# Add service account to cluster
gcloud container clusters get-credentials my-cluster
kubectl create serviceaccount my-sa -n default
kubectl create clusterrolebinding my-sa-binding \
  --clusterrole=cluster-admin \
  --serviceaccount=default:my-sa
```

## 10.2 Terraform IaC Patterns

### 10.2.1 VPC with Subnets

```hcl
provider "google" {
  project = "my-project"
  region  = "us-central1"
}

resource "google_compute_network" "vpc" {
  name                    = "my-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "private" {
  name          = "my-private-subnet"
  network       = google_compute_network.vpc.id
  ip_cidr_range = "10.0.1.0/24"
  region        = "us-central1"

  private_ip_google_access = true

  secondary_ip_range {
    range_name    = "pods"
    ip_cidr_range = "10.1.0.0/16"
  }

  secondary_ip_range {
    range_name    = "services"
    ip_cidr_range = "10.2.0.0/16"
  }
}

resource "google_compute_router" "router" {
  name    = "my-router"
  network = google_compute_network.vpc.id
  region  = "us-central1"
}

resource "google_compute_router_nat" "nat" {
  name                               = "my-nat"
  router                             = google_compute_router.router.name
  region                             = "us-central1"
  source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"

 nat_ip_allocate_option = "AUTO_ONLY"
}
```

### 10.2.2 GKE Cluster with Autopilot

```hcl
resource "google_container_cluster" "autopilot" {
  name     = "my-autopilot-cluster"
  location = "us-central1"
  enable_autopilot = true

  cluster_autoscaling {
    auto_provisioning_defaults {
      machine_class = "e2-medium"
    }
  }

  networking_mode     = "VPC_NATIVE"
  network             = google_compute_network.vpc.name
  subnetwork          = google_compute_subnetwork.private.name
  secondary_range_name = "pods"
  services_range_name = "services"

  private_cluster_config {
    enable_private_nodes   = true
    enable_private_endpoint = false
    master_ipv4_cidr_block = "172.16.0.0/28"
  }

  ip_allocation_policy {
    cluster_secondary_range_name  = "pods"
    services_secondary_range_name = "services"
  }
}
```

### 10.2.3 Cloud SQL Instance

```hcl
resource "google_sql_database_instance" "postgres" {
  name             = "my-postgres-instance"
  database_version = "POSTGRES_15"
  region           = "us-central1"

  deletion_protection = true

  settings {
    tier              = "db-n1-standard-2"
    availability_type = "REGIONAL"

    ip_configuration {
      ipv4_enabled    = false
      private_network = google_compute_network.vpc.id
      require_ssl     = true
    }

    backup_configuration {
      enabled                        = true
      start_time                     = "03:00"
      point_in_time_recovery_enabled = true
    }

    maintenance_window {
      day          = 7
      hour         = 4
    }
  }
}

resource "google_sql_database" "database" {
  name     = "mydb"
  instance = google_sql_database_instance.postgres.name
}
```

### 10.2.4 Cloud Storage with Lifecycle

```hcl
resource "google_storage_bucket" "my-bucket" {
  name          = "my-project-storage"
  location      = "US"
  storage_class = "STANDARD"

  uniform_bucket_level_access = true

  lifecycle_rule {
    condition {
      age = 30
    }
    action {
      type          = "SetStorageClass"
      storage_class = "NEARLINE"
    }
  }

  lifecycle_rule {
    condition {
      age = 90
    }
    action {
      type          = "SetStorageClass"
      storage_class = "COLDLINE"
    }
  }

  lifecycle_rule {
    condition {
      age = 365
    }
    action {
      type = "Delete"
    }
  }
}
```

### 10.2.5 Cloud Run Service

```hcl
resource "google_cloud_run_service" "my-service" {
  name     = "my-service"
  location = "us-central1"

  template {
    spec {
      containers {
        image = "gcr.io/my-project/my-image:latest"
        resources {
          limits = {
            cpu    = "1000m"
            memory = "512Mi"
          }
        }
        env {
          name  = "NODE_ENV"
          value = "production"
        }
      }

      service_account_name = google_service_account.my-sa.email

      vpc_access {
        connector = google_vpc_access.connector.name
        runtime   = "RUN_AND_ADVERTISE_EXTERNAL_IPS"
      }
    }

    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "10"
        "autoscaling.knative.dev/minScale" = "1"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

resource "google_vpc_access" "connector" {
  name    = "my-connector"
  region  = "us-central1"
  network = google_compute_network.vpc.id
}
```

## 10.3 Deployment Manager Templates

### 10.3.1 Simple VM Deployment

```yaml
# vm-template.yaml
resources:
  - name: my-vm
    type: compute.v1.instance
    properties:
      zone: us-central1-a
      machineType: zones/us-central1-a/machineTypes/e2-medium
      disks:
        - deviceName: boot
          type: PERSISTENT
          boot: true
          autoDelete: true
          initializeParams:
            sourceImage: projects/debian-cloud/global/images/family/debian-12
      networkInterfaces:
        - network: global/networks/default
          accessConfigs:
            - name: external-nat
              type: ONE_TO_ONE_NAT
      serviceAccounts:
        - email: default
          scopes:
            - https://www.googleapis.com/auth/cloud-platform
```

## 10.4 Deployment Configurations

### 10.4.1 Cloud Build CI/CD Pipeline

```yaml
# cloudbuild.yaml
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/my-image:$COMMIT_SHA', '.']

  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/my-image:$COMMIT_SHA']

  - name: 'gcr.io/cloud-builders/gcloud'
    args:
      - 'run'
      - 'deploy'
      - 'my-service'
      - '--image=gcr.io/$PROJECT_ID/my-image:$COMMIT_SHA'
      - '--region=us-central1'
      - '--platform=managed'
      - '--allow-unauthenticated'

images:
  - 'gcr.io/$PROJECT_ID/my-image:$COMMIT_SHA'
```

### 10.4.2 Cloud Run with Cloud Build

```yaml
# cloudbuild.yaml for Cloud Run
steps:
  - name: 'gcr.io/cloud-builders/npm'
    args: ['install']

  - name: 'gcr.io/cloud-builders/npm'
    args: ['run', 'test']

  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/$REPO_NAME:$COMMIT_SHA', '.']

  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/$REPO_NAME:$COMMIT_SHA']

  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: gcloud
    args:
      - 'run'
      - 'deploy'
      - '$SERVICE_NAME'
      - '--image=gcr.io/$PROJECT_ID/$REPO_NAME:$COMMIT_SHA'
      - '--region=us-central1'
      - '--platform=managed'
      - '--memory=512Mi'
      - '--cpu=1'
      - '--max-instances=10'

images:
  - 'gcr.io/$PROJECT_ID/$REPO_NAME:$COMMIT_SHA'
```

### 10.4.3 BigQuery Dataset with Access

```sql
-- Create dataset
CREATE SCHEMA my_dataset
OPTIONS (
  location = 'US',
  description = 'My analytics dataset',
  default_table_expiration_days = 30
);

-- Create table with clustering and partitioning
CREATE TABLE my_dataset.my_table
(
  event_date DATE,
  event_timestamp TIMESTAMP,
  user_id STRING,
  event_type STRING,
  properties STRING
)
PARTITION BY DATE(event_timestamp)
CLUSTER BY event_type, user_id
OPTIONS (
  description = 'Events table',
  expiration_timestamp = TIMESTAMP_ADD(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
);
```
