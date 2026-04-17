## § 2 · What This Skill Does

**Point Cloud Processing Pipeline Design** — Designs complete preprocessing chains from raw LiDAR packets (Velodyne VLP-32C, Ouster OS1-128, Livox Mid-360) through voxel downsampling, ground removal (RANSAC, Patchwork++), clustering (DBSCAN, HDBSCAN), and feature extraction. Provides Open3D and PCL code with benchmarked timing per stage.

**Multi-Sensor Fusion Architecture** — Architects tightly-coupled and loosely-coupled fusion schemes for camera+LiDAR+IMU, selecting appropriate state estimators (EKF vs factor graph), handling asynchronous message timing with interpolation, and validating consistency via Mahalanobis gating.

**SLAM System Integration & Tuning** — Integrates and tunes ORB-SLAM3, LIO-SAM, FAST-LIO2 for specific environments, adjusts map parameters, loop closure thresholds, IMU preintegration noise parameters, and validates absolute trajectory error (ATE) and relative pose error (RPE) against ground truth.

**Edge Inference Optimization** — Converts PyTorch models to TensorRT engines with INT8/FP16 calibration, achieves 5-10x speedup on Jetson Orin, validates accuracy degradation (< 1% mAP drop acceptable), and integrates into ROS2 nodes with zero-copy memory sharing via CUDA Unified Memory.
