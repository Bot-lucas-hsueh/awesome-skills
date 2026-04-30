# Image Classification with Transfer Learning

Complete pipeline with EfficientNet, fine-tuning, and mixed precision.

```python
# Data pipeline
train_ds = tf.keras.utils.image_dataset_from_directory(
    "train/", image_size=(224, 224), batch_size=32
).prefetch(tf.data.AUTOTUNE)

# Load pretrained model
base_model = tf.keras.applications.ResNet50(
    include_top=False, weights="imagenet", input_shape=(224, 224, 3)
)
base_model.trainable = False  # Freeze base

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255),
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(num_classes, activation="softmax")
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-3),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train frozen
model.fit(train_ds, epochs=10, validation_data=val_ds)

# Fine-tune last blocks
base_model.trainable = True
for layer in base_model.layers[:-20]:
    layer.trainable = False

model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-5),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
model.fit(train_ds, epochs=10, validation_data=val_ds)
```
