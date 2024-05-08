Capabilities of both platforms are similar,but  the resources that provide those capabilities are often organized differently. 

Azure and AWS Accounts & Subscriptions

Azure Subscriptions
    Grouping of resources with an assigned owner responsible for billing and permissions management. 
    Subscriptions exist independently of their owner accounts, and can be reassigned to new owners as needed.

Azure Account
    Represents Billing Relationship and Azure Subscriptions help organize access to Azure resources
    All user accounts are associated with either a Microsoft Account or Organizational Account(Microsoft Entra ID)


Compute Service on AWS and Azure
--------------------------------
AWS EC2                             Azure VM
On-demand bill per second, similar instance categories but exact RAM,CPU and Storage capabilities differ

VMWare Cloud on AWS                 Azure VMWare Solution
move VMware vSphere-based workloads and environments to the cloud

AWS Parallel Cluster                Azure CycleCloud
Create, manage, operate, and optimize HPC and large compute clusters of any scale.


AutoScaling
-----------
AWS Auto Scaling                    Virtual Machine Scale Sets/ App Service Auto Scale
                                    Deploy and manage identical sets of VMs
                                    Number of sets can autoscale.


                                    App Service Auto Scale
                                    Autoscale Azure App Service applications.


Batch Processing
----------------
AWS Batch                           Azure Batch
manage compute-intensive work across a scalable collection of VMs


Storage
-------
Amazon Elastic Block Storage (EBS)              Azure   Blob Storage

durable data storage for VMs

Amazon EC2 Instance Store                       Azure Temporary Storage
storage provides VMs with low-latency temporary read-write storage


Amazon EBS Provisioned IOPS Volume              Azure Premium Storage
higher performance disk I/O with premium storage

Amazon Elastic File System (EFS)                Azure Files


Containers and Container Orchestrators
--------------------------------------
ECS,Fargate         Azure Container Apps
ECR                 Azure Container Registry
EKS                 Azure Kubernetes Service
App Mesh            Istio Add-on for AKS


Serverless Computing
--------------------
AWS Lambda          Azure Functions, WebJobs (schedule or continuously run background tasks)

Databases
---------
RDS         Azure SQL Database
            Azure Database for MySQL
            Azure Database for PostgreSQL
            Azure Database for MariaDB


Serverless Relational Database
------------------------------
Amazon Aurora Serverless                Azure SQL Database Serverless
                                        Serverless SQL pool in Azure Synapse Analytics


NOSQL
-----

DynamoDB (Key-Value)                    Azure Cosmos DB (Globallly distributed, multi-model db, key-value,document,graphs,columnar)
SimpleDB
DocumentDB(Document)
Netptune (Graph)


Caching
--------
Elasticache                         Cache For Redis
MemoryDB for Redis


Analytics and Big Data
----------------------
AWS EMR         HDInsight - Managed Apache Distribution that includes Hadoop,Spark,Storm,HBase

Database Migration
------------------
Database Migration Service          Azure Database Migration Service


Messaging Services
------------------

SQS             Queue Storage
SNS             Service Bus
EventBridge     EventGrid
Kinesis         EventHubs
MQ              Service Bus


Networking
----------

AWS Network and Classic Load Balancer           Load Balancer
Application Gateway                             Application Load Balancer

Route 53                                        Azure DNS,Traffic Manager 
                                                DNS Name Management and DNS level traffic routing and failover services

DirectConnect                                   ExpressRoute

Route Tables                                    User Defined Routes

PrivateLink                                     Azure PrivateLink
VPC Peering                                     Azure Virtual Network (VNet) Peering
-connect 2 vpcs                                 -connect two or more Virtual Networks in Azure.


Content delivery Networks
Cloudfront                                                                                                  Azure Front Door
provides content delivery network (CDN) services, to globally deliver data, videos, applications, and APIs.


Network Service comparison
---------------------------
VPC                 Virtual Network
NAT Gateways        Virtual Network NAT
VPN Gateway         VPN Gateway
Route 53            DNS
VPC Flow Logs       Azure Network Watcher
Cloudfront          Front Door
VPC Peerign         VNET Peering
VPC Endpoints       Private Endpoints
Private Link        Azure Private Links
Route Table         Custom and User Defined routes


Regions and Zone
----------------



Marketplace
AWS Marketplace         Azure Marketplace
Easy-to-deploy and automatically configured third-party applications, including single virtual machine or multiple virtual machine solutions.

AI & ML
SageMaker               Machine Learning
A cloud service to train, deploy, automate, and manage machine learning models.

Alexa Skills Set        Bot Framework
Lex                     Speech Servics
Polly,Transcribe        Speech Services
Rekognition             Cognitive Services
Skills Kit              Virtual Assistant


Big Data and Analytics
Redshift                synape analytics
Lake Formation          Data share

