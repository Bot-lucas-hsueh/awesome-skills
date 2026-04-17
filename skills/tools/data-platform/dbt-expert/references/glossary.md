# Glossary

## Core Terms

| Term | Definition |
|------|------------|
| **Model** | SELECT statement that defines a table |
| **Source** | Raw data from warehouse |
| **Ref** | Reference to another model |
| **Macro** | Reusable SQL snippet |
| **Package** | Shareable dbt project |
| **Seed** | CSV file loaded to warehouse |
| **Snapshot** | Type 2 slowly changing dimension |

## Model Types

| Term | Definition |
|------|------------|
| **Staging** | Raw data with basic transforms |
| **Intermediate** | Reusable logic between staging and marts |
| **Fact** | Transactional data tables |
| **Dimension** | Descriptive data tables |
| **Aggregate** | Pre-aggregated summaries |

## Testing

| Term | Definition |
|------|------------|
| **Singular** | Custom test in tests/ folder |
| **Generic** | Schema test defined in YML |
| **Unique** | Test column uniqueness |
| **Not Null** | Test column has values |
| **Referential** | Test foreign key relationship |
| **Accepted Values** | Test column in list |

## Configuration

| Term | Definition |
|------|------------|
| **Materialization** | How model is built (table/view/ephemeral) |
| **Incremental** | Add new rows only |
| **Partition** | Cluster by time |
| **Alias** | Custom name in warehouse |
| **Schema** | Target schema name |