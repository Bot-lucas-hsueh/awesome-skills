# Examples

## 10.1 AWS CLI Commands

### 10.1.1 EC2 Commands

```bash
# Launch an EC2 instance
aws ec2 run-instances \
  --image-id ami-0abcdef1234567890 \
  --instance-type t3.micro \
  --key-name my-keypair \
  --security-group-ids sg-12345678 \
  --subnet-id subnet-12345678 \
  --iam-instance-profile Name=my-role \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=my-server}]'

# List running instances
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,Tags[?Key==`Name`].Value|[0],PrivateIpAddress]'

# Stop/Start instances
aws ec2 stop-instances --instance-ids i-1234567890abcdef0
aws ec2 start-instances --instance-ids i-1234567890abcdef0

# Create AMI from instance
aws ec2 create-image \
  --instance-id i-1234567890abcdef0 \
  --name "my-server-$(date +%Y%m%d)" \
  --description "Backup of my-server"
```

### 10.1.2 S3 Commands

```bash
# Create bucket with versioning
aws s3api create-bucket \
  --bucket my-unique-bucket-name \
  --region us-east-1

aws s3api put-bucket-versioning \
  --bucket my-unique-bucket-name \
  --versioning-configuration Status=Enabled

# Enable server-side encryption
aws s3api put-bucket-encryption \
  --bucket my-unique-bucket-name \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "AES256"
      }
    }]
  }'

# Set lifecycle policy
aws s3api put-bucket-lifecycle-configuration \
  --bucket my-unique-bucket-name \
  --lifecycle-configuration '{
    "Rules": [{
      "ID": "Move-to-Glacier",
      "Status": "Enabled",
      "Filter": {"Prefix": "logs/"},
      "Transitions": [{
        "Days": 30,
        "StorageClass": "GLACIER"
      }]
    }]
  }'

# Sync local directory to S3
aws s3 sync ./dist s3://my-bucket/ \
  --delete \
  --exclude ".git/*"
```

### 10.1.3 Lambda Commands

```bash
# Create Lambda function
aws lambda create-function \
  --function-name my-function \
  --runtime python3.11 \
  --role arn:aws:iam::123456789012:role/my-role \
  --handler index.handler \
  --zip-file fileb://function.zip \
  --timeout 30 \
  --memory-size 256

# Update function code
aws lambda update-function-code \
  --function-name my-function \
  --zip-file fileb://function.zip

# Invoke function
aws lambda invoke \
  --function-name my-function \
  --payload '{"key": "value"}' \
  --log-type Tail \
  response.json

# Add permission for S3 trigger
aws lambda add-permission \
  --function-name my-function \
  --statement-id s3-trigger \
  --action lambda:InvokeFunction \
  --principal s3.amazonaws.com \
  --source-arn arn:aws:s3:::my-bucket
```

### 10.1.4 IAM Commands

```bash
# Create IAM role with trust policy
aws iam create-role \
  --role-name my-ec2-role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "ec2.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

# Attach policy to role
aws iam attach-role-policy \
  --role-name my-ec2-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# Create instance profile and add role
aws iam create-instance-profile --instance-profile-name my-ec2-role
aws iam add-role-to-instance-profile \
  --instance-profile-name my-ec2-role \
  --role-name my-ec2-role

# Generate access report
aws iam generate-credential-report
aws iam get-credential-report
```

### 10.1.5 VPC Commands

```bash
# Create VPC with subnets
aws ec2 create-vpc --cidr-block 10.0.0.0/16

aws ec2 create-subnet \
  --vpc-id vpc-12345678 \
  --cidr-block 10.0.1.0/24 \
  --availability-zone us-east-1a

aws ec2 create-subnet \
  --vpc-id vpc-12345678 \
  --cidr-block 10.0.2.0/24 \
  --availability-zone us-east-1b

# Create and attach Internet Gateway
aws ec2 create-internet-gateway
aws ec2 attach-internet-gateway \
  --vpc-id vpc-12345678 \
  --internet-gateway-id igw-12345678

# Create route table with default route
aws ec2 create-route-table --vpc-id vpc-12345678
aws ec2 create-route \
  --route-table-id rtb-12345678 \
  --destination-cidr-block 0.0.0.0/0 \
  --gateway-id igw-12345678
```

## 10.2 Terraform IaC Patterns

### 10.2.1 VPC Module

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = true

  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}
```

### 10.2.2 EC2 with Auto Scaling

```hcl
resource "aws_launch_template" "app" {
  name_prefix   = "app-"
  image_id      = "ami-0abcdef1234567890"
  instance_type = "t3.micro"
  key_name      = "my-keypair"

  vpc_security_group_ids = [aws_security_group.app.id]

  user_data = base64encode(<<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl start httpd
              EOF)

  monitoring {
    enabled = true
  }

  tag_specifications {
    resource_type = "instance"
    tags = {
      Name = "app-instance"
    }
  }
}

