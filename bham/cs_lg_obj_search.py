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
from bham.builder.robots import Elevator
from bham.add_objects import AddObjects

robot = Scitosa5()
#robot = Scitosa5(with_cameras = Scitosa5.WITHOUT_DEPTHCAMS)
robot.translate(x=3.75,y=-4.1, z=1.5)
robot.rotate(z=-1.57)

lift = Elevator()
lift.translate(3.81419,2.51356,0)

# At lowest level, the lift is controlled through a socket interface
# by lift_controller.py, which in turn provides a ros interface...
lift.add_default_interface('socket')

docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
docking_station.properties(Object = True)
docking_station.properties(ChargingZone = True)
docking_station.translate(3.75,-4.375,0.335)
docking_station.rotate(0,0,-1.57)

docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
docking_station_label.properties(Object = True)
docking_station_label.translate(3.75,-4.475,1.75)
docking_station_label.rotate(1.57,0,3.14)

AddObjects.add_walls()
AddObjects.add_table()

## WEST WALL  
table1 = PassiveObject('environments/human_tut/tutorial_scene','Table')
table1.properties(Object = True, Type = 'Table')
table1.translate(x=6.4, y=-8.2, z=0.0)
table1.rotate(0,0,math.pi)
#
table2 = PassiveObject('environments/human_tut/tutorial_scene','Table')
table2.properties(Object = True, Type = 'Table')
table2.translate(x=6.4,y=-5.7,z=0.0)
table2.rotate(0,0,math.pi)
#
## SOUTH WALL
##### STRANDS WORKPLACE
table3 = PassiveObject('environments/human_tut/tutorial_scene','Table')
table3.properties(Object = True, Type = 'Table')
table3.translate(x=3.3, y=-5.175,z=0.0)
table3.rotate(0,0,math.pi*3/2)                 
####
table4 = PassiveObject('environments/human_tut/tutorial_scene','Table')
table4.properties(Object = True, Type = 'Table')
table4.translate(x=-1.0, y=-5.175, z=0.0)
table4.rotate(0,0,math.pi*3/2)                 
####
##### TABLE ISLAND
table5 = PassiveObject('environments/human_tut/tutorial_scene','Table')
table5.properties(Object = True, Type = 'Table')
table5.translate(x=-2,y=-7.5,z=0.0)
#####
table5b = PassiveObject('environments/human_tut/tutorial_scene','Table')
table5b.properties(Object = True, Type = 'Table')
table5b.translate(x=-3.225, y=-7.5,z=0.0)
table5b.rotate(0,0,math.pi)
####
##### NORTH WALL
####
table6 = PassiveObject('environments/human_tut/tutorial_scene','Table')
table6.properties(Object = True, Type = 'Table')
table6.translate(x=4.8,y=-9.8,z=0.0)
table6.rotate(0,0,math.pi/2)
####
table7 = PassiveObject('environments/human_tut/tutorial_scene','Table')
table7.properties(Object = True, Type = 'Table')
table7.translate(x=2.775,y=-9.8,z=0.0)
table7.rotate(0,0,math.pi/2)
####
table8 = PassiveObject('environments/human_tut/tutorial_scene','Table')
table8.properties(Object = True, Type = 'Table')
table8.translate(x=-1.0,y=-9.8,z=0.0)
table8.rotate(0,0,math.pi/2)
####

# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/cs_lg.blend')
env = Environment(model_file,fastmode=False)
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.05, 0, 0.78])

