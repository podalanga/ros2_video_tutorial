# 3R Arm Robot Package

This package contains the URDF description and visualization tools for a 3-DOF robotic arm.

## Package Contents

- `urdf/arm_clean.urdf` - Clean URDF file for the 3R arm robot
- `urdf/assets/` - STL mesh files for robot visualization
- `launch/` - Launch files for different scenarios
- `rviz/arm_config.rviz` - RViz configuration file

## Launch Files

### 1. Full Visualization (with RViz and Joint State Publisher GUI)
```bash
ros2 launch arm_package arm_display.launch.py
```
This launches:
- Robot State Publisher
- Joint State Publisher
- Joint State Publisher GUI (for interactive joint control)
- RViz2 with pre-configured settings

### 2. Headless Mode (no GUI)
```bash
ros2 launch arm_package arm_display.launch.py gui:=false
```
This launches only:
- Robot State Publisher
- Joint State Publisher

### 3. Robot State Publisher Only
```bash
ros2 launch arm_package robot_state_publisher.launch.py
```

## Usage Instructions

1. **Build the package:**
   ```bash
   cd /home/podalanga/Codes/ros/3r_arm_ros
   colcon build --packages-select arm_package
   source install/setup.bash
   ```

2. **Launch with full visualization:**
   ```bash
   ros2 launch arm_package arm_display.launch.py
   ```

3. **Control the robot joints:**
   - Use the Joint State Publisher GUI sliders to move the robot joints
   - The robot will update in real-time in RViz

4. **View robot in RViz:**
   - The robot model will be displayed in RViz
   - TF frames are shown for each link
   - Grid and axes help with spatial orientation

## Robot Description

The 3R arm robot has the following joints:
- `yaw_rotate` - Base rotation joint
- `link1_m2p` - First link pitch joint  
- `link2_joint` - Second link joint

## Troubleshooting

If you encounter issues:

1. **"Package not found" errors:**
   ```bash
   source install/setup.bash
   ```

2. **Missing dependencies:**
   ```bash
   sudo apt install ros-humble-joint-state-publisher-gui ros-humble-robot-state-publisher ros-humble-rviz2
   ```

3. **URDF file not found:**
   Make sure the package is built and sourced properly.

## Files Structure
```
arm_package/
├── launch/
│   ├── arm_display.launch.py
│   └── robot_state_publisher.launch.py
├── rviz/
│   └── arm_config.rviz
├── urdf/
│   ├── arm_clean.urdf
│   ├── arm.urdf
│   ├── config.json
│   └── assets/
│       ├── *.stl files
│       └── *.part files
├── package.xml
├── setup.py
└── README.md
```
