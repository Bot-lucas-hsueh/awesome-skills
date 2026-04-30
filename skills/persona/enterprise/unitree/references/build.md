# 3. BUILD
rosdep install --from-paths . --ignore-src -r -y
cd .. && colcon build
source install/setup.bash
