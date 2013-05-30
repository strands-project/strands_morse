#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <strands_sim> environment

Please note: For using the Kinect sensor, or any depth camera, Python 3.3 is required.

If you have problems with the installation please check out this answer:
https://sympa.laas.fr/sympa/arc/morse-users/2013-04/msg00015.html

"""

from morse.builder import *
from strands_sim.builder.robots import Scitosa5

#robot = Ranger()
robot = Scitosa5()

# tum_kitchen
robot.translate(x=2.5, y=3.2, z=0.0)
# sandbox
#robot.translate(1.0, 0.0, 0.0)

ptu = PTU() # creates a new instance of the actuator
ptu.translate(0, 0, 1.585)
ptu.rotate(0, 0, 0)
ptu.add_interface('ros', topic='/ptu')
robot.append(ptu)

ptu_pose = PTUPosture('ptu_pose')
ptu.append(ptu_pose)

kinect = DepthCamera() # Kinect()
kinect.translate(0, 0, 0.055)
kinect.rotate(0, 0, 0)
ptu.append(kinect)
kinect.add_interface('ros', topic='/kinect')

# Set the environment
env = Environment('tum_kitchen/tum_kitchen')
env.aim_camera([1.0470, 0, 0.7854])
