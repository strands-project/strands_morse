#! /usr/bin/env morseexec

"""
Brings in the CS building simulation environment from bham and uses ScitosA5.
"""

import sys
import subprocess 
import os

# Add the bham to the python path and to MORSE_RESOURCE_PATH

from morse.builder import *
from strands_sim.builder.robots import Scitosa5
from bham.builder.robots import Elevator

robot = Scitosa5()
robot.translate(x=-3.3, y=3.2, z=0.0)

lift = Elevator()
lift.translate(-5.05, 7.9, -6.04)

# At lowest level, the lift is controlled through a socket interface
# by lift_controller.py, which in turn provides a ros interface...
lift.add_default_interface('socket')


# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/cs_common_room.blend')
env = Environment(model_file,fastmode=False)
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.05, 0, 0.78])

