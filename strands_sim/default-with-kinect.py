#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <strands_sim> environment

Please note: For using the Kinect sensor, or any depth camera, Python 3.3 is required.

If you have problems with the installation please check out this answer:
https://sympa.laas.fr/sympa/arc/morse-users/2013-04/msg00015.html

"""
from morse.builder import *
from strands_sim.builder.robots import Scitosa5

import random
###############################################################################
# ROBOT
###############################################################################
robot = Scitosa5()

# tum_kitchen
robot.translate(x=2.5, y=3.2, z=0.0)
# sandbox
#robot.translate(1.0, 0.0, 0.0)

###############################################################################
# ACTUATORS
###############################################################################
ptu = PTU() # creates a new instance of the actuator
ptu.translate(0, 0, 1.585)
ptu.rotate(0, 0, 0)
ptu.add_interface('ros', topic='/ptu')
robot.append(ptu)

###############################################################################
# SENSORS
###############################################################################
ptu_pose = PTUPosture('ptu_pose')
ptu.append(ptu_pose)

kinect = DepthCamera() # Kinect() RVIZ crashes when kinect data is visualized!?
kinect.translate(0.04, -0.04, 0.065)
kinect.rotate(0, 0, 0)
ptu.append(kinect)
kinect.add_interface('ros', topic='/kinect')

# Semantic Camera
semanticcamera = SemanticCamera()
semanticcamera.translate(0.04, 0.04, 0.065)
semanticcamera.rotate(0.0, 0.4, 0.0)

ptu.append(semanticcamera)
semanticcamera.add_interface('ros', topic='/semcam')
#semanticcamera.add_interface('socket')

###############################################################################
# OBJECTS
###############################################################################
# cup on counter
cup1 = PassiveObject('/home/lars/work/devel/share/morse/data/props/kitchen_objects','Cup_Blue')
cup1.translate(x=random.uniform(3.1,3.5),
               y=random.uniform(-0.35,1.6),
               z=0.95)

# cup on workplace one
cup2 = PassiveObject('/home/lars/work/devel/share/morse/data/props/kitchen_objects','Cup_Gray')
cup2.translate(x=random.uniform(1.1,2.5),
               y=random.uniform(7.6,8.4),
               z=0.8)

# cup on workplace two 
cup3 = PassiveObject('/home/lars/work/devel/share/morse/data/props/kitchen_objects','Cup_Ocher')
cup3.translate(x=random.uniform(4.5,5.9),
               y=random.uniform(7.6,8.4),
               z=0.8)

###############################################################################    
# ENVIRONMENT
###############################################################################
env = Environment('tum_kitchen/tum_kitchen')
env.aim_camera([1.0470, 0, 0.7854])
