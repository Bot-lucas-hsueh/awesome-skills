## § 6 · Professional Toolkit

| Tool | Purpose — When to Use |
|------|----------------------|
| **Open3D 0.18** | Point cloud I/O, ICP registration, mesh reconstruction, RGBD integration — use for prototyping and offline processing pipelines |
| **PCL 1.13** | Production C++ point cloud library — use for real-time filtering (VoxelGrid, PassThrough, StatisticalOutlier) in ROS2 nodes |
| **TensorRT 10.x** | NVIDIA GPU inference optimization — use when deploying to Jetson Orin for 5-10x speedup over PyTorch |
| **ONNX Runtime 1.18** | Cross-platform inference (CUDA/TensorRT/CoreML EP) — use for portability across Orin, x86 GPU, and ARM CPU |
| **GTSAM 4.2** | Factor graph SLAM and sensor fusion — use for loosely-coupled LiDAR-IMU-GPS fusion with loop closure |
| **OpenCV 4.9** | Camera calibration (fisheye/perspective), stereo rectification, feature extraction (ORB, SIFT) |
| **ROS2 Humble/Iron** | Robot middleware for sensor drivers, TF2 transforms, visualization (RViz2), rosbag2 recording |
| **Autoware.Universe** | Full autonomous driving perception stack — use as reference for production-grade sensor fusion |
| **BrainFlow / Realsense SDK** | Intel RealSense D435i/L515 depth camera SDK — structured light and stereo depth with IMU |
| **KISS-ICP** | Lightweight LiDAR odometry — use when CPU budget is tight; robust to aggressive motion |
