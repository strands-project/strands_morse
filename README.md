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

* MORSE (strands-project/morse)
* Blender 2.63a
* ROS Groovy
* Python 3.2.3 (3.3.0)
* Ubuntu 12.04 LTS

Please note: Using a depth camera requires Python 3.3.0 and a corresponding Blender version (>2.65). 

Getting Started
---------------

Start some terminals and run the commands below:

1. Fire up roscore:
   
        $ roscore
       
2. Run the MORSE simulation:
      
        $ roslaunch strands_morse bham_cs_morse.launch
      
3. (optional) Launch the 2D navigation:

        $ roslaunch strands_morse bham_cs_nav2d.launch

4. (optional) To visualize the environment model in RVIZ run 

        $ rosrun rviz rviz
      
        $ roslaunch strands_morse bham_cs_rviz.launch
        
   and add a new display of type `RobotModel` in RVIZ. Set the robot_description to
   `/env/env_description` and TF prefix to `env`. (requires [strands_utils](https://github.com/strands-project/strands_utils))

The commands above use the lower ground floor of the Computer Science building
by default. For simulating a different level of the building please run:

        $ roslaunch strands_morse bham_cs_morse.launch env:=cs_1

   Other available environments are: <strong>cs_lg</strong>, <strong>cs_ug</strong>, <strong>cs_1</strong>, <strong>cs_2</strong>, <strong>cs</strong> (for the whole building)

   Similarly, you have to run the navigation and visualization with an extra argument as follows:

        $ roslaunch strands_morse bham_cs_nav2d.launch env:=cs_1               

        $ roslaunch strands_morse bham_cs_rviz.launch env:=cs_1
   
-----------------

To start run the MORSE simulation of the TUM kitchen with a ScitosA5:
      
       $ roslaunch strands_morse tum_kitchen_morse.launch

  Alternatively:

       $ roslaunch strands_morse tum_kitchen_morse.launch env:=tum_kitchen_WITHOUT_CAMERAS

-----------------

The Scitos robot model is equipped with a video, depth and semantic camera by
default. 

If you wish to start the robot without any camera provide
`Scitosa5.WITHOUT_CAMERAS` in the robot's constructor (see example below).
Starting the robot without any camera is useful to run MORSE in
<strong>fast_mode</strong>.

If you only want to disable the depth camera, provide
`Scitosa5.WITHOUT_DEPTHCAM` in the constructor. This might be useful if you run
MORSE on MacOSX, because users have reported problems when using a depth
camera.

Example usage in the MORSE builder script:

* with cameras:

        robot = Scitosa5()
        # Alterntively
        # robot = Scitosa5(Scitosa5.WITH_CAMERAS)

* without cameras
                            
        robot = Scitosa5(Scitosa5.WITHOUT_CAMERAS)

* without depth camera
        
        robot = Scitosa5(Scitosa5.WITHOUT_DEPTHCAMS)

* with OpenNI stack generating point clouds and images, be sure to launch `roslaunch strands_morse generate_camera_topics.launch` and
        
        robot = Scitosa5(Scitosa5.WITH_OPENNI)

