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
      
        $ rosrun strands_morse simulator.sh tum_kitchen
       
  Please note: Using a depth camera requires Python 3.3 and a corresponding Blender version:

        $ rosrun strands_morse simulator.sh tum_kitchen default-with-kinect.py
       
3. Launch the 2D navigation:

        $ roslaunch strands_morse tum_kitchen_nav2d.launch


-----------------

To start run the MORSE simulation of the UB CS building with a ScitosA5:
For the whole building:
      
       $ rosrun strands_morse simulator.sh bham_cs_sim bham_cs.py

Only for the lower ground floor:
       $ rosrun strands_morse simulator.sh bham_cs_sim bham_cs_LG.py


