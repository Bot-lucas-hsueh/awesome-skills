# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|-------------|----------|-----------|
| 1 | Forgetting `from_logits=True/False` | 🔴 High | Match to final layer activation |
| 2 | Not normalizing input data | 🔴 High | Scale pixel values to [0,1] |
| 3 | Large batch sizes for small datasets | 🟡 Medium | Use smaller batches (16-32) |
| 4 | Not using `tf.data.Dataset` | 🟡 Medium | Use for memory-efficient pipeline |
| 5 | Forgetting to set learning rate | 🟡 Medium | Start with 1e-3 for Adam |
| 6 | Not using callbacks for checkpoints | 🟡 Medium | Add ModelCheckpoint, EarlyStopping |
| 7 | Memory leaks from training loops | 🟡 Medium | Use `@tf.function` decorator |
| 8 | Mismatched input shapes | 🔴 High | Check `input_shape` in first layer |
| 9 | Not freezing pretrained weights | 🟡 Medium | Set `trainable=False` on base |
| 10 | Training on test data | 🔴 High | Always use separate validation set |

## 10.2 Common Error Solutions

### Input Shape Mismatch

```python
# Problem: Shape mismatch error
# Check input shape
print(X_train.shape)  # Should match model input

# Define input explicitly
inputs = keras.Input(shape=(height, width, channels))
model = keras.Model(inputs=inputs, outputs=...)
```

### GPU Memory Issues

```python
# Limit GPU memory growth
gpus = tf.config.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

# Or set memory limit
tf.config.set_logical_device_configuration(
    gpus[0],
    [tf.config.LogicalDeviceConfiguration(memory_limit=4096)]
)
```

### Data Type Issues

```python
# Cast to correct type
X_train = tf.cast(X_train, tf.float32)
y_train = tf.cast(y_train, tf.int32)

# Check mixed precision compatibility
from tensorflow.keras import mixed_precision
mixed_precision.set_global_policy('mixed_float16')  # For A100+
```

## 10.3 Performance Optimization

```python
# Use tf.function for speed
@tf.function
def train_step(x, y):
    with tf.GradientTape() as tape:
        predictions = model(x, training=True)
        loss = loss_fn(y, predictions)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    return loss

# Data pipeline optimization
dataset = dataset.cache()                   # Cache after loading
dataset = dataset.shuffle(buffer_size)      # Shuffle
dataset = dataset.batch(batch_size)         # Batch
dataset = dataset.prefetch(tf.data.AUTOTUNE)  # Prefetch
```

## 10.4 Mixed Precision Training

```python
# Enable mixed precision for faster training
from tensorflow.keras import mixed_precision

# Policy for V100/A100 GPUs
mixed_precision.set_global_policy('mixed_float16')

# Use loss scaling for stability
optimizer = keras.optimizers.Adam(learning_rate=0.001)
optimizer = mixed_precision.LossScaleOptimizer(optimizer, dynamic=True)

# Ensure output layer uses float32
model.add(layers.Dense(1, activation='sigmoid', dtype='float32'))
```

## 10.5 Debugging Tips

```python
# Disable optimizations for debugging
tf.config.run_functions_eagerly(True)

# Enable tensor logging
tf.debugging.set_log_device_placement(True)

# Check for NaN/Inf
model.compile(
    optimizer='adam',
    loss='mse',
    run_eagerly=True,  # Easier debugging
)

# Add assertions
@tf.function
def train_step(x, y):
    predictions = model(x, training=True)
    tf.debugging.assert_all_finite(predictions, "NaN or Inf in predictions")
    # ...
```

## 10.6 Model Deployment Checklist

```python
# Before deployment
# 1. Save in proper format
model.save('model.keras')  # Keras format (recommended)

# 2. Export for TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# 3. Test converted model
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

interpreter.set_tensor(input_index, input_data)
interpreter.invoke()
output = interpreter.get_tensor(output_index)
```
