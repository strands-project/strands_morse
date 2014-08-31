#! /usr/bin/env morseexec

"""
Brings in the KTH floor six simulation environment and uses ScitosA5.
"""

import sys
import subprocess 
import os
import random

from morse.builder import *
from strands_sim.builder.robots import Scitosa5

#robot = Scitosa5(with_cameras = Scitosa5.WITH_OPENNI)
robot = Scitosa5(with_cameras = Scitosa5.WITHOUT_DEPTHCAMS)
robot.translate(x=0.6,y=-3.375, z=0.0)

docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
docking_station.properties(Object = True)
docking_station.properties(ChargingZone = True)
docking_station.translate(0.875,-3.375,0.230)
docking_station.rotate(0,0,0.0)

docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
docking_station_label.properties(Object = True)
docking_station_label.translate(0.95,-3.375,1.745)
docking_station_label.rotate(1.57,0,-1.57)

# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/floorsix.blend')
env = Environment(model_file,fastmode=False)
env.place_camera([0.0, -10.0, 10.0])
env.aim_camera([0.8, 0, 0.0])

