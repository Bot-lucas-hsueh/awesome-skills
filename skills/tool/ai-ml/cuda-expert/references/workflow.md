# Standard Workflow

## 8.1 CUDA Development Pipeline

```
Phase 1: Environment Setup
├── Verify NVIDIA driver: nvidia-smi
├── Check CUDA version: nvcc --version
├── Verify cuBLAS/cuDNN if needed
└── Install Nsight tools (nsys, ncu, Nsight Eclipse)

Phase 2: Kernel Development
├── Write kernel with __global__ or __device__
├── Choose proper memory spaces (shared, registers)
├── Design thread/block hierarchy
└── Verify correctness with cuda-gdb

Phase 3: Performance Optimization
├── Profile with Nsight Compute (ncu)
├── Check occupancy with Nsight Compute
├── Optimize memory coalescing
├── Reduce shared memory bank conflicts
└── Use pinned memory for host transfers

Phase 4: Deployment
├── Ensure binary targets correct sm_XX
├── Package with appropriate CUDA runtime
└── Test on target hardware
```

## 8.2 Memory Optimization Workflow

### Step 1: Check Memory Access Patterns

```cpp
// BAD: Non-coalesced access (threads access non-adjacent memory)
__global__ void badKernel(float* data) {
    int tid = threadIdx.x;
    int i = tid * stride;  // Each thread jumps
    data[i] = ...;
}

// GOOD: Coalesced access (threads access adjacent memory)
__global__ void goodKernel(float* data) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    data[i] = ...;  // Sequential access
}
```

### Step 2: Shared Memory Optimization

```cpp
__global__ void sharedKernel(float* global, int N) {
    __shared__ float sdata[256];
    
    int tid = threadIdx.x;
    int i = blockIdx.x * blockDim.x + tid;
    
    // Load to shared memory (coalesced global read)
    sdata[tid] = global[i];
    __syncthreads();
    
    // Work with shared memory (fast)
    float result = sdata[tid] * 2.0f;
    __syncthreads();
    
    // Write back to global
    global[i] = result;
}
```

## 8.3 Profiling Workflow

### Using Nsight Compute (ncu)

```bash
# Basic profiling
ncu --set full ./mycuda_app

# Profile specific kernels
ncu --kernel name:myKernel --set full ./mycuda_app

# Profile and export to CSV
ncu --set full --report all --export results ./mycuda_app
```

### Key Metrics to Check

| Metric | Target | Notes |
|--------|--------|-------|
| SM Occupancy | >50% | Higher is usually better |
| Achieved Occupancy | Close to SM | Check for blockers |
| Memory Throughput | Near peak | Indicates bandwidth-bound |
| warp_execution_efficiency | >95% | Checks branch divergence |
| shared_efficiency | High | Good reuse of shared mem |

### Using Nsight Systems (nsys)

```bash
# Timeline profiling
nsys profile --trace=cuda,nvtx ./mycuda_app

# Export for GUI analysis
nsys profile --output=report ./mycuda_app
```

## 8.4 Debugging Workflow

```bash
# Compile with debug symbols (no -O)
nvcc -g -G -O0 code.cu -o code_debug

# Run with cuda-gdb
cuda-gdb ./code_debug

# Common cuda-gdb commands
(cuda-gdb) break myKernel
(cuda-gdb) run
(cuda-gdb) print variable_name
(cuda-gdb) info threads
(cuda-gdb) thread apply all bt
```

## 8.5 Multi-GPU Workflow

```cpp
// Get number of GPUs
int deviceCount;
cudaGetDeviceCount(&deviceCount);

// Set device for current thread
cudaSetDevice(gpu_id);

// Get device properties
cudaDeviceProp prop;
cudaGetDeviceProperties(&prop, gpu_id);

// Peer-to-peer memory access
cudaDeviceCanAccessPeer(&canAccess, dev0, dev1);
if (canAccess) {
    cudaEnablePeerAccess(dev1, 0);
}
```

## 8.6 Mixed Precision Workflow

```cpp
// Use Tensor Cores for matrix multiply (Ampere+)
#include <mma.h>

using namespace nvcuda::wmma;

// Example: 16x16x16 matrix multiply
fragment<matrix_a, m, n, k, half, row_major> a_frag;
fragment<matrix_b, m, n, k, half, col_major> b_frag;
fragment<accumulator, m, n, k, float> acc_frag;

mma_sync(acc_frag, a_frag, b_frag, acc_frag);
```
