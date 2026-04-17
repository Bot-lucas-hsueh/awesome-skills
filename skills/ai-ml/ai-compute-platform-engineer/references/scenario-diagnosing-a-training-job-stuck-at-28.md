## 9.2 Scenario: Diagnosing a Training Job Stuck at 28% MFU

**User:** "Our LLaMA-13B training on 64 A100s is only achieving 28% MFU. We expected ~45%. What's wrong?"

**AI Compute Platform Engineer:**
> **Step 1 — Profile with Nsight Systems:**
> ```bash
> # Run one training step with profiling
> nsys profile --trace=cuda,nvtx,nccl \
>   --output=/tmp/profile \
>   python train.py --max-steps 5
> ```
>
> **Common Root Causes at 28% MFU (diagnostic tree):**
>
> | Symptom | Root Cause | Probability |
> |---------|------------|-------------|
> | NCCL operations dominate timeline | IB link speed mismatch (100 Gb/s vs 200 Gb/s) or wrong NCCL_SOCKET_IFNAME | 40% |
> | GPU compute is idle 30%+ of time | DataLoader blocking — CPU preprocessing bottleneck | 25% |
> | Large variance in step time | One slow GPU (thermal throttle); single-rank stragglers | 20% |
> | Checkpoint blocks training | Synchronous checkpoint blocking backward pass | 15% |
>
> **Step 2 — Quick Diagnostic Commands:**
> ```bash
> # Check IB link speed (should be 200 Gb/s for HDR)
> ibstat | grep Rate
>
> # Verify NCCL is using IB (not Ethernet)
> export NCCL_DEBUG=INFO
> # Look for "NET/IB" in NCCL init logs — not "NET/Socket"
>
> # Check GPU temperature for throttling
> nvidia-smi --query-gpu=temperature.gpu,clocks_throttle_reasons.active \
>   --format=csv -l 5
>
> # NCCL bandwidth test (should be >70% of 200 Gb/s × 8 = 1.6 Tb/s)
> python -m torch.distributed.launch --nproc_per_node=8 \
>   nccl_tests/all_reduce_perf -b 1G -e 1G -f 2 -g 1
> ```
>
> **Most Likely Fix (based on 28% MFU symptom):**
> - If NCCL using Ethernet: `export NCCL_SOCKET_IFNAME=ib0` → expect +15% MFU
> - If DataLoader bottleneck: add `num_workers=8, pin_memory=True, prefetch_factor=4` → +5-10% MFU
> - If GPU thermal throttle: increase chassis airflow; contact datacenter ops for cooling → +3-8% MFU
>
> **Expected outcome**: 28% → 42-48% MFU after fixing NCCL interface + DataLoader.

---

### 9.3 Scenario: Designing a Fault-Tolerant Training Pipeline for 30-Day Runs

**User:** "We're running a 70B model training that will take 45 days on 512 GPUs. How do we design for fault tolerance — we've lost 3 days of training to failures already."

**AI Compute Platform Engineer:**
> **Failure Math for 512 H100s, 45-day Run:**
> - GPU MTBF: ~4,000 hours per GPU → per-cluster MTBF: 4,000
> - Over 45 days (1,080 hours): expected ~138 GPU failures → ~138 potential checkpoints lost without FT
>
> **Step 1 — Checkpoint Frequency:**
> ```python
> # Optimal checkpoint interval = MTBF
> optimal_interval_hours = 7.8
> steps_per_hour = 3600
> checkpoint_every_n_steps = int(optimal_interval_hours * steps_per_hour)
> # Example: 20 sec/step → 3.9 × 180 = 702 → checkpoint every 700 steps
> ```
>
> **Step 2 — Async Sharded Checkpoint (PyTorch DCP):**
> ```python
> from torch.distributed.checkpoint import FileSystemWriter, save_state_dict
> import threading
>
> def async_save_checkpoint(state, path):
>     """Non-blocking checkpoint — does not stall training"""
>     def _save():
>         writer = FileSystemWriter(path)
>         save_state_dict(state, storage_writer=writer)
>     t = threading.Thread(target=_save, daemon=True)
>     t.start()
>     return t  # join before next checkpoint to prevent overlap
>
> # In training loop:
> if step % checkpoint_every_n_steps == 0:
>     if prev_checkpoint_thread:
>         prev_checkpoint_thread.join()  # ensure previous completed
>     prev_checkpoint_thread = async_save_checkpoint(
>         {"model": model, "optimizer": optimizer, "step": step},
>         f"/checkpoint/ckpt-{step}"
>     )
> ```
>
> **Step 3 — Elastic Recovery with TorchElastic:**
> ```yaml
> # SLURM job script with auto-restart
> #SBATCH --requeue        # re-queue job on node failure
> #SBATCH --open-mode=append  # append logs (don't overwrite)
>
> srun torchrun \
>   --nnodes=$SLURM_NNODES \
>   --nproc_per_node=8 \
>   --rdzv_backend=c10d \
>   --rdzv_endpoint=$MASTER_ADDR:$MASTER_PORT \
>   --max_restarts=10 \  # auto-restart up to 10 times
>   train.py --resume-from-checkpoint /checkpoint/latest
> ```
>
> **Step 4 — Checkpoint Rotation (keep 3):**
> ```python
> checkpoints = sorted(glob("/checkpoint/ckpt-*"), key=lambda x: int(x.split('-')[-1]))
> if len(checkpoints) > 3:
>     shutil.rmtree(checkpoints[0])  # delete oldest
> ```
>
> **Expected outcome**: From losing days of training → job completion rate >99.5%, MTTF >8 hours per job.

---

