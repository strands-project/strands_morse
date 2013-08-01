#! /usr/bin/env morseexec

"""
Brings in the CS building simulation environment from bham and uses ScitosA5.
"""

import sys
import subprocess 
import os

from morse.builder import *
from strands_sim.builder.robots import Scitosa5
from bham.builder.robots import Elevator


robot = Scitosa5()
#robot = Scitosa5(with_cameras = Scitosa5.WITHOUT_DEPTHCAMS)

robot.translate(x=1, y=-6.50, z=1.5)
#robot.translate(x=-1.35, y=0.56, z=7.5)
robot.rotate(z=1.57)

lift = Elevator()
lift.translate(3.81419,2.51356,0)

# At lowest level, the lift is controlled through a socket interface
# by lift_controller.py, which in turn provides a ros interface...
lift.add_default_interface('socket')

docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
docking_station.properties(ChargingZone = True)
docking_station.translate(1,-4.65,0.335)
docking_station.rotate(0,0,1.57)

docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
docking_station_label.translate(1,-4.55,1.8)
docking_station_label.rotate(1.57,0,0)

# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/cs_lg.blend')
env = Environment(model_file,fastmode=False)
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.05, 0, 0.78])

