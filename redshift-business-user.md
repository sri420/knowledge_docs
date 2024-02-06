# As a solutions architect, I want to know the options, I have to provide the data in Redshift DB for consumption by business users based on their respective roles/permissions. I would want to consider both AWS native as well or third party solutions for this along with their pros and cons. Can you provide me details on them.

Here are some options to provide data in Amazon Redshift for consumption by different business users based on roles and permissions, along with pros and cons:

1. Use AWS Glue Data Catalog permissions:
- Glue data catalog can be used to define resource-based access control and permission policies for data in Redshift, like tables and databases. 
- Pros: Native AWS service and well integrated with Redshift. Granular permissions at resource level.
- Cons: Can get complex to set up and manage as number of resources and policies grow.

2. Use Amazon Redshift Views:
- You can create views in Redshift to restrict access to a subset/transformed data. Grant select permissions on views instead of underlying tables.
- Pros: Native to Redshift. Simple to set up and manage access. Allows SQL access for business users. 
- Cons: Underlying tables still accessible by admins. Views can impact performance.

3. Use Tableau Server/Looker for reporting and dashboards:
- Visual analytics tools like Tableau and Looker can connect to Redshift and provide dashboard interface for business users. 
- Pros: Rich visualizations for business users. Access control managed in the tool.
- Cons: Additional licensing cost. Limited to reporting, cannot run SQL or ad-hoc queries.

4. Use third-party row & column level security solutions:
- Solutions like Okera and Privacera provide fine-grained access control over Redshift tables at row, column levels. 
- Pros: Very granular access control possible. Use familiar SQL interface for access.
- Cons: Additional cost and network hops for each query can impact performance. 

In summary, depends on exact access control needs on whether native AWS options suffice or third-party solutions may be required - which come at an extra cost. But third-party solutions provide more granular control over data.


# How about considering AWS Quicksight for this requirement?
AWS QuickSight is an excellent option to consider for providing business users access to data in Amazon Redshift in a secure and controlled manner.

Here are some key aspects of using AWS QuickSight:

- It allows easy visualizations and dashboards for business users without needing SQL access to underlying data.

- Fine grained access controls and granular permissions possible at data set, dashboard levels based on users' department, role etc.

- Support SPICE queries for low latency access to Redshift data for aggregations and common computations.

- Usage based pricing makes it very cost efficient compared to traditional BI tools.

Pros of using AWS QuickSight:

- Easy to set up dashboards and data visualizations for business teams.

- In-built security and access controls to manage what users have access to.

- Flexible pricing and lower cost compared to traditional BI tools. 

- Tight integration with overall AWS ecosystem and Redshift.

Cons:

- Not for complex report development or pixel perfect dashboards.

- Limited capability for data preparation and transformations.

So in summary, QuickSight balances ease of use, security and cost when business teams need dashboarding, basic analytics on Redshift rather than complex transformations, pipelines and analytics. The permission control makes it apt for multi-tenant access scenarios.

# What features does Tableau provide to consume data from Redshift DB for business users?
Tableau provides rich and powerful capabilities to enable business users to consume and analyze data from Amazon Redshift:

1. Live Queries: Tableau can directly connect to Redshift and provide low latency access to data using optimized queries without needing to extract or move data.

2. Complex Visualizations: Users can create complex dashboards, reports and visualizations on Redshift data leveraging Tableau's chart types.

3. Data Blending: Tableau can seamlessly blend and analyze data from multiple data sources like Redshift, flat files, on-prem databases etc. 

4. Row Level Security: Tableau integrates with Redshift Row Level Security to ensure users see permitted data only.

5. User Management: Tableau Server allows managing permissions at user, group or project levels. Users access published dashboards and reports.

6. Analytics at Scale: Tableau leverages Redshift's fast distributed query processing to enable analysis on big data. Support analysis across multiple Redshift clusters.

7. Mobile Access: Users can view interactive dashboards on mobile tablets or phones using Tableau mobile apps.

8. Alerts and Subscriptions: Users can set up alerts on metrics and subscribe to scheduled reports.

In summary, Tableau provides both ease of use and depth of analytics around fast, scalable data in Amazon Redshift for business users - making it a popular BI solution.

# Is it possible to run SQL or adhoc queries from Tableau against Redshift data?
Yes, Tableau provides the capability to run custom SQL or adhoc queries against Amazon Redshift data. Some key ways to do this in Tableau are:

1. Custom SQL: Tableau desktop and Tableau Prep allows designers to directly write SQL statements against published Redshift tables, views or databases. Useful for transformations, mashups etc.

2. Data Source Filters: Tableau allows adding filters on data sources to narrow or slice data. Users can add parameters and select filter values dynamically.

3. Analytics Pane: In Tableau Desktop, the analytics pane allows business users to write adhoc SQL or visual analytics expressions on underlying data.

4. Tableau Ask Data: This uses a natural language interface to query data. Users can enter questions in plain English to analyze data rather than write SQL statements. It converts queries to efficient SQL behind the scenes.

5. Tableau REST APIs: External applications can leverage REST APIs to run parameterized SQL or custom queries against published Tableau data sources and extract data/results programmatically.

So in summary, even though Tableau is a visual analytics tool, it provides multiple options via SQL, natural language, parameters and APIs for business users or admins to query Redshift dynamically to complement interactive dashboards and reports. This makes it very flexible.

# How can I ensure that only business users only access the data for which they are authorized when using Redshift with Quicksight/Tableau?
Here are some good practices to ensure business users access only permitted data with Amazon Redshift, when using visualization tools like Quicksight and Tableau:

1. Leverage Redshift Row Level Security and create User Groups / Roles with access limited to subsets of data they are authorized for.

