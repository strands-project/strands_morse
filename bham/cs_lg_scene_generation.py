#! /usr/bin/env morseexec

"""
Brings in the CS building simulation environment from bham and uses ScitosA5.
"""

import sys
import subprocess 
import os
import random
import math

from morse.builder import *
from strands_sim.builder.robots import Scitosa5
#from bham.builder.robots import Elevator
from bham.add_objects import AddObjects


robot = Scitosa5()
#robot = Scitosa5(with_cameras = Scitosa5.WITHOUT_DEPTHCAMS)
#robot.battery.properties(DischargingRate=0.01)

robot.translate(x=1, y=-6.50, z=1.5)
#robot.translate(x=-1.35, y=0.56, z=7.5)
robot.rotate(z=1.57)

#lift = Elevator()
#lift.translate(3.81419,2.51356,0)

# At lowest level, the lift is controlled through a socket interface
# by lift_controller.py, which in turn provides a ros interface...
#lift.add_default_interface('socket')

docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
docking_station.properties(Object = True)
docking_station.properties(ChargingZone = True)
docking_station.translate(1,-4.65,0.335)
docking_station.rotate(0,0,1.57)

docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
docking_station_label.properties(Object = True)
docking_station_label.translate(1,-4.55,1.75)
docking_station_label.rotate(1.57,0,0)

#table = PassiveObject('environments/human_tut/tutorial_scene','Table')
#table.properties(Object = True, Type = 'Table')
#table.translate(x=-4.7,
#                y=-7.5,
#                z=0.0)
#table.translate(x=random.uniform(-4.7,-4.7),
#                y=random.uniform(-6.5,-6.5),
#                z=0.0)


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
###table5b = PassiveObject('environments/human_tut/tutorial_scene','Table')
###table5b.properties(Object = True, Type = 'Table')
###table5b.translate(x=-3.225, y=-7.5,z=0.0)
###table5b.rotate(0,0,math.pi)
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
#
##table.rotate(0,0,math.pi/2)
#
## for i in range(1):
#
##     human = Human() # create human 'robot'
##     human.translate(random.uniform(-5, 5), random.uniform(-5, 5))
##     #human.disable_keyboard_control()
##     human.use_world_camera()
#
##     waypoint = Waypoint() # create actuator
##     waypoint.add_interface('socket') # control via sockets
##     human.append(waypoint)
#

book = dict()
bottle = dict()
####calculator = dict()
cup = dict()
####glass = dict()
####headphone = dict()
####holepunch = dict()
keyboard = dict()
####keys = dict()
####lamp = dict()
laptop = dict()
####mobilephone = dict()
monitor = dict()
mouse = dict()
####pencil = dict()
pc = dict()
####stapler = dict()
telephone = dict()
###
for i in range(6):
###
   book[i] = PassiveObject('strands_sim/robots/strands_objects.blend','book')
   book[i].properties(Object = True, Type = 'Book')
   book[i].translate(x=0,y=0,z=1.0)
###   
   bottle[i] = PassiveObject('strands_sim/robots/strands_objects.blend','bottle')
   bottle[i].properties(Object = True, Type = 'Bottle')
   bottle[i].translate(x=0,y=0,z=1.0)
###
###   #calculator[i] = PassiveObject('strands_sim/robots/strands_objects.blend','calculator')
###   #calculator[i].properties(Object = True, Type = 'Calculator')
###   #calculator[i].translate(x=0,y=0,z=1.0)
###
   cup[i] = PassiveObject('strands_sim/robots/strands_objects.blend','cup')
   cup[i].properties(Object = True, Type = 'Cup')
   cup[i].translate(0,0,1.0)
###   
###   #glass[i] = PassiveObject('strands_sim/robots/strands_objects.blend','glass')
###   #glass[i].properties(Object = True, Type = 'Glass')
###   #glass[i].translate(x=0,y=0,z=1.0)
###   
###   #headphone[i] = PassiveObject('strands_sim/robots/strands_objects.blend','headphone')
###   #headphone[i].properties(Object = True, Type = 'Headphone')
###   #headphone[i].translate(0, 0,1.0)
###
###   #holepunch[i] = PassiveObject('strands_sim/robots/strands_objects.blend','holepunch')
###   #holepunch[i].properties(Object = True, Type = 'HolePunch')
###   #holepunch[i].translate(x=0,y=0,z=1.0)
###
   keyboard[i] = PassiveObject('strands_sim/robots/strands_objects.blend','keyboard')
   keyboard[i].properties(Object = True, Type = 'Keyboard')
   keyboard[i].translate(x=0,y=0,z=1.0)
###
###   #keys[i] = PassiveObject('strands_sim/robots/strands_objects.blend','keys')
###   #keys[i].properties(Object = True, Type = 'Keys')
###   #keys[i].translate(0,0,1.0)
###
   laptop[i] = PassiveObject('strands_sim/robots/strands_objects.blend','laptop')
   laptop[i].properties(Object = True, Type = 'Laptop')
   laptop[i].translate(x=0,y=0,z=1.0)
###   
###   #lamp[i] = PassiveObject('strands_sim/robots/strands_objects.blend','lamp')
###   #lamp[i].properties(Object = True, Type = 'Lamp')
###   #lamp[i].translate(0, 0,1.0)
###
###   #mobilephone[i] = PassiveObject('strands_sim/robots/strands_objects.blend','mobilephone')
###   #mobilephone[i].properties(Object = True, Type = 'MobilePhone')
###   #mobilephone[i].translate(x=0,y=0,z=1.0)
###   
   monitor[i] = PassiveObject('strands_sim/robots/strands_objects.blend','monitor')
   monitor[i].properties(Object = True, Type = 'Monitor')
   monitor[i].translate(x=0,y=0,z=1.0)
###   
   mouse[i] = PassiveObject('strands_sim/robots/strands_objects.blend','mouse')
   mouse[i].properties(Object = True, Type = 'Mouse')
   mouse[i].translate(x=0,y=0,z=1.0)
###   
###   #pencil[i] = PassiveObject('strands_sim/robots/strands_objects.blend','pencil')
###   #pencil[i].properties(Object = True, Type = 'Pencil')
###   #pencil[i].translate(x=0,y=0,z=1.0)
###   
   pc[i] = PassiveObject('strands_sim/robots/strands_objects.blend','pc')
   pc[i].properties(Object = True, Type = 'PC')
   pc[i].translate(0,0,1.0)
###   
###   #stapler[i] = PassiveObject('strands_sim/robots/strands_objects.blend','stapler')
###   #stapler[i].properties(Object = True, Type = 'Stapler')
###   #stapler[i].translate(0, 0,1.0)
###
   telephone[i] = PassiveObject('strands_sim/robots/strands_objects.blend','telephone')
   telephone[i].properties(Object = True, Type = 'Telephone')
   telephone[i].translate(x=0,y=0,z=1.0)
###

#AddObjects.add_walls()
#AddObjects.add_table()


# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/cs_lg.blend')
env = Environment(model_file,fastmode=False)
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.05, 0, 0.78])

