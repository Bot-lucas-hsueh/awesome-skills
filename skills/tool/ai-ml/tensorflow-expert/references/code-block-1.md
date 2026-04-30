# tf.data Pipeline

Efficient data pipelines with parallelization and prefetching.

```python
# Efficient data pipeline
train_ds = tf.data.Dataset.from_tensor_slices((X_train, y_train))
train_ds = (
    train_ds
    .shuffle(buffer_size=10000)
    .batch(batch_size=32)
    .prefetch(tf.data.AUTOTUNE)
    .map(lambda x, y: (tf.cast(x, tf.float32), y), num_parallel_calls=tf.data.AUTOTUNE)
    .cache()
)

# For large files (image dataset)
test_ds = tf.data.Dataset.load_from_directory(
    "gs://bucket/dataset/",
    labels="inferred",
    image_size=(224, 224),
    batch_size=32
)

# Key points:
# - cache() loads data into memory after first epoch
# - prefetch(tf.data.AUTOTUNE) overlaps data loading and training
# - num_parallel_calls speeds up transformations
# - shuffle before batch for proper randomization
```
