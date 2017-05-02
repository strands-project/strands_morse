#! /usr/bin/env morseexec

import sys
import subprocess 
import os
import random

from morse.builder import *
from strands_sim.builder.robots import Scitosa5

#robot = Scitosa5()
robot = Scitosa5(with_cameras = Scitosa5.WITHOUT_DEPTHCAMS)
robot.translate(x=2,y=2, z=0)
robot.rotate(z=-1.57)

# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'maps/basic_map.blend')
env = Environment(model_file,fastmode=False)
env.place_camera([0, 0, 20])
env.aim_camera([0.5, 0, -0.5])
