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

robot = Scitosa5(with_cameras = Scitosa5.WITH_OPENNI)
#robot = Scitosa5(with_cameras = Scitosa5.WITHOUT_DEPTHCAMS)
robot.translate(x=0.0,y=0.0, z=0.0)
robot.rotate(z=-1.57)

docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
docking_station.properties(Object = True)
docking_station.properties(ChargingZone = True)
docking_station.translate(0.875,-4.375,0.230)
docking_station.rotate(0,0,0.0)

docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
docking_station_label.properties(Object = True)
docking_station_label.translate(0.95,-4.475,1.745)
docking_station_label.rotate(1.57,0,-1.57)

# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/floorsix.blend')
env = Environment(model_file,fastmode=False)
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.05, 0, 0.78])

