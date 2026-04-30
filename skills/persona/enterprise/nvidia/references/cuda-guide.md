# CUDA Programming Patterns & Best Practices

## Execution Model

### Hierarchy
```
Grid → Blocks → Threads → Warps → Lanes
```

| Level | Description | Synchronization |
|-------|-------------|-----------------|
| Grid | Entire kernel launch | None (implicit at end) |
| Block | Up to 1024 threads | `__syncthreads()` |
| Warp | 32 threads (SIMT) | Implicit, lockstep |
| Lane | Single thread | N/A |

### Warp Execution
- Warps execute 32 threads in lockstep
- Divergence: If threads take different branches, both execute (masked)
- Minimize divergence for performance

## Memory Access Patterns

### Coalesced Access
```cuda
// ✅ COALESCED - consecutive threads access consecutive memory
__global__ void coalesced(float* out, const float* in) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    out[idx] = in[idx] * 2.0f;  // Perfect coalescing
}

// ❌ STRIDED - threads access with large stride
__global__ void strided(float* out, const float* in, int stride) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    out[idx] = in[idx * stride] * 2.0f;  // Poor utilization
}

// ✅ FIX - Use shared memory to transpose access pattern
__global__ void transpose_tiled(float* out, const float* in) {
    __shared__ float tile[32][33];  // Pad to avoid bank conflicts
    // Load coalesced into shared memory
    // Read transposed from shared memory
}
```

### Shared Memory Bank Conflicts
- 32 banks, 4 bytes each on modern GPUs
- Conflict: Multiple threads in warp access same bank
- Solution: Pad arrays (`[33]` instead of `[32]`)

## Optimization Checklist

### 1. Occupancy
```
Target: >70% occupancy (active warps / max warps)
```
- Registers per thread (limit to 64 for high occupancy)
- Shared memory per block
- Block size (multiples of 32)

### 2. Memory Throughput
```
Target: >80% of theoretical peak
```
- Use `float4` or `__half2` for vectorized loads
- Align data to 128-byte boundaries
- Prefetch with `__ldg()` (read-only data cache)

### 3. Instruction Throughput
```
Target: Maximize FMA (fused multiply-add) utilization
```
- Use `-use_fast_math` for approximate functions
- Prefer intrinsics: `__sinf()` over `sinf()`
- Avoid integer division/modulo

## CUDA Streams & Async

```cuda
// Create streams
cudaStream_t stream1, stream2;
cudaStreamCreate(&stream1);
cudaStreamCreate(&stream2);

// Overlap compute and transfer
cudaMemcpyAsync(d_a1, h_a1, size, cudaMemcpyHostToDevice, stream1);
kernel<<<blocks, threads, 0, stream1>>>(d_a1, d_b1);
cudaMemcpyAsync(h_c1, d_c1, size, cudaMemcpyDeviceToHost, stream1);

// Simultaneously on stream2
cudaMemcpyAsync(d_a2, h_a2, size, cudaMemcpyHostToDevice, stream2);
kernel<<<blocks, threads, 0, stream2>>>(d_a2, d_b2);
```

## CUDA Graphs

Capture and replay sequences for reduced CPU overhead:

```cuda
// Capture graph
cudaStreamBeginCapture(stream, cudaStreamCaptureModeGlobal);
for (int i = 0; i < 10; i++) {
    kernel<<<blocks, threads, 0, stream>>>(...);
    cudaMemcpyAsync(..., stream);
}
cudaGraph_t graph;
cudaStreamEndCapture(stream, &graph);

// Instantiate executable graph
cudaGraphExec_t instance;
cudaGraphInstantiate(&instance, graph, NULL, NULL, 0);

// Launch repeatedly (low CPU overhead)
for (int iter = 0; iter < 1000; iter++) {
    cudaGraphLaunch(instance, stream);
}
```

## Tensor Core Programming

### WMMA (Warp-level Matrix Multiply Accumulate)
```cuda
#include <mma.h>
using namespace nvcuda::wmma;

__global__ void wmma_kernel(...) {
    fragment<matrix_a, 16, 16, 16, half, row_major> a_frag;
    fragment<matrix_b, 16, 16, 16, half, col_major> b_frag;
    fragment<accumulator, 16, 16, 16, half> c_frag;
    
    load_matrix_sync(a_frag, a + a_offset, lda);
    load_matrix_sync(b_frag, b + b_offset, ldb);
    fill_fragment(c_frag, 0.0f);
    
    mma_sync(c_frag, a_frag, b_frag, c_frag);
    
    store_matrix_sync(c + c_offset, c_frag, ldc, mem_row_major);
}
```

### CUTLASS (Production-Ready)
```cuda
// Define GEMM type
using Gemm = cutlass::gemm::device::Gemm<
    cutlass::half_t, cutlass::layout::RowMajor,
    cutlass::half_t, cutlass::layout::ColumnMajor,
    cutlass::half_t, cutlass::layout::RowMajor,
    float,  // accumulator type
    cutlass::arch::OpClassTensorCore,
    cutlass::arch::Sm90  // Hopper
>;

// Launch
Gemm gemm_op;
gemm_op({{...}, {ptr_A, lda}, {ptr_B, ldb}, {ptr_C, ldc}, {ptr_D, ldd}, {alpha, beta}});
```

## Multi-GPU with NCCL

```cuda
// Initialize NCCL
ncclComm_t comm;
ncclUniqueId id;
if (rank == 0) ncclGetUniqueId(&id);
MPI_Bcast(&id, sizeof(id), MPI_BYTE, 0, MPI_COMM_WORLD);
ncclCommInitRank(&comm, nRanks, id, rank);

// AllReduce
ncclAllReduce(sendbuff, recvbuff, count, ncclFloat, ncclSum, comm, stream);

// AllGather for tensor parallelism
ncclAllGather(sendbuff, recvbuff, sendcount, ncclHalf, comm, stream);
```

## Debugging

### CUDA-GDB
```bash
cuda-gdb ./program
(cuda-gdb) set cuda break_on_launch application
(cuda-gdb) run
(cuda-gdb) cuda thread (0 0 0)  # Focus on specific thread
(cuda-gdb) print variable
```

### Compute Sanitizer
```bash
# Memory error detection
compute-sanitizer --tool memcheck ./program

# Race condition detection
compute-sanitizer --tool racecheck ./program

# Leak detection
compute-sanitizer --tool initcheck ./program
```

### Nsight Compute
```bash
# Collect detailed kernel metrics
ncu --metrics sm__throughput.avg.pct_of_peak_sustained_elapsed \
    --target-processes all \
    ./program
```

---

*Reference: CUDA C++ Programming Guide, CUDA Best Practices Guide*
