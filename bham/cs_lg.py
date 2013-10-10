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
robot.battery.properties(DischargingRate=0.01)

robot.translate(x=1, y=-6.50, z=1.5)
#robot.translate(x=-1.35, y=0.56, z=7.5)
robot.rotate(z=1.57)

lift = Elevator()
lift.translate(3.81419,2.51356,0)

# At lowest level, the lift is controlled through a socket interface
# by lift_controller.py, which in turn provides a ros interface...
lift.add_default_interface('socket')

docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
docking_station.properties(Object = True)
docking_station.properties(ChargingZone = True)
docking_station.translate(1,-4.65,0.335)
docking_station.rotate(0,0,1.57)

docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
docking_station_label.properties(Object = True)
docking_station_label.translate(1,-4.55,1.75)
docking_station_label.rotate(1.57,0,0)

table = PassiveObject('environments/human_tut/tutorial_scene','Table')
table.properties(Object = True, Type = 'Table')
table.translate(x=random.uniform(-2.7,-2.7),
                y=random.uniform(-6.5,-6.5),
                z=0.0)
#table.rotate(0,0,math.pi/2)



book = dict()
bottle = dict()
calculator = dict()
cup = dict()
glass = dict()
headphone = dict()
holepunch = dict()
keyboard = dict()
keys = dict()
lamp = dict()
laptop = dict()
mobilephone = dict()
monitor = dict()
mouse = dict()
pencil = dict()
pc = dict()
stapler = dict()
telephone = dict()

for i in range(6):

    book[i] = PassiveObject('props/strands_objects','book')
    book[i].properties(Object = True, Type = 'Book')
    book[i].translate(x=0,y=0,z=1.0)
    
    bottle[i] = PassiveObject('props/strands_objects','bottle')
    bottle[i].properties(Object = True, Type = 'Bottle')
    bottle[i].translate(x=0,y=0,z=1.0)

    calculator[i] = PassiveObject('props/strands_objects','calculator')
    calculator[i].properties(Object = True, Type = 'Calculator')
    calculator[i].translate(x=0,y=0,z=1.0)

    cup[i] = PassiveObject('props/strands_objects','cup')
    cup[i].properties(Object = True, Type = 'Cup')
    cup[i].translate(0,0,1.0)
    
    glass[i] = PassiveObject('props/strands_objects','glass')
    glass[i].properties(Object = True, Type = 'Glass')
    glass[i].translate(x=0,y=0,z=1.0)
    
    headphone[i] = PassiveObject('props/strands_objects','headphone')
    headphone[i].properties(Object = True, Type = 'Headphone')
    headphone[i].translate(0, 0,1.0)

    holepunch[i] = PassiveObject('props/strands_objects','holepunch')
    holepunch[i].properties(Object = True, Type = 'HolePunch')
    holepunch[i].translate(x=0,y=0,z=1.0)

    keyboard[i] = PassiveObject('props/strands_objects','keyboard')
    keyboard[i].properties(Object = True, Type = 'Keyboard')
    keyboard[i].translate(x=0,y=0,z=1.0)

    keys[i] = PassiveObject('props/strands_objects','keys')
    keys[i].properties(Object = True, Type = 'Keys')
    keys[i].translate(0,0,1.0)

    laptop[i] = PassiveObject('props/strands_objects','laptop')
    laptop[i].properties(Object = True, Type = 'Laptop')
    laptop[i].translate(x=0,y=0,z=1.0)
    
    lamp[i] = PassiveObject('props/strands_objects','lamp')
    lamp[i].properties(Object = True, Type = 'Lamp')
    lamp[i].translate(0, 0,1.0)

    mobilephone[i] = PassiveObject('props/strands_objects','mobilephone')
    mobilephone[i].properties(Object = True, Type = 'MobilePhone')
    mobilephone[i].translate(x=0,y=0,z=1.0)
    
    monitor[i] = PassiveObject('props/strands_objects','monitor')
    monitor[i].properties(Object = True, Type = 'Monitor')
    monitor[i].translate(x=0,y=0,z=1.0)
    
    mouse[i] = PassiveObject('props/strands_objects','mouse')
    mouse[i].properties(Object = True, Type = 'Mouse')
    mouse[i].translate(x=0,y=0,z=1.0)
    
    pencil[i] = PassiveObject('props/strands_objects','pencil')
    pencil[i].properties(Object = True, Type = 'Pencil')
    pencil[i].translate(x=0,y=0,z=1.0)
    
    pc[i] = PassiveObject('props/strands_objects','pc')
    pc[i].properties(Object = True, Type = 'PC')
    pc[i].translate(0,0,1.0)
    
    stapler[i] = PassiveObject('props/strands_objects','stapler')
    stapler[i].properties(Object = True, Type = 'Stapler')
    stapler[i].translate(0, 0,1.0)

    telephone[i] = PassiveObject('props/strands_objects','telephone')
    telephone[i].properties(Object = True, Type = 'Telephone')
    telephone[i].translate(x=0,y=0,z=1.0)


#AddObjects.add_walls()
#AddObjects.add_table()


# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/cs_lg.blend')
env = Environment(model_file,fastmode=False)
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.05, 0, 0.78])

