Capabilities of both platforms are similar,but  the resources that provide those capabilities are often organized differently. 

Azure and AWS Accounts & Subscriptions

Azure Subscriptions
    Grouping of resources with an assigned owner responsible for billing and permissions management. 
    Subscriptions exist independently of their owner accounts, and can be reassigned to new owners as needed.

Azure Account
    Represents Billing Relationship and Azure Subscriptions help organize access to Azure resources
    All user accounts are associated with either a Microsoft Account or Organizational Account(Microsoft Entra ID)




**Azure Accounts and Subscriptions:**
- An **Azure account** is a global unique entity that gets you access to Azure services and your Azure subscriptions¹. It is associated with an email address provided when creating the Azure subscription³.
- An **Azure subscription** is a logical container for your resources³. You can create multiple subscriptions in your Azure account to create separation for billing or management purposes¹. Each Azure resource is associated with only one subscription³.
- Azure subscriptions are linked to an Azure account and serve as a single billing unit for Azure resources used in that account⁴.

**AWS Accounts:**
- An **AWS account** is a single sign-in identity that has permissions to access AWS services⁵. AWS accounts have their own resources and contact information, and can be used to control access to AWS services⁵.
- AWS Identity and Access Management (IAM) allows you to create multiple users and manage the permissions for each of these users within your AWS account⁵.
- AWS also provides consolidated billing for multiple AWS accounts, allowing you to receive one bill for multiple AWS accounts, with cost breakdowns for each account⁵.

**Key Differences:**
- In Azure, you can create multiple subscriptions under one account, and each subscription can have different billing and management settings. In AWS, you have one account and you manage resources and permissions under that account.
- Azure uses the concept of subscriptions as a way to manage resources and billing, whereas AWS does not have a direct equivalent. Instead, AWS relies on IAM for user and resource management, and consolidated billing for handling costs across multiple accounts.



In **Azure**, you first create an **Azure account**. Once the account is set up, you can then create one or more **Azure subscriptions** within that account. Each subscription is a separate billing entity and can contain different resources. This allows for more granular control over resource usage and billing.

On the other hand, in **AWS**, you create an **AWS account**, and that's typically sufficient for most purposes. You can manage resources and permissions within that account using AWS Identity and Access Management (IAM). If you need to separate billing or manage resources across different business units, you might create multiple AWS accounts and consolidate the billing.

So, in summary, both Azure accounts and subscriptions are needed to use Azure services, while in AWS, an account is usually enough. 😊



Yes, Azure has a similar concept known as **Azure Management Groups**³.

Just like AWS Organizations allow you to manage multiple AWS accounts, **Azure Management Groups** provide a way to manage your Azure subscriptions³. If your organization has many subscriptions, you can organize them into management groups. These groups help you manage access, policies, and compliance for those subscriptions³.

So, in summary, while AWS uses AWS Organizations to manage multiple AWS accounts, Azure uses Azure Management Groups to manage multiple Azure subscriptions. I hope this answers your question! 😊


Microsoft Entra ID, formerly known as Azure Active Directory (Azure AD), is a cloud-based identity and access management service¹². It's used by your employees to access external resources such as Microsoft 365, the Azure portal, and thousands of other SaaS applications². It also helps them access internal resources like apps on your corporate intranet, and any cloud apps developed for your own organization².

Here are some key features of Microsoft Entra ID:
- **Unified Identity Management**: Manage all your identities and access to all your applications in a central location, whether they’re in the cloud or on-premises¹.
- **Secure Adaptive Access**: Protect access to resources and data using strong authentication and risk-based adaptive access policies without compromising user experience¹.
- **Seamless User Experiences**: Provide a fast, easy sign-in experience across your multicloud environment to keep your users productive, reduce time managing passwords, and increase productivity¹.
- **App Integrations and Single Sign-On (SSO)**: Connect your workforce to all your apps, from any location, using any device. Simplify app access from anywhere with single sign-on¹.
- **Multicloud Identity and Access Management**: Microsoft Entra ID is an integrated cloud identity and access solution, and a leader in the market for managing directories, enabling access to applications, and protecting identities¹.

The name change to Microsoft Entra ID represents the evolution and unification of the Microsoft Entra product family, and a commitment to simplify secure access experiences for everyone⁴. I hope this helps! 😊


----
Compute Service on AWS and Azure
--------------------------------
AWS EC2                             Azure VM
On-demand bill per second, similar instance categories but exact RAM,CPU and Storage capabilities differ

VMWare Cloud on AWS                 Azure VMWare Solution
move VMware vSphere-based workloads and environments to the cloud

AWS Parallel Cluster                Azure CycleCloud
Create, manage, operate, and optimize HPC and large compute clusters of any scale.

| AWS                  | Azure                 |           Details                                                                                              |
| -------------------  | ----------------------| ----------------------------------------------------------------------------------------------------------     |
| AWS EC2              |  Azure VM             |   On-demand bill per second, similar instance categories but exact RAM,CPU and Storage capabilities differ     |
|VMWare Cloud on AWS   | Azure VMWare Solution |   move VMware vSphere-based workloads and environments to the cloud                                            |
| AWS Parallel Cluster |  Azure CycleCloud     |   Create, manage, operate, and optimize HPC and large compute clusters of any scale                            |


AutoScaling
-----------

| AWS                 | Azure                           | Details                                  |
|---------------------|-------------------------------- |------------------------------------------|
|  AWS Auto Scaling   | Virtual Machine Scale Sets      |  Deploy and manage identical sets of VMs |
|                     |                                 |  Number of sets can autoscale            |
|                     | App Service Auto Scale          |  Autoscale Azure App Service applications|



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

