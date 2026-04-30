# Glossary

## Power BI Terms

| Term | Definition |
|------|------------|
| **Dataset** | Connection to data source with semantic model |
| **Report** | Collection of pages with visualizations |
| **Visual** | Individual chart, table, or graph |
| **Page** | Single report canvas |
| **Workspace** | Container for reports, datasets, dataflows |
| **App** | Packaged content for distribution |
| **Gateway** | On-premises data connection bridge |
| **Row-Level Security (RLS)** | Data filtering based on user identity |

## Data Modeling Terms

| Term | Definition |
|------|------------|
| **Fact Table** | Transactional data (sales, orders) |
| **Dimension Table** | Descriptive attributes (customer, product) |
| **Star Schema** | Fact surrounded by dimensions |
| **Snowflake Schema** | Normalized dimensions |
| **Cardinality** | Uniqueness of values in relationship |
| **Cross-filter** | Direction data flows between tables |
| **Snowflake Schema** | Normalized dimensions |
| **Slowly Changing Dimension (SCD)** | Dimension that changes over time |

## DAX Terms

| Term | Definition |
|------|------------|
| **Measure** | Aggregation calculated at query time |
| **Calculated Column** | Row-level calculation stored in model |
| **Calculated Table** | Table derived from expressions |
| **Context** | Current filter/row environment |
| **Filter Context** | Active filters on visualization |
| **Row Context** | Current row in iteration |
| **Context Transition** | Row to filter context conversion |
| **EARLIER** | Reference to outer row context |
| **CALCULATE** | Evaluates expression with modified filters |
| **CALCULATETABLE** | Returns table with modified filters |

## DAX Functions

| Function | Category | Purpose |
|----------|----------|---------|
| **SUM/COUNT/AVG** | Aggregate | Basic aggregations |
| **SUMX/COUNTX** | Iterator | Row-by-row aggregation |
| **CALCULATE** | Filter | Modify filter context |
| **FILTER** | Table | Return filtered table |
| **ALL** | Table | Remove filters |
| **RELATED** | Lookup | Get value from related table |
| **VALUES** | Table | Distinct values |
| **SUMMARIZECOLUMNS** | Table | Create summary table |
| **DISTINCT** | Table | Unique values |
| **MAX/MIN** | Math | Maximum/minimum value |
| **DIVIDE** | Math | Safe division |
| **IFERROR** | Logical | Error handling |
| **LOOKUPVALUE** | Lookup | Search for value |
| **TREATAS** | Table | Create virtual relationship |
| **USERELATIONSHIP** | Relationship | Use inactive relationship |

## Power Query Terms

| Term | Definition |
|------|------------|
| **M Language** | Formula language for Power Query |
| **Query Folding** | Push transformations to data source |
| **Dataflow** | Cloud-based data preparation |
| **Parameters** | Reusable configuration values |
| **Functions** | Reusable M code blocks |
| **Applied Steps** | Sequential transformations |

## Visualization Terms

| Term | Definition |
|------|------------|
| **Slicer** | Interactive filter visual |
| **Tooltip** | Hover information display |
| **Drillthrough** | Navigate to detail page |
| **Bookmarks** | Saved view state |
| **Field Parameters** | Dynamic measure selection |
| **Calculation Groups** | Collection of related calculations |

## Performance Terms

| Term | Definition |
|------|------------|
| **Aggregation** | Pre-computed summary tables |
| **Composite Model** | Mix of Import and DirectQuery |
| **Storage Mode** | Import vs DirectQuery vs Dual |
| **Query Cache** | Power BI cache for repeated queries |
| **VertiPaq** | Columnar database engine |
| **Data Model** | Tabular model in Analysis Services |

## Security Terms

| Term | Definition |
|------|------------|
| **RLS** | Row-Level Security |
| **Object-Level Security (OLS)** | Column/table hiding |
| **Admin API** | Workspace and user management |
| **Service Principal** | App-only authentication |
| **Workspaces** | Role-based access containers |
