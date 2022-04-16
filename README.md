# 3D-Occupancy-Maps-With-Quadrotors
To use this project on your local computer, clone it with these commands

    cd /catkin_ws/src
    git clone https://github.com/DolceParadise/3D-Occupancy-Maps-With-Quadrotors.git

## Prerequisites
To run this project, you must have a system with ROS Noetic and Teleop Twist Keyboard installed. Follow the instructions below for installation

    cd /catkin_ws/src/3D-Occupancy-Maps-With-Quadrotors
    chmod +x install_ros_noetic.sh
    ./install_ros_noetic.sh
    sudo apt-get install ros-noetic-teleop-twist-keyboard

## Mapping the world

After cloning the repository into src, run 

    cd /catkin_ws/ 
    catkin_make
 
 After the files are built, run the following commands in seperate terminals 

    roslaunch drone_test start.launch
    rosrun rviz rviz
    roslaunch drone_test gmap.launch
    roslaunch octomap_server octomap_mapping
    rosrun teleop_twist_keyboard teleop_twist_keyboard.py

After running these commands, a gazebo world will be launched with the quadrotor stationary on the ground along with the rviz visualisation of the map. Add a marker array in the rviz window and changed the field to occupancy_marker_array. Go to the terminal window with the teleop twist keyboard and start running the drone using teleop instructions. Once the drone takes off and starts navigating the world, the rviz visualization is populated with the occupancy map. You can save the map with 

    rosrun octomap_server octomap_saver -f my_octomap.ot
   for saving in octree format and 

    rosrun octomap_server octomap_saver -f my_octomap.bt
   for saving in binary tree format. 
   
## Working Demo 


https://user-images.githubusercontent.com/74451989/163691225-e5de2031-65c9-4553-9bf0-5f4ebf382c77.mp4




## Map your own world 
You can map any world using this project. Just replace the new_world in 3D-Occupancy-Maps-With-Quadrotors/drone_test/worlds and rename it new_world. Post that, follow the commands given above and voila! You can create the occupancy map of your gazebo world. 
## Future work

 1. Add autonomous mapping to eliminate the need of teleop
 2. Add Path Planning 

If you'd like to contribute to this project in any of the above fields or add a custom implementation, feel free to open an issue, fork the repository and make a pull request. You can contact me via [email](mailto:pratikmsr@outlook.com)

## Acknowledgement

This project was made by a student team of the RoboReg, a robotics research group part of the [Robotics Club IIT BHU](https://github.com/Robotics-Club-IIT-BHU). All the external files in this project are open source and used in good faith. We used the source code from the following respositories and we'd like to thank their maintainer. 

 1. [RAFALAMAO](https://github.com/RAFALAMAO)/**[hector_quadrotor_noetic](https://github.com/RAFALAMAO/hector_quadrotor_noetic)**
 2. [OctoMap](https://github.com/OctoMap)/**[octomap_mapping](https://github.com/OctoMap/octomap_mapping)**

## 
Made with the valuable contributions of 
|<img src="https://avatars.githubusercontent.com/u/77875542?v=4" alt="drawing" width="150"/> | <img src="https://avatars.githubusercontent.com/u/96468536?v=4" alt="drawing" width="150"/> | 
|--|--|
| [Chahak Jethani](https://github.com/sherlockholmes1603) | [Amitesh Vatsa](https://github.com/vtsamit) |

