#! /usr/bin/env morseexec

"""
Brings in the CS building simulation environment from bham and uses ScitosA5.
"""

import sys
import subprocess 
import os
import random

from morse.builder import *
from strands_sim.builder.robots import Scitosa5
#from bham.builder.robots import Elevator
from g4s.add_objects import AddObjects

#robot = Scitosa5()
robot = Scitosa5(with_cameras = Scitosa5.WITH_OPENNI)
robot.translate(x=15, y=-2.1, z=0.1)
robot.rotate(z=3.14)

docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
docking_station.properties(Object = True)
docking_station.properties(ChargingZone = True)
docking_station.translate(14,-2.1,0.335)
docking_station.rotate(0,0,-3.14)

docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
docking_station_label.properties(Object = True)
docking_station_label.translate(13.95,-2.1,1.75)
docking_station_label.rotate(1.57,0,1.57)

AddObjects.add_desk_divider()
AddObjects.add_right_table()
AddObjects.add_left_table()
AddObjects.add_shelf()
AddObjects.add_tall_shelf()

# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/g4s.blend')
env = Environment(model_file,fastmode=False)

#env.place_camera([20.0, -10.0, 15.0])
#env.aim_camera([1.05, 0, 0.78])
env.place_camera([2, -1.0, 30.0])
env.aim_camera([0, 0, 0.00])
