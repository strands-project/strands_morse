#! /usr/bin/env morseexec
from morse.builder import *
from bham_cs_sim.builder.robots import Elevator
import os

b21 = B21()

motion=MotionVW()
motion.translate(z=0.3,x=-3.3)
b21.append(motion)
b21.translate(x=-3.3)


# An odometry sensor to get odometry information
odometry = Odometry()
b21.append(odometry)
odometry.frequency(10)
odometry.add_interface('ros', topic="/odom",child_frame_id="/base_link")

# Append a sick laser
sick = Sick()
#sick.properties(resolution = 5)
#sick.properties(scan_window = 90)
sick.properties(Visible_arc = True)
sick.properties(laser_range = 30.0)
sick.translate(z=0.4)
b21.append(sick)
sick.add_stream('ros',topic="/scan",frame_id="/laser")

pose = Pose()
pose.translate(z=0.83,x=-3.3)
b21.append(pose)

pose.add_stream('ros')
motion.add_stream('ros',topic="/b21/cmd_vel")

lift = Elevator()
lift.translate(-5.05, 7.9, -6.04)

# At lowest level, the lift is controlled through a socket interface
# by lift_controller.py, which in turn provides a ros interface...
lift.add_default_interface('socket')

model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/CS_Building.blend')
env = Environment(model_file, fastmode = False)
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.05, 0, 0.78])
