# Standard Workflow

## 8.1 TensorFlow Training Pipeline

```
Phase 1: Data Preparation
├── Create tf.data.Dataset
├── Apply transformations
├── Batch and prefetch
└── Cache if data fits in memory

Phase 2: Model Definition
├── Use Sequential or Functional API
├── Choose appropriate layers
├── Set activation functions
└── Add regularization (Dropout, L2)

Phase 3: Compilation
├── Select optimizer (Adam, SGD)
├── Choose loss function
├── Define metrics
└── Configure callbacks

Phase 4: Training
├── Call model.fit()
├── Monitor training
├── Use callbacks for saving
└── Evaluate on validation

Phase 5: Deployment
├── Save model (SavedModel, HDF5)
├── Convert for TFLite/TensorRT
└── Deploy to target platform
```

## 8.2 Complete Training Example

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Data preparation
(X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()

# Normalize pixel values
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Create dataset
train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))
train_dataset = train_dataset.shuffle(10000)
train_dataset = train_dataset.batch(64).prefetch(tf.data.AUTOTUNE)

val_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test))
val_dataset = val_dataset.batch(64)

# Model definition
def create_model():
    model = keras.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(10)
    ])
    return model

model = create_model()

# Compile
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

# Callbacks
callbacks = [
    keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    ),
    keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.5,
        patience=3
    ),
]

# Train
history = model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=50,
    callbacks=callbacks
)
```

## 8.3 Custom Training Loop

```python
# For complex training logic
model = create_model()
optimizer = keras.optimizers.Adam(learning_rate=0.001)
loss_fn = keras.losses.SparseCategoricalCrossentropy(from_logits=True)
metrics = [keras.metrics.SparseCategoricalAccuracy()]

@tf.function  # Compile for speed
def train_step(x, y):
    with tf.GradientTape() as tape:
        predictions = model(x, training=True)
        loss = loss_fn(y, predictions)

    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    metrics[0].update_state(y, predictions)
    return loss

# Training loop
for epoch in range(num_epochs):
    for batch in train_dataset:
        loss = train_step(batch[0], batch[1])

    print(f"Epoch {epoch}: Loss={loss:.4f}, Acc={metrics[0].result():.4f}")
    metrics[0].reset_states()
```

## 8.4 Transfer Learning Workflow

```python
from tensorflow.keras.applications import ResNet50

# Load pretrained model
base_model = ResNet50(
    weights='imagenet',
    include_top=False,  # Remove classification head
    input_shape=(224, 224, 3)
)

# Freeze base model
base_model.trainable = False

# Add new head
model = keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(num_classes, activation='softmax')
])

# Fine-tune later layers
base_model.trainable = True
for layer in base_model.layers[:-10]:
    layer.trainable = False
```

## 8.5 Distributed Training

```python
# Multi-GPU strategy
strategy = tf.distribute.MirroredStrategy()
print(f"Number of devices: {strategy.num_replicas_in_sync}")

with strategy.scope():
    model = create_model()
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

model.fit(train_dataset, validation_data=val_dataset, epochs=50)

# For TPU
resolver = tf.distribute.cluster_resolver.TPUClusterResolver()
tf.config.experimental_connect_to_cluster(resolver)
tf.tpu.experimental.initialize_tpu_system(resolver)
strategy = tf.distribute.TPUStrategy(resolver)
```

## 8.6 Model Saving

```python
# Save entire model (recommended)
model.save('my_model.keras')  # Keras format

# Load model
loaded_model = keras.models.load_model('my_model.keras')

# Save as SavedModel (for TF Serving)
model.export('saved_model/1/')  # TensorFlow Serving format

# Export for TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)

# Quantized TFLite
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_types = [tf.float16]
tflite_model = converter.convert()
```
