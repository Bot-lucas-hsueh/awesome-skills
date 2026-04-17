# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|-------------|----------|-----------|
| 1 | Using `cudaMemcpy` on every iteration | 🔴 High | Async + pinned memory or unified memory |
| 2 | Coalesced vs strided access in global memory | 🔴 High | Design for coalesced access patterns |
| 3 | No `__syncthreads()` where needed | 🔴 High | Add sync after shared mem loads |
| 4 | Warp divergence (if/else branches) | 🟡 Medium | Restructure to minimize divergence |
| 5 | Using `atomicAdd` excessively | 🟡 Medium | Use reduction pattern instead |
| 6 | Small thread blocks (e.g., 32 threads) | 🟡 Medium | Use 128-256 threads per block |
| 7 | Ignoring memory alignment | 🟡 Medium | Pad arrays, use aligned types |
| 8 | No error checking on CUDA calls | 🔴 High | Add `CHECK_CUDA` macro |
| 9 | Forgetting `cudaDeviceSynchronize()` | 🔴 High | Add after kernel launch if needed |
| 10 | Mixing device IDs across threads | 🔴 High | Set device once per thread |

## 10.2 Best Practices

1. **Always use error checking** - Wrap CUDA calls with error checking macro

```cpp
#define CHECK_CUDA(call) \
    do { \
        cudaError_t err = call; \
        if (err != cudaSuccess) { \
            fprintf(stderr, "CUDA error at %s:%d: %s\n", \
                __FILE__, __LINE__, \
                cudaGetErrorString(err)); \
            exit(EXIT_FAILURE); \
        } \
    } while(0)
```

2. **Use pinned memory for frequent host-device transfers**

```cpp
// Allocate pinned memory
float *h_data;
cudaMallocHost(&h_data, size);  // Pinned (page-locked)

// Copy to device
cudaMemcpy(d_data, h_data, size, cudaMemcpyHostToDevice);
```

3. **Prefer streams for overlapping operations**

```cpp
cudaStream_t stream1, stream2;
cudaStreamCreate(&stream1);
cudaStreamCreate(&stream2);

kernel1<<<grid, block, 0, stream1>>>(d_data1);
kernel2<<<grid, block, 0, stream2>>>(d_data2);  // Runs concurrently
```

4. **Use `restrict` keyword for pointer arguments**

```cpp
// Tells compiler pointers don't alias
__global__ void kernel(float* __restrict__ a, 
                       const float* __restrict__ b);
```

5. **Prefer `__ldg()` for read-only data caches**

```cpp
__global__ void kernel(const float* data) {
    float val = __ldg(&data[idx]);  // Uses texture cache
}
```

## 10.3 Performance Anti-Patterns with Fixes

| Issue | Bad Pattern | Good Pattern |
|-------|------------|--------------|
| Non-coalesced writes | `data[tid] = value` with non-sequential idx | `data[blockIdx.x * N + tid]` |
| Bank conflicts | `shared[i]` and `shared[i+16]` simultaneous | Pad shared memory array |
| Register spilling | Too many local variables | Use shared memory or `__launch_bounds__` |
| Atomic bottleneck | All threads `atomicAdd` to same location | Grid-stride loop with per-block reduction |

## 10.4 Memory Configuration

```bash
# Check current memory configuration
nvidia-smi

# Query device properties in code
cudaDeviceProp prop;
cudaGetDeviceProperties(&prop, device_id);
printf("Shared mem per block: %zu KB\n", prop.sharedMemPerBlock / 1024);
printf("Registers per block: %d\n", prop.regsPerBlock);
printf("Warp size: %d\n", prop.warpSize);
printf("Max threads per block: %d\n", prop.maxThreadsPerBlock);
printf("Compute capability: %d.%d\n", prop.major, prop.minor);
```

## 10.5 Device Selection Best Practices

```cpp
// For multi-GPU systems, select GPU based on workload
int getBestDevice() {
    int deviceCount;
    cudaGetDeviceCount(&deviceCount);
    
    int bestDevice = 0;
    int maxMultiprocessors = 0;
    
    for (int i = 0; i < deviceCount; i++) {
        cudaDeviceProp prop;
        cudaGetDeviceProperties(&prop, i);
        if (prop.multiProcessorCount > maxMultiprocessors) {
            maxMultiprocessors = prop.multiProcessorCount;
            bestDevice = i;
        }
    }
    return bestDevice;
}

// Set device before any CUDA operations
int dev = getBestDevice();
cudaSetDevice(dev);
```
