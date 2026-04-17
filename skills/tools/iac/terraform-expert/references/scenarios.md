## 9. Scenario Examples

### 9.1 VPC Module Creation

**User:** "Create a reusable VPC module for AWS"

**Terraform Expert:**
> **Module Structure:**
> 
> **variables.tf:**
> ```hcl
> variable "cidr_block" {
>   description = "CIDR block for VPC"
>   type        = string
>   default     = "10.0.0.0/16"
> }
> 
> variable "availability_zones" {
>   description = "List of AZs"
>   type        = list(string)
> }
> 
> variable "environment" {
>   description = "Environment name"
>   type        = string
> }
> ```
> 
> **main.tf:**
> ```hcl
> resource "aws_vpc" "this" {
>   cidr_block           = var.cidr_block
>   enable_dns_hostnames = true
>   enable_dns_support   = true
> 
>   tags = {
>     Name        = "${var.environment}-vpc"
>     Environment = var.environment
>   }
> }
> 
> resource "aws_subnet" "public" {
>   count             = length(var.availability_zones)
>   vpc_id            = aws_vpc.this.id
>   cidr_block        = cidrsubnet(var.cidr_block, 8, count.index)
>   availability_zone = var.availability_zones[count.index]
> 
>   map_public_ip_on_launch = true
> 
>   tags = {
>     Name = "${var.environment}-public-${count.index + 1}"
>   }
> }
> 
> resource "aws_internet_gateway" "this" {
>   vpc_id = aws_vpc.this.id
> 
>   tags = {
>     Name = "${var.environment}-igw"
>   }
> }
> ```
> 
> **outputs.tf:**
> ```hcl
> output "vpc_id" {
>   value = aws_vpc.this.id
> }
> 
> output "public_subnets" {
>   value = aws_subnet.public[*].id
> }
> ```

### 9.2 Troubleshooting State Lock

**User:** "Terraform is stuck with 'Lock' error"

**Terraform Expert:**
> **Diagnosis:**
> 
> | Check| Command| Finding|
> |-----|--------|--------|
> | 1 | `aws dynamodb get-item --table-name terraform-state-locking --key '{"LockID": {"S": "envs/prod/terraform.tfstate-md5"}}'` | Lock held by another process |
> 
> **Solutions:**
> 
> 1. **Wait**: Another process may be completing
> 2. **Force Unlock** (if safe):
>    ```bash
>    terraform force-unlock <lock-id>
>    ```
> 3. **Check for stuck processes**: Review CI/CD logs
> 
> **Prevention:**
> - Ensure CI/CD uses locking
> - Set appropriate timeout
> - Use `-lock-timeout` for long operations

