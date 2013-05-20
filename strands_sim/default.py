#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <strands_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from strands_sim.builder.robots import Scitosa5

#robot = Ranger()
robot = Scitosa5()

# The list of the main methods to manipulate your components
# is here: http://www.openrobots.org/morse/doc/stable/user/builder_overview.html
robot.add_interface('ros')

# tum_kitchen
robot.translate(x=2.5, y=3.2, z=0.0)
# sandbox
#robot.translate(1.0, 0.0, 0.0)

odometry = Odometry()
robot.append(odometry)
odometry.add_interface('ros', topic="/odom")

scan = Hokuyo()
#scan.translate(x=0.275, z=0.252)
#scan.translate(x=0.65, z=-0.60)
scan.translate(x=0.30, z=0.386)
robot.append(scan)
scan.properties(Visible_arc = False)
scan.properties(laser_range = 30.0)
scan.properties(resolution = 1.0)
scan.properties(scan_window = 180.0)
scan.create_laser_arc()

scan.add_interface('ros', topic='/scan')

# Keyboard control
keyboard = Keyboard()
robot.append(keyboard)

motion = MotionXYW()
robot.append(motion)
motion.add_interface('ros', topic='/cmd_vel')

# Set the environment
env = Environment('tum_kitchen/tum_kitchen')
env.aim_camera([1.0470, 0, 0.7854])
