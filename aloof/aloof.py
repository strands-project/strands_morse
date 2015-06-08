#! /usr/bin/env morseexec

"""
Simple environemnt with ScitosA5.
"""

import sys
import subprocess
import os
import random

from morse.builder import *
from strands_sim.builder.robots import Scitosa5
#from bham.builder.robots import Elevator

monitor_table_top = 1.15 #higher value: higher off the table, default: 2
object_table_top = 0.95 #higher value: higher off the table, default: 2

#robot = Scitosa5()
robot = Scitosa5(with_cameras = Scitosa5.WITH_OPENNI)
robot.translate(x=3.3,y=-9,z=0.0)
robot.rotate(z=3.14)

docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
docking_station.properties(Object = True)
docking_station.properties(ChargingZone = True)
docking_station.translate(8,-4.12,0.335)
docking_station.rotate(0,0,1.57)

docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
docking_station_label.properties(Object = True)
docking_station_label.translate(8,-4.02,1.75)
docking_station_label.rotate(1.57,0,0)

## WEST WALL
table1 = PassiveObject('environments/human_tut/tutorial_scene','Table')
table1.properties(Object = True, Type = 'Table')
table1.translate(x=0.7, y=-3, z=0.0)
table1.rotate(0,0,math.pi)

table2 = PassiveObject('environments/human_tut/tutorial_scene','Table')
table2.properties(Object = True, Type = 'Table')
table2.translate(x=0.7,y=-9.0,z=0.0)
table2.rotate(0,0,math.pi)




###### OBJECTS ON WEST TABLE

west_monitor = PassiveObject('strands_sim/robots/strands_objects.blend','monitor')
west_monitor.properties(Object = True, Type = 'monitor')
west_monitor.translate(x=0.7,y=-9,z=monitor_table_top)
west_monitor.rotate(0,0,0)

west_keyboard = PassiveObject('strands_sim/robots/strands_objects.blend','keyboard')
west_keyboard.properties(Object = True, Type = 'keyboard')
west_keyboard.translate(x=1.0,y=-9,z=object_table_top)
west_keyboard.rotate(0,0,0)

west_mouse = PassiveObject('strands_sim/robots/strands_objects.blend','mouse')
west_mouse.properties(Object = True, Type = 'mouse')
west_mouse.translate(x=1.2,y=-9.5,z=object_table_top)
west_mouse.rotate(0,0,0)

west_mug = PassiveObject('strands_sim/robots/strands_objects.blend','cup')
west_mug.properties(Object = True, Type = 'cup')
west_mug.translate(x=1.2,y=-8.5,z=object_table_top)
west_mug.rotate(0,0,0)





## SOUTH WALL
table3 = PassiveObject('environments/human_tut/tutorial_scene','Table')
table3.properties(Object = True, Type = 'Table')
table3.translate(x=10.0, y=-11.3,z=0.0)
table3.rotate(0,0,math.pi*3/2)

## NORTH WALL
table4 = PassiveObject('environments/human_tut/tutorial_scene','Table')
table4.properties(Object = True, Type = 'Table')
table4.translate(x=10.0,y=-0.7,z=0.0)
table4.rotate(0,0,math.pi/2)

# EAST WALL
table5 = PassiveObject('environments/human_tut/tutorial_scene','Table')
table5.properties(Object = True, Type = 'Table')
table5.translate(x=19.3,y=-3.0,z=0.0)

table6 = PassiveObject('environments/human_tut/tutorial_scene','Table')
table6.properties(Object = True, Type = 'Table')
table6.translate(x=19.3,y=-9.0,z=0.0)

# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/aloof.blend')
env = Environment(model_file,fastmode=False)
env.place_camera([10, -6.0, 15.0])
env.aim_camera([0, 0, 0.00])
