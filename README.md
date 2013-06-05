strands_morse
=============

A MORSE-based simulation for the STRANDS project

Prerequisites
-------------

For running the simulation you would need:

* [MORSE](http://www.openrobots.org/morse/doc/latest/user/installation.html) 
* [Blender](http://www.blender.org/download/get-blender/)
* [ROS](http://www.ros.org/wiki/ROS/Installation)

Please refer to the respective installation guides to install them on your system. 

The current software has been tested under the following configuration:

* MORSE (latest)
* Blender 2.63a
* ROS Groovy
* Python 3.2.3 (3.3.0)
* Ubuntu 12.04 LTS  

Getting Started
---------------

Start four terminals and run the commands below  

1. Fire up roscore:
   
       $ roscore
       
2. Run the MORSE simulation:
   
       $ morse run strands_sim 
      
  Alternatively, run:
      
       $ rosrun strands_sim simulator.sh
       
  Please note: Using a depth camera requires Python 3.3 and a corresponding Blender version:

       $ morse run strands_sim default-with-kinect.py

3. Launch the ROS-based navigation:
   
       $ roslaunch strands_morse_2dnav nav.launch
       
4. Run and configure RVIZ

       $ rosrun rviz rviz 
    
5. Use RVIZ to navigate to places the environment. 

6. Well done!



To start run the MORSE simulation of the UB CS building with a ScitosA5:
      
       $ rosrun strands_sim simulator.sh bham_cs.py


