# Deploy with TF Serving

Export model and serve with Docker for production inference.

```python
# Export SavedModel with signature
@tf.function(input_signature=[tf.TensorSpec(shape=[None, 224, 224, 3], dtype=tf.float32)])
def serve_fn(image):
    return model(image)

signatures = {"serving_default": serve_fn.get_concrete_function()}
model.save("gs://bucket/model/1", signatures=signatures)

# Docker serving
# docker run -p 8501:8501 --mount src=gs://bucket/model,target=/models/mymodel \
#   -e MODEL_NAME=mymodel tensorflow/serving

# REST inference
# curl -X POST -d @instances.json http://localhost:8501/v1/models/mymodel:predict

# Key points:
# - input_signature enables batching at inference time
# - signatures dict enables multiple inference modes
# - gs:// for Cloud Storage; use /path for local
# - Expected latency: ~10-50ms per image on T4 GPU
```
