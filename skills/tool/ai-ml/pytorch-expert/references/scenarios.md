# Scenario Examples

## 9.1 Image Classification with ResNet

**User:** "Fine-tune ResNet for my dataset"

**PyTorch Expert:**
> **ResNet Fine-tuning:**
>
> ```python
> import torchvision.models as models
> import torch.nn as nn
>
> # Load pretrained ResNet
> model = models.resnet50(weights='IMAGENET1K_V1')
>
> # Replace classifier
> num_features = model.fc.in_features
> model.fc = nn.Linear(num_features, num_classes)
>
> # Freeze early layers (optional)
> for param in model.parameters():
>     param.requires_grad = False
>
> # Unfreeze last few layers
> for param in model.layer4.parameters():
>     param.requires_grad = True
> for param in model.fc.parameters():
>     param.requires_grad = True
>
> # Move to device
> device = torch.device("cuda")
> model = model.to(device)
>
> # Loss and optimizer (only trainable params)
> criterion = nn.CrossEntropyLoss()
> optimizer = torch.optim.AdamW(
>     filter(lambda p: p.requires_grad, model.parameters()),
>     lr=0.001
> )
> ```

## 9.2 Custom Attention Layer

**User:** "Implement self-attention for my model"

**PyTorch Expert:**
> **Self-Attention Implementation:**
>
> ```python
> class SelfAttention(nn.Module):
>     def __init__(self, embed_dim):
>         super().__init__()
>         self.query = nn.Linear(embed_dim, embed_dim)
>         self.key = nn.Linear(embed_dim, embed_dim)
>         self.value = nn.Linear(embed_dim, embed_dim)
>         self.scale = embed_dim ** -0.5
>
>     def forward(self, x):
>         # x: (batch, seq_len, embed_dim)
>         batch, seq_len, embed_dim = x.shape
>
>         q = self.query(x)
>         k = self.key(x)
>         v = self.value(x)
>
>         # Attention scores
>         scores = torch.matmul(q, k.transpose(-2, -1)) * self.scale
>         attn_weights = torch.softmax(scores, dim=-1)
>
>         # Apply attention
>         output = torch.matmul(attn_weights, v)
>
>         return output, attn_weights
>
> # Multi-head attention
> class MultiHeadAttention(nn.Module):
>     def __init__(self, embed_dim, num_heads):
>         super().__init__()
>         self.num_heads = num_heads
>         self.head_dim = embed_dim // num_heads
>
>         self.qkv = nn.Linear(embed_dim, embed_dim * 3)
>         self.proj = nn.Linear(embed_dim, embed_dim)
>
>     def forward(self, x):
>         batch, seq_len, embed_dim = x.shape
>
>         qkv = self.qkv(x).reshape(batch, seq_len, 3, self.num_heads, self.head_dim)
>         q, k, v = qkv.unbind(2)
>
>         scale = self.head_dim ** -0.5
>         scores = torch.matmul(q, k.transpose(-2, -1)) * scale
>         attn = torch.softmax(scores, dim=-1)
>
>         out = torch.matmul(attn, v)
>         return self.proj(out.reshape(batch, seq_len, embed_dim))
> ```

## 9.3 Gradient Clipping

**User:** "Prevent gradient explosion in RNN training"

**PyTorch Expert:**
> **Gradient Clipping:**
>
> ```python
> max_norm = 1.0  # Maximum gradient norm
>
> for epoch in range(num_epochs):
>     for batch in dataloader:
>         optimizer.zero_grad()
>
>         output = model(batch)
>         loss = criterion(output, target)
>         loss.backward()
>
>         # Clip gradients
>         torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm)
>
>         # Alternative: clip by value
>         # torch.nn.utils.clip_grad_value_(model.parameters(), clip_value)
>
>         optimizer.step()
> ```

## 9.4 Learning Rate Finder

**User:** "Find optimal learning rate"

**PyTorch Expert:**
> **LR Range Test:**
>
> ```python
> def find_lr(model, dataloader, optimizer, criterion, start_lr=1e-7, end_lr=1, steps=100):
>     import copy
>
>     model = copy.deepcopy(model)
>     optimizer = optim.Adam(model.parameters(), lr=start_lr)
>
>     lrs = []
>     losses = []
>     gamma = (end_lr / start_lr) ** (1 / steps)
>
>     for step in range(steps):
>         for batch in dataloader:
>             loss = train_step(model, batch, optimizer, criterion)
>             losses.append(loss)
>
>             # Update LR
>             for param_group in optimizer.param_groups:
>                 param_group['lr'] *= gamma
>             lrs.append(optimizer.param_groups[0]['lr'])
>
>             if len(losses) >= steps:
>                 break
>
>     return lrs, losses
>
> # Find optimal LR (usually where loss decreases fastest)
> lrs, losses = find_lr(model, train_loader, optimizer, criterion)
> optimal_lr = lrs[find_optimal_idx(losses)]
> ```

## 9.5 ONNX Export and Inference

**User:** "Export model to ONNX for production"

**PyTorch Expert:**
> **ONNX Export:**
>
> ```python
> import torch.onnx
>
> # Set model to eval mode
> model.eval()
>
> # Create dummy input
> dummy_input = torch.randn(1, 3, 224, 224)
>
> # Export
> torch.onnx.export(
>     model,
>     dummy_input,
>     "model.onnx",
>     input_names=["input"],
>     output_names=["output"],
>     dynamic_axes={
>         "input": {0: "batch_size"},
>         "output": {0: "batch_size"}
>     },
>     opset_version=14,  # ONNX opset version
>     do_constant_folding=True,  # Optimize
> )
>
> # Verify export
> import onnx
> onnx_model = onnx.load("model.onnx")
> onnx.checker.check_model(onnx_model)
>
> # ONNX Runtime inference
> import onnxruntime as ort
>
> ort_session = ort.InferenceSession("model.onnx")
> outputs = ort_session.run(None, {"input": numpy_input})
> ```
