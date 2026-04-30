# Functional API with Multi-Input

Multi-input Keras model for heterogeneous data sources.

```python
# Multi-input model
text_input = tf.keras.Input(shape=(max_len,), dtype=tf.int32, name="text")
embedding = tf.keras.layers.Embedding(vocab_size, 128)(text_input)
lstm_out = tf.keras.layers.Bidirectional(
    tf.keras.layers.LSTM(64)
)(embedding)

metadata_input = tf.keras.Input(shape=(num_metadata_features,), name="metadata")
dense_meta = tf.keras.layers.Dense(32, activation="relu")(metadata_input)

concat = tf.keras.layers.Concatenate()([lstm_out, dense_meta])
output = tf.keras.layers.Dense(1, activation="sigmoid")(concat)

model = tf.keras.Model(
    inputs=[text_input, metadata_input],
    outputs=output,
    name="multi_input_classifier"
)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
    loss="binary_crossentropy",
    metrics=["AUC", "Precision", "Recall"]
)

# Training
model.fit(
    {"text": text_data, "metadata": meta_data},
    {"output": labels},
    epochs=10,
    batch_size=32
)
```