resource "aws_autoscaling_group" "app" {
  vpc_zone_identifier = module.vpc.private_subnets
  desired_capacity    = 2
  max_size            = 5
  min_size            = 1

  launch_template {
    id      = aws_launch_template.app.id
    version = "$Latest"
  }

  tag {
    key                 = "Name"
    value               = "app-asg"
    propagate_at_launch = true
  }
}
```

### 10.2.3 RDS Aurora Cluster

```hcl
resource "aws_rds_cluster" "main" {
  cluster_identifier  = "my-aurora-cluster"
  engine              = "aurora-postgresql"
  engine_version      = "15.3"
  database_name       = "mydb"
  master_username     = "admin"
  master_password      = var.db_password
  skip_final_snapshot = true

  storage_encrypted = true
  kms_key_id        = aws_kms_key.main.arn

  backup_retention_period = 7
  preferred_backup_window = "03:00-04:00"

  db_subnet_group_name   = aws_db_subnet_group.main.name
  vpc_security_group_ids = [aws_security_group.rds.id]

  enabled_cloudwatch_logs_exports = ["postgresql"]
}

resource "aws_rds_cluster_instance" "replicas" {
  count = 2

  identifier     = "my-instance-${count.index}"
  cluster_identifier = aws_rds_cluster.main.id
  instance_class = "db.t3.medium"
  engine         = aws_rds_cluster.main.engine
  engine_version = aws_rds_cluster.main.engine_version

  publicly_accessible = false
  performance_insights_enabled = true
}
```

### 10.2.4 S3 with Policies

```hcl
resource "aws_s3_bucket" "app" {
  bucket = "my-app-assets"

  tags = {
    Environment = "production"
  }
}

resource "aws_s3_bucket_versioning" "app" {
  bucket = aws_s3_bucket.app.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "app" {
  bucket = aws_s3_bucket.app.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "app" {
  bucket = aws_s3_bucket.app.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

### 10.2.5 Lambda with CloudWatch

```hcl
resource "aws_lambda_function" "api" {
  filename         = "function.zip"
  function_name    = "api-handler"
  role             = aws_iam_role.lambda.arn
  handler          = "index.handler"
  source_code_hash = filebase64sha256("function.zip")
  runtime          = "nodejs18.x"
  timeout          = 30
  memory_size      = 512

  environment {
    variables = {
      NODE_ENV = "production"
      LOG_LEVEL = "info"
    }
  }

  vpc_config {
    subnet_ids         = module.vpc.private_subnets
    security_group_ids = [aws_security_group.lambda.id]
  }

  depends_on = [aws_cloudwatch_log_group.api]
}

resource "aws_cloudwatch_log_group" "api" {
  name              = "/aws/lambda/api-handler"
  retention_in_days = 14
}

resource "aws_cloudwatch_log_stream" "api" {
  name           = "api-stream"
  log_group_name = aws_cloudwatch_log_group.api.name
}
```

## 10.3 CloudFormation Snippets

### 10.3.1 Simple EC2 Instance

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Simple EC2 Instance

Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-0abcdef1234567890
      InstanceType: t3.micro
      KeyName: my-keypair
      SecurityGroups:
        - !Ref MySecurityGroup
      UserData:
        Fn::Base64: |
          #!/bin/bash
          yum update -y
          yum install -y httpd
          echo "Hello from CloudFormation" > /var/www/html/index.html
          systemctl start httpd

  MySecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow HTTP
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
```

## 10.4 Deployment Configurations

### 10.4.1 ECS Fargate Task Definition

```json
{
  "family": "my-web-app",
  "cpu": "256",
  "memory": "512",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "containerDefinitions": [
    {
      "name": "web",
      "image": "123456789.dkr.ecr.us-east-1.amazonaws.com/web:latest",
      "portMappings": [
        {
          "containerPort": 3000,
          "protocol": "tcp"
        }
      ],
      "essential": true,
      "environment": [
        {
          "name": "NODE_ENV",
          "value": "production"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/my-web-app",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ]
}
```

### 10.4.2 CodeDeploy AppSpec for ECS

```yaml
version: 0.0
Resources:
  - TargetService:
      Type: AWS::ECS::Service
      Properties:
        TaskDefinition: arn:aws:ecs:us-east-1:123456789:task-definition/my-app:3
        LoadBalancerInfo:
          ContainerName: web
          ContainerPort: 3000
Hooks:
  AfterAllowTestTraffic:
    - Location: scripts/run_tests.sh
      Timeout: 300
```
