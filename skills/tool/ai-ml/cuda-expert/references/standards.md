# Standards & Reference

## 7.1 Official Documentation

- [CUDA Toolkit Documentation](https://docs.nvidia.com/cuda/)
- [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)
- [CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)
- [NVIDIA Developer Blog](https://developer.nvidia.com/blog/)
- [CUDA Quick Start Guide](https://docs.nvidia.com/cuda/cuda-quick-start-guide/)

## 7.2 Kernel Execution Configuration

### Thread Hierarchy

```
Grid → Block → Thread
   ↓      ↓       ↓
(ndim)  (dim3)  (dim3)

Grid: total blocks (launch parameter)
Block: threads per block (must be ≤1024 for compute capability <9.0)
Thread: individual execution unit
```

### Launch Configuration Best Practices

```cpp
// Minimal threads per block (occupancy baseline)
dim3 blockSize(256);  // Common choice for compute capability 7.x+

// Calculate grid size from data size
int gridSize = (n + blockSize.x - 1) / blockSize.x;
myKernel<<<gridSize, blockSize>>>(args);

// For 3D data
dim3 blockSize(8, 8, 8);  // 512 threads per block
dim3 gridSize((nx+7)/8, (ny+7)/8, (nz+7)/8);
```

## 7.3 Memory Types Reference

| Memory Type | Scope | Latency | Bandwidth | Managed By |
|------------|-------|---------|-----------|------------|
| Register | Thread | ~0 cycles | Very High | Compiler |
| Local Memory | Thread | ~400 cycles | High | Compiler (spill) |
| Shared Memory | Block | ~1 cycle | Very High | Programmer |
| Global Memory | Global | ~400 cycles | High (device-dependent) | Programmer |
| Constant Memory | Global | ~1 cycle (cached) | Device-dependent | Programmer |
| Texture Memory | Global | ~1 cycle (cached) | Device-dependent | Programmer |

## 7.4 Common CUDA Runtime API Functions

| Function | Description |
|----------|-------------|
| `cudaMalloc()` | Allocate device memory |
| `cudaMemcpy()` | Copy between host/device |
| `cudaFree()` | Free device memory |
| `cudaDeviceSynchronize()` | Sync all threads |
| `cudaGetDeviceProperties()` | Query device capabilities |

## 7.5 Compute Capability & Device Support

| Compute Capability | GPUs | Key Features |
|-------------------|------|--------------|
| 7.0 (Volta) | V100 | Tensor Cores, FP16 |
| 7.5 (Turing) | RTX 20xx | Tensor Cores, RT Cores |
| 8.0 (Ampere) | A100 | FP64, TF32, structured sparsity |
| 8.9 (Ada) | RTX 40xx | DLSS 3, improved ray tracing |
| 9.0 (Hopper) | H100 | Transformer Engine, FP8 |

## 7.6 Compiler Flags

```bash
# Basic optimization
nvcc -O3 code.cu -o code

# Specify architecture
nvcc -O3 -arch=sm_80 code.cu -o code  # For Ampere (A100)
nvcc -O3 -arch=sm_90 code.cu -o code  # For Hopper (H100)

# Fast math (may reduce precision)
nvcc -O3 --use_fast_math code.cu -o code

# Separate compilation for large projects
nvcc -O3 -dc module1.cu module2.cu
nvcc -O3 -dlink module1.o module2.o -o link.o
```