2. Use separate database schemas and schemas within Redshift cluster for departments, business units etc. Grant SELECT permissions to groups at schema level.

3. Create granular Read-Only users and groups in Redshift just for access via Quicksight / Tableau. Do not grant full DB access.

4. In QuickSight Reader / Admin roles, authorize groups for access only to specific Datasets tied to their Redshift schemas.

5. In Tableau Server, manage permissions and just allow users to access published datasources and visuals objects (dashboards, reports) they can view.

6. Mask sensitive fields in Redshift using views, so they don’t flow to downstream tools.

7. Implement Tableau’s Row Level Security aware data sources based on user attributes.

8. Monitor activity to detect unauthorized data access attempted via the business intelligence tools. 

9. Follow principle of least privilege - only enable access that is needed. Redshift groups, QuickSight roles or Tableau users don't bypass business rules.

With these measures, unauthorized data access can be prevented even when enabling self-service analytics via BI tools. Security governance with DB teams reviewing access is key.

# Can you explain Redshift Row Level Security and also how user groups/roles can be leveraged to restrict access to data based on user authorizations?
Sure, here are the key details on Amazon Redshift Row Level Security (RLS) and how it can be used to enable user groups/roles to access restricted data they are authorized for:

1. Redshift Row Level Security (RLS) 
 - Allows restricting access to rows in database tables based on user group or other attributes.
 - Policies define which rows groups can access using SQL expressions filtering rows.
 - Policies attached to table, all queries against table filtered.

2. Implementing RLS with User Groups
 - Create user groups in Redshift to represent departments, roles etc 
   e.g. finance_analysts, marketing_executives
 - Create RLS policies on tables that reference user groups in predicates to filter rows.
   e.g. only show sales data for their regions  
 - User inherits permissions of groups they belong to.

3. Creating and Managing Roles
- Roles allow defining access privileges like SELECT, INSERT etc
- Groups can be assigned to Roles which have table/schema level privileges 
- New users just assigned to permitted groups to get access

4. Benefits
- No changes needed from BI tools like Tableau, QuickSight
- Audit and monitor access at group level  
- Add/remove users from group to grant/revoke access
- Flexible to update policies as business rules evolve

So in summary, leveraging RLS, User Groups and Roles allows implementing least privilege access for business users to access permitted data in Redshift in a secure, auditable and scalable manner.

# How to Create RLS policies on tables that reference user groups in predicates to filter rows
Here are the steps to create a Row Level Security (RLS) policy on a table that references a user group in the predicate to filter rows:

1. Create user groups and roles in Amazon Redshift 
   For example:
    ```
    CREATE GROUP finance_analysts;  
    CREATE GROUP marketing_executives;
    
    CREATE ROLE analyst_role;
    GRANT SELECT ON schema.table TO analyst_role; 
   ```

2. Define a RLS policy with a predicate conditioning access based on user group membership. Use `USER GROUP` check in WHERE clause.

    ```
    CREATE policy sales_policy ON schema.sales AS 
    TO group finance_analysts 
    USING (user_group() = 'finance_analysts') 
    WITH CHECK (region IN ('AMER', 'EMEA'));
    ```

3. The above policy allows the "finance_analysts" group to only access rows in the sales table for AMER and EMEA regions.

4. Associate this RLS policy with the table 

    ```
    ALTER TABLE schema.sales ENABLE ROW LEVEL SECURITY; 
    ```

5. Grant access to the table via roles for permitted groups

    ```
    GRANT SELECT ON table TO analyst_role;
    ```

Now any user belonging to the "finance_analysts" group will see restricted rows in sales table based on the region filter when querying via analyst_role.

So this demonstrates how RLS policies with user group predicates enable fine-grained access control over Redshift data.

# What are Tableau’s Row Level Security aware data sources. Why and how to use them?
Tableau’s Row Level Security (RLS) aware data sources allow integrating native row-level permissions from the underlying data sources like Amazon Redshift into Tableau, to ensure users see only permitted data rows.

Key reasons to use RLS aware data sources:

1. Apply user/group level access rules defined in Redshift within Tableau dashboards seamlessly 

2. Avoid duplicating permissions across data platform and visualization layer

3. Single source of truth for permissions at the data layer

4. Changes to RLS rules automatically reflected in Tableau

5. Simplified permission management in complex deployment


Configuring RLS Filters:

1. Define RLS rules, user groups, predicates in Redshift 

2. In Tableau Desktop, edit the data source connection

3. Navigate to “Row Level Security” tab

4. Select field(s) to apply e.g. User Group ID

5. Tableau will append native RLS predicates from Redshift to queries

This transparently filters each user’s view of permitted data without having to define separate data sets or manual filters in Tableau. Tight coupling between native RLS and analytics.

# Can we use Redshift Data API to access Redshift data from quicksight/tableau. What are the pros and cons of this approach.
Yes, it is possible to use the Amazon Redshift Data API to access data from Redshift and make it available for visualization tools like Quicksight and Tableau.

Here are some pros and cons of this approach:

Pros:

- Data API provides secure, scalable access to Redshift tables and views without connecting BI tools directly to the cluster

- Built-in support for caching, scaling, monitoring. Less load on Redshift.

- Query Isolation - Data API doesn't share DB connections or temporary credentials 

- Fine-grained Access Control possible through IAM permissions on API

- Pay only for queries run through the Data API and data scanned

Cons: 

- Additional component in the chain - some latency overhead

- Need to manage IAM Roles and API Access separately

- Additional costs for Data API requests and data processed

- BI tools lose ability to directly connect and query the database

In summary, Redshift Data API adds a secure abstraction layer and controls direct exposure of database from BI tools. This improves security and access controls but adds additional complexity. The performance overhead and cost should be evaluated especially for highly concurrent workloads.

 

