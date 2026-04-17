# Standards & Reference

## 7.1 Official Documentation

- [TensorFlow Documentation](https://www.tensorflow.org/guide)
- [Keras API](https://keras.io/api/)
- [TensorFlow Guide](https://www.tensorflow.org/guide/keras)
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [TensorFlow Model Garden](https://github.com/tensorflow/models)

## 7.2 Installation

```bash
pip install tensorflow
pip install tensorflow[and-cuda]  # With GPU support

# Verify installation
python -c "import tensorflow as tf; print(tf.__version__)"
```

## 7.3 Keras Sequential API

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Sequential model
model = keras.Sequential([
    layers.Dense(256, activation='relu', input_shape=(784,)),
    layers.Dropout(0.3),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

## 7.4 Functional API

```python
# Functional API for complex architectures
inputs = keras.Input(shape=(784,))
x = layers.Dense(256, activation='relu')(inputs)
x = layers.Dropout(0.3)(x)
x = layers.Dense(128, activation='relu')(x)
outputs = layers.Dense(10, activation='softmax')(x)

model = keras.Model(inputs=inputs, outputs=outputs)
```

## 7.5 Layers Reference

| Layer | Description | Common Parameters |
|-------|-------------|-------------------|
| `Dense` | Fully connected | units, activation |
| `Conv2D` | 2D convolution | filters, kernel_size |
| `MaxPooling2D` | Max pooling | pool_size |
| `LSTM` | LSTM layer | units, return_sequences |
| `Embedding` | Word embeddings | input_dim, output_dim |
| `BatchNormalization` | Batch norm | - |
| `Dropout` | Dropout | rate |
| `Flatten` | Flatten tensor | - |
| `GlobalAveragePooling2D` | Global pooling | - |

## 7.6 Optimizers Reference

```python
# Adam (most common)
optimizer = keras.optimizers.Adam(learning_rate=0.001)

# SGD with momentum
optimizer = keras.optimizers.SGD(
    learning_rate=0.01,
    momentum=0.9,
    nesterov=True
)

# AdamW (weight decay)
optimizer = keras.optimizers.AdamW(
    learning_rate=0.001,
    weight_decay=0.01
)

# RMSprop
optimizer = keras.optimizers.RMSprop(learning_rate=0.001)
```

## 7.7 Callbacks Reference

```python
from tensorflow.keras.callbacks import (
    ModelCheckpoint, EarlyStopping, ReduceLROnPlateau,
    TensorBoard, CSVLogger, LearningRateScheduler
)

callbacks = [
    # Save best model
    ModelCheckpoint(
        'best_model.keras',
        monitor='val_loss',
        save_best_only=True
    ),

    # Stop early
    EarlyStopping(
        monitor='val_loss',
        patience=10,
        restore_best_weights=True
    ),

    # Reduce LR on plateau
    ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.5,
        patience=5,
        min_lr=1e-7
    ),

    # TensorBoard
    TensorBoard(log_dir='./logs'),

    # CSV logging
    CSVLogger('training.log'),
]
```

## 7.8 Data Pipeline Reference

```python
# tf.data.Dataset (recommended)
dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))

dataset = dataset.shuffle(buffer_size=10000)
dataset = dataset.batch(32)
dataset = dataset.prefetch(tf.data.AUTOTUNE)

# Image data
train_ds = keras.utils.image_dataset_from_directory(
    'train_dir',
    image_size=(224, 224),
    batch_size=32,
    shuffle=True,
    validation_split=0.2,
    subset='training'
)

# Caching and performance
dataset = dataset.cache()  # Cache after loading
dataset = dataset.prefetch(tf.data.AUTOTUNE)  # Prefetch next batch
```
