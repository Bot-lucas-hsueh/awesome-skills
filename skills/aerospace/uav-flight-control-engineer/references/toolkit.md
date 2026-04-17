## § 6 Professional Toolkit

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **ArduPilot
| **MATLAB/Simulink + Aerospace Blockset** | Model-based design, flight dynamics simulation, rapid control prototyping | Control law design, gain scheduling, nonlinear simulation, code generation for embedded targets |
| **FlightGear + JSBSim** | Open-source 6-DOF flight simulation with realistic aerodynamics | HIL simulation, pilot training, flight envelope exploration without flight risk |
| **ROS2 + MAVROS** | Robot Operating System with MAVLink bridge for UAV autonomy | Mission management, computer vision integration, research platforms |
| **Vector NAV VN-300 / VectorNav** | High-precision GNSS/INS sensor with dual-antenna heading | When heading accuracy <0.5° is required; GPS-challenging environments |
| **STM32CubeIDE + FreeRTOS** | Embedded development for STM32-based flight controllers | Custom FCS hardware development, rate loop implementation at 1kHz+ |
| **QGroundControl
| **XFLR5
| **Python (scipy.signal, control)** | Control system analysis and filter design | Transfer function analysis, Bode plots, stability margins, EKF implementation |

---
