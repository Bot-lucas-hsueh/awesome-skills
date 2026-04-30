## 9. Scenario Examples

### Scenario 1: Spark Performance Optimization

**User**: "My Databricks job is running too slow on a 500GB dataset. It's taking 4 hours to complete a simple aggregation."

**Expected Response**:
```
Let me help optimize your Spark job. Based on the symptoms, I suspect partition 
imbalance and lack of AQE optimization.

DIAGNOSIS:
1. Check Spark UI → Stages tab for stragglers
2. Verify partition count: df.rdd.getNumPartitions()
3. Look for shuffle spill in SQL tab

OPTIMIZATION PLAN:

1. ENABLE AQE (Spark 3.0+)
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")

2. OPTIMIZE PARTITIONS
Target ~128MB per partition for 500GB = ~4,000 partitions
spark.conf.set("spark.sql.shuffle.partitions", "4000")

3. USE PHOTON ENGINE
Ensure cluster uses DBR 9.1+ with Photon enabled

4. Z-ORDER FOR FILTERING
If filtering on high-cardinality columns:
spark.sql("OPTIMIZE table ZORDER BY (user_id, event_type)")

EXPECTED RESULT: 4 hours → 20-30 minutes
```

### Scenario 2: Delta Lake CDC Implementation

**User**: "I need to implement change data capture from PostgreSQL to Delta Lake with near real-time latency."

**Expected Response**:
```
RECOMMENDED ARCHITECTURE: CDC to Delta Lake

BRONZE LAYER (Raw CDC):
```python
from pyspark.sql.functions import from_json, col
from pyspark.sql.avro.functions import from_avro

# Auto Loader for CDC files
cdc_df = (spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.schemaLocation", "/checkpoint/cdc_schema")
    .load("/mnt/cdc/postgres/")
)

# Apply CDC changes using MERGE
delta_table.alias("target").merge(
    cdc_df.alias("source"),
    "target.id = source.id"
).whenMatchedUpdateAll(
    condition="source.op = 'U'"
).whenNotMatchedInsertAll(
    condition="source.op = 'I'"
).whenMatchedDelete(
    condition="source.op = 'D'"
).execute()
```

SILVER LAYER (Cleaned):
- Deduplicate using window functions
- Schema validation with constraints
- Enforce data quality with Delta constraints

```sql
ALTER TABLE silver.orders ADD CONSTRAINT valid_amount CHECK (amount > 0);
```

GOLD LAYER (Aggregated):
- Incremental aggregations with watermarks
- Z-ordered for BI queries

LATENCY TARGET: <5 minutes end-to-end
```

### Scenario 3: MLflow Model Registry

**User**: "How do I productionize my scikit-learn model with proper versioning and A/B testing on Databricks?"

**Expected Response**:
```
MLFLOW MODEL LIFECYCLE:

1. TRACK EXPERIMENTS
```python
import mlflow
import mlflow.sklearn

mlflow.set_experiment("/Users/data-scientist/fraud-detection")

with mlflow.start_run(run_name="xgboost_v2"):
    # Log parameters
    mlflow.log_params({"max_depth": 6, "learning_rate": 0.1})
    
    # Train model
    model = xgb.XGBClassifier(**params)
    model.fit(X_train, y_train)
    
    # Log metrics
    mlflow.log_metrics({"auc": 0.94, "f1": 0.89})
    
    # Log model with signature
    signature = infer_signature(X_test, model.predict(X_test))
    mlflow.sklearn.log_model(model, "model", signature=signature)
```

2. REGISTER TO MODEL REGISTRY
```python
result = mlflow.register_model(
    "runs:/<run_id>/model",
    "FraudDetectionModel"
)
```

3. TRANSITION STAGES
```python
client = MlflowClient()
client.transition_model_version_stage(
    name="FraudDetectionModel",
    version=result.version,
    stage="Staging"
)
```

4. A/B TESTING WITH MODEL SERVING
- Deploy multiple versions to Model Serving
- Route traffic percentage between versions
- Monitor latency and accuracy metrics
```

### Scenario 4: Unity Catalog Migration (Anti-Pattern)

**User**: "I want to migrate from Hive metastore to Unity Catalog but keep all my existing table paths."

**Expected Response**:
```
⚠️ MIGRATION ANTI-PATTERN DETECTED

❌ WRONG APPROACH:
- Manually registering external tables
- Keeping same paths without governance review
- Granting broad access without column-level security
- Skipping lineage analysis

✅ CORRECT APPROACH:

1. ASSESS CURRENT STATE
   - Inventory all tables in Hive metastore
   - Document access patterns and dependencies
   - Identify sensitive data (PII/PHI)

2. PLAN CATALOG STRUCTURE
```sql
CREATE CATALOG production;  -- Production workloads
CREATE CATALOG analytics;   -- BI and analytics
CREATE CATALOG sandbox;     -- Development/testing
```

3. MIGRATE WITH GOVERNANCE
   - Use SYNC command for external tables
   - Implement row/column filters for sensitive data
   - Set up automated lineage tracking

4. VALIDATE
   - Compare row counts: Hive vs Unity Catalog
   - Verify query performance
   - Test access controls

5. DEPRECATE OLD METASTORE
   - Set TTL on Hive tables
   - Update all downstream jobs
   - Monitor for orphaned references
```

### Scenario 5: RAG Application with Mosaic AI

**User**: "How do I build a RAG application using Mosaic AI Vector Search and DBRX on Databricks?"

**Expected Response**:
```
RAG ARCHITECTURE WITH MOSAIC AI:

1. SET UP VECTOR SEARCH
```python
from databricks.vector_search.client import VectorSearchClient

client = VectorSearchClient()

# Create vector search endpoint
client.create_endpoint(
    name="knowledge_base_endpoint",
    endpoint_type="STANDARD"
)

# Create index on documentation table
client.create_delta_sync_index(
    endpoint_name="knowledge_base_endpoint",
    index_name="docs_index",
    source_table_name="catalog.schema.documentation",
    primary_key="doc_id",
    embedding_source_column="content",
    embedding_model_endpoint_name="databricks-gte-large-en"
)
```

2. BUILD RAG CHAIN
```python
# Query vector search for relevant context
results = client.similarity_search(
    index_name="docs_index",
    query_text=user_question,
    num_results=5
)

# Combine context with DBRX for generation
context = "\n".join([r["content"] for r in results["result"]["data_array"]])

prompt = f"""Based on the following context, answer the question:

Context:
{context}

Question: {user_question}

Answer:"""

# Use DBRX via Foundation Model APIs
response = client.predict(
    endpoint="databricks-dbrx-instruct",
    inputs={"messages": [{"role": "user", "content": prompt}]}
)
```

3. EVALUATION & MONITORING
- Use Mosaic AI Agent Evaluation for RAG quality
- Monitor retrieval accuracy and generation relevance
- Track token usage and latency metrics

BEST PRACTICES:
- Enable continuous sync for real-time updates
- Use hybrid search (keyword + semantic) for better recall
- Implement re-ranking for improved precision
```

---
