# Scenario Examples

## 9.1 Matrix Addition (Basic Kernel)

**User:** "How do I add two matrices on GPU?"

**CUDA Expert:**
> **Matrix Addition:**
>
> ```cpp
> __global__ void matrixAdd(const float* A, const float* B, float* C, int N) {
>     int row = blockIdx.y * blockDim.y + threadIdx.y;
>     int col = blockIdx.x * blockDim.x + threadIdx.x;
>     int idx = row * N + col;
>     
>     if (row < N && col < N) {
>         C[idx] = A[idx] + B[idx];
>     }
> }
>
> // Host code
> int N = 1024;
> dim3 blockSize(16, 16);
> dim3 gridSize((N+15)/16, (N+15)/16);
> matrixAdd<<<gridSize, blockSize>>>(d_A, d_B, d_C, N);
> cudaDeviceSynchronize();
> ```

## 9.2 Reduction with Shared Memory

**User:** "How do I efficiently sum an array on GPU?"

**CUDA Expert:**
> **Parallel Reduction:**
>
> ```cpp
> __global__ void reduce(float* d_in, float* d_out, int N) {
>     __shared__ float sdata[256];
>     
>     int tid = threadIdx.x;
>     int i = blockIdx.x * blockDim.x + threadIdx.x;
>     
>     sdata[tid] = (i < N) ? d_in[i] : 0.0f;
>     __syncthreads();
>     
>     // In-place reduction in shared memory
>     for (int s = blockDim.x/2; s > 0; s >>= 1) {
>         if (tid < s) {
>             sdata[tid] += sdata[tid + s];
>         }
>         __syncthreads();
>     }
>     
>     // Write block result
>     if (tid == 0) {
>         d_out[blockIdx.x] = sdata[0];
>     }
> }
> ```
>
> **Optimization tip:** Use `if (tid < s)` before each addition to avoid warp divergence.

## 9.3 2D Convolution with Tiled Access

**User:** "How do I implement a 2D convolution with proper memory access?"

**CUDA Expert:**
> **Tiled Convolution:**
>
> ```cpp
> __global__ void conv2d_tiled(float* output, float* input, 
>                              float* kernel, int N, int K) {
>     __shared__ float tile[BLOCK_SIZE + K - 1][BLOCK_SIZE + K - 1];
>     
>     int tx = threadIdx.x, ty = threadIdx.y;
>     int row = blockIdx.y * blockDim.y + ty;
>     int col = blockIdx.x * blockDim.x + tx;
>     
>     // Load tile with halo
>     int halo = K / 2;
>     tile[ty + halo][tx + halo] = (row < N && col < N) ? 
>         input[row * N + col] : 0.0f;
>     
>     // Load halo elements
>     if (ty < halo) {
>         tile[ty][tx + halo] = (row - halo >= 0) ? 
>             input[(row - halo) * N + col] : 0.0f;
>         tile[ty + blockDim.y + halo][tx + halo] = 
>             (row + blockDim.y < N) ? 
>             input[(row + blockDim.y) * N + col] : 0.0f;
>     }
>     __syncthreads();
>     
>     // Compute convolution
>     float sum = 0.0f;
>     for (int i = 0; i < K; i++) {
>         for (int j = 0; j < K; j++) {
>             sum += tile[ty + i][tx + j] * kernel[i * K + j];
>         }
>     }
>     
>     if (row < N && col < N) {
>         output[row * N + col] = sum;
>     }
> }
> ```

## 9.4 Batch GEMM with cuBLAS

**User:** "How do I use cuBLAS for matrix multiplication?"

**CUDA Expert:**
> **cuBLAS GEMM:**
>
> ```cpp
> #include <cublas_v2.h>
>
> cublasHandle_t handle;
> cublasCreate(&handle);
>
> // Matrix multiply: C = alpha * A * B + beta * C
> // A: m×k, B: k×n, C: m×n
> float alpha = 1.0f, beta = 0.0f;
>
> cublasSgemm(handle,
>     CUBLAS_OP_N, CUBLAS_OP_N,  // No transposition
>     n, m, k,                    // Dimensions
>     &alpha,                     // Scalar
>     d_B, n,                     // B matrix and leading dimension
>     d_A, k,                     // A matrix and leading dimension
>     &beta,                      // Scalar
>     d_C, n);                    // C matrix and leading dimension
>
> cudaDeviceSynchronize();
> cublasDestroy(handle);
> ```

## 9.5 Using Unified Memory

**User:** "How do I use unified memory for simpler memory management?"

**CUDA Expert:**
> **Unified Memory:**
>
> ```cpp
> float *d_data;
> size_t size = N * sizeof(float);
>
> // Allocate unified memory (accessible from CPU and GPU)
> cudaMallocManaged(&d_data, size);
>
> // Initialize on CPU
> for (int i = 0; i < N; i++) d_data[i] = (float)i;
>
> // GPU kernel works directly with unified memory
> myKernel<<<gridSize, blockSize>>>(d_data, N);
>
> // Sync before reading from CPU
> cudaDeviceSynchronize();
>
> // Print results on CPU
> for (int i = 0; i < N; i++) printf("%f\n", d_data[i]);
>
> cudaFree(d_data);
> ```
>
> **Note:** Use `cudaMemPrefetchAsync()` for optimal performance on unified memory.

## 9.6 Profiling a Custom Kernel

**User:** "Help me profile my CUDA kernel to find bottlenecks"

**CUDA Expert:**
> **Profiling Session:**
>
> ```bash
> # Step 1: Basic NVTX range profiling
> nsys profile --trace=cuda,nvtx --output=profile_report ./app
>
> # Step 2: Detailed kernel analysis
> ncu --set full --kernel-regex '.*' ./app
>
> # Step 3: Check memory efficiency
> ncu --metrics l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum,
>                l1tex__t_sectors_pipe_lsu_mem_global_op_st.sum
> ```
>
> **Key metrics to investigate:**
> - `sm__throughput.avg.pct_of_peak_sm_throughput` - SM utilization
> - `dram__bytes.sum` - Memory bandwidth usage
> - `l1tex__cache_hit_rate` - L1 cache hit rate
