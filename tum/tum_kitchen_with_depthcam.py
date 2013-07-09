#! /usr/bin/env morseexec
""" Basic MORSE simulation scene for <strands_sim> environment

Please note: For using the Kinect sensor, or any depth camera, Python 3.3 is required.

If you have problems with the installation please check out this answer:
https://sympa.laas.fr/sympa/arc/morse-users/2013-04/msg00015.html

"""
from morse.builder import *
from strands_sim.builder.robots import Scitosa5

import random
#######################b########################################################
# ROBOT
###############################################################################
robot = Scitosa5()

# tum_kitchen
robot.translate(x=2.5, y=3.2, z=0.0)
# sandbox
#robot.translate(1.0, 0.0, 0.0)


###############################################################################
# SENSORS
###############################################################################

# Battery discharging rate, in percent per seconds
# The battery state is published to /battery
robot.battery.properties(DischargingRate=1.0)

pose = Pose()
robot.append(pose)
pose.add_interface('ros', topic='/pose')

ptu_pose = PTUPosture('ptu_pose')
robot.ptu.append(ptu_pose)

depthcam = DepthCamera() # Kinect() RVIZ crashes when depthcam data is visualized!?
robot.ptu.append(depthcam)
#depthcam.translate(0.04, -0.04, 1.65)
depthcam.translate(0.04, -0.04, 0.065)
depthcam.rotate(0, 0, 0)
depthcam.add_interface('ros', topic='/depthcam')

# Semantic Camera
semanticcamera = SemanticCamera()
robot.ptu.append(semanticcamera)
#semanticcamera.translate(0.04, 0.04, 1.65)
semanticcamera.translate(0.04, 0.04, 0.065)
semanticcamera.rotate(0.0, 0.0, 0.0)
semanticcamera.add_interface('ros', topic='/semcam')

###############################################################################
# OBJECTS
###############################################################################
# cup on counter


# table = PassiveObject('environments/tum_kitchen/tum_kitchen','Desk.002')
# table.properties(Object = True)
# table.translate(x=random.uniform(2.0,2.0),
#                y=random.uniform(6.0,6.1),
#                z=0.0)
# table.rotate(z=0.7)


cup1 = PassiveObject('props/kitchen_objects','Cup_Blue')
cup1.properties(Object = True, Type = 'Cup')
cup1.translate(x=random.uniform(3.1,3.5),
               y=random.uniform(-0.35,1.6),
               z=0.95)


# cup on workplace one
cup2 = PassiveObject('props/kitchen_objects','Cup_Gray')
cup2.properties(Object = True, Type = 'Cup')
cup2.translate(x=random.uniform(1.1,2.5),
               y=random.uniform(7.6,8.4),
               z=0.8)

# cup on workplace two 
cup3 = PassiveObject('props/kitchen_objects','Cup_Ocher')
cup3.properties(Object = True, Type = 'Cup')
cup3.translate(x=random.uniform(4.5,5.9),
               y=random.uniform(7.6,8.4),
               z=0.8)

###############################################################################    
# ENVIRONMENT
###############################################################################
env = Environment('tum_kitchen/tum_kitchen')
env.aim_camera([1.0470, 0, 0.7854])
