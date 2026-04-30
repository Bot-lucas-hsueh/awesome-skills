# Scenario Examples

## 9.1 AWS VPC Creation

**User:** "How do I create an AWS VPC with Pulumi?"

**Pulumi Expert:**
> **Infrastructure Code:**
>
> ```typescript
> import * as pulumi from "@pulumi/pulumi";
> import * as aws from "@pulumi/aws";
> 
> const config = new pulumi.Config();
> const environment = config.require("environment");
> 
> // VPC
> const vpc = new aws.ec2.Vpc("main", {
>     cidrBlock: "10.0.0.0/16",
>     enableDnsHostnames: true,
>     enableDnsSupport: true,
>     tags: { Name: `${environment}-vpc` }
> });
> 
> // Internet Gateway
> const igw = new aws.ec2.InternetGateway("main", {
>     vpcId: vpc.id,
>     tags: { Name: `${environment}-igw` }
> });
> 
> // Public Subnet
> const publicSubnet = new aws.ec2.Subnet("public", {
>     vpcId: vpc.id,
>     cidrBlock: "10.0.1.0/24",
>     availabilityZone: "us-west-2a",
>     mapPublicIpOnLaunch: true,
>     tags: { Name: `${environment}-public-subnet` }
> });
> 
> // Route Table
> const publicRouteTable = new aws.ec2.RouteTable("public", {
>     vpcId: vpc.id,
>     routes: [{
>         cidrBlock: "0.0.0.0/0",
>         gatewayId: igw.id
>     }],
>     tags: { Name: `${environment}-public-rt` }
> });
> 
> // Associate
> new aws.ec2.RouteTableAssociation("public", {
>     subnetId: publicSubnet.id,
>     routeTableId: publicRouteTable.id
> });
> 
> export const vpcId = vpc.id;
> export const vpcCidr = vpc.cidrBlock;
> export const subnetId = publicSubnet.id;
> ```

## 9.2 Kubernetes Cluster

**User:** "How do I create an EKS cluster?"

**Pulumi Expert:**
> **EKS Setup:**
>
> ```typescript
> import * as pulumi from "@pulumi/pulumi";
> import * as aws from "@pulumi/aws";
> import * as eks from "@pulumi/eks";
> 
> const config = new pulumi.Config();
> 
> // EKS Cluster
> const cluster = new eks.Cluster("app-cluster", {
>     name: "app-cluster",
>     version: "1.28",
>     roleArn: eksClusterRole.arn,
>     vpcId: vpc.id,
>     publicSubnetIds: [publicSubnet1.id, publicSubnet2.id],
>     clusterSecurityGroup: clusterSg,
>     nodeGroupOptions: {
>         instanceTypes: ["t3.medium"],
>         desiredCapacity: 3,
>         minSize: 1,
>         maxSize: 5,
>     }
> });
> 
> export const kubeconfig = cluster.kubeconfig;
> export const clusterName = cluster.eksCluster.name;
> ```

## 9.3 RDS Database

**User:** "How do I set up an RDS PostgreSQL instance?"

**Pulumi Expert:**
> **RDS Setup:**
>
> ```typescript
> import * as aws from "@pulumi/aws";
> 
> const dbSubnetGroup = new aws.rds.SubnetGroup("main", {
>     name: "main-db-subnet",
>     subnetIds: [privateSubnet1.id, privateSubnet2.id],
> });
> 
> const dbInstance = new aws.rds.Instance("main", {
>     identifier: "main-db",
>     engine: "postgres",
>     engineVersion: "15.3",
>     instanceClass: "db.t3.medium",
>     allocatedStorage: 100,
>     dbName: "maindb",
>     username: "dbadmin",
>     password: config.requireSecret("dbPassword"),
>     dbSubnetGroupName: dbSubnetGroup.name,
>     vpcSecurityGroupIds: [dbSecurityGroup.id],
>     backupRetentionPeriod: 7,
>     skipFinalSnapshot: true,
> });
> 
> export const dbEndpoint = dbInstance.endpoint;
> export const dbPort = dbInstance.port;
> ```
