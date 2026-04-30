# Custom Training Loop

Fine-grained control with GradientTape and @tf.function.

```python
@tf.function
def train_step(x, y):
    with tf.GradientTape() as tape:
        predictions = model(x, training=True)
        loss = loss_fn(y, predictions)

    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    return loss

# Training loop
for epoch in range(num_epochs):
    epoch_loss_avg = tf.keras.metrics.Mean()
    for x, y in train_ds:
        loss = train_step(x, y)
        epoch_loss_avg.update_state(loss)

    # Validation
    val_results = model.evaluate(val_ds, return_dict=True)
    print(f"Epoch {epoch}: loss={epoch_loss_avg.result():.4f}, val_acc={val_results['accuracy']:.4f}")

# Key points:
# - @tf.function compiles to TensorFlow graph for 2-5x speedup
# - GradientTape records operations for automatic differentiation
# - Metrics need update_state() in custom loops
```
