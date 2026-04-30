# torch.compile

JIT compilation for faster inference and training.

```python
# Compile model for faster inference
model = MyModel().cuda()
model = torch.compile(model, mode="reduce-overhead")  # or "max-autotune"

# For training (experimental in PyTorch 2.x)
model = torch.compile(model, mode="default")

# Inspect compiled graph
@torch.compile(dynamic=True)
def fn(x):
    return model(x)

# Check if compiled
print(torch._dynamo.config.guard_n_modules)  # > 0 means compiled

# Compile options:
# - "default": balanced optimization
# - "reduce-overhead": reduce Python overhead (recommended for inference)
# - "max-autotune": maximize throughput (longer compile time)

# Common issues:
# - Use dynamic=True for variable input shapes
# - Some operations not yet supported in graph mode
# - First call has overhead from compilation
```
