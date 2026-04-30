# python Example

```
# Window function for running total
df.withColumn(
    "running_total",
    sum("amount").over(Window.partitionBy("customer_id").orderBy("created_at"))
)

# Lead/Lag for comparison
df.withColumn("prev_amount", lag("amount", 1).over(Window.partitionBy("customer_id").orderBy("created_at")))

# UDF (avoid when possible, use pandas_udf for performance)
from pyspark.sql.functions import udf

@udf(returnType=StringType())
def classify_order(amount):
    if amount < 50:
        return "small"
    elif amount < 200:
        return "medium"
    return "large"

df.withColumn("order_size", classify_order("amount"))

# Pandas UDF (vectorized, much faster)
from pyspark.sql.functions import pandas_udf
import pandas as pd

@pandas_udf(DoubleType())
def calculate_discount(pdf: pd.Series) -> pd.Series:
    return pdf * 0.1

df.withColumn("discount", calculate_discount(col("amount")))
```
