# Glossary

## Looker Terms

| Term | Definition |
|------|------------|
| **LookML** | Looker's modeling language for defining dimensions, measures, and relationships |
| **View** | A LookML object representing a database table plus derived fields |
| **Explore** | A set of views joined together, exposing dimensions and measures for querying |
| **Dashboard** | Collection of visualizations (tiles) on a single page |
| **Tile** | Individual visualization on a dashboard |
| **Look** | Saved visualization/query result |
| **Datagroup** | Caching policy defining when Looker re-queries the database |
| **PDT** | Persisted Derived Table - materialized in database for performance |
| **Aggregate Table** | Pre-computed summary table for faster aggregations |
| **User Attribute** | Runtime filter value determined by user/group |
| **Liquid** | Templating language for dynamic LookML values |
| **Pinning** | Locking dashboard tile positions |

## Metabase Terms

| Term | Definition |
|------|------------|
| **Question** | Individual query or visualization in Metabase |
| **Dashboard** | Collection of questions arranged on a canvas |
| **Collection** | Folder-like organization for questions and dashboards |
| **Segment** | Reusable saved filter condition |
| **Metric** | Reusable aggregation formula |
| **Native Query** | Custom SQL written directly (vs GUI query builder) |
| **Simple/Custom Question** | GUI-based query without/with custom expressions |
| **Field Filter** | Parameterized filter mapped to a field |
| **Card** | Dashboard item containing a question visualization |
| **Pulse** | Scheduled email/Slack report (legacy term, now "Subscriptions") |
| **Subscription** | Automated periodic dashboard export |
| **Caching** | Metabase feature to cache query results |

## BI & Data Modeling Terms

| Term | Definition |
|------|------------|
| **Semantic Layer** | Abstraction that provides consistent business definitions |
| **Fact Table** | Transaction/event data table (e.g., orders, events) |
| **Dimension Table** | Descriptive attributes (e.g., customer, product) |
| **Star Schema** | Fact table with denormalized dimension tables |
| **Snowflake Schema** | Normalized dimension tables with multiple levels |
| **Slowly Changing Dimension (SCD)** | Dimension that changes over time (Type 1, Type 2) |
| **Kimball Methodology** | Data warehousing design approach emphasizing business processes |
| **Inmon Methodology** | Top-down data warehouse design with normalized 3NF |
| **Data Mart** | Subset of data warehouse for specific business function |
| **OLAP** | Online Analytical Processing - multi-dimensional analysis |

## Embedding Terms

| Term | Definition |
|------|------------|
| **Signed URL** | URL with cryptographic signature for secure access |
| **JWT** | JSON Web Token - stateless authentication format |
| **iFrame** | HTML element for embedding external content |
| **CORS** | Cross-Origin Resource Sharing - browser security policy |
| **Row-Level Security (RLS)** | Filter data at query time based on user identity |
| **Embedding Secret** | Cryptographic key for signing embed URLs |
| **Sandbox** | Browser isolation preventing parent-child script access |
| **SSO** | Single Sign-On - centralized authentication |

## Performance Terms

| Term | Definition |
|------|------------|
| **Query Folding** | Pushing transformation logic to the database |
| **Materialization** | Pre-computing and storing query results |
| **Cache Hit** | Retrieving data from cache instead of database |
| **ETL** | Extract, Transform, Load - data pipeline process |
| **ELT** | Extract, Load, Transform - modern cloud data stack pattern |
| **Data Pipeline** | Automated flow of data between systems |
