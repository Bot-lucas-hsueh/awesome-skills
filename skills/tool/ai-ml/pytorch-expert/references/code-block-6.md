# Export to ONNX

Export PyTorch model to ONNX for production serving.

```python
import torch.onnx

model = MyModel().eval()

# Create dummy input matching expected shape
dummy_input = torch.randn(1, 3, 224, 224)

# Export
torch.onnx.export(
    model,
    dummy_input,
    "model.onnx",
    export_params=True,
    opset_version=17,
    input_names=["input"],
    output_names=["output"],
    dynamic_axes={
        "input": {0: "batch_size"},
        "output": {0: "batch_size"}
    }
)

# Verify
import onnx
onnx_model = onnx.load("model.onnx")
onnx.checker.check_model(onnx_model)

# Runtime inference
import onnxruntime as ort
session = ort.InferenceSession("model.onnx")
result = session.run(None, {"input": dummy_input.numpy()})

# Key points:
# - opset_version 17 is latest stable
# - dynamic_axes enables variable batch sizes
# - Always verify with onnx.checker.check_model()
```
